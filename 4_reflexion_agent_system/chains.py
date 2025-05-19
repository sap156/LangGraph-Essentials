# Import necessary libraries for creating prompts and interacting with the LLM
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import datetime
from langchain_openai import ChatOpenAI
from schema import AnswerQuestion, ReviseAnswer
from langchain_core.output_parsers.openai_tools import PydanticToolsParser, JsonOutputToolsParser
from langchain_core.messages import HumanMessage

# Initialize parsers for handling structured outputs
pydantic_parser = PydanticToolsParser(tools=[AnswerQuestion])  # Parses outputs into Pydantic models
parser = JsonOutputToolsParser(return_id=True)  # Parses outputs into JSON format with IDs

# Define the actor agent's prompt template
# This prompt guides the LLM to provide detailed answers, critique them, and suggest search queries
actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert AI researcher.
Current time: {time}

1. {first_instruction}
2. Reflect and critique your answer. Be severe to maximize improvement.
3. After the reflection, **list 1-3 search queries separately** for researching improvements. Do not include them inside the reflection.
""",
        ),
        MessagesPlaceholder(variable_name="messages"),  # Placeholder for conversation history
        ("system", "Answer the user's question above using the required format."),
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),  # Dynamically inject the current time
)

# Define the first responder's prompt template
# This template instructs the LLM to provide a detailed ~250-word answer
first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction="Provide a detailed ~250 word answer"
)

# Initialize the LLM with GPT-4o
llm = ChatOpenAI(model="gpt-4o")

# Create the first responder chain
# This chain uses the first responder prompt and binds the AnswerQuestion tool
first_responder_chain = first_responder_prompt_template | llm.bind_tools(tools=[AnswerQuestion], tool_choice='AnswerQuestion') 

# Validator for parsing and validating outputs
validator = PydanticToolsParser(tools=[AnswerQuestion])

# Define the revisor's instructions
# These instructions guide the LLM to revise its previous answer based on critique and new information
revise_instructions = """Revise your previous answer using the new information.
    - You should use the previous critique to add important information to your answer.
        - You MUST include numerical citations in your revised answer to ensure it can be verified.
        - Add a "References" section to the bottom of your answer (which does not count towards the word limit). In form of:
            - [1] https://example.com
            - [2] https://example.com
    - You should use the previous critique to remove superfluous information from your answer and make SURE it is not more than 250 words.
"""

# Create the revisor chain
# This chain uses the revisor instructions and binds the ReviseAnswer tool
revisor_chain = actor_prompt_template.partial(
    first_instruction=revise_instructions
) | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")

# Uncomment the following lines to test the first responder chain
# response = first_responder_chain.invoke({
#     "messages": [HumanMessage("AI Agents taking over content creation")]
# })

# print(response)


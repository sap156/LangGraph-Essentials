# Import necessary components from LangChain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # Core prompt components
#from langchain_google_genai import ChatGoogleGenerativeAI  # Optional: Google's AI model
from langchain_openai import ChatOpenAI  # OpenAI's chat model

# Define the generation prompt template
# This template is used to create Twitter posts
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
            " Generate the best twitter post possible for the user's request."
            " If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        # Placeholder for the conversation history
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Define the reflection prompt template
# This template is used to critique and improve generated tweets
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc.",
        ),
        # Placeholder for the messages to be critiqued
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Initialize the language model
# Using OpenAI's GPT-4o with temperature=0 for consistent outputs
llm = ChatOpenAI(model="gpt-4o")

# Create the chain pipelines
# generation_chain: prompt -> LLM -> response (creates tweets)
generation_chain = generation_prompt | llm
# reflection_chain: prompt -> LLM -> response (provides feedback)
reflection_chain = reflection_prompt | llm

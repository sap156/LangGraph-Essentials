# Import necessary libraries for creating a basic chatbot
from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the ChatGroq model with the specified version of LLaMA
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define the structure of the chat state using TypedDict
class BasicChatState(TypedDict):
    messages: Annotated[list, add_messages]

# Define the chatbot function that takes the current state as input
def chatbot(state: BasicChatState):
    # Generate a response by invoking the language model with the current messages
    return {
        "messages": [llm.invoke(state["messages"])]
    }

# Create a state graph for managing the chatbot's states and transitions
graph = StateGraph(BasicChatState)

# Add the chatbot node to the graph with the corresponding function
graph.add_node("chatbot", chatbot)
# Set the entry point of the graph to the chatbot node
graph.set_entry_point("chatbot")
# Add an edge from the chatbot node to the END node, indicating the end of the conversation
graph.add_edge("chatbot", END)

# Compile the graph into an application
app = graph.compile()

# Main loop for interacting with the user
while True: 
    # Get user input from the console
    user_input = input("User: ")
    # Check if the user wants to exit the chat
    if(user_input in ["exit", "end"]):
        break
    else: 
        # Invoke the compiled graph application with the user input
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        })

        # Print the result of the invocation, which should contain the AI's response
        print(result)

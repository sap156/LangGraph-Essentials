from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

# Import necessary libraries for creating a chatbot with SQLite checkpointing
# - `TypedDict` and `Annotated` from `typing`: To define the structure of the chatbot state.
# - `add_messages`, `StateGraph`, and `END` from `langgraph.graph`: To manage the state graph of the chatbot.
# - `ChatGroq` from `langchain_groq`: To use the Groq model for generating chatbot responses.
# - `HumanMessage` from `langchain_core.messages`: To structure the user input as a message.
# - `load_dotenv` from `dotenv`: To load environment variables from a `.env` file.
# - `SqliteSaver` from `langgraph.checkpoint.sqlite`: To enable SQLite checkpointing for the chatbot's memory.
# - `sqlite3`: To interact with the SQLite database.

load_dotenv()

# Establish a connection to the SQLite database for checkpointing.
# The database file is "checkpoint.sqlite" and the connection is set to allow
# sharing the same connection across multiple threads.
sqlite_conn = sqlite3.connect("checkpoint.sqlite", check_same_thread=False)

# Initialize the memory checkpointing system with the SQLite connection.
memory = SqliteSaver(sqlite_conn)

# Set up the chatbot model using the Groq framework with a specified LLaMA model.
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define the structure of the chatbot state using TypedDict.
# The state includes a list of messages, with the `add_messages` function
# from `langgraph.graph` applied to it.
class BasicChatState(TypedDict): 
    messages: Annotated[list, add_messages]

# Define the chatbot function, which generates a response based on the current state.
# It uses the LLaMA model to invoke a response, given the list of messages in the state.
def chatbot(state: BasicChatState): 
    return {
       "messages": [llm.invoke(state["messages"])]
    }

# Create a state graph for the chatbot using Langgraph.
graph = StateGraph(BasicChatState)

# Add the "chatbot" node to the graph, linking it to the `chatbot` function.
graph.add_node("chatbot", chatbot)

# Define the edges of the graph. Currently, it connects the "chatbot" node to the END node.
graph.add_edge("chatbot", END)

# Set the entry point of the graph to the "chatbot" node.
graph.set_entry_point("chatbot")

# Compile the graph into an application, with the SQLite memory checkpointing enabled.
app = graph.compile(checkpointer=memory)

# Configuration for the chatbot application, specifying a thread ID.
config = {"configurable": {
    "thread_id": 1
}}

# Main loop for interacting with the chatbot.
while True: 
    user_input = input("User: ")
    if(user_input in ["exit", "end"]):
        break
    else: 
        # Invoke the chatbot application with the user input, structured as a HumanMessage.
        # The config specifies the thread ID for the operation.
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        }, config=config)

        # Print the content of the AI's response, which is the last message in the result.
        print("AI: " + result["messages"][-1].content)


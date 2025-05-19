from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

# Import necessary libraries for creating a chatbot with in-memory checkpointing
# Add comments here to explain the use of in-memory checkpointing in the chatbot system

load_dotenv()

# Initialize the MemorySaver for in-memory checkpointing
memory = MemorySaver()

# Set up the language model
llm = ChatGroq(model="llama-3.1-8b-instant")

class BasicChatState(TypedDict): 
    messages: Annotated[list, add_messages]

def chatbot(state: BasicChatState): 
    return {
       "messages": [llm.invoke(state["messages"])]
    }

# Create a state graph for managing chatbot states
graph = StateGraph(BasicChatState)

# Add the chatbot node to the graph
graph.add_node("chatbot", chatbot)

# Define the end of the graph
graph.add_edge("chatbot", END)

# Set the entry point for the graph
graph.set_entry_point("chatbot")

# Compile the graph into an application with the memory checkpointer
app = graph.compile(checkpointer=memory)

config = {"configurable": {
    "thread_id": 1
}}

# Main loop for user interaction
while True: 
    user_input = input("User: ")
    if(user_input in ["exit", "end"]):
        break
    else: 
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        }, config=config)

        print("AI: " + result["messages"][-1].content)


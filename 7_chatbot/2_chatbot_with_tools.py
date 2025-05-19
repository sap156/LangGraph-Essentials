from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

# Import necessary libraries for creating a chatbot with tools
# Add comments here to explain the integration of tools in the chatbot system

load_dotenv()

class BasicChatBot(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize the search tool with a maximum of 2 results
search_tool = TavilySearchResults(max_results=2)
# List of tools to be used by the chatbot
tools = [search_tool]

# Initialize the language model
llm = ChatGroq(model="llama-3.1-8b-instant")

# Bind the tools to the language model
llm_with_tools = llm.bind_tools(tools=tools)

# Define the chatbot function
def chatbot(state: BasicChatBot):
    return {
        "messages": [llm_with_tools.invoke(state["messages"])], 
    }

# Define the router function for directing to tools or ending the conversation
def tools_router(state: BasicChatBot):
    last_message = state["messages"][-1]

    # Check if the last message has tool calls
    if(hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0):
        return "tool_node"
    else: 
        return END
    

# Create a tool node for managing tools in the graph
tool_node = ToolNode(tools=tools)

# Initialize the state graph for the chatbot
graph = StateGraph(BasicChatBot)

# Add nodes for the chatbot and tool management
graph.add_node("chatbot", chatbot)
graph.add_node("tool_node", tool_node)
# Set the entry point of the graph
graph.set_entry_point("chatbot")

# Add conditional edges for routing between chatbot and tools
graph.add_conditional_edges("chatbot", tools_router)
# Add an edge for the tool node to return to the chatbot
graph.add_edge("tool_node", "chatbot")

# Compile the graph into an application
app = graph.compile()

# Main loop for user interaction
while True: 
    user_input = input("User: ")
    # Exit the loop if the user types 'exit' or 'end'
    if(user_input in ["exit", "end"]):
        break
    else: 
        # Invoke the compiled app with the user input
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        })

        # Print the result from the chatbot
        print(result)






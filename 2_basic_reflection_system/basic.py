# Import required libraries
from typing import List, Sequence  # Type hints for list and sequence data structures
from dotenv import load_dotenv  # For loading environment variables
from langchain_core.messages import BaseMessage, HumanMessage  # Message types for LLM interaction
from langgraph.graph import END, MessageGraph  # Core components for building the graph
from chains import generation_chain, reflection_chain  # Custom chain implementations

# Load environment variables (API keys, etc.)
load_dotenv()

# Define constant names for graph nodes
REFLECT = "reflect"  # Node for reflection operations
GENERATE = "generate"  # Node for generation operations

# Initialize the message processing graph
graph = MessageGraph()

def generate_node(state): 
    """
    Generate new content based on the current state
    Args:
        state: Current conversation state/messages
    Returns:
        Generated response from the LLM
    """
    return generation_chain.invoke({
        "messages": state
    })

def reflect_node(messages):
    """
    Reflect on the current conversation and provide insights
    Args:
        messages: List of conversation messages
    Returns:
        List containing a single HumanMessage with reflection content
    """
    response = reflection_chain.invoke({
        "messages": messages
    })
    return [HumanMessage(content=response.content)]

# Add nodes to the graph for generation and reflection
graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)
# Set the initial entry point to the generation node
graph.set_entry_point(GENERATE)

def should_continue(state):
    """
    Determine if the conversation should continue or end
    Args:
        state: Current conversation state
    Returns:
        Either REFLECT to continue or END to terminate
    """
    # End conversation if more than 6 messages
    if (len(state) > 6):
        return END 
    return REFLECT

# Define the graph flow:
# 1. GENERATE node connects to should_continue decision function
graph.add_conditional_edges(GENERATE, should_continue)
# 2. REFLECT node always goes back to GENERATE
graph.add_edge(REFLECT, GENERATE)

# Compile the graph into an executable application
app = graph.compile()

# Visualize the graph structure
print(app.get_graph().draw_mermaid())  # Generate Mermaid diagram
app.get_graph().print_ascii()  # Print ASCII representation

# Run the graph with an initial prompt
response = app.invoke(HumanMessage(content="AI Agents taking over content creation"))

# Print the final response
print(response)


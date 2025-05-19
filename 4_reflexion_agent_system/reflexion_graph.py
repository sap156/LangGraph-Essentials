# Import necessary libraries for building the graph and handling messages
from typing import List
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import END, MessageGraph
from chains import revisor_chain, first_responder_chain
from execute_tools import execute_tools

# Initialize the message processing graph
# This graph orchestrates the flow of the reflexion agent system
graph = MessageGraph()
MAX_ITERATIONS = 2  # Define the maximum number of iterations for the event loop

# Add nodes to the graph
# Each node represents a step in the reflexion process
graph.add_node("draft", first_responder_chain)  # Node for generating the initial draft
graph.add_node("execute_tools", execute_tools)  # Node for executing search queries
graph.add_node("revisor", revisor_chain)  # Node for revising the draft

# Define the edges between nodes
# These edges represent the flow of data between steps
graph.add_edge("draft", "execute_tools")  # Draft -> Execute Tools
graph.add_edge("execute_tools", "revisor")  # Execute Tools -> Revisor

# Define the event loop logic
# This function determines whether to continue or end the process based on the number of iterations
def event_loop(state: List[BaseMessage]) -> str:
    """
    Event loop logic to control the flow of the graph.

    Args:
        state: List of messages representing the current conversation state.

    Returns:
        The next node to visit or END to terminate the process.
    """
    count_tool_visits = sum(isinstance(item, ToolMessage) for item in state)  # Count tool messages
    num_iterations = count_tool_visits  # Number of iterations is equal to tool visits
    if num_iterations > MAX_ITERATIONS:  # Terminate if iterations exceed the maximum
        return END
    return "execute_tools"  # Continue to the execute_tools node

# Add conditional edges to the graph
# The revisor node conditionally transitions to execute_tools or ends the process
graph.add_conditional_edges("revisor", event_loop)

# Set the entry point of the graph
# The process starts at the draft node
graph.set_entry_point("draft")

# Compile the graph into an executable application
app = graph.compile()

# Visualize the graph structure
# Generate a Mermaid diagram and print an ASCII representation
print(app.get_graph().draw_mermaid())

# Run the graph with an initial prompt
# This invokes the reflexion process with a user-provided question
response = app.invoke(
    "Write about how small business can leverage AI to grow"
)

# Print the final answer and the entire response
print(response[-1].tool_calls[0]["args"]["answer"])  # Print the final answer
print(response, "response")  # Print the entire response
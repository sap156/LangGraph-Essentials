# Import necessary libraries
from typing import TypedDict  # For defining structured state types
from langgraph.graph import END, StateGraph  # For creating and managing state graphs

# Define a simple state structure using TypedDict
# This state keeps track of a single integer count
class SimpleState(TypedDict):
    count: int

# Define a function to increment the count in the state
def increment(state: SimpleState) -> SimpleState: 
    """
    Increment the count in the state by 1.

    Args:
        state: The current state containing the count.

    Returns:
        A new state with the incremented count.
    """
    return {
        "count": state["count"] + 1
    }

# Define a function to decide whether to continue or stop the graph execution
def should_continue(state):
    """
    Determine if the graph should continue or stop based on the count.

    Args:
        state: The current state containing the count.

    Returns:
        "continue" if the count is less than 5, otherwise "stop".
    """
    if(state["count"] < 5): 
        return "continue"
    else: 
        return "stop"

# Initialize a state graph with the defined state structure
graph = StateGraph(SimpleState)

# Add a node to the graph for the increment function
graph.add_node("increment", increment)

# Set the entry point of the graph to the increment node
graph.set_entry_point("increment")

# Add conditional edges to the graph
# The graph transitions to "increment" if "continue" is returned, otherwise it stops
graph.add_conditional_edges(
    "increment", 
    should_continue, 
    {
        "continue": "increment", 
        "stop": END
    }
)

# Compile the graph into an executable application
app = graph.compile()

# Define the initial state
state = {
    "count": 0
}

# Invoke the graph with the initial state and print the result
result = app.invoke(state)
print(result)

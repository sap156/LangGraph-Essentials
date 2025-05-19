# Import necessary libraries
from typing import TypedDict, List, Annotated  # For defining structured state types and annotations
from langgraph.graph import END, StateGraph  # For creating and managing state graphs
import operator  # For defining operations on annotated fields

# Define a complex state structure using TypedDict
# This state includes a count, a sum (with addition operation), and a history (with concatenation operation)
class SimpleState(TypedDict):
    count: int
    sum: Annotated[int, operator.add]  # Annotated field for sum with addition operation
    history: Annotated[List[int], operator.concat]  # Annotated field for history with concatenation operation

# Define a function to increment the count in the state
def increment(state: SimpleState) -> SimpleState: 
    """
    Increment the count in the state by 1 and update the sum and history.

    Args:
        state: The current state containing the count, sum, and history.

    Returns:
        A new state with the updated count, sum, and history.
    """
    new_count = state["count"] + 1

    return {
        "count": new_count, 
        "sum": new_count,  # Update the sum with the new count
        "history": [new_count]  # Append the new count to the history
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
    "count": 0, 
    "sum": 0, 
    "history": []
}

# Invoke the graph with the initial state and print the result
result = app.invoke(state)
print(result)

from dotenv import load_dotenv

load_dotenv()

from langchain_core.agents import AgentFinish, AgentAction
from langgraph.graph import END, StateGraph

from nodes import reason_node, act_node
from react_state import AgentState

# Import necessary libraries for building the graph structure of the ReAct agent system
# Add comments here to explain the graph structure, nodes, and transitions

REASON_NODE = "reason_node"
ACT_NODE = "act_node"

def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    else:
        return ACT_NODE


graph = StateGraph(AgentState)

# Add nodes to the graph
graph.add_node(REASON_NODE, reason_node)
graph.set_entry_point(REASON_NODE)
graph.add_node(ACT_NODE, act_node)

# Define the transitions between nodes
graph.add_conditional_edges(
    REASON_NODE,
    should_continue,
)

# Add a bidirectional edge between ACT_NODE and REASON_NODE for back-and-forth transitions
graph.add_edge(ACT_NODE, REASON_NODE)

# Compile the graph into an application
app = graph.compile()

# Invoke the application with an initial input
result = app.invoke(
    {
        "input": "How many days ago was the latest SpaceX launch?", 
        "agent_outcome": None, 
        "intermediate_steps": []
    }
)

# Print the final result of the agent's reasoning
print(result["agent_outcome"].return_values["output"], "final result")


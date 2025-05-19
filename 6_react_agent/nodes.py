from dotenv import load_dotenv

from agent_reason_runnable import react_agent_runnable, tools
from react_state import AgentState

load_dotenv()

# The reason_node function is responsible for invoking the React agent's reasoning process.
# It takes the current state of the agent as input, calls the react_agent_runnable with this state,
# and returns the outcome of the agent's reasoning.
def reason_node(state: AgentState):
    agent_outcome = react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}


# The act_node function executes the action determined by the React agent.
# It extracts the agent's action from the state, identifies the corresponding tool,
# and invokes the tool with the provided input. The function returns the intermediate steps
# including the agent's action and the tool's output.
def act_node(state: AgentState):
    agent_action = state["agent_outcome"]
    
    # Extract tool name and input from AgentAction
    tool_name = agent_action.tool
    tool_input = agent_action.tool_input
    
    # Find the matching tool function
    tool_function = None
    for tool in tools:
        if tool.name == tool_name:
            tool_function = tool
            break
    
    # Execute the tool with the input
    if tool_function:
        if isinstance(tool_input, dict):
            output = tool_function.invoke(**tool_input)
        else:
            output = tool_function.invoke(tool_input)
    else:
        output = f"Tool '{tool_name}' not found"
    
    return {"intermediate_steps": [(agent_action, str(output))]}
# Import necessary libraries for handling messages and executing tools
import json
from typing import List, Dict, Any
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage, HumanMessage
from langchain_community.tools import TavilySearchResults

# Create the Tavily search tool
# This tool is used to perform web searches and retrieve results
# max_results specifies the maximum number of search results to return
tavily_tool = TavilySearchResults(max_results=5)

# Function to execute search queries from AnswerQuestion tool calls
def execute_tools(state: List[BaseMessage]) -> List[BaseMessage]:
    """
    Executes search queries extracted from tool calls in the AI message.

    Args:
        state: List of messages representing the current conversation state.

    Returns:
        List of ToolMessage objects containing the search results.
    """
    # Get the last AI message from the conversation state
    last_ai_message: AIMessage = state[-1]
    
    # Check if the AI message contains tool calls
    if not hasattr(last_ai_message, "tool_calls") or not last_ai_message.tool_calls:
        return []
    
    # Initialize a list to store tool messages
    tool_messages = []
    
    # Process each tool call in the AI message
    for tool_call in last_ai_message.tool_calls:
        if tool_call["name"] in ["AnswerQuestion", "ReviseAnswer"]:
            call_id = tool_call["id"]  # Extract the tool call ID
            search_queries = tool_call["args"].get("search_queries", [])  # Extract search queries
            
            # Execute each search query using the Tavily tool
            query_results = {}
            for query in search_queries:
                result = tavily_tool.invoke(query)  # Perform the search
                query_results[query] = result  # Store the results
            
            # Create a ToolMessage with the search results
            tool_messages.append(
                ToolMessage(
                    content=json.dumps(query_results),  # Serialize results as JSON
                    tool_call_id=call_id  # Associate the results with the tool call ID
                )
            )
    
    return tool_messages  # Return the list of ToolMessage objects

# Example usage
# test_state represents a sample conversation state with a tool call
test_state = [
    HumanMessage(
        content="Write about how small business can leverage AI to grow"
    ),
    AIMessage(
        content="", 
        tool_calls=[
            {
                "name": "AnswerQuestion",
                "args": {
                    'answer': '', 
                    'search_queries': [
                            'AI tools for small business', 
                            'AI in small business marketing', 
                            'AI automation for small business'
                    ], 
                    'reflection': {
                        'missing': '', 
                        'superfluous': ''
                    }
                },
                "id": "call_KpYHichFFEmLitHFvFhKy1Ra",
            }
        ],
    )
]

# Uncomment the following lines to test the execute_tools function
# results = execute_tools(test_state)

# print("Raw results:", results)
# if results:
#     parsed_content = json.loads(results[0].content)
#     print("Parsed content:", parsed_content)
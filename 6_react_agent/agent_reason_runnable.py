# Import necessary libraries for creating a ReAct agent
from langchain_openai import ChatOpenAI  # OpenAI's chat model interface
from langchain.agents import tool, create_react_agent  # Tools for creating ReAct agents
import datetime  # For working with date and time
from langchain_community.tools import TavilySearchResults  # Web search tool
from langchain import hub  # For pulling pre-defined prompts from LangChain hub

# Initialize the OpenAI language model with GPT-4
llm = ChatOpenAI(model="gpt-4")

# Define a custom tool to get the current system time
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """
    Returns the current date and time in the specified format.

    Args:
        format: A string specifying the desired date-time format.

    Returns:
        A string representing the current date and time in the specified format.
    """
    current_time = datetime.datetime.now()  # Get the current timestamp
    formatted_time = current_time.strftime(format)  # Format the timestamp
    return formatted_time

# Initialize the Tavily search tool for web searches
# This tool performs basic-depth web searches
search_tool = TavilySearchResults(search_depth="basic")

# Pull the ReAct prompt template from the LangChain hub
# This template defines the reasoning and acting behavior of the agent
react_prompt = hub.pull("hwchase17/react")

# Combine all tools into a list for the ReAct agent
tools = [get_system_time, search_tool]

# Create a ReAct agent runnable
# This agent uses the tools, LLM, and prompt template to perform reasoning and acting
react_agent_runnable = create_react_agent(tools=tools, llm=llm, prompt=react_prompt)
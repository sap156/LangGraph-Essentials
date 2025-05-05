# Import necessary libraries
#from langchain_google_genai import ChatGoogleGenerativeAI  # Google's Generative AI interface
from langchain_openai import ChatOpenAI  # OpenAI's chat model interface
from dotenv import load_dotenv  # For loading environment variables
from langchain.agents import initialize_agent, tool  # Core agent components
from langchain_community.tools import TavilySearchResults  # Web search tool
import datetime  # For time-related operations

# Load environment variables from .env file (typically contains API keys)
load_dotenv()

# Initialize the OpenAI model (GPT-4o)
llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

# Initialize the Google Generative AI model (Gemini 1.5 Pro)
#llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


# Initialize the Tavily search tool with basic depth 
# https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html
# This tool will be used for web searches
search_tool = TavilySearchResults(search_depth="basic")

# Define a custom tool using the @tool decorator
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """
    
    # Get current timestamp
    current_time = datetime.datetime.now()
    # Format the timestamp according to the specified format
    formatted_time = current_time.strftime(format)
    return formatted_time

# Combine all tools into a list for the agent
tools = [search_tool, get_system_time]

# Initialize the ReAct agent
# - tools: List of tools the agent can use
# - llm: The language model to use
# - agent: The type of agent (zero-shot means it doesn't require training)
# - verbose: Print detailed steps of agent's thinking process
agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

# Invoke the agent with a query that requires both search and time calculation
agent.invoke("When was SpaceX's last launch and how many days ago was that from this instant")


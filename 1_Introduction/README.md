# ReAct Agent with LangChain

This project implements a ReAct (Reasoning and Acting) agent using LangChain that combines web search capabilities with system time operations to answer complex queries.

## Overview

The agent demonstrates the integration of:
- Large Language Models (GPT-4o or Gemini 1.5 Pro)
- Web search functionality using Tavily
- Custom system time tools
- Zero-shot reasoning capabilities

## Components

### Language Models
The agent can work with either:
- OpenAI's GPT-4o
- Google's Gemini 1.5 Pro

```python
# OpenAI Configuration
llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

# Alternatively, Google's Gemini
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
```

### Tools
The agent uses two main tools:

1. **[Tavily Search Tool](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)**
   - Performs web searches with basic depth
   - Retrieves real-time information from the internet

2. **System Time Tool**
   - Custom tool for getting current system time
   - Supports flexible date-time formatting

## Setup

1. Install required dependencies:
```bash
pip install langchain langchain-openai python-dotenv
```

2. Create a `.env` file with your API keys (get them from [OpenAI Platform](https://platform.openai.com/) and [Tavily Dashboard](https://tavily.com/)):
```env
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
```

3. Load the environment variables:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Usage

The agent can handle complex queries that require both web search and time calculations:

```python
agent.invoke("When was SpaceX's last launch and how many days ago was that from this instant")
```

This will:
1. Search for SpaceX's latest launch information
2. Get the current system time
3. Calculate the time difference
4. Provide a comprehensive answer

## Output

![ReAct Agent Output](/Users/sap156/Documents/MyDevelopment/GenAI/langgraph/images/react_agent_basic.png)

## Features

- **Zero-shot Learning**: No training required for basic tasks
- **Verbose Mode**: Detailed step-by-step reasoning process
- **Flexible Tool Integration**: Easy to add new tools and capabilities
- **Real-time Information**: Up-to-date web search results

## Technical Details

### Agent Initialization
```python
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)
```

### Custom Tool Definition
```python
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """Returns the current date and time in the specified format"""
    current_time = datetime.datetime.now()
    return current_time.strftime(format)
```

## Requirements
- Python 3.8+
- LangChain
- OpenAI API key or Google AI API key
- Tavily API key
- python-dotenv

## Limitations
- Requires active internet connection for web searches
- API rate limits may apply
- Response quality depends on the chosen language model
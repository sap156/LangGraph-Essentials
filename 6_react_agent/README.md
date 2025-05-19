# ReAct Agent System

This folder contains the implementation of a ReAct (Reasoning and Acting) agent system using LangChain. The ReAct agent combines reasoning capabilities with tool usage to perform complex tasks.

## Overview

The ReAct agent system is designed to:
- Use a language model (GPT-4) for reasoning and decision-making.
- Integrate tools like web search and system time retrieval.
- Follow a structured prompt template to guide its behavior.

## Components

### 1. `agent_reason_runnable.py`

This file defines the main ReAct agent runnable.

- **Key Features**:
  - Initializes the GPT-4 language model.
  - Defines a custom tool to retrieve the current system time.
  - Integrates the Tavily search tool for web searches.
  - Pulls a ReAct prompt template from the LangChain hub.
  - Combines tools, the language model, and the prompt to create a runnable ReAct agent.

### 2. `nodes.py`

This file defines the individual nodes used in the ReAct agent system.

- **Key Features**:
  - Implements functions that represent specific tasks or actions.
  - Each node is designed to perform a discrete operation within the agent's workflow.

### 3. `react_graph.py`

This file defines the graph structure for the ReAct agent system.

- **Key Features**:
  - Uses LangGraph to create a graph-based workflow.
  - Defines nodes and transitions between them.
  - Orchestrates the flow of tasks within the ReAct agent.

### 4. `react_state.py`

This file manages the state of the ReAct agent system.

- **Key Features**:
  - Defines the state structure and transitions.
  - Ensures that the agent maintains context across tasks.

## Setup

1. Install the required dependencies:
```bash
pip install langchain langgraph langchain-openai
```

2. Run the ReAct agent:
```bash
python agent_reason_runnable.py
```

## Features

- **Reasoning and Acting**: Combines reasoning capabilities with tool usage.
- **Tool Integration**: Supports custom tools like system time retrieval and web search.
- **Graph-Based Workflow**: Uses a graph structure to manage tasks and transitions.
- **State Management**: Maintains context across multiple tasks.

## Limitations

- Requires an OpenAI API key.
- Dependent on the quality of the language model and tools.

## Future Improvements

- Add more tools for enhanced functionality.
- Improve the prompt template for better reasoning.
- Integrate additional data sources for richer context.

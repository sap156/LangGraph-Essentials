# Reflexion Agent System

This project implements a Reflexion Agent System using LangChain and LangGraph. The system is designed to generate, critique, and revise answers iteratively, leveraging structured outputs and external tools for improvement.

## Overview

The Reflexion Agent System consists of the following components:

1. **Chains**: Defines the logic for generating and revising answers.
2. **Execute Tools**: Handles the execution of external tools (e.g., web search) to gather additional information.
3. **Reflexion Graph**: Orchestrates the flow of the system using a graph-based workflow.
4. **Schema**: Defines the structured outputs for the system using Pydantic models.

## Components

### 1. Chains (`chains.py`)

This file defines the logic for generating and revising answers using LangChain's prompt templates and tools.

- **Actor Agent Prompt**: Guides the LLM to provide detailed answers, critique them, and suggest search queries.
- **First Responder Chain**: Generates an initial ~250-word answer using the `AnswerQuestion` tool.
- **Revisor Chain**: Revises the initial answer based on critique and new information, ensuring it includes citations and adheres to the word limit.

#### Key Features:
- Uses `ChatPromptTemplate` to define dynamic prompts.
- Binds tools like `AnswerQuestion` and `ReviseAnswer` to the LLM.
- Includes detailed instructions for revising answers.

### 2. Execute Tools (`execute_tools.py`)

This file handles the execution of external tools, such as web search, to gather additional information for improving answers.

- **Tavily Search Tool**: Performs web searches and retrieves results.
- **`execute_tools` Function**: Processes tool calls from the LLM, executes search queries, and returns the results as `ToolMessage` objects.

#### Key Features:
- Integrates with the Tavily search tool for real-time information retrieval.
- Processes search queries extracted from tool calls.
- Returns results in a structured format for further processing.

### 3. Reflexion Graph (`reflexion_graph.py`)

This file defines the graph-based workflow for the Reflexion Agent System.

- **Graph Nodes**:
  - `draft`: Generates the initial answer.
  - `execute_tools`: Executes search queries to gather additional information.
  - `revisor`: Revises the answer based on critique and new information.
- **Event Loop**: Controls the flow of the graph, limiting the number of iterations to avoid infinite loops.

#### Key Features:
- Uses `MessageGraph` to define the workflow.
- Supports conditional transitions between nodes.
- Visualizes the graph structure using Mermaid diagrams and ASCII representations.

### 4. Schema (`schema.py`)

This file defines the structured outputs for the system using Pydantic models.

- **Reflection Model**: Captures critiques of an answer, including missing and superfluous information.
- **AnswerQuestion Model**: Represents a detailed answer to a question, along with search queries and reflection.
- **ReviseAnswer Model**: Extends `AnswerQuestion` by adding a `references` field for citations.

#### Key Features:
- Ensures structured and validated outputs from the LLM.
- Provides detailed descriptions for each field.
- Supports extensibility for additional use cases.

## Setup

1. Install the required dependencies:
```bash
pip install langchain langgraph langchain-openai pydantic
```

2. Create a `.env` file with your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_key_here
```

3. Load the environment variables in your code:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Usage

1. Run the Reflexion Graph:
```python
python reflexion_graph.py
```

2. Test the Execute Tools functionality:
```python
python execute_tools.py
```

3. Modify the Chains or Schema as needed to customize the system.

## Features

- **Iterative Improvement**: Generates, critiques, and revises answers iteratively.
- **Structured Outputs**: Ensures responses conform to predefined formats.
- **Tool Integration**: Leverages external tools for real-time information retrieval.
- **Graph-Based Workflow**: Orchestrates the system using a flexible and extensible graph structure.

## Limitations

- Requires an OpenAI API key.
- Dependent on the quality of LLM responses and external tool results.
- Limited to the predefined number of iterations in the event loop.

## Future Improvements

- Add support for more complex workflows and tools.
- Enhance the critique and revision logic for better answers.
- Integrate additional data sources for richer information retrieval.

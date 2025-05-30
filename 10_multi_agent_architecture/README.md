# Multi-Agent Architecture

This folder contains examples and workflows demonstrating the implementation of multi-agent architectures using LangGraph. Multi-agent systems are designed to enable collaboration between specialized agents, each performing a specific role in a workflow. These examples showcase how to build, orchestrate, and visualize such workflows.

## Files

### 1. `1_subgraphs.ipynb`
This notebook demonstrates the use of subgraphs in multi-agent workflows. Subgraphs allow for modular and reusable components within a larger workflow. Key highlights include:
- **Defining Subgraphs:** Creating a subgraph with specific states and transitions.
- **Shared Schema:** Embedding a subgraph directly into a parent graph when both share the same schema.
- **Schema Transformation:** Invoking a subgraph with a different schema by transforming the input and output.
- **Visualization:** Generating a Mermaid diagram to visualize the workflow.

### 2. `2_supervisor_multiagent_workflow.ipynb`
This notebook implements a supervisor-driven multi-agent workflow. The supervisor orchestrates the workflow by routing tasks to specialized agents based on the current state. Key highlights include:
- **Supervisor Node:** A decision-making node that routes tasks to agents such as Prompt Enhancer, Researcher, or Coder.
- **Specialized Agents:**
  - **Prompt Enhancer:** Refines and clarifies user queries.
  - **Researcher:** Gathers information using tools like Tavily Search.
  - **Coder:** Handles technical problem-solving and code execution.
- **Validation Node:** Ensures the quality of the output and decides whether to terminate the workflow or route it back to the supervisor.
- **Visualization:** Generating a Mermaid diagram to visualize the workflow.

## Applications

Multi-agent architectures are useful for:
- **Complex Workflows:** Breaking down tasks into smaller, specialized components.
- **Collaboration:** Enabling multiple agents to work together to achieve a common goal.
- **Scalability:** Designing modular workflows that can be easily extended or modified.

## How to Use

1. Open the notebooks in Jupyter or VS Code.
2. Follow the instructions and run the cells sequentially.
3. Modify the workflows or agents as needed to suit your use case.
4. Use the visualization tools to debug and optimize the workflows.

## Dependencies

Ensure that the following dependencies are installed:
- `langgraph`
- `langchain`
- `pydantic`
- `dotenv`
- `IPython`

You can install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

---

For more information, refer to the main `README.md` file in the root directory.

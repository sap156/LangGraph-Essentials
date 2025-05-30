# Streaming Workflows

This folder contains examples and workflows demonstrating the use of streaming in LangGraph. Streaming workflows allow for real-time processing and event handling, making them suitable for applications that require immediate feedback or continuous updates.

## Files

### 1. `1_stream_events.ipynb`
This notebook demonstrates how to implement and use streaming workflows in LangGraph. Key highlights include:

- **Graph Definition:**
  - Defines a state graph with nodes for handling language model invocations and tool integrations.
  - Uses conditional transitions to route the workflow dynamically.

- **Streaming Modes:**
  - **Values Mode:** Streams the final values of the workflow.
  - **Updates Mode:** Streams intermediate updates during the workflow execution.
  - **Asynchronous Streaming:** Demonstrates asynchronous event handling for real-time applications.

- **Visualization:**
  - Generates a Mermaid diagram to visualize the workflow structure.

## Applications

Streaming workflows are useful for:
- **Real-Time Applications:** Chatbots, live data processing, and interactive tools.
- **Continuous Feedback:** Providing users with immediate updates during long-running tasks.
- **Event-Driven Systems:** Handling events as they occur in a structured and scalable manner.

## How to Use

1. Open the notebook in Jupyter or VS Code.
2. Follow the instructions and run the cells sequentially.
3. Modify the workflows or input data as needed to suit your use case.
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

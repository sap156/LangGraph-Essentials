# Human-in-the-Loop Examples

This directory contains various examples demonstrating human-in-the-loop workflows using state graphs and language models. Each file showcases a unique use case or functionality. Below is a detailed explanation of each file:

## 1. `1_using_input().py`
This Python script demonstrates a state machine workflow for generating and reviewing LinkedIn posts. It uses a language model to generate content and allows human intervention for review and feedback.

### Key Features:
- **State Machine Logic**: Implements states like `generate_post`, `get_review_decision`, `post`, and `collect_feedback`.
- **Human Input**: Prompts the user to approve or provide feedback on the generated post.
- **Language Model Integration**: Uses `ChatGroq` (unresolved import issue) for content generation.

### Workflow:
1. Generate a LinkedIn post.
2. Review the post and decide to approve or provide feedback.
3. Iterate until the post is finalized.

---

## 2. `2_command.ipynb`
This notebook demonstrates a simple state machine workflow where each node performs a specific action and transitions to the next state.

### Key Features:
- **State Transitions**: Nodes `node_a`, `node_b`, and `node_c` perform sequential updates to the state.
- **Command Updates**: Each node appends a character (`a`, `b`, `c`) to the state value.

### Workflow:
1. Start at `node_a`.
2. Transition to `node_b` and then to `node_c`.
3. End the workflow.

---

## 3. `3_resume.ipynb`
This notebook demonstrates a state machine workflow with human intervention and the ability to resume execution from a specific state.

### Key Features:
- **Human Intervention**: Uses the `interrupt` function to allow human input for decision-making.
- **State Resumption**: Supports resuming the workflow from a specific state.
- **Checkpointing**: Uses `MemorySaver` to save and restore state.

### Workflow:
1. Start at `node_a`.
2. Transition to `node_b` and prompt the user to choose between `node_c` and `node_d`.
3. Resume execution based on the user's choice.

---

## 4. `4_approval.ipynb`
This notebook demonstrates a state machine workflow with tool integration and conditional transitions.

### Key Features:
- **Tool Integration**: Uses `TavilySearchResults` as a tool for search results.
- **Conditional Transitions**: Routes the workflow based on the presence of tool calls in the state.
- **Language Model with Tools**: Integrates tools with the language model for enhanced functionality.

### Workflow:
1. Start at the `model` node.
2. Transition to the `tools` node if tool calls are present.
3. Iterate between `model` and `tools` until the workflow ends.

---

## 5. `5_multiturn_conversation.py`
This Python script demonstrates a multi-turn conversational workflow for generating and refining LinkedIn posts with human feedback.

### Key Features:
- **Multi-Turn Interaction**: Allows iterative refinement of generated content based on human feedback.
- **Interrupt Mechanism**: Pauses execution to collect feedback from the user.
- **Finalization**: Ends the workflow once the user is satisfied with the content.

### Workflow:
1. Generate a LinkedIn post based on a user-provided topic.
2. Collect feedback from the user and refine the post.
3. Finalize the post once the user is satisfied.

---

## Common Concepts
- **StateGraph**: A framework for defining and managing state machine workflows.
- **Command**: Represents transitions and updates to the state.
- **Interrupt**: Allows human intervention during workflow execution.
- **MemorySaver**: Provides checkpointing and state resumption capabilities.

---

## Notes
- The `langchain_groq` module is used in some examples but has an unresolved import issue. Ensure the module is installed or replace it with an alternative.
- These examples are designed to be modular and extensible, allowing you to adapt them to your specific use cases.

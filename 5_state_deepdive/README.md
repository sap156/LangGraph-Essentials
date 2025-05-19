# State Deep Dive with LangGraph

This project explores the use of state graphs in LangGraph to manage and manipulate stateful workflows. Two examples are provided to demonstrate basic and complex state management.

## Overview

State graphs allow for the definition of workflows where the state is updated and transitions are determined based on conditions. This project includes:

1. **Basic State Management**: A simple example with a single state field (`count`).
2. **Complex State Management**: A more advanced example with multiple state fields (`count`, `sum`, and `history`) and annotated operations.

## Components

### 1. Basic State (`1_basic_state.py`)

This file demonstrates a simple state graph with a single state field (`count`).

- **State Structure**:
  - `count`: An integer representing the current count.
- **Increment Function**:
  - Increments the `count` by 1.
- **Conditional Edges**:
  - Transitions to the `increment` node if `count` is less than 5.
  - Ends the graph execution if `count` reaches 5.

#### Key Features:
- Simple state structure using `TypedDict`.
- Basic conditional logic for graph transitions.

#### Example Output:
```
{'count': 5}
```

### 2. Complex State (`2_complex_state.py`)

This file demonstrates a more advanced state graph with multiple state fields and annotated operations.

- **State Structure**:
  - `count`: An integer representing the current count.
  - `sum`: An integer representing the cumulative sum of counts (annotated with `operator.add`).
  - `history`: A list of integers representing the history of counts (annotated with `operator.concat`).
- **Increment Function**:
  - Increments the `count` by 1.
  - Updates the `sum` with the new count.
  - Appends the new count to the `history`.
- **Conditional Edges**:
  - Transitions to the `increment` node if `count` is less than 5.
  - Ends the graph execution if `count` reaches 5.

#### Key Features:
- Complex state structure with annotated fields.
- Advanced state manipulation in the `increment` function.

#### Example Output:
```
{'count': 5, 'sum': 5, 'history': [5]}
```

## Setup

1. Install the required dependencies:
```bash
pip install langgraph
```

2. Run the examples:
```bash
python 1_basic_state.py
python 2_complex_state.py
```

## Features

- **Stateful Workflows**: Manage and manipulate state across multiple nodes.
- **Conditional Transitions**: Define dynamic transitions based on state conditions.
- **Annotated Fields**: Use annotations to define operations on state fields.

## Limitations

- Limited to the predefined state structure.
- Requires manual definition of state transitions and operations.

## Future Improvements

- Add support for more complex state operations.
- Integrate external tools for dynamic state updates.
- Provide visualization for state transitions.

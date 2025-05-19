# Chatbot System

This folder contains implementations of various chatbot systems using LangChain. Each file demonstrates a different aspect of chatbot functionality, from basic interactions to advanced checkpointing mechanisms.

## Overview

The chatbot system is designed to:
- Handle user interactions using a language model.
- Integrate tools for enhanced functionality.
- Maintain conversation context using checkpointing mechanisms.

## Components

### 1. `1_basic_chatbot.py`

This file implements a basic chatbot system.

- **Key Features**:
  - Handles simple user interactions.
  - Uses a language model for generating responses.

### 2. `2_chatbot_with_tools.py`

This file extends the basic chatbot by integrating tools.

- **Key Features**:
  - Supports tool usage for enhanced functionality.
  - Demonstrates how to combine tools with a chatbot system.

### 3. `3_chat_with_in_memory_checkpointer.py`

This file adds in-memory checkpointing to the chatbot system.

- **Key Features**:
  - Maintains conversation context in memory.
  - Allows the chatbot to handle multi-turn conversations.

### 4. `4_chat_with_sqlite_checkpointer.py`

This file adds SQLite-based checkpointing to the chatbot system.

- **Key Features**:
  - Stores conversation context in a SQLite database.
  - Ensures persistence across sessions.

## Setup

1. Install the required dependencies:
```bash
pip install langchain sqlite3
```

2. Run the chatbot examples:
```bash
python 1_basic_chatbot.py
python 2_chatbot_with_tools.py
python 3_chat_with_in_memory_checkpointer.py
python 4_chat_with_sqlite_checkpointer.py
```

## Features

- **Basic Chatbot**: Handles simple user interactions.
- **Tool Integration**: Enhances chatbot functionality with tools.
- **Checkpointing**: Maintains conversation context using in-memory or SQLite checkpointing.

## Limitations

- Requires a language model for generating responses.
- Dependent on the quality of the language model and tools.

## Future Improvements

- Add more tools for enhanced functionality.
- Improve checkpointing mechanisms for scalability.
- Integrate additional data sources for richer context.

# Structured Outputs with LangChain

This project demonstrates how to use LangChain to generate structured outputs using Pydantic models, TypedDict, and JSON schemas. The structured outputs ensure that the responses from the language model (LLM) conform to a predefined format, making them easier to parse and use in downstream applications.

## Overview

The notebook `types.ipynb` explores three approaches to structuring outputs from the LLM:

1. **Pydantic Models**: Define structured outputs using Python's Pydantic library.
2. **TypedDict**: Use Python's `TypedDict` to define lightweight schemas for structured outputs.
3. **JSON Schema**: Define outputs using JSON schema for flexibility and compatibility with external systems.

## Components

### 1. Pydantic Models

Pydantic models are used to define structured outputs with detailed field descriptions. This approach is ideal for Python-based applications that require strict type validation.

#### Example:
```python
from pydantic import BaseModel, Field

class Country(BaseModel):
    """Information about a country"""
    name: str = Field(description="name of the country")
    language: str = Field(description="language of the country")
    capital: str = Field(description="Capital of the country")

structured_llm = llm.with_structured_output(Country)
structured_llm.invoke("Tell me about France")
```

### 2. TypedDict

TypedDict is a lightweight way to define structured outputs. It is particularly useful for simple use cases where full-fledged models are not required.

#### Example:
```python
from typing_extensions import Annotated, TypedDict

class Joke(TypedDict):
    """Joke to tell user."""
    setup: Annotated[str, ..., "The setup of the joke"]
    punchline: Annotated[str, ..., "The punchline of the joke"]
    rating: Annotated[Optional[int], None, "How funny the joke is, from 1 to 10"]

structured_llm = llm.with_structured_output(Joke)
structured_llm.invoke("Tell me a joke about cats")
```

### 3. JSON Schema

JSON schema provides a flexible way to define structured outputs, making it compatible with a wide range of systems and programming languages.

#### Example:
```python
json_schema = {
    "title": "joke",
    "description": "Joke to tell user.",
    "type": "object",
    "properties": {
        "setup": {
            "type": "string",
            "description": "The setup of the joke",
        },
        "punchline": {
            "type": "string",
            "description": "The punchline to the joke",
        },
        "rating": {
            "type": "integer",
            "description": "How funny the joke is, from 1 to 10",
            "default": None,
        },
    },
    "required": ["setup", "punchline"],
}

structured_llm = llm.with_structured_output(json_schema)
structured_llm.invoke("Tell me a joke about cats")
```

## Setup

1. Install the required dependencies:
```bash
pip install langchain-openai pydantic typing-extensions
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

Run the notebook `types.ipynb` to explore the structured output examples. Each cell demonstrates a different approach to structuring outputs from the LLM.

## Features

- **Structured Outputs**: Ensures that LLM responses conform to predefined formats.
- **Flexibility**: Supports Pydantic, TypedDict, and JSON schema for defining structures.
- **Ease of Use**: Simplifies downstream processing of LLM responses.

## Limitations

- Requires an OpenAI API key.
- Structured outputs depend on the LLM's ability to adhere to the schema.
- JSON schema support may require additional validation in some cases.

## Future Improvements

- Add support for more complex schemas.
- Explore integration with other LLMs.
- Provide examples for multi-field validation and nested schemas.

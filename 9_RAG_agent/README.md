# Retrieval-Augmented Generation (RAG) Agent Examples

This folder contains examples demonstrating the use of Retrieval-Augmented Generation (RAG) workflows. Each file showcases a unique use case or functionality of RAG agents.

---

## 1. `1_basic.ipynb`
This notebook introduces the basic concepts of RAG workflows.

### Key Features:
- **Document Embedding**: Uses OpenAI embeddings to represent documents in vector space.
- **Vector Store**: Implements a Chroma vector store for document retrieval.
- **Question Answering**: Retrieves relevant documents and answers questions based on the context.

### Workflow:
1. Embed documents using OpenAI embeddings.
2. Store the embeddings in a Chroma vector store.
3. Retrieve relevant documents based on a query.
4. Use a language model to generate answers from the retrieved documents.

---

## 2. `2_classification_driven_agent.ipynb`
This notebook implements a classification-driven RAG agent.

### Key Features:
- **Question Classification**: Determines whether a question is on-topic or off-topic.
- **Conditional Workflow**: Routes the workflow based on the classification result.
- **Document Retrieval**: Retrieves relevant documents for on-topic questions.
- **Answer Generation**: Generates answers using a language model and retrieved documents.

### Workflow:
1. Classify the question as on-topic or off-topic.
2. Retrieve relevant documents for on-topic questions.
3. Generate answers using the retrieved documents.
4. Respond with an off-topic message for off-topic questions.

---

## 3. `3_rag_powered_tool_calling.ipynb`
This notebook demonstrates RAG-powered tool calling.

### Key Features:
- **Tool Integration**: Integrates tools for answering specific types of questions.
- **Retriever Tool**: Uses a retriever tool for document-based question answering.
- **Off-Topic Handling**: Defines a tool for handling off-topic questions.

### Workflow:
1. Use a retriever tool to answer on-topic questions.
2. Use an off-topic tool to handle unrelated questions.
3. Generate responses using the appropriate tool.

---

## 4. `4_advanced_multi_step_reasoning.ipynb`
This notebook explores advanced multi-step reasoning with RAG.

### Key Features:
- **Question Rewriting**: Rewrites user questions to improve retrieval results.
- **Document Grading**: Grades retrieved documents for relevance.
- **Iterative Refinement**: Refines questions iteratively to improve retrieval.
- **Answer Generation**: Generates answers using a language model and graded documents.

### Workflow:
1. Rewrite the user question to optimize retrieval.
2. Retrieve documents and grade them for relevance.
3. Refine the question if no relevant documents are found.
4. Generate answers using the most relevant documents.
5. Respond with a fallback message if no relevant documents are found after refinement.

---

## Notes
- These examples demonstrate the flexibility and power of RAG workflows for various use cases.
- The notebooks are designed to be modular and extensible, allowing you to adapt them to your specific requirements.

# 🌌 Generative AI with LangChain

This module serves as a practical guide to building Large Language Model (LLM) applications using **LangChain**. It covers the fundamental building blocks of modern GenAI development, from basic prompts to advanced RAG pipelines.

## 🧱 Key Components

- **[`01_Models`](./01_Models)**: Integrating with various LLM providers (Hugging Face, OpenAI, etc.).
- **[`02_Prompts`](./02_Prompts)**: Designing effective Prompt Templates and Few-Shot examples.
- **[`03_Chains`](./03_Chains)**: Orchestrating multiple LLM calls into a single workflow.
- **[`04_RAG`](./04_RAG)**: Retrieval-Augmented Generation using Vector Stores and Document Loaders.
- **[`05_Tools`](./05_Tools)**: Equipping agents with external tools for search, math, and API calls.

## 🛠️ Getting Started

### Installation
```bash
pip install langchain langchain-community langchain-huggingface sentence-transformers chromadb
```

### Concepts Covered
- **LCEL (LangChain Expression Language)**: Declarative way to compose chains.
- **ChatModels & TextModels**: Handling different LLM interfaces.
- **Output Parsers**: Extracting structured data from raw LLM responses.
- **Vector Databases**: Setting up indexing for retrieval.

---
*Part of the [AI Engineering Roadmap](../README.md)*

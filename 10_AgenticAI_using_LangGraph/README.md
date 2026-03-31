# 🤖 Agentic AI with LangGraph

This module explores the development of stateful, multi-agent AI systems utilizing **LangGraph**. Unlike simple linear chains, LangGraph allows for cyclic graphs, complex state management, and human-in-the-loop interactions.

## 📈 Learning Progression

The exercises are structured to build complexity step-by-step:

1. **[Sequential Workflows](./1_sequential_Workflows)**: Implementing linear multi-step agent processes.
2. **[Parallel Workflows](./2_parallel-workflows)**: Executing multiple agent tasks concurrently for efficiency.
3. **[Conditional Workflows](./3_conditional-workflow)**: Using routers to direct the flow based on LLM decisions.
4. **[Iterative Workflows](./4_iterative-workflow)**: Implementing loops for task refinement and self-correction.
5. **[Chatbot Implementation](./5_chatbot)**: Building a persistent, stateful conversational agent.

## 🗝️ Core Concepts Covered

- **Nodes & Edges**: Defining the structure of the agentic graph.
- **State Management**: Using `TypedDict` to pass context between nodes.
- **Conditional Edges**: Logic-based routing within the graph.
- **Persistence**: Using `Checkpointers` to save and resume agent state.

## 🛠️ Getting Started

### Installation
Ensure you have the following packages installed:
```bash
pip install langgraph langchain-huggingface python-dotenv
```

### Environment Setup
Create a `.env` file with your API keys:
```env
HUGGINGFACE_REPO_ID=your_model_id
HUGGINGFACEHUB_API_TOKEN=your_token
```

---
*Part of the [AI Engineering Roadmap](../README.md)*

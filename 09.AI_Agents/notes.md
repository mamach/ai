# AI Agents
- setting up a modern AI agent in python that integrates an LLM, RAG and MCP involves combining
    - Reasoning
    - data retrieval
    - context servers/ standardized tool

# Project Setup
- 
```
mkdir ai-agent-demo
cd ai-agent-demo
python -m venv venv
source venv/bin/activate

pip install langchain langchain-openai langchain-community chromadb mcp python-dotenv
```

- .env
```
OPENAI_API_KEY="key-here"
```

--- 
# Implement the Core Components
- A complete agent architecture brings together RAG and MCP managed by an LLM Agent Loop.
- RAG
    - RAG allows your agent to serch through a local knowledge base (vector database) before answering or acting.
- MCP
    - MCP standardizes how agents connect to external tools, databases, or resources via http servers.
    - Python can be used to rwap MCP client.
- 
---
# Agent Loop
- Wire the LLM, prompt, and tools together using a framework like Langchain. 
- The agent loop handles the reasoning steps
    - Thoutghts -> Tool Call -> Observation -> Final Answer
- 
---
- User Input -> LLM Reasoning -> Execution and Observation -> Final Synthesis

---


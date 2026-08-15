# MCP
- A standard way for LLMs to use tools.

## Ecosystem
- MCP Host
    - Claude Desktop
    - IDE
    - AI Tools
- MCP Client
    - connects to mcp server with MCP protocol.
- MCP Server
    - invokes web apis
    - executes queries
    - reads and writes files

# RAG
- LLMs augumented with retrieved knowledge.
- User Query -> retriever fetches info -> Retruns documents -> query+retrieved documents to LLMs -> LLM generates response
- Knowledge base
    - PDF
    - Vector DB
    - Code
- Retriever is run time knowledge retrieval.

# AI Agents
- LLM that can take actions and make decisions.
- Human Control -> HIL
- Short term memory.

---
- MCP is about how LLMs use tools Think of it as standard interface between an LLM and external systems.
- Databases, file systems, GitHub, internal APIs
- Instead of every app inventing its own glue code, MCP defines a consistent way for models to discover tools, invoke them and get structured results back.
- MCP does not decide what to do. It standardizes how tools are exposed.

--- 
- RAG (Retrieval-Augumented Generation) is about what the model knows at runtime.
- The model stays frozen.
- No retraining.
- When a user asks a question, a retriever fetches releavant documents(pdfs, code, vector db) and those are injected into the prompt.
- RAG is great for
    - Internal knowledge bases.
    - Fresh or private data
    - Reducing hallucinations.
- RAG doesnot take actions. It only improve answers.

---
- AI agents are about doing things.
- An aget observers, reasons, decides, acts, and repeats.
- It can call tools, write code, browse the internet, store memory, delegate tasks, and operate with different level of autonomy.

---





















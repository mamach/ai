# MCP

## Intro
- An MCP server setup paired with ai agents to creates an extensible system where your models
    - can read local files
    - execute code
    - access live apis and
    - query databases.
- The Model Context Protocol, originally developed by Anthropic, acts as a open standard bridge between LLM and local or remote tools/data sources.


## Architecture
- When setting up MCP with AI agents, the architecture consists of 3 distinct layers.
    1. AI Host/ AI Agent Runtime e.g. OpenClaw
    2. MCP Client e.g., Claude Code or Lang Chain
    3. MCP Server e.g., Local/ Remote filesystem, postgres, browser, github etc.
- MCP Host: The execution runtime that drives the reasoning. (e.g., Claude Code, Open Claw, Anaconda Agent Studio etc.)
- MCP Client: The layer inside the agent framework that translates the LLM's function calls into standardized MCP requests.
- MCP Server: Lightweight, isolated microservices that expose standard interfaces.
    - Tools: Functions the model can run (e.g., write_file, query_db)
    - Resources: Context/data sources model (e.g., file paths, logs)
    - Prompts: Pre-configured template instructions.
-

## MCP Server Setup
- MCP Server stack
- Granting direct access to local filesystem and a SQLite database.
- Node.js and python
-
```
node -v
pip install uv
```
- mcp server manifest

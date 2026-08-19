# Function Calling and Tool Calling
- Function calling and Tool Calling are the core mechanics that allow an LLM to interact with the outside world.
    - APIs
    - Databases
    - Python functions
    - MCP Servers
- Function Calling is the specific mechanism of outputting structured JSON argument. 
- Tool Calling modren umbrella term (introduced by OpenAI, Anthropic, and Opensource Models) that encompasses functions, built in capabilities, and external plugins

---
# How Tool/Function Calling works 
- LLM will never executes code itself.
- LLM acts as reasoning engine that generates a structured request.
- Life Cycle
    - Schema Declaration
        - Pass list of availabool tools with names decriptions and JSON schema for arguments along with the users prompt to LLM API.
    - Intent Extraction
        - LLM decides  it needs external help.
        - Instead of natural text, it responds with special payload "Call function calculate shipping with arguments weight_kg=5, distance_km=100"
    - Execution and feedback
        - Your python code intercepts this json, executes real python locally, and send the output back to LLM as new message (role: tool), allowing LLM to write its final message.

---
# Tool Calling relates to RAG and MCP
- RAG as a Tool: In a pure function calling setup, RAG is just a tool. 
- You define tool called search_vector_database(query: str). 
- When the user asks a private question, the LLM triggers this tool function, receives text chunks and synthesizes an answer.
- MCP as a Tool Provider: MCP standardizes how these JSON schemas and execution handlers are delivered.
- Instead of manually writing JSON scchemas in your application code, an external MCP server dynamically publishes its tools and handles execution securely over a local transport or http endpoint.

---
-  

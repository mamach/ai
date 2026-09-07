- An opensource ecosystem for modern AI engineering spans several distinct layers from infra routing and model serving to vector search, context retrieval, protocol integration, and agent orchestration.

# AI Gateway and Infrastructure
- Bifrost: A high performance ultra low latency ai gateway written in GO. It unifies multi provider model routing, handles semantic caching, implements virtual key governance, and natively supports MCP orchestration.
- LiteLLM: A widely adopted python based proxy and routing tool that standardizes dozens of LLM APIs into unified OpenAI  compatible format with built in cost tracking and rate limiting.
- vLLM/Ollama: Industry standard for local and cloud model serving. vLLM excels at high througput production inference vi pagedattention while ollama streamlines local developer workflows. 

# RAG and Document intelligence
- LlamaIndex and LangChain: Core frameworks for data ingestion, indexing strategies and connecting private copuses to LLMs.
- RAGFlow / Dify: Specialized engines tailored for deep document understanding, visual layout parsing, and out of the the box RAG Pipelines.
- Milvus / Qdrant/ Chroma: Cloud native vector databases engineered for scalable similarity search and high speed retrieval.

# MCP and Tooling
- MCP servers and Clients: Open protocols developed to standardize how ai models and agents securely connect to local data sources, developers tools, and enterprise databases. Gateways like biforst integrate natively as MCP servers/clients to securely handle tool routing and authorization.
- Composio / Browser Use: Open source ecosystems that give agents secure tool execution environments and programmatic access to web browsers or external apis.

# AI Agents and Orchestration
- LangGraph / Crew AI / AutoGen: Frameworks designed for multi-agent loops, stateful workflows, role based task delegation, and autonomous execution.
- Flowise / Langflow: Visual low code drag and drop builders that allow rapid prototyping and composition of agentic workflows and RAG chains.

---




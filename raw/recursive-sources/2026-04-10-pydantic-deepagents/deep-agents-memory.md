---
title: Memory - Docs by LangChain
source_url: https://docs.langchain.com/oss/python/deepagents/memory
final_url: https://docs.langchain.com/oss/python/deepagents/memory
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:33:35.482722+00:00
---

# Memory - Docs by LangChain

## 원본 URL

https://docs.langchain.com/oss/python/deepagents/memory

## 주요 헤딩

- Memory
- ​ How memory works
- ​ Scoped memory
- ​ Advanced usage

## 추출 본문

Memory - Docs by LangChain
Skip to main content
Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. Buy tickets >
Docs by LangChain home page
Open source
Search...
⌘ K
Ask AI
GitHub
Try LangSmith
Try LangSmith
Search...
Navigation
Core capabilities
Memory
Deep Agents
LangChain
LangGraph
Integrations
Learn
Reference
Contribute
Python
Overview
Get started
Quickstart
Customization
Comparison
Changelog
Deployment
Deploy with the CLI
Going to production
Core capabilities
Overview
Models
Context engineering
Backends
Subagents
Async subagents
Human-in-the-loop
Memory
Skills
Sandboxes
Streaming
Frontend
Overview
Patterns
Protocols
Agent Client Protocol (ACP)
Command line interface
Use the CLI
Model providers
Configuration
MCP Tools
On this page How memory works
Scoped memory
Agent-scoped memory
User-scoped memory
Advanced usage
Episodic memory
Organization-level memory
Background consolidation
Consolidation agent
Cron
Read-only vs writable memory
Concurrent writes
Multiple agents in the same deployment
Core capabilities
Memory
Copy page
Add persistent memory to agents built with Deep Agents so they learn and improve across conversations
Copy page
Memory lets your agent learn and improve across conversations. Deep Agents makes memory first class with filesystem-backed memory: the agent reads and writes memory as files, and you control where those files are stored using backends .
This page covers long-term memory : memory that persists across conversations. For short-term memory (conversation history and scratch files within a single session), see the context engineering guide. Short-term memory is managed automatically as part of the agent’s state .
​
How memory works
Point the agent at memory files. Pass file paths to memory=
when creating the agent. You can also pass skills via skills=
for procedural memory (reusable instructions that tell the agent how to perform a task). A backend controls where files are stored and who can access them.
Agent reads memory. The agent can load memory files into the system prompt at startup, or read them on demand during the conversation. For example, skills use on-demand loading: the agent reads only skill descriptions at startup, then reads the full skill file only when it matches a task. This keeps context lean until a capability is needed.
Agent updates memory (optional). When the agent learns new information, it can use its built-in edit_file
tool to update memory files. Updates can happen during the conversation (the default) or in the background between conversations via background consolidation . Changes are persisted and available in the next conversation. Not all memory is writable: developer-defined skills and organization policies are typically read-only. See read-only vs writable memory for details.
The two most common patterns are agent-scoped memory (shared across all users) and user-scoped memory (isolated per user).
​
Scoped memory
Agent memory can be scoped so the same memory files are accessible to everyone using the agent or memory files can be individual to each user.
​
Agent-scoped memory
Give the agent its own persistent identity that evolves over time. Agent-scoped memory is shared across all users, so the agent builds up its own persona, accumulated knowledge, and learned preferences through every conversation. As it interacts with users, it develops expertise, refines its approach, and remembers what works. It can also learn and update skills when it has write access.
The key is the backend namespace: setting it to (assistant_id,)
means every conversation for this agent reads and writes to the same memory file.
Accessing ctx.runtime.server_info
requires deepagents>=0.5.0
. On older versions, read the assistant ID from get_config()["metadata"]["assistant_id"]
instead.
from deepagents import create_deep_agent
from deepagents . backends import CompositeBackend , StateBackend , StoreBackend
agent = create_deep_agent (
memory = [ "/memories/AGENTS.md" ],
skills = [ "/skills/" ],
backend = CompositeBackend (
default = StateBackend (),
routes = {
"/memories/" : StoreBackend (
namespace = lambda ctx : (
ctx . runtime . server_info . assistant_id ,
),
),
"/skills/" : StoreBackend (
namespace = lambda ctx : (
ctx . runtime . server_info . assistant_id ,
),
),
},
),
)
Full example: seed memory and invoke
Populate the store with initial memories, then invoke the agent across two threads to see it remember and update what it learns.
from langchain_core . utils . uuid import uuid7
from deepagents import create_deep_agent
from deepagents . backends import CompositeBackend , StateBackend , StoreBackend
from deepagents . backends . utils import create_file_data
from langgraph . store . memory import InMemoryStore
store = InMemoryStore () # Use platform store when deploying to LangSmith
# Seed the memory file
store . put (
( "my-agent" ,),
"/memories/AGENTS.md" ,
create_file_data ( """## Response style
- Keep responses concise
- Use code examples where possible
""" ),
)
# Seed a skill
store . put (
( "my-agent" ,),
"/skills/langgraph-docs/SKILL.md" ,
create_file_data ( """---
name: langgraph-docs
description: Fetch relevant LangGraph documentation to provide accurate guidance.
---
# langgraph-docs
Use the fetch_url tool to read https://docs.langchain.com/llms.txt, then fetch relevant pages.
""" ),
)
agent = create_deep_agent (
memory = [ "/memories/AGENTS.md" ],
skills = [ "/skills/" ],
backend = lambda rt : CompositeBackend (
default = StateBackend ( rt ),
routes = {
"/memories/" : StoreBackend (
rt , namespace = lambda ctx : ( "my-agent" ,)
),
"/skills/" : StoreBackend (
rt , namespace = lambda ctx : ( "my-agent" ,)
),
},
),
store = store ,

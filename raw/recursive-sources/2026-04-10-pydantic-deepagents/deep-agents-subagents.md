---
title: Subagents - Docs by LangChain
source_url: https://docs.langchain.com/oss/python/deepagents/subagents
final_url: https://docs.langchain.com/oss/python/deepagents/subagents
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:33:35.252492+00:00
---

# Subagents - Docs by LangChain

## 원본 URL

https://docs.langchain.com/oss/python/deepagents/subagents

## 주요 헤딩

- Subagents
- ​ Why use subagents?
- ​ Configuration
- ​ Using SubAgent
- ​ Using CompiledSubAgent
- ​ Streaming
- ​ Structured output
- ​ The general-purpose subagent
- Example
- ​ Best practices
- ​ Common patterns
- ​ Context management
- ​ Troubleshooting

## 추출 본문

Subagents - Docs by LangChain
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
Subagents
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
On this page Why use subagents?
Configuration
SubAgent (Dictionary-based)
CompiledSubAgent
Using SubAgent
Using CompiledSubAgent
Streaming
Structured output
The general-purpose subagent
Override the general-purpose subagent
When to use it
Skills inheritance
Best practices
Write clear descriptions
Keep system prompts detailed
Minimize tool sets
Choose models by task
Return concise results
Common patterns
Multiple specialized subagents
Context management
Per-subagent context
Identifying which subagent called a tool
Troubleshooting
Subagent not being called
Context still getting bloated
Wrong subagent being selected
Core capabilities
Subagents
Copy page
Learn how to use subagents to delegate work and keep context clean
Copy page
Deep Agents can create subagents to delegate work. You can specify custom subagents in the subagents
parameter. Subagents are useful for context quarantine (keeping the main agent’s context clean) and for providing specialized instructions.
This page covers synchronous subagents, where the supervisor blocks until the subagent finishes. For long-running tasks, parallel workstreams, or cases where you need mid-flight steering and cancellation, see Async subagents .
​
Why use subagents?
Subagents solve the context bloat problem . When agents use tools with large outputs (web search, file reads, database queries), the context window fills up quickly with intermediate results. Subagents isolate this detailed work—the main agent receives only the final result, not the dozens of tool calls that produced it.
When to use subagents:
✅ Multi-step tasks that would clutter the main agent’s context
✅ Specialized domains that need custom instructions or tools
✅ Tasks requiring different model capabilities
✅ When you want to keep the main agent focused on high-level coordination
When NOT to use subagents:
❌ Simple, single-step tasks
❌ When you need to maintain intermediate context
❌ When the overhead outweighs benefits
​
Configuration
subagents
should be a list of dictionaries or CompiledSubAgent
objects. There are two types:
​
SubAgent (Dictionary-based)
For most use cases, define subagents as dictionaries matching the SubAgent
spec with the following fields:
Field Type Description name
str
Required. Unique identifier for the subagent. The main agent uses this name when calling the task()
tool. The subagent name becomes metadata for AIMessage
s and for streaming, which helps to differentiate between agents. description
str
Required. Description of what this subagent does. Be specific and action-oriented. The main agent uses this to decide when to delegate. system_prompt
str
Required. Instructions for the subagent. Custom subagents must define their own. Include tool usage guidance and output format requirements.
Does not inherit from main agent. tools
list[Callable]
Required. Tools the subagent can use. Custom subagents specify their own. Keep this minimal and include only what’s needed.
Does not inherit from main agent. model
str
| BaseChatModel
Optional. Overrides the main agent’s model. Omit to use the main agent’s model.
Inherits from main agent by default. You can pass either a model identifier string like 'openai:gpt-5'
(using the 'provider:model'
format) or a LangChain chat model object ( init_chat_model("gpt-5")
or ChatOpenAI(model="gpt-5")
). middleware
list[Middleware]
Optional. Additional middleware for custom behavior, logging, or rate limiting.
Does not inherit from main agent. interrupt_on
dict[str, bool]
Optional. Configure human-in-the-loop for specific tools. Subagent value overrides main agent. Requires checkpointer.
Inherits from main agent by default. Subagent value overrides the default. skills
list[str]
Optional. Skills source paths. When specified, the subagent will load skills from these directories (e.g., ["/skills/research/", "/skills/web-search/"]
). This allows subagents to have different skill sets than the main agent.
Does not inherit from main agent. Only the general-purpose subagent inherits the main agent’s skills. When a subagent has skills, it runs its own independent SkillsMiddleware
instance. Skill state is fully isolated—a subagent’s loaded skills are not visible to the parent, and vice versa.
CLI users: You can also define subagents as AGENTS.md
files on disk instead of in code. The name
, description
, and model
fields map to YAML frontmatter, and the markdown body becomes the system_prompt
. See Custom subagents for the file format.
​
CompiledSubAgent
For complex workflows, use a prebuilt LangGraph graph as a CompiledSubAgent
:
Field Type Description name
str
Required. Unique identifier for the subagent. The subagent name becomes metadata for AIMessage
s and for streaming, which helps to differentiate between agents. description
str
Required. What this subagent does. runnable
Runnable
Required. A compiled LangGraph graph (must call .compile()

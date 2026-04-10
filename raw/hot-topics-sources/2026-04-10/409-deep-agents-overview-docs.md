---
title: Deep Agents overview - Docs by LangChain
source_url: https://docs.langchain.com/oss/python/deepagents/overview
final_url: https://docs.langchain.com/oss/python/deepagents/overview
status: 200
content_type: text/html; charset=utf-8
topics: [Deep Agents (LangChain Harness for Long-Running Tasks)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:23.496842+00:00
---

# Deep Agents overview - Docs by LangChain

## 원본 URL

https://docs.langchain.com/oss/python/deepagents/overview

## 추출 본문

Deep Agents overview - Docs by LangChain

Skip to main content

Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. Buy tickets >

Docs by LangChain home page

Open source

Search...

⌘K

Ask AI

GitHub

Try LangSmith

Try LangSmith

Search...

Navigation

Deep Agents overview

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

On this page

 Create a deep agent

When to use the Deep Agents

Core capabilities

Get started

Deep Agents overview

Copy page

Build agents that can plan, use subagents, and leverage file systems for complex tasks

Copy page

The easiest way to start building agents and applications powered by LLMs—with built-in capabilities for task planning, file systems for context management, subagent-spawning, and long-term memory.
You can use deep agents for any task, including complex, multi-step tasks.We think of 
deepagents
 as an “agent harness”. It is the same core tool calling loop as other agent frameworks, but with built-in tools and capabilities.
deepagents
 is a standalone library built on top of LangChain’s core building blocks for agents. It uses the LangGraph runtime for durable execution, streaming, human-in-the-loop, and other features.The 
deepagents
 repository contains:
Deep Agents SDK: A package for building agents that can handle any task

Deep Agents CLI: A terminal coding agent built on the Deep Agents SDK

ACP integration: An Agent Client Protocol connector for using deep agents in code editors like Zed
LangChain is the framework that provides the core building blocks for your agents.
To learn more about the differences between LangChain, LangGraph, and Deep Agents, see Frameworks, runtimes, and harnesses.

​

 Create a deep agent

# pip install -qU deepagentsfrom deepagents import create_deep_agentdef get_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create_deep_agent( tools=[get_weather], system_prompt="You are a helpful assistant",)# Run the agentagent.invoke( {"messages": [{"role": "user", "content": "what is the weather in sf"}]})

See the Quickstart and Customization guide to get started building your own agents and applications with Deep Agents.

Use LangSmith to trace requests, debug agent behavior, and evaluate outputs. Set 
LANGSMITH_TRACING=true
 and your API key to get started.

​

When to use the Deep Agents
Use the Deep Agents SDK when you want to build agents that can:
Handle complex, multi-step tasks that require planning and decomposition

Manage large amounts of context through file system tools and summarization

Swap filesystem backends to use in-memory state, local disk, durable stores, sandboxes, or your own custom backend

Execute shell commands via the 
execute
 tool when using a sandbox backend

Delegate work to specialized subagents for context isolation

Persist memory across conversations and threads

Require human approval for sensitive operations with human-in-the-loop workflows

Use any model that supports tool calling — provider agnostic across frontier and open models
For building simpler agents, consider using LangChain’s 
create_agent
 or building a custom LangGraph workflow.

​

Core capabilities

Planning and task decomposition

Deep Agents include a built-in 
write_todos
 tool that enables agents to break down complex tasks into discrete steps, track progress, and adapt plans as new information emerges.

Context management

File system tools (
ls
, 
read_file
, 
write_file
, 
edit_file
) allow agents to offload large context to in-memory or filesystem storage, preventing context window overflow and enabling work with variable-length tool results. Auto-summarization compacts older conversation messages when the context window grows long, keeping the agent effective across extended sessions.

Shell execution

When using a sandbox backend, agents get an 
execute
 tool to run shell commands for tests, builds, git operations, and system tasks. Sandbox backends provide isolation so agents can execute code without compromising your host system.

Pluggable filesystem backends

The virtual filesystem is powered by pluggable backends that you can swap to fit your use case. Choose from in-memory state, local disk, LangGraph store for cross-thread persistence, sandboxes for isolated code execution (Modal, Daytona, Deno), or combine multiple backends with composite routing. You can also implement your own custom backend.

Subagent spawning

A built-in 
task
 tool enables agents to spawn specialized subagents for context isolation. This keeps the main agent’s context clean while still going deep on specific subtasks.

Long-term memory

Extend agents with persistent memory across threads using LangGraph’s Memory Store. Agents can save and retrieve information from previous conversations.

Human-in-the-loop

Configure human approval for sensitive tool operations using LangGraph’s interrupt capabilities. Control which tools require confirmation before execution.

Skills

Extend agents with reusable skills that provide specialized workflows, domain knowledge, and custom instructions.

Smart defaults

Ships with opinionated system prompts that teach the model how to use its tools effectively — plan before acting, verify work, and manage context. Customize or replace the defaults as needed.

​

Get started

SDK Quickstart

Build your first deep agent

Customization

Learn about customization options for the SDK

Models

Configure models and providers

Backends

Choose and configure pluggable filesystem backends

Sandboxes

Execute code in isolated environments

Human-in-the-loop

Configure approval for sensitive operations

CLI

Use the Deep Agents CLI

ACP

Use deep agents in code editors via ACP

Reference

See the 
deepagents
 API reference

Edit this page on GitHub or file an issue.

Connect these docs to Claude, VSCode, and more via MCP for real-time answers.

Was this page helpful?

YesNo

Quickstart

Next

⌘I

Docs by LangChain home page
githubxlinkedinyoutube

Resources
ForumChangelogLangChain AcademyTrust Center

Company
HomeAboutCareersBlog

githubxlinkedinyoutube

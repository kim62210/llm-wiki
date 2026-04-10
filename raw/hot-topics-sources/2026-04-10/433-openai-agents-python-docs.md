---
title: OpenAI Agents SDK
source_url: https://openai.github.io/openai-agents-python
final_url: https://openai.github.io/openai-agents-python/
status: 200
content_type: text/html; charset=utf-8
topics: [OpenAI Agents SDK]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:27.591447+00:00
---

# OpenAI Agents SDK

## 원본 URL

https://openai.github.io/openai-agents-python

## 추출 본문

OpenAI Agents SDK

 Skip to content
 

 OpenAI Agents SDK
 

 
 Intro
 
 

 English
 

 日本語
 

 한국어
 

 简体中文
 

 Initializing search
 

 openai-agents-python
 

 OpenAI Agents SDK
 

 openai-agents-python
 

 Intro
 
 
 Intro
 
 
 Table of contents
 

 Why use the Agents SDK
 

 Installation
 

 Hello world example
 

 Start here
 

 Choose your path
 

 Quickstart
 
 

 Configuration
 
 

 Documentation
 
 
 Documentation
 

 Agents
 
 

 Models
 
 

 Tools
 
 

 Guardrails
 
 

 Running agents
 
 

 Streaming
 
 

 Agent orchestration
 
 

 Handoffs
 
 

 Results
 
 

 Human-in-the-loop
 
 

 Sessions
 
 
 Sessions
 

 Sessions
 
 

 SQLAlchemy sessions
 
 

 Advanced SQLite sessions
 
 

 Encrypted sessions
 
 

 Context management
 
 

 Usage
 
 

 Model context protocol (MCP)
 
 

 Tracing
 
 

 Realtime agents
 
 
 Realtime agents
 

 Quickstart
 
 

 Realtime transport
 
 

 Realtime agents guide
 
 

 Voice agents
 
 
 Voice agents
 

 Quickstart
 
 

 Pipelines and workflows
 
 

 Tracing
 
 

 Agent visualization
 
 

 REPL utility
 
 

 Examples
 
 

 Release process/changelog
 
 

 API Reference
 
 
 API Reference
 

 Agents
 
 
 Agents
 

 Agents module
 
 

 Agents
 
 

 Runner
 
 

 Run Config
 
 

 Run State
 
 

 Responses WebSocket Session
 
 

 Run Error Handlers
 
 

 Memory
 
 

 repl
 
 

 Tools
 
 

 Tool Context
 
 

 Results
 
 

 Streaming events
 
 

 Handoffs
 
 

 Lifecycle
 
 

 Items
 
 

 Run context
 
 

 Usage
 
 

 Exceptions
 
 

 Guardrails
 
 

 Prompts
 
 

 Model settings
 
 

 Strict Schema
 
 

 Tool Guardrails
 
 

 Computer
 
 

 Agent output
 
 

 Function schema
 
 

 Model interface
 
 

 OpenAI Chat Completions model
 
 

 OpenAI Responses model
 
 

 OpenAI Provider
 
 

 Multi Provider
 
 

 MCP Servers
 
 

 MCP Util
 
 

 Manager
 
 

 Tracing
 
 
 Tracing
 

 Tracing module
 
 

 Creating traces/spans
 
 

 Traces
 
 

 Spans
 
 

 Processor interface
 
 

 Processors
 
 

 Scope
 
 

 Setup
 
 

 Span data
 
 

 Util
 
 

 Realtime
 
 
 Realtime
 

 RealtimeAgent
 
 

 RealtimeRunner
 
 

 RealtimeSession
 
 

 Realtime Events
 
 

 Realtime Configuration
 
 

 Model
 
 

 Voice
 
 
 Voice
 

 Pipeline
 
 

 Workflow
 
 

 Input
 
 

 Result
 
 

 Pipeline Config
 
 

 Events
 
 

 Exceptions
 
 

 Model
 
 

 Utils
 
 

 OpenAIVoiceModelProvider
 
 

 OpenAI STT
 
 

 OpenAI TTS
 
 

 Extensions
 
 
 Extensions
 

 Handoff filters
 
 

 Handoff prompt
 
 

 Third-party adapters
 
 
 Third-party adapters
 

 Any-LLM model
 
 

 Any-LLM provider
 
 

 LiteLLM model
 
 

 LiteLLM provider
 
 

 Tool Output Trimmer
 
 

 SQLAlchemySession
 
 

 Async Sqlite Session
 
 

 RedisSession
 
 

 DaprSession
 
 

 EncryptedSession
 
 

 AdvancedSQLiteSession
 
 

 Table of contents
 

 Why use the Agents SDK
 

 Installation
 

 Hello world example
 

 Start here
 

 Choose your path
 

OpenAI Agents SDK

The OpenAI Agents SDK enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, Swarm. The Agents SDK has a very small set of primitives:

Agents, which are LLMs equipped with instructions and tools

Agents as tools / Handoffs, which allow agents to delegate to other agents for specific tasks

Guardrails, which enable validation of agent inputs and outputs

In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real-world applications without a steep learning curve. In addition, the SDK comes with built-in tracing that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.

Why use the Agents SDK

The SDK has two driving design principles:

Enough features to be worth using, but few enough primitives to make it quick to learn.

Works great out of the box, but you can customize exactly what happens.

Here are the main features of the SDK:

Agent loop: A built-in agent loop that handles tool invocation, sends results back to the LLM, and continues until the task is complete.

Python-first: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.

Agents as tools / Handoffs: A powerful mechanism for coordinating and delegating work across multiple agents.

Guardrails: Run input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass.

Function tools: Turn any Python function into a tool with automatic schema generation and Pydantic-powered validation.

MCP server tool calling: Built-in MCP server tool integration that works the same way as function tools.

Sessions: A persistent memory layer for maintaining working context within an agent loop.

Human in the loop: Built-in mechanisms for involving humans across agent runs.

Tracing: Built-in tracing for visualizing, debugging, and monitoring workflows, with support for the OpenAI suite of evaluation, fine-tuning, and distillation tools.

Realtime Agents: Build powerful voice agents with 
gpt-realtime-1.5
, automatic interruption detection, context management, guardrails, and more.

Installation

pipinstallopenai-agents

Hello world example

fromagentsimportAgent,Runneragent=Agent(name="Assistant",instructions="You are a helpful assistant")result=Runner.run_sync(agent,"Write a haiku about recursion in programming.")print(result.final_output)# Code within the code,# Functions calling themselves,# Infinite loop's dance.

(If running this, ensure you set the 
OPENAI_API_KEY
 environment variable)

exportOPENAI_API_KEY=sk-...

Start here

Build your first text-based agent with the Quickstart.

Then decide how you want to carry state across turns in Running agents.

If you are deciding between handoffs and manager-style orchestration, read Agent orchestration.

Choose your path

Use this table when you know the job you want to do, but not which page explains it.
GoalStart hereBuild the first text agent and see one complete runQuickstartAdd function tools, hosted tools, or agents as toolsToolsDecide between handoffs and manager-style orchestrationAgent orchestrationKeep memory across turnsRunning agents and SessionsUse OpenAI models, websocket transport, or non-OpenAI providersModelsReview outputs, run items, interruptions, and resume stateResultsBuild a low-latency voice agent with 
gpt-realtime-1.5
Realtime agents quickstart and Realtime transportBuild a speech-to-text / agent / text-to-speech pipelineVoice pipeline quickstart

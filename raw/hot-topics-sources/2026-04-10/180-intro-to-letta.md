---
title: Intro to Letta | Letta Docs
source_url: https://docs.letta.com/concepts/memgpt
final_url: https://docs.letta.com/guides/get-started/intro
status: 200
content_type: text/html; charset=utf-8
topics: [Letta (MemGPT) Stateful Agent Runtime]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:51.995480+00:00
---

# Intro to Letta | Letta Docs

## 원본 URL

https://docs.letta.com/concepts/memgpt

## 추출 본문

Intro to Letta | Letta DocsSkip to content

 Letta Docs 

SearchCtrlK

Auto

Light

Dark

Sign up

Guides

API Reference

Letta Code

Guides

API Reference

Letta Code

Letta Code ↗

Letta Code SDK ↗

Get started
Intro to Letta

Quickstart (API)

Models

Pricing

Core concepts
Stateful agents

Messages
Message types

Streaming

Image inputs

Structured outputs

Long-running executions

Compaction

Conversations

Memory
Memory blocks

Shared memory

Archival memory

Context hierarchy

Tools
Client tools

Built-in tools

Server tools

Human-in-the-loop

MCP tools

Skills ↗

Filesystem

AgentFile (.af)

Docker server
Server setup

Model providers

Tutorials
First steps
Overview

Your first Letta agent

Talk to your PDF

Memory
Shared memory blocks

Retrieval
Overview

Agentic RAG with Letta

Simple RAG with Letta

Multi-agent patterns
Overview

Supervisor-worker

Round-robin

Parallel execution

Producer-reviewer

Hierarchical teams

Advanced
Overview

Custom RAG pipelines

Customer-specific agents with Letta API

Activate voice mode

Integrations
Overview

Build a Multi-User Chatbot with Letta, Supabase, and Next.js

Create a Discord bot

Integrating external memory storage with Letta

n8n workflow integration

Building a Full-Stack AI Agent Application with Letta and Supabase

Letta Telegram bot

Connecting Zapier and Letta

Experimental & legacy
Sleep-time agents

Scheduling

Voice agents
Voice agents

LiveKit integration

Vapi integration

Development tools
Letta ADE
ADE overview

Letta Desktop (legacy)

Community tools
lettactl

Letta Snippets

Testing & evals
Letta Evals

Getting started

Core concepts
Core concepts

Suites

Datasets

Targets

Graders

Extractors

Gates

Configuration
Suite YAML reference

Graders
Tool Graders

Rubric Graders

Multi-metric evaluation

Extractors
Built-in extractors

Custom extractors

Advanced
Custom Graders

Multi-turn conversations

CLI reference
CLI commands

Results & metrics
Understanding results

Troubleshooting
Troubleshooting

Templates & versioning
Intro to templates

Template versioning

Memory variables

Role-based access control

Discord

Auto

Light

Dark

On this page

Overview

Get started

For developers

Frequently asked questions

On this page

Overview

Get started

For developers

Frequently asked questions

Get started

Intro to Letta

Copy Markdown

Open in Claude

Open in ChatGPT

Open in Cursor

Copy Markdown

View as Markdown

Intro to Letta

Creating stateful agents that can remember and learn

Letta is the platform for building stateful agents that remember, learn, and improve over time.
Letta agents are deeply personalized and form living memories about themselves, the world they live in, you, and your users.

Get started
Section titled “Get started”

The fastest way to try Letta is via Letta Code (in your terminal) or chat.letta.com (in your browser).

Letta CodeMemory-first coding agent in your terminal. Get started in 30 seconds.

Letta ChatChat with a personalized agent that remembers.

For developers
Section titled “For developers”

Turn your personal stateful agents into production applications.

Letta Code SDKBuild TypeScript apps on top of Letta Code agents.

Client SDKsTypeScript and Python clients for the Letta API.

Frequently asked questions
Section titled “Frequently asked questions”

For more questions, visit the Letta Discord server.

How can I build a custom agent?
The fastest way to build a custom personal agent is to download Letta Code. You can customize your agent’s behavior by modifying its memory, and extend its abilities by adding skills.

If you want a ready-to-go Letta Code setup that has common skills for Discord, WhatsApp, Telegram, browser use and more pre-installed, check out the LettaBot GitHub repo.
Can I use Letta Code through a UI (not the terminal)?
Yes - the Letta Code SDK allows you to build your own UIs on top of Letta Code agents. See the Letta OSS UI repo for an Electron app example, and LettaBot for an example of interacting with a Letta Code agent through native messaging apps like Telegram (both built on the Letta Code SDK).
Which Letta SDK/API should I use?
We recommend most developers build on the Letta Code SDK, which includes rich support for agent skills and local tool execution / computer use (
Bash
, 
Grep
, etc). If you are building an agent that does not require skills or local tool execution (e.g. a chatbot), consider building directly on the Letta API instead.
What’s the difference between Letta Code SDK and the Letta API?
The Letta Code SDK is built on top of the core Letta API, and adds pre-built support for skills and local / client-side tool exeuction.
ProductUse viaFunctionMost similar toLettaBotTelegram, WhatsApp, Discord, etc.Adds cron jobs / heartbeats and bundled skills to Letta CodeOpenClaw (formerly ClawdBot, MoltBot)Letta CodeTerminal / CLI, GitHub ActionLocal tool execution and pre-built computer use toolsClaude Code, Codex CLI, OpenCodeLetta Code SDKTypeScript onlySame agent harness as Letta Code, but accessible via TypeScriptClaude Agent SDKLetta APITypeScript, Python, or RESTA stateful LLM API that connects memory to any model providerOpenAI Responses API

Previous

Letta Code SDK ↗

Next

Quickstart (API)

Create your first stateful agent and send it a message

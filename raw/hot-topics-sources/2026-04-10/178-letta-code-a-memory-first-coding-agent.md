---
title: Letta Code: A Memory-First Coding Agent  | Letta
source_url: https://www.letta.com/blog/letta-code
final_url: https://www.letta.com/blog/letta-code
status: 200
content_type: text/html; charset=utf-8
topics: [Letta (MemGPT) Stateful Agent Runtime]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:50.209223+00:00
---

# Letta Code: A Memory-First Coding Agent  | Letta

## 원본 URL

https://www.letta.com/blog/letta-code

## 추출 본문

Letta Code: A Memory-First Coding Agent | Letta

Research

Product

Letta Code

Run agents locally inside your terminal

Letta API

Build agents into your apps with our API

Resources

Blog

Learn about product and research updates

Customer Stories

Read about Letta in production

Demos

See Letta in action

Model Leaderboard

Understand which LLMs work best

Developer Community

Join the Letta community on Discord

Company

About us

Learn about our mission and team

Careers

Join our team to work on open AI

Contact us

Get in touch

Pricing

Letta Developer Platform

Use the Letta API to build agents that can actually remember and learn about your users over time. Open source, production ready, and fully model-agnostic.

Letta Code

Letta Code is a memory-first coding harness, built on top of the Letta API. Instead of working in independent sessions, you work with a persisted agent that learns over time and is portable across models.

Light

Dark

11.3K

Menu

Close

19K
DocsSign In

Light

Dark

Product

Letta Code: A Memory-First Coding Agent

December 16, 2025

Letta Code is a memory-first coding agent, designed for working with agents that learn over time. When working with coding agents today, interactions happen in independent sessions. Letta Code is built around long-lived agents that persist across sessions and improve with use. Rather than working in independent sessions, each session is tied to a persisted agent that learns. Letta Code is also the #1 model-agnostic OSS harness on TerminalBench, and achieves comparable performance to harnesses built by LLM providers (Claude Code, Gemini CLI, Codex CLI) on their own models.

Continual Learning & Memory for Coding Agents 

Agents today accumulate valuable experience: they receive the user’s preferences and feedback, review significant parts of code, and observe the outcomes of taking actions like running scripts or commands. Yet today this experience is largely wasted. Letta agents learn from experience through agenticcontext engineering, long-term memory, and skill learning. The more you work with an agent, the more context and memory it accumulates, and the better it becomes. 

Memory Initialization 

When you get started with Letta Code, you can run an `/init` command to encourage your agent to learn about your existing project. This will trigger your agent to run deep research on your local codebase, forming memories and rewriting its system prompt (through memory blocks) as it learns.

‍

‍

Your agent will continue to learn automatically, but you can also explicitly trigger your agent to reflect and learn with the `/remember` command. 

Skill Learning 

Many tasks that we work on with coding agents are repeated or follow similar patterns - for example API patterns or running DB migrations. Once you’ve worked with an agent to coach it through a complex task, you can trigger it to learn a skill from its experience, so the agent itself or other agents can reference the skill for similar tasks in the future. Skill learning can dramatically improve performance on future similar tasks, as we showed with recent results on TerminalBench.

On our team, some skills that agents have contributed (with the help of human engineers) are: 

Generating DB migrations on schema changes

Creating PostHog dashboards with the PostHog CLI

Best practices for API changes   

Since skills are simply 
.md
 files, they can be managed in git repositories for versioning - or even used by other coding agents that support skills. 

Persisted State

Agents can also lookup past conversations (or even conversations of other agents) through the Letta API. The builtin `/search` command allows you to easily search through messages, so you can find the agent you worked on something with. The Letta API supports vector, full-text, and hybrid search over messages and available tools.

Letta Code is the #1 model-agnostic OSS coding harness 

Letta Code adds statefulness and learning to coding agents, but is the #1 model-agnostic, OSS harness on Terminal-Bench. Letta Code’s performance is comparable to provider-specific harnesses (Gemini CLI, Claude Code, Codex) across model providers, and significantly outperforms the previous leading model-agnostic harness, Terminus 2.

This means that even without memory, you can expect Letta Code agents to work just as well with a frontier model as they would with a specific harness built by the model provider. 

Getting Started with Letta Code 

To try out Letta Code, you can install it with 
npm install -g @letta-ai/letta-code
 (see the full documentation).

Back

Twitter/X

LinkedIn

Company

Company announcements, partnerships

Mar 16, 2026

Letta's next phase

Letta builds agents that learn. Agents with persistent memory, real computer access, and the infrastructure to improve from their own lived experience and work. Letta Code is the runtime that brings these together: git-backed memory, skills, subagents, and deployment that works across every model provider.

Jul 7, 2025

Agent Memory: How to Build Agents that Learn and Remember

Traditional LLMs operate in a stateless paradigm—each interaction exists in isolation, with no knowledge carried forward from previous conversations. Agent memory solves this problem.

Jul 3, 2025

Anatomy of a Context Window: A Guide to Context Engineering

As AI agents become more sophisticated, understanding how to design and manage their context windows (via context engineering) has become crucial for developers.

May 14, 2025

Memory Blocks: The Key to Agentic Context Management

Memory blocks offer an elegant abstraction for context window management. By structuring the context into discrete, functional units, we can give LLM agents more consistent, usable memory.

Feb 13, 2025

RAG is not Agent Memory

Although RAG provides a way to connect LLMs and agents to more data than what can fit into context, traditional RAG is insufficient for building agent memory.

Feb 6, 2025

Stateful Agents: The Missing Link in LLM Intelligence

Introducing “stateful agents”: AI systems that maintain persistent memory and actually learn during deployment, not just during training.

Nov 14, 2024

The AI agents stack

Understanding the AI agents stack landscape.

Nov 7, 2024

New course on Letta with DeepLearning.AI

DeepLearning.AI has released a new course on agent memory in collaboration with Letta.

Sep 23, 2024

Announcing Letta

We are excited to publicly announce Letta.

Sep 23, 2024

MemGPT is now part of Letta

The MemGPT open source project is now part of Letta.

Product

Release notes, feature announcements

Apr 6, 2026

Introducing the Letta Code app

Today we’re launching the Letta Code app, a new way to interact with deeply personalized agents that learn over time and work locally on your machine.

Mar 4, 2026

Remote Environments for Letta Code

Using remote environments, you can message an agent working on your laptop from your phone. 

Jan 21, 2026

Conversations: Shared Agent Memory across Concurrent Experiences

The Conversations API allows you to build agents that can maintain shared memory across parallel experiences with users

Dec 1, 2025

Programmatic Tool Calling with any LLM

The Letta API now supports programmatic tool calling for any LLM model, enabling agents to generate their own workflows.

Oct 23, 2025

Letta Evals: Evaluating Agents that Learn

Introducing Letta Evals: an open-source evaluation framework for systematically testing stateful agents.

Oct 14, 2025

Rearchitecting Letta’s Agent Loop: Lessons from ReAct, MemGPT, & Claude Code

Introducing Letta's new agent architecture, optimized for frontier reasoning models.

Sep 30, 2025

Introducing Claude Sonnet 4.5 and the memory omni-tool in Letta

Letta agents can now take full advantage of Sonnet 4.5’s advanced memory tool capabilities to dynamically manage their own memory blocks.

Jul 24, 2025

Introducing Letta Filesystem

Today we're announcing Letta Filesystem, which provides an interface for agents to organize and reference content from documents like PDFs, transcripts, documentation, and more.

Apr 17, 2025

Announcing Letta Client SDKs for Python and TypeScript

We've releasing new client SDKs (support for TypeScript and Python) and upgraded developer documentation

Apr 2, 2025

Agent File

Introducing Agent File (.af): An open file format for serializing stateful agents with persistent memory and behavior.

Jan 15, 2025

Introducing the Agent Development Environment

Introducing the Letta Agent Development Environment (ADE): Agents as Context + Tools

Dec 13, 2024

Letta v0.6.4 release

Letta v0.6.4 adds Python 3.13 support and an official TypeScript SDK.

Nov 6, 2024

Letta v0.5.2 release

Letta v0.5.2 adds tool rules, which allows you to constrain the behavior of your Letta agents similar to graphs.

Oct 23, 2024

Letta v0.5.1 release

Letta v0.5.1 adds support for auto-loading entire external tool libraries into your Letta server.

Oct 14, 2024

Letta v0.5 release

Letta v0.5 adds dynamic model (LLM) listings across multiple providers.

Oct 3, 2024

Letta v0.4.1 release

Letta v0.4.1 adds support for Composio, LangChain, and CrewAI tools.

Research

Sleep-time compute, anatomy of a context window

Apr 2, 2026

Context Constitution

Today we are releasing the Context Constitution: a set of principles governing how AI agents manage context to learn from experience.

Feb 12, 2026

Introducing Context Repositories: Git-based Memory for Coding Agents

We're introducing Context Repositories, a rebuild of how memory works in Letta Code based on programmatic context management and git-based versioning.

Dec 11, 2025

Continual Learning in Token Space

At Letta, we believe that learning in token space is the key to building AI agents that truly improve over time. Our interest in this problem is driven by a simple observation: agents that can carry their memories across model generations will outlast any single foundation model.

Dec 2, 2025

Skill Learning: Bringing Continual Learning to CLI Agents

Today we’re releasing Skill Learning, a way to dynamically learn skills through experience. With Skill Learning, agents can use their past experience to actually improve, rather than degrade, over time.

Nov 7, 2025

Can Any Model Use Skills? Adding Skills to Context-Bench

Today we're releasing Skill Use, a new evaluation suite inside of Context-Bench that measures how well models discover and load relevant skills from a library to complete tasks.

Oct 30, 2025

Context-Bench: Benchmarking LLMs on Agentic Context Engineering

We are open-sourcing Context-Bench, which evaluates how well language models can chain file operations, trace entity relationships, and manage multi-step information retrieval in long-horizon tasks.

Aug 27, 2025

Introducing Recovery-Bench: Evaluating LLMs' Ability to Recover from Mistakes

We're excited to announce Recovery-Bench, a benchmark and evaluation method for measuring how well agents can recover from errors and corrupted states.

Aug 12, 2025

Benchmarking AI Agent Memory: Is a Filesystem All You Need?

Letta Filesystem scores 74.0% of the LoCoMo benchmark by simply storing conversational histories in a file, beating out specialized memory tool libraries.

Aug 5, 2025

Building the #1 open source terminal-use agent using Letta

We built the #1 open-source agent for terminal use, achieving 42.5% overall score on Terminal-Bench ranking 4th overall and 2nd among agents using Claude 4 Sonnet.

May 29, 2025

Letta Leaderboard: Benchmarking LLMs on Agentic Memory

We're excited to announce the Letta Leaderboard, a comprehensive benchmark suite that evaluates how effectively LLMs manage agentic memory. 

Apr 21, 2025

Sleep-time Compute

Sleep-time compute is a new way to scale AI capabilities: letting models "think" during downtime. Instead of sitting idle between tasks, AI agents can now use their "sleep" time to process information and form new connections by rewriting their memory state.

in this article

This is some text inside of a div block.

Product

What is Letta
CustomersResearchNews

DEVELOPERS

GitHub

11.9K

DocumentationCommunityDemos

Company

About usOpen positionsPrivacy policyTerms of service

Newsletter

Thank you, you are subscribed

Oops! Something went wrong while submitting the form.

Follow Letta

Follow Letta

Follow Letta

Follow Letta

Follow Letta

Follow Letta

GitHub

Discord

Twitter/X

Bluesky

Instagram

YouTube

LinkedIn

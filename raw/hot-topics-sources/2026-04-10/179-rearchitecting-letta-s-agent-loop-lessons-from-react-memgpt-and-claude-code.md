---
title: Rearchitecting Letta’s Agent Loop: Lessons from ReAct, MemGPT, & Claude Code  | Letta
source_url: https://www.letta.com/blog/letta-v1-agent
final_url: https://www.letta.com/blog/letta-v1-agent
status: 200
content_type: text/html; charset=utf-8
topics: [Letta (MemGPT) Stateful Agent Runtime]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:50.435653+00:00
---

# Rearchitecting Letta’s Agent Loop: Lessons from ReAct, MemGPT, & Claude Code  | Letta

## 원본 URL

https://www.letta.com/blog/letta-v1-agent

## 추출 본문

Rearchitecting Letta’s Agent Loop: Lessons from ReAct, MemGPT, & Claude Code | Letta

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

Rearchitecting Letta’s Agent Loop: Lessons from ReAct, MemGPT, & Claude Code

October 14, 2025

A common definition for agents is that they're simply a loop that calls an LLM and executes a tool. In other words (as Simon Willison defines an agent): 

An LLM agent runs tools in a loop to achieve a goal. 

But not all loops are created equal. The underlying design of the agent loop fundamentally shapes how your agent behaves: when it decides to reason, when to terminate, and whether it gets stuck in infinite loops or exits prematurely. 

What is agent architecture? 

The performance of your agents depends not just on the model and prompts, but the agent architecture: exactly how the LLM is invoked in a loop to reason and take actions. At each iteration, the agent must decide to do one or more of the following:

Call a tool (e.g., an MCP tool) or send a message

Reason (spend compute cycles thinking)

Terminate (exit the loop)

Each of these decisions can be controlled by the LLM itself (e.g. the LLM deciding to reason) or by the agent architecture controlling invocations to the LLM. Historically, LLMs could only specify tool calls or assistant messages explicitly, so additional logic from the agent architecture was necessary to trigger reasoning or make termination decisions. While modern LLMs often have reasoning capabilities built-in, they still lack a built-in way to determine whether to continue executing — this remains the responsibility of the agent architecture.

Early agent architectures: ReAct and MemGPT

ReAct: Sequential reasoning and actions

ReAct was an early and influential LLM-based agent that combined reasoning and actions in sequence to achieve tasks. In the ReAct architecture, the LLM would be prompted to generate (in each response) a thought, an action, and (optionally) a token indicating the loop should be terminated.

Since the ReAct architecture pre-dated tool calling and native reasoning in LLMs, generation of actions, thoughts, and stop tokens were all done through formatted prompts.

MemGPT: The first stateful agent

MemGPT was another early agent architecture and notably the first example of a stateful agent with persistent memory. MemGPT's architecture was built on top of early LLM tool calling, making every action a tool call (including assistant message, via a special 
send_message
 tool).

This design enabled the tool schemas to manage reasoning and control flow by injecting special keyword arguments into tools:

thinking
: The model's reasoning or chain-of-thought (similar to “thoughts” in ReAct)

request_heartbeat
: Request tool chaining to continue execution

Each time the LLM invoked a tool, it would also be triggered to reason and determine whether the tool chain should continue. This allowed for agentic tool chaining and chain-of-thought reasoning before it was built into base models.

By default, 
request_heartbeat
 is set to 
False
 in MemGPT, so agents terminate by default rather than continue by default as in ReAct. The tool-based architecture also enabled powerful features to be built on top of the MemGPT agent loop such as tool rules, where tool calling patterns could be forced to follow specific constraints. However, MemGPT’s reliance on tool calling meant that only models that were capable of reliable tool-calling could work with MemGPT.

Although both ReAct and MemGPT are technically just “LLMs in a loop”, the way the underlying LLM is used differs significantly and results in different agent behaviors. 

Agent architectures today: Letta, Claude Agents SDK, and OpenAI Codex

Agents are far more pervasive today than in 2023 when MemGPT was first released. Most models now support tool calling and native reasoning (reasoning tokens generated “directly” by the model rather than through prompting). LLM providers themselves now offer pre-built agents like OpenAI Codex and Claude Agents SDK, and have trained their models to be optimized to their own preferred agent architecture design choices.

Today's LLMs are also trained to be adept at agentic patterns such as multi-step tool calling, reasoning interleaved within tool calling, and self-directed termination conditions. As models become more heavily post-trained on new agentic patterns, agent architectures benefit from converging to match these patterns — in other words, staying "in-distribution" relative to the data the LLM was trained on.

Letta's new agent architecture

At Letta, we're transitioning from the previous MemGPT-style architecture to a new Letta V1 architecture (
letta_v1_agent
) that follows these modern patterns. In this architecture, 
heartbeats
 and the 
send_message
 tool are deprecated. Only native reasoning and direct assistant message generations from the models are supported. 

What this means in practice

We’ve found the
letta_v1_agent
 architecture significantly improves performance for the latest models like GPT-5 and Claude 4.5 Sonnet, with other benefits such as: 

Full support for native reasoning: The new architecture uses Responses API under the hood for OpenAI, and handles encrypted reasoning across providers. This allows models to fully leverage their reasoning capabilities to achieve frontier performance. 

Compatibility with any LLM: Tool calling support is no longer a requirement to connect an LLM to Letta. 

Simpler base system prompt: Understanding of the agentic control loop is baked into the underlying models. 

At the same time, there are some downsides compared to the previous MemGPT architecture: 

No direct support for prompted reasoning: Non-reasoning models (e.g., GPT-5 mini, GPT-4o mini) will no longer generate reasoning, and developers cannot mutate the native reasoning state or pass reasoning traces across different models (from closed APIs that encrypt the reasoning). 

No heartbeats: Agents no longer understand the concept of heartbeats (unless implemented manually). For repeatedly triggering agents to run independently (e.g., processing time or sleep-time compute), you'll need custom prompting to explain this environment to the agent

More limited tool rules: Tool rules cannot be applied to 
AssistantMessage
, as it is no longer a tool call.  

The reasoning token dilemma

Reasoning is now built into models themselves, but the major frontier AI providers (OpenAI, Anthropic, Google Gemini) actively prevent developers from accessing and controlling this reasoning. One advantage of prompted reasoning tokens is ownership: you can see them, modify them, and send them to any model. In contrast, “native reasoning” tokens are often not transparent (the developer can only see a summary), and immutable (the developer is not allowed to modify them without voiding the API request). The performance difference between native reasoning and prompted reasoning remains unclear and likely varies by use case.

We'll continue supporting the original MemGPT agent architecture, but recommend using the new Letta V1 architecture for the latest reasoning models like GPT-5 and Claude 4.5 Sonnet.

Conclusion

Fully leveraging the underlying model capabilities to achieve frontier performance requires careful architecting of the underlying agentic loop and agent architecture, and adapting them alongside evolutions in model development. To see what agents are capable of today, try the latest agent architecture on the Letta Platform. 

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

Dec 16, 2025

Letta Code: A Memory-First Coding Agent

Introducing Letta Code, a memory-first coding agent. Letta Code is the #1 model-agnostic open source agent on the leading AI coding benchmark Terminal-Bench.

Dec 1, 2025

Programmatic Tool Calling with any LLM

The Letta API now supports programmatic tool calling for any LLM model, enabling agents to generate their own workflows.

Oct 23, 2025

Letta Evals: Evaluating Agents that Learn

Introducing Letta Evals: an open-source evaluation framework for systematically testing stateful agents.

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

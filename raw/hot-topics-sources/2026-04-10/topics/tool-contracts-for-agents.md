---
title: Tool Contracts & Writing Tools for Agents
section: Harness Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Tool Contracts & Writing Tools for Agents

## 기존 큐레이션 요약

- 정의: 결정론적 시스템과 비결정론적 에이전트 사이의 계약으로 툴을 설계하는 에이전트 우선 설계 철학.
- 왜 중요한가: Anthropic의 "Writing effective tools for agents" 가이드라인과 2026년 2월 Managed Agents 블로그의 `execute(name, input) → string` 계약("the harness left the container")이 tool design의 기본 언어가 됐고, Cursor 3.0이 Await tool·screenshot-based clicking을 도입하면서 "에이전트에게 맞는 툴 API는 사람용 API와 다르다"는 명제가 보편화됐다.

## 개별 원문 수집 스냅샷

### Writing effective tools for AI agents — with agents

- URL: https://www.anthropic.com/engineering/writing-tools-for-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/025-writing-effective-tools-for-agents.md`
- 수집 제목: Writing effective tools for AI agents—using AI agents \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Writing effective tools for agents — with agents Published Sep 11, 2025 Agents are only as effective as the tools we give them. We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself. The Model Context Protocol (MCP) can empower LLM agents with potentially hundreds of tools to solve real-world tasks. But how do we make those tools maximally effective? In this post, we describe our most effective techniques for improving performance in a variety of agentic AI systems1. We begin by covering how you can: Build and test prototypes of your tools Create and run comprehensive evaluations of you

### Scaling Managed Agents: Decoupling the brain from the hands

- URL: https://www.anthropic.com/engineering/managed-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md`
- 수집 제목: Scaling Managed Agents: Decoupling the brain from the hands \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Scaling Managed Agents: Decoupling the brain from the hands Harnesses encode assumptions that go stale as models improve. Managed Agents—our hosted service for long-horizon agent work—is built around interfaces that stay stable as harnesses change. Get started with Claude Managed Agents by following our docs. A running topic on the Engineering Blog is how to build effective agents and design harnesses for long-running work. A common thread across this work is that harnesses encode assumptions about what Claude can’t do on its own. However, those assumptions need to be frequently questioned because they can go stale as models improve. As just one example, in prior work we 

### Claude Agent SDK Overview

- URL: https://code.claude.com/docs/en/agent-sdk/overview
- raw snapshot: `raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md`
- 수집 제목: Agent SDK overview - Claude Code Docs

Agent SDK overview - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Agent SDK Agent SDK overview Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Agent SDK Overview Quickstart Core concepts How the agent loop works Use Claude Code features Work with sessions Input and output Streaming Input Handle approvals and user input Stream responses in real-time Get structured output from agents Extend with tools Give Claude custom tools Connect to external tools with MCP Scale to many tools with tool search Subagents in the SDK Customize behavior Modifying system prompts Slash Commands in the S

### Cursor 3.0 Changelog

- URL: https://cursor.com/changelog/3-0
- raw snapshot: `raw/hot-topics-sources/2026-04-10/057-cursor-3-0-changelog.md`
- 수집 제목: New Cursor Interface · Cursor

New Cursor Interface · Cursor Skip to content Cursor Product↓ Agents Code Review Cloud ↗ Tab CLI Marketplace ↗ Enterprise Pricing Resources↓ Changelog Blog Docs Community Help ↗ Workshops Forum ↗ Careers Product → Enterprise Pricing Resources → Sign inContactContact salesDownload 3.0Apr 2, 2026 · Changelog Changelog New Cursor Interface Cursor 3 is now available. #Agents Window The new Cursor interface allows you to run many agents in parallel across repos and environments: locally, in worktrees, in the cloud, and on remote SSH. It's simpler, more powerful, and centered around agents, while keeping the depth of a development environment. To try the Agents Window, upgrade Cursor and type Cmd+Shift+P -> Agents Window . You can switch back to the IDE anytime, or have both open simultaneously.

### Chat modes (Aider)

- URL: https://aider.chat/docs/usage/modes.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/065-chat-modes.md`
- 수집 제목: Chat modes | aiderMenuExpand(external link)DocumentSearchCopyCopied

Chat modes | aiderSkip to main contentMenuExpand(external link)DocumentSearchCopyCopied aider Installation Optional steps Aider with docker GitHub Codespaces Replit Usage Tips In-chat commands Chat modes Tutorial videos Voice-to-code with aider Images & web pages Prompt caching Aider in your IDE Notifications Aider in your browser Specifying coding conventions Copy/paste with web chat Linting and testing Editing config & text files Connecting to LLMs OpenAI Anthropic Gemini GROQ LM Studio xAI Azure Cohere DeepSeek Ollama OpenAI compatible APIs OpenRouter GitHub Copilot Vertex AI Amazon Bedrock Other LLMs Model warnings Configuration API Keys Options reference YAML config file Config with .env Editor configuration Reasoning models Advanced model settings Model Aliases Troubleshooting File e

---
title: Subagents & Multi-Agent Orchestration in the Harness
section: Harness Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Subagents & Multi-Agent Orchestration in the Harness

## 기존 큐레이션 요약

- 정의: 메인 세션이 전용 컨텍스트·권한을 가진 서브에이전트에 작업을 위임하는 오케스트레이션 패턴.
- 왜 중요한가: Claude Code가 `/agents`·`.claude/agents/`·`Agent` 툴·`parent_tool_use_id` 필드를 정식화했고, Anthropic 3월 harness 블로그에서 planner-generator-evaluator 3-agent 구조가 long-running 코딩을 가능하게 한 핵심이라고 공개하면서 "GAN-style agent loop" 패턴이 업계 표준 토론거리가 됐다.

## 개별 원문 수집 스냅샷

### Create custom subagents (Claude Code)

- URL: https://code.claude.com/docs/en/sub-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/008-create-custom-subagents.md`
- 수집 제목: Create custom subagents - Claude Code Docs

Create custom subagents - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Agents Create custom subagents Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Agents Create custom subagents Run agent teams Tools and plugins Model Context Protocol (MCP) Discover and install prebuilt plugins Create plugins Extend Claude with skills Automation Automate with hooks Push external events to Claude Run prompts on a schedule Programmatic usage Troubleshooting Troubleshooting On this page Built-in subagents Quickstart: create your first subagent Configure subagents Use the /agents command Choose the 

### Harness design for long-running application development

- URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- raw snapshot: `raw/hot-topics-sources/2026-04-10/011-harness-design-for-long-running-application-development.md`
- 수집 제목: Harness design for long-running application development \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Harness design for long-running application development Published Mar 24, 2026 Harness design is key to performance at the frontier of agentic coding. Here's how we pushed Claude further in frontend design and long-running autonomous software engineering. Written by Prithvi Rajasekaran, a member of our Labs team. Over the past several months I’ve been working on two interconnected problems: getting Claude to produce high-quality frontend designs, and getting it to build complete applications without human intervention. This work originated with earlier efforts on our frontend design skill and long-running coding agent harness, where my colleagues and I were able to improv

### Claude Agent SDK Overview

- URL: https://code.claude.com/docs/en/agent-sdk/overview
- raw snapshot: `raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md`
- 수집 제목: Agent SDK overview - Claude Code Docs

Agent SDK overview - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Agent SDK Agent SDK overview Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Agent SDK Overview Quickstart Core concepts How the agent loop works Use Claude Code features Work with sessions Input and output Streaming Input Handle approvals and user input Stream responses in real-time Get structured output from agents Extend with tools Give Claude custom tools Connect to external tools with MCP Scale to many tools with tool search Subagents in the SDK Customize behavior Modifying system prompts Slash Commands in the S

### Common workflows (Claude Code)

- URL: https://code.claude.com/docs/en/common-workflows
- raw snapshot: `raw/hot-topics-sources/2026-04-10/054-common-workflows.md`
- 수집 제목: Common workflows - Claude Code Docs

Common workflows - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Use Claude Code Common workflows Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Getting started Overview Quickstart Changelog Core concepts How Claude Code works Extend Claude Code Explore the .claude directory Explore the context window Use Claude Code Store instructions and memories Permission modes Common workflows Best practices Platforms and integrations Overview Remote Control Claude Code on the web Claude Code on desktop Chrome extension (beta) Computer use (preview) Visual Studio Code JetBrains IDEs Code revie

### Effective harnesses for long-running agents

- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/041-effective-harnesses-for-long-running-agents.md`
- 수집 제목: Effective harnesses for long-running agents \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Effective harnesses for long-running agents Published Nov 26, 2025 Agents still face challenges working across many context windows. We looked to human engineers for inspiration in creating a more effective harness for long-running agents. As AI agents become more capable, developers are increasingly asking them to take on complex tasks requiring work that spans hours, or even days. However, getting agents to make consistent progress across multiple context windows remains an open problem. The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before. Imagine a software project staffed

---
title: Agent Harnesses for Long-Running Coding Sessions
section: Harness Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Agent Harnesses for Long-Running Coding Sessions

## 기존 큐레이션 요약

- 정의: 컨텍스트 윈도우를 넘어 몇 시간 동안 자율적으로 코딩을 이어가게 하는 에이전트 실행 구조.
- 왜 중요한가: Anthropic이 2025년 11월 "Effective harnesses for long-running agents"에서 initializer + coding agent 2단 구조와 claude-progress.txt 기반 세션 이어받기 패턴을 공개했고, 2026년 3월에는 generator-evaluator 3-agent 구조로 확장한 후속편을 내며 "harness engineering"을 공식 카테고리로 띄웠다.

## 개별 원문 수집 스냅샷

### Effective harnesses for long-running agents

- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/041-effective-harnesses-for-long-running-agents.md`
- 수집 제목: Effective harnesses for long-running agents \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Effective harnesses for long-running agents Published Nov 26, 2025 Agents still face challenges working across many context windows. We looked to human engineers for inspiration in creating a more effective harness for long-running agents. As AI agents become more capable, developers are increasingly asking them to take on complex tasks requiring work that spans hours, or even days. However, getting agents to make consistent progress across multiple context windows remains an open problem. The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before. Imagine a software project staffed

### Harness design for long-running application development

- URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- raw snapshot: `raw/hot-topics-sources/2026-04-10/011-harness-design-for-long-running-application-development.md`
- 수집 제목: Harness design for long-running application development \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Harness design for long-running application development Published Mar 24, 2026 Harness design is key to performance at the frontier of agentic coding. Here's how we pushed Claude further in frontend design and long-running autonomous software engineering. Written by Prithvi Rajasekaran, a member of our Labs team. Over the past several months I’ve been working on two interconnected problems: getting Claude to produce high-quality frontend designs, and getting it to build complete applications without human intervention. This work originated with earlier efforts on our frontend design skill and long-running coding agent harness, where my colleagues and I were able to improv

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

### anthropics/claude-agent-sdk-typescript

- URL: https://github.com/anthropics/claude-agent-sdk-typescript
- raw snapshot: `raw/hot-topics-sources/2026-04-10/044-anthropics-claude-agent-sdk-typescript.md`
- 수집 제목: GitHub - anthropics/claude-agent-sdk-typescript · GitHub

GitHub - anthropics/claude-agent-sdk-typescript · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CAS

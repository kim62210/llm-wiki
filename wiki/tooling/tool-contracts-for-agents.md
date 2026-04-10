---
title: Tool Contracts & Writing Tools for Agents
category: tooling
page_type: concept
tags: [tooling, concept, tool, contracts, for, agents]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/tool-contracts-for-agents.md, raw/hot-topics-sources/2026-04-10/025-writing-effective-tools-for-agents.md, raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md, raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md, raw/hot-topics-sources/2026-04-10/057-cursor-3-0-changelog.md, raw/hot-topics-sources/2026-04-10/065-chat-modes.md]
created: 2026-04-10
updated: 2026-04-10
---
# Tool Contracts & Writing Tools for Agents

결정론적 시스템과 비결정론적 에이전트 사이의 계약으로 툴을 설계하는 에이전트 우선 설계 철학.

## 왜 중요한가

Anthropic의 "Writing effective tools for agents" 가이드라인과 2026년 2월 Managed Agents 블로그의 `execute(name, input) → string` 계약("the harness left the container")이 tool design의 기본 언어가 됐고, Cursor 3.0이 Await tool·screenshot-based clicking을 도입하면서 "에이전트에게 맞는 툴 API는 사람용 API와 다르다"는 명제가 보편화됐다.

## 대표 레퍼런스

- [Writing effective tools for AI agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Cursor 3.0 Changelog](https://cursor.com/changelog/3-0)
- [Chat modes (Aider)](https://aider.chat/docs/usage/modes.html)

## 2026년 4월 큐레이션 요약

- 정의: 결정론적 시스템과 비결정론적 에이전트 사이의 계약으로 툴을 설계하는 에이전트 우선 설계 철학.
- 왜 중요한가: Anthropic의 "Writing effective tools for agents" 가이드라인과 2026년 2월 Managed Agents 블로그의 `execute(name, input) → string` 계약("the harness left the container")이 tool design의 기본 언어가 됐고, Cursor 3.0이 Await tool·screenshot-based clicking을 도입하면서 "에이전트에게 맞는 툴 API는 사람용 API와 다르다"는 명제가 보편화됐다.
- 직접 수집 원문: 5개
- 주요 도메인: anthropic.com×2, code.claude.com×1, cursor.com×1, aider.chat×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/tool-contracts-for-agents.md`

### source별 핵심 신호

- **Writing effective tools for AI agents—using AI agents \ Anthropic** (`anthropic.com`): https://www.anthropic.com/engineering/writing-tools-for-agents
  - 메모: Agents are only as effective as the tools we give them. We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself.
- **Scaling Managed Agents: Decoupling the brain from the hands \ Anthropic** (`anthropic.com`): https://www.anthropic.com/engineering/managed-agents
  - 메모: Harnesses encode assumptions that go stale as models improve. Managed Agents—our hosted service for long-horizon agent work—is built around interfaces that stay stable as harnesses change.
- **Agent SDK overview - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/agent-sdk/overview
  - 메모: Intercept and control agent behavior with hooks
- **New Cursor Interface · Cursor** (`cursor.com`): https://cursor.com/changelog/3-0
  - 메모: This allows you to give more precise feedback and iterate faster by pointing the agent to exactly the part of the interface you're referring to.
- **Chat modes | aiderMenuExpand(external link)DocumentSearchCopyCopied** (`aider.chat`): https://aider.chat/docs/usage/modes.html
  - 메모: Like code mode, aider will change your files. An architect model will propose changes and an editor model will translate that proposal into specific file edits.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[microvm-agent-sandboxes|Firecracker/microVM Sandboxes for Agent Code Execution]]

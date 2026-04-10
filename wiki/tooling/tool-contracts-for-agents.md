---
title: Tool Contracts & Writing Tools for Agents
category: tooling
page_type: concept
tags: [tooling, concept, tool, contracts, for, agents]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
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

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[microvm-agent-sandboxes|Firecracker/microVM Sandboxes for Agent Code Execution]]

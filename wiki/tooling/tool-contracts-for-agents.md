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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: www.anthropic.com 2건, code.claude.com 1건, cursor.com 1건
- source 조합: 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/tool-contracts-for-agents.md`
- [Writing effective tools for AI agents—using AI agents \ Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents) — `raw/hot-topics-sources/2026-04-10/025-writing-effective-tools-for-agents.md`
  - 메모: --- title: Writing effective tools for AI agents—using AI agents \ Anthropic source_url: https://www.anthropic.com/engineering/writing-tools-for-agents final_url: https://www.anthropic.com/engineering/writing-tools-for-agents status: 200 content_type: text/html; charset=utf-8 top
- [Scaling Managed Agents: Decoupling the brain from the hands \ Anthropic](https://www.anthropic.com/engineering/managed-agents) — `raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md`
  - 메모: --- title: Scaling Managed Agents: Decoupling the brain from the hands \ Anthropic source_url: https://www.anthropic.com/engineering/managed-agents final_url: https://www.anthropic.com/engineering/managed-agents status: 200 content_type: text/html; charset=utf-8 topics: [Agent Ha
- [Agent SDK overview - Claude Code Docs](https://code.claude.com/docs/en/agent-sdk/overview) — `raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md`
  - 메모: --- title: Agent SDK overview - Claude Code Docs source_url: https://code.claude.com/docs/en/agent-sdk/overview final_url: https://code.claude.com/docs/en/agent-sdk/overview status: 200 content_type: text/html; charset=utf-8 topics: [Agent Harnesses for Long-Running Coding Sessio
- [New Cursor Interface · Cursor](https://cursor.com/changelog/3-0) — `raw/hot-topics-sources/2026-04-10/057-cursor-3-0-changelog.md`
  - 메모: --- title: New Cursor Interface · Cursor source_url: https://cursor.com/changelog/3-0 final_url: https://cursor.com/changelog/3-0 status: 200 content_type: text/html; charset=utf-8 topics: [Cursor Cloud Agents & Parallel Worktree Agents, Git Worktree Isolation for Parallel Coding
- [Chat modes | aiderMenuExpand(external link)DocumentSearchCopyCopied](https://aider.chat/docs/usage/modes.html) — `raw/hot-topics-sources/2026-04-10/065-chat-modes.md`
  - 메모: --- title: Chat modes | aiderMenuExpand(external link)DocumentSearchCopyCopied source_url: https://aider.chat/docs/usage/modes.html final_url: https://aider.chat/docs/usage/modes.html status: 200 content_type: text/html; charset=utf-8 topics: [Tool Contracts & Writing Tools for A

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[microvm-agent-sandboxes|Firecracker/microVM Sandboxes for Agent Code Execution]]

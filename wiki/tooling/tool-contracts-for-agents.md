---
title: Tool Contracts & Writing Tools for Agents
category: tooling
page_type: concept
tags: [tooling, concept, tool, contracts, for, agents]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/tool-contracts-for-agents.md, raw/hot-topics-sources/2026-04-10/025-writing-effective-tools-for-agents.md, raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md, raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md, raw/hot-topics-sources/2026-04-10/057-cursor-3-0-changelog.md, raw/hot-topics-sources/2026-04-10/065-chat-modes.md]
created: 2026-04-10
updated: 2026-04-13
---
# Tool Contracts & Writing Tools for Agents

결정론적 시스템과 비결정론적 에이전트 사이의 계약으로 툴을 설계하는 에이전트 우선 설계 철학.

## 왜 중요한가

Anthropic의 "Writing effective tools for agents" 가이드라인과 [[scaling-managed-agents|Managed Agents 블로그]]의 `execute(name, input) → string` 계약("the harness left the container")이 tool design의 기본 언어가 됐다. Cursor 3.0이 Await tool·screenshot-based clicking을 도입하면서 "에이전트에게 맞는 툴 API는 사람용 API와 다르다"는 명제가 보편화됐다.

## 대표 레퍼런스

- [Writing effective tools for AI agents -- with agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Cursor 3.0 Changelog](https://cursor.com/changelog/3-0)
- [Chat modes (Aider)](https://aider.chat/docs/usage/modes.html)

## 핵심 메커니즘

**도구는 사람용 API가 아니다.** 에이전트용 도구는 다음 특성을 가져야 한다:
- 목적이 명확하고 중복이 적다
- 결과를 agent-friendly한 형태로 요약한다
- 실패 시 에이전트가 복구 가능한 에러 메시지를 반환한다
- tool 설명(description)이 성능에 직접 영향을 준다
- pagination, filtering, truncation으로 토큰 효율을 관리한다

source 분포: anthropic.com×2, code.claude.com×1, cursor.com×1, aider.chat×1 -- 개념, 구현, 평가가 연결되어 있다.

## 도입 체크리스트

- 이 도구가 실제로 에이전트에게 필요한 capability인가?
- 도구 응답이 에이전트가 소화할 수 있는 크기인가?
- 실패 모드를 에이전트가 복구할 수 있는가?
- [[vercel-ai-sdk-tool-calling|approval이 필요한 도구]]와 자동 실행 가능한 도구를 구분했는가?

## 관련 문서

- [[writing-effective-tools-for-agents|Writing Effective Tools for Agents]]
- [[scaling-managed-agents|Scaling Managed Agents]]
- [[microvm-agent-sandboxes|Firecracker/microVM Sandboxes for Agent Code Execution]]

---
title: Claude Agent Sessions
category: tooling
page_type: summary
tags: [tooling, summary, claude-agent-sdk, sessions, state]
sources: [raw/recursive-sources/2026-04-10-sdk-mcp/claude-agent-sessions.md]
created: 2026-04-10
updated: 2026-04-10
---

# Claude Agent Sessions

Claude Agent SDK에서 sessions 개념을 설명하는 문서 요약이다. 장기 실행 에이전트에서 세션이 어떤 상태 단위로 기능하는지를 이해하는 데 중요하다.

## 핵심 내용

- session이 에이전트 실행 단위이자 상태 축적 단위로 동작함을 설명한다.
- long-running workflow에서 세션을 어떻게 이어 가는지를 다룬다.
- 단발 호출이 아니라 지속 작업을 처리하기 위한 핵심 개념을 제공한다.

## 왜 중요한가

장기 실행 에이전트 문제는 결국 “세션을 어떻게 관리할 것인가”의 문제로 돌아간다. 따라서 session 문서는 harness와 state 설계를 잇는 핵심 레퍼런스다.

## 실무 적용 관점

세션을 어디까지 지속시키고, 무엇을 외부 상태로 빼며, 어떤 시점에 재개/복구할지를 설계하는 것이 운영 품질에 직접 연결된다.

## 관련 문서

- [[claude-agent-sdk-overview|Claude Agent SDK Overview]]
- [[claude-agent-loop|Claude Agent Loop]]
- [[long-running-agent-harnesses|Agent Harnesses for Long-Running Coding Sessions]]


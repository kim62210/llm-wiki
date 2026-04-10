---
title: Claude Agent Loop
category: tooling
page_type: summary
tags: [tooling, summary, claude-agent-sdk, agent-loop, runtime]
sources: [raw/recursive-sources/2026-04-10-sdk-mcp/claude-agent-loop.md]
created: 2026-04-10
updated: 2026-04-10
---

# Claude Agent Loop

Claude Agent SDK에서 agent loop가 어떻게 동작하는지 설명하는 문서 요약이다. 에이전트가 입력을 받고, 도구를 호출하고, 세션을 이어 가는 실행 핵심을 다룬다.

## 핵심 내용

- agent loop의 반복 구조를 설명한다.
- 모델 호출과 tool routing이 어떻게 엮이는지 다룬다.
- 세션 단위의 실행과 상태 흐름을 이해하는 기준을 제공한다.

## 왜 중요한가

에이전트 SDK의 실질적인 핵심은 loop다. 이 문서를 이해해야 tool use, approvals, sessions 같은 다른 개념도 하나의 실행 모델로 연결된다.

## 실무 적용 관점

에이전트 시스템을 디버깅하거나 확장할 때는 기능 목록보다 loop를 이해하는 것이 중요하다. 결국 문제의 대부분은 loop의 어디서 상태가 어긋나는지에서 발생한다.

## 관련 문서

- [[claude-agent-sdk-overview|Claude Agent SDK Overview]]
- [[claude-agent-sdk-quickstart|Claude Agent SDK Quickstart]]
- [[long-running-agent-harnesses|Agent Harnesses for Long-Running Coding Sessions]]


---
title: Writing Effective Tools for Agents
category: tooling
page_type: summary
tags: [tooling, summary, tools, evaluation, [[coding-agent|agent]]s]
sources: [raw/2026-04-10-hot-ai-topics-sources/agent-skills/05-anthropic-com-writing-effective-tools-for-agents.md]
created: 2026-04-10
updated: 2026-04-13
---
# Writing Effective Tools for Agents

Anthropic이 에이전트용 도구 설계 원칙을 정리한 엔지니어링 글 요약이다. 핵심 메시지는, 사람용 API를 만들듯 도구를 만들면 안 되고 **비결정적 에이전트가 쓰기 좋은 인터페이스**를 별도로 설계해야 한다는 점이다.

원문 URL: https://www.anthropic.com/engineering/writing-tools-for-agents

## 핵심 내용

- 도구는 deterministic system과 non-deterministic agent 사이의 계약이다.
- 더 많은 도구가 항상 더 좋은 결과를 주지 않는다.
- 도구 응답은 의미 있는 컨텍스트만 돌려줘야 한다.
- pagination, filtering, truncation, format selection 같은 토큰 효율 설계가 중요하다.
- 도구 설명(prompt-like description) 자체도 성능에 큰 영향을 준다.

## 왜 중요한가

에이전트 성능은 모델 자체보다 **어떤 도구를 어떤 형태로 주는가**에 크게 좌우된다. 이 글은 도구 설계를 evaluation-driven process로 다뤄야 한다고 명시적으로 설명한다.

## 실무 적용 관점

좋은 에이전트 도구는 보통 다음 특징을 가진다:

1. 목적이 명확하고 중복이 적다
2. 결과를 agent-friendly한 형태로 요약해 준다
3. 실패 시 에이전트가 복구 가능한 에러 메시지를 준다
4. 평가 루프를 통해 반복적으로 다듬을 수 있다

즉, 도구는 "기능 래퍼"가 아니라 **행동을 유도하는 인터페이스**다. [[scaling-managed-agents|Managed Agents 블로그]]의 `execute(name, input) → string` 계약과 같은 선상에 있다.

## 관련 문서

- [[tool-contracts-for-agents|Tool Contracts & Writing Tools for Agents]]
- [[vercel-ai-sdk-tool-calling|Vercel AI SDK Tool Calling]]
- [[model-context-protocol-mcp|Model Context Protocol ([[model-context-protocol-mcp|MCP]])]]

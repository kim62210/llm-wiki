---
title: The Lethal Trifecta for AI Agents
category: concepts
page_type: summary
tags: [concepts, summary, security, prompt-injection, simon-willison]
sources: [raw/2026-04-10-hot-ai-topics-sources/lethal-trifecta/01-simonwillison-net-the-lethal-trifecta-for-ai-agents.md]
created: 2026-04-10
updated: 2026-04-10
---

# The Lethal Trifecta for AI Agents

Simon Willison이 lethal trifecta를 직접 설명한 원문 글 요약이다. 개념 정의보다, 왜 이 규칙이 실제 agent 보안 설계의 출발점이어야 하는지를 강하게 경고한다.

## 핵심 내용

- private data access
- exposure to untrusted content
- external communication

이 세 조건이 동시에 모이면 prompt injection을 통해 데이터 유출이 매우 쉬워진다는 주장이다.

## 왜 중요한가

이 글은 lethal trifecta를 추상 원칙이 아니라 **즉시 적용해야 하는 설계 금기 조합**으로 제시한다. 특히 MCP처럼 여러 도구를 조합하는 환경에서 위험이 급격히 커진다고 경고한다.

## 실무 적용 관점

agent 설계에서 “더 많은 기능”보다 먼저 봐야 할 것은 이 세 능력이 동시에 결합되는가 여부다. 이 문서는 그 판단 기준을 가장 직관적으로 제공한다.

| 조건 | 질문 |
|---|---|
| private data access | 내부 데이터/비밀에 접근하는가 |
| untrusted content exposure | 외부 입력을 읽는가 |
| external communication | 외부로 전송/행동할 수 있는가 |

세 칸 모두 “예”가 되는 순간, 이 문서는 그것을 즉시 위험 신호로 보라고 말한다.

## 관련 문서

- [[lethal-trifecta|Lethal Trifecta (치명적 3요소)]]
- [[agent-prompt-injection-defense|Agent Prompt Injection Defense & Trustworthy Agents]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]

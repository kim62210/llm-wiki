---
title: The Lethal Trifecta for AI Agents
category: concepts
page_type: summary
tags: [concepts, summary, [[llm-security-owasp|security]], prompt-injection, simon-willison]
sources: [raw/2026-04-10-hot-ai-topics-sources/lethal-trifecta/01-simonwillison-net-the-lethal-trifecta-for-ai-agents.md]
created: 2026-04-10
updated: 2026-04-13
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

## 원문이 다루는 흐름

원문은 대체로 `The problem is that LLMs follow instructions in content` → `This is a very common problem` → `It’s very easy to expose yourself to this risk` → `Guardrails won’t protect you` → `This is an example of the “[[agent-prompt-injection-defense|prompt injection]]” class of attacks` 순서로 전개된다. 따라서 `The Lethal Trifecta for AI Agents` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다.

- 따라가야 할 순서: The problem is that LLMs follow instructions in content, This is a very common problem, It’s very easy to expose yourself to this risk, Guardrails won’t protect you, This is an example of the “prompt injection” class of attacks
- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **The lethal trifecta for AI agents: private data, untrusted content, and external communication** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/lethal-trifecta/01-simonwillison-net-the-lethal-trifecta-for-ai-agents.md` · source: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ · 볼 섹션: The problem is that LLMs follow instructions in content, This is a very common problem, It’s very easy to expose yourself to this risk, Guardrails won’t protect you

## 관련 문서

- [[lethal-trifecta|Lethal Trifecta (치명적 3요소)]]
- [[agent-prompt-injection-defense|Agent Prompt Injection Defense & Trustworthy Agents]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]

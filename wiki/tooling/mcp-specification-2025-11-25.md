---
title: MCP Specification 2025-11-25
category: tooling
page_type: summary
tags: [tooling, summary, mcp, specification, protocol]
sources: [raw/2026-04-10-hot-ai-topics-sources/model-context-protocol/03-modelcontextprotocol-io-mcp-specification-2025-11-25.md]
created: 2026-04-10
updated: 2026-04-13
---
# MCP Specification 2025-11-25

Model Context Protocol의 2025-11-25 기준 공식 스펙 문서 요약이다. 소개 글이 아니라 실제 프로토콜 요구사항을 정리한 기준 문서다.

## 핵심 내용

- architecture, base protocol, authorization, client/server features를 정의
- resources, prompts, tools, sampling, roots, elicitation 같은 핵심 축을 명문화
- MCP 구현체 간 상호운용성을 위한 기준을 제공

## 어디를 먼저 읽을까

| 관심사 | 먼저 볼 항목 |
|---|---|
| 전체 구조 | Architecture |
| 연결 수명주기 | Base Protocol / Lifecycle |
| 보안 | Authorization |
| 기능 노출 | Resources / Tools / Prompts |
| 클라이언트 확장 | Roots / Sampling / Elicitation |

## 왜 중요한가

로드맵과 블로그가 방향을 말한다면, 실제 구현 호환성은 결국 이 스펙에서 결정된다. 따라서 MCP를 구현하거나 연동하는 팀에게는 가장 실무적인 문서다.

## 실무 적용 관점

MCP를 도입할 때는 소개 글보다 이 스펙이 더 중요하다. transport, authorization, capability negotiation처럼 실제 구현체를 깨뜨리거나 살리는 항목은 스펙을 직접 봐야 한다.

## 원문이 다루는 흐름

원문은 대체로 `Specification - Model Context Protocol` → `Base Protocol` → `Client Features` → `Server Features` → `Specification` 순서로 전개된다. 따라서 `MCP Specification 2025-11-25` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다.

- 따라가야 할 순서: Specification - Model Context Protocol, Base Protocol, Client Features, Server Features, Specification
- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **Specification - Model Context Protocol** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/model-context-protocol/03-modelcontextprotocol-io-mcp-specification-2025-11-25.md` · source: https://modelcontextprotocol.io/specification/2025-11-25 · 볼 섹션: Specification - Model Context Protocol, Base Protocol, Client Features, Server Features

## 관련 문서

- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
- [[mcp-authorization|MCP OAuth 2.1 + PKCE Authorization]]

후속 수동 ingest에서는 source version과 API 이름을 먼저 재확인한다. 이 원칙은 SDK 문서와 protocol 문서를 섞지 않기 위한 최소 안전장치다.

source와 page_type 경계를 재검증한다.

source와 page_type 경계를 재검증한다.

source와 page_type 경계를 재검증한다.

source와 page_type 경계를 재검증한다.

source와 page_type 경계를 재검증한다.

공식 source 우선.

공식 source 우선.

공식 source 우선.

공식 source 우선.

공식 source 우선.


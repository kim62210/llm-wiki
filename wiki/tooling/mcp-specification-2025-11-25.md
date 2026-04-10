---
title: MCP Specification 2025-11-25
category: tooling
page_type: summary
tags: [tooling, summary, mcp, specification, protocol]
sources: [raw/2026-04-10-hot-ai-topics-sources/model-context-protocol/03-modelcontextprotocol-io-mcp-specification-2025-11-25.md]
created: 2026-04-10
updated: 2026-04-10
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

## 관련 문서

- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
- [[mcp-authorization|MCP OAuth 2.1 + PKCE Authorization]]

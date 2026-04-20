---
title: MCP [[mcp-architecture|OAuth]] 2.1 + PKCE Authorization
aliases: [mcp-oauth-pkce-authorization]
category: tooling
page_type: entity
project: MCP OAuth 2.1 + PKCE Authorization
tags: [tooling, entity, mcp, authorization]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/mcp-authorization.md, raw/hot-topics-sources/2026-04-10/050-mcp-authorization-[[mcp-specification-2025-11-25|specification]].md, raw/hot-topics-sources/2026-04-10/047-mcp-specification-2025-11-25.md, raw/hot-topics-sources/2026-04-10/045-the-2026-mcp-roadmap.md, raw/hot-topics-sources/2026-04-10/049-modelcontextprotocol-modelcontextprotocol.md, raw/hot-topics-sources/2026-04-10/048-mcp-what-is-the-model-context-protocol.md]
created: 2026-04-10
updated: 2026-04-13
---
# MCP OAuth 2.1 + PKCE Authorization

MCP 서버를 OAuth 2.1 리소스 서버로 다루는 PKCE·Resource Indicator 기반 인증 스펙.

## 왜 지금 중요한가

2025-11-25 MCP 스펙에서 remote MCP 서버는 OAuth 2.1 + PKCE + RFC 8707 Resource Indicator가 MUST가 됐고, Client ID Metadata Document·동적 등록·audience binding이 의무화되면서 2026년 1월 Anthropic Git MCP 서버에서 path traversal+argument injection이 RCE로 연결된 사건 이후 토큰 audience 검증이 필수 방어선으로 자리잡았다.

## 대표 레퍼런스

- [MCP Authorization Specification (draft)](https://modelcontextprotocol.io/specification/draft/basic/authorization)
- [MCP Specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- [The 2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)
- [modelcontextprotocol/modelcontextprotocol (GitHub)](https://github.com/modelcontextprotocol/modelcontextprotocol)
- [MCP What is the Model Context Protocol?](https://modelcontextprotocol.io/)

## 해석 포인트

MCP OAuth 2.1 + PKCE Authorization은 단순한 제품 소개보다 **모델 능력보다 개발자 경험과 운영 통합면이 중요한 도구 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `modelcontextprotocol.io×3, blog.modelcontextprotocol.io×1, github.com×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: MCP 서버를 OAuth 2.1 리소스 서버로 다루는 PKCE·Resource Indicator 기반 인증 스펙.
- 왜 중요한가: 2025-11-25 MCP 스펙에서 remote MCP 서버는 OAuth 2.1 + PKCE + RFC 8707 Resource Indicator가 MUST가 됐고, Client ID Metadata Document·동적 등록·audience binding이 의무화되면서 2026년 1월 Anthropic Git MCP 서버에서 path traversal+argument injection이 RCE로 연결된 사건 이후 토큰 audience 검증이 필수 방어선으로 자리잡았다.
- 직접 수집 원문: 5개
- 주요 도메인: modelcontextprotocol.io×3, blog.modelcontextprotocol.io×1, github.com×1

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
- [[claude-code-hooks-system|Claude Code Hooks System]]


---
title: MCP OAuth 2.1 + PKCE Authorization
aliases: ["mcp-oauth-pkce-authorization"]
category: tooling
page_type: entity
project: MCP OAuth 2.1 + PKCE Authorization
tags: [tooling, entity, mcp, authorization]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/mcp-authorization.md, raw/hot-topics-sources/2026-04-10/050-mcp-authorization-specification.md, raw/hot-topics-sources/2026-04-10/047-mcp-specification-2025-11-25.md, raw/hot-topics-sources/2026-04-10/045-the-2026-mcp-roadmap.md, raw/hot-topics-sources/2026-04-10/049-modelcontextprotocol-modelcontextprotocol.md, raw/hot-topics-sources/2026-04-10/048-mcp-what-is-the-model-context-protocol.md]
created: 2026-04-10
updated: 2026-04-10
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

## 2026년 4월 큐레이션 요약

- 정의: MCP 서버를 OAuth 2.1 리소스 서버로 다루는 PKCE·Resource Indicator 기반 인증 스펙.
- 왜 중요한가: 2025-11-25 MCP 스펙에서 remote MCP 서버는 OAuth 2.1 + PKCE + RFC 8707 Resource Indicator가 MUST가 됐고, Client ID Metadata Document·동적 등록·audience binding이 의무화되면서 2026년 1월 Anthropic Git MCP 서버에서 path traversal+argument injection이 RCE로 연결된 사건 이후 토큰 audience 검증이 필수 방어선으로 자리잡았다.
- 직접 수집 원문: 5개
- 주요 도메인: modelcontextprotocol.io×3, blog.modelcontextprotocol.io×1, github.com×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/mcp-authorization.md`

### source별 핵심 신호

- **Authorization - Model Context Protocol** (`modelcontextprotocol.io`): https://modelcontextprotocol.io/specification/draft/basic/authorization
  - 메모: The Model Context Protocol provides authorization capabilities at the transport level,
- **Specification - Model Context Protocol** (`modelcontextprotocol.io`): https://modelcontextprotocol.io/specification/2025-11-25
  - 메모: Model Context Protocol (MCP) is an open protocol that
- **The 2026 MCP Roadmap | Model Context Protocol Blog** (`blog.modelcontextprotocol.io`): https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
  - 메모: The 2026 MCP Roadmap | Model Context Protocol BlogSkip to content
- **GitHub - modelcontextprotocol/modelcontextprotocol: Specification and documentation for the Model Context Protocol · GitHub** (`github.com`): https://github.com/modelcontextprotocol/modelcontextprotocol
  - 메모: GitHub - modelcontextprotocol/modelcontextprotocol: Specification and documentation for the Model Context Protocol · GitHub
- **What is the Model Context Protocol (MCP)? - Model Context Protocol** (`modelcontextprotocol.io`): https://modelcontextprotocol.io/docs/getting-started/intro
  - 메모: What is the Model Context Protocol (MCP)?

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
- [[claude-code-hooks-system|Claude Code Hooks System]]

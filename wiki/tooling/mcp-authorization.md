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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: modelcontextprotocol.io 3건, blog.modelcontextprotocol.io 1건, github.com 1건
- source 조합: 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/mcp-authorization.md`
- [Authorization - Model Context Protocol](https://modelcontextprotocol.io/specification/draft/basic/authorization) — `raw/hot-topics-sources/2026-04-10/050-mcp-authorization-specification.md`
  - 메모: --- title: Authorization - Model Context Protocol source_url: https://modelcontextprotocol.io/specification/draft/basic/authorization final_url: https://modelcontextprotocol.io/specification/draft/basic/authorization status: 200 content_type: text/html; charset=utf-8 topics: [MCP
- [Specification - Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) — `raw/hot-topics-sources/2026-04-10/047-mcp-specification-2025-11-25.md`
  - 메모: --- title: Specification - Model Context Protocol source_url: https://modelcontextprotocol.io/specification/2025-11-25 final_url: https://modelcontextprotocol.io/specification/2025-11-25 status: 200 content_type: text/html; charset=utf-8 topics: [MCP 2026 Roadmap & Enterprise Rea
- [The 2026 MCP Roadmap | Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap) — `raw/hot-topics-sources/2026-04-10/045-the-2026-mcp-roadmap.md`
  - 메모: --- title: The 2026 MCP Roadmap | Model Context Protocol Blog source_url: https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap final_url: https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/ status: 200 content_type: text/html; charset=utf-8 topics: [MCP 2026 Roadm
- [GitHub - modelcontextprotocol/modelcontextprotocol: Specification and documentation for the Model Context Protocol · GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol) — `raw/hot-topics-sources/2026-04-10/049-modelcontextprotocol-modelcontextprotocol.md`
  - 메모: --- title: GitHub - modelcontextprotocol/modelcontextprotocol: Specification and documentation for the Model Context Protocol · GitHub source_url: https://github.com/modelcontextprotocol/modelcontextprotocol final_url: https://github.com/modelcontextprotocol/modelcontextprotocol 
- [What is the Model Context Protocol (MCP)? - Model Context Protocol](https://modelcontextprotocol.io) — `raw/hot-topics-sources/2026-04-10/048-mcp-what-is-the-model-context-protocol.md`
  - 메모: --- title: What is the Model Context Protocol (MCP)? - Model Context Protocol source_url: https://modelcontextprotocol.io final_url: https://modelcontextprotocol.io/docs/getting-started/intro status: 200 content_type: text/html; charset=utf-8 topics: [MCP 2026 Roadmap & Enterpris

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
- [[claude-code-hooks-system|Claude Code Hooks System]]

---
title: MCP OAuth 2.1 + PKCE Authorization
aliases: ["mcp-oauth-pkce-authorization"]
category: tooling
page_type: entity
project: MCP OAuth 2.1 + PKCE Authorization
tags: [tooling, entity, mcp, authorization]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
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

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
- [[claude-code-hooks-system|Claude Code Hooks System]]

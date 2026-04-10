---
title: MCP Authorization Draft
category: tooling
page_type: summary
tags: [tooling, summary, mcp, authorization, security]
sources: [raw/recursive-sources/2026-04-10-sdk-mcp/mcp-authorization-draft.md]
created: 2026-04-10
updated: 2026-04-10
---

# MCP Authorization Draft

MCP authorization draft를 요약한 문서다. 공식 스펙과 연결되지만, 특히 권한 부여와 security boundary를 중심으로 읽기 좋다.

## 핵심 내용

- authorization 흐름의 핵심 요구사항을 다룬다.
- remote MCP server에서 왜 auth가 중요한지 설명한다.
- protocol security를 실제 운영 요구사항과 연결한다.

## 왜 중요한가

MCP는 단순 로컬 툴 연결을 넘어 원격 서비스와 조직 단위 배포로 확장되고 있기 때문에, authorization은 부가 기능이 아니라 필수 구조다.

## 실무 적용 관점

MCP를 production에 붙이려면 authorization draft와 정식 스펙을 함께 봐야 한다. 특히 credential scope, token audience, consent flow를 어떻게 잡을지가 중요하다.

## 관련 문서

- [[mcp-authorization|MCP OAuth 2.1 + PKCE Authorization]]
- [[mcp-specification-2025-11-25|MCP Specification 2025-11-25]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]


---
title: [[model-context-protocol|MCP]] Authorization Draft
category: tooling
page_type: summary
tags: [tooling, summary, mcp, authorization, [[llm-security-owasp|security]]]
sources: [raw/recursive-sources/2026-04-10-sdk-mcp/mcp-authorization-draft.md]
created: 2026-04-10
updated: 2026-04-13
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

## 원문이 다루는 흐름

원문은 대체로 `Authorization - Model Context Protocol` → `Base Protocol` → `Client Features` → `Server Features` → `Authorization` 순서로 전개된다. 따라서 `MCP Authorization Draft` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다.

- 따라가야 할 순서: Authorization - Model Context Protocol, Base Protocol, Client Features, Server Features, Authorization
- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **MCP Authorization Draft** — snapshot: `raw/recursive-sources/2026-04-10-sdk-mcp/mcp-authorization-draft.md` · source: https://modelcontextprotocol.io/specification/draft/basic/authorization · 볼 섹션: Authorization - Model Context Protocol, Base Protocol, Client Features, Server Features

## 관련 문서

- [[mcp-authorization|MCP OAuth 2.1 + PKCE Authorization]]
- [[mcp-specification-2025-11-25|MCP Specification 2025-11-25]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]

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

공식 source 우선.

공식 source 우선.

공식 source 우선.

공식 source 우선.

공식 source 우선.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

원문 기준 유지.

최신 spec 재확인.

Authorization draft는 특히 token audience, protected resource metadata, authorization server discovery를 분리해서 읽어야 한다. 구현자는 optional이라는 단어를 보안 생략으로 오해하지 말고, HTTP transport에서 제한 자원을 다룰 때 필요한 OAuth 2.1 역할과 검증 책임을 먼저 확인해야 한다.


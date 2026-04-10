---
title: What is the Model Context Protocol (MCP)?
category: tooling
page_type: summary
tags: [tooling, summary, mcp, protocol, intro]
sources: [raw/2026-04-10-hot-ai-topics-sources/model-context-protocol/04-modelcontextprotocol-io-mcp-what-is-the-model-context-protocol.md]
created: 2026-04-10
updated: 2026-04-10
---

# What is the Model Context Protocol (MCP)?

MCP 공식 문서의 입문 설명 페이지 요약이다. 호스트, 클라이언트, 서버 구조와 리소스/프롬프트/도구/샘플링 같은 기본 개념을 빠르게 이해하는 데 적합하다.

## 핵심 내용

- MCP는 LLM 앱과 외부 도구/데이터를 표준화된 방식으로 연결하려는 프로토콜이다.
- JSON-RPC 기반 메시지 포맷을 사용한다.
- 서버는 resources, prompts, tools를 제공한다.
- 클라이언트는 sampling, roots, elicitation 같은 기능을 제공할 수 있다.

## 왜 중요한가

`Model Context Protocol (MCP)` 허브 페이지가 “왜 중요한가”를 설명한다면, 이 문서는 **MCP가 정확히 무엇인지**를 가장 빠르게 설명하는 입문 자료다.

## 실무 적용 관점

새로운 팀원이나 시스템 설계자가 MCP를 처음 접할 때, 스펙 문서 전체보다 이 문서를 먼저 읽는 편이 좋다. 구조적 개념을 먼저 잡아야 이후 authorization, transport, roadmap 논의를 이해하기 쉽다.

## 관련 문서

- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
- [[mcp-authorization|MCP OAuth 2.1 + PKCE Authorization]]


---
title: Pydantic AI MCP Overview
category: tooling
page_type: summary
tags: [tooling, summary, pydantic-ai, mcp, tools]
sources: [raw/recursive-sources/2026-04-10-pydantic-deepagents/pydantic-ai-mcp-overview.md]
created: 2026-04-10
updated: 2026-04-13
---
# Pydantic AI MCP Overview

[[pydantic-ai|Pydantic AI]]에서 [[model-context-protocol-mcp|MCP]]를 붙이는 방법을 설명하는 공식 문서 요약이다. MCP를 agent tool surface로 통합하는 방식과 Python 생태계와의 결합 관점을 정리한다.

## 구조도

```mermaid
flowchart LR
    A[Pydantic AI Agent] --> B[MCP client]
    B --> C[remote/local MCP server]
    C --> D[tools/resources/prompts]
    D --> E[typed result + app logic]
```

Pydantic AI의 MCP 문맥은 단순 protocol 소개보다, Python agent 안에서 타입과 의존성 경계를 유지한 채 외부 도구를 붙이는 방법에 가깝다.

## 지원 방식

원문 기준으로 Pydantic AI는 MCP를 세 가지 방식으로 지원한다:
1. **직접 MCP client** -- `MCPServer`로 local/remote MCP 서버에 직접 연결
2. **FastMCP client** -- `FastMCPToolset`으로 FastMCP 서버 연결 (FastMCP로 빌드되지 않은 서버도 지원)
3. **모델 제공자 built-in MCP tool** -- `MCPServerTool`로 provider의 내장 MCP 기능 활용

핵심은 MCP를 도구 transport이면서도 capability surface 표준으로 다루는 점이다. agent가 서버의 tools/resources/prompts에 공통 방식으로 접근하게 해 준다.

## 실무 비교

| 관점 | Pydantic AI에서의 의미 | 주의점 |
| --- | --- | --- |
| 타입 안전성 | tool 결과를 app 로직으로 연결하기 쉬움 | 서버 출력 신뢰를 과대평가하면 안 됨 |
| 통합성 | Python 서비스와 자연스럽게 결합 | 외부 서버 lifecycle 관리 필요 |
| 확장성 | 다양한 capability를 표준 방식으로 추가 | 권한/승인/관측 체계가 함께 필요 |

## 실무 관점

- Pydantic AI에서 MCP를 붙일 때는 "어떤 서버를 연결할까"보다 "어떤 capability를 어떤 trust boundary 안에 둘까"가 더 중요하다.
- tool 설명과 결과 검증, 오류 처리, 감사 로그를 [[tool-contracts-for-agents|tool contract]] 관점으로 같이 설계해야 한다.

## 관련 문서

- [[pydantic-ai|Pydantic AI]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]
- [[mcp-architecture|MCP Architecture]]

---
title: What is the Model Context Protocol (MCP)?
category: tooling
page_type: summary
tags: [tooling, summary, mcp, protocol, intro]
sources: [raw/hot-topics-sources/2026-04-10/048-mcp-what-is-the-model-context-protocol.md]
created: 2026-04-10
updated: 2026-04-13
---
# What is the Model Context Protocol (MCP)?

[[model-context-protocol-mcp|MCP]] 공식 문서의 입문 설명 페이지 요약이다. 호스트, 클라이언트, 서버 구조와 리소스/프롬프트/도구/샘플링 같은 기본 개념을 빠르게 이해하는 데 적합하다.

원문 URL: https://modelcontextprotocol.io

## 핵심 내용

- MCP는 LLM 앱과 외부 도구/데이터를 표준화된 방식으로 연결하려는 프로토콜이다.
- JSON-RPC 기반 메시지 포맷을 사용한다.
- 서버는 resources, prompts, tools를 제공한다.
- 클라이언트는 sampling, roots, elicitation 같은 기능을 제공할 수 있다.

## MCP를 처음 설명할 때 잡아야 할 세 질문

| 질문 | 원문이 주는 답 | 실무 해석 |
|---|---|---|
| 무엇을 연결하나? | 데이터 소스, 도구, 워크플로우를 AI 앱에 연결한다 | MCP는 단일 툴 프로토콜이 아니라 capability 연결 표준이다 |
| 왜 중요한가? | AI용 USB-C처럼 표준 포트를 제공한다 | 매번 vendor-specific integration을 새로 짜지 않아도 되는 생태계 효과가 생긴다 |
| 누가 이득을 보나? | 개발자, AI 앱/에이전트, 최종 사용자 모두 혜택을 본다 | 구현 난이도, 앱 기능성, 사용자 경험이 동시에 개선되는 드문 종류의 표준이다 |

## 원문이 강조하는 대표 시나리오

| 시나리오 | 문서가 보여주는 의미 |
|---|---|
| Calendar + Notion 연결 | 개인화된 assistant를 만드는 가장 직관적 예시 |
| [[claude-code|Claude Code]] + Figma | 설계 자산이 바로 생성 워크플로우로 연결될 수 있음을 보여준다 |
| enterprise chatbot + 여러 DB | 조직 데이터 접근을 대화형 분석 흐름으로 묶는 패턴 |
| Blender + 3D printer | MCP가 사무 자동화뿐 아니라 물리적 workflow까지 확장될 수 있음을 시사 |

이 문서는 "MCP란 무엇인가"를 개념 정의로만 끝내지 않고, 표준 인터페이스가 열어주는 앱 조합의 폭을 먼저 체감하게 만든다.

## 관련 문서

- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]
- [[mcp-architecture|MCP Architecture]]
- [[mcp-authorization|MCP OAuth 2.1 + PKCE Authorization]]

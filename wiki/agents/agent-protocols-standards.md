---
title: 에이전트 프로토콜과 표준 (Agent Protocols & Standards)
category: agents
page_type: concept
tags: [agents, protocols, standards, a2a, acp, mcp, aaif, interoperability, hub]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

이 페이지는 AI 에이전트 간, 그리고 에이전트와 도구 간의 상호운용성을 위한 프로토콜과 표준을 연결하는 허브다. 2025-2026년 사이에 에이전트 프로토콜 생태계가 급속히 성숙하여, 2026년 2월 기준으로 3계층 프로토콜 스택이 업계 합의 아키텍처로 자리잡았다: MCP(에이전트-도구), A2A(에이전트-에이전트), WebMCP(에이전트-웹). 이 모든 프로토콜이 Linux Foundation의 AAIF(Agentic AI Foundation) 산하에서 관리된다.

## 프로토콜 스택

```
+----------------------------+
|        WebMCP              | -- 에이전트의 웹 접근
+----------------------------+
|        A2A                 | -- 에이전트 간 통신
|  (ACP 흡수)               |
+----------------------------+
|        MCP                 | -- 에이전트-도구 연결
+----------------------------+
```

## [[model-context-protocol-mcp|MCP (Model Context Protocol)]]

[[model-context-protocol-mcp|MCP]]는 Anthropic이 만들고 2025년 12월 Linux Foundation에 기부한 프로토콜로, AI 에이전트가 외부 도구, 데이터 소스, 서비스에 연결하는 표준 인터페이스다. "AI의 USB-C"로 비유된다.

**핵심 설계**: JSON-RPC 2.0 기반의 클라이언트-서버 아키텍처. 에이전트(호스트)가 MCP 클라이언트를 통해 MCP 서버(도구 제공자)에 연결한다. 도구(Tools), 리소스(Resources), 프롬프트(Prompts)의 세 가지 프리미티브를 제공한다.

**채택 규모**: 2026년 2월 기준 월간 SDK 다운로드 9,700만 회(Python + TypeScript 합산). Anthropic, OpenAI, Google, Microsoft, Amazon 등 모든 주요 AI 제공업체가 채택했다. [[claude-code|Claude Code]], [[codex-cli|Codex CLI]], GitHub Copilot 등 주요 코딩 에이전트가 MCP를 통해 도구를 연결한다.

**상세 페이지**: [[model-context-protocol-mcp]], [[mcp-architecture]], [[mcp-authorization]], [[mcp-server-cards]]

## [[a2a-protocol|A2A (Agent-to-Agent Protocol)]]

[[a2a-protocol|A2A]]는 Google Cloud가 2025년 4월에 발표한 프로토콜로, 서로 다른 프레임워크와 벤더로 구축된 에이전트 간의 수평적 통신을 표준화한다. MCP가 에이전트의 "손"(도구 접근)이라면, A2A는 에이전트의 "말"(에이전트 간 대화)이다.

**핵심 기능**: 에이전트 발견(Agent Card), 작업 위임(Task Delegation), 능력 협상, SSE 기반 스트리밍, 비동기 작업, 엔터프라이즈급 인증/인가. JSON-RPC 2.0 over HTTPS 기반이다.

**3계층 아키텍처**: Layer 1은 핵심 데이터 구조(Agent Card, Task, Message, Part), Layer 2는 추상 연산(발견, 작업 관리), Layer 3은 프로토콜 바인딩(JSON-RPC, gRPC, HTTP/REST)이다.

**ACP 흡수**: 2025년 8월 IBM의 ACP가 A2A에 병합되었다. 새 프로젝트에서는 A2A를 사용해야 한다.

**채택**: 2026년 기준 150+ 조직이 지원. Google, Microsoft, AWS 등 주요 클라우드 플랫폼에 통합되었다.

**상세 페이지**: [[a2a-protocol]], [[a2a-t-telecom]]

## [[acp-protocol|ACP (Agent Communication Protocol)]]

[[acp-protocol|ACP]]는 IBM의 Bee AI 팀이 개발한 에이전트 간 통신 프로토콜이다. REST 기반의 단순한 HTTP 엔드포인트를 사용하며, 비동기 우선(async-first) 설계로 장기 실행 작업을 효과적으로 처리한다. 2025년 8월 A2A에 병합되어, 독립 프로토콜로서는 더 이상 발전하지 않는다. ACP의 설계 철학(단순성, 비동기 우선)은 A2A에 흡수되어 반영되었다.

**상세 페이지**: [[acp-protocol]]

## AAIF (Agentic AI Foundation)

Linux Foundation 산하에 2025년 12월 설립된 거버넌스 조직이다. 공동 설립자 6곳: OpenAI, Anthropic, Google, Microsoft, AWS, Block. 2026년 2월 기준 100+ 엔터프라이즈가 서포터로 참여하고 있다.

AAIF의 역할은 MCP, A2A, WebMCP 등 에이전트 프로토콜의 표준화, 발전, 호환성 관리다. 프로토콜 스펙의 버전 관리, 호환성 테스트 프레임워크, 인증 프로그램을 운영한다.

에이전트 시스템의 보안과 거버넌스 관련 표준도 개발 중이며, [[nist-ai-agent-standards|NIST AI 에이전트 표준]]과 협력하고 있다.

## MCP와 A2A의 관계

MCP와 A2A는 경쟁이 아닌 보완 관계다. MCP는 개별 에이전트가 외부 도구에 접근하는 수직적(vertical) 통합을, A2A는 에이전트 간의 수평적(horizontal) 통신을 담당한다.

실제 프로덕션 멀티 에이전트 시스템에서는 두 프로토콜을 함께 사용한다. 오케스트레이터 에이전트가 A2A로 전문 에이전트에게 작업을 위임하고, 각 전문 에이전트는 MCP를 통해 필요한 도구(데이터베이스, API, 파일 시스템 등)에 접근한다.

## 프로토콜 비교

| 속성 | MCP | A2A | ACP (병합됨) |
|------|-----|-----|-------------|
| 역할 | 에이전트-도구 | 에이전트-에이전트 | 에이전트-에이전트 |
| 프로토콜 기반 | JSON-RPC 2.0 | JSON-RPC 2.0/HTTPS | REST/HTTP |
| 거버넌스 | AAIF (Linux Foundation) | AAIF (Linux Foundation) | A2A에 병합 |
| 발견 메커니즘 | MCP Server Cards | Agent Cards | Capability Endpoint |
| 스트리밍 | SSE | SSE | SSE |
| 출시 | 2024-11 | 2025-04 | 2025 (병합: 2025-08) |

## 관련 문서

- [[model-context-protocol-mcp]] -- MCP 상세
- [[mcp-architecture]] -- MCP 아키텍처
- [[a2a-protocol]] -- A2A 프로토콜 상세
- [[acp-protocol]] -- ACP (A2A에 병합)
- [[nist-ai-agent-standards]] -- NIST 에이전트 표준
- [[zero-trust-ai-agents]] -- 에이전트 보안 모델
- [[owasp-agentic-top-10]] -- 에이전트 보안 위협
- [[orchestrator-worker-pattern]] -- 멀티 에이전트 오케스트레이션
- [[evolution-of-agentic-patterns]] -- 에이전트 패턴의 진화

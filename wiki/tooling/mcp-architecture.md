---
title: MCP Architecture
category: tooling
page_type: summary
tags: [tooling, summary, mcp, architecture, protocol]
sources: [raw/recursive-sources/2026-04-10-sdk-mcp/mcp-architecture.md]
created: 2026-04-10
updated: 2026-04-10
---

# MCP Architecture

Model Context Protocol의 architecture 문서 요약이다. host / client / server 구조를 더 구체적으로 이해하기 위한 문서다.

## 핵심 내용

- MCP를 이루는 각 주체의 역할과 경계를 설명한다.
- 데이터, 도구, 프롬프트가 어떤 구조 안에서 이동하는지 이해하게 돕는다.
- 스펙보다 더 구조적 관점에서 프로토콜을 본다.

## 왜 중요한가

What is MCP?가 입문서라면, architecture 문서는 실제 시스템 관점에서 프로토콜을 이해하게 해 준다. 구현과 운영을 준비하는 팀에게 특히 중요하다.

## 실무 적용 관점

MCP 연동에서 문제가 생기면 기능보다 경계를 먼저 봐야 한다. host, client, server가 각각 어디까지 책임지는지 이해하는 것이 설계와 디버깅의 출발점이다.

## 관련 문서

- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]
- [[mcp-specification-2025-11-25|MCP Specification 2025-11-25]]
- [[what-is-mcp|What is the Model Context Protocol (MCP)?]]


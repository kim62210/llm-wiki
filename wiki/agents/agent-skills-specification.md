---
title: Agent Skills Specification
category: agents
page_type: summary
tags: [agents, summary, skills, specification, agent-skills]
sources: [raw/hot-topics-sources/2026-04-10/022-agent-skills-specification.md]
created: 2026-04-10
updated: 2026-04-10
---

# Agent Skills Specification

Agent Skills 포맷을 공식적으로 정의하는 specification 문서 요약이다. SKILL.md 기반 능력 번들을 어떻게 배치하고 기술하며, 클라이언트가 이를 어떻게 로딩해야 하는지에 대한 규약을 제공한다.

## 핵심 내용

- skill의 디렉토리 구조를 표준화한다.
- SKILL.md의 frontmatter 필드(name, description 등)를 정의한다.
- skill 제작자와 client 구현자 양쪽을 위한 규칙을 제공한다.
- 단순 텍스트 프롬프트가 아니라 **재사용 가능한 능력 패키지**라는 관점을 강조한다.

## 왜 중요한가

에이전트 생태계가 커질수록 “능력을 어떻게 묶고 배포할 것인가”가 중요해진다. 이 specification은 skill을 특정 벤더 기능이 아니라 **도구 간 호환 가능한 패키징 규약**으로 정리한다는 점에서 의미가 크다.

## 실무 적용 관점

스킬 시스템을 설계할 때 중요한 것은 프롬프트 한 파일이 아니라:

1. 어떤 메타데이터가 discovery를 돕는가  
2. 어떤 리소스를 lazy-loading할 것인가  
3. skill 실행 범위를 얼마나 명확히 구분할 것인가

라는 점이다. 이 문서는 바로 그 계약을 제공한다.

## 관련 문서

- [[agent-skills|Agent Skills]]
- [[writing-effective-tools-for-agents|Writing Effective Tools for Agents]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]


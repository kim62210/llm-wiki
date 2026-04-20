---
title: Deep Agents
category: tooling
page_type: entity
project: Deep Agents
tags: [tooling, entity, deep, agents, dev-tooling-and-frameworks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/deep-agents.md, raw/hot-topics-sources/2026-04-10/408-langchain-ai-deepagents-github.md, raw/hot-topics-sources/2026-04-10/409-deep-agents-overview-docs.md, raw/hot-topics-sources/2026-04-10/410-langchain-deep-agents-product-page.md, raw/hot-topics-sources/2026-04-10/411-deepagents-pypi.md, raw/hot-topics-sources/2026-04-10/412-langchain-releases-deep-agents-structured-runtime-for-planning-memory-context-is.md]
created: 2026-04-10
updated: 2026-04-13
---
# Deep Agents

이 페이지는 Deep Agents를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 플래너·파일시스템·서브에이전트를 기본 탑재한 LangGraph 기반 딥 에이전트 하네스이기 때문이다.

## 정의

플래너·파일시스템·서브에이전트를 기본 탑재한 [[langgraph|LangGraph]] 기반 딥 에이전트 하네스.

## 왜 지금 중요한가

2026년 3월 정식 릴리스 이후 [[claude-code|Claude Code]]식 "코딩·리서치 에이전트" 패턴을 프레임워크화해 빠르게 확산됐고, write_todos·FilesystemBackend·서브에이전트 컨텍스트 격리로 롱 컨텍스트 붕괴 문제를 정면 해결한다.

## 개요

이 페이지는 **Deep Agents** 자체를 지속적으로 누적·갱신하기 위한 허브 페이지다.

## 대표 자료

- [langchain-ai/deepagents GitHub](https://github.com/langchain-ai/deepagents)
- [Deep Agents Overview Docs](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangChain Deep Agents Product Page](https://www.langchain.com/deep-agents)
- [deepagents PyPI](https://pypi.org/project/deepagents/)
- [LangChain Releases Deep Agents: Structured Runtime for Planning, Memory, Context Isolation](https://www.marktechpost.com/2026/03/15/langchain-releases-deep-agents-a-structured-runtime-for-planning-memory-and-context-isolation-in-multi-step-ai-agents/)

## 하위 문서 읽기 경로

- [[deep-agents-quickstart|Deep Agents Quickstart]] — planning, filesystem, subagents를 갖춘 deep agent를 빠르게 띄우는 입문 경로
- [[deep-agents-subagents|Deep Agents Subagents]] — context isolation 중심의 subagent 설계 가이드
- [[deep-agents-memory|Deep Agents Memory]] — scoped memory와 forgetting 정책 정리
- [[deep-agents-production|Deep Agents Going to Production]] — guardrails, execution environment, frontend까지 포함한 운영 가이드

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[langgraph]]
- [[dspy-gepa]]

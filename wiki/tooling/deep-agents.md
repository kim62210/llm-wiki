---
title: Deep Agents
category: tooling
page_type: entity
project: Deep Agents
tags: [tooling, entity, deep, agents, dev-tooling-and-frameworks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/deep-agents.md, raw/hot-topics-sources/2026-04-10/408-langchain-ai-deepagents-github.md, raw/hot-topics-sources/2026-04-10/409-deep-agents-overview-docs.md, raw/hot-topics-sources/2026-04-10/410-langchain-deep-agents-product-page.md, raw/hot-topics-sources/2026-04-10/411-deepagents-pypi.md, raw/hot-topics-sources/2026-04-10/412-langchain-releases-deep-agents-structured-runtime-for-planning-memory-context-is.md]
created: 2026-04-10
updated: 2026-04-10
---
# Deep Agents

이 페이지는 Deep Agents를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 플래너·파일시스템·서브에이전트를 기본 탑재한 LangGraph 기반 딥 에이전트 하네스이기 때문이다.

## 정의

플래너·파일시스템·서브에이전트를 기본 탑재한 LangGraph 기반 딥 에이전트 하네스.

## 왜 지금 중요한가

2026년 3월 정식 릴리스 이후 Claude Code식 "코딩·리서치 에이전트" 패턴을 프레임워크화해 빠르게 확산됐고, write_todos·FilesystemBackend·서브에이전트 컨텍스트 격리로 롱 컨텍스트 붕괴 문제를 정면 해결한다.

## 개요

이 페이지는 **Deep Agents** 자체를 지속적으로 누적·갱신하기 위한 허브 페이지다.

## 대표 자료

- [langchain-ai/deepagents GitHub](https://github.com/langchain-ai/deepagents)
- [Deep Agents Overview Docs](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangChain Deep Agents Product Page](https://www.langchain.com/deep-agents)
- [deepagents PyPI](https://pypi.org/project/deepagents/)
- [LangChain Releases Deep Agents: Structured Runtime for Planning, Memory, Context Isolation](https://www.marktechpost.com/2026/03/15/langchain-releases-deep-agents-a-structured-runtime-for-planning-memory-and-context-isolation-in-multi-step-ai-agents/)

## 해석 포인트

Deep Agents은 단순한 제품 소개보다 **모델 능력보다 개발자 경험과 운영 통합면이 중요한 도구 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `github.com×1, docs.langchain.com×1, langchain.com×1, pypi.org×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: 플래너·파일시스템·서브에이전트를 기본 탑재한 LangGraph 기반 딥 에이전트 하네스.
- 왜 중요한가: 2026년 3월 정식 릴리스 이후 Claude Code식 "코딩·리서치 에이전트" 패턴을 프레임워크화해 빠르게 확산됐고, write_todos·FilesystemBackend·서브에이전트 컨텍스트 격리로 롱 컨텍스트 붕괴 문제를 정면 해결한다.
- 직접 수집 원문: 5개
- 주요 도메인: github.com×1, docs.langchain.com×1, langchain.com×1, pypi.org×1, marktechpost.com×1

## 핵심 포인트

Deep Agents는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 이 페이지는 Deep Agents를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 플래너·파일시스템·서브에이전트를 기본 탑재한 LangGraph 기반 딥 에이전트 하네스이기 때문이다.이며, 직접 수집한 source 5건은 docs.langchain.com×1, github.com×1, langchain.com×1, marktechpost.com×1, pypi.org×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 docs.langchain.com×1, github.com×1, langchain.com×1, marktechpost.com×1, pypi.org×1로 분포한다. 공식 문서와 구현 저장소가 같이 있어 실제 도입 관점의 정보가 강한 편이다.

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/deep-agents.md`

### source별 핵심 신호

- **GitHub - langchain-ai/deepagents: Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks. · GitHub** (`github.com`): https://github.com/langchain-ai/deepagents
  - 메모: To see all available qualifiers, see our documentation.
- **Deep Agents overview - Docs by LangChain** (`docs.langchain.com`): https://docs.langchain.com/oss/python/deepagents/overview
  - 메모: Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. Buy tickets >
- **LangChain Deep Agents: Build Agents for Complex, Multi-Step Tasks** (`langchain.com`): https://www.langchain.com/deep-agents
  - 메모: Quick start agents with any model provider
- **Client Challenge** (`pypi.org`): https://pypi.org/project/deepagents
  - 메모: A required part of this site couldn’t load. This may be due to a browser
- **LangChain Releases Deep Agents: A Structured Runtime for Planning, Memory, and Context Isolation in Multi-Step AI Agents - MarkTechPost** (`marktechpost.com`): https://www.marktechpost.com/2026/03/15/langchain-releases-deep-agents-a-structured-runtime-for-planning-memory-and-context-isolation-in-multi-step-ai-agents/
  - 메모: HomeEditors PickAgentic AILangChain Releases Deep Agents: A Structured Runtime for Planning, Memory, and Context...


## source 종합 해석

`Deep Agents`는 단일 발표보다 **여러 source가 어떤 관점에서 이 대상을 규정하는가**를 함께 읽을 때 의미가 커진다.

이번 수집에서는 GitHub - langchain-ai/deepagents: Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks. · GitHub, Deep Agents overview - Docs by LangChain, LangChain Deep Agents: Build Agents for Complex, Multi-Step Tasks처럼 출시 공지·문서·평가 신호가 같이 모여, 기능 자체보다 생태계 위치와 운영 전제가 더 중요하다는 점이 드러난다.

함께 읽을 문서로는 ai-hot-topics-2026-04, langgraph, dspy-gepa가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- 도입 판단 시 기능 목록만 보지 말고, 공식 문서·릴리스 노트·벤치마크가 서로 얼마나 일관되게 같은 메시지를 주는지 확인한다.
- 비교 후보와의 차이는 API/운영 통합, 성능 수치, 생태계 성숙도 같은 기준으로 정리하는 것이 좋다.

## 하위 문서 읽기 경로

- [[deep-agents-quickstart|Deep Agents Quickstart]] — planning, filesystem, subagents를 갖춘 deep agent를 빠르게 띄우는 입문 경로
- [[deep-agents-subagents|Deep Agents Subagents]] — context isolation 중심의 subagent 설계 가이드
- [[deep-agents-memory|Deep Agents Memory]] — scoped memory와 forgetting 정책 정리
- [[deep-agents-production|Deep Agents Going to Production]] — guardrails, execution environment, frontend까지 포함한 운영 가이드

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[langgraph]]
- [[dspy-gepa]]

---
title: Letta (MemGPT) Stateful Agent Runtime
aliases: ["letta"]
category: rag
page_type: entity
project: Letta Stateful Agent Runtime
tags: [rag, entity, letta, stateful, agent, runtime]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/letta-stateful-agent-runtime.md, raw/hot-topics-sources/2026-04-10/177-letta-github.md, raw/hot-topics-sources/2026-04-10/178-letta-code-a-memory-first-coding-agent.md, raw/hot-topics-sources/2026-04-10/179-rearchitecting-letta-s-agent-loop-lessons-from-react-memgpt-and-claude-code.md, raw/hot-topics-sources/2026-04-10/180-intro-to-letta.md, raw/hot-topics-sources/2026-04-10/181-agent-memory-how-to-build-agents-that-learn-and-remember.md]
created: 2026-04-10
updated: 2026-04-10
---
# Letta (MemGPT) Stateful Agent Runtime

LLM-as-OS 모델로 Core/Recall/Archival 3-tier 메모리를 관리하는 에이전트 플랫폼.

## 왜 지금 중요한가

2025년 12월 Letta Code 출시 이후 Terminal-Bench 1위 OSS 코딩 하네스 타이틀을 유지 중이며, v0.16.7(2026-03-31)과 Conversations API로 공유 메모리 기반 multi-session 에이전트 수요가 폭발 중이다.

## 대표 레퍼런스

- [Letta GitHub (letta-ai/letta)](https://github.com/letta-ai/letta)
- [Letta Code: A Memory-First Coding Agent](https://www.letta.com/blog/letta-code)
- [Rearchitecting Letta's Agent Loop: Lessons from ReAct, MemGPT, & Claude Code](https://www.letta.com/blog/letta-v1-agent)
- [Intro to Letta (MemGPT docs)](https://docs.letta.com/concepts/memgpt/)
- [Agent Memory: How to Build Agents that Learn and Remember](https://www.letta.com/blog/agent-memory)

## 해석 포인트

Letta (MemGPT) Stateful Agent Runtime은 단순한 제품 소개보다 **에이전트의 상태 지속성과 회수 정확도를 좌우하는 메모리 계층 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `letta.com×3, github.com×1, docs.letta.com×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 검색 정확도, 지연시간, 문맥 길이, 회수 일관성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: LLM-as-OS 모델로 Core/Recall/Archival 3-tier 메모리를 관리하는 에이전트 플랫폼.
- 왜 중요한가: 2025년 12월 Letta Code 출시 이후 Terminal-Bench 1위 OSS 코딩 하네스 타이틀을 유지 중이며, v0.16.7(2026-03-31)과 Conversations API로 공유 메모리 기반 multi-session 에이전트 수요가 폭발 중이다.
- 직접 수집 원문: 5개
- 주요 도메인: letta.com×3, github.com×1, docs.letta.com×1

## 핵심 메커니즘

LLM-as-OS 모델로 Core/Recall/Archival 3-tier 메모리를 관리하는 에이전트 플랫폼. RAG 계열 토픽은 보통 하나의 검색 기법보다 **인덱싱 방식, 검색 인터페이스, 후처리·압축 전략**의 조합으로 이해해야 한다. 이번 source 묶음에서도 `letta.com×3, github.com×1, docs.letta.com×1`처럼 서로 다른 층위의 구현/연구 source가 함께 나타난다.

## 운영 관점

2025년 12월 Letta Code 출시 이후 Terminal-Bench 1위 OSS 코딩 하네스 타이틀을 유지 중이며, v0.16.7(2026-03-31)과 Conversations API로 공유 메모리 기반 multi-session 에이전트 수요가 폭발 중이다. 실제 운영에서는 retrieval quality 하나만 보는 것이 아니라 latency, index 비용, update 빈도, multi-hop 질의 대응 여부를 함께 봐야 한다.

## 핵심 포인트

Letta (MemGPT) Stateful Agent Runtime는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 LLM-as-OS 모델로 Core/Recall/Archival 3-tier 메모리를 관리하는 에이전트 플랫폼.이며, 직접 수집한 source 5건은 letta.com×3, docs.letta.com×1, github.com×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 letta.com×3, docs.letta.com×1, github.com×1로 분포한다. 공식 문서와 구현 저장소가 같이 있어 실제 도입 관점의 정보가 강한 편이다.

## 실무 관점

실무에서는 검색 품질만이 아니라 컨텍스트 예산, chunking, 메모리 구조, 재랭킹, 운영 비용까지 함께 고려해야 한다. 그래서 이 토픽은 검색 정확도보다 '어떤 상황에서 어떤 구조를 쓰는가' 관점으로 읽는 것이 유용하다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/letta-stateful-agent-runtime.md`

### source별 핵심 신호

- **GitHub - letta-ai/letta: Letta is the platform for building stateful agents: AI with advanced memory that can learn and self-improve over time. · GitHub** (`github.com`): https://github.com/letta-ai/letta
  - 메모: To see all available qualifiers, see our documentation.
- **Letta Code: A Memory-First Coding Agent  | Letta** (`letta.com`): https://www.letta.com/blog/letta-code
  - 메모: Letta Code: A Memory-First Coding Agent | Letta
- **Rearchitecting Letta’s Agent Loop: Lessons from ReAct, MemGPT, & Claude Code  | Letta** (`letta.com`): https://www.letta.com/blog/letta-v1-agent
  - 메모: Rearchitecting Letta’s Agent Loop: Lessons from ReAct, MemGPT, & Claude Code | Letta
- **Intro to Letta | Letta Docs** (`docs.letta.com`): https://docs.letta.com/guides/get-started/intro
  - 메모: Building a Full-Stack AI Agent Application with Letta and Supabase
- **Agent Memory: How to Build Agents that Learn and Remember  | Letta** (`letta.com`): https://www.letta.com/blog/agent-memory
  - 메모: Agent Memory: How to Build Agents that Learn and Remember | Letta

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[contextual-retrieval|Contextual Retrieval (Anthropic)]]
- [[mem0-universal-memory-layer|Mem0 Universal Memory Layer]]

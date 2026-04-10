---
title: Zep / Graphiti Temporal Knowledge Graph Memory
category: rag
page_type: concept
tags: [rag, concept, temporal, knowledge, graph, memory]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/temporal-knowledge-graph-memory.md, raw/hot-topics-sources/2026-04-10/187-zep-a-temporal-knowledge-graph-architecture-for-agent-memory.md, raw/hot-topics-sources/2026-04-10/188-graphiti-github.md, raw/hot-topics-sources/2026-04-10/189-zep-platform.md, raw/hot-topics-sources/2026-04-10/190-zep-blog-a-temporal-knowledge-graph-architecture-for-agent-memory.md, raw/hot-topics-sources/2026-04-10/191-graphiti-knowledge-graph-memory-for-an-agentic-world.md]
created: 2026-04-10
updated: 2026-04-10
---
# Zep / Graphiti Temporal Knowledge Graph Memory

사실의 유효 기간(bi-temporal)을 추적하는 지식 그래프 기반 에이전트 메모리.

## 왜 중요한가

LongMemEval에서 GPT-4o 기준 Zep 63.8% vs Mem0 49.0%로 15pt 격차를 기록하며 "시간 추론이 필요한 엔터프라이즈 메모리"의 de facto 표준으로 부상했고, Graphiti는 2026년 1분기에 Neo4j와 공식 파트너십을 맺으며 Knowledge Graph Memory 카테고리를 열었다.

## 대표 레퍼런스

- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv 2501.13956)](https://arxiv.org/abs/2501.13956)
- [Graphiti GitHub (getzep/graphiti)](https://github.com/getzep/graphiti)
- [Zep Platform](https://www.getzep.com/)
- [Zep Blog: A Temporal Knowledge Graph Architecture for Agent Memory](https://blog.getzep.com/zep-a-temporal-knowledge-graph-architecture-for-agent-memory/)
- [Graphiti: Knowledge Graph Memory for an Agentic World (Neo4j Blog)](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/)

## 해석 포인트

Zep / Graphiti Temporal Knowledge Graph Memory은 **에이전트의 상태 지속성과 회수 정확도를 좌우하는 메모리 계층 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arxiv.org×1, github.com×1, getzep.com×1, blog.getzep.com×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 검색 정확도, 지연시간, 문맥 길이, 회수 일관성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 사실의 유효 기간(bi-temporal)을 추적하는 지식 그래프 기반 에이전트 메모리.
- 왜 중요한가: LongMemEval에서 GPT-4o 기준 Zep 63.8% vs Mem0 49.0%로 15pt 격차를 기록하며 "시간 추론이 필요한 엔터프라이즈 메모리"의 de facto 표준으로 부상했고, Graphiti는 2026년 1분기에 Neo4j와 공식 파트너십을 맺으며 Knowledge Graph Memory 카테고리를 열었다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×1, github.com×1, getzep.com×1, blog.getzep.com×1, neo4j.com×1

## 핵심 메커니즘

사실의 유효 기간(bi-temporal)을 추적하는 지식 그래프 기반 에이전트 메모리. RAG 계열 토픽은 보통 하나의 검색 기법보다 **인덱싱 방식, 검색 인터페이스, 후처리·압축 전략**의 조합으로 이해해야 한다. 이번 source 묶음에서도 `arxiv.org×1, github.com×1, getzep.com×1, blog.getzep.com×1, neo4j.com×1`처럼 서로 다른 층위의 구현/연구 source가 함께 나타난다.

## 운영 관점

LongMemEval에서 GPT-4o 기준 Zep 63.8% vs Mem0 49.0%로 15pt 격차를 기록하며 "시간 추론이 필요한 엔터프라이즈 메모리"의 de facto 표준으로 부상했고, Graphiti는 2026년 1분기에 Neo4j와 공식 파트너십을 맺으며 Knowledge Graph Memory 카테고리를 열었다. 실제 운영에서는 retrieval quality 하나만 보는 것이 아니라 latency, index 비용, update 빈도, multi-hop 질의 대응 여부를 함께 봐야 한다.

## 핵심 포인트

Zep / Graphiti Temporal Knowledge Graph Memory는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 사실의 유효 기간(bi-temporal)을 추적하는 지식 그래프 기반 에이전트 메모리.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 arxiv.org×1, blog.getzep.com×1, getzep.com×1, github.com×1, neo4j.com×1로 분포한다. 연구 신호와 구현체가 같이 보여서 실험 결과와 적용 방법을 연결해 보기 좋다.

## 실무 관점

실무에서는 검색 품질만이 아니라 컨텍스트 예산, chunking, 메모리 구조, 재랭킹, 운영 비용까지 함께 고려해야 한다. 그래서 이 토픽은 검색 정확도보다 '어떤 상황에서 어떤 구조를 쓰는가' 관점으로 읽는 것이 유용하다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/temporal-knowledge-graph-memory.md`

### source별 핵심 신호

- **[2501.13956] Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (`arxiv.org`): https://arxiv.org/abs/2501.13956
  - 메모: We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark.
- **GitHub - getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents · GitHub** (`github.com`): https://github.com/getzep/graphiti
  - 메모: To see all available qualifiers, see our documentation.
- **Context Engineering & Agent Memory Platform for AI Agents - Zep** (`getzep.com`): https://www.getzep.com
  - 메모: Agent MemoryGraph RAGAgent ContextKnowledge Graph MCPOpen Source
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (`blog.getzep.com`): https://blog.getzep.com/zep-a-temporal-knowledge-graph-architecture-for-agent-memory/
  - 메모: Blog /Zep: A Temporal Knowledge Graph Architecture for Agent Memory
- **Graphiti: Knowledge Graph Memory for an Agentic World** (`neo4j.com`): https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/
  - 메모: Neo4j Aura Agent A single console to manage all your DB instances

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[mem0-universal-memory-layer|Mem0 Universal Memory Layer]]
- [[embedding-leaderboard-shakeup-2026|Qwen3 / Voyage-4 Embedding Leaderboard Shakeup]]

---
title: Agentic RAG with Hierarchical Retrieval Interfaces
category: rag
page_type: concept
tags: [rag, concept, agentic, rag]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/agentic-rag.md, raw/hot-topics-sources/2026-04-10/167-a-rag-scaling-agentic-[[contextual-retrieval|retrieval]]-augmented-generation-via-hierarchical-retrieval-.md, raw/hot-topics-sources/2026-04-10/168-agentic-retrieval-augmented-generation-a-survey-on-agentic-rag.md, raw/hot-topics-sources/2026-04-10/169-a-rag-github-repository.md, raw/hot-topics-sources/2026-04-10/170-agenticrag-survey-github.md, raw/hot-topics-sources/2026-04-10/171-hero-adaptive-orchestration-of-agentic-rag-on-heterogeneous-mobile-soc.md]
created: 2026-04-10
updated: 2026-04-13
---
# Agentic RAG with Hierarchical Retrieval Interfaces

LLM이 검색 도구를 스스로 호출·반복하며 다단계 탐색을 수행하는 RAG 패러다임.

## 왜 중요한가

2026년 2월 A-RAG 논문이 keyword/semantic/chunk-read 3-tool 인터페이스로 멀티홉 QA SOTA를 경신했고, Agentic RAG Survey가 4월 1일자로 개정되며 reflection·planning·tool-use를 기본으로 하는 RAG 파이프라인이 표준으로 자리잡고 있다.

## 대표 레퍼런스

- [A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces (arXiv 2602.03442)](https://arxiv.org/abs/2602.03442)
- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG (arXiv 2501.09136)](https://arxiv.org/abs/2501.09136)
- [A-RAG GitHub Repository](https://github.com/Ayanami0730/arag)
- [AgenticRAG-Survey GitHub (Singh et al.)](https://github.com/asinghcsu/AgenticRAG-Survey)
- [HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC (arXiv 2603.01661)](https://arxiv.org/abs/2603.01661)

## 운영 관점

2026년 2월 A-RAG 논문이 keyword/semantic/chunk-read 3-tool 인터페이스로 멀티홉 QA SOTA를 경신했고, Agentic RAG Survey가 4월 1일자로 개정되며 reflection·planning·tool-use를 기본으로 하는 RAG 파이프라인이 표준으로 자리잡고 있다. 실제 운영에서는 retrieval quality 하나만 보는 것이 아니라 latency, index 비용, update 빈도, multi-hop 질의 대응 여부를 함께 봐야 한다.

## 실무 관점

실무에서는 검색 품질만이 아니라 컨텍스트 예산, chunking, 메모리 구조, 재랭킹, 운영 비용까지 함께 고려해야 한다. 그래서 이 토픽은 검색 정확도보다 '어떤 상황에서 어떤 구조를 쓰는가' 관점으로 읽는 것이 유용하다. 검색 결과는 [[agent-memory-systems|Agent Memory Systems]]의 외부 기억 계층으로 통합되며, 다중 에이전트 환경에서는 [[orchestrator-worker-pattern|Orchestrator-Worker Pattern]]으로 검색 전문 서브에이전트를 분리하는 방식이 실무 표준이 되고 있다.

## 관련 문서
- [[rag-agent-handoff]] -- RAG-에이전트 핸드오프
- [[research-learning-to-reason-with-search-paper]]
- [[memory-in-the-age-of-ai-agents-paper]]

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[context-rot|Context Rot & Effective Context Window]]
- [[contextual-retrieval|Contextual Retrieval (Anthropic)]]
- [[rag-architecture-evolution-2026]] -- 2026년 RAG 아키텍처 전반 진화 동향
- [[agent-memory-systems]] -- Agentic RAG 결과가 통합되는 에이전트 메모리 계층
- [[orchestrator-worker-pattern]] -- 검색 전문 서브에이전트 분리 패턴


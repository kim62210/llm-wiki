---
source: arxiv
arxiv_id: "2602.03442"
title: "A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces"
date: 2026-02-05
url: "https://arxiv.org/abs/2602.03442"
fetched: 2026-04-15
status: pending_ingest
---

## Abstract

A-RAG is an Agentic RAG framework that exposes hierarchical retrieval interfaces directly to the model. It provides three retrieval tools: keyword search, semantic search, and chunk read, enabling the agent to adaptively search and retrieve information across multiple granularities.

This approach scales agentic RAG by allowing the model to intelligently break down complex queries into focused subqueries, execute them in parallel, and return structured responses.

## Key Points

- 핵심 기여: 계층적 검색 인터페이스를 모델에 직접 노출하는 에이전틱 RAG 프레임워크
- 3가지 도구: keyword search, semantic search, chunk read
- 다중 세분도(granularity)에서 적응적 검색/조회
- 복잡한 쿼리를 하위 쿼리로 분해 후 병렬 실행
- multi-hop QA에서 SOTA 성능

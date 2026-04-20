---
title: Advanced RAG 패턴
category: concepts
page_type: concept
tags: [advanced-rag, rag, pre-retrieval, post-retrieval, optimization, pipeline]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# Advanced RAG 패턴

Naive RAG(단순 검색->생성)의 한계를 극복하기 위해 검색 전(Pre-retrieval), 검색 중(Retrieval), 검색 후(Post-retrieval) 각 단계를 최적화하는 패턴 모음. Gao et al. (2024) RAG 서베이에서 체계화됨.

## Naive RAG vs Advanced RAG

```mermaid
flowchart TD
    subgraph Naive[Naive RAG]
        Q1[쿼리] --> R1[벡터 검색] --> G1[LLM 생성]
    end
    subgraph Advanced[Advanced RAG]
        Q2[쿼리] --> Pre[Pre-Retrieval 쿼리 변환/확장]
        Pre --> R2[Retrieval 하이브리드/멀티홉]
        R2 --> Post[Post-Retrieval 재순위/압축]
        Post --> G2[LLM 생성 + 인용]
    end
```

## Pre-Retrieval 최적화

쿼리를 변환해 검색 품질을 높이는 기법:

| 기법 | 원리 | 관련 페이지 |
|------|------|------------|
| [[hyde-rag\|HyDE]] | 가상 답변 생성 후 임베딩 검색 | 쿼리-문서 격차 해소 |
| [[rag-fusion\|RAG Fusion]] | 쿼리 다중 변형 + RRF 통합 | 검색 다양성 확보 |
| [[step-back-prompting\|Step-Back]] | 추상화된 상위 질문으로 변환 | 배경 지식 확보 |
| Query Decomposition | 복합 질문을 하위 질문으로 분해 | 멀티홉 대응 |

## Retrieval 최적화

- **[[dense-sparse-hybrid-retrieval\|하이브리드 검색]]**: BM25 키워드 + 벡터 시맨틱 결합
- **[[multi-hop-retrieval\|멀티홉]]**: 반복적 증거 수집
- **[[parent-document-retrieval\|부모 문서 검색]]**: 작은 청크로 검색, 큰 문서로 컨텍스트

## Post-Retrieval 최적화

검색 결과를 LLM에 전달하기 전 정제:

- **[[reranker-cross-encoder\|리랭킹]]**: Cross-Encoder로 재순위
- **[[contextual-compression-retrieval\|압축]]**: 관련 부분만 추출
- **[[rag-hallucination-reduction\|충실도 검증]]**: NLI 기반 근거 검증

## Modular RAG

Advanced RAG를 넘어 각 모듈을 자유롭게 조합하는 패러다임. [[agentic-rag|에이전틱 RAG]]에서 에이전트가 검색 전략을 동적으로 선택한다.

## 관련 문서

- [[rag-pipeline]] -- RAG 파이프라인 기초
- [[agentic-rag]] -- 에이전틱 RAG
- [[self-rag]] -- Self-RAG
- [[adaptive-rag]] -- 적응형 RAG
- [[raptor-tree-retrieval]] -- RAPTOR 트리 검색

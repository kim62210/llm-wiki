---
title: Serverless Object-Storage Vector DBs (Turbopuffer 등)
category: rag
page_type: entity
project: Serverless Object-Storage Vector DBs
tags: [rag, entity, serverless, vector, dbs]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/serverless-vector-dbs.md, raw/hot-topics-sources/2026-04-10/207-turbopuffer-documentation.md, raw/hot-topics-sources/2026-04-10/208-qdrant-official-site.md, raw/hot-topics-sources/2026-04-10/209-lancedb-github.md, raw/hot-topics-sources/2026-04-10/210-vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search.md, raw/hot-topics-sources/2026-04-10/211-a-practical-guide-to-training-custom-rerankers.md]
created: 2026-04-10
updated: 2026-04-10
---
# Serverless Object-Storage Vector DBs (Turbopuffer 등)

벡터 + BM25를 S3/GCS 기반으로 저장해 TB급 인덱스 비용을 수십 배 낮춘 벡터DB.

## 왜 지금 중요한가

Turbopuffer가 object-storage 기반 하이브리드 검색(p50 8ms warm, p90 444ms cold)으로 1M+ 컨텍스트 시대의 "first-stage retrieval" 기본값이 됐고, Qdrant는 양자화, LanceDB는 in-process 멀티모달로 각각 틈새를 공고히 하며 "disk-first vector DB" 트렌드가 굳어졌다.

## 대표 레퍼런스

- [Turbopuffer Documentation](https://turbopuffer.com/docs)
- [Qdrant Official Site](https://qdrant.tech/)
- [LanceDB GitHub](https://github.com/lancedb/lancedb)
- [Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (Hugging Face Forums)](https://discuss.huggingface.co/t/vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search-bm25-text-image-vectors/171610)
- [A Practical Guide to Training Custom Rerankers (LanceDB Blog)](https://www.lancedb.com/blog/a-practical-guide-to-training-custom-rerankers)

## 2026년 4월 큐레이션 요약

- 정의: 벡터 + BM25를 S3/GCS 기반으로 저장해 TB급 인덱스 비용을 수십 배 낮춘 벡터DB.
- 왜 중요한가: Turbopuffer가 object-storage 기반 하이브리드 검색(p50 8ms warm, p90 444ms cold)으로 1M+ 컨텍스트 시대의 "first-stage retrieval" 기본값이 됐고, Qdrant는 양자화, LanceDB는 in-process 멀티모달로 각각 틈새를 공고히 하며 "disk-first vector DB" 트렌드가 굳어졌다.
- 직접 수집 원문: 5개
- 주요 도메인: turbopuffer.com×1, qdrant.tech×1, github.com×1, discuss.huggingface.co×1, lancedb.com×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/serverless-vector-dbs.md`

### source별 핵심 신호

- **Introduction** (`turbopuffer.com`): https://turbopuffer.com/docs
  - 메모: Query prices reduced by up to 94%We've reduced query prices by up to 94%
- **Qdrant - Vector Search Engine** (`qdrant.tech`): https://qdrant.tech
  - 메모: Qdrant helps you build the AI retrieval you want. Ship high performance, full-feature vector search at any scale and with any deployment model.
- **GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub** (`github.com`): https://github.com/lancedb/lancedb
  - 메모: To see all available qualifiers, see our documentation.
- **Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (BM25 + text & image vectors) - Community Calls - Hugging Face Forums** (`discuss.huggingface.co`): https://discuss.huggingface.co/t/vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search-bm25-text-image-vectors/171610
  - 메모: Hi everyone — we’re evaluating search platforms for a hybrid search use case and would appreciate insights from people who’ve used Vespa, Qdrant, or Turbopuffer in real systems.
- **A Practical Guide to Training Custom Rerankers** (`lancedb.com`): https://www.lancedb.com/blog/a-practical-guide-to-training-custom-rerankers
  - 메모: Unified vector, full-text, and hybrid search with SQL filters for production-ready retrieval

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[graphrag-in-production|GraphRAG / LightRAG / LazyGraphRAG in Production]]

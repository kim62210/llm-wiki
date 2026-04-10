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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: turbopuffer.com 1건, qdrant.tech 1건, github.com 1건
- source 조합: 구현체

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/serverless-vector-dbs.md`
- [Introduction](https://turbopuffer.com/docs) — `raw/hot-topics-sources/2026-04-10/207-turbopuffer-documentation.md`
  - 메모: --- title: Introduction source_url: https://turbopuffer.com/docs final_url: https://turbopuffer.com/docs status: 200 content_type: text/html; charset=utf-8 topics: [Serverless Object-Storage Vector DBs (Turbopuffer 등)] sections: [RAG & Context Engineering] fetched_at: 2026-04-10T
- [Qdrant - Vector Search Engine](https://qdrant.tech) — `raw/hot-topics-sources/2026-04-10/208-qdrant-official-site.md`
  - 메모: --- title: Qdrant - Vector Search Engine source_url: https://qdrant.tech final_url: https://qdrant.tech status: 200 content_type: text/html; charset=UTF-8 topics: [Serverless Object-Storage Vector DBs (Turbopuffer 등)] sections: [RAG & Context Engineering] fetched_at: 2026-04-10T0
- [GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub](https://github.com/lancedb/lancedb) — `raw/hot-topics-sources/2026-04-10/209-lancedb-github.md`
  - 메모: --- title: GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub source_url: https://github.com/lancedb/lancedb final_url: https://github.com/lancedb/lancedb status: 200 content_type: text/html; charset=u
- [Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (BM25 + text & image vectors) - Community Calls - Hugging Face Forums](https://discuss.huggingface.co/t/vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search-bm25-text-image-vectors/171610) — `raw/hot-topics-sources/2026-04-10/210-vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search.md`
  - 메모: --- title: Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (BM25 + text & image vectors) - Community Calls - Hugging Face Forums source_url: https://discuss.huggingface.co/t/vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search-bm25-text-image-vectors/171610 f
- [A Practical Guide to Training Custom Rerankers](https://www.lancedb.com/blog/a-practical-guide-to-training-custom-rerankers) — `raw/hot-topics-sources/2026-04-10/211-a-practical-guide-to-training-custom-rerankers.md`
  - 메모: --- title: A Practical Guide to Training Custom Rerankers source_url: https://www.lancedb.com/blog/a-practical-guide-to-training-custom-rerankers final_url: https://www.lancedb.com/blog/a-practical-guide-to-training-custom-rerankers status: 200 content_type: text/html; charset=ut

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[graphrag-in-production|GraphRAG / LightRAG / LazyGraphRAG in Production]]

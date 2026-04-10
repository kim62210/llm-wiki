---
title: Serverless Object-Storage Vector DBs (Turbopuffer 등)
category: rag
page_type: entity
project: Serverless Object-Storage Vector DBs
tags: [rag, entity, serverless, vector, dbs]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
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

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[graphrag-in-production|GraphRAG / LightRAG / LazyGraphRAG in Production]]

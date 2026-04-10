---
title: LMCache-Based Distributed KV Cache Offloading
category: inference
page_type: entity
project: LMCache-Based Distributed KV Cache Offloading
tags: [inference, entity, lmcache, kv, cache, layer]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/lmcache-kv-cache-layer.md, raw/hot-topics-sources/2026-04-10/095-lmcache-an-efficient-kv-cache-layer-for-enterprise-scale-llm-inference.md, raw/hot-topics-sources/2026-04-10/096-lmcache-lmcache-github-repository.md, raw/hot-topics-sources/2026-04-10/097-llm-d-kv-cache-architecture-documentation.md, raw/hot-topics-sources/2026-04-10/098-llm-d-llm-d-kv-cache-manager-repository.md, raw/hot-topics-sources/2026-04-10/099-nixlconnector-usage-guide.md]
created: 2026-04-10
updated: 2026-04-10
---
# LMCache-Based Distributed KV Cache Offloading

GPU 외부(CPU/디스크/S3)로 KV 캐시를 오프로드하고 크로스 엔진 재사용하는 계층.

## 왜 지금 중요한가

2025년 말 vLLM V1 + LMCache 조합이 multi-round QA·RAG에서 3-10배 지연 절감을 기록했고, llm-d의 KV-Cache Aware Routing과 함께 2026년 초 엔터프라이즈 표준 스택으로 부상했다.

## 대표 레퍼런스

- [LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference (arxiv)](https://arxiv.org/abs/2510.09665)
- [LMCache/LMCache GitHub repository](https://github.com/LMCache/LMCache)
- [llm-d KV Cache Architecture documentation](https://llm-d.ai/docs/architecture/Components/kv-cache)
- [llm-d/llm-d-kv-cache-manager repository](https://github.com/llm-d/llm-d-kv-cache-manager)
- [NixlConnector Usage Guide (vLLM)](https://docs.vllm.ai/en/stable/features/nixl_connector_usage/)

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/lmcache-kv-cache-layer.md`
- raw source: `raw/hot-topics-sources/2026-04-10/095-lmcache-an-efficient-kv-cache-layer-for-enterprise-scale-llm-inference.md`
- raw source: `raw/hot-topics-sources/2026-04-10/096-lmcache-lmcache-github-repository.md`
- raw source: `raw/hot-topics-sources/2026-04-10/097-llm-d-kv-cache-architecture-documentation.md`
- raw source: `raw/hot-topics-sources/2026-04-10/098-llm-d-llm-d-kv-cache-manager-repository.md`
- raw source: `raw/hot-topics-sources/2026-04-10/099-nixlconnector-usage-guide.md`

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[deepseek-sparse-attention|DeepSeek Sparse Attention (DSA) for Long Context]]
- [[flashinfer|FlashInfer Kernel Library for LLM Serving]]

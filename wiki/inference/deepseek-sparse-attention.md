---
title: DeepSeek Sparse Attention (DSA) for Long Context
category: inference
page_type: concept
tags: [inference, concept, deepseek, sparse, attention]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# DeepSeek Sparse Attention (DSA) for Long Context

lightning indexer와 top-k 셀렉터로 토큰 단위 희소 attention을 구현하는 방식.

## 왜 중요한가

DeepSeek-V3.2에서 O(L²)를 O(Lk)로 축소하며 긴 컨텍스트 학습·추론 효율을 크게 개선했고, 2026년 초 SGLang이 NativeSparseAttnBackend를, HISA·SALS 등 후속 arxiv 논문이 쏟아지고 있다.

## 대표 레퍼런스

- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556)
- [DeepSeek-V3.2-Exp GitHub repository](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp)
- [HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention](https://arxiv.org/html/2603.28458)
- [SALS: Sparse Attention in Latent Space for KV cache Compression](https://arxiv.org/pdf/2510.24273)
- [DeepSeek-V3.2 Usage Guide (vLLM Recipes)](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]
- [[lmcache-kv-cache-layer|LMCache-Based Distributed KV Cache Offloading]]

---
title: DeepSeek Sparse Attention (DSA) for Long Context
category: inference
page_type: concept
tags: [inference, concept, deepseek, sparse, attention]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/deepseek-sparse-attention.md, raw/hot-topics-sources/2026-04-10/090-deepseek-v3-2-pushing-the-frontier-of-open-large-language-models.md, raw/hot-topics-sources/2026-04-10/091-deepseek-v3-2-exp-github-repository.md, raw/hot-topics-sources/2026-04-10/092-hisa-efficient-hierarchical-indexing-for-fine-grained-sparse-attention.md, raw/hot-topics-sources/2026-04-10/093-sals-sparse-attention-in-latent-space-for-kv-cache-compression.md, raw/hot-topics-sources/2026-04-10/094-deepseek-v3-2-usage-guide.md]
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

## 2026년 4월 큐레이션 요약

- 정의: lightning indexer와 top-k 셀렉터로 토큰 단위 희소 attention을 구현하는 방식.
- 왜 중요한가: DeepSeek-V3.2에서 O(L²)를 O(Lk)로 축소하며 긴 컨텍스트 학습·추론 효율을 크게 개선했고, 2026년 초 SGLang이 NativeSparseAttnBackend를, HISA·SALS 등 후속 arxiv 논문이 쏟아지고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×3, github.com×1, docs.vllm.ai×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/deepseek-sparse-attention.md`

### source별 핵심 신호

- **[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models** (`arxiv.org`): https://arxiv.org/abs/2512.02556
  - 메모: We introduce DeepSeek-V3.2, a model that harmonizes high computational efficiency with superior reasoning and agent performance.
- **GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub** (`github.com`): https://github.com/deepseek-ai/DeepSeek-V3.2-Exp
  - 메모: To see all available qualifiers, see our documentation.
- **HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention** (`arxiv.org`): https://arxiv.org/html/2603.28458
  - 메모: While the downstream sparse attention itself scales favorably, the indexer must still scan the entire prefix for every query, introducing an 𝒪​(L2)\mathcal{O}(L^{2}) per-layer bottleneck that grows prohibitively with con
- **SALS: Sparse Attention in Latent Space for KV cache Compression** (`arxiv.org`): https://arxiv.org/pdf/2510.24273
  - 메모: << /Author (Junlin Mu; Hantao Huang; Jihang Zhang; Minghui Yu; Tao Wang; Yidong Li) /Creator (arXiv GenPDF \(tex2pdf:e76afa9\)) /DOI (https://doi.org/10.48550/arXiv.2510.24273) /License (http://arxiv.org/licenses/nonexcl
- **DeepSeek-V3.2 Usage Guide - vLLM Recipes** (`docs.vllm.ai`): https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html
  - 메모: DeepSeek-V3.2 is a model that balances computational efficiency with strong reasoning and agent capabilities through three technical innovations:

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]
- [[lmcache-kv-cache-layer|LMCache-Based Distributed KV Cache Offloading]]

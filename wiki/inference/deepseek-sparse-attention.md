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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 3건, github.com 1건, docs.vllm.ai 1건
- source 조합: 구현체

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/deepseek-sparse-attention.md`
- [[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556) — `raw/hot-topics-sources/2026-04-10/090-deepseek-v3-2-pushing-the-frontier-of-open-large-language-models.md`
  - 메모: --- title: [2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models source_url: https://arxiv.org/abs/2512.02556 final_url: https://arxiv.org/abs/2512.02556 status: 200 content_type: text/html; charset=utf-8 topics: [DeepSeek Sparse Attention (DSA) for Long 
- [GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) — `raw/hot-topics-sources/2026-04-10/091-deepseek-v3-2-exp-github-repository.md`
  - 메모: --- title: GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub source_url: https://github.com/deepseek-ai/DeepSeek-V3.2-Exp final_url: https://github.com/deepseek-ai/DeepSeek-V3.2-Exp status: 200 content_type: text/html; charset=utf-8 topics: [DeepSeek Sparse Attention (DSA) for Long
- [HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention](https://arxiv.org/html/2603.28458) — `raw/hot-topics-sources/2026-04-10/092-hisa-efficient-hierarchical-indexing-for-fine-grained-sparse-attention.md`
  - 메모: --- title: HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention source_url: https://arxiv.org/html/2603.28458 final_url: https://arxiv.org/html/2603.28458 status: 200 content_type: text/html; charset=utf-8 topics: [DeepSeek Sparse Attention (DSA) for Long Conte
- [093-sals-sparse-attention-in-latent-space-for-kv-cache-compression](https://arxiv.org/pdf/2510.24273) — `raw/hot-topics-sources/2026-04-10/093-sals-sparse-attention-in-latent-space-for-kv-cache-compression.md`
  - 메모: --- title: SALS: Sparse Attention in Latent Space for KV cache Compression source_url: https://arxiv.org/pdf/2510.24273 final_url: https://arxiv.org/pdf/2510.24273 status: 200 content_type: application/pdf topics: [DeepSeek Sparse Attention (DSA) for Long Context] sections: [Infe
- [DeepSeek-V3.2 Usage Guide - vLLM Recipes](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html) — `raw/hot-topics-sources/2026-04-10/094-deepseek-v3-2-usage-guide.md`
  - 메모: --- title: DeepSeek-V3.2 Usage Guide - vLLM Recipes source_url: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html final_url: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html status: 200 content_type: text/html; charset=utf-8 to

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]
- [[lmcache-kv-cache-layer|LMCache-Based Distributed KV Cache Offloading]]

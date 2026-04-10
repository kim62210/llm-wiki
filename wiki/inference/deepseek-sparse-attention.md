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

## 해석 포인트

DeepSeek Sparse Attention (DSA) for Long Context은 **attention 계산 경로 자체를 다시 설계해 병목을 줄이는 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arxiv.org×3, github.com×1, docs.vllm.ai×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 TTFT, TPOT, 메모리 사용량, 하드웨어 의존성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: lightning indexer와 top-k 셀렉터로 토큰 단위 희소 attention을 구현하는 방식.
- 왜 중요한가: DeepSeek-V3.2에서 O(L²)를 O(Lk)로 축소하며 긴 컨텍스트 학습·추론 효율을 크게 개선했고, 2026년 초 SGLang이 NativeSparseAttnBackend를, HISA·SALS 등 후속 arxiv 논문이 쏟아지고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×3, github.com×1, docs.vllm.ai×1

## 핵심 메커니즘

lightning indexer와 top-k 셀렉터로 토큰 단위 희소 attention을 구현하는 방식. 추론/서빙 토픽은 대부분 **throughput, latency, memory, hardware topology**의 trade-off에서 의미가 생긴다. source를 함께 보면 `arxiv.org×3, github.com×1, docs.vllm.ai×1`처럼 논문과 구현체/벤더 문서가 동시에 등장한다.

## 구현·운영 관점

DeepSeek-V3.2에서 O(L²)를 O(Lk)로 축소하며 긴 컨텍스트 학습·추론 효율을 크게 개선했고, 2026년 초 SGLang이 NativeSparseAttnBackend를, HISA·SALS 등 후속 arxiv 논문이 쏟아지고 있다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 핵심 포인트

DeepSeek Sparse Attention (DSA) for Long Context는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 lightning indexer와 top-k 셀렉터로 토큰 단위 희소 attention을 구현하는 방식.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 arxiv.org×3, docs.vllm.ai×1, github.com×1로 분포한다. 연구·공식문서·구현체가 모두 섞여 있어서 개념과 운영을 함께 추적하기 좋다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

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


## source 종합 해석

예를 들어 source note는 We introduce DeepSeek-V3.2, a model that harmonizes high computational efficiency with superior reasoning and agent performance.

또 다른 source는 To see all available qualifiers, see our documentation.

즉, 이 토픽이 중요한 이유는 `DeepSeek-V3.2에서 O(L²)를 O(Lk)로 축소하며 긴 컨텍스트 학습·추론 효율을 크게 개선했고, 2026년 초 SGLang이 NativeSparseAttnBackend를, HISA·SALS 등 후속 arxiv 논문이 쏟아지고 있다.`라는 한 문장보다, 여러 source가 같은 문제를 서로 다른 층위(개념·측정·구현)에서 지지한다는 데 있다.

함께 읽을 문서로는 2026년 4월 AI 개발 핫토픽 100선, Wide Expert Parallelism (WideEP) for MoE, LMCache-Based Distributed KV Cache Offloading가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- source note가 추상 개념/실험 결과/운영 사례 중 어디에 치우쳐 있는지 보면, 이 토픽을 실무에서 어떻게 다뤄야 하는지가 드러난다.
- `DeepSeek-V3.2에서 O(L²)를 O(Lk)로 축소하며 긴 컨텍스트 학습·추론 효율을 크게 개선했고, 2026년 초 SGLang이 NativeSparseAttnBackend를, HISA·SALS 등 후속 arxiv 논문이 쏟아지고 있다.`라는 중요도 설명은 보통 과장되기 쉬우므로, 구체적 수치·벤치마크·운영 사례를 같이 확인해야 한다.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]
- [[lmcache-kv-cache-layer|LMCache-Based Distributed KV Cache Offloading]]

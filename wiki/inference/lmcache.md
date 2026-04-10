---
title: LMCache + Mooncake KV Cache Layer
category: inference
page_type: entity
project: LMCache + Mooncake KV Cache Layer
tags: [inference, entity, lmcache]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/lmcache.md, raw/hot-topics-sources/2026-04-10/096-lmcache-lmcache-github-repository.md, raw/hot-topics-sources/2026-04-10/334-welcome-to-mooncake-documentation.md, raw/hot-topics-sources/2026-04-10/335-kvcache-ai-mooncake-github-repository.md, raw/hot-topics-sources/2026-04-10/336-mooncake-integration-lmcache-docs.md, raw/hot-topics-sources/2026-04-10/337-vllm-v1-disaggregated-serving-with-mooncake-store-and-lmcache.md]
created: 2026-04-10
updated: 2026-04-10
---
# LMCache + Mooncake KV Cache Layer

GPU/CPU/디스크/원격 스토리지에 걸친 계층형 KV 캐시 재사용 레이어.

## 왜 지금 중요한가

2026년 2월 12일 Mooncake가 PyTorch Ecosystem에 공식 합류했고 LMCache v0.4.3이 4월 6일 릴리스되면서, vLLM V1의 기본 디스어그리게이션 커넥터로 채택되어 엔터프라이즈 LLM 추론의 사실상의 KV 캐시 관리 표준이 되었다.

## 대표 레퍼런스

- [LMCache/LMCache GitHub Repository](https://github.com/LMCache/LMCache)
- [Welcome to Mooncake Documentation](https://kvcache-ai.github.io/Mooncake/)
- [kvcache-ai/Mooncake GitHub Repository](https://github.com/kvcache-ai/Mooncake)
- [Mooncake Integration - LMCache Docs](https://docs.lmcache.ai/kv_cache/mooncake.html)
- [vLLM V1 Disaggregated Serving with Mooncake Store and LMCache](https://kvcache-ai.github.io/Mooncake/getting_started/examples/vllm-integration/vllmv1-lmcache-integration.html)

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: github.com 2건, kvcache-ai.github.io 2건, docs.lmcache.ai 1건
- source 조합: 구현체, 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/lmcache.md`
- [GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub](https://github.com/LMCache/LMCache) — `raw/hot-topics-sources/2026-04-10/096-lmcache-lmcache-github-repository.md`
  - 메모: --- title: GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub source_url: https://github.com/LMCache/LMCache final_url: https://github.com/LMCache/LMCache status: 200 content_type: text/html; charset=utf-8 topics: [LMCache-Based Distributed KV
- [Welcome to Mooncake — Mooncake](https://kvcache-ai.github.io/Mooncake) — `raw/hot-topics-sources/2026-04-10/334-welcome-to-mooncake-documentation.md`
  - 메모: --- title: Welcome to Mooncake — Mooncake source_url: https://kvcache-ai.github.io/Mooncake final_url: https://kvcache-ai.github.io/Mooncake/ status: 200 content_type: text/html; charset=utf-8 topics: [LMCache + Mooncake KV Cache Layer] sections: [Infra & Serving] fetched_at: 202
- [GitHub - kvcache-ai/Mooncake: Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI. · GitHub](https://github.com/kvcache-ai/Mooncake) — `raw/hot-topics-sources/2026-04-10/335-kvcache-ai-mooncake-github-repository.md`
  - 메모: --- title: GitHub - kvcache-ai/Mooncake: Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI. · GitHub source_url: https://github.com/kvcache-ai/Mooncake final_url: https://github.com/kvcache-ai/Mooncake status: 200 content_type: text/html; ch
- [Mooncake | LMCache](https://docs.lmcache.ai/kv_cache/mooncake.html) — `raw/hot-topics-sources/2026-04-10/336-mooncake-integration-lmcache-docs.md`
  - 메모: --- title: Mooncake | LMCache source_url: https://docs.lmcache.ai/kv_cache/mooncake.html final_url: https://docs.lmcache.ai/kv_cache/mooncake.html status: 200 content_type: text/html; charset=utf-8 topics: [LMCache + Mooncake KV Cache Layer] sections: [Infra & Serving] fetched_at
- [vLLM V1 Disaggregated Serving with Mooncake Store and LMCache — Mooncake](https://kvcache-ai.github.io/Mooncake/getting_started/examples/vllm-integration/vllmv1-lmcache-integration.html) — `raw/hot-topics-sources/2026-04-10/337-vllm-v1-disaggregated-serving-with-mooncake-store-and-lmcache.md`
  - 메모: --- title: vLLM V1 Disaggregated Serving with Mooncake Store and LMCache — Mooncake source_url: https://kvcache-ai.github.io/Mooncake/getting_started/examples/vllm-integration/vllmv1-lmcache-integration.html final_url: https://kvcache-ai.github.io/Mooncake/getting_started/example

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[llm-d|llm-d & Gateway API Inference Extension]]
- [[vllm-semantic-router|vLLM Semantic Router (Iris / Athena)]]

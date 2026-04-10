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

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/lmcache.md`
- raw source: `raw/hot-topics-sources/2026-04-10/096-lmcache-lmcache-github-repository.md`
- raw source: `raw/hot-topics-sources/2026-04-10/334-welcome-to-mooncake-documentation.md`
- raw source: `raw/hot-topics-sources/2026-04-10/335-kvcache-ai-mooncake-github-repository.md`
- raw source: `raw/hot-topics-sources/2026-04-10/336-mooncake-integration-lmcache-docs.md`
- raw source: `raw/hot-topics-sources/2026-04-10/337-vllm-v1-disaggregated-serving-with-mooncake-store-and-lmcache.md`

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[llm-d|llm-d & Gateway API Inference Extension]]
- [[vllm-semantic-router|vLLM Semantic Router (Iris / Athena)]]

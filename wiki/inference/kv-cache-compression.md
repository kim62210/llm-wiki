---
title: Chunk-Semantic KV Cache Compression
category: inference
page_type: concept
tags: [inference, concept, kv, cache, compression]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/kv-cache-compression.md, raw/hot-topics-sources/2026-04-10/105-chunkkv-semantic-preserving-kv-cache-compression-for-efficient-long-context-llm-.md, raw/hot-topics-sources/2026-04-10/106-fastkv-kv-cache-compression-for-fast-long-context-inference.md, raw/hot-topics-sources/2026-04-10/107-structkv-preserving-the-structural-skeleton-for-scalable-long-context-inference.md, raw/hot-topics-sources/2026-04-10/108-kvsculpt-kv-cache-compression-as-distillation.md, raw/hot-topics-sources/2026-04-10/109-rocketkv-accelerating-long-context-llm-inference-via-two-stage-kv-cache-compress.md]
created: 2026-04-10
updated: 2026-04-10
---
# Chunk-Semantic KV Cache Compression

토큰 단위가 아닌 의미 청크 단위로 KV 엔트리를 선택·압축하는 기법.

## 왜 중요한가

2026년 초 FastKV(v6, 2026.02), StructKV, KVSculpt, EchoKV 등 청크/구조 기반 논문이 대거 등장해 128K 이상 컨텍스트에서 정확도 유지 채 처리량을 최대 26.5% 끌어올렸다.

## 대표 레퍼런스

- [ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2502.00299)
- [FastKV: KV Cache Compression for Fast Long-Context Inference](https://arxiv.org/abs/2502.01068)
- [StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference](https://arxiv.org/abs/2604.06746)
- [KVSculpt: KV Cache Compression as Distillation](https://arxiv.org/abs/2603.27819)
- [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://arxiv.org/html/2502.14051v3)

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 5건

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/kv-cache-compression.md`
- [[2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2502.00299) — `raw/hot-topics-sources/2026-04-10/105-chunkkv-semantic-preserving-kv-cache-compression-for-efficient-long-context-llm-.md`
  - 메모: --- title: [2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference source_url: https://arxiv.org/abs/2502.00299 final_url: https://arxiv.org/abs/2502.00299 status: 200 content_type: text/html; charset=utf-8 topics: [Chunk-Semantic K
- [[2502.01068] FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration](https://arxiv.org/abs/2502.01068) — `raw/hot-topics-sources/2026-04-10/106-fastkv-kv-cache-compression-for-fast-long-context-inference.md`
  - 메모: --- title: [2502.01068] FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration source_url: https://arxiv.org/abs/2502.01068 final_url: https://arxiv.org/abs/2502.01068 status: 200 content_type: text/html; charset=utf-8 topics: [Chunk-Se
- [[2604.06746] StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference](https://arxiv.org/abs/2604.06746) — `raw/hot-topics-sources/2026-04-10/107-structkv-preserving-the-structural-skeleton-for-scalable-long-context-inference.md`
  - 메모: --- title: [2604.06746] StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference source_url: https://arxiv.org/abs/2604.06746 final_url: https://arxiv.org/abs/2604.06746 status: 200 content_type: text/html; charset=utf-8 topics: [Chunk-Semantic KV Cache Co
- [[2603.27819] KVSculpt: KV Cache Compression as Distillation](https://arxiv.org/abs/2603.27819) — `raw/hot-topics-sources/2026-04-10/108-kvsculpt-kv-cache-compression-as-distillation.md`
  - 메모: --- title: [2603.27819] KVSculpt: KV Cache Compression as Distillation source_url: https://arxiv.org/abs/2603.27819 final_url: https://arxiv.org/abs/2603.27819 status: 200 content_type: text/html; charset=utf-8 topics: [Chunk-Semantic KV Cache Compression] sections: [Inference Op
- [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://arxiv.org/html/2502.14051v3) — `raw/hot-topics-sources/2026-04-10/109-rocketkv-accelerating-long-context-llm-inference-via-two-stage-kv-cache-compress.md`
  - 메모: --- title: RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression source_url: https://arxiv.org/html/2502.14051v3 final_url: https://arxiv.org/html/2502.14051v3 status: 200 content_type: text/html; charset=utf-8 topics: [Chunk-Semantic KV Cache Compr

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[flashinfer|FlashInfer Kernel Library for LLM Serving]]
- [[xgrammar-2|XGrammar-2 Constrained Decoding for Agentic LLMs]]

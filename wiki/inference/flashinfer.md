---
title: FlashInfer Kernel Library for LLM Serving
category: inference
page_type: entity
project: FlashInfer Kernel Library for LLM Serving
tags: [inference, entity, flashinfer]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/flashinfer.md, raw/hot-topics-sources/2026-04-10/100-flashinfer-efficient-and-customizable-attention-engine-for-llm-inference-serving.md, raw/hot-topics-sources/2026-04-10/101-flashinfer-ai-flashinfer-github-repository.md, raw/hot-topics-sources/2026-04-10/102-run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer.md, raw/hot-topics-sources/2026-04-10/103-mlsys-2026-flashinfer-ai-kernel-generation-contest.md, raw/hot-topics-sources/2026-04-10/104-flashinfer-on-rocm-high-throughput-prefill-attention-via-aiter.md]
created: 2026-04-10
updated: 2026-04-10
---
# FlashInfer Kernel Library for LLM Serving

vLLM/SGLang/TRT-LLM이 공유하는 attention·MoE·GEMM 커널 라이브러리.

## 왜 지금 중요한가

NVIDIA가 2026년 들어 TensorRT-LLM의 최고 성능 커널을 FlashInfer에 직접 릴리스하기 시작했고, v0.6.x에서 Blackwell FP4 GEMM·스펙 디코드 1.14배 가속을 제공하며 MLSys 2026 커널 컨테스트 기반이 되었다.

## 대표 레퍼런스

- [FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving](https://arxiv.org/abs/2501.01005)
- [flashinfer-ai/flashinfer GitHub repository](https://github.com/flashinfer-ai/flashinfer)
- [Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer](https://developer.nvidia.com/blog/run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer/)
- [MLSys 2026 FlashInfer AI Kernel Generation Contest](https://mlsys26.flashinfer.ai/)
- [FlashInfer on ROCm: High-Throughput Prefill Attention via AITER](https://rocm.blogs.amd.com/artificial-intelligence/flashinfer-release2/README.html)

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/flashinfer.md`
- raw source: `raw/hot-topics-sources/2026-04-10/100-flashinfer-efficient-and-customizable-attention-engine-for-llm-inference-serving.md`
- raw source: `raw/hot-topics-sources/2026-04-10/101-flashinfer-ai-flashinfer-github-repository.md`
- raw source: `raw/hot-topics-sources/2026-04-10/102-run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer.md`
- raw source: `raw/hot-topics-sources/2026-04-10/103-mlsys-2026-flashinfer-ai-kernel-generation-contest.md`
- raw source: `raw/hot-topics-sources/2026-04-10/104-flashinfer-on-rocm-high-throughput-prefill-attention-via-aiter.md`

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[lmcache-kv-cache-layer|LMCache-Based Distributed KV Cache Offloading]]
- [[kv-cache-compression|Chunk-Semantic KV Cache Compression]]

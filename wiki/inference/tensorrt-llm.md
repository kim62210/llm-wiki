---
title: TensorRT-LLM 1.3 with Day-0 Model Support
category: inference
page_type: entity
project: TensorRT-LLM 1.3 with Day-0 Model Support
tags: [inference, entity, tensorrt, llm]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/tensorrt-llm.md, raw/hot-topics-sources/2026-04-10/343-tensorrt-llm-release-notes.md, raw/hot-topics-sources/2026-04-10/344-nvidia-tensorrt-llm-github-releases.md, raw/hot-topics-sources/2026-04-10/345-nvidia-tensorrt-llm-github-repository.md, raw/hot-topics-sources/2026-04-10/346-tensorrt-llm-documentation.md, raw/hot-topics-sources/2026-04-10/347-tensorrt-llm-speculative-sampling-documentation.md]
created: 2026-04-10
updated: 2026-04-10
---
# TensorRT-LLM 1.3 with Day-0 Model Support

NVIDIA의 프로덕션 LLM 엔진으로 Day-0 GPT-OSS 지원과 새 C++ 샘플러를 기본화.

## 왜 지금 중요한가

2026년 3월 1.3.0rc 시리즈가 활발히 릴리스되면서 GPT-OSS-120B/20B와 EXAONE 4.0 Day-0 지원, B200에서 Llama 4 40k+ tok/s를 기록하며 NVIDIA 하드웨어의 공식 속도 기준점으로 자리잡았다.

## 대표 레퍼런스

- [TensorRT-LLM Release Notes](https://nvidia.github.io/TensorRT-LLM/release-notes.html)
- [NVIDIA/TensorRT-LLM GitHub Releases](https://github.com/NVIDIA/TensorRT-LLM/releases)
- [NVIDIA/TensorRT-LLM GitHub Repository](https://github.com/NVIDIA/TensorRT-LLM)
- [TensorRT LLM Documentation](https://nvidia.github.io/TensorRT-LLM/)
- [TensorRT LLM Speculative Sampling Documentation](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html)

## 2026년 4월 큐레이션 요약

- 정의: NVIDIA의 프로덕션 LLM 엔진으로 Day-0 GPT-OSS 지원과 새 C++ 샘플러를 기본화.
- 왜 중요한가: 2026년 3월 1.3.0rc 시리즈가 활발히 릴리스되면서 GPT-OSS-120B/20B와 EXAONE 4.0 Day-0 지원, B200에서 Llama 4 40k+ tok/s를 기록하며 NVIDIA 하드웨어의 공식 속도 기준점으로 자리잡았다.
- 직접 수집 원문: 5개
- 주요 도메인: nvidia.github.io×3, github.com×2

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/tensorrt-llm.md`

### source별 핵심 신호

- **Release Notes — TensorRT LLM** (`nvidia.github.io`): https://nvidia.github.io/TensorRT-LLM/release-notes.html
  - 메모: Accelerating Long-Context Inference with Skip Softmax Attention
- **Releases · NVIDIA/TensorRT-LLM · GitHub** (`github.com`): https://github.com/NVIDIA/TensorRT-LLM/releases
  - 메모: To see all available qualifiers, see our documentation.
- **GitHub - NVIDIA/TensorRT-LLM: TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way. · GitHub** (`github.com`): https://github.com/NVIDIA/TensorRT-LLM
  - 메모: To see all available qualifiers, see our documentation.
- **Welcome to TensorRT LLM’s Documentation! — TensorRT LLM** (`nvidia.github.io`): https://nvidia.github.io/TensorRT-LLM/
  - 메모: Accelerating Long-Context Inference with Skip Softmax Attention
- **Speculative Sampling — TensorRT-LLM** (`nvidia.github.io`): https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html
  - 메모: Speculative Sampling (also referred to as Speculative Decoding) is a set of techniques designed to allow generation of more than one token per forward pass iteration.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[vllm-semantic-router|vLLM Semantic Router (Iris / Athena)]]
- [[vllm-rocm-platform|AMD ROCm as First-Class vLLM Platform]]

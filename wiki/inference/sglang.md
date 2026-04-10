---
title: SGLang on GB300 NVL72 with NVFP4
category: inference
page_type: entity
project: SGLang on GB300 NVL72 with NVFP4
tags: [inference, entity, sglang]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/sglang.md, raw/hot-topics-sources/2026-04-10/325-unlocking-25x-inference-performance-with-sglang-on-nvidia-gb300-nvl72.md, raw/hot-topics-sources/2026-04-10/326-deploying-deepseek-on-gb300-nvl72-big-wins-in-long-context-inference.md, raw/hot-topics-sources/2026-04-10/327-sgl-project-sglang-github-repository.md, raw/hot-topics-sources/2026-04-10/085-sglang-q1-2026-development-roadmap.md, raw/hot-topics-sources/2026-04-10/328-sglang-documentation.md]
created: 2026-04-10
updated: 2026-04-10
---
# SGLang on GB300 NVL72 with NVFP4

SGLang이 NVFP4 GEMM과 Dynamo 디스어그리게이션으로 GB300 NVL72에서 DeepSeek-R1을 최대 25배 가속.

## 왜 지금 중요한가

2026년 2월 InferenceXv2 벤치마크에서 H200 대비 25배, GB200 NVL72 대비 8배 성능 향상을 공개적으로 증명했고, GB300 세대 하드웨어의 전환점 벤치마크로 광범위하게 인용되고 있다.

## 대표 레퍼런스

- [Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72 (2026-02-20)](https://lmsys.org/blog/2026-02-20-gb300-inferencex/)
- [Deploying DeepSeek on GB300 NVL72: Big Wins in Long-Context Inference (2026-02-19)](https://www.lmsys.org/blog/2026-02-19-gb300-longctx/)
- [sgl-project/sglang GitHub Repository](https://github.com/sgl-project/sglang)
- [SGLang Development Roadmap (2026 Q1) - Issue #12780](https://github.com/sgl-project/sglang/issues/12780)
- [SGLang Documentation](http://docs.sglang.io/)

## 2026년 4월 큐레이션 요약

- 정의: SGLang이 NVFP4 GEMM과 Dynamo 디스어그리게이션으로 GB300 NVL72에서 DeepSeek-R1을 최대 25배 가속.
- 왜 중요한가: 2026년 2월 InferenceXv2 벤치마크에서 H200 대비 25배, GB200 NVL72 대비 8배 성능 향상을 공개적으로 증명했고, GB300 세대 하드웨어의 전환점 벤치마크로 광범위하게 인용되고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: lmsys.org×2, github.com×2, docs.sglang.io×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/sglang.md`

### source별 핵심 신호

- **Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72 - LMSYS Blog | LMSYS Org** (`lmsys.org`): https://www.lmsys.org/blog/2026-02-20-gb300-inferencex/
  - 메모: The SGLang team has worked closely with NVIDIA across multiple GPU generations to unlock step-function gains in inference performance for large-scale deployments of Mixture of Expert (MoE) reasoning models.
- **Deploying DeepSeek on GB300 NVL72: Big Wins in Long-Context Inference - LMSYS Blog | LMSYS Org** (`lmsys.org`): https://www.lmsys.org/blog/2026-02-19-gb300-longctx/
  - 메모: 2. Prefill Path: PP Prefill, Long-Context TTFT, and Faster Kernels
- **GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub** (`github.com`): https://github.com/sgl-project/sglang
  - 메모: To see all available qualifiers, see our documentation.
- **Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub** (`github.com`): https://github.com/sgl-project/sglang/issues/12780
  - 메모: To see all available qualifiers, see our documentation.
- **SGLang Documentation — SGLang** (`docs.sglang.io`): http://docs.sglang.io
  - 메모: Popular Model Usage (DeepSeek, GPT-OSS, GLM, Llama, MiniMax, Qwen, and more)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[vllm-v1-engine|vLLM V1 Engine on Blackwell (GB200/GB300)]]
- [[llm-d|llm-d & Gateway API Inference Extension]]

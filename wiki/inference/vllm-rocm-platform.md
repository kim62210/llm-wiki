---
title: AMD ROCm as First-Class vLLM Platform
category: inference
page_type: entity
project: AMD ROCm as First-Class vLLM Platform
tags: [inference, entity, vllm, rocm, platform]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/vllm-rocm-platform.md, raw/hot-topics-sources/2026-04-10/348-beyond-porting-how-vllm-orchestrates-high-performance-inference-on-amd-rocm.md, raw/hot-topics-sources/2026-04-10/349-rocm-becomes-a-first-class-platform-in-the-vllm-ecosystem-rocm-blogs.md, raw/hot-topics-sources/2026-04-10/350-vllm-inference-rocm-documentation.md, raw/hot-topics-sources/2026-04-10/351-llm-inference-frameworks-rocm-documentation.md, raw/hot-topics-sources/2026-04-10/352-sglang-fast-serving-framework-on-amd-instinct-gpus-rocm-blogs.md]
created: 2026-04-10
updated: 2026-04-10
---
# AMD ROCm as First-Class vLLM Platform

vLLM ROCm 백엔드가 MI300X/MI325X/MI350X에서 7개 어텐션 백엔드를 제공.

## 왜 지금 중요한가

2025년 12월 29일 ROCm CI 파이프라인이 상시 가동되었고 2026년 1월 6일 공식 ROCm vLLM-omni Docker 이미지가 공개되었으며, 2월 27일 vLLM 공식 블로그가 AMD를 first-class platform으로 선언하면서 GPU 공급 병목의 실질적 대안으로 급부상했다.

## 대표 레퍼런스

- [Beyond Porting: How vLLM Orchestrates High-Performance Inference on AMD ROCm (2026-02-27)](https://blog.vllm.ai/2026/02/27/rocm-attention-backend.html)
- [ROCm Becomes a First-Class Platform in the vLLM Ecosystem - ROCm Blogs](https://rocm.blogs.amd.com/software-tools-optimization/vllm-omni/README.html)
- [vLLM Inference - ROCm Documentation](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html)
- [LLM Inference Frameworks - ROCm Documentation](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html)
- [SGLang: Fast Serving Framework on AMD Instinct GPUs - ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/sglang/README.html)

## 2026년 4월 큐레이션 요약

- 정의: vLLM ROCm 백엔드가 MI300X/MI325X/MI350X에서 7개 어텐션 백엔드를 제공.
- 왜 중요한가: 2025년 12월 29일 ROCm CI 파이프라인이 상시 가동되었고 2026년 1월 6일 공식 ROCm vLLM-omni Docker 이미지가 공개되었으며, 2월 27일 vLLM 공식 블로그가 AMD를 first-class platform으로 선언하면서 GPU 공급 병목의 실질적 대안으로 급부상했다.
- 직접 수집 원문: 5개
- 주요 도메인: rocm.blogs.amd.com×2, rocm.docs.amd.com×2, vllm.ai×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/vllm-rocm-platform.md`

### source별 핵심 신호

- **Beyond Porting: How vLLM Orchestrates High-Performance Inference on AMD ROCm | vLLM Blog** (`vllm.ai`): https://vllm.ai/blog/rocm-attention-backend
  - 메모: In collaboration with the open-source community, vLLM \+ NVIDIA has achieved significant performance milestones on the gpt-oss-120b model running on NVIDIA's Blackwell GPUs. Through deep...
- **ROCm Becomes a First-Class Platform in the vLLM Ecosystem — ROCm Blogs** (`rocm.blogs.amd.com`): https://rocm.blogs.amd.com/software-tools-optimization/vllm-omni/README.html
  - 메모: As the generative AI ecosystem matures, vLLM embraces a multivendor ecosystem.
- **vLLM inference — ROCm Documentation** (`rocm.docs.amd.com`): https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html
  - 메모: Train a model with Primus and Megatron-LM
- **LLM inference frameworks — ROCm Documentation** (`rocm.docs.amd.com`): https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html
  - 메모: Train a model with Primus and Megatron-LM
- **SGLang: Fast Serving Framework for Large Language and Vision-Language Models on AMD Instinct GPUs — ROCm Blogs** (`rocm.blogs.amd.com`): https://rocm.blogs.amd.com/artificial-intelligence/sglang/README.html
  - 메모: SGLang: Fast Serving Framework for Large Language and Vision-Language Models on AMD Instinct GPUs

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[tensorrt-llm|TensorRT-LLM 1.3 with Day-0 Model Support]]

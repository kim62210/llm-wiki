---
title: NVFP4 Quantization for LLM Inference
category: inference
page_type: concept
tags: [inference, concept, nvfp4, quantization]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/nvfp4-quantization.md, raw/hot-topics-sources/2026-04-10/071-introducing-nvfp4-for-efficient-and-accurate-low-precision-inference.md, raw/hot-topics-sources/2026-04-10/072-accelerating-llms-with-nvfp4-quantization.md, raw/hot-topics-sources/2026-04-10/073-nvfp4-llm-compressor-documentation.md, raw/hot-topics-sources/2026-04-10/074-nvidia-model-optimizer-repository.md, raw/hot-topics-sources/2026-04-10/075-quantization-aware-distillation-for-nvfp4-inference-accuracy-recovery.md]
created: 2026-04-10
updated: 2026-04-10
---
# NVFP4 Quantization for LLM Inference

Blackwell 전용 4비트 부동소수점 포맷, 16값 블록 이중 스케일링.

## 왜 중요한가

2026년 2월 vLLM/TensorRT-LLM에 공식 통합되어 FP8 대비 1.8배, FP16 대비 3.5배 메모리 절감과 1% 미만 정확도 손실을 달성했다. DeepSeek-R1/V3.2, Llama 4 Scout 등 주요 모델의 NVFP4 체크포인트가 HuggingFace에 배포되었다.

## 대표 레퍼런스

- [Introducing NVFP4 for Efficient and Accurate Low-Precision Inference (NVIDIA blog)](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/)
- [Accelerating LLMs with NVFP4 quantization (Red Hat)](https://developers.redhat.com/articles/2026/02/04/accelerating-large-language-models-nvfp4-quantization)
- [NVFP4 LLM Compressor Documentation](https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4/)
- [NVIDIA Model-Optimizer repository](https://github.com/NVIDIA/Model-Optimizer)
- [Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery (NVIDIA research)](https://research.nvidia.com/labs/nemotron/files/NVFP4-QAD-Report.pdf)

## 2026년 4월 큐레이션 요약

- 정의: Blackwell 전용 4비트 부동소수점 포맷, 16값 블록 이중 스케일링.
- 왜 중요한가: 2026년 2월 vLLM/TensorRT-LLM에 공식 통합되어 FP8 대비 1.8배, FP16 대비 3.5배 메모리 절감과 1% 미만 정확도 손실을 달성했다. DeepSeek-R1/V3.2, Llama 4 Scout 등 주요 모델의 NVFP4 체크포인트가 HuggingFace에 배포되었다.
- 직접 수집 원문: 5개
- 주요 도메인: developer.nvidia.com×1, developers.redhat.com×1, docs.vllm.ai×1, github.com×1, research.nvidia.com×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/nvfp4-quantization.md`

### source별 핵심 신호

- **Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog** (`developer.nvidia.com`): https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference
  - 메모: NVIDIA Blackwell's NVFP4, a 4-bit floating point format, is designed to improve model accuracy at ultra-low precision by using a two-level scaling strategy that includes a fine-grained E4M3 scaling factor and a second-le
- **Accelerating large language models with NVFP4 quantization | Red Hat Developer** (`developers.redhat.com`): https://developers.redhat.com/articles/2026/02/04/accelerating-large-language-models-nvfp4-quantization
  - 메모: Try Red Hat products and technologies without setup or configuration fees for 30 days with this shared Red Hat OpenShift and Kubernetes cluster.
- **fp4 Quantization with NVFP4 - LLM Compressor Docs** (`docs.vllm.ai`): https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4/
  - 메모: Big Model Quantization with Sequential Onloading
- **GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub** (`github.com`): https://github.com/NVIDIA/Model-Optimizer
  - 메모: To see all available qualifiers, see our documentation.
- **Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery (NVIDIA research)** (`research.nvidia.com`): https://research.nvidia.com/labs/nemotron/files/NVFP4-QAD-Report.pdf
  - 메모: << /Linearized 1 /L 619229 /H [ 2295 387 ] /O 466 /E 312919 /N 17 /T 616185 >>

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[flashattention-4|FlashAttention-4 on Blackwell]]
- [[eagle-3-speculative-decoding|EAGLE-3 Speculative Decoding]]

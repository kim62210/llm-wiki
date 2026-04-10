---
title: NVFP4 Quantization for LLM Inference
category: inference
page_type: concept
tags: [inference, concept, nvfp4, quantization]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
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

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[flashattention-4|FlashAttention-4 on Blackwell]]
- [[eagle-3-speculative-decoding|EAGLE-3 Speculative Decoding]]

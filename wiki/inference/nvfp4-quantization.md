---
title: NVFP4 Quantization for LLM Inference
category: inference
page_type: concept
tags: [inference, concept, nvfp4, quantization]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/nvfp4-quantization.md, raw/hot-topics-sources/2026-04-10/071-introducing-nvfp4-for-efficient-and-accurate-low-precision-inference.md, raw/hot-topics-sources/2026-04-10/072-accelerating-llms-with-nvfp4-quantization.md, raw/hot-topics-sources/2026-04-10/073-nvfp4-llm-compressor-documentation.md, raw/hot-topics-sources/2026-04-10/074-nvidia-model-optimizer-repository.md, raw/hot-topics-sources/2026-04-10/075-quantization-aware-distillation-for-nvfp4-inference-accuracy-recovery.md]
created: 2026-04-10
updated: 2026-04-13
---
# NVFP4 Quantization for LLM Inference

Blackwell 전용 4비트 부동소수점 포맷, 16값 블록 이중 스케일링.

## 왜 중요한가

2026년 2월 [[vllm-v1-engine|vLLM]]/TensorRT-LLM에 공식 통합되어 FP8 대비 1.8배, FP16 대비 3.5배 메모리 절감과 1% 미만 정확도 손실을 달성했다. DeepSeek-R1/V3.2, Llama 4 Scout 등 주요 모델의 NVFP4 체크포인트가 HuggingFace에 배포되었다.

## 대표 레퍼런스

- [Introducing NVFP4 for Efficient and Accurate Low-Precision Inference ([[blackwell-ultra-b300|NVIDIA]] blog)](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/)
- [Accelerating LLMs with NVFP4 [[ai-inference-quantization-2026|quantization]] (Red Hat)](https://developers.redhat.com/articles/2026/02/04/accelerating-large-language-models-nvfp4-quantization)
- [NVFP4 LLM Compressor Documentation](https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4/)
- [NVIDIA Model-Optimizer repository](https://github.com/NVIDIA/Model-Optimizer)
- [Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery (NVIDIA research)](https://research.nvidia.com/labs/nemotron/files/NVFP4-QAD-Report.pdf)

## 구현·운영 관점

2026년 2월 vLLM/TensorRT-LLM에 공식 통합되어 FP8 대비 1.8배, FP16 대비 3.5배 메모리 절감과 1% 미만 정확도 손실을 달성했다. DeepSeek-R1/V3.2, Llama 4 Scout 등 주요 모델의 NVFP4 체크포인트가 HuggingFace에 배포되었다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

## 관련 문서
- [[nvidia-vera-rubin]]
- [[ai-inference-quantization-2026]]
- [[turboquant]]
- [[meta-adaptive-ranking]]
- [[long-context-scaling]]

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[flashattention-4|FlashAttention-4 on Blackwell]]
- [[eagle-3-speculative-decoding|EAGLE-3 Speculative Decoding]]


---
title: FlashAttention-4 on Blackwell
category: inference
page_type: concept
tags: [inference, concept, flashattention, 4]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# FlashAttention-4 on Blackwell

Blackwell GPU 비대칭 스케일링에 맞춘 attention 커널 재설계.

## 왜 중요한가

Tri Dao 팀이 2026년 3월 발표, B200에서 1613 TFLOPs/s(71% 활용률)로 cuDNN 대비 1.3배, Triton 대비 2.7배 속도 향상을 달성했다. softmax 지수 연산 소프트웨어 에뮬레이션과 2-CTA MMA 모드 활용이 핵심이다.

## 대표 레퍼런스

- [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/abs/2603.05451)
- [FlashAttention-4 blog post by Tri Dao](https://tridao.me/blog/2026/flash4/)
- [FlashAttention-4 Princeton AI Lab blog](https://blog.ai.princeton.edu/2026/03/12/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling/)
- [Dao-AILab/flash-attention GitHub repository](https://github.com/Dao-AILab/flash-attention)
- [Generalized Dot-Product Attention PyTorch blog](https://pytorch.org/blog/)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[nvfp4-quantization|NVFP4 Quantization for LLM Inference]]

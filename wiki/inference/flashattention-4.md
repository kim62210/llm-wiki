---
title: FlashAttention-4 on Blackwell
category: inference
page_type: concept
tags: [inference, concept, flashattention, 4]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/flashattention-4.md, raw/hot-topics-sources/2026-04-10/066-flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardwa.md, raw/hot-topics-sources/2026-04-10/067-flashattention-4-blog-post-by-tri-dao.md, raw/hot-topics-sources/2026-04-10/068-flashattention-4-princeton-ai-lab-blog.md, raw/hot-topics-sources/2026-04-10/069-dao-ailab-flash-attention-github-repository.md, raw/hot-topics-sources/2026-04-10/070-generalized-dot-product-attention-pytorch-blog.md]
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

## 2026년 4월 큐레이션 요약

- 정의: Blackwell GPU 비대칭 스케일링에 맞춘 attention 커널 재설계.
- 왜 중요한가: Tri Dao 팀이 2026년 3월 발표, B200에서 1613 TFLOPs/s(71% 활용률)로 cuDNN 대비 1.3배, Triton 대비 2.7배 속도 향상을 달성했다. softmax 지수 연산 소프트웨어 에뮬레이션과 2-CTA MMA 모드 활용이 핵심이다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×1, tridao.me×1, blog.ai.princeton.edu×1, github.com×1, pytorch.org×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/flashattention-4.md`

### source별 핵심 신호

- **[2603.05451] FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling** (`arxiv.org`): https://arxiv.org/abs/2603.05451
  - 메모: Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications.
- **FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | Tri Dao** (`tridao.me`): https://tridao.me/blog/2026/flash4/
  - 메모: This scaling asymmetry has profound implications for optimizing complex kernels like attention for the Blackwell architecture.
- **FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling – Princeton Laboratory for Artificial Intelligence Research Blog** (`blog.ai.princeton.edu`): https://blog.ai.princeton.edu/2026/03/12/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling/
  - 메모: Transformers remain the backbone for most AI applications, from large language models to vision and multimodal systems.
- **GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact attention · GitHub** (`github.com`): https://github.com/Dao-AILab/flash-attention
  - 메모: To see all available qualifiers, see our documentation.
- **Blog – PyTorch** (`pytorch.org`): https://pytorch.org/blog/
  - 메모: On Hopper and Blackwell GPUs, FlexAttention now has a FlashAttention-4 backend.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[nvfp4-quantization|NVFP4 Quantization for LLM Inference]]

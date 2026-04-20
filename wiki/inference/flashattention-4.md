---
title: FlashAttention-4 on Blackwell
category: inference
page_type: concept
tags: [inference, concept, flash[[self-attention-mechanism|attention]], 4]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/flashattention-4.md, raw/hot-topics-sources/2026-04-10/066-flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardwa.md, raw/hot-topics-sources/2026-04-10/067-flashattention-4-blog-post-by-tri-dao.md, raw/hot-topics-sources/2026-04-10/068-flashattention-4-princeton-ai-lab-blog.md, raw/hot-topics-sources/2026-04-10/069-dao-ailab-flash-attention-github-repository.md, raw/hot-topics-sources/2026-04-10/070-generalized-dot-product-attention-pytorch-blog.md]
created: 2026-04-10
updated: 2026-04-13
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

## 구현·운영 관점

Tri Dao 팀이 2026년 3월 발표, B200에서 1613 TFLOPs/s(71% 활용률)로 cuDNN 대비 1.3배, Triton 대비 2.7배 속도 향상을 달성했다. softmax 지수 연산 소프트웨어 에뮬레이션과 2-CTA MMA 모드 활용이 핵심이다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

## 관련 문서
- [[sparse-attention-patterns]]
- [[long-context-scaling]]

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[nvfp4-quantization|NVFP4 Quantization for LLM Inference]]
- [[flashattention-4-paper|FlashAttention-4 paper]] — Blackwell attention kernel co-design 논문


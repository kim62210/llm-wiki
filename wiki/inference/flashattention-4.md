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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 1건, tridao.me 1건, blog.ai.princeton.edu 1건
- source 조합: 구현체

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/flashattention-4.md`
- [[2603.05451] FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/abs/2603.05451) — `raw/hot-topics-sources/2026-04-10/066-flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardwa.md`
  - 메모: --- title: [2603.05451] FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling source_url: https://arxiv.org/abs/2603.05451 final_url: https://arxiv.org/abs/2603.05451 status: 200 content_type: text/html; charset=utf-8 topics: [FlashAttention-
- [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | Tri Dao](https://tridao.me/blog/2026/flash4) — `raw/hot-topics-sources/2026-04-10/067-flashattention-4-blog-post-by-tri-dao.md`
  - 메모: --- title: FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | Tri Dao source_url: https://tridao.me/blog/2026/flash4 final_url: https://tridao.me/blog/2026/flash4/ status: 200 content_type: text/html; charset=utf-8 topics: [FlashAttentio
- [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling – Princeton Laboratory for Artificial Intelligence Research Blog](https://blog.ai.princeton.edu/2026/03/12/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling) — `raw/hot-topics-sources/2026-04-10/068-flashattention-4-princeton-ai-lab-blog.md`
  - 메모: --- title: FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling – Princeton Laboratory for Artificial Intelligence Research Blog source_url: https://blog.ai.princeton.edu/2026/03/12/flashattention-4-algorithm-and-kernel-pipelining-co-design-
- [GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact attention · GitHub](https://github.com/Dao-AILab/flash-attention) — `raw/hot-topics-sources/2026-04-10/069-dao-ailab-flash-attention-github-repository.md`
  - 메모: --- title: GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact attention · GitHub source_url: https://github.com/Dao-AILab/flash-attention final_url: https://github.com/Dao-AILab/flash-attention status: 200 content_type: text/html; charset=utf-8 topics: [FlashAtte
- [Blog – PyTorch](https://pytorch.org/blog) — `raw/hot-topics-sources/2026-04-10/070-generalized-dot-product-attention-pytorch-blog.md`
  - 메모: --- title: Blog – PyTorch source_url: https://pytorch.org/blog final_url: https://pytorch.org/blog/ status: 200 content_type: text/html; charset=UTF-8 topics: [FlashAttention-4 on Blackwell] sections: [Inference Optimization] fetched_at: 2026-04-10T01:43:34.352415+00:00 --- # Blo

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[nvfp4-quantization|NVFP4 Quantization for LLM Inference]]

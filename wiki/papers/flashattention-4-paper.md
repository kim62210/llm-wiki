---
title: FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling
category: papers
page_type: paper
tags: [paper, inference, attention, gpu-kernels]
sources: [raw/hot-topics-sources/2026-04-10/066-flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardwa.md]
created: 2026-04-10
updated: 2026-04-10
---

# FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

Blackwell GPU의 비대칭 하드웨어 스케일링에 맞춰 attention kernel을 다시 설계한 FlashAttention-4 논문이다.

## 핵심 기여

- Hopper 중심 최적화였던 FlashAttention-3를 넘어 Blackwell 병목에 맞춘 재설계
- 비동기 MMA, larger tile, softmax 관련 non-matmul 연산 축소 기법 제안
- CuTe-DSL 기반 구현으로 C++ template 대비 빠른 compile time 확보

## 결과와 시사점

- B200 BF16에서 cuDNN 9.13 대비 최대 1.3배, Triton 대비 2.7배 속도 향상
- 최대 1613 TFLOPs/s, 71% utilization 도달

## 한계

특정 세대 GPU(Blackwell)에 강하게 최적화되어 있어, 범용 attention 최적화라기보다 아키텍처 종속성이 크다.

## 실무 적용 관점

추론 최적화는 더 이상 알고리즘만의 문제가 아니라 **GPU 세대별 병목 구조와 커널 설계의 공동 최적화**라는 점을 보여준다.

## 관련 문서

- [[flashattention-4]]
- [[disaggregated-serving]]
- [[tensorrt-llm]]

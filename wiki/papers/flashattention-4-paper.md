---
title: [[flash-[[self-attention-mechanism|attention]]-fundamentals|FlashAttention]]-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling
category: papers
page_type: paper
tags: [paper, inference, attention, gpu-kernels]
sources: [raw/hot-topics-sources/2026-04-10/066-flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardwa.md]
created: 2026-04-10
updated: 2026-04-13
---
# FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

Blackwell [[blackwell-ultra-b300|GPU]]의 비대칭 하드웨어 스케일링에 맞춰 attention kernel을 다시 설계한 FlashAttention-4 논문이다.

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

## 문제 설정

`FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling`는 **장기 과제에서 모델/에이전트 성능을 어떻게 끌어올리는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다

## 리뷰 포인트

- `FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **2603.05451 FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling** — https://arxiv.org/abs/2603.05451 · 초록 단서: Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications. While FlashAttention-3 optimize... · snapshot: `raw/hot-topics-sources/2026-04-10/066-flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardwa.md`

## 관련 문서
- [[flash-decoding]] -- Flash Decoding (KV 시퀀스 분할 병렬 디코딩)

- [[flashattention-4]]
- [[disaggregated-serving]]
- [[tensorrt-llm]]

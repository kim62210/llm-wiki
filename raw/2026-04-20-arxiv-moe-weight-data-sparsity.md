---
source: arxiv
arxiv_id: "2601.15370"
title: "Improving MoE Compute Efficiency by Composing Weight and Data Sparsity"
authors: ["Maciej Kilian", "Oleg Mkrtchyan", "Luke Zettlemoyer", "Akshat Shrivastava", "Armen Aghajanyan"]
date: 2026-01-21
url: "https://arxiv.org/abs/2601.15370"
fetched: 2026-04-20
status: pending_ingest
tags: [mixture-of-experts, sparsity, load-balancing, null-experts, autoregressive, multimodal, compute-efficiency]
---

## Abstract

MoE(Mixture-of-Experts) layer는 **weight sparsity**(각 토큰이 일부 expert만 활성화)로 compute 효율을 얻는다. 이 논문은 **data sparsity**(각 expert가 일부 token만 처리)를 complementary 축으로 도입하고, autoregressive 모델에서 causality 위반 없이 결합하는 방법을 제안.

## 핵심 혁신: Null Experts

- **문제**: Expert-choice routing은 causality를 위반 → autoregressive 설정에서 쓸 수 없음
- **해결**: Routing pool에 zero-compute "null experts" 추가
- 표준 load balancing objective가 real + null expert 사이 uniform 사용을 학습 → **expectation 기준 data sparsity** 생성, causality 유지

## 구조

| Sparsity 유형 | 메커니즘 |
|---------------|----------|
| **Weight sparsity** | 토큰이 일부 expert만 활성화 (기존 MoE) |
| **Data sparsity** | Null expert로 routing되는 토큰은 compute 0 (신규) |

## 주요 결과

- **Compute-efficient frontier** 개선 — weight sparsity 단독 대비 더 나은 FLOP-loss trade-off
- Training loss와 downstream task 둘 다 개선
- **Modality-aware routing 자발적 등장**: vision token은 text token보다 null expert로 더 자주 routing됨 (explicit modality routing 없이도)

## 시사점

- Multimodal MoE에서 "modality-specific compute"를 자동으로 할당하는 mechanism
- Null expert는 "skip connection의 MoE 버전"처럼 작동
- Autoregressive + expert-choice의 오랜 긴장 해결

## 기존 페이지 업데이트 후보

- `wiki/papers/moe-scaling-laws-paper.md` (2604.09175)에 대비되는 구현 측면
- `wiki/architectures/mixture-of-experts.md` — null expert 개념 추가
- `wiki/concepts/load-balancing-moe.md` (신규 생성 가능)

## Raw 요약 키워드
MoE, null expert, data sparsity, weight sparsity, load balancing, expert-choice routing, causality, autoregressive MoE, modality-aware routing

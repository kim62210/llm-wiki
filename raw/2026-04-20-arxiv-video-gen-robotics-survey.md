---
source: arxiv
arxiv_id: "2601.07823"
title: "Video Generation Models in Robotics -- Applications, Research Challenges, Future Directions"
authors: ["Zhiting Mei", "Tenny Yin", "Ola Shorinwa", "Apurva Badithela", "Zhonghe Zheng", "Joseph Bruno", "Madison Bland", "Lihan Zha", "Asher Hancock", "Jaime Fernández Fisac", "Philip Dames", "Anirudha Majumdar"]
date: 2026-01-12
url: "https://arxiv.org/abs/2601.07823"
fetched: 2026-04-20
status: pending_ingest
tags: [video-generation, robotics, world-model, embodied-ai, imitation-learning, policy-evaluation, survey]
---

## Abstract

Video generation 모델이 "physical world의 고충실도 모델"로서 로보틱스에서 어떻게 쓰이는지 체계적으로 정리한 survey. Photorealistic 시뮬레이션을 제약 가정 없이 생성하며, 전통적 physics simulator의 한계(rigid body 중심, deformable/접촉 모델링의 제약)를 극복.

## 주요 응용

- **Imitation learning**: 합성 데모 생성
- **Reinforcement learning**: 가상 환경 상호작용
- **Visual planning**: 미래 관측 예측 기반 계획
- **Policy evaluation**: 저비용 closed-loop 시뮬레이션

## Video-as-World-Model 관점

- Photorealistic + physically consistent deformable-body 시뮬레이션
- Language-only abstraction보다 더 expressive한 world model
- Cost-effective 데이터 생성, action prediction, dynamics modeling, reward modeling 가능

## 핵심 도전 과제

| 범주 | 문제 |
|------|------|
| **신뢰성** | Instruction following 불량, hallucination(물리 법칙 위반), unsafe 콘텐츠 |
| **계산 비용** | 훈련·추론 모두 막대한 연산 필요 |
| **데이터 큐레이션** | 로보틱스용 고품질 비디오 데이터셋 부족 |
| **Safety-critical 적용** | 자율주행·의료 로봇 같은 영역에서 검증 필요 |

## 미래 방향

- Physics 위반 감지·보정 내장 video model
- 보다 효율적 아키텍처 (edge deployment 가능 수준)
- Sim-to-real gap 좁히기 위한 domain randomization 개선
- Trustworthiness 인증 프레임워크

## 실무 시사점

- NVIDIA Cosmos 같은 Physical AI foundation model이 이 방향의 구현체
- Sim2Real/Real2Real 변환이 robotics RL에서 core bottleneck 완화
- 기존 AR/VR 비디오 모델 → 로봇 policy 평가용으로 재활용 trend

## Raw 요약 키워드
embodied world model, video foundation model, imitation learning, policy evaluation, Sim2Real, physics violation, deformable body simulation

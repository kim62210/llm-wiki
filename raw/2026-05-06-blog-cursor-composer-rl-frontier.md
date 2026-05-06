---
source: blog
url: https://cursor.com/blog/composer
title: "Composer: Building a fast frontier model with RL"
author: Cursor team
date: 2025-10-29
fetched: 2026-05-06
status: pending_ingest
tags: [cursor, composer, agent-model, mixture-of-experts, reinforcement-learning, async-rl]
---

# Composer: Building a Fast Frontier Model with RL (Cursor)

## 핵심 발표

Cursor가 자체 코딩 에이전트 모델 **Composer**를 공개. 핵심 주장:

> "Composer achieves frontier coding results with generation speed four times faster than similar models."

기존 클로즈드 SOTA 대비 4배 빠른 생성 속도, 30초 미만 인터랙션.

## 아키텍처

- **Mixture-of-Experts (MoE)** 언어 모델
- 긴 컨텍스트 윈도우 지원
- **강화학습(RL)**으로 다양한 개발 환경에서 특화 훈련

## 트레이닝 인프라

자체 트레이닝 시스템 (PyTorch + Ray) - 대규모 비동기 강화학습:

- **Native low-precision training**: "MXFP8 MoE kernels with expert parallelism and hybrid sharded data parallelism"
- **Scale**: "thousands of NVIDIA GPUs with minimal communication cost"
- **RL 환경**: 수십만 개의 동시 샌드박스 코딩 환경

## 트레이닝 시 도구 접근

훈련 중 모델은 production search/edit 도구를 사용해 다양한 어려운 문제를 효율적으로 해결하도록 학습:
- 파일 읽기/편집
- 터미널 명령어 실행
- 코드베이스 전반 시맨틱 검색

훈련을 통해 학습되는 자율 능력:
- 복잡한 검색
- 린터 에러 수정
- 단위 테스트 작성·실행

## Cursor Bench (내부 벤치마크)

- 실제 Cursor 엔지니어/연구자의 에이전트 요청
- 손으로 큐레이션된 최적 솔루션
- 평가: **정확성** + **기존 코드 추상화 준수도**

## 성능 포지셔닝

- 빠른 frontier 모델 (Haiku 4.5, Gemini Flash 2.5)보다는 위
- GPT-5, Sonnet 4.5에 비해서는 아래

## 메모

- 게시일: 2025년 10월 29일
- 카테고리: Research
- Composer는 Cursor 2.0의 핵심 신기능
- 참고: Composer 2 (후속) 공개 시 Kimi K2.5 base에서 continued pretraining 후 RL

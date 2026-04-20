---
source: web
title: "JEPA & World Models - Joint Embedding Predictive Architecture"
url: "https://introl.com/blog/world-models-race-agi-2026"
date: 2026-03-15
fetched: 2026-04-15
status: pending_ingest
---

## Overview

World Model은 환경의 역학을 내부적으로 모사하는 AI 모델. JEPA(Joint Embedding Predictive Architecture)는 LeCun이 제안한 프레임워크로, 고차원 공간이 아닌 추상적 표현 공간에서 미래 상태를 예측하는 접근.

## JEPA Core Idea

- 생성 모델은 고차원 디테일(픽셀 단위)에서 미래를 예측하므로 본질적으로 부정확
- JEPA는 추상적 표현 공간에서 예측 -- "중요한 것"만 학습
- 입력과 목표를 같은 임베딩 공간에 매핑 후, 표현 수준에서 예측

## I-JEPA (Image Joint Embedding Predictive Architecture)

- Meta에서 2023년 발표, LeCun의 비전 최초 실현
- 이미지의 일부에서 나머지를 표현 공간에서 예측
- 피셀 단위 재구성 대신 의미적 표현 예측
- 자기지도학습으로 라벨 없이 시각적 표현 학습

## 2026 World Models Race

- AMI Labs (LeCun): $1.03B 시드, JEPA 기반
- Google DeepMind: Genie 2, 시뮬레이션 기반
- NVIDIA Cosmos: Physical AI 플랫폼
- 로보틱스, 자율주행, 산업 시뮬레이션에서 핵심 기술로 부상

## LLM vs World Models

- LLM: 텍스트 토큰 예측, 언어에 특화
- World Model: 물리적 세계의 동적 모사, 멀티모달
- LeCun: "현재 LLM 집착은 잘못된 방향, world model이 진정한 AGI 경로"

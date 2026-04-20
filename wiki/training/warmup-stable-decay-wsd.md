---
title: Warmup-Stable-Decay (WSD) 스케줄러
category: training
page_type: concept
tags: [wsd, learning-rate, scheduler, continual-pretraining, checkpoint-reuse]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-17
updated: 2026-04-17
---

# Warmup-Stable-Decay (WSD) 스케줄러

3단계 학습률 스케줄: **워밍업 -> 안정(plateau) -> 짧은 감쇠**. 코사인 스케줄과 달리 안정 구간의 체크포인트를 재사용할 수 있어 **지속 사전학습(continual pretraining)**에 적합하다.

## 3단계 구조

```mermaid
flowchart LR
    W[1. Warmup<br/>선형 증가<br/>~2000 steps] --> S[2. Stable<br/>최대 LR 유지<br/>전체의 80-90%]
    S --> D[3. Decay<br/>급격한 감쇠<br/>~10% steps]
    S -.->|체크포인트 재사용| S2[새 데이터로 이어서 학습]
    S2 --> D2[3. Decay]
```

## 코사인 스케줄과의 비교

| 측면 | 코사인 | WSD |
|------|--------|-----|
| 감쇠 형태 | 전체 구간 코사인 곡선 | 마지막 10%에서 급감쇠 |
| 체크포인트 재사용 | 어려움 (이미 감쇠 중) | 용이 (안정 구간) |
| 최종 성능 | 동등 | 동등 (감쇠 후) |
| 지속 학습 | 비적합 | **최적** |

## MiniCPM/Phi-3 적용

MiniCPM과 Phi-3은 WSD의 변형을 채택:
- 1차 일반 웹 데이터로 안정 구간까지 학습
- [[mid-training-phase|Mid-Training]]에서 고품질 데이터로 안정 구간 연장
- 최종 감쇠로 수렴

## 관련 문서

- [[learning-rate-scheduling]] -- 학습률 스케줄링 전체
- [[compute-optimal-training]] -- 연산 최적 학습
- [[domain-adaptive-continual-pretraining]] -- DACP
- [[mid-training-phase]] -- Mid-Training Phase

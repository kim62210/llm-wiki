---
title: LLM 하이퍼파라미터 탐색 (Hyperparameter Search for LLMs)
category: training
page_type: concept
tags: [hyperparameter, mup, proxy-model, bayesian-optimization]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# LLM 하이퍼파라미터 탐색 (Hyperparameter Search for LLMs)

## 개념 요약

LLM 학습의 하이퍼파라미터(HPO, Hyperparameter Optimization)는 수조 개 토큰, 수천 개 GPU로 학습하는 환경에서 직접 탐색하기 불가능하다. 현대적 접근은 **소형 프록시 모델(proxy model)** 에서 탐색 후 대형 모델로 전이하는 원칙에 기반한다.

## muP (Maximal Update Parameterization)

Yang & Hu (2022) "Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer"에서 제안.

**핵심 아이디어**: 모델 너비(width)에 따라 파라미터 초기화와 학습률을 특정 방식으로 스케일하면, 작은 모델에서 찾은 최적 하이퍼파라미터가 큰 모델에서도 동일하게 작동한다.

### 표준 파라미타이제이션 vs muP

| 항목 | Standard Parameterization (SP) | muP |
|------|-------------------------------|-----|
| 가중치 초기화 | $\sigma \propto 1/\sqrt{n}$ | 레이어 유형별 별도 스케일 |
| 최적 학습률 | 너비 변화 시 재탐색 필요 | 너비에 **전이 가능** |
| Attention 스케일 | $1/\sqrt{d}$ | $1/d$ |
| 출력 레이어 | 표준 | 별도 스케일 감소 |

### muP 워크플로우

```mermaid
flowchart LR
    Small["소형 프록시 모델\n예: 40M~200M 파라미터"]
    HPO["HPO 실행\n학습률/배치 크기/warmup 탐색"]
    Transfer["최적 HP 전이\n크기 불변 HP 직접 사용"]
    Large["대형 목표 모델\n예: 7B~70B 파라미터"]
    Small --> HPO --> Transfer --> Large
```

Microsoft의 연구에서 muP로 탐색된 HP를 6.7B 모델에 적용해 재탐색 없이 좋은 성능을 달성했다.

## Proxy Scaling Laws

소형 모델의 벤치마크 성능이 대형 모델의 성능과 단조 상관관계를 가지면, 소형 모델을 proxy로 사용할 수 있다.

- 여러 HP 설정을 소형 모델(예: 100M, 1B)로 평가
- 소형에서 상대적으로 우수한 설정이 대형에서도 우수하다고 가정
- 단, 특정 능력(in-context learning, instruction following)은 모델 크기에 창발적으로 나타나 proxy가 부정확할 수 있음

## 실용적 HPO 범위

LLM 실전 학습에서 탐색하는 하이퍼파라미터 범위:

| 하이퍼파라미터 | 실용 범위 | 비고 |
|--------------|-----------|------|
| 학습률 (lr) | 1e-5 ~ 1e-3 | 보통 3e-4 부근이 sweet spot |
| Warmup 비율 | 0.5% ~ 5% | 전체 스텝 대비 |
| 배치 크기 | 512K ~ 4M 토큰 | 토큰 단위 |
| 가중치 감쇠 (weight decay) | 0.01 ~ 0.1 | |
| 그래디언트 클리핑 | 0.5 ~ 2.0 | 보통 1.0 |
| 드롭아웃 | 0 ~ 0.1 | 사전학습에서는 보통 0 |

## HPO 탐색 전략 비교

### Grid Search (격자 탐색)

- 사전 정의된 모든 조합 시도
- 2-3개 파라미터, 각 3-5개 값: 27-125개 실험 - 소형 모델에서 가능
- 차원이 늘어날수록 지수적 폭발

### Random Search (무작위 탐색)

- 연속 분포에서 무작위 샘플링
- Bergstra & Bengio (2012): 대부분 상황에서 Grid보다 효율적
- 중요하지 않은 파라미터의 낭비 제거

### Bayesian Optimization (베이즈 최적화)

- 이전 실험 결과를 바탕으로 **가장 유망한 다음 설정 선택**
- 가우시안 프로세스(GP) 또는 TPE(Tree-structured Parzen Estimator) 사용
- 실험 수를 최소화하면서 탐색 - LLM 학습처럼 비용이 비쌀 때 유리
- 라이브러리: Optuna, Ray Tune, Weights & Biases Sweeps

### Successive Halving / Hyperband

- 많은 설정을 짧게 실험 -> 성능 하위 절반 제거 -> 남은 것을 더 길게 실험
- 제한된 예산 내에서 좋은 설정을 빠르게 식별
- ASHA(Asynchronous Successive Halving): 비동기 분산 버전

## 실전 권장

1. muP를 사전 적용해 스케일링 안정성 확보
2. 소형 프록시(100M~1B)로 Bayesian Optimization 20-50회 실행
3. 학습률과 배치 크기를 가장 먼저 탐색 (영향력 최대)
4. 선택된 HP를 중간 크기(예: 1B)에서 검증 후 대형 모델에 적용

## 관련 문서

- [[neural-scaling-laws]] - 모델 크기와 성능의 관계
- [[learning-rate-scheduling]] - 학습률 스케줄러 설계
- [[adamw-optimizer]] - AdamW의 HP 설정
- [[training-stability]] - HP가 안정성에 미치는 영향

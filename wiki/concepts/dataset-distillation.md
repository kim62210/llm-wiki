---
title: 데이터셋 증류 (Dataset Distillation)
category: concepts
page_type: concept
tags: [데이터셋증류, synthetic데이터, 데이터압축, 메타학습, 코어셋]
sources: [raw/2026-04-17-topic-queue-v2.md]
created: 2026-04-17
updated: 2026-04-17
---

# 데이터셋 증류 (Dataset Distillation)

데이터셋 증류(dataset distillation)는 대규모 실제 데이터셋의 핵심 정보를 소수의 합성(synthetic) 예시에 압축하는 기법이다. 증류된 소형 데이터셋으로 학습한 모델이 원본 전체 데이터셋으로 학습한 모델에 가까운 성능을 내는 것이 목표다.

## 핵심 아이디어

```mermaid
flowchart LR
    ORIG[원본 데이터셋\n수십만 ~ 수억 샘플] --> DISTILL[데이터셋 증류\n알고리즘]
    DISTILL --> SYNTH[합성 데이터셋\n수십 ~ 수천 샘플]
    SYNTH -->|동일 품질로 학습| MODEL[학습된 모델]
    ORIG -->|전체 학습| MODEL2[학습된 모델]
    MODEL -.->|성능 근사| MODEL2
```

MNIST 전체(60,000 샘플) 대신 클래스당 1개(총 10개)의 합성 이미지로 거의 동등한 성능을 달성하는 것이 초기 연구의 목표였다. 이후 ImageNet, NLP, 코드 데이터에도 확장됐다.

## 왜 필요한가

- **반복 실험 가속**: 소형 증류 데이터셋으로 아키텍처/하이퍼파라미터 탐색 비용 절감
- **연속 학습(continual learning)**: 이전 태스크 데이터를 소수 합성 예시로 요약하여 망각(forgetting) 완화
- **프라이버시**: 실제 데이터 대신 합성 데이터로 공유 가능
- **데이터 효율 학습**: 레이블이 비싼 도메인에서 적은 예시로 최대 효과

## 주요 방법론

### 1. 메타 학습 기반 (원조 방법, Wang et al. 2018)

합성 데이터셋 S를 `외부 변수(outer variable)`로 취급하고, 내부 최적화(inner optimization)는 S로 모델을 학습시키며, 외부 최적화(outer optimization)는 학습된 모델이 원본 검증 세트에서 잘 동작하도록 S를 갱신한다.

```mermaid
flowchart TD
    S[합성 데이터셋 S 초기화] --> INNER[내부 루프\nS로 모델 파라미터 학습\n수 스텝 SGD]
    INNER --> OUTER[외부 루프\n검증 손실로 S 자체를 역전파\ndS = -lr * grad_S(L_val)]
    OUTER --> S
    S -->|수렴 시| RESULT[최적 합성 데이터셋]
```

이 이중 최적화(bi-level optimization)는 계산 비용이 높다. 내부 루프의 전개(unroll) 깊이만큼 메모리가 필요하다.

### 2. 커널 매칭 (Kernel Ridge Regression, KRR)

신경 접선 커널(Neural Tangent Kernel, NTK) 이론을 활용한다. 무한 넓이 네트워크에서 학습 동역학이 커널 방정식으로 근사 가능함을 이용해 합성 데이터셋이 원본과 동일한 커널 리지 회귀 솔루션을 내도록 최적화한다.

계산적으로 더 효율적이며, 커널 함수 선택이 핵심이다.

### 3. 분포 매칭 (Distribution Matching)

합성 데이터셋으로 학습한 모델의 중간 특징(feature) 분포가 실제 데이터로 학습한 모델의 분포와 일치하도록 최적화한다.

```python
# 분포 매칭 손실 (개념적)
loss = MMD(features(synthetic), features(real))
# MMD: Maximum Mean Discrepancy
```

### 4. 그래디언트 매칭 (DC, Dataset Condensation)

합성 데이터셋으로 계산한 그래디언트가 실제 데이터셋의 그래디언트와 일치하도록 최적화한다. Zhao et al. (2020) DC(Dataset Condensation) 방법이 대표적이다.

```mermaid
flowchart LR
    REAL[실제 배치] -->|그래디언트 계산| GR[grad_real]
    SYNTH2[합성 데이터] -->|그래디언트 계산| GS[grad_synth]
    GR --> MATCH[그래디언트 일치 손실\n||grad_real - grad_synth||^2]
    GS --> MATCH
    MATCH -->|역전파| SYNTH2
```

### 5. 궤적 매칭 (MTT, Match Training Trajectories)

실제 데이터로 학습한 모델의 파라미터 궤적(trajectory)을 합성 데이터로 재현하도록 최적화한다. 단순 그래디언트 매칭보다 장기 학습 효과를 더 잘 포착한다.

## 코어셋(Coreset)과의 비교

| 항목 | 코어셋 | 데이터셋 증류 |
|------|--------|--------------|
| 데이터 형태 | 실제 데이터 중 선택 | 합성(최적화된) 데이터 |
| 원본 데이터 포함 여부 | 항상 원본 샘플 | 원본과 다를 수 있음 |
| 최적화 대상 | 선택 인덱스 | 데이터 픽셀/값 자체 |
| 생성 비용 | 낮음 | 높음 (이중 최적화) |
| 압축 비율 | 보통 낮음 | 매우 높을 수 있음 |

## LLM 시대의 데이터셋 증류

대형 언어 모델 시대에는 데이터셋 증류의 개념이 **합성 데이터 생성(synthetic data generation)**으로 확장됐다. LLM을 활용해 고품질 학습 데이터를 생성하고, 그 중 소수의 고밀도 예시로 소형 모델을 파인튜닝하는 패턴이 일반화됐다(예: Alpaca, Self-Instruct 계열).

## 한계

- 이중 최적화의 계산 비용: 대규모 데이터셋과 모델에 적용하기 어려움
- 아키텍처 의존성: 특정 아키텍처에서 증류된 데이터가 다른 아키텍처에 이전(transfer)되지 않을 수 있음
- 분포 외(OOD) 견고성: 증류 데이터로 학습한 모델이 분포 외 입력에 취약할 수 있음

## 왜 중요한가

[[data-centric-ai]] 관점에서 데이터셋 증류는 데이터 자체를 학습 가능한 대상으로 보는 혁신적 접근이다. [[knowledge-distillation-theory]]가 모델을 압축하듯, 데이터셋 증류는 데이터를 압축한다. 두 기법을 결합하면 극도로 효율적인 소형 모델-소형 데이터 파이프라인을 구성할 수 있다.

## 관련 문서

- [[data-centric-ai]] - 데이터 품질 중심 AI 개발 패러다임
- [[knowledge-distillation-theory]] - 모델 지식 증류 이론
- [[label-noise-learning]] - 노이즈 레이블 환경에서의 강건 학습
- [[data-annotation]] - 데이터 레이블링 전략과 품질 관리

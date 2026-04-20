---
title: 그래디언트 클리핑 (Gradient Clipping)
category: training
page_type: concept
tags: [gradient-clipping, training-stability, gradient-explosion]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 그래디언트 클리핑 (Gradient Clipping)

## 개념 요약

그래디언트 클리핑(Gradient Clipping)은 역전파(backpropagation) 중 계산된 그래디언트의 크기를 제한하여 **그래디언트 폭발(gradient explosion)** 을 방지하는 기법이다. 특히 Transformer 기반 LLM 학습에서 학습 안정성의 기본 구성 요소로 사용된다.

## 두 가지 클리핑 방식

### 1. Norm Clipping (노름 클리핑) - 권장

전체 파라미터의 그래디언트 벡터 노름(norm)이 임계값을 초과할 때 균일하게 스케일 다운한다.

$$
g \leftarrow g \cdot \frac{\text{clip\_norm}}{\max(\|g\|_2,\ \text{clip\_norm})}
$$

- 방향은 보존하고 크기만 제한
- 업데이트 방향의 의미가 유지됨

### 2. Value Clipping (값 클리핑)

각 그래디언트 원소를 개별적으로 `[-threshold, threshold]` 범위로 자른다.

$$
g_i \leftarrow \text{clip}(g_i,\ -\text{threshold},\ +\text{threshold})
$$

- 구현이 단순하지만 방향이 왜곡될 수 있음
- 현재는 대부분 Norm Clipping을 사용

## 임계값 선택

LLM 학습에서 `clip_norm = 1.0`이 가장 흔한 기본값이다.

| 모델/설정 | clip_norm |
|----------|-----------|
| GPT-2, GPT-3 | 1.0 |
| LLaMA 계열 | 1.0 |
| Chinchilla | 1.0 |
| 소형 실험 모델 | 0.5 - 5.0 |

임계값이 너무 작으면 학습이 느려지고, 너무 크면 클리핑이 실질적으로 작동하지 않는다. 훈련 초반 그래디언트 노름 분포를 모니터링해 설정한다.

## Per-Layer vs Global Norm

**Global Norm(전역 노름)**: 모든 레이어의 그래디언트를 하나의 벡터로 연결해 단일 노름을 계산 후 클리핑. 표준적인 방법.

$$
\|g\|_{global} = \sqrt{\sum_{l} \|g_l\|_2^2}
$$

**Per-Layer Norm(레이어별 노름)**: 각 레이어를 독립적으로 클리핑. 특정 레이어의 폭발을 더 정밀하게 제어할 수 있으나 레이어 간 상대적 크기 정보를 잃는다.

## Adaptive Gradient Clipping (AGC)

Brock et al. (2021, NFNets)에서 제안한 기법. 그래디언트 노름을 파라미터 노름에 비례해 클리핑한다.

$$
\lambda_l = \frac{\|W_l\|_F}{\|g_l\|_F}, \quad g_l \leftarrow \min\left(1,\ \frac{\lambda_l \cdot \text{clip\_factor}}{\|g_l\|_F}\right) \cdot g_l
$$

- 레이어별 파라미터 스케일에 적응적으로 동작
- BatchNorm 없이도 대규모 배치 학습을 안정화
- LLM에서는 아직 Global Norm Clipping이 더 보편적

## LLM 학습에서의 실전 설정

```python
# PyTorch 예시
optimizer.zero_grad()
loss.backward()
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
optimizer.step()
```

- **모니터링**: 그래디언트 노름을 매 스텝 로깅. 클리핑 발동 빈도가 너무 높으면 학습률을 낮추거나 모델 구조를 점검
- **Loss Spike 관계**: 갑작스러운 loss spike 직후 그래디언트 노름이 급증하는 패턴이 일반적. 클리핑이 spike를 완전히 방지하지는 못하지만 확산을 억제
- **Mixed Precision**: FP16/BF16 학습 시 그래디언트 스케일러(GradScaler)와 함께 사용. 스케일러가 오버플로우를 감지하면 해당 스텝의 업데이트를 건너뜀

## 관련 문서
- [[loss-spike-training-instability]] -- Loss Spike와 훈련 불안정성

- [[training-stability]] - 학습 안정성 전반
- [[loss-spike-debugging]] - 그래디언트 폭발 디버깅
- [[gradient-norm-monitoring]] - 노름 모니터링 실천법
- [[mixed-precision-training]] - FP16/BF16과의 연동
- [[adamw-optimizer]] - 옵티마이저와의 상호작용

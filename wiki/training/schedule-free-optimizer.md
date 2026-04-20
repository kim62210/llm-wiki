---
title: Schedule-Free 옵티마이저
category: training
page_type: concept
tags: [optimizer, schedule-free, polyak-averaging, adam, SGD]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# Schedule-Free 옵티마이저

## 개요

Schedule-Free 옵티마이저는 학습률 스케줄(learning rate schedule) 없이도 수렴 성능을 유지하는 최적화 알고리즘이다. 기존 Adam, SGD 계열 옵티마이저는 워밍업(warmup), 코사인 감쇠(cosine decay), 선형 감쇠 등의 스케줄을 전제로 설계되어 있어 학습 토큰 수(budget)를 사전에 고정해야 했다. Schedule-Free는 이 제약을 제거하여 "언제든지 멈춰도 좋은" 유연한 학습을 가능하게 한다.

## 핵심 아이디어: Polyak-Ruppert 평균화

Schedule-Free의 핵심은 **Polyak-Ruppert 평균화(Polyak averaging)**다. 일반 옵티마이저가 단일 파라미터 궤적을 따라 이동하는 반면, Schedule-Free는 두 종류의 파라미터를 동시에 관리한다.

| 파라미터 | 역할 |
|----------|------|
| $x_t$ (기울기 계산용) | 실제 업데이트가 일어나는 점 (fast weights) |
| $z_t$ (평균 파라미터) | 지수 이동 평균된 점 (slow weights) |

추론(inference) 시에는 $z_t$를 사용하고, 기울기 계산은 보간된 점 $y_t = (1-\beta) z_t + \beta x_t$ 에서 수행한다. 이 설계 덕분에 학습 마지막 단계에서 스케줄이 "LR을 0으로 줄이며 수렴"하는 효과를 내부적으로 대체한다.

```mermaid
flowchart TD
    A[스텝 t에서 기울기 계산] --> B["보간점 y_t 계산\ny_t = (1-β)z_t + βx_t"]
    B --> C[∇f(y_t) 계산]
    C --> D["x_t 업데이트\n(Adam/SGD 규칙 적용)"]
    D --> E["z_t 업데이트\n(Polyak 평균화)"]
    E --> F{추론 필요?}
    F -- Yes --> G[z_t 사용]
    F -- No --> B
```

위 흐름에서 $z_t$는 훈련 내내 축적된 평균이므로 마지막 체크포인트에서 최고의 품질을 제공한다.

## 기존 스케줄 기반 접근과의 비교

기존 훈련에서는 [[learning-rate-scheduling]]이 필수적이다. Cosine Annealing 기준으로, 학습 초반에 낮은 LR로 시작해 중반에 최고점에 달한 뒤 마지막에 0 부근으로 수렴한다. 이 방식의 문제는:

1. **Budget 고정 강제**: 총 학습 스텝을 미리 정해야 한다.
2. **중간 체크포인트 품질 저하**: 스케줄 중간에 멈추면 성능이 나쁘다.
3. **Continual Learning 부적합**: 추가 학습 시 스케줄 재설계가 필요하다.

Schedule-Free는 이 세 가지를 모두 해결한다. 학습을 어느 시점에서 중단해도 $z_t$ 파라미터가 좋은 품질을 보장한다.

## 알고리즘 변형

**Schedule-Free SGD**:
$$z_{t+1} = z_t - \alpha \nabla f(y_t)$$
$$x_{t+1} = x_t - \alpha \nabla f(y_t)$$
$$y_{t+1} = (1 - c \cdot \beta) z_{t+1} + c \cdot \beta \cdot x_{t+1}$$

**Schedule-Free AdamW**: 위 구조에 Adam의 모멘트 추정($m_t$, $v_t$)과 가중치 감쇠(weight decay)를 결합한다. 가중치 감쇠는 $x_t$에 적용하며 [[optimization-theory]]의 L2 정규화 해석과 일치한다.

## 실용적 고려사항

- **워밍업 여전히 권장**: Schedule-Free 자체는 스케줄이 필요 없지만, 초기 몇 백 스텝의 워밍업은 수치 안정성을 위해 권장된다.
- **$\beta$ 하이퍼파라미터**: Polyak 평균화 비율. 보통 $\beta = 0.9$ 또는 $0.999$를 사용하며 모델 크기에 따라 조정한다.
- **학습률 선택**: 스케줄이 없으므로 peak LR 값 선택이 기존보다 중요하다. 기존 최적 peak LR보다 약간 낮게 시작하는 것이 안전하다.
- **Finetuning 적용**: 사전학습뿐 아니라 SFT, DPO 등 파인튜닝 단계에도 적용 가능하다.

## 성능 특성

Meta AI의 원논문(Aaron Defazio et al., 2024)에서 다음을 보고했다:

- ImageNet, LLM 학습 등 다양한 벤치마크에서 잘 조정된 코사인 스케줄과 **동등하거나 우수한 성능**
- Continual pretraining 시나리오에서 스케줄 기반 대비 명확한 우위
- 파이토치(PyTorch) 공식 구현으로 `schedulefree` 패키지 제공

## 한계

- **Checkpoint 전략 변경 필요**: 추론용 파라미터($z_t$)와 훈련용 파라미터($x_t$)를 별도 저장해야 한다.
- **초대형 모델 실증 부족**: 수백 B 파라미터 규모 LLM 학습 사례가 아직 제한적이다.
- **분산 학습 통합**: FSDP, Tensor Parallelism과의 통합 시 추가 구현 고려가 필요하다.

## 관련 문서

- [[optimization-theory]] - 볼록 최적화, SGD 수렴 이론 기반
- [[learning-rate-scheduling]] - 기존 스케줄 방식과의 비교
- [[muon-optimizer]] - 또 다른 스케줄-프리 계열 옵티마이저
- [[adamw-optimizer]] - Schedule-Free AdamW의 기반 알고리즘
- [[continual-pretraining]] - Schedule-Free가 특히 유리한 시나리오

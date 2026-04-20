---
title: 행동 복제 (Behavior Cloning)
category: concepts
page_type: concept
tags: [behavior-cloning, imitation-learning, supervised-learning, robotics]
sources: []
created: 2026-04-20
updated: 2026-04-20
---

# 행동 복제 (Behavior Cloning)

## 정의

행동 복제(Behavior Cloning, BC)는 [[imitation-learning|모방 학습(imitation learning)]]의 가장 단순한 형태로, 전문가(expert)의 (상태, 행동) 쌍 데이터를 지도 학습(supervised learning)으로 학습하여 정책(policy)을 직접 복사하는 방법이다. 강화 학습(RL)처럼 환경과의 상호작용 없이, 전문가 데이터만으로 정책 $\pi_\theta$를 학습한다.

목표는 전문가 정책 $\pi^*$를 흉내 내도록 $\pi_\theta$를 학습하는 것으로, 손실 함수는 단순한 크로스 엔트로피 또는 MSE다:

$$\mathcal{L}(\theta) = \mathbb{E}_{(s,a) \sim \mathcal{D}_\text{expert}} \left[ \| \pi_\theta(s) - a \|^2 \right]$$

## 학습 파이프라인

```mermaid
flowchart LR
    E[전문가] -->|시연| D[데이터셋\n(s, a) 쌍]
    D -->|지도 학습| P[정책 학습\nπ_θ]
    P -->|배포| Env[환경 실행]
    Env -->|분포 이탈| Err[오류 누적\nCompounding Error]
```

전문가의 시연 데이터를 수집해 지도 학습으로 정책을 학습한다. 배포 후 분포 이탈(distribution shift)이 발생하면 오류가 누적되는 구조적 취약점이 있다.

## 장점

- **단순성**: 별도의 보상 함수 설계 없이 전문가 데이터만 있으면 된다.
- **안정성**: 일반 지도 학습이므로 학습 과정이 안정적이다.
- **데이터 효율**: 소규모 전문가 데이터로도 초기 동작 수준의 정책을 빠르게 얻을 수 있다.
- **범용성**: 이산/연속 행동 공간 모두 적용 가능하다.

## 한계

### 분포 이탈 (Distribution Shift)

학습 시점의 상태 분포 $d_{\pi^*}$와 실행 시점의 상태 분포 $d_{\pi_\theta}$가 다르면 성능이 급격히 저하된다. 전문가가 방문하지 않은 상태에서는 정책이 신뢰할 수 없는 행동을 출력한다.

### 복합 오류 (Compounding Error)

시간축에서 오류가 누적된다. 시각 $t$의 작은 실수가 $t+1$의 상태를 왜곡하고, 이 상태에서의 오류가 다시 $t+2$를 왜곡하는 연쇄 반응이 발생한다. 에피소드 길이 $T$에 대해 오류가 $O(T^2)$으로 증가할 수 있다.

### 모드 커버리지 문제

평균 회귀(regression to mean) 경향으로 인해 멀티모달 행동 분포를 모델링할 때 중간값을 출력하는 문제가 생긴다. [[diffusion-policy-robot|확산 정책(Diffusion Policy)]]은 이 문제를 확산 모델로 해결한다.

## BC vs 강화 학습 비교

| 측면 | BC | RL |
|------|----|----|
| 보상 함수 | 불필요 | 필수 |
| 환경 상호작용 | 불필요 | 필수 (샘플 비효율) |
| 학습 안정성 | 높음 | 낮음 (보상 희소 등) |
| 분포 이탈 | 취약 | 덜 취약 |
| 전문가 능력 상한 | 전문가 수준 한정 | 초월 가능 |
| 최적화 난이도 | 낮음 (지도 학습) | 높음 (탐색 + 신용 할당) |

## 개선 기법: DAgger

DAgger(Dataset Aggregation)는 BC의 분포 이탈 문제를 해결하는 대표적 방법이다. 학습된 정책으로 환경을 실행하며 전문가에게 방문 상태에 대한 올바른 행동을 라벨링 받아 데이터셋을 누적·확장한다.

1. $\pi_\theta$로 환경 실행
2. 방문한 상태 $s$에 대해 전문가에게 $\pi^*(s)$ 질의
3. 새 데이터를 기존 데이터셋에 추가
4. 확장된 데이터셋으로 정책 재학습

이론적으로 DAgger는 분포 이탈 오류를 $O(T)$에서 $O(1)$로 줄인다.

## LLM과의 연결: SFT는 BC의 일종

LLM의 사전학습 이후 단계인 지도 미세조정(SFT, Supervised Fine-Tuning)은 행동 복제의 일종으로 볼 수 있다. 인간 전문가의 (프롬프트, 응답) 쌍을 전문가 시연 데이터로, 토큰 생성 정책을 학습 대상 정책으로 간주하면 구조가 동일하다. SFT 이후 RLHF([[on-policy-distillation|온-폴리시 방식]])로 분포 이탈을 보정하는 과정은 DAgger와 유사한 동기를 가진다.

## 응용 분야

- **로봇공학**: [[robot-teleoperation-data|텔레오퍼레이션 데이터]]로 조작 정책 학습
- **자율주행**: 운전자의 주행 영상 데이터로 초기 정책 학습
- **게임 AI**: 인간 플레이 기록으로 에이전트 초기화
- **LLM SFT**: 위에서 설명한 언어 모델 미세조정

## 관련 문서

- [[imitation-learning|모방 학습 (Imitation Learning)]]
- [[inverse-rl-imitation|역강화 학습 (Inverse RL)]]
- [[diffusion-policy-robot|확산 정책 (Diffusion Policy for Robot)]]
- [[robot-teleoperation-data|로봇 텔레오퍼레이션 데이터]]
- [[robot-learning-sim2real|Sim-to-Real 전이]]
- [[on-policy-distillation|온-폴리시 증류]]

---
source: arxiv
url: https://arxiv.org/abs/1802.01561
title: IMPALA / V-trace (Espeholt et al. 2018)
fetched: 2026-05-06
status: pending_ingest
---

# IMPALA — Importance Weighted Actor-Learner Architecture

## 메타데이터
- 논문: "IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures"
- 저자: Lasse Espeholt, Hubert Soyer, Remi Munos, Karen Simonyan, Volodymir Mnih, Tom Ward, Yotam Doron, Vlad Firoiu, Tim Harley, Iain Dunning, Shane Legg, Koray Kavukcuoglu (DeepMind)
- arXiv: 1802.01561 — 제출 2018-02-05
- 발표: ICML 2018
- 공식 구현: google-deepmind/scalable_agent (TensorFlow)

## 핵심 기여
1. **Decoupled actor-learner** — actor는 rollout만, learner는 gradient update만 담당. 비동기 통신
2. **V-trace off-policy correction** — actor가 stale policy로 수집한 trajectory를 learner의 fresh policy로 보정
3. **Single-learner, multi-actor 토폴로지** — 한 learner가 수백~수천 actor의 데이터 처리
4. **DMLab-30, Atari-57**에서 multi-task 단일 모델 학습 데모 — positive transfer 증거

## V-trace 보정
- Truncated importance sampling weight: $\rho_t = \min(\bar{\rho}, \pi(a_t|s_t) / \mu(a_t|s_t))$
- $c_t = \min(\bar{c}, \pi(a_t|s_t) / \mu(a_t|s_t))$ — 보조 truncation, 분산 감소
- V-trace target: $v_s = V(x_s) + \sum_t \gamma^{t-s} (\prod_{i=s}^{t-1} c_i) \rho_t \delta_t V$
- $\bar{\rho}$, $\bar{c}$ 두 hyperparameter — 일반적으로 $\bar{\rho} = \bar{c} = 1$
- $\rho_t = \bar{c}_t$일 때 on-policy advantage actor-critic으로 환원

## 분산 토폴로지
- **Single-learner**: GPU 1대(혹은 multi-GPU) 위 거대 batched learner
- **Multi-actor**: 수백~수천 CPU 머신, 각자 환경 stepping + 정책 inference
- Actor는 trajectory chunk(통상 20-100 step)를 learner의 queue에 push
- Learner는 batch로 gradient step → updated weights를 actor에 broadcast (gRPC)
- **Multi-learner** 변종: 여러 learner를 동기/비동기로 운영, 더 큰 batch

## 처리량
- 단일 머신 batched learner: **~250,000 frames/second** (A3C 대비 30배)
- 다수 actor + GPU learner: thousands of machines로 scale

## 통신 패턴
- gRPC TCP: actor → learner trajectory push, learner → actor weight broadcast
- 이후 계열 (Sebulba, R2D2, Ape-X) 모두 이 패턴 변형

## A3C / A2C / Ape-X와의 차이
| 측면 | A3C | A2C | Ape-X | IMPALA |
|------|-----|-----|-------|--------|
| 분산 actor | yes | sync | yes | yes |
| 분산 learner | shared params | yes | central | yes (single) |
| Replay buffer | no | no | prioritized | no (queue) |
| Off-policy 보정 | none | none | importance | **V-trace** |
| GPU 효율 | 낮음 | 중간 | 높음 | **매우 높음** (batched) |

## 핵심 인용
> "IMPALA, a distributed agent that scales to thousands of machines without sacrificing data efficiency or resource utilization." — abstract
>
> "achieving stable learning at high throughput by combining decoupled acting and learning with a novel off-policy correction method called V-trace." — abstract
>
> "data throughput rates of 250,000 frames per second, making it over 30 times faster than single-machine A3C." — paper §5

## 후속 영향
- DeepMind R2D2 (recurrent IMPALA), MuZero, AlphaStar 모두 IMPALA 계열
- OpenAI Five의 "rapid" 분산 학습도 유사 패턴
- Sebulba(Hessel et al. 2021)가 IMPALA를 단일 TPU 호스트에 압축

## 관련 항목
- Sebulba, Anakin (TPU 압축 변종)
- A3C (Mnih et al. 2016), Ape-X (Horgan et al. 2018)
- V-trace 후속: ABC (Asynchronous Batch Critic) 등

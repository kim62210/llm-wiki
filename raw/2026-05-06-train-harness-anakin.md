---
source: arxiv + deepmind
url: https://arxiv.org/abs/2104.06272
title: Anakin 아키텍처 (DeepMind Podracer, 2021)
fetched: 2026-05-06
status: pending_ingest
---

# Anakin 아키텍처 — actor-learner 분리 없는 fully on-device RL

## 메타데이터
- 논문: "Podracer architectures for scalable Reinforcement Learning" (2104.06272)
- Sebulba와 같은 논문에 함께 소개된 자매 아키텍처
- 시스템: TPU pod, JAX/XLA 기반

## 핵심 아이디어
- **환경(env), action selection, learning을 모두 TPU 가속기 위에서 실행**
- 환경 자체를 JAX pure function으로 구현 → XLA로 컴파일 → TPU에서 직접 step
- Actor/learner 분리가 없음 — 전체 RL loop이 device 위에서 결정론적으로 실행
- Sebulba보다 단순하고, 작은 환경(grid-world, 단순 board game 등)에 적합

## 분산 토폴로지
- 환경(green) + action(yellow) + learning(pink) 모두 가속기에서 실행
- 모든 TPU core에 동일한 computation을 replicate (`jax.pmap`)
- 각 core가 자기 batch의 env를 step + 학습까지 자체 완료
- pod 단위로 replica를 늘려 throughput을 선형 확장

## 통신 패턴
- core 간 통신은 `jax.pmean` 으로 gradient averaging
- host CPU의 개입 거의 없음 — Python overhead 제거
- Multi-host TPU pod에서도 XLA가 collective ops를 알아서 처리

## 실측 처리량
- 작은 NN + grid-world: **5,000,000 steps/second**
- 복잡한 환경 + 16-core TPU: **3,000,000+ steps/second**
- Anakin 실험은 self-contained + deterministic → reproducibility 우수

## 제약
- 환경이 **JAX pure function으로 구현 가능해야 함** — Atari, MuJoCo 등은 wrapper 필요
- 환경 randomness도 PRNG 명시적 split로 처리해야 함
- gymnax, brax, jumanji 같은 JAX-native env 라이브러리와 결합

## 핵심 인용
> "In Anakin, the environment (in green), action selection (in yellow) and learning (in pink) are all executed on the accelerators, and the computation is replicated across all available cores." — paper §4
>
> "There is no need for the actor/learner separation that is so popular in large scale deep RL platforms." — paper §4
>
> "Anakin experiments are self contained and deterministic." — paper §4

## 후속 영향
- InstaDeep의 **Mava** (multi-agent RL) 및 **Stoix** (single-agent RL) 둘 다 Anakin 패턴 채택
- gymnax, gymnax-blines, brax (Google Brain) 등이 JAX-native env로 Anakin compat
- Sebulba와 함께 JAX 분산 RL 표준 패턴 정립

## 관련 항목
- Sebulba (actor-learner 분리 변종)
- Mava (multi-agent JAX), Stoix, gymnax
- Brax (Google Brain JAX physics)
- pmap/pmean (JAX collective)

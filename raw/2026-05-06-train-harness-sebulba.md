---
source: arxiv + github
url: https://arxiv.org/abs/2104.06272
title: Sebulba 아키텍처 (DeepMind Podracer, 2021)
fetched: 2026-05-06
status: pending_ingest
---

# Sebulba 아키텍처 — DeepMind Podracer 시리즈 중 actor-learner decomposed 변종

## 메타데이터
- 논문: "Podracer architectures for scalable Reinforcement Learning" (2104.06272)
- 저자: Matteo Hessel, Manuel Kroiss, Aidan Clark, Iurii Kemaev, John Quan, Thomas Keck, Fabio Viola, Hado van Hasselt (DeepMind)
- 제출일: 2021-04-13
- 공식 구현: instadeepai/sebulba (JAX 기반), vwxyzjn/cleanba (CleanRL 단일파일)
- 시스템: TPU pod / TPU v3, v4 / 8-core TPU 단일 호스트가 기본 단위

## 핵심 기여
- DeepMind 내부 RL 연구를 위한 **Podracer** 두 변종 발표: **Anakin**(완전 on-device 환경 + 학습)과 **Sebulba**(actor-learner 분리)
- 분산 actor-learner 토폴로지를 단일 TPU 호스트에 압축하여 효율과 비용을 최적화
- Atari 200M frame 학습을 8-core TPU에서 ~1시간, GCP preemptible 인스턴스 약 $2.88

## 분산 토폴로지
- **8개 TPU 코어를 두 disjoint 그룹으로 분할**:
  - `A`개 코어: actor 전용 (rollout 추론)
  - `8 - A`개 코어: learner 전용 (gradient update)
- 각 Python thread가 환경 batch를 병렬로 step → observation을 acting TPU 코어에 전달 → action 받기
- Trajectory는 큐(`Pipeline`)에 들어가 learner devices 간 sharding됨
- `ParamsSource` 컴포넌트가 learner → actor 파라미터 전달 (latest weights 동기화)

## 통신 패턴
- 모든 컴퓨트는 단일 TPU 호스트 안에서 진행되며, 머신 간 통신 없음
- Learner thread는 모든 learning TPU 코어에서 동일한 update 함수를 `jax.pmap`으로 실행
- 파라미터 업데이트는 `jax.pmean` / `jax.psum` 으로 averaged
- Multi-pod 확장 시: pod 간 replica 식으로 scale, pod 내부는 위 구조

## rollout vs policy update 분리
- 비동기 acting + 비동기 learning: actor가 trajectory를 큐에 넣고 곧바로 다음 batch 진행
- Off-policy 보정은 V-trace (IMPALA 계열) 활용
- Sebulba 자체는 알고리즘 구현 templated — IMPALA, PPO, R2D2 등을 plug-in 가능

## 실측 처리량
- Atari 200M frames in ~1 hour on 8-core TPU
- DMLab 환경에서 IMPALA보다 wall-clock 단축
- Cleanba 구현 보고: 1 GPU + 10 CPU에서 monobeast IMPALA 대비 6.8x, moolib IMPALA 대비 1.2x; 8 GPU + 40 CPU에서 5x / 2x

## 핵심 인용
> "𝐴 cores are used exclusively to act, and the remaining 8 − 𝐴 cores are used to learn." — paper §3
>
> "Each Python thread steps an entire batch of environments in parallel and feeds the resulting batch of observations to a TPU core, to perform inference of that batch of observations and select the next batch of actions." — paper §3.1
>
> "parameter updates can be averaged across all participating learner cores using JAX's pmean/psum primitives." — paper §3.1

## 운영 / 엔터프라이즈 측면
- DeepMind 자체 RL 연구 인프라 (XLand, AlphaZero 후속 등)에 영향
- InstaDeep이 enterprise RL 적용 — DeepPCB(반도체 라우팅) 등 실제 산업 사례에서 사용
- JAX의 `pmap`/`pjit` API 진화에 직접 기여 — James Bradbury 인용

## 관련 항목
- IMPALA / V-trace (분산 actor-critic, 동일 저자 라인)
- Anakin (Podracer 자매 아키텍처)
- Cleanba (CleanRL 구현)
- Mava, Stoix (InstaDeep multi-agent / single-agent JAX 라이브러리)

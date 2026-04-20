---
title: OpenHands SWE-Bench Scaling Notes
category: applications
page_type: case-study
tags: [applications, case-study, openhands, swe-bench, coding-agents]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-agent-benchmarks/03-openhands-dev-sota-on-swe-bench-verified-with-inference-time-scaling-and-c.md]
created: 2026-04-10
updated: 2026-04-13
---
# OpenHands SWE-Bench Scaling Notes

OpenHands가 inference-time scaling과 critic model을 통해 [[swe-bench-ecosystem-2026|SWE-bench Verified]] 성능을 끌어올린 사례를 정리한 case-study다.

## 핵심 내용

- 단순 모델 교체가 아니라 inference-time scaling을 성능 레버로 사용
- critic model을 통해 해결 경로를 교정
- [[how-coding-agents-work|coding agent]] benchmark에서 운영 전략이 성능을 어떻게 바꾸는지 보여줌

## 왜 중요한가

이 사례는 “좋은 모델이면 끝”이 아니라, **같은 모델이라도 추론 예산과 critic 구조에 따라 결과가 크게 달라질 수 있음**을 보여준다.

## 실무 적용 관점

실무 팀은 benchmark score를 볼 때 base model만 볼 것이 아니라, 어떤 scaling 전략과 reviewer/critic 구조가 같이 들어갔는지도 확인해야 한다. [[long-horizon-agent-benchmarks|장기 실행 에이전트 벤치마크]] 맥락에서 운영 전략의 중요성을 보여주는 사례다.

## 원문이 다루는 흐름

원문은 `SWE-Bench and OpenHands` → `Inference-Time Scaling: More Compute, Better Results` → `Building a Better Critic` → `Why We Built a Critic Model and Where It's Going` → `Try OpenHands Today` 흐름으로 사례를 쌓아 간다. 그래서 이 페이지는 결과 수치만 보는 대신 **문제 배경 → 개입 방식 → 얻은 교훈**의 순서로 읽는 것이 적절하다.

- 따라가야 할 순서: SWE-Bench and OpenHands, Inference-Time Scaling: More Compute, Better Results, Building a Better Critic, Why We Built a Critic Model and Where It's Going, Try OpenHands Today
- 위키에 남겨야 할 축: 문제 배경, 개입 방식, 재사용 가능한 교훈

## 읽기 포인트

- 이 문서는 **사례를 재현 가능한 운영 교훈으로 어떻게 바꿀 것인가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- 사례 문서는 '무엇을 했다'보다 '왜 그 선택이 먹혔는가, 어떤 전제가 있었는가'를 남길 때 재사용 가치가 생긴다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/long-horizon-agent-benchmarks/03-openhands-dev-sota-on-swe-bench-verified-with-inference-time-scaling-and-c.md` · source: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model · 볼 섹션: SWE-Bench and OpenHands, Inference-Time Scaling: More Compute, Better Results, Building a Better Critic, Why We Built a Critic Model and Where It's Going

## 관련 문서

- [[swe-bench-pro|SWE-bench Pro]]
- [[swe-evo-paper|SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios]]
- [[tool-invocation-evaluators|Tool Selection & Tool Invocation Evaluators]]

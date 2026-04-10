---
title: OpenHands SWE-Bench Scaling Notes
category: applications
page_type: case-study
tags: [applications, case-study, openhands, swe-bench, coding-agents]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-agent-benchmarks/03-openhands-dev-sota-on-swe-bench-verified-with-inference-time-scaling-and-c.md]
created: 2026-04-10
updated: 2026-04-10
---

# OpenHands SWE-Bench Scaling Notes

OpenHands가 inference-time scaling과 critic model을 통해 SWE-bench Verified 성능을 끌어올린 사례를 정리한 case-study다.

## 핵심 내용

- 단순 모델 교체가 아니라 inference-time scaling을 성능 레버로 사용
- critic model을 통해 해결 경로를 교정
- coding agent benchmark에서 운영 전략이 성능을 어떻게 바꾸는지 보여줌

## 왜 중요한가

이 사례는 “좋은 모델이면 끝”이 아니라, **같은 모델이라도 추론 예산과 critic 구조에 따라 결과가 크게 달라질 수 있음**을 보여준다.

## 실무 적용 관점

실무 팀은 benchmark score를 볼 때 base model만 볼 것이 아니라, 어떤 scaling 전략과 reviewer/critic 구조가 같이 들어갔는지도 확인해야 한다.

## 관련 문서

- [[swe-bench-pro|SWE-bench Pro]]
- [[swe-evo-paper|SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios]]
- [[tool-invocation-evaluators|Tool Selection & Tool Invocation Evaluators]]


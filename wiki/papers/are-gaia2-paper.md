---
title: ARE: Scaling Up Agent Environments and Evaluations
category: papers
page_type: paper
tags: [paper, benchmarks, environments, gaia2]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-agent-benchmarks/01-arxiv-org-are-scaling-up-agent-environments-and-evaluations.md]
created: 2026-04-10
updated: 2026-04-10
---

# ARE: Scaling Up Agent Environments and Evaluations

Meta가 제안한 ARE 플랫폼과 Gaia2 벤치마크를 설명하는 논문이다. 에이전트 평가를 단순 정적 QA가 아니라 **환경, 도구, 시간 제약, 비동기성**을 포함하는 실행 문제로 끌어올린 점이 핵심이다.

## 핵심 기여

- 에이전트 연구용 환경을 빠르게 만들고 확장하기 위한 ARE 플랫폼 제안
- 비동기성, 잡음, 모호성, temporal constraint를 포함하는 Gaia2 벤치마크 소개
- agent benchmark를 고정 테스트셋이 아니라 지속적으로 확장 가능한 환경 문제로 재정의

## 결과와 시사점

- 강한 reasoning 모델이 항상 더 효율적인 것은 아니며, intelligence와 efficiency 사이 trade-off가 드러남
- 정적 평가에서는 보이지 않던 failure mode가 비동기 환경에서 드러난다

## 한계

환경 기반 벤치마크는 현실성을 높이지만, 구현과 운영 복잡도도 함께 크게 올라간다.

## 실무 적용 관점

이 논문은 앞으로의 agent eval이 “정답 맞히기”보다 **어떤 환경에서 얼마의 예산으로 얼마나 안정적으로 행동하는가**를 측정하는 방향으로 갈 것임을 보여준다.

## 관련 문서

- [[long-horizon-agent-benchmarks|Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)]]
- [[swe-evo-paper|SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios]]
- [[llm-observability-platforms|Production Observability Platforms Convergence]]


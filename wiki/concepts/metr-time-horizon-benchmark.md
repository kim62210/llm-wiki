---
title: METR Time Horizon Benchmark
category: concepts
page_type: entity
project: METR Time Horizon Benchmark
tags: [concepts, entity, metr, time, horizon, benchmark]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/metr-time-horizon-benchmark.md, raw/hot-topics-sources/2026-04-10/388-task-completion-time-horizons-of-frontier-ai-models.md, raw/hot-topics-sources/2026-04-10/389-time-horizon-1-1.md, raw/hot-topics-sources/2026-04-10/390-measuring-ai-ability-to-complete-long-tasks.md, raw/hot-topics-sources/2026-04-10/391-measuring-ai-ability-to-complete-long-software-tasks.md, raw/hot-topics-sources/2026-04-10/392-how-does-time-horizon-vary-across-domains.md]
created: 2026-04-10
updated: 2026-04-10
---
# METR Time Horizon Benchmark

프론티어 에이전트가 50% 신뢰도로 완수 가능한 인간 작업 시간을 측정하는 지표.

## 왜 지금 중요한가

2026년 1월 29일 Time Horizon 1.1 공개 후 3월 업데이트에서 최근 모델의 배증 주기가 165일 → 131일로 가속됨이 확인되며, 장기 자율성 위험 예측의 사실상 업계 표준 지표로 자리잡았다.

## 대표 레퍼런스

- [Task-Completion Time Horizons of Frontier AI Models (METR)](https://metr.org/time-horizons/)
- [Time Horizon 1.1 (METR, Jan 29 2026)](https://metr.org/blog/2026-1-29-time-horizon-1-1/)
- [Measuring AI Ability to Complete Long Tasks (METR)](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [Measuring AI Ability to Complete Long Software Tasks (arXiv 2503.14499)](https://arxiv.org/abs/2503.14499)
- [How Does Time Horizon Vary Across Domains?](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/)

## 해석 포인트

METR Time Horizon Benchmark은 단순한 제품 소개보다 **성능만이 아니라 운영 설계까지 함께 봐야 하는 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `metr.org×4, arxiv.org×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 평가셋 범위, 난도 분포, 실제 사용성과의 상관 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: 프론티어 에이전트가 50% 신뢰도로 완수 가능한 인간 작업 시간을 측정하는 지표.
- 왜 중요한가: 2026년 1월 29일 Time Horizon 1.1 공개 후 3월 업데이트에서 최근 모델의 배증 주기가 165일 → 131일로 가속됨이 확인되며, 장기 자율성 위험 예측의 사실상 업계 표준 지표로 자리잡았다.
- 직접 수집 원문: 5개
- 주요 도메인: metr.org×4, arxiv.org×1

## 핵심 포인트

METR Time Horizon Benchmark는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 프론티어 에이전트가 50% 신뢰도로 완수 가능한 인간 작업 시간을 측정하는 지표.이며, 직접 수집한 source 5건은 metr.org×4, arxiv.org×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 metr.org×4, arxiv.org×1로 분포한다. 연구 논문 비중이 높아 메커니즘·평가·한계 쪽 정보가 중심이다.

## 실무 관점

개념 페이지는 용어 정의에서 끝나지 않고, 어떤 시스템 설계 문제를 해결하려고 등장했는지와 어디까지가 적용 범위인지까지 함께 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/metr-time-horizon-benchmark.md`

### source별 핵심 신호

- **Task-Completion Time Horizons of Frontier AI Models - METR** (`metr.org`): https://metr.org/time-horizons/
  - 메모: These are our most up-to-date measurements of the task-completion time horizons for public frontier language models. We intend to update this page periodically whenever we have new measurements to share.
- **Time Horizon 1.1 - METR** (`metr.org`): https://metr.org/blog/2026-1-29-time-horizon-1-1/
  - 메모: We’re releasing a new version of our time horizon estimates (TH1.1), using more tasks and a new eval infrastructure.
- **Measuring AI Ability to Complete Long Tasks - METR** (`metr.org`): https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
  - 메모: We propose measuring AI performance in terms of the length of tasks AI agents can complete.
- **[2503.14499] Measuring AI Ability to Complete Long Software Tasks** (`arxiv.org`): https://arxiv.org/abs/2503.14499
  - 메모: Despite rapid progress on AI benchmarks, the real-world meaning of benchmark performance remains unclear.
- **How Does Time Horizon Vary Across Domains? - METR** (`metr.org`): https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/
  - 메모: In the paper Measuring AI Ability to Complete Long Software Tasks (Kwa & West et al.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[responsible-scaling-policy-v3-and-frontier-safety-roadmap|Responsible Scaling Policy v3 & Frontier Safety Roadmap]]
- [[cot-monitorability|Chain-of-Thought Monitorability]]
- [[context-engineering|Context Engineering]]

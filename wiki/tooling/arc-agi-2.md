---
title: ARC-AGI-2
category: tooling
page_type: entity
project: ARC-AGI-2
tags: [tooling, entity, arc, agi, model-releases-and-benchmarks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/arc-agi-2.md, raw/hot-topics-sources/2026-04-10/158-arc-agi-2-overview-arc-prize.md, raw/hot-topics-sources/2026-04-10/159-arc-prize-leaderboard.md, raw/hot-topics-sources/2026-04-10/160-arc-agi-v2-leaderboard-llm-stats.md, raw/hot-topics-sources/2026-04-10/161-beating-arc-agi-2-with-code-evolution-imbue.md, raw/hot-topics-sources/2026-04-10/162-arc-prize-2026-kaggle.md]
created: 2026-04-10
updated: 2026-04-10
---
# ARC-AGI-2

이 페이지는 ARC-AGI-2를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 ARC Prize가 운영하는 추상 추론/유동지능(fluid intelligence) 벤치마크 2세대이기 때문이다.

## 정의

ARC Prize가 운영하는 추상 추론/유동지능(fluid intelligence) 벤치마크 2세대.

## 왜 지금 중요한가

2026년 2월 Gemini 3.1 Pro가 공개 API 중 최초로 77.1%를 기록한 뒤 Imbue의 code evolution 기법이 95.1%, Confluence Lab이 97.9%(태스크당 $11.77)까지 밀어올리면서 "log-linear scaling으로는 못 깬다"던 벽이 흔들리고 있어 AGI 진척도 지표로 월간 주목도가 폭증했다.

## 개요

이 페이지는 **ARC-AGI-2** 자체를 지속적으로 누적·갱신하기 위한 허브 페이지다.

## 대표 자료

- [ARC-AGI-2 Overview — ARC Prize](https://arcprize.org/arc-agi/2)
- [ARC Prize Leaderboard](https://arcprize.org/leaderboard)
- [ARC-AGI v2 Leaderboard — LLM Stats](https://llm-stats.com/benchmarks/arc-agi-v2)
- [Beating ARC-AGI-2 with Code Evolution — Imbue](https://imbue.com/research/2026-02-27-arc-agi-2-evolution/)
- [ARC Prize 2026 — Kaggle](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-2/leaderboard)

## 해석 포인트

ARC-AGI-2은 단순한 제품 소개보다 **모델 능력보다 개발자 경험과 운영 통합면이 중요한 도구 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `arcprize.org×2, llm-stats.com×1, imbue.com×1, kaggle.com×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: ARC Prize가 운영하는 추상 추론/유동지능(fluid intelligence) 벤치마크 2세대.
- 왜 중요한가: 2026년 2월 Gemini 3.1 Pro가 공개 API 중 최초로 77.1%를 기록한 뒤 Imbue의 code evolution 기법이 95.1%, Confluence Lab이 97.9%(태스크당 $11.77)까지 밀어올리면서 "log-linear scaling으로는 못 깬다"던 벽이 흔들리고 있어 AGI 진척도 지표로 월간 주목도가 폭증했다.
- 직접 수집 원문: 5개
- 주요 도메인: arcprize.org×2, llm-stats.com×1, imbue.com×1, kaggle.com×1

## 핵심 포인트

ARC-AGI-2는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 이 페이지는 ARC-AGI-2를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 ARC Prize가 운영하는 추상 추론/유동지능(fluid intelligence) 벤치마크 2세대이기 때문이다.이며, 직접 수집한 source 5건은 arcprize.org×2, imbue.com×1, kaggle.com×1, llm-stats.com×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 arcprize.org×2, imbue.com×1, kaggle.com×1, llm-stats.com×1로 분포한다. source 구성이 비교적 고르게 분포해 허브형 개요 문서로 읽기 좋다.

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/arc-agi-2.md`

### source별 핵심 신호

- **ARC-AGI-2** (`arcprize.org`): https://arcprize.org/arc-agi/2
  - 메모: Can you create a system that can reach 85% accuracy?
- **ARC Prize - Leaderboard** (`arcprize.org`): https://arcprize.org/leaderboard
  - 메모: Reasoning Systems Trend Line solutions display connected points representing the same model at different reasoning levels.
- **ARC-AGI v2 Leaderboard** (`llm-stats.com`): https://llm-stats.com/benchmarks/arc-agi-v2
  - 메모: Interactive timeline showing model performance evolution on ARC-AGI v2
- **Beating ARC-AGI-2 with Code Evolution - imbue** (`imbue.com`): https://imbue.com/research/2026-02-27-arc-agi-2-evolution/
  - 메모: Our code evolution method improves the reasoning capabilities of cheap models by 2x-3x.
- **ARC Prize 2026 - ARC-AGI-2 | Kaggle** (`kaggle.com`): https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-2/leaderboard

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[terminal-bench-2-0]]

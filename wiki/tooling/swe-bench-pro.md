---
title: SWE-bench Pro
category: tooling
page_type: entity
project: SWE-bench Pro
tags: [tooling, entity, swe, bench, pro, model-releases-and-benchmarks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/swe-bench-pro.md, raw/hot-topics-sources/2026-04-10/150-swe-bench-pro-paper-landing-scale-labs.md, raw/hot-topics-sources/2026-04-10/143-swe-bench-pro-leaderboard-scale-labs.md, raw/hot-topics-sources/2026-04-10/151-swe-bench-pro-leaderboard-scale.md, raw/hot-topics-sources/2026-04-10/152-swe-bench-pro-project-scale.md, raw/hot-topics-sources/2026-04-10/153-scaleapi-swe-bench-pro-os-github.md]
created: 2026-04-10
updated: 2026-04-10
---
# SWE-bench Pro

이 페이지는 SWE-bench Pro를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Scale AI가 구축한 장기 호흡(long-horizon) 소프트웨어 엔지니어링 벤치마크이기 때문이다.

## 정의

Scale AI가 구축한 장기 호흡(long-horizon) 소프트웨어 엔지니어링 벤치마크.

## 왜 지금 중요한가

41개 저장소 1,865개 태스크(공개 731 + Held-out 858 + 상용 276)로 GPL/상용 코드 기반 오염 방지 설계, SWE-bench Verified가 80%를 넘어 포화되자 2026년 사실상의 후속 표준으로 부상했고 GLM-5.1 58.4%/GPT-5.4-pro 59.1% 등 최상위 모델도 60% 문턱에서 분투 중이다.

## 개요

이 페이지는 **SWE-bench Pro** 자체를 지속적으로 누적·갱신하기 위한 허브 페이지다.

## 대표 자료

- [SWE-Bench Pro Paper Landing — Scale Labs](https://labs.scale.com/papers/swe_bench_pro)
- [SWE-Bench Pro Leaderboard (Public) — Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [SWE-Bench Pro Leaderboard (Private) — Scale](https://labs.scale.com/leaderboard/swe_bench_pro_private)
- [SWE-Bench Pro Project — Scale](https://scaleapi.github.io/SWE-bench_Pro-os/)
- [scaleapi/SWE-bench_Pro-os — GitHub](https://github.com/scaleapi/SWE-bench_Pro-os)

## 해석 포인트

SWE-bench Pro은 단순한 제품 소개보다 **모델 능력보다 개발자 경험과 운영 통합면이 중요한 도구 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `labs.scale.com×3, scaleapi.github.io×1, github.com×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 평가셋 범위, 난도 분포, 실제 사용성과의 상관 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: Scale AI가 구축한 장기 호흡(long-horizon) 소프트웨어 엔지니어링 벤치마크.
- 왜 중요한가: 41개 저장소 1,865개 태스크(공개 731 + Held-out 858 + 상용 276)로 GPL/상용 코드 기반 오염 방지 설계, SWE-bench Verified가 80%를 넘어 포화되자 2026년 사실상의 후속 표준으로 부상했고 GLM-5.1 58.4%/GPT-5.4-pro 59.1% 등 최상위 모델도 60% 문턱에서 분투 중이다.
- 직접 수집 원문: 5개
- 주요 도메인: labs.scale.com×3, scaleapi.github.io×1, github.com×1

## 핵심 포인트

SWE-bench Pro는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 이 페이지는 SWE-bench Pro를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Scale AI가 구축한 장기 호흡(long-horizon) 소프트웨어 엔지니어링 벤치마크이기 때문이다.이며, 직접 수집한 source 5건은 labs.scale.com×3, github.com×1, scaleapi.github.io×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 labs.scale.com×3, github.com×1, scaleapi.github.io×1로 분포한다. 구현 저장소 비중이 높아 실제 사용·통합 관점이 두드러진다.

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/swe-bench-pro.md`

### source별 핵심 신호

- **SWE-Bench Pro: AI on Software Engineering Tasks | Scale Labs** (`labs.scale.com`): https://labs.scale.com/papers/swe_bench_pro
  - 메모: AgentsSafety, Evaluation and Alignment9/19/2025
- **SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale** (`labs.scale.com`): https://labs.scale.com/leaderboard/swe_bench_pro_public
  - 메모: SWE-Bench Pro is a benchmark designed to provide a rigorous and realistic evaluation of AI agents for software engineering.
- **Scale Labs Leaderboard: SWE-Bench Pro (Private Dataset)** (`labs.scale.com`): https://labs.scale.com/leaderboard/swe_bench_pro_private
  - 메모: SWE-Bench Pro is a benchmark designed to provide a rigorous and realistic evaluation of AI agents for software engineering.
- **SWE-Bench Pro** (`scaleapi.github.io`): https://scaleapi.github.io/SWE-bench_Pro-os/
  - 메모: Model% Resolved(+/-)Link🥇SWE-Agent + claude-4-5-Sonnet43.72🔗🥈SWE-Agent + claude-4-Sonnet42.70🔗🥉SWE-Agent + claude-4-5-haiku39.45🔗SWE-Agent + gpt-5-2025-08-07 (High)36.30🔗SWE-Agent + glm-4.535.52🔗SWE-Agent + kimi-k2-instr
- **GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub** (`github.com`): https://github.com/scaleapi/SWE-bench_Pro-os
  - 메모: To see all available qualifiers, see our documentation.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[qwen3-6-plus]]
- [[terminal-bench-2-0]]

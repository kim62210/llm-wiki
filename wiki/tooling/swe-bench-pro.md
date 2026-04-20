---
title: SWE-bench Pro
category: tooling
page_type: entity
project: SWE-bench Pro
tags: [tooling, entity, swe, bench, pro, model-releases-and-benchmarks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/swe-bench-pro.md, raw/hot-topics-sources/2026-04-10/150-swe-bench-pro-paper-landing-scale-labs.md, raw/hot-topics-sources/2026-04-10/143-swe-bench-pro-leaderboard-scale-labs.md, raw/hot-topics-sources/2026-04-10/151-swe-bench-pro-leaderboard-scale.md, raw/hot-topics-sources/2026-04-10/152-swe-bench-pro-project-scale.md, raw/hot-topics-sources/2026-04-10/153-scaleapi-swe-bench-pro-os-github.md]
created: 2026-04-10
updated: 2026-04-13
---
# SWE-bench Pro

Scale AI가 구축한 장기 호흡(long-horizon) 소프트웨어 엔지니어링 벤치마크.

## 왜 지금 중요한가

41개 저장소 1,865개 태스크(공개 731 + Held-out 858 + 상용 276)로 구성. GPL/상용 코드 기반 오염 방지 설계로 [[terminal-bench-2-0|Terminal-Bench 2.0]]과 함께 2026년 에이전틱 코딩 평가의 후속 표준으로 자리잡았다. SWE-bench Verified가 80%를 넘어 포화되자 등장했고, [[glm-5-1|GLM-5.1]] 58.4% / GPT-5.4-pro 59.1% 등 최상위 모델도 60% 문턱에서 분투 중이다.

## 대표 자료

- [SWE-Bench Pro Paper Landing -- Scale Labs](https://labs.scale.com/papers/swe_bench_pro)
- [SWE-Bench Pro Leaderboard (Public) -- Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [SWE-Bench Pro Leaderboard (Private) -- Scale](https://labs.scale.com/leaderboard/swe_bench_pro_private)
- [SWE-Bench Pro Project -- Scale](https://scaleapi.github.io/SWE-bench_Pro-os/)
- [scaleapi/SWE-bench_Pro-os -- GitHub](https://github.com/scaleapi/SWE-bench_Pro-os)

## 리더보드 현황 (오픈소스 데이터셋)

1. SWE-Agent + claude-4-5-Sonnet: 43.72%
2. SWE-Agent + claude-4-Sonnet: 42.70%
3. SWE-Agent + claude-4-5-haiku: 39.45%
4. SWE-Agent + gpt-5-2025-08-07 (High): 36.30%

## 해석 포인트

평가셋 범위, 난도 분포, 실제 사용성과의 상관 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다. [[arc-agi-2]]와 함께 읽으면 코딩 에이전트 vs. 추론 에이전트 평가의 차이가 선명해진다. [[long-horizon-agent-benchmarks|장기 에이전트 벤치마크]] 생태계에서 포화된 Verified 이후의 다음 기준점을 제시하며, [[agent-trajectory-evaluation|에이전트 궤적 평가]] 방법론으로 단계별 실패 지점을 추적할 수 있다.

## 관련 문서

- [[qwen3-6-plus]]
- [[terminal-bench-2-0]]
- [[arc-agi-2]]

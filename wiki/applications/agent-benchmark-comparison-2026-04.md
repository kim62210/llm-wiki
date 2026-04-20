---
title: 2026년 4월 에이전트 벤치마크 비교
category: applications
page_type: summary
tags: [applications, summary, benchmarks, agents, comparison]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/swe-bench-pro.md, raw/hot-topics-sources/2026-04-10/topics/terminal-bench-2-0.md, raw/hot-topics-sources/2026-04-10/topics/arc-agi-2.md, raw/hot-topics-sources/2026-04-10/topics/metr-time-horizon-benchmark.md]
created: 2026-04-10
updated: 2026-04-13
---
# 2026년 4월 에이전트 벤치마크 비교

에이전트/모델 평가에서 자주 등장하는 벤치마크들을 **무엇을 재는가** 기준으로 비교한 summary다.

## 한눈에 보기

| 벤치마크 | 측정 대상 | 특징 |
|---|---|---|
| [[swe-bench-pro|SWE-bench Pro]] | 장기 소프트웨어 엔지니어링 | 다파일 변경, 장기 진화 과제 |
| [[terminal-bench-2-0|Terminal-Bench 2.0]] | 터미널 기반 agentic coding | 셸, 환경 설정, 복구, 실행 |
| [[arc-agi-2|ARC-AGI-2]] | 추상 추론 / fluid intelligence | 일반화와 추상 규칙 발견 |
| [[metr-time-horizon-benchmark|METR Time Horizon Benchmark]] | 자율 작업 지속 시간 | “얼마나 오래 유의미하게 일할 수 있는가” |
| [[long-horizon-agent-benchmarks|Long-Horizon Agent Benchmarks]] | 여러 long-horizon 과제 계열 | breadth-first 비교 지도 역할 |

## 왜 중요한가

모델 발표에서는 여러 benchmark 수치를 한꺼번에 제시하지만, 각 벤치마크는 전혀 다른 능력을 측정한다. 따라서 점수 비교보다 먼저 **그 벤치마크가 무엇을 요구하는가**를 이해해야 한다.

## 읽는 포인트

### SWE-bench Pro
실제 소프트웨어 진화와 가까운 과제를 통해, 장기적인 multi-file reasoning을 얼마나 잘 버티는지 본다.

### Terminal-Bench 2.0
코드를 “쓸 수 있는가”보다, 터미널과 도구를 다루며 상태를 관리하고 실패를 복구할 수 있는가를 본다.

### ARC-AGI-2
코딩이나 도구 사용보다 추상 규칙 발견과 general reasoning 쪽에 가깝다.

### METR Time Horizon
성능 점수 대신, 모델이 인간 작업을 얼마나 긴 시간대까지 대체할 수 있는지라는 운영형 지표를 제공한다.

## 실무 적용 관점

- coding agent를 뽑는다면 SWE-bench와 Terminal-Bench를 함께 봐야 한다.
- general reasoning 능력을 보려면 ARC-AGI 같은 축을 따로 봐야 한다.
- 자율성 위험 / 운영 가능성을 보려면 METR Time Horizon 같은 시간축 지표가 중요하다.

즉, benchmark는 경쟁 순위표가 아니라 **의사결정용 능력 분해표**로 읽는 편이 낫다.

## 관련 문서

- [[frontier-model-comparison-2026-04|2026년 4월 Frontier Model 비교]]
- [[livebench]] -- 오염 없는 동적 벤치마크 (벤치마크 생태계 맥락)
- [[long-horizon-agent-benchmarks|Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)]]
- [[openhands-swe-bench-scaling-notes|OpenHands SWE-Bench Scaling Notes]]

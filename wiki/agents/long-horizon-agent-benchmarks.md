---
title: Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)
category: agents
page_type: concept
tags: [agents, concept, long, horizon, agent, benchmarks, agent-architecture]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/long-horizon-agent-benchmarks.md, raw/hot-topics-sources/2026-04-10/034-are-scaling-up-agent-environments-and-evaluations.md, raw/hot-topics-sources/2026-04-10/035-swe-evo-benchmarking-coding-agents-in-long-horizon-software-evolution.md, raw/hot-topics-sources/2026-04-10/036-sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model.md, raw/hot-topics-sources/2026-04-10/012-introducing-claude-opus-4-5.md, raw/hot-topics-sources/2026-04-10/037-introducing-claude-sonnet-4-5.md]
created: 2026-04-10
updated: 2026-04-10
---
# Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)

이 페이지는 Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)를 다룬다. 핵심은 수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대.

## 왜 지금 중요한가

2025년 9월 Meta의 ARE 플랫폼과 GAIA 2가 시간·예산 제약을 도입했고, 2025년 12월 SWE-EVO는 GPT-5가 SWE-Bench Verified(65%) 대비 21%만 해결한다는 결과로 long-horizon 갭을 폭로했으며, 이로 인해 2026년 1분기 모든 주요 lab이 평가 프레임워크를 long-horizon 중심으로 재정비 중이다.

## 대표 자료

- [ARE: Scaling up Agent Environments and Evaluations (Meta, GAIA 2)](https://arxiv.org/abs/2509.17158)
- [SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution](https://arxiv.org/abs/2512.18470)
- [SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model (OpenHands)](https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model)
- [Introducing Claude Opus 4.5 (SWE-bench Verified 80.9%)](https://www.anthropic.com/news/claude-opus-4-5)
- [Introducing Claude Sonnet 4.5 (OSWorld 61.4%, 30+ hour focus)](https://www.anthropic.com/news/claude-sonnet-4-5)

## 해석 포인트

Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)은 **성능만이 아니라 운영 설계까지 함께 봐야 하는 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arxiv.org×2, anthropic.com×2, openhands.dev×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 평가셋 범위, 난도 분포, 실제 사용성과의 상관를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대.
- 왜 중요한가: 2025년 9월 Meta의 ARE 플랫폼과 GAIA 2가 시간·예산 제약을 도입했고, 2025년 12월 SWE-EVO는 GPT-5가 SWE-Bench Verified(65%) 대비 21%만 해결한다는 결과로 long-horizon 갭을 폭로했으며, 이로 인해 2026년 1분기 모든 주요 lab이 평가 프레임워크를 long-horizon 중심으로 재정비 중이다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×2, anthropic.com×2, openhands.dev×1

## 핵심 구조

수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대. 에이전트 토픽은 보통 모델 자체보다 **루프 구조, 상태 관리, 작업 분해, 검증 방식**이 핵심이다. 이번 source 묶음도 `arxiv.org×2, anthropic.com×2, openhands.dev×1`를 오가며 설계 패턴과 구현 사례를 함께 보여 준다.

## 핵심 포인트

Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 이 페이지는 Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)를 다룬다. 핵심은 수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 anthropic.com×2, arxiv.org×2, openhands.dev×1로 분포한다. 연구 논문과 공식 문서가 함께 있어 원리와 제품화 흐름을 같이 읽을 수 있다.

## 실무 관점

실무에서는 장기 실행, 상태 관리, 실패 복구, 평가 루프를 함께 설계해야 이 토픽이 효과를 낸다. 즉 개별 아이디어보다 에이전트 시스템 전체의 제약 속에서 읽는 것이 중요하다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/long-horizon-agent-benchmarks.md`

### source별 핵심 신호

- **[2509.17158] ARE: Scaling Up Agent Environments and Evaluations** (`arxiv.org`): https://arxiv.org/abs/2509.17158
  - 메모: We introduce Meta Agents Research Environments (ARE), a research platform for scalable creation of environments, integration of synthetic or real applications, and execution of agentic orchestrations.
- **[2512.18470] SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios** (`arxiv.org`): https://arxiv.org/abs/2512.18470
  - 메모: Existing benchmarks for AI coding agents focus on isolated, single-issue tasks such as fixing a bug or adding a small feature.
- **SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025** (`openhands.dev`): https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model
  - 메모: SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model
- **Introducing Claude Opus 4.5 \ Anthropic** (`anthropic.com`): https://www.anthropic.com/news/claude-opus-4-5
  - 메모: Our newest model, Claude Opus 4.5, is available today. It’s intelligent, efficient, and the best model in the world for coding, agents, and computer use.
- **Introducing Claude Sonnet 4.5 \ Anthropic** (`anthropic.com`): https://www.anthropic.com/news/claude-sonnet-4-5
  - 메모: Claude Sonnet 4.5 is the best coding model in the world. It's the strongest model for building complex agents. It’s the best model at using computers. And it shows substantial gains in reasoning and math.


## source 종합 해석

이 개념의 핵심은 `수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대.`에 있지만, 실제 의미는 원문 source들이 어떤 병목·trade-off를 반복적으로 강조하는지에서 더 또렷해진다.

예를 들어 source note는 We introduce Meta Agents Research Environments (ARE), a research platform for scalable creation of environments, integration of synthetic or real applications, and execution of agentic orchestrations.

또 다른 source는 Existing benchmarks for AI coding agents focus on isolated, single-issue tasks such as fixing a bug or adding a small feature.

즉, 이 토픽이 중요한 이유는 `2025년 9월 Meta의 ARE 플랫폼과 GAIA 2가 시간·예산 제약을 도입했고, 2025년 12월 SWE-EVO는 GPT-5가 SWE-Bench Verified(65%) 대비 21%만 해결한다는 결과로 long-horizon 갭을 폭로했으며, 이로 인해 2026년 1분기 모든 주요 lab이 평가 프레임워크를 long-horizon 중심으로 재정비 중이다.`라는 한 문장보다, 여러 source가 같은 문제를 서로 다른 층위(개념·측정·구현)에서 지지한다는 데 있다.

함께 읽을 문서로는 ai-hot-topics-2026-04, agent-trees, lethal-trifecta가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- `수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대.`를 실제로 적용할 때는 정의 자체보다 측정 지표와 실패 모드가 무엇인지 같이 봐야 한다.
- source note가 추상 개념/실험 결과/운영 사례 중 어디에 치우쳐 있는지 보면, 이 토픽을 실무에서 어떻게 다뤄야 하는지가 드러난다.
- `2025년 9월 Meta의 ARE 플랫폼과 GAIA 2가 시간·예산 제약을 도입했고, 2025년 12월 SWE-EVO는 GPT-5가 SWE-Bench Verified(65%) 대비 21%만 해결한다는 결과로 long-horizon 갭을 폭로했으며, 이로 인해 2026년 1분기 모든 주요 lab이 평가 프레임워크를 long-horizon 중심으로 재정비 중이다.`라는 중요도 설명은 보통 과장되기 쉬우므로, 구체적 수치·벤치마크·운영 사례를 같이 확인해야 한다.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[agent-trees]]
- [[lethal-trifecta]]

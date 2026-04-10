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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 2건, www.anthropic.com 2건, openhands.dev 1건
- source 조합: 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/long-horizon-agent-benchmarks.md`
- [[2509.17158] ARE: Scaling Up Agent Environments and Evaluations](https://arxiv.org/abs/2509.17158) — `raw/hot-topics-sources/2026-04-10/034-are-scaling-up-agent-environments-and-evaluations.md`
  - 메모: --- title: [2509.17158] ARE: Scaling Up Agent Environments and Evaluations source_url: https://arxiv.org/abs/2509.17158 final_url: https://arxiv.org/abs/2509.17158 status: 200 content_type: text/html; charset=utf-8 topics: [Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / 
- [[2512.18470] SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios](https://arxiv.org/abs/2512.18470) — `raw/hot-topics-sources/2026-04-10/035-swe-evo-benchmarking-coding-agents-in-long-horizon-software-evolution.md`
  - 메모: --- title: [2512.18470] SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios source_url: https://arxiv.org/abs/2512.18470 final_url: https://arxiv.org/abs/2512.18470 status: 200 content_type: text/html; charset=utf-8 topics: [Long-Horizon Agent Benchma
- [SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025](https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model) — `raw/hot-topics-sources/2026-04-10/036-sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model.md`
  - 메모: --- title: SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025 source_url: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model final_url: https://openhands.dev/blog/sota-on-swe-bench-verified-with-i
- [Introducing Claude Opus 4.5 \ Anthropic](https://www.anthropic.com/news/claude-opus-4-5) — `raw/hot-topics-sources/2026-04-10/012-introducing-claude-opus-4-5.md`
  - 메모: --- title: Introducing Claude Opus 4.5 \ Anthropic source_url: https://www.anthropic.com/news/claude-opus-4-5 final_url: https://www.anthropic.com/news/claude-opus-4-5 status: 200 content_type: text/html; charset=utf-8 topics: [Generator-Evaluator Harness Architecture, Long-Horiz
- [Introducing Claude Sonnet 4.5 \ Anthropic](https://www.anthropic.com/news/claude-sonnet-4-5) — `raw/hot-topics-sources/2026-04-10/037-introducing-claude-sonnet-4-5.md`
  - 메모: --- title: Introducing Claude Sonnet 4.5 \ Anthropic source_url: https://www.anthropic.com/news/claude-sonnet-4-5 final_url: https://www.anthropic.com/news/claude-sonnet-4-5 status: 200 content_type: text/html; charset=utf-8 topics: [Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Be

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[agent-trees]]
- [[lethal-trifecta]]

---
title: Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks
category: papers
page_type: paper
tags: [paper, [[context-engineering|planning]], [[long-running-agent-harnesses|long-horizon]], agents]
sources: [raw/2026-04-10-hot-ai-topics-sources/agent-trees/02-arxiv-org-plan-and-act-improving-planning-of-agents-for-long-horizon-t.md]
created: 2026-04-10
updated: 2026-04-13
---
# Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks

장기 과제에서 에이전트가 한 번에 전부 행동하려 하기보다, 먼저 계획을 세우고 이후 실행을 분리하는 접근을 제안한 논문이다.

## 핵심 기여

- long-horizon task에서 planning 단계를 명시적으로 분리
- 계획과 실행을 분리함으로써 trajectory 혼잡과 목표 상실을 줄이려는 접근 제안
- 단순 ReAct 루프보다 구조화된 계획이 더 강력한 조건을 보여줌

## 결과와 시사점

- 장기 과제에서는 한 단계씩 반응하는 것보다, 중간 수준 계획 구조를 먼저 세우는 편이 안정적이다.
- 이후 hierarchical planning, agent trees, planner-worker 구조를 이해하는 데 중요한 연결점 역할을 한다.

## 한계

계획이 잘못 서면 이후 실행 전체가 그 계획의 오류를 상속받는다. 즉 planning 분리는 강력하지만 planning quality에 민감하다.

## 실무 적용 관점

이 논문은 에이전트 설계에서 “더 좋은 prompting”보다 **계획을 언제 외부화하고 언제 고정할 것인가**가 중요한 문제라는 점을 보여준다.

## 문제 설정

`Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks** — https://arxiv.org/abs/2503.09572 · 초록 단서: Large language models (LLMs) have shown remarkable advancements in enabling language agents to tackle simple tasks. However, applying them for complex, multi-step, long-horizon... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/agent-trees/02-arxiv-org-plan-and-act-improving-planning-of-agents-for-long-horizon-t.md`

## 관련 문서

- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[orchestrator-worker-pattern|Orchestrator-Worker Multi-Agent Pattern]]
- [[subagents|Subagents]]

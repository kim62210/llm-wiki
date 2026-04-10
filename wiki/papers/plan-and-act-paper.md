---
title: Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks
category: papers
page_type: paper
tags: [paper, planning, long-horizon, agents]
sources: [raw/2026-04-10-hot-ai-topics-sources/agent-trees/02-arxiv-org-plan-and-act-improving-planning-of-agents-for-long-horizon-t.md]
created: 2026-04-10
updated: 2026-04-10
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

## 관련 문서

- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[orchestrator-worker-pattern|Orchestrator-Worker Multi-Agent Pattern]]
- [[subagents|Subagents]]


---
title: Scaling Long-Horizon LLM Agent via Context-Folding
category: papers
page_type: paper
tags: [paper, agents, context-folding, rl]
sources: [raw/hot-topics-sources/2026-04-10/029-scaling-long-horizon-llm-agent-via-context-folding.md]
created: 2026-04-10
updated: 2026-04-10
---

# Scaling Long-Horizon LLM Agent via Context-Folding

서브태스크를 branch한 뒤 fold하여 요약으로 되돌리는 **Context-Folding**을 RL 프레임워크로 학습시킨 논문이다.

## 핵심 기여

- sub-trajectory를 완료 후 접어 넣는 folding 연산을 long-horizon agent의 기본 행동으로 제안
- FoldGRPO라는 end-to-end RL 학습 프레임워크 도입
- summarization-based context management보다 더 작은 active context로 경쟁력 있는 성능을 달성

## 결과와 시사점

- Deep Research, SWE 계열 과제에서 ReAct baseline과 동등 또는 우수 성능
- active context를 약 10배 줄이면서도 성능 유지

## 한계

folding 정책을 학습시키는 보상 설계가 까다롭고, 요약이 잘못되면 이후 단계 전체에 누적 오류가 생길 수 있다.

## 실무 적용 관점

장기 호흡 agent를 설계할 때 context budget을 늘리는 대신 **작업 구조 자체를 접는 방식**으로 문제를 풀 수 있음을 보여준다.

## 관련 문서

- [[context-folding]]
- [[long-horizon-rl-training-for-agents]]
- [[subagents]]

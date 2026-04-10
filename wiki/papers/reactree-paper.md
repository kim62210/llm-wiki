---
title: ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning
category: papers
page_type: paper
tags: [paper, agents, planning, hierarchy]
sources: [raw/hot-topics-sources/2026-04-10/030-reactree-hierarchical-llm-agent-trees-with-control-flow-for-long-horizon-task-pl.md, raw/2026-04-10-hot-ai-topics-sources/agent-trees/01-arxiv-org-reactree-hierarchical-llm-agent-trees-with-control-flow-for-.md]
created: 2026-04-10
updated: 2026-04-10
---

# ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

단일 trajectory 대신 agent tree와 control flow node를 도입해 장기 계획 문제를 푸는 hierarchical planning 논문이다.

## 핵심 기여

- 복잡한 목표를 subgoal tree로 쪼개는 agent node + control flow node 구조 제안
- episodic memory와 working memory를 함께 엮어 트리 탐색 품질 향상
- ReAct 같은 평면적 루프 대비 hierarchy의 장점을 정량적으로 제시

## 결과와 시사점

- WAH-NL에서 Qwen 2.5 72B 기준 61% 성공률로 ReAct 31%를 크게 상회
- ALFRED 등 장기 계획 과제에서도 일관된 우위 보고

## 한계

트리 확장 전략과 control flow 자체가 추가 복잡도를 만들며, 환경별 탐색 비용이 커질 수 있다.

## 실무 적용 관점

long-horizon planning에서 핵심은 더 긴 CoT가 아니라 **계획 구조를 계층화하고 기억을 국소화하는 것**이라는 메시지를 준다.

## 관련 문서

- [[agent-trees]]
- [[subagents]]
- [[agent-memory-systems]]

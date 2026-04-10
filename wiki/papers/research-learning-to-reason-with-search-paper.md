---
title: ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning
category: papers
page_type: paper
tags: [paper, search, reinforcement-learning, reasoning]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/05-arxiv-org-research-learning-to-reason-with-search-for-llms-via-reinfor.md]
created: 2026-04-10
updated: 2026-04-10
---

# ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning

search를 reasoning 과정의 일부로 보고, 이를 강화학습으로 최적화하는 접근을 제안한 논문이다.

## 핵심 기여

- search policy와 reasoning policy를 함께 학습 대상으로 설정
- retrieval을 외부 부가 기능이 아니라 문제 해결 루프의 핵심 행동으로 통합
- RL을 통해 search-aware reasoning agent를 훈련하는 틀을 제공

## 결과와 시사점

- long-horizon reasoning에서 search는 단순 retrieval step이 아니라 적극적인 탐색 전략이 된다.
- search와 reasoning을 함께 학습시키는 것이 정적 CoT보다 더 강한 agent behavior를 만들 수 있음을 시사한다.

## 한계

search 품질과 환경 노이즈에 따라 학습 안정성이 흔들릴 수 있고, 실제 검색 인프라와의 결합 비용도 크다.

## 실무 적용 관점

이 논문은 “검색을 붙인 모델”보다 **검색을 배우는 에이전트**라는 관점이 앞으로 더 중요해질 수 있음을 보여준다.

## 관련 문서

- [[agentic-rl-survey-paper|The Landscape of Agentic Reinforcement Learning for LLMs: A Survey]]
- [[agentic-rag|Agentic RAG with Hierarchical Retrieval Interfaces]]
- [[tool-invocation-evaluators|Tool Selection & Tool Invocation Evaluators]]


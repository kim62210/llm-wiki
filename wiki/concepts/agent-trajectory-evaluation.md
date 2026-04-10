---
title: Agent Trajectory Evaluation
category: concepts
page_type: concept
tags: [concepts, concept, agent, trajectory, evaluation, evals-and-observability]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---
# Agent Trajectory Evaluation

이 페이지는 Agent Trajectory Evaluation를 다룬다. 핵심은 최종 출력이 아닌 에이전트의 중간 도구 호출 경로를 평가이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

최종 출력이 아닌 에이전트의 중간 도구 호출 경로를 평가.

## 왜 지금 중요한가

단순 Pass@1 메트릭이 "고득점 착시"를 만든다는 지적이 확산되면서, TRACE·AgentEvals 같은 궤적 기반 평가 프레임워크와 LangSmith 궤적 eval이 deep research 에이전트 평가의 기본 축이 되었다.

## 대표 자료

- [TRACE: Trajectory-Aware Comprehensive Evaluation for Deep Research Agents (arXiv:2602.21230)](https://arxiv.org/abs/2602.21230)
- [AgentEvals GitHub Repository (LangChain)](https://github.com/langchain-ai/agentevals)
- [How to evaluate your agent with trajectory evaluations (LangSmith Docs)](https://docs.langchain.com/langsmith/trajectory-evals)
- [A Study of Thought-Action-Result Trajectories (ASE 2025)](https://software-lab.org/publications/ase2025_trajectories.pdf)
- [An Open Toolkit for Diagnosing LLM Agent Trajectories (EMNLP 2025)](https://aclanthology.org/2025.emnlp-demos.15.pdf)

## 2026년 4월 핫토픽 맥락

단순 Pass@1 메트릭이 "고득점 착시"를 만든다는 지적이 확산되면서, TRACE·AgentEvals 같은 궤적 기반 평가 프레임워크와 LangSmith 궤적 eval이 deep research 에이전트 평가의 기본 축이 되었다.

### 추가 레퍼런스

- [TRACE: Trajectory-Aware Comprehensive Evaluation for Deep Research Agents (arXiv:2602.21230)](https://arxiv.org/abs/2602.21230)
- [AgentEvals GitHub Repository (LangChain)](https://github.com/langchain-ai/agentevals)
- [How to evaluate your agent with trajectory evaluations (LangSmith Docs)](https://docs.langchain.com/langsmith/trajectory-evals)
- [A Study of Thought-Action-Result Trajectories (ASE 2025)](https://software-lab.org/publications/ase2025_trajectories.pdf)
- [An Open Toolkit for Diagnosing LLM Agent Trajectories (EMNLP 2025)](https://aclanthology.org/2025.emnlp-demos.15.pdf)

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[error-analysis-for-evals]]
- [[multi-turn-agent-evaluation]]

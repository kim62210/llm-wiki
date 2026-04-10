---
title: Multi-Turn Agent Evaluation
category: concepts
page_type: concept
tags: [concepts, concept, multi, turn, agent, evaluation, evals-and-observability]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/multi-turn-agent-evaluation.md, raw/hot-topics-sources/2026-04-10/227-improve-agent-quality-with-insights-agent-and-multi-turn-evals.md, raw/hot-topics-sources/2026-04-10/228-langsmith-evaluation-documentation.md, raw/hot-topics-sources/2026-04-10/229-evaluate-end-to-end-agent-interactions-with-multi-turn-evals.md, raw/hot-topics-sources/2026-04-10/230-langsmith-evaluations-platform.md, raw/hot-topics-sources/2026-04-10/231-langsmith-platform-overview.md]
created: 2026-04-10
updated: 2026-04-10
---
# Multi-Turn Agent Evaluation

이 페이지는 Multi-Turn Agent Evaluation를 다룬다. 핵심은 대화 전체 세션 단위로 사용자 목표 달성 여부를 채점이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

대화 전체 세션 단위로 사용자 목표 달성 여부를 채점.

## 왜 지금 중요한가

LangSmith가 2025년 10월 "threads"를 일급 개념으로 승격하고 Multi-turn Evals + Insights Agent를 출시하면서, 단일 턴을 넘어 세션 전체를 평가하는 것이 2026년 상반기 에이전트 품질 관리의 새 기준이 되었다.

## 대표 자료

- [Improve agent quality with Insights Agent and Multi-turn Evals (LangChain Blog, 2025-10-23)](https://blog.langchain.com/insights-agent-multiturn-evals-langsmith/)
- [LangSmith Evaluation Documentation](https://docs.langchain.com/langsmith/evaluation)
- [Evaluate end-to-end agent interactions with Multi-turn Evals (LangChain Changelog)](https://changelog.langchain.com/announcements/evaluate-end-to-end-agent-interactions-with-multi-turn-evals)
- [LangSmith Evaluations Platform](https://www.langchain.com/langsmith/evaluation)
- [LangSmith Platform Overview](https://www.langchain.com/langsmith-platform)

## 해석 포인트

Multi-Turn Agent Evaluation은 **성능만이 아니라 운영 설계까지 함께 봐야 하는 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `langchain.com×2, blog.langchain.com×1, docs.langchain.com×1, changelog.langchain.com×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 대화 전체 세션 단위로 사용자 목표 달성 여부를 채점.
- 왜 중요한가: LangSmith가 2025년 10월 "threads"를 일급 개념으로 승격하고 Multi-turn Evals + Insights Agent를 출시하면서, 단일 턴을 넘어 세션 전체를 평가하는 것이 2026년 상반기 에이전트 품질 관리의 새 기준이 되었다.
- 직접 수집 원문: 5개
- 주요 도메인: langchain.com×2, blog.langchain.com×1, docs.langchain.com×1, changelog.langchain.com×1

## 핵심 메커니즘

대화 전체 세션 단위로 사용자 목표 달성 여부를 채점. 이 개념은 단일 문장 정의보다 **어떤 failure mode를 설명하는지, 어떤 구조적 trade-off를 드러내는지**를 함께 볼 때 가치가 커진다.

## 핵심 포인트

Multi-Turn Agent Evaluation는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 이 페이지는 Multi-Turn Agent Evaluation를 다룬다. 핵심은 대화 전체 세션 단위로 사용자 목표 달성 여부를 채점이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 langchain.com×2, blog.langchain.com×1, changelog.langchain.com×1, docs.langchain.com×1로 분포한다. 공식 문서/엔지니어링 글 비중이 높아 운영·제품 맥락이 강하다.

## 실무 관점

개념 페이지는 용어 정의에서 끝나지 않고, 어떤 시스템 설계 문제를 해결하려고 등장했는지와 어디까지가 적용 범위인지까지 함께 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/multi-turn-agent-evaluation.md`

### source별 핵심 신호

- **Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmith** (`blog.langchain.com`): https://blog.langchain.com/insights-agent-multiturn-evals-langsmith/
  - 메모: We’re releasing new capabilities in LangSmith to help monitor agents in production.
- **LangSmith Evaluation - Docs by LangChain** (`docs.langchain.com`): https://docs.langchain.com/langsmith/evaluation
  - 메모: Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. Buy tickets >
- **LangChain - Changelog | Evaluate end-to-end agent interactions with** (`changelog.langchain.com`): https://changelog.langchain.com/announcements/evaluate-end-to-end-agent-interactions-with-multi-turn-evals
  - 메모: Quick start agents with any model provider
- **LangSmith - LLM & AI Agent Evals Platform: Continuously improve agents** (`langchain.com`): https://www.langchain.com/langsmith/evaluation
  - 메모: Quick start agents with any model provider
- **LangSmith: AI Agent & LLM Observability and Evals Platform** (`langchain.com`): https://www.langchain.com/langsmith-platform
  - 메모: Quick start agents with any model provider

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[agent-trajectory-evaluation]]
- [[tool-invocation-evaluators]]

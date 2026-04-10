---
title: Memory in the Age of AI Agents
category: papers
page_type: paper
tags: [paper, agents, memory, survey]
sources: [raw/hot-topics-sources/2026-04-10/016-memory-in-the-age-of-ai-agents.md]
created: 2026-04-10
updated: 2026-04-10
---

# Memory in the Age of AI Agents

에이전트 메모리 연구를 token-level, parametric, latent memory와 factual / experiential / working memory 축으로 재정리한 대형 서베이다.

## 핵심 기여

- agent memory와 LLM memory, RAG, context engineering의 경계를 분리
- 형태(forms), 기능(functions), 동학(dynamics) 세 축으로 메모리 연구를 재구성
- 벤치마크와 오픈소스 프레임워크를 함께 정리해 실무/연구 접점을 제공

## 결과와 시사점

- 장기 지속 에이전트에서 memory가 독립 설계축이라는 공감대를 제공
- 후속 연구 주제(자동화, RL 통합, 멀티모달, 신뢰성)를 명시적으로 지도화

## 한계

서베이이기 때문에 특정 설계의 우월성을 결정적으로 증명하지는 않으며, taxonomy 자체도 이후 빠르게 진화할 수 있다.

## 실무 적용 관점

메모리 시스템을 단순 '대화 저장'으로 보지 않고, **사실 / 경험 / 작업 메모리**를 분리 설계해야 한다는 기준점을 준다.

## 관련 문서

- [[agent-memory-systems]]
- [[context-engineering]]
- [[agentic-rag]]

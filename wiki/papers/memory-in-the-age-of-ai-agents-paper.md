---
title: Memory in the Age of AI Agents
category: papers
page_type: paper
tags: [paper, agents, memory, survey]
sources: [raw/hot-topics-sources/2026-04-10/016-memory-in-the-age-of-ai-agents.md]
created: 2026-04-10
updated: 2026-04-13
---
# Memory in the Age of AI Agents

에이전트 메모리 연구를 token-level, parametric, latent memory와 factual / experiential / working memory 축으로 재정리한 대형 서베이다.

## 핵심 기여

- [[agent-memory-systems|agent memory]]와 LLM memory, [[agentic-rag|RAG]], context engineering의 경계를 분리
- 형태(forms), 기능(functions), 동학(dynamics) 세 축으로 메모리 연구를 재구성
- 벤치마크와 오픈소스 프레임워크를 함께 정리해 실무/연구 접점을 제공

## 결과와 시사점

- 장기 지속 에이전트에서 memory가 독립 설계축이라는 공감대를 제공
- 후속 연구 주제(자동화, RL 통합, 멀티모달, 신뢰성)를 명시적으로 지도화

## 한계

서베이이기 때문에 특정 설계의 우월성을 결정적으로 증명하지는 않으며, taxonomy 자체도 이후 빠르게 진화할 수 있다.

## 실무 적용 관점

메모리 시스템을 단순 '대화 저장'으로 보지 않고, **사실 / 경험 / 작업 메모리**를 분리 설계해야 한다는 기준점을 준다.

## 문제 설정

`Memory in the Age of AI Agents`는 **긴 컨텍스트/메모리 병목을 어떻게 줄이는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다
- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `Memory in the Age of AI Agents`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **2512.13564 Memory in the Age of AI Agents** — https://arxiv.org/abs/2512.13564 · 초록 단서: Memory has emerged, and will continue to remain, a core capability of foundation model-based agents. As research on agent memory rapidly expands and attracts unprecedented atten... · snapshot: `raw/hot-topics-sources/2026-04-10/016-memory-in-the-age-of-ai-agents.md`

## 관련 문서

- [[agent-memory-systems]]
- [[context-engineering]]
- [[agentic-rag]]

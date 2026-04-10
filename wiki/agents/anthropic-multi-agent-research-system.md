---
title: Anthropic Multi-Agent Research System
category: agents
page_type: summary
tags: [agents, summary, anthropic, multi-agent, research]
sources: [raw/hot-topics-sources/2026-04-10/006-how-we-built-our-multi-agent-research-system.md, raw/2026-04-10-hot-ai-topics-sources/agent-trees/05-anthropic-com-how-we-built-our-multi-agent-research-system.md]
created: 2026-04-10
updated: 2026-04-10
---

# Anthropic Multi-Agent Research System

Anthropic이 Claude Research 기능의 백엔드로 사용한 멀티 에이전트 연구 시스템을 설명하는 엔지니어링 글 요약이다. 단일 에이전트를 더 똑똑하게 만드는 대신, **리드 에이전트와 병렬 서브에이전트의 협업 구조**로 성능을 확장한 사례라는 점에서 중요하다.

## 핵심 내용

- 리드 에이전트가 사용자 질의를 해석하고 조사 전략을 세운다.
- 서브에이전트들은 서로 다른 방향으로 병렬 탐색을 수행한다.
- 각 서브에이전트는 자기 컨텍스트 안에서 검색과 도구 사용을 반복하고, 결과만 압축해 반환한다.
- 마지막에는 citation agent가 근거 위치를 정리해 응답의 출처를 강화한다.

## 왜 중요한가

이 글은 멀티 에이전트 시스템이 단순한 아이디어 차원이 아니라, 실제 프로덕션급 Research 기능에 적용되었음을 보여준다. 특히 Anthropic이 내부 평가에서 **lead agent + parallel subagents** 구조가 단일 agent보다 크게 우수했다고 밝힌 점은, 오케스트레이션 자체가 성능 스케일링 레버라는 점을 뒷받침한다.

## 설계 포인트

### 1. breadth-first 탐색에 강함
독립 방향을 동시에 파고들 수 있기 때문에, 검색 공간이 넓은 문제에서 강점을 보인다.

### 2. context window를 병렬로 확장
서브에이전트가 각자 독립 컨텍스트를 가지므로, 전체 시스템은 사실상 더 많은 토큰 예산을 병렬로 사용할 수 있다.

### 3. coordination cost가 생김
에이전트 수가 늘수록 tool design, evaluation, prompt engineering, coordination failure가 더 중요해진다.

## 실무 적용 관점

이 문서는 “멀티 에이전트가 좋다”가 아니라, **언제 멀티 에이전트가 비용을 정당화하는가**를 묻도록 만든다. 검색 범위가 넓고 병렬 탐색 가치가 큰 태스크에서는 유효하지만, 실시간 협업과 강한 상태 공유가 필요한 작업에서는 오히려 coordination cost가 병목이 될 수 있다.

## 관련 문서

- [[orchestrator-worker-pattern|Orchestrator-Worker Multi-Agent Pattern]]
- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[subagents|Subagents]]


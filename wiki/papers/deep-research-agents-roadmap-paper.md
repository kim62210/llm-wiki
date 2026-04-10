---
title: Deep Research Agents: A Systematic Examination and Roadmap
category: papers
page_type: paper
tags: [paper, agents, research, roadmap, long-horizon]
sources: [raw/2026-04-10-hot-ai-topics-sources/agent-trees/03-arxiv-org-deep-research-agents-a-systematic-examination-and-roadmap.md]
created: 2026-04-10
updated: 2026-04-10
---

# Deep Research Agents: A Systematic Examination and Roadmap

deep research agent를 하나의 제품 카테고리가 아니라 **장기 정보 탐색과 합성 문제를 푸는 에이전트 클래스**로 바라보는 로드맵형 논문이다.

## 핵심 기여

- deep research agent의 문제 설정과 설계 축을 체계적으로 정리
- 장기 정보 탐색, 멀티스텝 검색, 근거 합성, citation 생성 같은 요소를 하나의 워크플로우로 묶음
- 이후 연구가 어디에 집중해야 하는지 로드맵 형태로 제안

## 결과와 시사점

- deep research는 단순 web search wrapper가 아니라, planning / retrieval / synthesis / verification가 결합된 시스템 문제다.
- 따라서 모델 성능만으로는 충분하지 않고, 하네스와 평가 체계가 함께 설계돼야 한다.

## 한계

로드맵형 논문이라 설계 공간을 잘 보여 주지만, 특정 아키텍처가 항상 최선이라는 결론을 주지는 않는다.

## 실무 적용 관점

이 문서는 deep research agent를 만들 때 “검색을 더 잘하게 만들자”보다 **어떤 단계들을 분리하고 어떤 실패를 측정할 것인가**를 먼저 생각하게 만든다.

## 관련 문서

- [[anthropic-multi-agent-research-system|Anthropic Multi-Agent Research System]]
- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[orchestrator-worker-pattern|Orchestrator-Worker Multi-Agent Pattern]]


---
title: Deep Research Agents: A Systematic Examination and Roadmap
category: papers
page_type: paper
tags: [paper, agents, research, roadmap, [[long-running-agent-harnesses|long-horizon]]]
sources: [raw/2026-04-10-hot-ai-topics-sources/agent-trees/03-arxiv-org-deep-research-agents-a-systematic-examination-and-roadmap.md]
created: 2026-04-10
updated: 2026-04-13
---
# Deep Research Agents: A Systematic Examination and Roadmap

deep [[coding-agent|research agent]]를 하나의 제품 카테고리가 아니라 **장기 정보 탐색과 합성 문제를 푸는 에이전트 클래스**로 바라보는 로드맵형 논문이다.

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

## 문제 설정

`Deep Research Agents: A Systematic Examination and Roadmap`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다
- 검증 신호 자체를 학습·강화해야 test-time scaling이 의미를 가진다는 관점이 숨어 있다
- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `Deep Research Agents: A Systematic Examination and Roadmap`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **Deep Research Agents: A Systematic Examination And Roadmap** — https://arxiv.org/abs/2506.18096 · 초록 단서: The rapid progress of Large Language Models (LLMs) has given rise to a new category of autonomous AI systems, referred to as Deep Research (DR) agents. These agents are designed... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/agent-trees/03-arxiv-org-deep-research-agents-a-systematic-examination-and-roadmap.md`

## 분해된 설계 공간

| 축 | 논문이 구분하는 선택지 | 위키 해석 |
|---|---|---|
| 정보 획득 | API 기반 retrieval vs browser-based exploration | 정적 데이터 접근과 웹 환경 탐색은 실패 모드가 다르다 |
| tool stack | code execution, multimodal input, MCP integration | deep research는 검색만이 아니라 실행과 확장성 문제까지 포함한다 |
| workflow | static vs dynamic | 고정 체인으로 충분한지, 도중에 계획을 바꾸는지가 큰 차이를 만든다 |
| composition | single-agent vs multi-agent | 탐색 범위가 넓을수록 병렬 분업 가치가 커진다 |
| benchmark 한계 | 외부 지식 제한, sequential inefficiency, metric misalignment | 현재 평가가 실제 research work의 목표와 어긋날 수 있음을 지적한다 |

## 실무 해석

이 논문이 좋은 이유는 "deep research agent를 만들어라"가 아니라, **어떤 축을 먼저 선택해야 하는지**를 보여준다는 데 있다. 실제로 제품을 만들 때도 검색기 성능, 브라우저 안정성, citation 품질, orchestrator 설계를 한 번에 최적화하기 어렵기 때문에, 이 분해표가 우선순위를 정하는 기준점이 된다.

## 관련 문서

- [[anthropic-multi-agent-research-system|Anthropic Multi-Agent Research System]]
- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[orchestrator-worker-pattern|Orchestrator-Worker Multi-Agent Pattern]]

---
title: SkyworkAI DeepResearchAgent
category: agents
page_type: entity
project: SkyworkAI DeepResearchAgent
tags: [agents, entity, deep-research, skyworkai, multi-agent]
sources: [raw/2026-04-10-hot-ai-topics-sources/agent-trees/04-github-com-skyworkai-deepresearchagent.md]
created: 2026-04-10
updated: 2026-04-13
---
# SkyworkAI DeepResearchAgent

SkyworkAI가 공개한 deep research agent 구현체 허브 페이지다. [[deep-research-agents-roadmap|Deep Research Agents Roadmap]]의 실제 구현 레퍼런스이다. 논문/블로그 수준의 설계 논의를 실제 오픈소스 시스템으로 확인할 수 있다는 점에서 가치가 있다.

## 개요

이 프로젝트는 [[long-horizon-agent-benchmarks|long-horizon]] research workflow를:

- planning
- search
- [[orchestrator-worker-pattern|multi-agent coordination]]
- synthesis

같은 단계로 분리해 구현한 오픈소스 레퍼런스에 가깝다.

## 왜 중요한가

많은 deep research 논의가 개념 수준에 머무는 반면, 이 프로젝트는 **실제 구현 관점**에서 아키텍처를 확인할 수 있게 해 준다. 즉 “어떻게 만들었는가”를 GitHub 수준에서 추적할 수 있다.

## 실무 적용 관점

이 엔티티는 완성형 제품이라기보다, deep research agent 설계를 검토할 때 참고할 수 있는 공개 구현체다. 따라서 직접 도입보다도:

1. 어떤 모듈 분리가 쓰였는지  
2. 어떤 툴 계약을 두었는지  
3. orchestration이 어떻게 코드로 표현되는지  

를 확인하는 용도로 읽는 것이 좋다.

## 원문이 다루는 흐름

관련 source를 묶어 보면 `SkyworkAI DeepResearchAgent`는 `Navigation Menu` → `Search code, repositories, users, issues, pull requests...` → `Provide feedback` → `Saved searches` → `Use saved searches to filter your results more quickly` 축으로 설명된다. 즉 기능 목록 하나보다 **정체성·연동 방식·운영 경계**를 같이 봐야 이 항목의 의미가 선명해진다.

- 따라가야 할 순서: Navigation Menu, Search code, repositories, users, issues, pull requests..., Provide feedback, Saved searches, Use saved searches to filter your results more quickly
- 위키에 남겨야 할 축: 이 대상이 맡는 역할, 연동 방식과 권한 경계, 도입 시 운영 제약

## 읽기 포인트

- 이 문서는 **도구 자체보다 운영 경계와 도입 전제를 어떻게 읽어야 하는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- `SkyworkAI DeepResearchAgent` 같은 entity 페이지는 기능 카탈로그가 아니라 허브이므로, 주변 summary/paper 문서와 연결해서 읽어야 도입 판단 기준이 생긴다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **GitHub - SkyworkAI/DeepResearchAgent: DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains.** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/agent-trees/04-github-com-skyworkai-deepresearchagent.md` · source: https://github.com/SkyworkAI/DeepResearchAgent · 볼 섹션: Navigation Menu, Search code, repositories, users, issues, pull requests..., Provide feedback, Saved searches

## 관련 문서

- [[deep-research-agents-roadmap-paper|Deep Research Agents: A Systematic Examination and Roadmap]]
- [[anthropic-multi-agent-research-system|Anthropic Multi-Agent Research System]]
- [[agent-trees|Hierarchical Planning with Agent Trees]]

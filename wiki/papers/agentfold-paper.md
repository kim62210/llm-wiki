---
title: AgentFold: Long-Horizon Web Agents with Proactive Context Management
category: papers
page_type: paper
tags: [paper, agents, context-folding, web-agents]
sources: [raw/hot-topics-sources/2026-04-10/004-agentfold-long-horizon-web-agents-with-proactive-context-management.md]
created: 2026-04-10
updated: 2026-04-10
---

# AgentFold: Long-Horizon Web Agents with Proactive Context Management

웹 에이전트가 단순히 로그를 누적하는 대신, 히스토리를 능동적으로 접어 넣는 **proactive context management** 패러다임을 제안한다.

## 핵심 기여

- context를 수동 로그가 아니라 적극적으로 재구성하는 cognitive workspace로 재정의
- 세밀한 보존과 깊은 추상화를 모두 허용하는 folding 연산 도입
- BrowseComp 계열에서 대형 오픈 모델과 일부 proprietary agent를 넘어서는 결과 제시

## 결과와 시사점

- BrowseComp 36.2%, BrowseComp-ZH 47.3%
- 대규모 continual pretraining이나 RL 없이 supervised fine-tuning만으로 strong baseline을 상회

## 한계

웹 탐색 특화 설정에서 강점을 보인 만큼, 일반 코딩/도구 사용 환경으로 옮길 때는 folding 정책의 일반화가 추가 검증돼야 한다.

## 실무 적용 관점

긴 히스토리를 다루는 agent는 단순 요약보다 **언제 세부를 남기고 언제 과감히 접을지**를 제어하는 정책이 중요하다는 점을 보여준다.

## 관련 문서

- [[context-folding]]
- [[context-engineering]]
- [[subagents]]

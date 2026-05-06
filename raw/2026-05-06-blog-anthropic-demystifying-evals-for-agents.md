---
source: blog
url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
title: Demystifying evals for AI agents
author: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe (Anthropic)
date: 2026-01-09
fetched: 2026-05-06
status: pending_ingest
tags: [agents, evaluation, evals, anthropic-engineering, swe-bench, pass-at-k]
---

# Demystifying evals for AI agents (Anthropic Engineering)

## 핵심 명제

에이전트 평가는 single-turn LLM 평가보다 근본적으로 어렵다:
- 다중 턴 운영
- 도구 호출
- 상태 변경
- 중간 결과에 적응

따라서 **여러 grader 타입을 결합한 정교한 평가 전략** 필요.

## Agents가 어려운 이유

> "frontier models can also find creative solutions that surpass the limits of static evals"

사례: Opus 4.5가 비행 예약 정책의 loophole을 발견 - 기술적으로 eval에 "fail" 했지만 사용자에게 더 좋은 결과 제공.

에이전트의 자율성/지능/유연성 자체가 평가의 어려움을 만든다.

## 시작: 20-50 Task 접근

> "20-50 simple tasks drawn from real failures"

- 수백 개를 기다리지 말 것
- 초기 단계 변화는 큰 effect size
- 수동 체크와 사용자 보고된 실패를 테스트 케이스로 변환

작업 품질 기준:
> "A good task is one where two domain experts would independently reach the same pass/fail verdict."

각 작업에는 reference solution이 있어야 함.

## 3가지 Grader 타입

### Code-based graders
- Fast, cheap, objective, reproducible
- String matching, binary tests, static analysis, outcome verification
- 단점: 유효한 변형에 brittle

### Model-based graders
- Flexible, scalable, 뉘앙스 처리
- Rubric-based scoring, natural language assertions
- 단점: 비결정적, 인간 판단 대비 calibration 필요

### Human graders
- Gold standard
- 비용 비싸고 느림

## Agent Type별 전략

### Coding Agents
> "well-specified tasks, stable test environments, and thorough tests for the generated code"

- SWE-bench Verified - test suite 실행으로 채점
- Terminal-Bench - end-to-end 기술 작업
- 트랜스크립트 분석으로 코드 품질 평가 (heuristics + LLM rubrics)

### Conversational Agents
> "verifiable end-state outcomes and rubrics that capture both task completion and interaction quality"

다차원 성공 측정:
- 티켓 해결 상태
- Turn count limits
- Tone appropriateness

LLM 시뮬레이션 페르소나로 확장 인터랙션.

### Research Agents
> "experts may disagree on whether a synthesis is comprehensive, ground truth shifts as reference content changes constantly"

전략: grader 타입 결합 + 잦은 인간 전문가 calibration
- Groundedness checks
- Coverage checks
- Source quality verification

### Computer Use Agents
실제/샌드박스 환경에서 실행, 결과 검증:
- WebArena: URL과 페이지 상태 체크
- OSWorld: 파일 시스템 상태, 앱 config, DB 콘텐츠 검사

## 핵심 유지보수

### Reading Transcripts
> "failures should seem fair: it's clear what the agent got wrong and why."

트랜스크립트를 통해 grader가 valid 솔루션을 잘못 거부하는지 확인 - 에이전트 개발의 critical skill.

### Avoiding Saturation
- Capability eval이 100%면 개선 신호 없음
- Eval saturation 시 진보가 느려짐
- 큰 개선이 작은 점수 상승으로 표현되는 deceptive metrics

### Long-term Health
> "dedicated evals teams to own core infrastructure, while domain experts and product teams contribute most eval tasks"

Eval-driven development - 기능 구현 전 테스트 빌드.

## 핵심 통계

- SWE-bench: "from 40% to >80% in just one year"
- Opus 4.5 CORE-Bench: 처음 42% → 채점 이슈 수정 후 **95%로 상승**
- METR가 misconfigured task 발견: 채점 요구가 stated instructions를 따르는 모델을 처벌함

## Non-Determinism Metrics

복합 메트릭으로 변동성 캡처:

- **pass@k**: k번 시도 중 적어도 1번 성공할 확률 (도구처럼 1번 성공으로 충분한 경우)
- **pass^k**: 모든 k 시도가 성공할 확률 (사용자 직면 에이전트, 신뢰성 critical)

> "At k=10, these metrics diverge dramatically—pass@k approaches 100% while pass^k falls toward 0%."

## 더 큰 평가 프레임

자동 evals + production monitoring + A/B testing + user feedback + transcript review + systematic human studies.

> "Swiss Cheese Model from safety engineering"

단일 방법이 모든 이슈 못 잡음. 효과적 팀은 **모든 접근법 결합**.

## 메모

- 게시일: 2026년 1월 9일
- Authors: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe
- 관련: "Building effective agents", "How we built our multi-agent research system" 시리즈

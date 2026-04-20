---
title: OMC Deep Interview
aliases: [OMC Deep Interview]
category: tooling
page_type: project-internal
project: oh-my-claudecode
tags: [omc, deep-interview, socratic, [[context-engineering|requirements]], ouroboros, ambiguity]
sources: [raw/2026-04-09-omc-README.md, raw/2026-04-09-omc-AGENTS.md]
created: 2026-04-09
updated: 2026-04-13
---
# OMC Deep Interview

> Socratic 질문과 **수학적 모호성 측정**으로 요구사항을 명확화하는 스킬. Ouroboros에서 영감.

## 개요

Deep Interview는 사용자의 아이디어가 **충분히 명확해질 때까지** 소크라테스식 질문을 반복한다. 단순한 "몇 가지 질문" 방식이 아니라, **mathematical ambiguity gating**으로 명확도를 수치화하고 임계값을 넘을 때까지 계속 묻는다.

OMC 레퍼런스에 따르면 "Ouroboros-inspired"로 명시되어 있다.

## 호출 방법

```bash
# 매직 키워드
deep interview "I want to build a task management app"
interview me about this feature
don't assume — interview first
ouroboros: design a new product

# 슬래시
/deep-interview "I want to build a task management app"
/deep-interview --autoresearch improve startup performance
```

활성 키워드: `interview`, `deep interview`, `gather requirements`, `interview me`, `don't assume`, `ouroboros`

## 언제 쓰나

README의 "Not Sure Where to Start?" 섹션이 전형적 용례:

> 요구사항이 불확실하거나, 아이디어가 모호하거나, 설계를 마이크로매니지하고 싶을 때.

즉:
- "뭔가 만들고 싶은데 구체적으로는 잘 모르겠다"
- "아이디어는 있는데 빈 구멍이 많다"
- "autopilot 돌리기 전에 생각을 정리하고 싶다"

## 동작 원리

```
User: "/deep-interview I want to build a task management app"
    │
    ▼
초기 모호성 측정 → 높음
    │
    ▼
Round 1 질문
    "이 앱은 누구를 위한 것인가?"
    "기존 Todo 앱과 어떻게 다른가?"
    "핵심 가치 제안은 무엇인가?"
    │
    ▼
사용자 답변 수집
    │
    ▼
모호성 재측정 → 중간
    │
    ▼
Round 2 질문 (더 깊은 차원)
    "우선순위는 어떻게 정하는가?"
    "리마인더는 필요한가?"
    "팀 공유 기능은?"
    │
    ▼
...
    │
    ▼
모호성 < 임계값
    │
    ▼
실행 가능한 요구사항 생성 → 다음 단계 (autopilot/ralplan 등)
```

## 가중치 차원

Deep Interview는 여러 차원을 **가중 측정**한다. 소스에서 명시된 표현은 "weighted dimensions"로 요약. 전형적인 차원 예:

- **Who** (사용자·페르소나)
- **Why** (문제·가치 제안)
- **What** (기능·범위)
- **How** (제약·아키텍처)
- **When** (우선순위·타임라인)

각 차원의 모호도가 측정되어 총합이 임계값을 넘는 차원부터 우선 질문이 생성된다.

## Ambiguity Gating (수학적 게이트)

Deep Interview의 핵심은 **정량적 gating**이다:

1. 모든 차원에 대해 현재 모호도 점수 계산
2. 가중치 합계가 임계값 이상이면 인터뷰 계속
3. 임계값 미만이 되면 요구사항이 "충분히 명확"함 선언
4. 자동으로 다음 단계(실행)로 전환 가능

이는 "몇 번 질문하고 끝" 방식보다 신뢰성이 높다.

## 숨은 가정 노출

Socratic 방법론의 핵심: **사용자가 당연하게 여기지만 실제로는 결정되지 않은 것들**을 끌어낸다.

예시 질문:
- "이 기능이 '성공'하는 건 무엇을 의미하는가?"
- "사용자가 처음 앱을 열었을 때 보이는 화면을 그려볼 수 있는가?"
- "이 결정을 번복해야 한다면 어떤 징후가 나타나야 하는가?"
- "이 기능이 없다면 사용자는 어떻게 이 문제를 해결하는가?"

## 다른 스킬과의 연계

### → Autopilot

Deep Interview로 요구사항이 정제되면 바로 autopilot으로 실행할 수 있다:

```
/deep-interview "I want a todo app"
    │
    ▼ 인터뷰 완료 (모호성 < 임계값)
    │
    ▼
autopilot으로 자동 전환 (또는 사용자 명시 호출)
```

### → Ralplan

더 보수적인 경로. 인터뷰 → 기획 합의 → 실행:

```
/deep-interview → /ralplan → /autopilot
```

### → Autoresearch (`--autoresearch` 플래그)

인터뷰 결과를 바탕으로 `omc autoresearch` CLI 명령의 미션과 evaluator를 준비한다:

```bash
/deep-interview --autoresearch improve startup performance
```

이 경우 인터뷰는 **autoresearch의 런칭 준비** 역할. 인터뷰가 끝나면 `omc autoresearch --mission "..." --eval "..."`가 실행된다.

## `autoresearch`와의 관계

`omc autoresearch`는 thin-supervisor autoresearch runtime의 **실제 CLI 명령**이다:

```bash
omc autoresearch
omc autoresearch --mission "improve startup performance" --eval "npm test -- --run src/cli/__tests__/autoresearch.test.ts"
omc autoresearch init --topic "benchmark onboarding flow"
```

- 단독 슬래시 스킬 `/autoresearch`는 **존재하지 않음**
- In-session으로 시작하려면 `/deep-interview --autoresearch ...` 경로 사용

## 사용 시나리오

### 좋은 사용 사례

- **새 기능 기획**: "사용자 프로파일 섹션 만들고 싶어" → 페르소나, 필드, 권한 등 구체화 필요
- **아이디어 검증**: "이런 SaaS 해볼까?" → 시장·차별화·범위 명확화
- **요구사항 갭 메꾸기**: PM이 대략적인 PRD만 줬을 때 빈 곳 찾기
- **autopilot 전 준비**: autopilot이 헤매지 않도록 사전 정제

### 나쁜 사용 사례

- **이미 명확한 요구사항**: 사용자가 세부까지 다 정해 놓은 상태면 오버킬
- **기술적 디버깅**: 요구사항 명확화와 무관
- **단일 파일 수정**: 간단한 작업은 그냥 실행

## 실무 팁

- **인내심 필요**: 인터뷰가 길어질 수 있음. 사용자가 "그냥 해줘" 모드라면 적합하지 않음
- **답변 품질이 결과를 결정**: 대충 답하면 모호성이 떨어지지 않음 → 진지하게 답하라
- **중간 중단 가능**: `cancelomc`로 종료, 그 시점까지의 명확화된 내용은 남음
- **autoresearch와 결합**: 성능 최적화 같은 실험적 작업은 `--autoresearch` 플래그로 이어가면 효율적

## 관련 문서

- [[oh-my-claudecode]]
- [[omc-execution-modes]]
- [[omc-autopilot]]
- [[omc-ralplan]]
- [[omc-magic-keyword]]


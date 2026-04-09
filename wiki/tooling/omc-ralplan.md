---
title: OMC Ralplan
aliases: ["OMC Ralplan"]
category: tooling
page_type: project-internal
project: oh-my-claudecode
tags: [omc, ralplan, planning, consensus, planner, architect, critic]
sources: [raw/2026-04-09-omc-AGENTS.md, raw/2026-04-09-omc-ARCHITECTURE.md]
created: 2026-04-09
updated: 2026-04-09
---

# OMC Ralplan

> Planner + Architect + Critic의 반복 루프로 **컨센서스 기획**에 도달하는 스킬. Ralph 모드의 기획 게이트 역할도 함께 수행.

## 개요

Ralplan은 Ralph + Plan의 합성어다. 한 번의 기획으로 끝내지 않고 **세 에이전트의 의견이 합의될 때까지 반복**한다:

- `planner`: 태스크 시퀀싱과 실행 계획
- `architect`: 시스템 설계와 인터페이스
- `critic`: 갭 분석과 다각도 리뷰

셋 다 opus 티어로 운영되며 서로의 출력을 검토하는 구조다.

## 호출 방법

```bash
# 매직 키워드
ralplan this feature
consensus plan: database migration strategy

# 슬래시
/ralplan this refactor
```

활성 키워드: `ralplan`, `consensus plan`

## 동작 원리

### 기본 모드 (short)

```
User: "ralplan migrate to TypeScript"
    │
    ▼
Round 1
    ├─ planner 제안 → 초안
    ├─ architect 리뷰 + 수정
    └─ critic 갭 지적
    │
    ▼
Round 2 (critic이 요청하는 경우)
    ├─ planner 갭 반영 개정
    ├─ architect 재승인
    └─ critic 승인 또는 추가 지적
    │
    ▼
모두 동의 → 합의된 플랜 산출
```

### `--deliberate` 모드 (RALPLAN-DR)

고위험 작업에 사용하는 **RALPLAN-DR (Deliberative Review)** 구조적 심의 모드.

```bash
ralplan --deliberate migrate production database
```

- 더 많은 라운드 반복
- 각 라운드마다 명시적 논거 요구
- Critic이 하나의 갭도 발견하지 못해야 종료
- 토큰 비용 크게 증가하나 품질 가장 높음

## 왜 필요한가

단일 에이전트의 플랜 한계:
- **확증 편향**: 자기가 떠올린 첫 아이디어에 고착
- **갭 맹점**: 스스로 간과하는 사각지대를 지적해 줄 사람이 없음
- **깊이 부족**: 표면만 훑고 끝내는 경향

Ralplan의 해결:
- **다각도 리뷰**: planner(실행 가능성), architect(설계 건전성), critic(빈 구멍)
- **반복 정제**: 한 에이전트의 지적을 다른 에이전트가 수용해야 다음 라운드로
- **게이트**: 합의가 안 되면 실행 단계로 넘어갈 수 없음

## 에이전트 역할 경계

Ralplan의 세 에이전트는 각자 하지 말아야 할 일이 명확하다 ([[OMC Agent Catalog]] 참조):

| 에이전트 | Does | Does Not |
|---|---|---|
| `planner` | 태스크 플랜 작성 | 요구사항 분석, 플랜 자체 리뷰 |
| `architect` | 시스템 설계, 경계, 인터페이스 | 요구사항 수집, 기획 주도 |
| `critic` | 플랜 품질 갭 분석 | 요구사항 분석, 코드 분석 |

이 분리가 Ralplan의 품질 게이트를 유지한다.

## Ralph와의 관계

[[OMC Ralph Mode]]에는 **ralplan-first 게이트**가 있다:

```
Ralph 활성 + 구현 단계 진입?
    │
    ▼
.omc/plans/prd-*.md AND .omc/plans/test-spec-*.md 존재?
    │
    ├─ YES → 구현 허용
    └─ NO  → Ralplan으로 강제 이동, 기획부터 완성
```

즉 Ralph 모드는 반드시 Ralplan의 산출물(PRD + 테스트 스펙)이 있어야 실행 단계로 진입할 수 있다. 이는 "무계획 반복"을 방지한다.

## 산출물 경로

Ralplan은 합의된 기획을 다음 위치에 저장:

```
.omc/plans/
├── prd-<feature>.md          # 제품 요구사항 문서
├── test-spec-<feature>.md    # 테스트 스펙
└── autopilot-impl.md         # (Autopilot 사용 시)
```

## 사용 시나리오

### 좋은 사용 사례

- **고위험 마이그레이션**: 프로덕션 DB 스키마 변경, 인증 시스템 교체
- **복잡한 기능 설계**: 여러 서비스 연동이 필요한 신규 기능
- **아키텍처 결정**: 마이크로서비스 분리, 큐 도입, 캐시 전략

### 나쁜 사용 사례

- **단순 버그 수정**: 오버헤드만 큼
- **이미 명확한 요구사항**: 바로 구현이 더 빠름
- **실험적 프로토타입**: 빠른 반복이 더 가치 있음

## `--deliberate` 사용 기준

RALPLAN-DR 모드는 다음 조건일 때 고려:

- 되돌릴 수 없는 결정 (데이터 삭제, 프로덕션 머신 재구성)
- 법/보안 리스크가 큼
- 여러 팀이 영향받는 공통 인프라 변경
- 롤백 비용이 매우 높음

그 외에는 기본 모드로 충분하다.

## 실무 팁

- **플랜 산출물 커밋 여부**: `.omc/plans/`는 `.gitignore` 대상이지만 중요한 의사결정은 별도 문서로 복사해 커밋 권장
- **Critic의 "승인" 판단**: critic이 쉽게 통과시키면 의심. 한 번도 갭을 못 찾았다면 프롬프트 재검토
- **시간 비용**: opus 세 에이전트 × 여러 라운드 = 상당한 대기 시간. 긴급 작업에는 부적절
- **사용자 개입**: Ralplan은 사람 개입 없이 돌지만, 중간 산출물을 검토해 방향을 수정하는 것도 가능

## 관련 문서

- [[oh-my-claudecode (OMC)]]
- [[OMC Execution Modes]]
- [[OMC Ralph Mode]]
- [[OMC Autopilot]]
- [[OMC Agent Catalog]]
- [[OMC Deep Interview]]

---
title: OMC Ultrawork
aliases: ["OMC Ultrawork"]
category: tooling
page_type: project-internal
project: oh-my-claudecode
tags: [omc, ultrawork, parallel, burst, execution]
sources: [raw/2026-04-09-omc-README.md, raw/2026-04-09-omc-ARCHITECTURE.md, raw/2026-04-09-omc-HOOKS.md]
created: 2026-04-09
updated: 2026-04-09
---

# OMC Ultrawork

> 최대 병렬성으로 독립 태스크를 한꺼번에 해치우는 버스트 모드.

## 개요

Ultrawork는 **non-team 병렬 실행** 모드다. Team 모드는 staged 파이프라인(plan → prd → exec → verify → fix)으로 체계적이지만, Ultrawork는 그 오버헤드 없이 바로 병렬 spawn한다. 독립적이고 반복적인 작업에 적합.

## 호출 방법

```bash
# 매직 키워드
ultrawork implement user authentication with OAuth
ulw write all tests for this module
uw fix all eslint warnings
```

활성 키워드: `ultrawork`, `ulw`, `uw`, `parallel`

## 동작 원리

```
사용자: "ulw fix all TypeScript errors"
    │
    ▼
keyword-detector: ultrawork 감지
    │
    ▼
상태 파일 생성: .omc/state/ultrawork-state.json
    │
    ▼
오케스트레이터가 태스크를 독립 단위로 분해
    │
    ▼
Task 툴로 여러 자식 에이전트 동시 spawn (최대 6개)
    │
    ├─ executor 1: "fix errors in src/auth/"
    ├─ executor 2: "fix errors in src/api/"
    ├─ executor 3: "fix errors in src/ui/"
    └─ ...
    │
    ▼
각 결과 수집 후 통합 보고
```

## Team 모드와의 차이

| 항목 | Ultrawork | Team |
|---|---|---|
| 파이프라인 | 없음 (바로 실행) | 5-stage (plan→prd→exec→verify→fix) |
| 태스크 공유 | 독립 분배 | 공유 태스크 리스트 |
| 검증 | 비교적 약함 | 강함 (team-verify 단계) |
| 기획 | 없음 | 명시적 (team-plan/prd) |
| 적합 | 독립 반복 작업 | 복잡한 조율이 필요한 기능 |
| 오버헤드 | 작음 | 큼 |

**규칙**: "Team 오버헤드가 부담되는 버스트 병렬 작업"에 Ultrawork를 쓴다. 복잡한 기능 개발은 Team.

## Ralph와의 관계

Ralph 모드는 Ultrawork를 **자동 포함**한다. Ralph를 활성화하면 `linked_ultrawork: true`가 설정되면서 병렬 실행이 함께 켜진다.

```
ralph = persistence (verifier 종료 확인까지) + ultrawork (병렬)
```

즉 Ultrawork 단독 사용은 "지속 보장은 필요 없지만 병렬성은 원함" 시나리오다.

## 상태 구조

`.omc/state/ultrawork-state.json`:

```json
{
  "active": true,
  "reinforcement_count": 3,
  "started_at": "2025-01-15T10:30:00Z",
  "prompt": "ultrawork fix all tests",
  "session_id": "abc123",
  "linked_ralph": false,
  "last_checked_at": "2025-01-15T10:45:00Z"
}
```

- `reinforcement_count`: persistent-mode 훅이 주입한 "boulder never stops" 메시지 횟수
- `linked_ralph`: Ralph와 연동되어 있는지 (Ralph가 Ultrawork를 부른 경우)

## 병렬성 상한

OMC는 **최대 6개 동시 자식 에이전트**를 허용한다. Ultrawork는 이 상한 내에서 최대한 많은 태스크를 동시에 실행한다.

6개를 초과하는 작업은 큐에 쌓이고, 앞선 작업이 끝나는 대로 spawn된다.

## 모델 라우팅

Ultrawork로 spawn된 자식 에이전트들은 각자 자기 기본 모델을 사용한다:

- 기본 executor → sonnet
- explore가 필요하면 → haiku
- 리뷰 단계 → opus

즉 Ultrawork는 **모델을 통일하지 않는다**. [[OMC Model Routing]] 정책이 그대로 적용된다.

## 사용 예

### 좋은 사용 사례

- **일괄 버그 수정**: "fix all the lint warnings" — 각 파일이 독립적
- **문서 생성**: 여러 모듈에 대해 JSDoc/독스트링 일괄 작성
- **테스트 작성**: 각 함수별 테스트를 병렬 작성
- **리팩터링**: 파일 단위로 독립된 변환

```bash
ulw add jsdoc to every function in src/
ultrawork write unit tests for all utility functions
uw run all tests and fix the failing ones
```

### 나쁜 사용 사례

- **의존성이 있는 작업**: A가 끝나야 B를 시작할 수 있는 경우 → Team 모드 또는 순차 실행
- **복잡한 아키텍처 결정**: 병렬로 돌리면 에이전트마다 다른 선택을 할 수 있음 → Ralplan 먼저
- **정밀한 검증이 필요한 작업**: Ultrawork는 verifier가 기본 파이프라인에 없음 → Team이나 Ralph 사용

## 매직 키워드 설정

`config.jsonc`에서 ultrawork 트리거 키워드 커스터마이즈 가능:

```jsonc
{
  "magicKeywords": {
    "ultrawork": ["ultrawork", "ulw", "uw", "parallel", "burst"]
  }
}
```

## 취소 방법

```bash
cancelomc
# 또는
/oh-my-claudecode:cancel
```

`.omc/state/ultrawork-state.json`이 정리되고 진행 중인 spawn이 중단된다. 단, 이미 실행 중인 자식 에이전트의 완료는 기다림.

## 비용 고려

Ultrawork는 병렬성이 크기 때문에 **토큰 폭발 위험**이 있다. 6개 에이전트 × 각자 긴 작업 = 단일 작업의 6배 이상 비용.

**비용 관리 팁**:
- 단순 태스크는 ecomode와 조합해 haiku 강제
- 복잡한 작업이 많으면 max 병렬 수 조정 고려
- 사전에 범위를 좁혀서 불필요한 에이전트 spawn 방지

## 실무 고려사항

- **태스크 독립성 확인**: spawn 전에 진짜 독립적인지 확인. 아니면 서로 충돌
- **Git 동시 편집 주의**: 여러 executor가 같은 파일 건드리면 충돌 → 파일 단위로 분할
- **결과 통합 시간**: 병렬 실행은 빠르지만 결과 취합에는 여전히 오케스트레이터 시간이 걸림
- **첫 사용은 작게**: `uw fix 3 files` 같은 소규모로 시작해 패턴 파악 후 확장

## 관련 문서

- [[oh-my-claudecode (OMC)]]
- [[OMC Execution Modes]]
- [[OMC Ralph Mode]]
- [[OMC Team Mode]]
- [[OMC Model Routing]]
- [[Multi-Agent Orchestration]]

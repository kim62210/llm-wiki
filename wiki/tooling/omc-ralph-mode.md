---
title: OMC Ralph Mode
aliases: [OMC Ralph Mode, omc ralph mode, omc-ralph-mode]
category: tooling
page_type: project-internal
project: oh-my-claudecode
tags: [omc, ralph, persistence, verification, loop]
sources: [raw/2026-04-09-omc-HOOKS.md, raw/2026-04-09-omc-AGENTS.md, raw/2026-04-09-omc-ARCHITECTURE.md]
created: 2026-04-09
updated: 2026-04-13
---
# OMC Ralph Mode

> "The boulder never stops." 검증이 완료될 때까지 중단하지 않는 지속 실행 모드.

## 개요

Ralph는 Sisyphus처럼 작업을 계속 굴려 올리는 **지속(persistence) 모드**다. 일반적인 Claude 세션은 한 응답 사이클 후 종료되는 경향이 있지만, Ralph가 활성화되면 **verifier 에이전트가 "완료"로 확정하기 전까지** Claude는 중단할 수 없다.

프로젝트명이 "oh-my-claude-sisyphus"인 이유가 여기 있다.

## 호출 방법

```bash
# 매직 키워드 트리거
ralph: refactor the authentication module
ralph this file
don't stop until all tests pass
must complete the migration
keep going until zero errors
```

활성 키워드: `ralph`, `don't stop`, `must complete`, `keep going`, `until done`

## 동작 원리

```
사용자: "ralph: fix all TypeScript errors"
    │
    ▼
keyword-detector 훅: ralph 감지
    │
    ▼
상태 파일 생성: .omc/state/ralph-state.json
    { active: true, iteration: 0, max_iterations: 10, ... }
    │
    ▼
Claude가 작업 수행
    │
    ▼
Claude가 응답 종료 시도 (Stop 이벤트)
    │
    ▼
persistent-mode 훅 개입:
    - ralph-state.json active=true 확인
    - "The boulder never stops" 메시지 주입
    - iteration++ 후 Claude를 다시 트리거
    │
    ▼
Claude가 작업 계속
    │
    ▼
verifier 에이전트가 완료 확인 → active=false
    │
    ▼
persistent-mode가 Stop 허용 → 세션 종료
```

**핵심**: Ralph 자체는 스킬이지만, 실제 "안 멈추게 하는" 로직은 `persistent-mode` 훅이 담당. Ralph는 상태 파일을 만들고, 훅이 그 파일을 보고 Stop을 차단한다.

## Ralplan-First Gate

Ralph가 활성 상태일 때는 **기획 완성 게이트**가 적용된다:

```
Ralph 활성 + 구현 시작?
    │
    ▼
.omc/plans/prd-*.md 존재? AND .omc/plans/test-spec-*.md 존재?
    │
    ├─ YES → 구현 진행 허용
    └─ NO  → ralplan으로 강제 이동, 기획부터 완성
```

이 게이트는 "plan 없이 마구 코딩하다가 반복 실행에 갇히는" 시나리오를 막는다.

## Ultrawork 자동 포함

Ralph 모드에는 [[omc-ultrawork]]이 기본 포함된다. 즉 Ralph를 켜면 병렬 에이전트 오케스트레이션도 자동 활성화된다.

```
ralph = persistence + ultrawork + default execution
```

이는 "끝낼 때까지 + 최대 병렬로 작업"하는 조합이다.

## 상태 구조

`.omc/state/ralph-state.json`:

```json
{
  "active": true,
  "iteration": 3,
  "max_iterations": 10,
  "current_phase": "execution",
  "started_at": "2025-01-15T10:30:00Z",
  "prompt": "ralph: fix all tests",
  "session_id": "abc123",
  "project_path": "/path/to/project",
  "linked_ultrawork": true,
  "last_checked_at": "2025-01-15T11:15:00Z",
  "completed_at": null
}
```

**주요 필드**:
- `iteration` / `max_iterations`: 무한 루프 방지용 카운터
- `current_phase`: 현재 단계 ([[context-engineering|planning]]/execution/verification 등)
- `linked_ultrawork`: ultrawork 연동 여부
- `last_checked_at`: staleness 감지용 (2시간 이상 stale → inactive 처리)

## Staleness 처리

`persistent-mode` 훅은 상태 파일이 2시간 이상 오래되면 **stale**로 간주하고 inactive 처리한다. 이는 다음 시나리오를 방지:

- 사용자가 `cancelomc` 없이 세션을 닫음
- 기계를 껐다 켰는데 `.omc/state/ralph-state.json`이 여전히 `active: true`
- 새 세션이 시작되자마자 이전 상태에 묶여 "The boulder never stops" 무한 주입

2시간이 지나면 자동으로 놓아준다.

## 취소 방법

Ralph를 멈추는 유일한 방법:

```bash
# 매직 키워드
cancelomc
stopomc

# 슬래시 명령
/oh-my-claudecode:cancel
```

`cancel` 스킬이 `.omc/state/ralph-state.json`의 `active`를 false로 만들고 상태 파일을 정리.

> **주의**: `cancel`은 다른 모든 키워드보다 우선 순위가 높다. 사용자가 "cancelomc"를 입력하면 ralph가 같이 있어도 cancel만 처리된다.

## verifier 에이전트의 역할

Ralph 루프가 정상 종료되려면 `verifier` 에이전트가 완료를 확인해야 한다.

verifier가 점검하는 것:
- BUILD: 빌드 통과
- TEST: 모든 테스트 통과
- LINT: 린트 에러 0
- FUNCTIONALITY: 기능이 의도대로 동작
- ARCHITECT: Opus 티어 리뷰 승인
- TODO: 모든 태스크 완료
- ERROR_FREE: 해결되지 않은 에러 없음

**Evidence 요구사항**: 5분 이내의 실제 명령 출력이 포함되어야 함.

## 알림 연동

Ralph 모드가 첫 Stop 이벤트에 도달하면 Discord/Telegram/Slack 알림이 발송된다 (설정된 경우). 메시지에는 세션 정보와 진행 상황이 포함된다.

## 실무 사용법

### 좋은 사용 사례

- "모든 테스트가 통과할 때까지" 같은 명확한 종료 조건
- 여러 파일에 걸친 반복적 리팩터링
- 빌드 에러 전수 제거
- 중단되면 안 되는 장기 마이그레이션

### 나쁜 사용 사례

- 짧은 1회 작업 (오버헤드만 큼)
- 종료 조건이 모호한 탐색 작업 → `/deep-interview` 먼저
- 엄청난 토큰 예산이 없는 프로토타입

## 주의사항

- **취소 방법을 꼭 외울 것**: `cancelomc` 없이 세션을 닫으면 상태가 2시간 남아 있음
- **ralplan-first 게이트 우회 불가**: 기획 없이 바로 구현하고 싶으면 Ralph 말고 Ultrawork 사용
- **max_iterations 기본 10**: 그 이상 돌려야 하면 명시 설정 필요
- **에이전트 역할 분리**: writer ≠ verifier 원칙. 스스로 "다 했음"이라고 말하는 걸 믿지 않음

## 관련 문서

- [[oh-my-claudecode]]
- [[omc-execution-modes]]
- [[omc-ultrawork]]
- [[omc-hook-system]]
- [[omc-state-management]]
- [[omc-ralplan]]


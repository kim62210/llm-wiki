---
title: OMC Execution Modes
aliases: ["OMC Execution Modes"]
category: tooling
page_type: project-internal
project: oh-my-claudecode
tags: [omc, execution, team, autopilot, ralph, ultrawork, ccg, ralplan]
sources: [raw/2026-04-09-omc-README.md, raw/2026-04-09-omc-ARCHITECTURE.md, raw/2026-04-09-omc-AGENTS.md, raw/2026-04-09-omc-FEATURES.md]
created: 2026-04-09
updated: 2026-04-09
---

# OMC Execution Modes

> OMC가 제공하는 여러 실행 전략 한눈에 보기. Team부터 Ultrawork까지 6가지 모드가 있으며, 각기 다른 상황을 겨냥한다.

## 모드 한 줄 요약

| 모드 | 기본 용도 |
|---|---|
| **Team** (권장) | 5-stage 파이프라인 기반 다중 Claude 에이전트 조율 |
| **omc team (CLI)** | tmux 기반 실제 `claude`/`codex`/`gemini` 워커 프로세스 |
| **CCG** | Claude + Codex + Gemini 삼중 자문, Claude가 합성 |
| **Autopilot** | 아이디어 → 동작 코드 단일 리드 에이전트 자율 실행 |
| **Ultrawork** | 최대 병렬성 (non-team) |
| **Ralph** | 검증 통과할 때까지 반복하는 지속 모드 |
| **Pipeline** | 순차 스테이지 처리 |
| **Ultrapilot** (legacy) | autopilot 파이프라인 별칭 (deprecated) |

## 상세 비교

| 모드 | 실행 | 병렬성 | 끈기 | 계획 강도 |
|---|---|---|---|---|
| Team | staged pipeline | 높음 (N workers) | 중간 | 강함 (plan→prd→exec→verify→fix) |
| omc team CLI | tmux panes | 높음 (실제 프로세스) | 중간 | 사용자 지시 의존 |
| CCG | 3-model fan-out | 낮음 (3-way) | 낮음 | 낮음 |
| Autopilot | 5-phase pipeline | 중간 (Ralph+Ultrawork 조합) | 강함 | 강함 |
| Ultrawork | 다수 Task 툴 병렬 | 최대 | 중간 | 낮음 |
| Ralph | 반복 루프 | 낮음 | 최강 | 중간 (ralplan-first gate) |

## Team Mode (v4.1.7부터 기본)

**Canonical 오케스트레이션 표면**. Legacy `swarm` 키워드는 제거됨.

```bash
/team 3:executor "fix all TypeScript errors"
```

**Staged 파이프라인**: `team-plan → team-prd → team-exec → team-verify → team-fix (loop)`

**상태 전이**:
- `team-plan → team-prd`: 기획/분해 완료
- `team-prd → team-exec`: 수용 기준·범위 명시 완료
- `team-exec → team-verify`: 모든 실행 태스크가 terminal 상태 도달
- `team-verify → team-fix | complete | failed`: 검증 결과에 따라 분기
- `team-fix → team-exec | team-verify | complete | failed`: 수정 후 재실행

**종료 상태**: `complete`, `failed`, `cancelled`.

**재개**: 기존 team state 감지 후 마지막 미완료 스테이지부터 재개.

**활성화**:
```json
// ~/.claude/settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

상세: [[omc-team-mode]]

## omc team (CLI, v4.4.0+)

tmux 기반 **실제 워커 프로세스** 생성. `claude`/`codex`/`gemini` CLI를 split-pane으로 실행.

```bash
omc team 2:codex "review auth module for security issues"
omc team 2:gemini "redesign UI components for accessibility"
omc team 1:claude "implement the payment flow"
omc team status auth-review
omc team shutdown auth-review
```

| Surface | 워커 | 최적 |
|---|---|---|
| `omc team N:codex` | N개 Codex CLI 패널 | 코드 리뷰, 보안 분석, 아키텍처 |
| `omc team N:gemini` | N개 Gemini CLI 패널 | UI/UX, 문서, 대용량 컨텍스트 |
| `omc team N:claude` | N개 Claude CLI 패널 | tmux 내 Claude CLI 일반 작업 |

**v4.4.0 변경**: Codex/Gemini MCP 서버(`x`, `g` providers) 제거. 대신 CLI-first Team runtime으로 전환. 워커는 on-demand spawn, 태스크 완료 시 자동 종료 (idle 리소스 소비 없음).

**요구사항**: `codex`/`gemini` CLI 설치 + 활성 tmux 세션.

## Autopilot

아이디어 → 검증된 동작 코드까지 5-phase 자율 실행. 상세는 [[omc-autopilot]].

```bash
/autopilot "build a REST API for managing tasks"
# 또는
autopilot: build me a todo app
```

**5-Phase**:
1. **Expansion**: Analyst + Architect가 아이디어를 요구사항·스펙으로 확장
2. **Planning**: Architect가 실행 플랜 작성, Critic이 검증
3. **Execution**: Ralph + Ultrawork로 병렬 구현
4. **QA**: UltraQA가 build/lint/test 통과 보장
5. **Validation**: 전문 architect들이 기능·보안·품질 최종 리뷰

**기본 설정**:
- `maxIterations`: 10
- `maxExpansionIterations`: 2
- `maxArchitectIterations`: 5
- `maxQaCycles`: 5
- `maxValidationRounds`: 3
- `parallelExecutors`: 5
- `autoCommit`: false

## Ralph

"검증이 확인될 때까지 중단 금지". 상세는 [[omc-ralph-mode]].

```bash
ralph: refactor the authentication module
```

- `verifier` 에이전트가 완료 확인해야 루프 종료
- **ralplan-first gate**: ralph 활성 시 `.omc/plans/prd-*.md`와 `test-spec-*.md`가 모두 존재해야 구현 시작 허용
- ralph 활성화 시 ultrawork의 병렬 실행이 자동 포함됨

## Ultrawork

최대 병렬성. 독립 태스크를 한꺼번에 spawn. 상세는 [[omc-ultrawork]].

```bash
ultrawork implement user authentication with OAuth
ulw write all tests for this module
```

- Team 오버헤드가 부담되는 버스트 작업용
- ralph 모드의 내부 실행 엔진으로도 사용됨

## CCG (Claude-Codex-Gemini)

3개 모델에 동시 질의 후 Claude가 합성.

```bash
/ccg "review this authentication implementation"
/ccg Review this PR — architecture (Codex) and UI components (Gemini)
```

- `/ask codex` + `/ask gemini`를 병렬 실행
- Claude가 결과를 통합·판단
- Codex는 아키텍처/보안 강점, Gemini는 UI/대용량 컨텍스트 강점

상세: [[omc-ccg]]

## Ralplan

Planner + Architect + Critic 루프를 돌려 컨센서스에 도달하는 반복 기획. 상세는 [[omc-ralplan]].

```bash
ralplan this feature
```

- 기본: 짧고 빠른 컨센서스
- `--deliberate`: 고위험 작업용 RALPLAN-DR 구조적 심의 (길고 신중)

## Ultraqa

QA 사이클링 — test → verify → fix → repeat. Autopilot의 Phase 4로도 쓰임.

```bash
/oh-my-claudecode:ultraqa
```

- 상태 필드: `active`, `current_phase`, `iteration`, `started_at`, `completed_at`

## Deep Interview

Socratic 딥 인터뷰로 요구사항을 수학적으로 명확화. 상세는 [[omc-deep-interview]].

```bash
/deep-interview "I want to build a task management app"
```

- Ouroboros에서 영감받은 Ambiguity Gating
- 모호성이 기준 이하로 떨어질 때까지 질문 반복
- 완료 후 바로 autoresearch/autopilot으로 연결 가능

## Pipeline Mode

순차 스테이지 처리. 엄격한 순서가 필요한 다단계 변환에 사용.

- `team-plan → team-prd → team-exec → team-verify → team-fix`를 strict하게 지키고 싶을 때
- 일반적으로 Team 모드가 포함하므로 단독 사용은 드묾

## Ecomode

토큰 효율 모드. 경량 모델로 강제 실행.

```bash
$ecomode
```

- 긴 작업이나 실험 단계에서 비용 절감
- 상태 필드: `active` 하나만

## 실무 선택 가이드

| 상황 | 추천 모드 |
|---|---|
| 여러 에이전트 조율 필요 | Team |
| 아이디어 단계 → 동작 코드 | Autopilot |
| "꼭 끝내야 함" 강박이 있는 작업 | Ralph |
| 독립 태스크 대량 | Ultrawork |
| Codex·Gemini 의견도 듣고 싶음 | CCG |
| 요구사항이 불명확 | Deep Interview |
| 기획 품질이 중요 | Ralplan (`--deliberate`) |
| 비용 절감 | Ecomode |

## 상태 관리 통합

모든 모드는 [[omc-state-management]] 규약을 지킨다:
- 시작 시 `state_write` (active=true)
- 단계 전환 시 `current_phase` 업데이트
- 종료 시 `active=false` + `completed_at`
- 취소 시 `state_clear`

## 관련 문서

- [[oh-my-claudecode]]
- [[omc-autopilot]]
- [[omc-ralph-mode]]
- [[omc-ultrawork]]
- [[omc-team-mode]]
- [[omc-ccg]]
- [[omc-ralplan]]
- [[omc-deep-interview]]
- [[omc-state-management]]

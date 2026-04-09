---
title: OMC State Management
aliases: ["OMC State Management", "State Management"]
category: concepts
page_type: project-internal
project: oh-my-claudecode
tags: [omc, state, notepad, project-memory, compaction, control-plane]
sources: [raw/2026-04-09-omc-ARCHITECTURE.md, raw/2026-04-09-omc-HOOKS.md]
created: 2026-04-09
updated: 2026-04-09
---

# OMC State Management

> `.omc/` 디렉토리 기반 지속 상태 시스템. 컨텍스트 컴팩션을 이겨내고 장기 작업을 재개할 수 있게 한다.

## 왜 중요한가

LLM의 컨텍스트 윈도우는 유한하다. Claude Code는 한계에 가까워지면 **컴팩션(compaction)**을 수행해 이전 대화를 요약한다. 이 과정에서 중요한 작업 상태, 결정, 진행 중인 TODO가 사라질 수 있다. OMC의 상태 관리 시스템은 이를 방지한다:

1. **컴팩션 전** 중요 정보를 파일 시스템에 저장
2. **컴팩션 후** 저장된 정보를 컨텍스트에 재주입
3. **세션 간** 프로젝트 지식을 영속화

## 디렉토리 구조

```
.omc/
├── state/                     # 모드별 상태 파일 (JSON)
│   ├── autopilot-state.json   # autopilot 진행
│   ├── ralph-state.json       # ralph 루프 상태
│   ├── team/                  # 팀 태스크 상태
│   ├── interop/               # 크로스 툴 태스크/메시지 봉투
│   └── sessions/              # 세션별 상태
│       └── {sessionId}/
├── notepad.md                 # 컴팩션 생존 메모
├── project-memory.json        # 프로젝트 지식 저장소
├── plans/                     # 실행 계획
├── notepads/                  # 플랜별 지식 캡처
│   └── {plan-name}/
│       ├── learnings.md
│       ├── decisions.md
│       ├── issues.md
│       └── problems.md
├── prompts/                   # 프롬프트/응답 아티팩트
├── autopilot/                 # autopilot 아티팩트
│   └── spec.md
├── research/                  # 리서치 결과
└── logs/                      # 실행 로그
```

## Control Plane vs Data Plane

OMC는 **오케스트레이션 메타데이터**와 **큰 지속 아티팩트**를 분리한다.

| Plane | 내용 | 위치 |
|---|---|---|
| **Control Plane** | 큐 상태, 워커 할당, 세션 상태, 크로스 툴 태스크 봉투 | `.omc/state/**` |
| **Data Plane** | 플랜, 스펙, 프롬프트, 결과, 트레이스 등 durable 아티팩트 | `.omc/plans/`, `.omc/notepads/`, `.omc/prompts/`, `.omc/state/interop/artifacts/**` |

구체적 핸드오프 예시:
- 공유 interop 상태는 태스크/메시지 메타데이터를 인라인 유지 + 오버사이즈 태스크 설명·결과·메시지 본문은 `.omc/state/interop/artifacts/**`에 저장
- 프롬프트 영속화는 durable 프롬프트/응답 파일을 `.omc/prompts/**`에 저장 + 디스크립터 메타데이터는 job 상태와 함께 기록

**분리의 이점**: 스케줄러와 상태 체크가 가볍게 유지되면서도 풍부한 아티팩트는 durable & inspectable.

## Artifact Descriptors (바운디드 핸드오프)

큰 아티팩트를 참조할 때는 **디스크립터**를 쓴다. Canonical shape:

| Field | 목적 |
|---|---|
| `kind` | 아티팩트 카테고리 (plan, prompt, result, trace 등) |
| `path` | durable 경로 |
| `contentHash?` | 무결성 체크 힌트 |
| `createdAt` | 생성 시각 |
| `producer` | 소유 툴/스킬/워커 |
| `sizeBytes?` | 임계값 판정용 |
| `retention` | 정리/소유 라이프사이클 힌트 |
| `expiresAt?` | 단명 아티팩트 만료 |

**바운디드 핸드오프 규칙**:
1. 작은 페이로드는 인라인 유지
2. control plane 상태를 부풀릴 크기라면 디스크립터 + 짧은 사람-읽기용 요약으로 전환
3. 디스크립터에 소유/retention 메타데이터를 함께 보존 → 추후 정리·감사 결정론 유지

## Notepad 시스템

**파일**: `.omc/notepad.md`

**특징**: 컨텍스트 컴팩션이 일어나도 살아남는다. 컴팩션 후 재주입됨.

**MCP 툴**:

| 툴 | 설명 |
|---|---|
| `notepad_read` | 내용 읽기 |
| `notepad_write_priority` | 최고 우선 메모 (영구 보존) |
| `notepad_write_working` | 작업 진행 메모 |
| `notepad_write_manual` | 수동 메모 |
| `notepad_prune` | 오래된 메모 정리 |
| `notepad_stats` | 상태 확인 |

**동작**:
1. `PreCompact` 이벤트 시 중요 정보를 notepad에 저장
2. 컴팩션 수행
3. 컴팩션 후 notepad 내용이 컨텍스트에 재주입
4. 에이전트는 notepad를 읽어 이전 맥락 회복

## Project Memory

**파일**: `.omc/project-memory.json`

**특징**: 세션 간 영속. 프로젝트 레벨 지식 저장소.

**MCP 툴**:
- `project_memory_read`
- `project_memory_write` (전체 덮어쓰기)
- `project_memory_add_note` (일반 노트 추가)
- `project_memory_add_directive` (지침 추가)

**저장 타입**:
- **Notes**: 프로젝트에 대해 학습한 사실 (아키텍처 패턴, 버그 이력 등)
- **Directives**: 프로젝트 작업 시 따라야 할 지침

**라이프사이클 연동**:
- `SessionStart`: 로드하고 컨텍스트에 주입
- `PostToolUse`: 툴 결과에서 지식 추출해 저장
- `PreCompact`: 컴팩션 전 보존

## Plan Notepad (플랜별 지식 캡처)

**경로**: `.omc/notepads/{plan-name}/`

실행 계획별로 학습을 분리 저장:

| 파일 | 내용 |
|---|---|
| `learnings.md` | 발견 패턴, 성공 접근법 |
| `decisions.md` | 아키텍처 결정 + 근거 |
| `issues.md` | 문제와 블로커 |
| `problems.md` | 기술 부채와 주의사항 |

모든 엔트리는 자동으로 타임스탬프가 붙는다 (ISO 8601).

## Session Scope

**경로**: `.omc/state/sessions/{sessionId}/`

세션별로 상태를 격리 저장. 같은 프로젝트에서 여러 세션이 동시 실행되어도 상태 충돌 없음.

## Centralized State (선택)

기본적으로 상태는 프로젝트의 `.omc/` 디렉토리에 저장되고 worktree가 삭제되면 함께 사라진다. Worktree 삭제에도 상태를 보존하려면:

```bash
# ~/.bashrc 또는 ~/.zshrc
export OMC_STATE_DIR="$HOME/.claude/omc"
```

상태는 `~/.claude/omc/{project-identifier}/`에 저장되며 프로젝트 식별자는 Git remote URL의 해시(로컬 전용 repo는 디렉토리 경로 해시로 대체).

**충돌 시 동작**: 레거시 `{worktree}/.omc/`와 중앙 디렉토리가 모두 존재하면 notice 로그 후 중앙 디렉토리 사용. 수동 마이그레이션 후 레거시 삭제 권장.

## Persistent Memory Tags

중요 정보는 `<remember>` 태그로 표시:

```xml
<!-- 7일 보존 -->
<remember>API endpoint changed to /v2</remember>

<!-- 영구 보존 -->
<remember priority>Never access production DB directly</remember>
```

| 태그 | 보존 기간 |
|---|---|
| `<remember>` | 7일 |
| `<remember priority>` | 영구 |

## Mode Lifecycle Requirements

각 모드는 다음 상태 관리 규약을 지켜야 함:

- **모드 시작**: `state_write`로 `mode`, `active: true`, `started_at`, 모드별 필드 기록
- **단계/이터레이션 전환**: `current_phase`/`iteration` 업데이트
- **완료**: `active: false`, terminal `current_phase`, `completed_at`
- **취소**: `state_clear(mode="<mode>")`

**모드별 권장 필드**:
- `ralph`: `active`, `iteration`, `max_iterations`, `current_phase`, `started_at`, `completed_at`
- `autopilot`: `active`, `current_phase` (`expansion|planning|execution|qa|validation|complete`), `started_at`, `completed_at`
- `ultrawork`: `active`, `reinforcement_count`, `started_at`
- `team`: `active`, `current_phase` (`team-plan|team-prd|team-exec|team-verify|team-fix|complete`), `agent_count`, `team_name`
- `ecomode`: `active`
- `ultraqa`: `active`, `current_phase`, `iteration`, `started_at`, `completed_at`

## MCP State Tools

`omc setup`으로 등록되는 MCP 툴:

**State & Memory**:
- `state_read`, `state_write`, `state_clear`, `state_list_active`, `state_get_status`
- `project_memory_read`, `project_memory_write`, `project_memory_add_note`, `project_memory_add_directive`
- `notepad_read`, `notepad_write_priority`, `notepad_write_working`, `notepad_write_manual`, `notepad_prune`, `notepad_stats`

## 실무 고려사항

- **상태 파일 수동 편집 금지**: JSON 스키마가 변할 수 있음. MCP 툴 경유 권장
- **디스크 공간**: 장기 작업은 `.omc/` 크기 폭증 → 정기 `notepad_prune`
- **다중 세션**: 같은 프로젝트에 여러 Claude Code 세션 열 때 `sessions/{sessionId}/` 격리에 의존
- **Worktree 전환**: `OMC_STATE_DIR` 없이 worktree 삭제하면 진행 중인 작업 증발

## 관련 문서

- [[oh-my-claudecode (OMC)]]
- [[OMC Hook System]]
- [[OMC Execution Modes]]
- [[OMC Autopilot]]

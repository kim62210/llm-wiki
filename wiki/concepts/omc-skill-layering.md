---
title: OMC Skill Layering
aliases: [OMC Skill Layering, Skills]
category: concepts
page_type: project-internal
project: oh-my-claudecode
tags: [omc, [[hermes-agent|skill]]s, composition, layering]
sources: [raw/2026-04-09-omc-ARCHITECTURE.md, raw/2026-04-09-omc-AGENTS.md]
created: 2026-04-09
updated: 2026-04-13
---
# OMC Skill Layering

> 스킬은 에이전트를 교체하는 게 아니라 **행동을 주입(behavior injection)** 한다.

## 핵심 아이디어

OMC의 스킬은 플러그인이 아니라 **오케스트레이터의 행동을 수정하는 레이어**다. 스킬을 활성화하면 기존 에이전트가 그대로 동작하되, 추가 능력(병렬 실행, 지속 루프, 커밋 자동화 등)이 덧씌워진다.

```
[Execution Skill] + [0-N Enhancements] + [Optional Guarantee]
```

## 3-레이어 구조

```
┌─────────────────────────────────────────────────────────────┐
│  GUARANTEE LAYER (optional)                                  │
│  ralph: "Cannot stop until verified done"                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  ENHANCEMENT LAYER (0-N skills)                              │
│  ultrawork (parallel) | git-master (commits) | frontend-ui-ux│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  EXECUTION LAYER (primary skill)                             │
│  default (build) | orchestrate (coordinate) | planner (plan) │
└─────────────────────────────────────────────────────────────┘
```

### Execution Layer (실행 레이어)

필수 레이어. 태스크의 주 실행 방식을 결정:
- `default`: 일반 빌드/구현
- `orchestrate`: 다수 에이전트 조율
- `planner`: 기획 모드

### Enhancement Layer (강화 레이어)

0개 이상 쌓을 수 있는 부가 기능:
- `ultrawork`: 병렬 에이전트 스폰
- `git-master`: 원자적 커밋 자동화
- `frontend-ui-ux`: UI/UX 중심 워크플로우
- 기타 도메인 특화 스킬

### Guarantee Layer (보장 레이어) — 선택

작업 완료 보장 정책. 현재 대표 예시는 `ralph`:
- "검증이 성공할 때까지 중단 금지"
- Stop 이벤트를 가로채고 재진입 유도

## 조합 예시

**사용자 요청**: `"ultrawork: refactor API with proper commits"`

활성화되는 스킬:
- Execution: `default`
- Enhancement: `ultrawork` (병렬) + `git-master` (커밋)
- Guarantee: (없음)

**사용자 요청**: `"ralph: refactor the authentication module"`

- Execution: `default`
- Enhancement: (자동 매칭)
- Guarantee: `ralph` (검증 완료까지 지속)

## 스킬 호출 방법

1. **슬래시 명령**: `/oh-my-claudecode:autopilot ...`
2. **[[omc-magic-keyword]]**: 자연어 키워드가 포함된 메시지
3. **브라우징**: `/skills` 대화형 목록

## 스킬 학습 시스템

OMC는 세션에서 문제 해결 패턴을 **재사용 가능한 스킬로 자동 추출**한다. `/learner` 스킬이 그 역할을 담당.

### 스토리지 스코프

| | Project Scope | User Scope |
|---|---|---|
| 경로 | `.omc/skills/` | `~/.omc/skills/` |
| 공유 대상 | 팀 (버전 관리) | 본인의 모든 프로젝트 |
| 우선순위 | 높음 (user override) | 낮음 (fallback) |

### 스킬 파일 형식

```yaml
---
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
---

Wrap handler at server.py:42 in try/except ClientDisconnectedError...
```

### 자동 주입

매칭되는 triggers가 사용자 프롬프트에서 감지되면 해당 스킬이 컨텍스트에 자동 로드된다. **수동 recall 불필요**.

## 카탈로그 규모

총 **31개+ 스킬** (28개 user-invocable + 3개 internal/pipeline).

### Workflow Skills (핵심)
`autopilot`, `ralph`, `ultrawork`, `team`, `ccg`, `ralplan`, `deep-interview`, `ultraqa`, `plan`, `ai-slop-cleaner`, `visual-verdict`, `web-clone`, `ecomode`

### Utility Skills
`cancel`, `hud`, `omc-setup`, `omc-doctor`, `learner`, `skill`, `trace`, `release`, `deepinit`, `sciomc`, `external-context`, `writer-memory`

### Agent Shortcuts (키워드 트리거)
`analyze` → debugger, `deepsearch` → explore, `tdd` → test-engineer, `build-fix` → debugger, `code-review` → code-reviewer, `security-review` → security-reviewer, `frontend-ui-ux` → designer, `git-master` → git-master

## 관리 명령

```bash
/skill list              # 전체 스킬 보기
/skill add               # 수동 스킬 추가
/skill remove <name>     # 제거
/skill edit <name>       # 편집
/skill search <keyword>  # 검색
```

## 실무 팁

- **스킬은 가볍게 조합하라**: Guarantee 레이어를 너무 자주 쓰면 Stop 훅이 끼어들어 리소스 낭비
- **프로젝트 스코프 우선**: 팀 공유가 필요한 스킬은 `.omc/skills/`에 커밋
- **Trigger 설계**: 너무 일반적 키워드는 false positive 유발
- **Learner 활용**: 수동으로 스킬 작성하지 말고 세션 후 `/learner` 실행

## 관련 문서

- [[oh-my-claudecode]]
- [[omc-magic-keyword]]
- [[omc-execution-modes]]
- [[multi-agent-orchestration]]

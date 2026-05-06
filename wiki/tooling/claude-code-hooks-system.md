---
title: Claude Code Hooks System
category: tooling
page_type: project-internal
project: Claude Code
tags: [tooling, project-internal, claude, code, hooks, system, harness-engineering, async-events, handler-types]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/claude-code-hooks-system.md, raw/hot-topics-sources/2026-04-10/051-claude-code-hooks-reference.md, raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md, raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md, raw/hot-topics-sources/2026-04-10/053-anthropics-claude-code.md, raw/hot-topics-sources/2026-04-10/054-common-workflows.md, raw/2026-05-06-harness-pattern-hook-system.md]
created: 2026-04-10
updated: 2026-05-06
---
# Claude Code Hooks System

Claude Code 내부에서 라이프사이클 이벤트에 사용자 정의 스크립트를 끼워 넣는 `settings.json` 기반 확장 훅. "LLM 대신 결정론적 레일을 깐다"는 harness 철학의 표준 구현 도구다.

## 개요

Claude Code Hooks System은 에이전트 실행의 특정 시점(이벤트)에 사용자 정의 스크립트를 실행할 수 있는 확장 포인트다. `~/.claude/settings.json` 또는 프로젝트의 `.claude/settings.json`에 선언하며, 에이전트의 행동을 LLM 프롬프트가 아니라 **결정론적 코드**로 제어할 수 있다.

## 이벤트 타입

```mermaid
flowchart TD
    Session[세션 시작] --> InstructionsLoaded[InstructionsLoaded]
    InstructionsLoaded --> UserInput[사용자 입력]
    UserInput --> TaskCreated[TaskCreated]
    TaskCreated --> PreToolUse[PreToolUse]
    PreToolUse --> |"BLOCK → 취소"| ModelRetry[모델 재판단]
    PreToolUse --> |"ALLOW"| ToolExec[도구 실행]
    ToolExec --> PostToolUse[PostToolUse]
    PostToolUse --> NextStep[다음 스텝]
    NextStep --> PreToolUse
    NextStep --> |"작업 완료"| StopSession[세션 종료]

    CwdChanged[CwdChanged] -.->|"비동기 이벤트"| AnyPoint[임의 시점]
    FileChanged[FileChanged] -.-> AnyPoint
    PermissionDenied[PermissionDenied] -.-> AnyPoint
```

| 이벤트 | 발생 시점 | 활용 예시 |
|---|---|---|
| `PreToolUse` | 도구 실행 직전 | 위험 명령 차단, input 수정, 로깅 |
| `PostToolUse` | 도구 실행 직후 | 결과 검증, 알림, 부수효과 처리 |
| `InstructionsLoaded` | CLAUDE.md 로드 후 | 환경 변수 주입, 동적 지시 추가 |
| `TaskCreated` | 태스크 생성 시 | 태스크 트래킹, Notion 이슈 생성 |
| `CwdChanged` | 작업 디렉토리 변경 시 | 프로젝트별 설정 자동 로드 |
| `FileChanged` | 파일 수정 감지 시 | 린터 자동 실행, 변경 추적 |
| `PermissionDenied` | 권한 거부 시 | 알림, 대안 제안 |
| `WorktreeCreate` | worktree 생성 시 | 브랜치 준비, 환경 셋업 |
| `WorktreeRemove` | worktree 제거 시 | 정리 스크립트 실행 |

## settings.json 구조

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "if": "input.command.startsWith('rm -rf')",
        "action": "BLOCK",
        "message": "위험한 삭제 명령은 허용되지 않습니다."
      },
      {
        "matcher": "Bash",
        "action": "RUN",
        "command": "echo '[LOG] Bash 도구 호출: {{input.command}}' >> /tmp/agent.log"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "action": "RUN",
        "command": "npx prettier --write {{input.file_path}} 2>/dev/null || true"
      }
    ],
    "TaskCreated": [
      {
        "action": "RUN",
        "command": "~/.claude/hooks/notify-task.sh '{{task.description}}'"
      }
    ]
  }
}
```

## `if` 필드 (Permission Rule 문법)

v2.1.85 이후 `if` 필드로 훅을 조건부 실행할 수 있다. 이 필드는 JavaScript-like 표현식을 평가한다:

```json
{
  "matcher": "Bash",
  "if": "input.command.includes('sudo') || input.command.includes('chmod')",
  "action": "BLOCK"
}
```

## PreToolUse에서 Input 수정

v2.0.10부터 `PreToolUse` 훅이 도구 입력(tool input)을 수정해서 반환할 수 있다. 이를 이용해:

- 경로를 안전한 경로로 리다이렉트
- 명령어에 자동으로 안전 플래그 추가
- 재시도 루프를 결정론적으로 차단

```bash
#!/bin/bash
# PreToolUse 훅: rm 명령을 trash로 대체
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.command')
if echo "$COMMAND" | grep -qE '^rm '; then
  NEW_CMD="${COMMAND/rm /trash }"
  echo "$INPUT" | jq --arg cmd "$NEW_CMD" '.command = $cmd'
else
  echo "$INPUT"
fi
```

## Harness 철학과의 연결

Claude Code Hooks는 [[anthropic-harness-design|Anthropic 하네스 설계]] 철학의 핵심 구현이다:

> "에이전트의 판단에 맡길 것과 결정론적 코드로 제어할 것을 분리한다"

훅이 없으면 모든 제약이 프롬프트에 의존 -> 불안정. 훅을 사용하면 위험 행동을 코드 수준에서 막을 수 있어 안전성과 예측 가능성이 향상된다.

## 실무 활용 예시

1. **Prettier 자동 포맷**: `PostToolUse(Write)` -> 파일 저장 후 자동 포맷
2. **위험 명령 차단**: `PreToolUse(Bash)` -> `rm -rf`, `force push` 등 차단
3. **Notion 이슈 자동 생성**: `TaskCreated` -> 태스크를 Notion에 자동 기록
4. **프로젝트별 환경 자동 로드**: `CwdChanged` -> 해당 프로젝트 `.env` 자동 활성화
5. **작업 완료 알림**: `PostToolUse(Bash)` -> 장시간 명령 완료 시 알림 전송

## 2026년 신규 비동기 이벤트

2026년에 추가된 async event들은 임의 시점(non-blocking)에 발화하며, 외부 변경(파일/설정/디렉토리), 권한 흐름, subagent lifecycle 등을 다룬다.

| 이벤트 | matcher | 활용 |
|--------|---------|------|
| `FileChanged` | literal 파일명 (regex 아님, 예: `.envrc\|.env`) | 감시 파일 변경 추적 |
| `ConfigChange` | `user_settings\|project_settings\|local_settings\|policy_settings\|skills` | 설정 reload 트리거 |
| `CwdChanged` | matcher 없음 | 프로젝트별 환경 자동 로드 |
| `Notification` | `permission_prompt\|idle_prompt\|auth_success\|elicitation_complete` | 알림 처리 |
| `SubagentStart` / `SubagentStop` | agent 종류 (`general-purpose\|Explore\|Plan\|<custom>`) | subagent 추적 |
| `InstructionsLoaded` | 없음 | CLAUDE.md / `.claude/rules/*.md` 로딩 후 동적 지시 |
| `PreCompact` / `PostCompact` | `manual\|auto` | 컨텍스트 압축 직전 상태 보존 |
| `Elicitation` / `ElicitationResult` | 없음 | 사용자 정보 요청 흐름 |
| `WorktreeCreate` / `WorktreeRemove` | 없음 | worktree 라이프사이클 |
| `UserPromptExpansion` | 없음 | 프롬프트 확장 단계 |
| `PermissionRequest` / `PermissionDenied` | 없음 | 권한 흐름 가시화 |
| `TaskCreated` / `TaskCompleted` | 없음 | 태스크 추적 |
| `TeammateIdle` | 없음 | 팀 에이전트 idle 처리 |

자세한 일반 패턴은 [[hook-system-patterns|Hook System Patterns]] 참조.

## 5종 Handler 타입

| 타입 | 설명 |
|------|------|
| `command` | Shell 스크립트 (stdin JSON, exit code + stdout 응답) |
| `http` | HTTP POST (JSON body), `allowedEnvVars`로 env 화이트리스트 |
| `mcp_tool` | 연결된 [[mcp-protocol-deep-dive\|MCP server]]의 tool 호출 |
| `prompt` | LLM에게 yes/no 결정 위임 |
| `agent` | 서브에이전트를 spawn해서 검증 (experimental) |

각 타입별 schema와 예시는 [[hook-system-patterns]]의 Handler 5가지 타입 섹션 참조.

## Permission Decision 4가지

PreToolUse 훅의 `permissionDecision`:
- `allow`: permission prompt 건너뜀
- `deny`: 도구 호출 차단 (Claude에게 메시지)
- `ask`: 사용자에게 컨펌 요청
- `defer`: graceful exit, 나중에 재개 (non-interactive 전용)

## Exit Code 규약

| Code | 의미 | 동작 |
|------|------|------|
| 0 | 성공 | stdout 파싱 후 진행 |
| 2 | 차단 에러 | stderr를 Claude에 전달, 도구 실행 차단 |
| 그 외 | 비차단 에러 | stderr 첫 줄만 transcript에 표시, 진행 |

## 컨텍스트 주입 한도

`additionalContext`, `systemMessage`, plain stdout으로 주입되는 텍스트는 **10K 문자 cap**. 초과 시 파일로 저장되고 preview만 주입된다.

## 환경 변수

- `$CLAUDE_PROJECT_DIR` - 프로젝트 루트
- `${CLAUDE_PLUGIN_ROOT}` - 플러그인 설치 디렉토리
- `${CLAUDE_PLUGIN_DATA}` - 플러그인 persistent data
- `CLAUDE_ENV_FILE` - SessionStart/Setup/CwdChanged/FileChanged에서 환경변수 영속화 path
- `$CLAUDE_CODE_REMOTE` - web 환경에서 "true"

## 대표 자료

- [Claude Code Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [Common workflows (Claude Code)](https://code.claude.com/docs/en/common-workflows)

## 관련 문서

- [[hook-system-patterns]] -- 일반 hook 패턴 (source-agnostic)
- [[claude-agent-loop|Claude Agent Loop]]
- [[anthropic-harness-design|Anthropic Harness Design]]
- [[agent-skills|Agent Skills]]
- [[skill-system-architecture]] -- skill의 hooks 필드와 lifecycle
- [[mcp-authorization|MCP Authorization]]
- [[mcp-protocol-deep-dive]] -- mcp_tool hook 통합
- [[subagent-spawning]] -- SubagentStart/Stop 훅과 연관

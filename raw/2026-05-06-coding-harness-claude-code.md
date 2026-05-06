---
source: Anthropic 공식 문서 + Anthropic Engineering 블로그
url:
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://code.claude.com/docs/en/overview
  - https://code.claude.com/docs/en/sub-agents
  - https://code.claude.com/docs/en/hooks
title: Claude Code / Claude Agent SDK 하네스 아키텍처 디테일
fetched: 2026-05-06
status: pending_ingest
tags: [claude-code, claude-agent-sdk, harness, hooks, subagents, slash-commands, mcp, anthropic]
---

# Claude Code / Claude Agent SDK 하네스

## 한국어 요약 — 핵심 포인트

Anthropic의 공식 자료에 따르면 Claude Code는 단일 CLI 형태가 아니라 **공통 엔진(Claude Code engine) + 멀티 표면(Terminal, VS Code, JetBrains, Desktop, Web, GitHub Action, Slack 등)** 구조다. 사용자의 CLAUDE.md, settings.json, MCP 서버 설정은 모든 표면에서 동일하게 동작한다.

핵심 아키텍처 빌딩 블록:

1. **Agent loop** — Anthropic이 명시적으로 정의: `gather context -> take action -> verify work -> repeat`. Tools가 1순위 빌딩 블록으로 컨텍스트 윈도우에 직접 노출된다.
2. **Tools** — Bash / Read / Edit / Write / Grep / Glob / Task(서브에이전트 호출) 등 native tools와 MCP 외부 도구. Tools가 첫째이고 codebase는 grep/tail로 탐색 가능한 컨텍스트 소스로 취급(file system as context).
3. **Subagents** — 별도 컨텍스트 윈도우, 별도 시스템 프롬프트, 도구 화이트리스트 보유. 결과만 부모 에이전트에 요약 반환. 검색·로그·파일 내용으로 부모 컨텍스트가 오염되는 것을 막는 핵심 메커니즘.
4. **Compaction** — 컨텍스트 한계 도달 시 자동 요약. `/compact` 슬래시 커맨드로 수동 호출도 가능. SDK가 자동으로 처리.
5. **Skills** — `/review-pr`, `/deploy-staging` 같은 재사용 가능 워크플로우를 패키징.
6. **CLAUDE.md + auto memory** — 프로젝트 루트에 두면 매 세션 시작 시 로드. 추가로 빌드 명령, 디버깅 인사이트 등을 자동 기억.
7. **Hooks** — 5가지 핸들러 타입(command/http/mcp_tool/prompt/agent) × 다중 이벤트로 라이프사이클 가로채기.
8. **MCP** — 외부 데이터·도구 통합 표준.

## 1. Core agent loop & tools (Building agents with the Claude Agent SDK)

> "gather context -> take action -> verify work -> repeat."

> "Tools are the primary building blocks of execution for your agent. Tools are prominent in Claude's context window, making them the primary actions Claude will consider when deciding how to complete a task."

Tools는 다음 카테고리로 분류:
- **Custom tools** — 개발자가 정의한 API
- **Bash/scripts** — 일반 목적 컴퓨터 접근
- **Code generation** — 재사용 가능한 컴포저블 출력
- **MCP** — 표준 외부 통합

### Verification 메커니즘 3종
- **Rules-based feedback** — 린팅, 명시적 검증 규칙
- **Visual feedback** — 스크린샷, 렌더링 결과
- **LLM-as-judge** — 보조 모델 평가 (덜 견고함을 명시적으로 인정)

### Context engineering
> "automatically summarizes previous messages when the context limit approaches, so your agent won't run out of context."

> Subagents "use their own isolated context windows, and only send relevant information back to the orchestrator, rather than their full context."

> File system as context: bash 도구로 grep/tail 등을 호출 — "a form of context engineering."

## 2. Claude Code 표면 통합 (Overview)

> "Each surface connects to the same underlying Claude Code engine, so your CLAUDE.md files, settings, and MCP servers work across all of them."

지원 표면:
- Terminal CLI (`curl -fsSL https://claude.ai/install.sh | bash`)
- VS Code, Cursor, JetBrains 플러그인
- Desktop App (macOS/Windows)
- Web (`claude.ai/code`)
- iOS app
- GitHub Actions / GitLab CI
- Slack, Discord, Telegram, iMessage 채널

추가 운영 메커니즘:
- **Routines** — Anthropic 인프라에서 cron으로 실행 (PC가 꺼져 있어도 동작)
- **Desktop scheduled tasks** — 로컬에서 실행
- **`/loop`** — CLI 세션 내 반복 폴링
- **Remote Control** — 모바일/브라우저에서 로컬 세션 조작
- **`claude --teleport`** — Web 세션을 터미널로 가져오기
- **`/desktop`** — 터미널 세션을 Desktop 앱으로 핸드오프

## 3. Subagents 아키텍처 (sub-agents 페이지)

> "Subagents are specialized AI assistants that handle specific types of tasks. Use one when a side task would flood your main conversation with search results, logs, or file contents you won't reference again: the subagent does that work in its own context and returns only the summary."

> "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions."

> "Claude uses each subagent's description to decide when to delegate tasks."

이점:
- **Preserve context** — 탐색·구현을 메인에서 격리
- **Enforce constraints** — 도구 제한
- **Reuse configurations** — 사용자 레벨 정의
- **Specialize behavior** — 도메인 특화 시스템 프롬프트
- **Control costs** — Haiku 같은 빠른 모델로 라우팅

> Note: "If you need multiple agents working in parallel and communicating with each other, see [agent teams] instead. Subagents work within a single session; agent teams coordinate across separate sessions."

## 4. Hooks 아키텍처 (hooks 페이지) — 가장 풍부한 기술 디테일

### 이벤트 카테고리 (3 cadences)

> "Events fall into three cadences: once per session (`SessionStart`, `SessionEnd`), once per turn (`UserPromptSubmit`, `Stop`, `StopFailure`), and on every tool call inside the agentic loop (`PreToolUse`, `PostToolUse`):"

전체 이벤트 목록:
- **Session-level**: `SessionStart`, `SessionEnd`
- **Turn-level**: `UserPromptSubmit`, `UserPromptExpansion`, `Stop`, `StopFailure`
- **Loop-level**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`
- **Subagent**: `SubagentStart`, `SubagentStop`
- **Compaction**: `PreCompact`, `PostCompact`
- **Async**: `Notification`, `FileChanged`, `CwdChanged`, `ConfigChange`

### 설정 파일 위치
| Location | Scope | Shareable |
|---|---|---|
| `~/.claude/settings.json` | All your projects | No, local to your machine |
| `.claude/settings.json` | Single project | Yes, can be committed to the repo |
| `.claude/settings.local.json` | Single project | No, gitignored |

### 3-레벨 nesting 구조
> "1. Choose a hook event to respond to, like `PreToolUse` or `Stop`
> 2. Add a matcher group to filter when it fires, like 'only for the Bash tool'
> 3. Define one or more hook handlers to run when matched"

### 5가지 핸들러 타입
1. `command` — shell command, JSON input via stdin, 결과는 exit code/stdout
2. `http` — HTTP POST에 JSON 전송
3. `mcp_tool` — 연결된 MCP 서버 도구 호출
4. `prompt` — Claude 모델에 single-turn 평가 의뢰
5. `agent` — Read/Grep/Glob 등을 사용하는 서브에이전트 spawn

### 공통 필드
| Field | Required | Description |
|---|---|---|
| `type` | yes | `"command"`, `"http"`, `"mcp_tool"`, `"prompt"`, or `"agent"` |
| `if` | no | Permission rule syntax (`"Bash(git *)"`, `"Edit(*.ts)"`) |
| `timeout` | no | Defaults: 600 for command, 30 for prompt, 60 for agent |
| `statusMessage` | no | 스피너 메시지 |

### Matcher 평가 규칙
| Matcher value | Evaluated as | Example |
|---|---|---|
| `"*"`, `""`, omitted | Match all | 모든 발생 |
| Only letters, digits, `_`, `\|` | Exact / pipe-separated | `Bash`, `Edit\|Write` |
| Other characters | JS regex | `^Notebook` |

MCP 도구 매칭: `mcp__<server>__<tool>` 형식. 서버 전체는 `mcp__memory__.*` (`.*` 필수).

### Decision 제어 (PreToolUse 전용 hookSpecificOutput)

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask|defer",
    "permissionDecisionReason": "My reason here",
    "updatedInput": { "field_to_modify": "new value" },
    "additionalContext": "Current environment: production. Proceed with caution."
  }
}
```

- `allow` — 권한 프롬프트 스킵
- `deny` — 도구 호출 차단
- `ask` — 사용자 확인 요청
- `defer` — graceful exit, 도구는 나중에 재개 가능

다중 hook 우선순위:
> "When multiple PreToolUse hooks return different decisions, precedence is `deny` > `defer` > `ask` > `allow`."

### Exit code 의미
> "Exit 0 means success. Claude Code parses stdout for JSON output fields..."
> "Exit 2 means a blocking error. Claude Code ignores stdout and any JSON in it. Instead, stderr text is fed back to Claude as an error message..."
> "Any other exit code is a non-blocking error for most hook events."

### Block 가능 여부
| Event | Can block? | Exit 2 behavior |
|---|---|---|
| `PreToolUse` | Yes | Blocks the tool call |
| `PermissionRequest` | Yes | Denies the permission |
| `UserPromptSubmit` | Yes | Blocks prompt processing and erases the prompt |
| `Stop` | Yes | Prevents Claude from stopping |
| `SubagentStop` | Yes | Prevents subagent stopping |
| `PostToolUse` | No | Shows stderr to Claude (tool already ran) |
| `PostToolBatch` | Yes | Stops the agentic loop before next model call |
| `PreCompact` | Yes | Blocks compaction |
| `SessionStart`/`SessionEnd` | No | Shows stderr to user only |

### additionalContext 주입
> "The `additionalContext` field passes a string from your hook into Claude's context window. Claude Code wraps the string in a system reminder and inserts it into the conversation at the point where the hook fired."

- `SessionStart`/`Setup`/`SubagentStart`: 대화 시작 전
- `UserPromptSubmit`/`UserPromptExpansion`: 제출 프롬프트와 함께
- `PreToolUse`/`PostToolUse` 등: tool result 옆

### Hook deduplication
> "All matching hooks run in parallel, and identical handlers are deduplicated automatically. Command hooks are deduplicated by command string, and HTTP hooks are deduplicated by URL."

### 출력 캡
> "Hook output injected into context (additionalContext, systemMessage, or plain stdout) is capped at 10,000 characters."

### 실전 예시 (rm 차단)

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "if": "Bash(rm *)",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-rm.sh"
      }]
    }]
  }
}
```

```bash
#!/bin/bash
COMMAND=$(jq -r '.tool_input.command')
if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked by hook"
    }
  }'
else
  exit 0
fi
```

## 5. CLAUDE.md & Auto Memory

> "[`CLAUDE.md`](/en/memory) is a markdown file you add to your project root that Claude Code reads at the start of every session. Use it to set coding standards, architecture decisions, preferred libraries, and review checklists. Claude also builds [auto memory](/en/memory#auto-memory) as it works, saving learnings like build commands and debugging insights across sessions without you writing anything."

## 6. Agent SDK 추상화 (production 관점)

> "For fully custom workflows, the [Agent SDK](/en/agent-sdk/overview) lets you build your own agents powered by Claude Code's tools and capabilities, with full control over orchestration, tool access, and permissions."

CLI 합성성:
> "Claude Code is composable and follows the Unix philosophy. Pipe logs into it, run it in CI, or chain it with other tools"

```bash
tail -200 app.log | claude -p "Slack me if you see any anomalies"
git diff main --name-only | claude -p "review these changed files for security issues"
```

## 7. 엔터프라이즈 통합

- **Provider routing** — Anthropic API, Amazon Bedrock, Microsoft Foundry, Google Vertex AI
- **Permission modes** — `default`, `plan`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` (hook input의 `permission_mode` 필드로 노출)

## 미확인/추가 조사 필요 항목
- 서브에이전트 정의 frontmatter의 정확한 schema (name/description/tools)는 별도 페이지(`/en/sub-agents`) 끝까지 확인 필요. 현재 본 자료는 partial 추출. 더 풍부한 schema는 raw 추가 ingest 시 docs `https://code.claude.com/docs/en/sub-agents` 전체 fetch 권장. [교차검증 필요]
- "agent teams" 메커니즘 (여러 세션 코디네이션) 디테일은 별도 페이지 (`/en/agent-teams`).

## 출처
- https://claude.com/blog/building-agents-with-the-claude-agent-sdk (Anthropic Engineering, Building agents with the Claude Agent SDK)
- https://code.claude.com/docs/en/overview (Claude Code overview)
- https://code.claude.com/docs/en/sub-agents (Create custom subagents)
- https://code.claude.com/docs/en/hooks (Hooks)

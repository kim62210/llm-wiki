---
source: Cline 공식 문서 + DeepWiki + GitHub
url:
  - https://docs.cline.bot/core-workflows/plan-and-act
  - https://docs.cline.bot/getting-started/what-is-cline
  - https://deepwiki.com/cline/cline/3.4-plan-and-act-modes
  - https://github.com/cline/cline
title: Cline 하네스 — Plan/Act 모드, VSCode 확장, StateManager, MCP
fetched: 2026-05-06
status: pending_ingest
tags: [cline, vscode-extension, plan-act-mode, statemanager, mcp, computer-use, claude-dev, browser-tool, approval-workflow]
---

# Cline 하네스 아키텍처

## 한국어 요약 — 핵심 포인트

Cline(구 Claude Dev)은 VS Code, Cursor, JetBrains의 에디터 익스텐션으로 동작하는 코딩 에이전트로, **Plan/Act 모드 분리 + 명시적 사용자 승인 + Zero-trust 아키텍처**를 핵심 차별점으로 한다.

1. **Plan / Act mode** — 단일 토글로 read-only 탐색 모드와 변경/실행 모드를 분리. 컨텍스트는 모드 전환 시 보존. 모드별로 별도 모델 설정 가능 (강한 추론 모델 + 빠른 실행 모델 조합).
2. **StateManager** — `Mode` 타입(`"plan" | "act"`)을 글로벌 상태로 보관. `togglePlanActModeProto` RPC로 전환. Debounced flush로 디스크 저장.
3. **Tool 4종** — Read/write files, Execute terminal commands, Browser automation (Computer Use), MCP integration.
4. **Approval workflow** — 모든 파일 변경 / 명령 실행에 사용자 승인 게이트.
5. **Zero-trust** — 코드가 Cline 서버를 거치지 않고 사용자 API 키로 직접 LLM 호출.
6. **Browser tool** — Claude Sonnet의 Computer Use 능력 활용. 헤드리스 브라우저 launch, click/type/scroll, screenshot/console log 캡처.
7. **`@url` 기능** — URL 가져와 markdown 변환.

## 1. Plan / Act 모드 (docs.cline.bot/core-workflows/plan-and-act)

### Plan mode
> "In this mode, Cline can read your codebase, run searches, and discuss strategy, but cannot modify any files or execute commands."

> "It keeps the conversation focused on understanding and planning, without the distraction of implementation details."

허용 활동:
- 익숙치 않은 코드베이스 탐색
- 아키텍처 결정 토의
- 엣지 케이스 식별
- 구현 전략 작성
- 코드 리뷰

### Act mode
> "Cline retains the full context from your planning session and can now modify files, run commands, and execute your strategy."

### Context 전환
> "The conversation history carries over when you switch modes. Cline remembers everything you discussed in Plan mode, so you don't need to repeat yourself."

> "the planning phase [to build] context that Cline needs to implement changes effectively"

### Per-mode 모델
> "When enabled, switching between Plan and Act mode automatically switches to the configured model for that mode."

설정 흐름:
1. Cline Settings 열기
2. "Use different models for Plan and Act" 활성
3. 각 모드별 모델 선택

→ Plan에 강한 reasoning 모델 (예: Claude Opus, GPT-5), Act에 빠른 실행 모델 (예: Haiku, GPT-4o).

## 2. StateManager 구현 (deepwiki.com/cline/cline)

### Mode 타입
> Mode 타입은 `"plan"` | `"act"` 두 string literal의 union.

> `"plan"`: "read-only exploration and planning"
> `"act"`: "full execution mode" (file writes, shell commands, browser automation)

### 저장 위치
- Reading: `StateManager.get().getGlobalSettingsKey("mode")`
- Writing: `StateManager.get().setGlobalState("mode", modeToSwitchTo)`

> "StateManager employs a debounced flush mechanism to persist state to disk."

### Mode 전환 RPC
> 전환은 `StateService` RPC `togglePlanActModeProto`로 발생. 호출 시 글로벌 `"mode"` 키 업데이트.

> "If a task is actively running, the Controller subsequently rebuilds the task's `ApiHandler` via `buildApiHandler` to apply mode-specific configurations."

### Webview broadcast
> 현재 모드는 `ExtensionState`의 일부로 UI에 broadcast.

> "The UI reflects the change via the updated `ExtensionState` broadcast."

### Per-mode API config
> `planActSeparateModelsSetting` 활성 시 별도 provider 사용:
> - `planModeApiProvider`
> - `actModeApiProvider`

> Webview는 `normalizeApiConfiguration`으로 활성 모드의 provider만 정규화 표시.

### UI state
- ChatTextArea: 모드 토글 색 코드 (plan = `var(--vscode-activityWarningBadge-background)`, act = `var(--vscode-focusBorder)`)
- ChatRow: `plan_mode_respond` vs `act_mode_respond` 메시지 타입 별도 렌더링

### System prompt 동적 생성
> "is dynamically generated based on the active mode"

> Plan mode: `READ_ONLY_TOOLS` (read_file, list_files 등) 만 노출
> Act mode: 전체 도구셋 노출

### 응답 타입 분기
- `plan_mode_respond`
- `act_mode_respond`

→ 모델이 모드별로 적절한 progress update를 줄 수 있도록 응답 schema 자체를 분리.

## 3. 핵심 도구 (docs.cline.bot/getting-started)

### File operations
> "Read and write files - Navigate your codebase, create new files, and make targeted edits."

> "Create and edit files + monitor linter/compiler errors along the way"

### Terminal command execution
> "Run terminal commands - Execute shell commands, run tests, install packages, and debug errors in real-time."

> "Execute commands directly in your terminal and monitor their output"

### Browser automation (Computer Use)
> "Use a browser - Launch a browser to test web apps, capture screenshots, and interact with pages."

> 구현: "Using Claude Sonnet's new Computer Use capability, Cline can launch a browser, click elements, type text, and scroll, capturing screenshots and console logs at each step."

### `@url` web content
> "@url to fetch and convert to markdown"

### MCP integration
> "Connect external tools - Extend capabilities with MCP servers for databases, APIs, and documentation."

자동 MCP 서버 생성 능력:
> "add a tool that fetches Jira tickets" 같은 자연어 요청 → "Cline handles everything, from creating a new MCP server to installing it."

## 4. Approval workflow

> "permission every step of the way"

> "human-in-the-loop GUI to approve every file change and terminal command"

> "You approve every change before it happens"

→ 모든 destructive action(파일 수정, 명령 실행, 브라우저 액션)에 명시적 사용자 승인 게이트. 멀티 에이전트 / 자율 실행이 본격화되어도 Cline은 의도적으로 human-in-loop 디폴트를 유지.

## 5. Zero-trust 아키텍처

> "Zero trust architecture - Your code never touches our servers. Cline runs entirely client-side with your API keys."

→ Cursor와 대조: Cursor는 자체 서버에서 임베딩 처리. Cline은 코드를 자체 인프라로 전혀 보내지 않음.

> "Transparent by default - Watch every file read, every decision considered, every token used."

## 6. 컨텍스트 수집 절차

> "examining file structure & source code ASTs, running regex searches" 후 진행.

→ AST 기반 + regex로 hybrid 컨텍스트 수집. 단순 grep 대비 구조 인식 추가.

## 7. 설치 / 환경

- VS Code Marketplace 익스텐션 (`saoudrizwan.claude-dev`)
- Cursor, JetBrains에도 동일 패키지 지원
- VS Code Cmd/Ctrl+L (sidebar) 또는 Cmd/Ctrl+J (JetBrains)

## 8. 타 도구와 차이

| 항목 | Cline | Claude Code | Cursor | Aider |
|---|---|---|---|---|
| 호스팅 | 100% client-side | Anthropic 서버 일부 | Anysphere 서버 | client-side |
| 모드 분리 | Plan/Act 명시적 | 없음 (단일 loop) | 없음 (Composer + agent) | code/ask/architect |
| 승인 게이트 | 모든 변경 | hooks로 커스텀 | sandbox + 일부 게이트 | git diff 후 commit |
| Browser | Computer Use 통합 | Chrome MCP | 없음 | 없음 |

## 9. 엔터프라이즈 고려사항

- **Zero-trust**가 회사 정책 (자체 코드 외부 노출 불가)에 부합
- **Approval gate**가 감사 추적에 자연스러움
- 그러나 **자동화 / CI 통합**은 약함 (Plan/Act는 인터랙티브 가정)
- **MCP**로 회사 내부 도구 연결 가능

## 출처
- https://docs.cline.bot/core-workflows/plan-and-act (Plan & Act Mode)
- https://docs.cline.bot/getting-started/what-is-cline (What is Cline)
- https://deepwiki.com/cline/cline/3.4-plan-and-act-modes (Plan and Act Modes 구현 상세)
- https://github.com/cline/cline (Cline GitHub)
- https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev (VS Code Marketplace)

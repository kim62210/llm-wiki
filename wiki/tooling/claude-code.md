---
title: Claude Code
aliases: [Claude Code]
category: tooling
page_type: entity
project: Claude Code
tags: [claude-code, anthropic, coding-agent, cli, hooks, subagents, mcp]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md, raw/2026-05-06-coding-harness-claude-code.md]
created: 2026-04-09
updated: 2026-05-06
---
# Claude Code

Anthropic이 제공하는 공식 [[coding-agent]]. Simon Willison이 [[agentic-engineering-guide]] 전반에 걸쳐 가장 많이 레퍼런스하는 도구다.

## 개요

Claude Code는 Claude 모델(대표적으로 Opus 4.6, Sonnet 4.6 등)을 감싼 [[how-coding-agents-work|에이전트 하네스]]. 코드 읽기/쓰기/실행 능력을 갖춘다. 단일 CLI가 아니라 **공통 엔진(Claude Code engine) + 멀티 표면(multi-surface)** 구조로, 사용자의 CLAUDE.md, settings.json, MCP 서버 설정은 모든 표면에서 동일하게 동작한다.

## 하네스 아키텍처 핵심 빌딩 블록

Anthropic 공식 가이드("Building agents with the Claude Agent SDK")에서 명시하는 8가지 빌딩 블록.

```mermaid
flowchart TD
    Loop[Agent loop<br/>gather context -> take action -> verify work -> repeat]
    Loop --> Tools[Tools<br/>Bash/Read/Edit/Write/Grep/Glob/Task]
    Loop --> Sub[Subagents<br/>별도 컨텍스트 윈도우]
    Loop --> Comp[Compaction<br/>자동/수동 요약]
    Loop --> Skills[Skills<br/>슬래시 커맨드 패키지]
    Loop --> Memory[CLAUDE.md + Auto Memory]
    Loop --> Hooks[Hooks<br/>5 핸들러 x 11+ 이벤트]
    Loop --> MCP[[mcp-protocol|MCP]]
```

### 1. Agent loop

Anthropic이 명시적으로 정의한 4단계 사이클:

> "gather context -> take action -> verify work -> repeat."

Tools가 첫째 빌딩 블록. 코드베이스는 grep/tail로 탐색 가능한 컨텍스트 소스로 취급(file system as context). [[claude-agent-loop]] 참고.

### 2. Tools

| 카테고리 | 예시 | 역할 |
|---|---|---|
| Custom tools | 개발자 정의 API | 도메인 특화 |
| Bash/scripts | shell 명령 | 일반 목적 컴퓨터 접근 |
| Code generation | 재사용 가능 컴포저블 출력 | 결과 산출 |
| MCP | 외부 통합 | 표준 외부 도구 |

검증 메커니즘 3종:
- **Rules-based feedback** (린팅, 명시적 검증 규칙)
- **Visual feedback** (스크린샷, 렌더링 결과)
- **LLM-as-judge** (보조 모델 평가, 견고함 부족 인정)

### 3. Subagents

> "Subagents are specialized AI assistants that handle specific types of tasks. Use one when a side task would flood your main conversation with search results, logs, or file contents you won't reference again: the subagent does that work in its own context and returns only the summary."

각 서브에이전트는 (a) 자체 컨텍스트 윈도우, (b) 커스텀 시스템 프롬프트, (c) 특정 도구 액세스, (d) 독립 권한을 보유. 결과만 부모에 요약 반환. [[subagents]] 참고.

### 4. Compaction

> "automatically summarizes previous messages when the context limit approaches, so your agent won't run out of context."

`/compact` 슬래시 커맨드로 수동 호출 가능.

## 배포 형태

Simon Willison의 가이드와 CLI 환경에서 언급되는 형태:

- **Terminal CLI**: 기본 개발자 워크플로우
- **Desktop 앱** (Mac/Windows)
- **Web 앱** (claude.ai/code, "Claude Code for web")
- **IDE 확장** (VS Code, JetBrains)

Simon은 [[linear-walkthroughs]] 사례에서 "Claude Code for web"을 GitHub 저장소 분석에 활용했다.

## Simon의 사용 사례

가이드에 등장하는 대표 활용:

| 사례 | 기법 | 참조 |
|------|------|------|
| SwiftUI 슬라이드 앱 Present를 vibe coded | 즉석 생성 | [[linear-walkthroughs]] |
| GIF 최적화 도구 (Gifsicle→WASM) | 긴 시행착오 컴파일 | [[gif-optimization-case-study]] |
| Word cloud Rust CLI + 애니메이션 설명 | 비동기 연구 + Opus 4.6 | [[interactive-explanations]] |
| 디프 뷰 문자 단위 강조 | Explore subagent | [[subagents]] |

## 주요 기능

가이드에서 암시되거나 명시되는 특징:

### 1. Explore Subagent (기본 패턴)
새 저장소에서 작업 시작 시 자동으로 Explore 서브에이전트를 발사해 코드베이스를 매핑. 부모 에이전트의 컨텍스트 창을 보존. 자세한 것은 [[subagents]] 참조.

### 2. 병렬 서브에이전트
여러 서브에이전트를 동시에 실행 가능. 독립 파일 편집, 대량 탐색, 병렬 리팩토링에 유리.

### 3. 브라우저 자동화 통합
`uvx rodney --help`, `uvx showboat --help` 같은 외부 CLI를 자동 설치·활용 가능. [[agentic-manual-testing]] 참조.

### 4. Git 통합
"Use git bisect to find when this bug was introduced"처럼 자연어 Git 지시를 이해. [[git-with-coding-agents]] 참조.

### 5. 리즈닝 모델 활용
Opus 4.6 같은 reasoning-enabled 모델로 복잡한 디버깅에 유리.

## 효과적 사용 패턴

Simon이 권장하는 세션 시작 패턴:

```
1. First run the tests
2. Use red/green TDD
3. Use subagents where independent work can parallelize
4. Use rodney/playwright for browser testing
5. Write a walkthrough with showboat when done
```

## 대체제

가이드에 언급된 다른 [[coding-agent|코딩 에이전트]]들:
- OpenAI Codex (비동기 작업에 유리)
- Gemini CLI
- Gemini Jules (비동기 리팩토링 워커)

### 6. Claude Code Routines (클라우드 자동화)

2026년 4월 공개. 프롬프트 + 레포지토리 + 커넥터를 패키징하여 Anthropic 관리 클라우드에서 자동 실행하는 기능. 스케줄, API, GitHub 이벤트 트리거를 조합 가능. 노트북을 닫아도 백그라운드에서 동작한다.

활용 예: 야간 백로그 정리, 알림 기반 자동 대응, PR 자동 코드 리뷰, 배포 후 검증, 문서 드리프트 감지.

상세: [[claude-code-routines|Claude Code Routines]]

## 멀티 표면(multi-surface) 통합

> "Each surface connects to the same underlying Claude Code engine, so your CLAUDE.md files, settings, and MCP servers work across all of them."

지원 표면:

- **Terminal CLI** (`curl -fsSL https://claude.ai/install.sh | bash`)
- **VS Code, Cursor, JetBrains** 플러그인
- **Desktop App** (macOS/Windows)
- **Web** (`claude.ai/code`)
- **iOS app**
- **GitHub Actions / GitLab CI**
- **Slack, Discord, Telegram, iMessage** 채널

추가 운영 메커니즘:

- **Routines** - Anthropic 인프라에서 cron 실행 (PC OFF 상태에서도 동작)
- **Desktop scheduled tasks** - 로컬 실행
- **`/loop`** - CLI 세션 내 반복 폴링
- **Remote Control** - 모바일/브라우저에서 로컬 세션 조작
- **`claude --teleport`** - Web 세션을 터미널로 가져오기
- **`/desktop`** - 터미널 세션을 Desktop 앱으로 핸드오프

## Hooks 시스템 (가장 풍부한 기술 디테일)

[[claude-code-hooks-system]]에 깊은 디테일. 핵심 요약:

### 이벤트 카테고리 (3 cadences)

> "Events fall into three cadences: once per session (`SessionStart`, `SessionEnd`), once per turn (`UserPromptSubmit`, `Stop`, `StopFailure`), and on every tool call inside the agentic loop (`PreToolUse`, `PostToolUse`)"

- **Session-level**: `SessionStart`, `SessionEnd`
- **Turn-level**: `UserPromptSubmit`, `UserPromptExpansion`, `Stop`, `StopFailure`
- **Loop-level**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`
- **Subagent**: `SubagentStart`, `SubagentStop`
- **Compaction**: `PreCompact`, `PostCompact`
- **Async**: `Notification`, `FileChanged`, `CwdChanged`, `ConfigChange`

### 5가지 핸들러 타입

| 타입 | 동작 |
|---|---|
| `command` | shell command, JSON input via stdin, exit code/stdout 결과 |
| `http` | HTTP POST에 JSON 전송 |
| `mcp_tool` | 연결된 MCP 서버 도구 호출 |
| `prompt` | Claude 모델에 single-turn 평가 의뢰 |
| `agent` | Read/Grep/Glob 등 사용 서브에이전트 spawn |

### 3-레벨 settings.json 구조

| Location | Scope | Shareable |
|---|---|---|
| `~/.claude/settings.json` | All projects | No, local |
| `.claude/settings.json` | Single project | Yes (committable) |
| `.claude/settings.local.json` | Single project | No, gitignored |

### Decision precedence (PreToolUse)

다중 hook 결과 충돌 시 우선순위:

> "When multiple PreToolUse hooks return different decisions, precedence is `deny` > `defer` > `ask` > `allow`."

- `allow` - 권한 프롬프트 스킵
- `deny` - 도구 호출 차단
- `ask` - 사용자 확인 요청
- `defer` - graceful exit, 도구 나중 재개 가능

### Block 가능 이벤트

| Event | Can block? | Exit 2 behavior |
|---|---|---|
| `PreToolUse` | Yes | Tool call 차단 |
| `PermissionRequest` | Yes | Permission 거부 |
| `UserPromptSubmit` | Yes | Prompt 차단 + erase |
| `Stop` / `SubagentStop` | Yes | 정지 방지 |
| `PostToolBatch` | Yes | 다음 model call 전 loop 중단 |
| `PreCompact` | Yes | Compaction 차단 |
| `PostToolUse` | No | stderr를 Claude에 표시 (이미 실행됨) |
| `SessionStart`/`End` | No | stderr 사용자에만 표시 |

### Hook 출력 캡

> "Hook output injected into context (additionalContext, systemMessage, or plain stdout) is capped at 10,000 characters."

## Permission modes

`default`, `plan`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` (hook input의 `permission_mode` 필드로 노출).

## Provider routing (엔터프라이즈)

Anthropic API, Amazon Bedrock, Microsoft Foundry, Google Vertex AI를 프로바이더로 선택 가능. CLAUDE.md/settings/MCP 설정은 동일하게 유지.

## CLI 합성성 (Unix philosophy)

> "Claude Code is composable and follows the Unix philosophy. Pipe logs into it, run it in CI, or chain it with other tools"

```bash
tail -200 app.log | claude -p "Slack me if you see any anomalies"
git diff main --name-only | claude -p "review these changed files for security issues"
```

## 관련 문서
- [[claude-opus-4-5-release-notes]] -- [[claude-[[coding-agent|agent]]-sdk|Claude]] Opus 4.5 Release Notes
- [[claude-prompts-git-timeline]] -- Claude 시스템 프롬프트를 git 타임라인으로 추적하기
- [[claude-code-vs-codex-comparison]] -- Claude Code vs Codex CLI 실전 비교 (2026-04)

- [[coding-agent]]
- [[how-coding-agents-work]]
- [[subagents]]
- [[first-run-the-tests]]
- [[red-green-tdd]]
- [[agentic-manual-testing]]
- [[git-with-coding-agents]]
- [[agentic-engineering-guide]]
- [[claude-code-routines]] -- 클라우드 기반 자동화 (Routines)
- [[claude-code-hooks-system]] -- Hooks 시스템 상세
- [[anthropic-harness-design]] -- Anthropic harness 디자인 원칙
- [[claude-agent-sdk]] -- Production-grade SDK 추상화
- [[mcp-protocol]] -- MCP 표준
- [[prompt-caching-agentic]] -- Anthropic 프롬프트 캐싱
- [[coding-harness-comparison]] -- 코딩 에이전트 하네스 횡단 비교

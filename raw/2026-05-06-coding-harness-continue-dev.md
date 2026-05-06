---
source: Continue.dev 공식 문서 + GitHub
url:
  - https://docs.continue.dev/customize/overview
  - https://docs.continue.dev/reference
  - https://docs.continue.dev/customize/deep-dives/configuration
  - https://docs.continue.dev/ide-extensions/agent/quick-start
  - https://docs.continue.dev/guides/cli
title: Continue.dev — config.yaml 스키마, model roles, context providers, MCP, Hub vs Local
fetched: 2026-05-06
status: pending_ingest
tags: [continue-dev, config-yaml, model-roles, context-providers, mcp, prompt-files, agent-config, vscode-jetbrains-extension, hub]
---

# Continue.dev 하네스 아키텍처

## 한국어 요약 — 핵심 포인트

Continue.dev는 VS Code / JetBrains 확장으로, "configurability를 정체성으로" 삼은 오픈소스 코딩 에이전트다.

1. **단일 config.yaml** — 모든 에이전트 행동이 한 yaml에서 정의됨. (구 `config.json`은 deprecated)
2. **Model roles 시스템** — 동일 provider의 동일 모델이 chat / autocomplete / embed / rerank / edit / apply / summarize 중 선택된 role만 수행. 디폴트 `[chat, edit, apply, summarize]`. role마다 다른 모델 가능 → 강한 모델은 chat에, 빠른 모델은 autocomplete에.
3. **Context providers** — file, code, codebase, currentFile, terminal, problems, web, search, diff, folder, open, repo-map, http 등 plug-in 가능한 컨텍스트 소스.
4. **Rules** — Agent / Chat / Edit 요청 모두에 prefix concatenation. Hub-hosted (`uses: org/rule-name`) 또는 로컬 파일 (`file://...`) 양쪽 가능.
5. **Prompts/Slash commands** — `/name` 으로 invoke. 각 prompt는 name + description + prompt 본문. MCP "prompts"도 자동으로 슬래시 커맨드화.
6. **MCP servers** — 자체 server 정의(name/command/args/env/cwd) 또는 hub 참조.
7. **Hub vs Local** — Continue Hub로 공유 / 팀 단위 관리. 로컬 yaml과 합성(`mergeBehavior: merge | overwrite`).
8. **CLI** — `cn` 명령으로 헤드리스 실행 가능.

## 1. Configuration locations (deep-dives/configuration)

### User-level
- `~/.continue/config.yaml` (macOS / Linux)
- `%USERPROFILE%\.continue\config.yaml` (Windows)

### Workspace-level
- `.continuerc.json` (프로젝트 루트)

### Programmatic
- `~/.continue/config.ts` — `modifyConfig` export 필수

> "Local user-level configuration is stored and can be edited in your home directory in `config.yaml`"

### Merge behavior
- `merge` (default) — `.continuerc.json`이 `config.json` 위에 적용
- `overwrite` — 모든 top-level property를 overwrite

## 2. Hub vs Local

> 두 방식:
> - **Hub Configs** — Continue.dev 사이트의 Agent selector
> - **Local Configs** — YAML 직접 편집

### 진입점
- VS Code: Cmd/Ctrl+L (sidebar) → Agent selector
- JetBrains: Cmd/Ctrl+J → Agent selector

## 3. config.yaml 스키마 (reference)

### Top-level fields
- `name` — 프로젝트/구성 식별자
- `version` — 구성 버전
- `schema` — 스키마 버전 (예: `v1`)
- `models` — 모델 목록
- `context` — 컨텍스트 provider 목록
- `rules` — 시스템 메시지에 concatenate되는 규칙
- `prompts` — 슬래시 커맨드
- `docs` — 문서 인덱싱
- `mcpServers` — MCP 서버
- `data` — 데이터 소스

## 4. Models 블록 — Roles 시스템

### 필수 properties
- `name` — 구성 내 unique 식별자
- `provider` — service provider (openai, ollama, mistral 등)
- `model` — 구체 모델명 (gpt-4, starcoder 등)

### Roles
> "The `roles` array specifies capabilities: `chat`, `autocomplete`, `embed`, `rerank`, `edit`, `apply`, `summarize`."

> 디폴트: `[chat, edit, apply, summarize]`

→ 한 모델을 여러 role에 동시에 쓰거나, role별 다른 모델을 선택 가능. 예: GPT-5는 chat / Codestral은 autocomplete / VoyageAI는 embed / Cohere reranker는 rerank.

### 추가 옵션
- `capabilities` — autodetection override (`tool_use`, `image_input`)
- `promptTemplates` — role별 커스텀 템플릿
- `chatOptions` — chat / agent / plan 모드별 system message override
- `autocompleteOptions` — debounce delay, token limit, 템플릿

## 5. Context Providers

### 형식
- `provider` — 식별자 (`file`, `code`, `diff`, `http`, `terminal` 등)
- `name` — 표시명 (선택)
- `params` — provider별 파라미터

### 예상 provider 목록 (검색·웹페이지 비공개로 일부만 확인됨; [교차검증 필요])
- `file` — 사용자가 첨부한 파일
- `code` — 선택 코드 블록
- `codebase` — 전체 codebase 검색
- `currentFile` — 활성 에디터 파일
- `terminal` — 터미널 출력
- `problems` — 에디터 진단/에러
- `web` — 웹 검색
- `search` — 정의된 검색
- `diff` — git diff
- `folder` — 폴더 트리
- `open` — 열린 파일들
- `repo-map` — repo 구조
- `http` — 사용자 정의 URL

> "Examples include providers for: file, code, diff, http (with custom URLs), and terminal."

## 6. Rules

### 동작
> "Rules concatenate into system messages across Agent, Chat, and Edit requests."

### 참조 방식
- Hub: `uses: sanity/sanity-opinionated`
- Local: `uses: file://user/Desktop/rules.md`

→ 팀 단위 코딩 표준을 hub에서 공유, 개인 보강은 로컬 파일로.

## 7. Prompts (Slash commands)

### Invocation
> "Prompts invoke with `/` commands."

### 정의
> "Configuration references prompts via hub paths or local files, with required metadata including `name`, `description`, and `prompt` content."

### MCP prompts 통합
> "Continue supports MCP 'prompts' by creating slash commands."

→ MCP 서버에서 prompt를 export하면 자동으로 `/{prompt-name}` 슬래시 커맨드로 노출됨.

### 구 방식 deprecation
> "The slashCommands array is deprecated. For creating custom slash commands, use prompt files instead."

## 8. MCP servers

### 필드
- `name` — 식별자
- `command` — 실행 명령 (필수)
- `args` — 명령 인자 배열 (선택)
- `env` — 환경 변수 맵 (선택)
- `cwd` — 작업 디렉토리 (선택)

→ Claude Code의 `.mcp.json` 형식과 거의 동일. provider 호환성 보장.

## 9. CLI (`cn`)

> Continue CLI: `cn`

- 헤드리스 모드로 agent 실행
- CI / 자동화 통합
- 동일 config.yaml 재사용

## 10. Agent 정의

> "Continue Agents are defined using the config.yaml specification. Agents are composed of models, rules, and tools (MCP servers)."

→ "Agent" = 모델 선택 + rule 셋 + MCP 도구 셋 의 한 묶음. config.yaml 하나가 곧 한 agent의 정의.

## 11. 모드 (Chat / Agent / Plan)

`chatOptions`에서 system message를 모드별로 override 가능. Agent와 Plan은 명시적으로 분리되어 있음 (Cline의 plan/act와 비슷한 결).

## 12. 다른 하네스와 차이 / 강점

| 항목 | Continue.dev | Cline | Aider | Cursor |
|---|---|---|---|---|
| 정체성 | Configurability | Plan/Act + zero-trust | terminal git-native | 자체 모델 + IDE |
| 단일 config | yaml 하나 | settings GUI | CLI flag + yaml | 비공개 |
| Hub 공유 | Continue Hub | 없음 | 없음 | 없음 |
| Multi-role | 명시적 (chat/embed/rerank/edit/apply 분리) | provider 1개 | 1-2 model | 모델 자체 통합 |
| MCP prompts → slash | 자동 | 수동 | 미지원 | 미지원 |
| 오픈소스 | Apache 2.0 | Apache 2.0 | Apache 2.0 | 비공개 |

## 13. 엔터프라이즈 / 프로덕션 관점

- **모델 무관성** — Provider lock-in 없음. 자체 호스팅 OK.
- **Rules hub** — 회사 코딩 표준을 중앙 관리하면서 사용자별 보강 가능.
- **Roles 분리** — chat은 비싼 모델, autocomplete는 저렴한 로컬 모델 → 비용 최적화.
- **MCP 통합** — 회사 내부 도구 (Jira / Confluence / DB) 연결.
- **CLI** — CI에서 자동화 가능.

## 미확인 / 추가 조사 항목
- Continue context-providers 페이지 정확한 URL이 docs 사이트에서 404 / 리디렉션 — 최신 공식 listing은 별도 레퍼런스 fetch 필요. [교차검증 필요]
- Slash commands 페이지도 동일하게 404 발생. (검색 결과만 인용)
- Continue Hub 고유 거버넌스 / RBAC 모델은 별도 페이지에서 확인 필요. [교차검증 필요]

## 출처
- https://docs.continue.dev/customize/overview (Customization Overview)
- https://docs.continue.dev/reference (config.yaml Reference)
- https://docs.continue.dev/customize/deep-dives/configuration (How to Configure Continue)
- https://docs.continue.dev/ide-extensions/agent/quick-start (Agent Quick Start)
- https://docs.continue.dev/guides/cli (Continue CLI)
- https://github.com/continuedev/continue (GitHub)

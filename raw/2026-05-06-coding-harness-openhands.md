---
source: OpenHands 공식 문서 + arXiv 논문 + GitHub
url:
  - https://docs.openhands.dev/openhands/usage/architecture/runtime
  - https://arxiv.org/html/2511.03690v1
  - https://github.com/OpenHands/OpenHands
title: OpenHands 하네스 — EventStream V1 SDK, ConversationState, Workspace 추상화, 보안 모델
fetched: 2026-05-06
status: pending_ingest
tags: [openhands, opendevin, codeact, eventstream, runtime, sandbox, mcp, agent-sdk, all-hands-ai]
---

# OpenHands 하네스 아키텍처

## 한국어 요약 — 핵심 포인트

OpenHands는 All-Hands-AI의 오픈소스(MIT) 자율 SE 에이전트로, 2025년 V1 SDK 출시 이후 **event sourcing pattern + Action–Execution–Observation 분리 + opt-in sandbox** 구조를 굳혔다.

1. **EventStream + ConversationState** — 모든 상호작용은 immutable event로 append-only EventLog에 기록. ConversationState만이 stateful 컴포넌트. Two-path update (state-only vs event-based) + FIFO lock으로 thread-safety.
2. **Action–Execution–Observation** — Tool은 Pydantic Action schema → ToolExecutor → 구조화된 Observation. LLM 입력 검증 + 결과 마샬링이 일관되게 처리됨.
3. **Skills via AgentContext** — `.openhands/skills/`, `.cursorrules`, `agents.md` 등 markdown 호환 포맷 지원. trigger=None(always)이거나 keyword-based conditional activation.
4. **MCP first-class** — JSON Schema → Action 모델 자동 변환, 결과는 Observation. MCPToolDefinition + MCPToolExecutor가 FastMCP MCPClient 위임.
5. **Workspace abstraction** — LocalWorkspace (호스트 직접 실행) vs RemoteWorkspace (DockerWorkspace, APIRemoteWorkspace, Modal, Daytona, E2B). factory pattern으로 동일 코드가 로컬/원격에서 동작.
6. **Opt-in sandbox** — 디폴트는 비격리(MCP 가정 정합). 컨테이너 격리는 명시적 선택.
7. **Persistence** — base_state.json + 개별 event JSON. dual-path로 incremental 저장. 재시작 시 base 로드 + event replay.
8. **Security**: SecurityAnalyzer (low/medium/high/unknown 위험 등급) + ConfirmationPolicy. SecretRegistry로 per-session 자격증명 격리.
9. **CodeAct generalist agent** — 코드 실행으로 모든 액션 표현하는 핵심 패러다임.
10. **결과**: SWE-Bench Verified 72.8%, GAIA 67.9%. 100+ 모델 지원.

## 1. EventStream / V1 아키텍처 (arxiv.org/html/2511.03690v1)

### Event sourcing core
> "At V1's core lies an event-sourcing pattern treating all interactions as immutable events appended to a log."

### Event class hierarchy
- 베이스 `Event`: "immutable structure (ID, timestamp, source) with type-safe serialization"
- `LLMConvertibleEvent`: LLM에 보낼 수 있음
- 내부 events: state management과 control flow, LLM에 노출 X

### ConversationState (단일 stateful 컴포넌트)
- **Mutable metadata**: agent_status, stats, confirmation_policy
- **Append-only EventLog**

> "A FIFO lock ensures thread-safe updates through a two-path pattern: state-only updates for metadata changes, and event-based updates that append to the log."

### Persistence
> "dual-path design—only new events write to disk, avoiding rewrites of large histories"

> "Conversations resume by loading base_state.json and replaying events from the directory, with agents automatically detecting incomplete conversations and continuing from the last processed event."

## 2. Action–Execution–Observation pattern

### 정의
- **Action**: "Specifies the input schema for a tool call. LLM-generated arguments are validated against a Pydantic model before execution."
- **Execution**: `ToolExecutor`. "receives a validated Action and performs the underlying execution."
- **Observation**: "Captures the output of the execution, defining a structured return schema, and converting results (or errors) into a LLM-compatible format."

이 분리로 **타입 안정성 + LLM 호환 마샬링 + 에러 통합**이 일관되게 보장.

## 3. Skills (AgentContext)

### 정의
> "AgentContext centralizes all inputs that shape LLM behavior, including prefixes/suffixes for system/user messages and user-defined Skill objects."

### 정의 방식
> "defined programmatically or loaded from markdown files (e.g., .openhands/skills/, or compatible formats like .cursorrules, agents.md)."

### Trigger 모드
- `trigger=None` — 항상 활성
- Keyword 기반 conditional — user input의 키워드 매칭으로 활성

→ Cursor의 `.cursorrules`, GitHub Copilot의 `agents.md`와 호환. **다른 도구에서 작성한 컨벤션을 직접 재사용**할 수 있는 멀티-에이전트 호환성.

## 4. MCP 통합

> "Their JSON Schemas are automatically translated into Action models, and their results are surfaced as structured Observation."

구현:
- `MCPToolDefinition`
- `MCPToolExecutor` — "delegates execution to FastMCP's MCPClient, which manages server communication and transport details"

> "external MCP tools behave identically to native tools—validated on input, type-safe at runtime, and serialized for LLM consumption."

## 5. Workspace abstraction

### Opt-in sandboxing 철학
> "Sandboxing should be opt-in, not universal. V1 unifies agent and tool execution in a single process by default, aligning with MCP's assumptions."

### 두 가지 워크스페이스 모드

**LocalWorkspace** — "the host filesystem and shell" 직접 사용. 컨테이너 오버헤드 없음.

**RemoteWorkspace** — `DockerWorkspace` 또는 `APIRemoteWorkspace`. 동일 인터페이스, HTTP로 Agent Server에 위임.

> "Each agent instance runs in an independent container with a dedicated file system, environment, and resource. This containerized design simplifies deployment and enables SaaS-style multi-tenancy while preserving workspace isolation."

### Factory pattern
> "When instantiated with a string path or LocalWorkspace, it returns a LocalConversation that executes the full agent loop in-process. When provided a RemoteWorkspace, the same call transparently constructs a RemoteConversation."

## 6. Runtime details (docs.openhands.dev/openhands/usage/architecture/runtime)

### Client-server architecture
- Client: `openhands/runtime/impl/action_execution/action_execution_client.py`
- Runtimes: `openhands/runtime/impl/docker/docker_runtime.py`, `local/local_runtime.py`

### Communication flow
> "communicates with the action execution server over RESTful API, sending actions and receiving observations"

### Build process
1. 사용자 base Docker image
2. OpenHands가 OH Runtime Image 구성 (OpenHands 코드 + runtime client)
3. Container launch

### Container 내부 컴포넌트
- ActionExecutor (코어)
- Bash Shell
- Browser environment
- Plugins (Jupyter Server 등)

### 실행 흐름
> "The action execution server initializes an ActionExecutor inside the container, setting up necessary components like a bash shell and loading any specified plugins."

Path: Backend → EventStream → ActionExecutor → Observation → Backend

### Plugins
- Python class. base `Plugin` 상속. `openhands/runtime/plugins/__init__.py`의 `ALL_PLUGINS`에 등록.

| 플러그인 | 위치 | 기능 |
|---|---|---|
| Jupyter | `openhands/runtime/plugins/jupyter/__init__.py` | Kernel Gateway 통한 IPython cell 실행 |
| VS Code | `openhands/runtime/plugins/vscode/*` | 토큰화된 connection URL 노출 |
| Agent Skills | `openhands/runtime/plugins/agent_skills/*` | 능력 확장 |

> "Plugins are initialized asynchronously when the runtime starts and are accessible to actions"

설정: `Agent.sandbox_plugins: list[PluginRequirement]`

### Volume management
> "OpenHands supports bind mounts and Docker named volumes in SandboxConfig.volumes" — overlay copy-on-write 가능. Overlay 모드는 `SANDBOX_VOLUME_OVERLAYS` env로 활성.

## 7. Agent Server

### REST endpoints
- `POST /conversations`
- `GET /conversations/id`
- WebSocket — 실시간 event 스트리밍

> "When a RemoteConversation starts, it serializes agent configuration—including LLM settings, tools, and context—into JSON and submits it to /conversations. The server reconstructs the agent, launches a local execution loop, and streams structured events back in real time."

## 8. 보안 모델

### SecurityAnalyzer
도구 호출을 위험 등급으로 평가: `low`, `medium`, `high`, `unknown`.

### ConfirmationPolicy
> "whether user approval is required before execution based on the action's details and assessed risk"

> "When approval is required, the agent pauses in a special WAITING_FOR_CONFIRMATION state until the user explicitly approves or rejects the action."

### SecretRegistry
> "secure, late-bound, and remotely manageable credentials"

> "ensures strict per-session isolation. Tools access secrets only at execution time, and all secret values appearing in outputs are masked to prevent leakage."

### Architecture separation
> "This architecture separates risk assessment from enforcement, allowing developers [to] define custom SecurityAnalyzer and ConfirmationPolicy without touching tool executors or core logic."

## 9. 핵심 설계 원칙 (4)

1. **Optional isolation** — Local by default, sandboxed when needed
2. **Stateless by default** — Immutable components; single ConversationState as source of truth
3. **Strict separation of concerns** — 4 modular packages (SDK, Tools, Workspace, Server)
4. **Two-layer composability** — Independent deployment packages + typed component extension

## 10. 결과 / 채택

- **SWE-Bench Verified**: 72.8%
- **GAIA**: 67.9%
- 100+ 언어 모델 지원
- GitHub 72.7k 스타, 9.2k forks
- 사용 기업: TikTok, VMware, Roche, Amazon, Netflix, Mastercard, Red Hat, MongoDB, Apple, NVIDIA, Google
- 배포 옵션:
  - Software Agent SDK (Python)
  - CLI (Claude Code 스타일)
  - Local GUI (REST + React)
  - Cloud Platform (Minimax 무료 / 엔터프라이즈)
  - Self-hosted Kubernetes

## 11. CodeAct paradigm

> "OpenHands includes a strong generalist agent implemented based on the CodeAct architecture, with additions for web browsing and code editing specialists."

> "The CodeAct agent, without any modifications to its system prompt, demonstrates competitive performance across three major task categories: software development, web interaction, and miscellaneous tasks."

CodeAct = 모든 액션을 코드 실행으로 표현 (별도 tool calling 포맷 대신).

## 출처
- https://docs.openhands.dev/openhands/usage/architecture/runtime (Runtime Architecture)
- https://arxiv.org/html/2511.03690v1 (The OpenHands Software Agent SDK paper)
- https://github.com/OpenHands/OpenHands (OpenHands GitHub)
- https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf (ICLR 2025 OpenHands paper)

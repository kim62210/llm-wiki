---
title: OpenHands - 자율 소프트웨어 엔지니어링 에이전트
category: tooling
page_type: entity
project: OpenHands
tags: [autonomous-agent, swe-agent, open-source, coding, github, devin, eventstream, codeact, mcp, all-hands-ai]
sources: [raw/2026-04-14-ai-hot-topics-100.md, raw/2026-05-06-coding-harness-openhands.md]
created: 2026-04-14
updated: 2026-05-06
---

# OpenHands / Devin

## 개요

OpenHands는 All-Hands-AI가 개발한 모델 무관(model-agnostic) 자율 소프트웨어 엔지니어링 에이전트로, MIT 라이선스 기반 오픈소스 프로젝트다. GitHub 스타 70,000개 이상, 기여자 약 490명, $18.8M Series A 펀딩을 확보했으며 2026년 3월 기준 v1.6.0이 최신 버전이다.

실제 GitHub 이슈 해결, 그린필드 앱 구축, 디버깅 등 소프트웨어 엔지니어링의 전 과정을 자동화하는 것을 목표로 한다. 독점 SaaS인 Devin과 경쟁하면서도 오픈소스 자체 호스팅 방식으로 차별화한다. SWE-bench에서 53%+ 해결률로 Devin(~50%)과 동등 이상의 성능을 보이며, 비용 효율성 면에서 우위를 점한다.

## 핵심 특징

### 모델 무관 아키텍처

다양한 언어 모델과 호환되어 태스크 특성에 맞는 최적의 모델을 선택할 수 있다. 작업 단계별로 모델을 전환하는 것도 가능하다.

### 모델별 성능 특성 (OpenHands Index 기준)

| 모델 | 강점 | 특징 |
|------|------|------|
| Claude 4.5 Opus | 종합 1위 | 이슈 해결, 프론트엔드, 테스팅에서 최고. 병렬 도구 사용으로 작업 속도 가장 빠름 |
| GPT 5.2 Codex | 장기 호흡 태스크 | 그린필드 개발에서 유의미하게 높은 성공률 |
| Gemini 3 Flash | 비용 효율 | 코드 기반 작업에 강하나 프론트엔드 작업에서 약세 |
| DeepSeek-v3.2 | 오픈소스 최강 | 그린필드 개발에서 특히 효과적 |

### 샌드박스 실행 환경

모든 작업이 격리된 Docker 컨테이너 내에서 실행된다. 코드 작성, 터미널 명령어 실행, 웹 브라우징, GitHub PR 생성을 수행하며, 모든 행동이 로깅되어 투명성을 확보한다.

### OpenHands Index 벤치마크

회사 자체 벤치마크로 5가지 작업군에서 언어 모델을 평가하며, 벤치마킹 코드 전체가 오픈소스로 공개되어 있다.

| 작업군 | 기반 벤치마크 | 평가 대상 |
|--------|-------------|---------|
| 이슈 해결 | SWE-Bench Verified | 버그 수정, 기능 구현 |
| 그린필드 개발 | commit0 | 처음부터 앱 구축 |
| 프론트엔드 개발 | SWE-Bench Multimodal (verified) | UI/UX 구현 |
| 소프트웨어 테스팅 | SWT-Bench | 테스트 코드 작성 |
| 정보 수집 | GAIA | 코드베이스 탐색, 문서 분석 |

## 기술 상세

### Devin과의 비교

| 기준 | OpenHands | Devin |
|------|----------|-------|
| 라이선스 | MIT (오픈소스) | 독점 SaaS |
| 호스팅 | 자체 호스팅 + 클라우드 | 클라우드 전용 |
| SWE-bench | 53%+ | ~50% |
| 모델 선택 | 멀티 모델 (태스크별 전환 가능) | 고정 |
| 설정 복잡도 | 높음 (Docker 환경 필요) | 낮음 (즉시 사용) |
| 비용 구조 | 인프라 비용 + 모델 API 비용만 | 구독 요금 |
| 투명성 | 모든 행동 로깅, 코드 공개 | 블랙박스 |

### 아키텍처

```mermaid
flowchart TD
    Issue[GitHub Issue] --> Agent[OpenHands Agent]
    Agent --> ModelSelect{모델 선택}
    ModelSelect -->|이슈 해결| Claude[Claude 4.5 Opus]
    ModelSelect -->|그린필드| GPT[GPT 5.2 Codex]
    ModelSelect -->|비용 최적화| Flash[Gemini 3 Flash]
    Claude --> Sandbox[Docker Sandbox]
    GPT --> Sandbox
    Flash --> Sandbox
    Sandbox --> Code[코드 작성]
    Sandbox --> Terminal[터미널 실행]
    Sandbox --> Browser[웹 브라우징]
    Code --> PR[Pull Request]
    Terminal --> PR
    Browser --> PR
    PR --> Log[행동 로그]
```

### 속도 특성

벤치마크 결과, 클로즈드 소스 모델이 오픈소스 모델 대비 실행 속도에서 전반적으로 앞섰다. 이는 독점 추론 최적화(전용 인프라, 양자화 등)가 오픈소스 환경에서 아직 완전히 재현되지 않았기 때문으로 분석된다. Claude 4.5 Opus는 모델 크기에도 불구하고 병렬 도구 사용 능력 덕분에 가장 빠른 작업 완료 시간을 기록했다.

### 경쟁 환경 (자율 코딩 에이전트 2026)

| 에이전트 | 유형 | SWE-bench | 핵심 차별점 |
|----------|------|-----------|-----------|
| OpenHands | 오픈소스 (MIT) | 53%+ | 모델 무관, 자체 호스팅, 최대 커뮤니티 |
| Devin | 독점 SaaS | ~50% | 원클릭 셋업, 관리형 서비스 |
| [[claude-code]] | CLI 에이전트 | - | Anthropic 네이티브, 터미널 우선 |
| Codex CLI | CLI 에이전트 | - | OpenAI 네이티브, Rust 기반 |
| [[augment-intent]] | IDE 통합 | - | git worktree 격리, 자동 검증 |

### GitHub 통합 워크플로

OpenHands는 GitHub App으로 설치하여 이슈에 자동 반응하는 워크플로를 구성할 수 있다. 이슈가 생성되면 에이전트가 자동으로 코드를 분석하고, Docker 샌드박스에서 수정을 시도한 뒤, PR을 생성한다. 이 과정에서 모든 행동(파일 읽기/쓰기, 터미널 명령, 웹 검색)이 투명하게 로깅되어 사람 개발자가 에이전트의 추론 과정을 검토할 수 있다.

### 실무 고려사항

- 자체 호스팅 시 Docker 환경과 충분한 컴퓨팅 리소스 필요
- 모델 API 비용은 태스크 복잡도에 비례하여 증가 -- 간단한 이슈는 Gemini Flash로, 복잡한 이슈는 Claude Opus로 라우팅하는 전략이 비용 효율적
- 프로덕션 배포보다는 개발 보조 도구로 사용하는 것이 현실적
- 벤치마크 결과는 index.openhands.dev에서 실시간 확인 가능
- v1.6.0 기준 GitHub 스타 70K+, 기여자 490명으로 오픈소스 코딩 에이전트 중 최대 커뮤니티

## V1 SDK 아키텍처 (2025-2026)

OpenHands V1 SDK 출시 후 정착된 아키텍처 (arXiv:2511.03690).

### Event sourcing core

> "At V1's core lies an event-sourcing pattern treating all interactions as immutable events appended to a log."

```mermaid
flowchart TD
    User[사용자 입력] --> CS[ConversationState<br/>유일한 stateful 컴포넌트]
    CS --> Meta[Mutable metadata<br/>agent_status, stats, policy]
    CS --> Log[Append-only EventLog]
    Log --> E1[Event 1]
    Log --> E2[Event 2]
    Log --> E3[Event N]
    Lock[FIFO Lock] --> CS
    CS --> Persist[Persistence<br/>base_state.json + 개별 event JSON]
```

### Event 클래스 위계

- 베이스 `Event`: "immutable structure (ID, timestamp, source) with type-safe serialization"
- `LLMConvertibleEvent`: LLM에 전달 가능
- 내부 events: state management과 control flow, LLM 노출 X

### ConversationState (유일한 stateful 컴포넌트)

> "A FIFO lock ensures thread-safe updates through a two-path pattern: state-only updates for metadata changes, and event-based updates that append to the log."

### Persistence

> "dual-path design—only new events write to disk, avoiding rewrites of large histories"

> "Conversations resume by loading base_state.json and replaying events from the directory, with agents automatically detecting incomplete conversations and continuing from the last processed event."

## Action–Execution–Observation 패턴

| 단계 | 역할 |
|---|---|
| **Action** | "Specifies the input schema for a tool call. LLM-generated arguments are validated against a Pydantic model before execution." |
| **Execution** | `ToolExecutor`. "receives a validated Action and performs the underlying execution." |
| **Observation** | "Captures the output of the execution, defining a structured return schema, and converting results (or errors) into a LLM-compatible format." |

이 분리로 **타입 안정성 + LLM 호환 마샬링 + 에러 통합**이 일관되게 보장.

## Skills (AgentContext)

> "AgentContext centralizes all inputs that shape LLM behavior, including prefixes/suffixes for system/user messages and user-defined Skill objects."

### 정의 방식

> "defined programmatically or loaded from markdown files (e.g., .openhands/skills/, or compatible formats like .cursorrules, agents.md)."

### Trigger 모드

- `trigger=None` — 항상 활성
- Keyword 기반 conditional — user input 키워드 매칭으로 활성

→ Cursor의 `.cursorrules`, GitHub Copilot의 `agents.md`와 호환. **다른 도구의 컨벤션을 직접 재사용** 가능.

## MCP 통합 (first-class)

> "Their JSON Schemas are automatically translated into Action models, and their results are surfaced as structured Observation."

구현:

- `MCPToolDefinition`
- `MCPToolExecutor` — "delegates execution to FastMCP's MCPClient, which manages server communication and transport details"

> "external MCP tools behave identically to native tools—validated on input, type-safe at runtime, and serialized for LLM consumption."

## Workspace 추상화

### Opt-in sandboxing 철학

> "Sandboxing should be opt-in, not universal. V1 unifies agent and tool execution in a single process by default, aligning with MCP's assumptions."

### 두 가지 워크스페이스 모드

| 모드 | 동작 |
|---|---|
| **LocalWorkspace** | "the host filesystem and shell" 직접 사용. 컨테이너 오버헤드 없음 |
| **RemoteWorkspace** | `DockerWorkspace`, `APIRemoteWorkspace`, Modal, Daytona, E2B. HTTP로 Agent Server에 위임 |

> "Each agent instance runs in an independent container with a dedicated file system, environment, and resource. This containerized design simplifies deployment and enables SaaS-style multi-tenancy while preserving workspace isolation."

### Factory pattern

> "When instantiated with a string path or LocalWorkspace, it returns a LocalConversation that executes the full agent loop in-process. When provided a RemoteWorkspace, the same call transparently constructs a RemoteConversation."

→ 동일 코드가 로컬/원격에서 동작.

## Runtime details

### Client-server architecture

- Client: `openhands/runtime/impl/action_execution/action_execution_client.py`
- Runtimes: `openhands/runtime/impl/docker/docker_runtime.py`, `local/local_runtime.py`

### 통신

> "communicates with the action execution server over RESTful API, sending actions and receiving observations"

### Container 내부 컴포넌트

- ActionExecutor (코어)
- Bash Shell
- Browser environment
- Plugins (Jupyter Server 등)

| 플러그인 | 위치 | 기능 |
|---|---|---|
| Jupyter | `openhands/runtime/plugins/jupyter/__init__.py` | Kernel Gateway 통한 IPython cell 실행 |
| VS Code | `openhands/runtime/plugins/vscode/*` | 토큰화된 connection URL 노출 |
| Agent Skills | `openhands/runtime/plugins/agent_skills/*` | 능력 확장 |

### Volume management

> "OpenHands supports bind mounts and Docker named volumes in SandboxConfig.volumes" — overlay copy-on-write 가능. Overlay 모드는 `SANDBOX_VOLUME_OVERLAYS` env로 활성화.

## Agent Server REST endpoints

- `POST /conversations`
- `GET /conversations/id`
- WebSocket — 실시간 event 스트리밍

> "When a RemoteConversation starts, it serializes agent configuration—including LLM settings, tools, and context—into JSON and submits it to /conversations. The server reconstructs the agent, launches a local execution loop, and streams structured events back in real time."

## 보안 모델

### SecurityAnalyzer

도구 호출을 위험 등급으로 평가: `low`, `medium`, `high`, `unknown`.

### ConfirmationPolicy

> "whether user approval is required before execution based on the action's details and assessed risk"

> "When approval is required, the agent pauses in a special WAITING_FOR_CONFIRMATION state until the user explicitly approves or rejects the action."

### SecretRegistry

> "secure, late-bound, and remotely manageable credentials"

> "ensures strict per-session isolation. Tools access secrets only at execution time, and all secret values appearing in outputs are masked to prevent leakage."

### 분리 원칙

> "This architecture separates risk assessment from enforcement, allowing developers [to] define custom SecurityAnalyzer and ConfirmationPolicy without touching tool executors or core logic."

## CodeAct paradigm

> "OpenHands includes a strong generalist agent implemented based on the CodeAct architecture, with additions for web browsing and code editing specialists."

> "The CodeAct agent, without any modifications to its system prompt, demonstrates competitive performance across three major task categories: software development, web interaction, and miscellaneous tasks."

CodeAct = **모든 액션을 코드 실행으로 표현** (별도 tool calling 포맷 대신).

## 핵심 설계 원칙 (4)

1. **Optional isolation** — Local by default, sandboxed when needed
2. **Stateless by default** — Immutable components; single ConversationState as source of truth
3. **Strict separation of concerns** — 4 modular packages (SDK, Tools, Workspace, Server)
4. **Two-layer composability** — Independent deployment packages + typed component extension

## 결과

- **SWE-Bench Verified**: 72.8%
- **GAIA**: 67.9%
- 100+ 언어 모델 지원
- GitHub 72.7k 스타, 9.2k forks
- 사용 기업: TikTok, VMware, Roche, Amazon, Netflix, Mastercard, Red Hat, MongoDB, Apple, NVIDIA, Google
- 배포 옵션: Software Agent SDK (Python), CLI, Local GUI (REST + React), Cloud Platform, Self-hosted Kubernetes

## 관련 문서

- [[swe-bench-pro]] -- SWE-bench Pro 벤치마크
- [[swe-bench-ecosystem-2026]] -- SWE-bench 생태계 2026년 현황
- [[ai-code-review-tools]] -- AI 코드 리뷰 도구
- [[how-coding-agents-work]] -- 코딩 에이전트 작동 원리
- [[swe-agent|SWE-agent (Princeton/Stanford)]] -- ACI 연구 산출물
- [[mcp-protocol|MCP]] -- first-class 통합
- [[devin-2-0-release|Devin 2.0]] -- 비교 대상 closed-source 자율 에이전트
- [[coding-harness-comparison|코딩 에이전트 하네스 횡단 비교]]
- [[event-sourcing-pattern]] -- EventStream의 이론적 기반

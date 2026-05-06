---
source: Cursor (Anysphere) 엔지니어링 블로그 + Pragmatic Engineer
url:
  - https://cursor.com/blog/composer
  - https://cursor.com/blog/continually-improving-agent-harness
  - https://cursor.com/blog/agent-sandboxing
  - https://cursor.com/blog/self-driving-codebases
  - https://cursor.com/blog
  - https://newsletter.pragmaticengineer.com/p/cursor
title: Cursor 하네스 아키텍처 — Composer, agent harness, sandbox, self-driving
fetched: 2026-05-06
status: pending_ingest
tags: [cursor, anysphere, composer, harness, sandbox, multi-agent, mixture-of-experts, rl, anyrun, priompt]
---

# Cursor 하네스 아키텍처

## 한국어 요약 — 핵심 포인트

Cursor의 공식 엔지니어링 블로그(2026년 봄 기준)에서 드러나는 하네스 구조는 다음과 같다:

1. **Composer (자체 모델)** — Mixture-of-Experts(MoE) 아키텍처에 RL을 사용해 코딩 태스크에 직접 최적화. MXFP8 MoE 커널 + expert parallelism + hybrid sharded data parallelism으로 저정밀 훈련 가속. PyTorch + Ray 기반 비동기 RL을 수천 NVIDIA GPU에서 실행. 유사 지능 모델 대비 4배 빠름. RL이 도구 사용 효율성과 병렬화를 직접 보상.
2. **Agent harness** — 모델과 코딩 태스크를 잇는 인프라 레이어. system prompt, tool 설명, 컨텍스트 관리, 실행 프레임워크. 새 모델이 들어오면 수 주에 걸쳐 하네스 튜닝. 모델별 도구 포맷이 다름 (OpenAI는 patch-based, Anthropic은 string replacement).
3. **CursorBench** — 자체 평가 스위트. 공개 벤치 + 내부 eval + 온라인 A/B (latency, token efficiency, tool call count로 측정).
4. **Sandbox** — macOS Seatbelt(`sandbox-exec`), Linux Landlock+seccomp, Windows는 WSL2+Linux 샌드박스. 정책은 워크스페이스/`.cursorignore`로부터 런타임 동적 생성.
5. **Self-driving codebases** — 단일 long-horizon agent 대신 root planner → subplanners → workers 계층 구조. "freshness mechanisms"로 컨텍스트 드리프트 방지. 안티프래자일(개별 실패 허용).
6. **Indexing** — Merkle tree 기반 변경 감지로 3분마다 sync. 파일명 obfuscation + 코드 청크 암호화 후 서버에서 임베딩 생성, Turbopuffer 벡터 DB 저장.
7. **Inference infra** — AWS+Azure에서 수만 NVIDIA H100. Anyrun이라는 Rust orchestrator 서비스가 백그라운드 에이전트 launch 담당.
8. **Prompt compilation** — Priompt(오픈소스, JSX 컴포넌트로 priority score 부여, 토큰 초과 시 binary search로 낮은 우선순위 drop).

## 1. Composer 모델 (cursor.com/blog/composer)

### 아키텍처
> "Composer is a mixture-of-experts (MoE) language model supporting long-context generation and understanding."

### Training
> "reinforcement learning (RL) in a diverse range of development environments"

> "MXFP8 MoE kernels with expert parallelism and hybrid sharded data parallelism"

> "faster inference speeds without requiring post-training quantization."

### Tools
- 단순: 파일 읽기/편집
- 고급: "terminal commands and codebase-wide semantic search"

> "running hundreds of thousands of concurrent sandboxed coding environments" — RL을 위해 도구 사용을 학습시키는 데 필요했던 동시 환경 규모

### Multi-agent / Latency
> "generation speed four times faster than similar models."

> RL이 "efficient choices in tool use and to maximize parallelism whenever possible"을 직접 보상.

### Production scaling
> "PyTorch and Ray to power asynchronous reinforcement learning at scale"

> Training scaled "to thousands of NVIDIA GPUs with minimal communication cost"

> VM scheduler rewritten to "support the bursty nature and scale of training runs"

## 2. Agent Harness (continually-improving-agent-harness)

### 정의
> 하네스는 "the foundational infrastructure connecting language models to coding tasks. It encompasses system prompts, tool descriptions, context management, and execution frameworks that enable agents to build software effectively."

### 개발 프로세스 (vision-driven)
> "start with an opinion about what the ideal agent experience should look like"

이후 가설 → 실험 → "quantitative and qualitative signals from evals and real usage"로 반복.

### 새 모델 채택
> "spend weeks customizing our harness to a model's strengths and quirks until the same model inside our specially tuned harness is noticeably faster, smarter, and more efficient."

### 평가
> "public benchmarks alongside our own eval suite, CursorBench, which gives us a fast, standardized read on quality and lets us compare across time."

> "deploy two or more harness variants side by side and A/B test them on real usage" — latency, token efficiency, tool call count로 측정.

### 모델별 tool 포맷 차이
> "OpenAI's models are trained to edit files using a patch-based format, while Anthropic's models are trained on string replacement"

→ 모델별로 선호 포맷을 별도 제공.

### Reliability sprint
> "all tool calls to at least 2 or often 3 9s of reliability" — 99.9% / 99.99% 안정성 달성. 체계적 분류 + 이상치 탐지로 unexpected error를 자릿수 단위로 감소.

### Context rot
누적된 tool call 에러가 후속 결정 품질을 저하시키는 "context rot" 문제를 다루며, 자동화 시스템으로 emerging issue를 surface하고 fix.

## 3. Sandboxing (cursor.com/blog/agent-sandboxing)

### 동기
> "A mistaken agent can delete databases, ship broken code, or leak secrets."

> "Sandboxed agents stop 40% less often than unsandboxed ones, saving users hours of manual review and approval."

### 플랫폼별 구현

**macOS**: Seatbelt (`sandbox-exec`), 2007년 도입 메커니즘 (Chrome도 사용). 워크스페이스 설정/`.cursorignore`로부터 정책 런타임 동적 생성. syscall + 파일·디렉토리 접근 fine-grained 제한.

**Linux**: Landlock + seccomp 조합.
> "Seccomp blocks unsafe syscalls, while Landlock enforces filesystem restrictions, letting us make ignored files completely inaccessible to the sandboxed process."

워크스페이스를 overlay filesystem으로 매핑. 파일 remounting이 가장 느린 컴포넌트.

**Windows**: 네이티브 sandboxing primitive 부족 → WSL2 안에 Linux sandbox 실행.

### 보호 대상
- `.vscode`, `.git/config`, `.cursorignore` 등
- 인터넷 접근은 대부분 approval 필요

### 에이전트 적응
- Shell tool 설명에 sandbox 제약과 권한 상승 요청 방법 추가
- 실패 패턴: 에이전트가 동일 명령 반복 retry → 에러 메시지에 sandbox 위반을 명시적으로 surface하고 권한 escalation 권장

### 배포
> "We now see a third of requests on supported platforms running with the sandbox," — NVIDIA 등 엔터프라이즈 고객 포함.

## 4. Self-driving codebases (cursor.com/blog/self-driving-codebases)

### Vision
약 1,000 commits/hour로 일주일 동안 thousands of agents가 협업해 web browser 프로젝트를 자율 개발하는 실험.

> "These models were not explicitly trained in this way, which suggests it's emergent behavior and possibly the correct way of structuring software projects after all."

### Long-horizon 실패
> "The model lost track of what it was doing, frequently stopped to proclaim success despite being far from it, and got stuck on complex implementation details." (Claude Opus 4.5 기준)

→ 단일 에이전트 long reasoning 대신 role 특화 + 계층 planning.

### Context freshness mechanisms
- Frequent scratchpad rewrites (append 대신 rewrite)
- Automatic summarization at context limits
- Self-reflection reminders in system prompts
- 가정에 대한 challenging 장려

### Anti-fragility
> "As we scale the number of agents running simultaneously, we also increase the probability of failure. Our system needs to withstand individual agents failing, allowing others to recover."

> "a small but stable rate of errors" 허용이 직렬 quality-checking 보다 빠른 수렴.

### 최종 멀티 에이전트 아키텍처
- **Root planner**: 전체 scope 소유, 코드 생성 안 함
- **Subplanners**: 좁은 슬라이스를 재귀적으로 위임
- **Workers**: 독립 실행, handoff submit

> "Workers pick up tasks and are solely responsible for driving them to completion. They're unaware of the larger system."

### Infrastructure
- 분산 시스템보다 단일 큰 Linux VM이 더 효과적
- 동시 컴파일의 disk I/O가 bottleneck

> "project structure, architectural decisions, and developer experience can affect token and commit throughput."

→ copy-on-write, deduplication 같은 storage system 패턴 도입 검토.

## 5. Indexing & 검색 (Pragmatic Engineer 분석)

### 임베딩 파이프라인
- 코드 청크 + 파일명 모두 obfuscation/암호화 후 서버 전송
- 서버: 복호화 → 임베딩 생성 (OpenAI 또는 자체 모델) → Turbopuffer 벡터 DB
- "the server does not store any source code" — 임베딩만 저장, 매칭 후 클라이언트에서 파일 fetch

### Merkle tree sync
> "Every 3 minutes, Cursor does an index sync"

> "Every file gets a hash, based on its contents. The leaves of the tree are files"

> "Every folder gets a hash, based on the hash of its children."

→ 클라이언트 vs 서버 트리 비교로 변경 파일만 재인덱싱.

### Inference 인프라
- "tens of thousands of NVIDIA H100 GPUs" (AWS + Azure)
- "Azure GPUs are solely for inference, not other LLM-related work."
- Anyrun (Rust 작성 orchestrator) — 백그라운드 에이전트 launch 담당

### 스케일
- "1M transactions per second"
- "100x growth in users and load in 12 months"
- DB 마이그레이션: Yugabyte → PostgreSQL (스케일 한계로)
- Monolithic 백엔드 (팀 속도 우선)

### Tab autocomplete
- Sub-second 지연 요구 → 컨텍스트 크기와 응답 속도 간 긴장

## 6. Prompt compilation (Priompt)

> Priompt (open-sourced at github.com/anysphere/priompt) compiles prompts as JSX components where each element has a priority score. When the total context exceeds the model's token budget, lower-priority elements get dropped via binary search.

> Fine-tuned 7B CodeLlama reranker — up to 500,000 tokens per query, blob-storage KV caching로 20x 비용 절감. [교차검증 필요]

## 7. Cursor Engineering 블로그 인덱스 (2026)

| 게시일 | 제목 | 저자 |
|---|---|---|
| Mar 19, 2026 | Introducing Composer 2 | — |
| Mar 27, 2026 | A technical report on Composer 2 | Sasha Rush |
| Mar 26, 2026 | Improving Composer through real-time RL | — |
| Apr 30, 2026 | Continually improving our agent harness | Stefan Heule, Jediah Katz |
| Apr 14, 2026 | Speeding up GPU kernels by 38% with a multi-agent system | Wilson, Sahil, Yuan, Edward |
| Apr 29, 2026 | Build programmatic agents with the Cursor SDK | — |
| Apr 6, 2026 | Better MoE model inference with warp decode | — |
| Mar 11, 2026 | How we compare model quality in Cursor | — |
| Apr 21, 2026 | Keeping the Cursor app stable | Andrew, Kevin |
| — | Implementing a secure sandbox for local agents | — |
| — | Towards self-driving codebases | — |
| — | Dynamic context discovery | — |
| — | Improving Cursor's agent for OpenAI Codex models | — |
| — | Best practices for coding with agents | — |
| — | Expanding our long-running agents research preview | — |
| — | Scaling long-running autonomous coding | — |
| — | Meet the new Cursor (Cursor 3) | — |

## 출처
- https://cursor.com/blog/composer (Composer: Building a fast frontier model with RL)
- https://cursor.com/blog/continually-improving-agent-harness (Continually improving our agent harness)
- https://cursor.com/blog/agent-sandboxing (Implementing a secure sandbox for local agents)
- https://cursor.com/blog/self-driving-codebases (Towards self-driving codebases)
- https://cursor.com/blog (Cursor 엔지니어링 블로그 인덱스)
- https://newsletter.pragmaticengineer.com/p/cursor (Real-world engineering challenges: building Cursor)

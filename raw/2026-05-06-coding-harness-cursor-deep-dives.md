---
source: Cursor 엔지니어링 블로그 (deep dives)
url:
  - https://cursor.com/blog/scaling-agents
  - https://cursor.com/blog/codex-model-harness
  - https://cursor.com/blog/dynamic-context-discovery
title: Cursor 하네스 deep dives — long-running agents, Codex 모델 적응, dynamic context discovery
fetched: 2026-05-06
status: pending_ingest
tags: [cursor, agent-harness, long-running-agents, codex-model, dynamic-context, context-engineering, lazy-loading, judge-agent, planner-worker]
---

# Cursor 하네스 — Deep Dives

## 한국어 요약 — 핵심 포인트

이 raw 파일은 Cursor 엔지니어링 블로그에서 본진 하네스 글(`continually-improving-agent-harness`)에 추가로 long-running 인프라, OpenAI Codex 모델 적응, dynamic context discovery라는 3개 deep-dive 글을 정리한다. 핵심:

1. **Long-running scaling** — 평탄 coordination → hierarchical(Planner-Worker) 전환으로 신뢰성 ↑. integrator 역할 시도는 병목으로 폐기. drift / tunnel vision 방지 위해 주기적 fresh start. judge agent로 cycle 끝에서 progress 평가. GPT-5.2가 long-horizon에 우월.
2. **Codex 모델 harness** — OpenAI Codex 모델은 OpenAI의 frontier model을 agentic coding으로 fine-tune. shell 도구를 그대로 두지 말고 tool로 감싸기. 툴 이름을 shell convention(`rg`)에 맞춤. **reasoning trace 보존이 핵심** — 제거하면 CursorBench 30% 하락.
3. **Dynamic context discovery** — 정적 풀 컨텍스트 대신 lazy-load. MCP 도구도 이름만 노출. 세련된 retrieval 도구로 agent가 직접 fetch. 결과: MCP tool runs에서 **총 agent token 46.9% 감소** + 품질 향상.

## 1. Scaling long-running autonomous coding (cursor.com/blog/scaling-agents)

### 평탄 → 계층 전환
> "Planners continuously explore the codebase and create tasks"

> "Workers pick up tasks and focus entirely on completing them."

→ self-driving codebases 글의 root planner / subplanners / workers 패턴이 이 글에서 더 정착됨.

### 단순화가 곧 신뢰성
> "The best system is often simpler than you'd expect."

Integrator role 시도 폐기:
> "an integrator role for quality control" 시도 → "it created more bottlenecks than it solved."

### Drift / tunnel vision
> "Agents occasionally run for far too long."

> "We still need periodic fresh starts to combat drift and tunnel vision."

→ 매우 긴 task는 단일 에이전트가 끝까지 가지 않고 주기적으로 컨텍스트를 reset하고 다시 plan 생성.

### Judge agent
> "a judge agent" — cycle 끝에서 progress 평가.

→ self-driving 글에서 언급된 anti-fragility를 **judge agent**라는 명시적 컴포넌트로 구현.

### 운영 스케일
> "hundreds of workers run concurrently"
> "over a million lines of code"
> "trillions of tokens"

### 모델별 long-horizon 성능
> "Model choice matters for extremely long-running tasks."

> GPT-5.2가 extended work에 우월.

> "Opus 4.5 tends to stop earlier and take shortcuts when convenient."

→ 단일 모델이 모든 운영 시나리오에 최적이지 않음. 하네스 자체가 모델별 행동 차이를 capability map에 기록하고 라우팅 가능해야 함.

## 2. Codex 모델 하네스 (cursor.com/blog/codex-model-harness)

### Codex 모델 정의
> "OpenAI's Codex models are versions of their latest frontier model, trained specifically for agentic coding."

### Tool 디자인 — shell 컨벤션 정렬
> "made the names and definitions of tools in Cursor closer to their shell equivalents like `rg` (ripgrep)."

> "If a tool exists for an action, prefer to use the tool instead of shell commands (e.g. read_file over `cat`)."

→ 모델이 자연스럽게 도구 호출로 향하게 하기 위해 도구 이름을 shell 명령에 맞춤. 단, 동시에 도구 사용을 명시적으로 지시.

### Reasoning summaries 길이 제한
> "limit reasoning summaries to 1 or 2 sentences, note when discovering new information or initiating a new tactic"

→ reasoning을 막지 않되, agent의 채팅 출력은 짧게 압축.

### Linter 통합
> "After substantive edits, use the read_lints tool to check recently edited files for linter errors"

→ SWE-agent의 ACI lesson(linter on edit)을 반영. 단, Cursor는 별도 도구로 노출.

### Autonomy bias
> 사용자가 implementation을 원한다고 가정하고 "go ahead and actually implement the change"

### Reasoning trace 보존 — 핵심 발견
> Reasoning trace 제거 시 "30% performance drop" on CursorBench

→ Codex 모델은 reasoning trace를 다음 turn 컨텍스트로 받아야 일관성 유지. 제거하면 self-consistency 손상.

### Message ordering
> "managing message ordering to prevent system prompt instructions from contradicting user requests"

## 3. Dynamic context discovery (cursor.com/blog/dynamic-context-discovery)

### 문제
> "providing fewer details up front" 이 agent로 하여금 "pull relevant context on its own"

> "tool calls can dramatically increase the context window"

### Lazy-loading 패턴
> 정적 컨텍스트 최소화. MCP 도구는 "only receive a small bit of static context, including names of the tools."

→ MCP 서버 100개 연결되어도 모든 도구의 schema를 prompt에 넣지 않음. 이름만 노출, agent가 필요시 schema fetch.

### Retrieval 패턴
- 파일 기반 search: `tail`, `grep`, `rg` 파라미터화
- Semantic discovery: "semantic search" — 적절한 skill 검색
- Terminal history: "integrated terminal outputs" 쿼리 (예: "why did my command fail?")

### 결과
> MCP tool runs에서 "reduced total agent tokens by 46.9%"

> 응답 품질도 향상 — "confusing or contradictory information" 제거.

### 구현 메커니즘
- 긴 응답을 truncate하지 않고 accessible 파일로 변환
- MCP 도구를 "one folder per server"로 논리 그룹핑
- 채팅 히스토리를 컨텍스트 요약 시 쿼리 가능 파일로 취급

## 4. 통합 시사 — 하네스 디자인 원칙

이 3개 글에서 도출되는 Cursor의 하네스 design rules:

| 원칙 | 메커니즘 | 출처 글 |
|---|---|---|
| 계층 구조가 평탄 구조보다 신뢰성 ↑ | Planner-Worker, integrator 폐기 | scaling-agents |
| 주기적 fresh start로 drift 방지 | Judge agent + cycle reset | scaling-agents |
| 모델별 최적화 (long-horizon) | GPT-5.2 vs Opus 4.5 routing | scaling-agents |
| Tool 이름을 모델 직관에 맞춤 | shell convention (rg, read_file) | codex-model-harness |
| Reasoning trace 보존 필수 | 제거 시 30% drop | codex-model-harness |
| 정적 컨텍스트 최소화 | MCP 도구 이름만, schema는 lazy fetch | dynamic-context-discovery |
| 출력은 파일로, prompt는 짧게 | truncate 대신 파일화 | dynamic-context-discovery |
| 도구 사용 직접 보상 | 명시적 instruction "prefer tool over shell" | codex-model-harness |
| Linter on edit | `read_lints` 후처리 도구 | codex-model-harness |

## 5. 다른 하네스와 비교 메모

- SWE-agent의 **linter on edit**은 Cursor에서 명시적 도구화 (`read_lints`).
- OpenHands의 **Skills (markdown)**는 Cursor의 dynamic context와 비슷한 lazy-load 철학.
- Devin의 **planner-executor**는 Cursor의 planner-worker와 같은 패턴.
- Claude Code의 **subagent isolation**은 Cursor의 worker isolation과 같은 컨텍스트 보존 메커니즘.

## 출처
- https://cursor.com/blog/scaling-agents (Scaling long-running autonomous coding)
- https://cursor.com/blog/codex-model-harness (Improving Cursor's agent for OpenAI Codex models)
- https://cursor.com/blog/dynamic-context-discovery (Dynamic context discovery)

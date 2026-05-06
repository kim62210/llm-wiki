---
source: blog
url: https://www.anthropic.com/engineering/writing-tools-for-agents
title: Writing effective tools for AI agents - using AI agents
author: Ken Aizawa (with contributions from Barry Zhang, Zachary Witten, Daniel Jiang)
date: 2025-09-11
fetched: 2026-05-06
status: pending_ingest
tags: [agents, tool-design, mcp, evaluation-driven-development, anthropic-engineering]
---

# Writing effective tools for AI agents (Anthropic Engineering)

## 핵심 명제

> "Agents are only as effective as the tools we give them."

기존 소프트웨어는 결정적(deterministic) 시스템에 맞춰 설계됐지만 에이전트는 비결정적(non-deterministic) 시스템이다. 도구도 이에 맞게 설계 패러다임이 달라져야 함.

## 권장 워크플로우 (Evaluation-Driven Development)

3단계 순환:

1. **Build prototypes** - Claude Code + 로컬 MCP 서버
2. **Run comprehensive evaluations** - 실제 작업으로 평가
3. **Iterative refinement** - 에이전트가 결과를 분석하고 도구를 개선

> "holding out test sets ensures you don't overfit to training evaluations."

## 효과적 도구 5대 원칙

### 1. Intentional Tool Selection (의도적 도구 선택)
- 모든 API 엔드포인트를 도구로 만들지 말 것
- "more tools don't always lead to better outcomes"
- 다단계 작업을 통합: `list_users`, `list_events`, `create_event` 대신 `schedule_event` 하나

### 2. Judicious Context Use (신중한 컨텍스트 사용)
- 도구는 "high signal information"만 반환
- UUID, mime type 같은 기술적 식별자를 의미적 라벨(이름, 파일 타입)로 대체
- 모든 가능한 정보가 아니라 컨텍스트 관련성 우선

### 3. Combinable Workflows (조합 가능한 워크플로우)
- 네임스페이싱 신중히
- "prefix- and suffix-based namespacing has non-trivial effects on performance"
- 서비스별로 그룹: `asana_search`, `jira_search`

### 4. Token-Efficient Responses (토큰 효율적 응답)
- 페이지네이션, 필터링, 트런케이션, 범위 선택 with sensible defaults
- **Claude Code restricts responses to 25,000 tokens by default**
- Verbose vs. concise 응답 형식 선택권 제공

### 5. Precise Prompt Engineering (정교한 프롬프트 엔지니어링)
- 도구 설명에 특수 쿼리 형식, 리소스 간 관계, 명확한 파라미터 명명
- "small refinements to tool descriptions can yield dramatic improvements"

## 응답 형식 제어 예시

```typescript
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

- Slack 스레드 detailed 응답: 206 토큰
- Concise 버전: **72 토큰**, 본질 정보는 유지

## 에러 메시지 디자인

**나쁜 예**: `"Error: invalid_parameter"`

**좋은 예**: `"Parameter must be a valid user_id (numeric). Use search_users(name='Jane') first to retrieve IDs, then call with specific user_id values."`

→ 에이전트에게 다음 행동을 알려주는 에러 메시지

## 평가 작업 예시

**좋은 작업** (실제 워크플로우 반영, 다중 도구 호출 필요):
- "Schedule a meeting with Jane next week to discuss our latest Acme Corp project. Attach the notes from our last project planning meeting and reserve a conference room."
- "Customer ID 9182 reported triple-charging. Find all relevant log entries and determine if other customers were affected."

**나쁜 작업** (지나치게 단순):
- "Schedule a meeting with jane@acme.corp next week."
- "Search the payment logs for `purchase_complete`."

## 정량적 결과

내부 평가에서:
- **Slack MCP server**: 인간이 작성한 도구가 Claude 최적화 버전보다 hold-out 테스트셋에서 **낮은 정확도**
- **Asana MCP server**: 같은 패턴 - Claude 주도 최적화가 수동 구현 능가

## 에이전트 행동에 대한 핵심 통찰

> "agents may hallucinate or fail to grasp how to use a tool"

종래의 SW 계약(타입 시그니처 등)으로는 부족. 에이전트는 인지 패턴 - 컨텍스트 한계 - 에 맞춰 도구가 설계되어야 한다. 계산 한계가 아니라 인지 한계가 제약.

## 실무 팁

- 로컬 MCP 서버 연결: `claude mcp add <name> <command> [args...]`
- LLM용 문서: `docs.anthropic.com/llms.txt` 같은 flat llms.txt 파일

## 메모

- 게시일: 2025년 9월 11일
- 핵심 메시지: 도구를 만들 때 사용자(LLM 에이전트)의 인지 모델에 맞춰 디자인하라.
- "agents need tools designed around their cognitive patterns" - 인간 친화적 API ≠ 에이전트 친화적 API

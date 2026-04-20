---
title: Gemini CLI Subagents
category: agents
page_type: project-internal
project: Gemini CLI
tags: [gemini, google, subagents, multi-agent, cli, parallel-agents]
sources: [raw/2026-04-16-gemini-cli-subagents.md]
created: 2026-04-16
updated: 2026-04-16
---

# Gemini CLI Subagents

Google [[coding-agent|Gemini CLI]]에 도입된 [[subagents|서브에이전트]] 아키텍처. 주 에이전트 세션 옆에서 동작하는 전문 에이전트들에게 작업을 위임하는 패턴이다.

## 격리 모델

각 서브에이전트는 독립된 생태계에서 동작한다:

- 별도 컨텍스트 윈도우
- 커스텀 시스템 인스트럭션
- 큐레이팅된 도구 세트
- 독립 MCP 서버 접근

```mermaid
flowchart TD
    User[사용자] --> Main[주 에이전트 Orchestrator]
    Main -->|@frontend| FE[프론트엔드 전문가]
    Main -->|@generalist| GEN[범용 에이전트]
    Main -->|@codebase_investigator| INV[코드베이스 조사]
    FE --> Result1[통합 응답]
    GEN --> Result2[통합 응답]
    INV --> Result3[통합 응답]
    Result1 --> Main
    Result2 --> Main
    Result3 --> Main
```

주 에이전트는 "전략적 오케스트레이터" 역할이며, 서브에이전트의 수십 번의 도구 호출이나 테스트 실행이 하나의 통합 응답으로 압축되어 반환된다.

## 설정

마크다운 파일 + YAML 프론트매터 형식:
- 개인: `~/.gemini/agents`
- 프로젝트: `.gemini/agents`
- 확장 번들: `agents/` 디렉토리

호출 문법: `@agent-name <요청>` (예: `@frontend-specialist Can you review our app?`)
`/agents` 명령으로 등록된 서브에이전트 목록 확인.

## 내장 서브에이전트

| 이름 | 역할 |
|------|------|
| generalist | 범용 태스크 핸들러, 전체 도구 접근 |
| cli_help | Gemini CLI 문서 전문가 |
| codebase_investigator | 아키텍처 매핑 및 버그 분석 |

## 병렬 실행

"Run the frontend-specialist on each package in parallel" 같은 요청으로 동시 실행 가능. 다만 **병렬 코드 편집은 충돌 위험**이 있다:

> "multiple agents editing code at the same time can lead to conflicts and agents overwriting one another."

이는 [[git-worktree-isolation|Git Worktree 격리]] 같은 메커니즘 없이 병렬 편집을 허용하는 경우의 전형적 문제다.

## Claude Code 서브에이전트와 비교

| 측면 | Gemini CLI | Claude Code |
|------|-----------|-------------|
| 호출 문법 | `@agent-name` | `Agent()` 도구 호출 |
| 정의 형식 | 마크다운 + YAML | 내부 서브에이전트 타입 |
| 커스텀 에이전트 | 사용자 정의 가능 | 사전 정의 타입 중심 |
| 병렬 실행 | 지원 (충돌 주의) | 지원 (worktree 격리) |
| MCP 격리 | 에이전트별 독립 | 상속 |
| 컨텍스트 격리 | 완전 분리 | 완전 분리 |

## 관련 문서

- [[subagents]] -- 서브에이전트 일반 개념
- [[orchestrator-worker-pattern]] -- 오케스트레이터-워커 패턴
- [[multi-agent-orchestration]] -- 멀티에이전트 오케스트레이션
- [[git-worktree-isolation]] -- 병렬 에이전트 충돌 방지
- [[google-adk]] -- Google ADK

---
title: Coding Agent
aliases: [coding agent]
category: concepts
page_type: concept
tags: [coding-agent, agent, llm-harness, definition]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-13
---
# Coding Agent

## 정의

**Coding agent**는 코드를 *작성*하고 *실행*할 수 있는 에이전트다. Simon Willison은 이를 [[how-coding-agents-work|LLM을 감싼 하네스(harness)]]로 설명한다.

에이전트의 일반 정의:
> "An agent is software that runs tools in a loop to achieve a goal."

코딩 에이전트의 결정적 특징은 **코드 실행 능력**이다:
> "Without the ability to directly run the code, anything output by an LLM is of limited value."

## 대표 코딩 에이전트

Simon Willison이 [[agentic-engineering-guide]]에서 언급한 예:

| 에이전트 | 제공사 | 비고 |
|----------|--------|------|
| [[claude-code]] | Anthropic | 터미널 CLI, 웹, 데스크탑, IDE |
| OpenAI Codex | OpenAI | 비동기 에이전트 |
| Gemini CLI | Google | |
| Gemini Jules | Google | 비동기 리팩토링 |

## 동작 원리 (요약)

에이전트 루프:
1. LLM에 프롬프트 전송 (시스템 프롬프트 + 대화 이력 + 사용자 메시지)
2. LLM이 도구 호출(tool call)을 반환
3. 하네스가 도구를 실행
4. 결과를 다시 LLM에 피드백
5. 목표 달성까지 반복

대표 도구: `Bash()` (터미널 실행), `Python()` (코드 실행), 파일 읽기/쓰기, 웹 fetch.

상세는 [[how-coding-agents-work]] 참조.

## 컨텍스트 창 한계

LLM은 동시에 처리할 수 있는 토큰 수(컨텍스트 제한)가 있다. Simon은 "지난 2년간 상대적으로 정체"되어 있으며 대략 100만 토큰, 최적 성능은 20만 토큰 아래에서 나온다고 언급한다. 이 한계를 우회하기 위해 [[subagents]] 패턴이 쓰인다.

## 평가 기준

Simon이 암시하는 좋은 코딩 에이전트의 조건:
- 강력한 도구 세트 (bash, 파일 편집, 웹 fetch)
- 서브에이전트 지원 (컨텍스트 보존)
- 코드 실행 결과를 보고 반복하는 능력 ([[agentic-manual-testing]])
- 테스트 지향적 행동 ([[red-green-tdd]], [[first-run-the-tests]])

## 관련 문서
- [[aider]] -- Aider (터미널 AI 페어 프로그래밍 도구)
- [[ai-documentation-generation]] -- AI 문서 생성 자동화 (AI Documentation Generation)
- [[coding-agents-general-agents-paper]] -- 코딩 에이전트는 범용 에이전트가 될 수 있는가?
- [[pydantic-ai-agent-core]] -- Pydantic AI Agent Core Concepts
- [[ai-code-migration]] -- AI 코드 마이그레이션

- [[how-coding-agents-work]]
- [[agentic-engineering]]
- [[anti-patterns]] — 코딩 에이전트 사용 시 흔히 빠지는 안티패턴
- [[subagents]]
- [[claude-code]]
- [[agentic-manual-testing]]
- [[agentic-engineering-guide]]

---
title: Claude Code Hooks System
category: tooling
page_type: project-internal
project: Claude Code
tags: [tooling, project-internal, claude, code, hooks, system, harness-engineering]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/claude-code-hooks-system.md, raw/hot-topics-sources/2026-04-10/051-claude-code-hooks-reference.md, raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md, raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md, raw/hot-topics-sources/2026-04-10/053-anthropics-claude-code.md, raw/hot-topics-sources/2026-04-10/054-common-workflows.md]
created: 2026-04-10
updated: 2026-04-10
---
# Claude Code Hooks System

이 페이지는 Claude Code 내부에서 Claude Code Hooks System이 어떤 역할을 하는지 정리한 프로젝트 스냅샷이다. 핵심 범위는 툴 호출 전후·세션 이벤트에 사용자 정의 스크립트를 끼워 넣는 settings.json 기반 확장 훅이다.

## 정의

툴 호출 전후·세션 이벤트에 사용자 정의 스크립트를 끼워 넣는 settings.json 기반 확장 훅.

## 왜 지금 중요한가

Claude Code v2.1.85 이후 `if` 필드(permission rule 문법)·CwdChanged·FileChanged·InstructionsLoaded·TaskCreated·PermissionDenied 등 신규 이벤트가 쏟아졌고, v2.0.10부터 PreToolUse 훅이 툴 input을 수정해서 재시도 루프를 끊을 수 있게 되면서 "LLM 대신 결정론적 레일을 깐다"는 harness 철학의 표준 구현 도구가 됐다.

## 대표 자료

- [Claude Code Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [Claude Code Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [anthropics/claude-code (GitHub)](https://github.com/anthropics/claude-code)
- [Common workflows (Claude Code)](https://code.claude.com/docs/en/common-workflows)

## 해석 포인트

이 문서는 특정 프로젝트 내부 기능을 다루므로, 일반 개념보다 **현재 제품에서 어떤 역할을 맡는가**가 중요하다. source 분포가 `code.claude.com×4, github.com×1`인 점을 보면, 문서·릴리스·구현 맥락을 함께 읽어야 오해가 줄어든다.

따라서 이 페이지는 '무엇인가'보다 **어디에 끼워 넣어야 하는가**를 기준으로 읽어야 한다. 운영 단계에서는 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성를 중심으로 영향 범위를 추적하는 편이 낫다.

## 2026년 4월 큐레이션 요약

- 정의: 툴 호출 전후·세션 이벤트에 사용자 정의 스크립트를 끼워 넣는 settings.json 기반 확장 훅.
- 왜 중요한가: Claude Code v2.1.85 이후 `if` 필드(permission rule 문법)·CwdChanged·FileChanged·InstructionsLoaded·TaskCreated·PermissionDenied 등 신규 이벤트가 쏟아졌고, v2.0.10부터 PreToolUse 훅이 툴 input을 수정해서 재시도 루프를 끊을 수 있게 되면서 "LLM 대신 결정론적 레일을 깐다"는 harness 철학의 표준 구현 도구가 됐다.
- 직접 수집 원문: 5개
- 주요 도메인: code.claude.com×4, github.com×1

## 프로젝트 맥락

Claude Code Hooks System는 일반 개념이라기보다 특정 제품 내부에서 의미가 생기는 기능 스냅샷이다. 그래서 이 문서는 '정의'보다 **프로젝트 안에서 어떤 문제를 해결하는가**를 중심으로 읽는 편이 맞다.

## 운영 관점

Claude Code v2.1.85 이후 `if` 필드(permission rule 문법)·CwdChanged·FileChanged·InstructionsLoaded·TaskCreated·PermissionDenied 등 신규 이벤트가 쏟아졌고, v2.0.10부터 PreToolUse 훅이 툴 input을 수정해서 재시도 루프를 끊을 수 있게 되면서 "LLM 대신 결정론적 레일을 깐다"는 harness 철학의 표준 구현 도구가 됐다. 이런 유형은 제품 버전 변화에 민감하므로, 이후 심화 작업에서는 changelog / docs / 구현 예시를 함께 추적해야 한다.

## 핵심 포인트

Claude Code Hooks System는 일반 개념이라기보다 특정 프로젝트 내부 기능을 설명하는 문서다. 현재 페이지의 핵심 정의는 이 페이지는 Claude Code 내부에서 Claude Code Hooks System이 어떤 역할을 하는지 정리한 프로젝트 스냅샷이다. 핵심 범위는 툴 호출 전후·세션 이벤트에 사용자 정의 스크립트를 끼워 넣는 settings.json 기반 확장 훅이다.이며, source 5건이 이 기능의 설계 배경과 운영 맥락을 보강한다.

## source로 보면

수집된 source는 code.claude.com×4, github.com×1로 분포한다. 구현 저장소 비중이 높아 실제 사용·통합 관점이 두드러진다.

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/claude-code-hooks-system.md`

### source별 핵심 신호

- **Hooks reference - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/hooks
  - 메모: Hooks are user-defined shell commands, HTTP endpoints, or LLM prompts that execute automatically at specific points in Claude Code’s lifecycle.
- **Changelog - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/changelog
  - 메모: This page is generated from the CHANGELOG.md on GitHub.Run
- **Agent SDK overview - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/agent-sdk/overview
  - 메모: Intercept and control agent behavior with hooks
- **GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub** (`github.com`): https://github.com/anthropics/claude-code
  - 메모: To see all available qualifiers, see our documentation.
- **Common workflows - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/common-workflows
  - 메모: This page covers practical workflows for everyday development: exploring unfamiliar code, debugging, refactoring, writing tests, creating PRs, and managing sessions.


## source 종합 해석

이 페이지는 `Claude Code Hooks System`를 일반 개념이 아니라 **특정 시스템 내부 설계 스냅샷**으로 읽어야 한다.

직접 수집된 source는 Hooks reference - Claude Code Docs, Changelog - Claude Code Docs를 통해 기능 정의와 운영 맥락을 함께 보여준다.

함께 읽을 문서로는 ai-hot-topics-2026-04, mcp-oauth-pkce-authorization, agent-skills가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- project-internal 문서는 일반 원칙으로 일반화하기보다, 현재 프로젝트 스냅샷으로 읽고 버전 변화에 대비해 추적하는 편이 안전하다.
- 운영 시에는 기능 자체보다 권한 경계, 장애 시 fallback, 상위 허브(entity)와의 관계를 같이 점검한다.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[mcp-oauth-pkce-authorization]]
- [[agent-skills]]

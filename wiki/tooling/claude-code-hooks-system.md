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

## 프로젝트 맥락

이 항목은 **Claude Code** 내부 구현 또는 제품 기능을 다루는 문서다. 일반 개념 페이지로 보기보다 특정 프로젝트의 현재 설계와 운영 스냅샷으로 읽는 것이 적절하다.

## 대표 자료

- [Claude Code Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [Claude Code Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [anthropics/claude-code (GitHub)](https://github.com/anthropics/claude-code)
- [Common workflows (Claude Code)](https://code.claude.com/docs/en/common-workflows)

## 2026년 4월 큐레이션 요약

- 정의: 툴 호출 전후·세션 이벤트에 사용자 정의 스크립트를 끼워 넣는 settings.json 기반 확장 훅.
- 왜 중요한가: Claude Code v2.1.85 이후 `if` 필드(permission rule 문법)·CwdChanged·FileChanged·InstructionsLoaded·TaskCreated·PermissionDenied 등 신규 이벤트가 쏟아졌고, v2.0.10부터 PreToolUse 훅이 툴 input을 수정해서 재시도 루프를 끊을 수 있게 되면서 "LLM 대신 결정론적 레일을 깐다"는 harness 철학의 표준 구현 도구가 됐다.
- 직접 수집 원문: 5개
- 주요 도메인: code.claude.com×4, github.com×1

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

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[mcp-oauth-pkce-authorization]]
- [[agent-skills]]

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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: code.claude.com 4건, github.com 1건
- source 조합: 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/claude-code-hooks-system.md`
- [Hooks reference - Claude Code Docs](https://code.claude.com/docs/en/hooks) — `raw/hot-topics-sources/2026-04-10/051-claude-code-hooks-reference.md`
  - 메모: --- title: Hooks reference - Claude Code Docs source_url: https://code.claude.com/docs/en/hooks final_url: https://code.claude.com/docs/en/hooks status: 200 content_type: text/html; charset=utf-8 topics: [Claude Code Hooks System, Git Worktree Isolation for Parallel Coding Agents
- [Changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog) — `raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md`
  - 메모: --- title: Changelog - Claude Code Docs source_url: https://code.claude.com/docs/en/changelog final_url: https://code.claude.com/docs/en/changelog status: 200 content_type: text/html; charset=utf-8 topics: [Claude Code Hooks System, Agent Skills (SKILL.md) Standard, Git Worktree 
- [Agent SDK overview - Claude Code Docs](https://code.claude.com/docs/en/agent-sdk/overview) — `raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md`
  - 메모: --- title: Agent SDK overview - Claude Code Docs source_url: https://code.claude.com/docs/en/agent-sdk/overview final_url: https://code.claude.com/docs/en/agent-sdk/overview status: 200 content_type: text/html; charset=utf-8 topics: [Agent Harnesses for Long-Running Coding Sessio
- [GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub](https://github.com/anthropics/claude-code) — `raw/hot-topics-sources/2026-04-10/053-anthropics-claude-code.md`
  - 메모: --- title: GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language comma
- [Common workflows - Claude Code Docs](https://code.claude.com/docs/en/common-workflows) — `raw/hot-topics-sources/2026-04-10/054-common-workflows.md`
  - 메모: --- title: Common workflows - Claude Code Docs source_url: https://code.claude.com/docs/en/common-workflows final_url: https://code.claude.com/docs/en/common-workflows status: 200 content_type: text/html; charset=utf-8 topics: [Claude Code Hooks System, Subagents & Multi-Agent Or

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[mcp-oauth-pkce-authorization]]
- [[agent-skills]]

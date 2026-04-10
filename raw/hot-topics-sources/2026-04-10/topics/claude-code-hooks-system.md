---
title: Claude Code Hooks System
section: Harness Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Claude Code Hooks System

## 기존 큐레이션 요약

- 정의: 툴 호출 전후·세션 이벤트에 사용자 정의 스크립트를 끼워 넣는 settings.json 기반 확장 훅.
- 왜 중요한가: Claude Code v2.1.85 이후 `if` 필드(permission rule 문법)·CwdChanged·FileChanged·InstructionsLoaded·TaskCreated·PermissionDenied 등 신규 이벤트가 쏟아졌고, v2.0.10부터 PreToolUse 훅이 툴 input을 수정해서 재시도 루프를 끊을 수 있게 되면서 "LLM 대신 결정론적 레일을 깐다"는 harness 철학의 표준 구현 도구가 됐다.

## 개별 원문 수집 스냅샷

### Claude Code Hooks Reference

- URL: https://code.claude.com/docs/en/hooks
- raw snapshot: `raw/hot-topics-sources/2026-04-10/051-claude-code-hooks-reference.md`
- 수집 제목: Hooks reference - Claude Code Docs

Hooks reference - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Reference Hooks reference Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Reference CLI reference Commands Environment variables Tools reference Interactive mode Checkpointing Hooks reference Plugins reference Channels reference On this page Hook lifecycle How a hook resolves Configuration Hook locations Matcher patterns Match MCP tools Hook handler fields Common fields Command hook fields HTTP hook fields Prompt and agent hook fields Reference scripts by path Hooks in skills and agents The /hooks menu Disable or remove

### Claude Code Changelog

- URL: https://code.claude.com/docs/en/changelog
- raw snapshot: `raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md`
- 수집 제목: Changelog - Claude Code Docs

Changelog - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Getting started Changelog Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Getting started Overview Quickstart Changelog Core concepts How Claude Code works Extend Claude Code Explore the .claude directory Explore the context window Use Claude Code Store instructions and memories Permission modes Common workflows Best practices Platforms and integrations Overview Remote Control Claude Code on the web Claude Code on desktop Chrome extension (beta) Computer use (preview) Visual Studio Code JetBrains IDEs Code review & CI/CD Clau

### Claude Code Agent SDK Overview

- URL: https://code.claude.com/docs/en/agent-sdk/overview
- raw snapshot: `raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md`
- 수집 제목: Agent SDK overview - Claude Code Docs

Agent SDK overview - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Agent SDK Agent SDK overview Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Agent SDK Overview Quickstart Core concepts How the agent loop works Use Claude Code features Work with sessions Input and output Streaming Input Handle approvals and user input Stream responses in real-time Get structured output from agents Extend with tools Give Claude custom tools Connect to external tools with MCP Scale to many tools with tool search Subagents in the SDK Customize behavior Modifying system prompts Slash Commands in the S

### anthropics/claude-code (GitHub)

- URL: https://github.com/anthropics/claude-code
- raw snapshot: `raw/hot-topics-sources/2026-04-10/053-anthropics-claude-code.md`
- 수집 제목: GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub

GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as

### Common workflows (Claude Code)

- URL: https://code.claude.com/docs/en/common-workflows
- raw snapshot: `raw/hot-topics-sources/2026-04-10/054-common-workflows.md`
- 수집 제목: Common workflows - Claude Code Docs

Common workflows - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Use Claude Code Common workflows Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Getting started Overview Quickstart Changelog Core concepts How Claude Code works Extend Claude Code Explore the .claude directory Explore the context window Use Claude Code Store instructions and memories Permission modes Common workflows Best practices Platforms and integrations Overview Remote Control Claude Code on the web Claude Code on desktop Chrome extension (beta) Computer use (preview) Visual Studio Code JetBrains IDEs Code revie

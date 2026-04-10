---
title: Git Worktree Isolation for Parallel Coding Agents
section: Harness Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Git Worktree Isolation for Parallel Coding Agents

## 기존 큐레이션 요약

- 정의: 각 에이전트에게 독립된 git worktree를 할당해 파일 충돌 없이 병렬 작업하게 하는 격리 패턴.
- 왜 중요한가: Claude Code가 `--worktree` 플래그·`.claude/worktrees/`·`WorktreeCreate`/`WorktreeRemove` 훅·`isolation: worktree` 서브에이전트 프론트매터를 정식 지원하고, Cursor 3.0도 `/worktree` 명령을 코어로 흡수하면서 "서브에이전트 하나당 worktree 하나" 패턴이 2026년 표준 병렬 실행 방식으로 굳어졌다.

## 개별 원문 수집 스냅샷

### Claude Code Common Workflows — Worktrees

- URL: https://code.claude.com/docs/en/common-workflows
- raw snapshot: `raw/hot-topics-sources/2026-04-10/054-common-workflows.md`
- 수집 제목: Common workflows - Claude Code Docs

Common workflows - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Use Claude Code Common workflows Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Getting started Overview Quickstart Changelog Core concepts How Claude Code works Extend Claude Code Explore the .claude directory Explore the context window Use Claude Code Store instructions and memories Permission modes Common workflows Best practices Platforms and integrations Overview Remote Control Claude Code on the web Claude Code on desktop Chrome extension (beta) Computer use (preview) Visual Studio Code JetBrains IDEs Code revie

### Claude Code Hooks Reference

- URL: https://code.claude.com/docs/en/hooks
- raw snapshot: `raw/hot-topics-sources/2026-04-10/051-claude-code-hooks-reference.md`
- 수집 제목: Hooks reference - Claude Code Docs

Hooks reference - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Reference Hooks reference Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Reference CLI reference Commands Environment variables Tools reference Interactive mode Checkpointing Hooks reference Plugins reference Channels reference On this page Hook lifecycle How a hook resolves Configuration Hook locations Matcher patterns Match MCP tools Hook handler fields Common fields Command hook fields HTTP hook fields Prompt and agent hook fields Reference scripts by path Hooks in skills and agents The /hooks menu Disable or remove

### Create custom subagents (Claude Code)

- URL: https://code.claude.com/docs/en/sub-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/008-create-custom-subagents.md`
- 수집 제목: Create custom subagents - Claude Code Docs

Create custom subagents - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Agents Create custom subagents Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Agents Create custom subagents Run agent teams Tools and plugins Model Context Protocol (MCP) Discover and install prebuilt plugins Create plugins Extend Claude with skills Automation Automate with hooks Push external events to Claude Run prompts on a schedule Programmatic usage Troubleshooting Troubleshooting On this page Built-in subagents Quickstart: create your first subagent Configure subagents Use the /agents command Choose the 

### Cursor 3.0 Changelog

- URL: https://cursor.com/changelog/3-0
- raw snapshot: `raw/hot-topics-sources/2026-04-10/057-cursor-3-0-changelog.md`
- 수집 제목: New Cursor Interface · Cursor

New Cursor Interface · Cursor Skip to content Cursor Product↓ Agents Code Review Cloud ↗ Tab CLI Marketplace ↗ Enterprise Pricing Resources↓ Changelog Blog Docs Community Help ↗ Workshops Forum ↗ Careers Product → Enterprise Pricing Resources → Sign inContactContact salesDownload 3.0Apr 2, 2026 · Changelog Changelog New Cursor Interface Cursor 3 is now available. #Agents Window The new Cursor interface allows you to run many agents in parallel across repos and environments: locally, in worktrees, in the cloud, and on remote SSH. It's simpler, more powerful, and centered around agents, while keeping the depth of a development environment. To try the Agents Window, upgrade Cursor and type Cmd+Shift+P -> Agents Window . You can switch back to the IDE anytime, or have both open simultaneously.

### Claude Code Changelog

- URL: https://code.claude.com/docs/en/changelog
- raw snapshot: `raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md`
- 수집 제목: Changelog - Claude Code Docs

Changelog - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Getting started Changelog Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Getting started Overview Quickstart Changelog Core concepts How Claude Code works Extend Claude Code Explore the .claude directory Explore the context window Use Claude Code Store instructions and memories Permission modes Common workflows Best practices Platforms and integrations Overview Remote Control Claude Code on the web Claude Code on desktop Chrome extension (beta) Computer use (preview) Visual Studio Code JetBrains IDEs Code review & CI/CD Clau

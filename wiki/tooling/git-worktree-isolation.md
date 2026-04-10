---
title: Git Worktree Isolation for Parallel Coding Agents
category: tooling
page_type: concept
tags: [tooling, concept, git, worktree, isolation]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Git Worktree Isolation for Parallel Coding Agents

각 에이전트에게 독립된 git worktree를 할당해 파일 충돌 없이 병렬 작업하게 하는 격리 패턴.

## 왜 중요한가

Claude Code가 `--worktree` 플래그·`.claude/worktrees/`·`WorktreeCreate`/`WorktreeRemove` 훅·`isolation: worktree` 서브에이전트 프론트매터를 정식 지원하고, Cursor 3.0도 `/worktree` 명령을 코어로 흡수하면서 "서브에이전트 하나당 worktree 하나" 패턴이 2026년 표준 병렬 실행 방식으로 굳어졌다.

## 대표 레퍼런스

- [Claude Code Common Workflows — Worktrees](https://code.claude.com/docs/en/common-workflows)
- [Claude Code Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Create custom subagents (Claude Code)](https://code.claude.com/docs/en/sub-agents)
- [Cursor 3.0 Changelog](https://cursor.com/changelog/3-0)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[cursor-cloud-agents-and-parallel-worktree-agents|Cursor Cloud Agents & Parallel Worktree Agents]]
- [[microvm-agent-sandboxes|Firecracker/microVM Sandboxes for Agent Code Execution]]

---
title: Firecracker/microVM Sandboxes for Agent Code Execution
category: tooling
page_type: concept
tags: [tooling, concept, microvm, agent, sandboxes]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/microvm-agent-sandboxes.md, raw/hot-topics-sources/2026-04-10/062-e2b-documentation.md, raw/hot-topics-sources/2026-04-10/063-e2b-homepage.md, raw/hot-topics-sources/2026-04-10/064-e2b-dev-e2b.md, raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md, raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md]
created: 2026-04-10
updated: 2026-04-10
---
# Firecracker/microVM Sandboxes for Agent Code Execution

Linux 컨테이너의 공유 커널 대신 KVM 기반 microVM으로 에이전트 생성 코드를 격리 실행하는 방식.

## 왜 중요한가

2026년 들어 E2B가 자신의 샌드박스가 Firecracker microVM(≈125-150ms 부팅) 위에서 돈다고 공식화했고, Claude Code v2.1.98은 Linux에서 PID namespace 서브프로세스 sandboxing과 `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`를 추가하면서 "LLM 생성 코드 = 적대적 입력"이라는 하이퍼스케일러 컨센서스가 일반 개발자 환경까지 내려왔다.

## 대표 레퍼런스

- [E2B Documentation](https://e2b.dev/docs)
- [E2B Homepage](https://e2b.dev/)
- [e2b-dev/E2B (GitHub)](https://github.com/e2b-dev/E2B)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/microvm-agent-sandboxes.md`
- raw source: `raw/hot-topics-sources/2026-04-10/062-e2b-documentation.md`
- raw source: `raw/hot-topics-sources/2026-04-10/063-e2b-homepage.md`
- raw source: `raw/hot-topics-sources/2026-04-10/064-e2b-dev-e2b.md`
- raw source: `raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md`
- raw source: `raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md`

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[git-worktree-isolation|Git Worktree Isolation for Parallel Coding Agents]]
- [[tool-contracts-for-agents|Tool Contracts & Writing Tools for Agents]]

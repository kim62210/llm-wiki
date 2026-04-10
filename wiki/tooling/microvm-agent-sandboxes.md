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

- 수집 소스 수: 5
- 상위 도메인: e2b.dev 2건, github.com 1건, code.claude.com 1건
- source 조합: 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/microvm-agent-sandboxes.md`
- [Documentation - E2B](https://e2b.dev/docs) — `raw/hot-topics-sources/2026-04-10/062-e2b-documentation.md`
  - 메모: --- title: Documentation - E2B source_url: https://e2b.dev/docs final_url: https://e2b.dev/docs status: 200 content_type: text/html; charset=utf-8 topics: [Firecracker/microVM Sandboxes for Agent Code Execution] sections: [Harness Engineering] fetched_at: 2026-04-10T01:43:33.4266
- [E2B | The Enterprise AI Agent Cloud](https://e2b.dev) — `raw/hot-topics-sources/2026-04-10/063-e2b-homepage.md`
  - 메모: --- title: E2B | The Enterprise AI Agent Cloud source_url: https://e2b.dev final_url: https://e2b.dev status: 200 content_type: text/html; charset=utf-8 topics: [Firecracker/microVM Sandboxes for Agent Code Execution] sections: [Harness Engineering] fetched_at: 2026-04-10T01:43:3
- [GitHub - e2b-dev/E2B: Open-source, secure environment with real-world tools for enterprise-grade agents. · GitHub](https://github.com/e2b-dev/E2B) — `raw/hot-topics-sources/2026-04-10/064-e2b-dev-e2b.md`
  - 메모: --- title: GitHub - e2b-dev/E2B: Open-source, secure environment with real-world tools for enterprise-grade agents. · GitHub source_url: https://github.com/e2b-dev/E2B final_url: https://github.com/e2b-dev/E2B status: 200 content_type: text/html; charset=utf-8 topics: [Firecracke
- [Changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog) — `raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md`
  - 메모: --- title: Changelog - Claude Code Docs source_url: https://code.claude.com/docs/en/changelog final_url: https://code.claude.com/docs/en/changelog status: 200 content_type: text/html; charset=utf-8 topics: [Claude Code Hooks System, Agent Skills (SKILL.md) Standard, Git Worktree 
- [Scaling Managed Agents: Decoupling the brain from the hands \ Anthropic](https://www.anthropic.com/engineering/managed-agents) — `raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md`
  - 메모: --- title: Scaling Managed Agents: Decoupling the brain from the hands \ Anthropic source_url: https://www.anthropic.com/engineering/managed-agents final_url: https://www.anthropic.com/engineering/managed-agents status: 200 content_type: text/html; charset=utf-8 topics: [Agent Ha

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[git-worktree-isolation|Git Worktree Isolation for Parallel Coding Agents]]
- [[tool-contracts-for-agents|Tool Contracts & Writing Tools for Agents]]

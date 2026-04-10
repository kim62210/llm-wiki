---
title: Agent Skills
category: agents
page_type: concept
tags: [agents, concept, agent, skills]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/agent-skills.md, raw/hot-topics-sources/2026-04-10/021-equipping-agents-for-the-real-world-with-agent-skills.md, raw/hot-topics-sources/2026-04-10/022-agent-skills-specification.md, raw/hot-topics-sources/2026-04-10/023-anthropics-skills-github-repository.md, raw/hot-topics-sources/2026-04-10/024-agent-skills.md, raw/hot-topics-sources/2026-04-10/025-writing-effective-tools-for-agents.md, raw/hot-topics-sources/2026-04-10/055-extend-claude-with-skills.md, raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md, raw/hot-topics-sources/2026-04-10/056-discover-and-install-plugins-through-marketplaces.md, raw/hot-topics-sources/2026-04-10/043-claude-agent-sdk-overview.md]
created: 2026-04-10
updated: 2026-04-10
---
# Agent Skills

에이전트가 파일시스템에 저장된 SKILL.md 폴더를 메타데이터 → 본문 → 리소스 3단계로 점진적 로딩하는 능력 패키징 표준. 또한 SKILL.md 프론트매터와 참고 파일·스크립트 번들로 에이전트 역량을 모듈화하는 오픈 표준.

## 왜 중요한가

2025년 10월 Anthropic이 "Equipping agents for the real world with Agent Skills"로 공개한 후 12월 오픈 스펙으로 표준화되었고, 2026년 들어 OpenAI Codex CLI/ChatGPT, Microsoft Copilot, VS Code 등이 동일 포맷을 채택하면서 사실상 산업 표준 컨텍스트 패키징 형식이 되었다.

Claude Code가 `.claude/commands/`와 슬래시 커맨드를 `.claude/skills/`로 합병하면서 agentskills.io 오픈 표준이 공식화됐고, `disable-model-invocation`·`paths`·`context: fork`·`${CLAUDE_SKILL_DIR}` 같은 세밀한 제어 필드가 2026년 초 추가되며 여러 코딩 에이전트에 공통 포맷으로 퍼지기 시작했다.

## 대표 레퍼런스

- [Equipping agents for the real world with Agent Skills](https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills)
- [Agent Skills Specification](https://agentskills.io/specification)
- [anthropics/skills GitHub Repository](https://github.com/anthropics/skills)
- [Agent Skills (Claude API Docs)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Writing effective tools for agents (Anthropic)](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [anthropics/skills (GitHub)](https://github.com/anthropics/skills)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [Discover and install plugins through marketplaces](https://code.claude.com/docs/en/discover-plugins)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)

## 2026년 4월 큐레이션 요약

- 정의: SKILL.md 프론트매터와 참고 파일·스크립트 번들로 에이전트 역량을 모듈화하는 오픈 표준.
- 왜 중요한가: Claude Code가 `.claude/commands/`와 슬래시 커맨드를 `.claude/skills/`로 합병하면서 agentskills.io 오픈 표준이 공식화됐고, `disable-model-invocation`·`paths`·`context: fork`·`${CLAUDE_SKILL_DIR}` 같은 세밀한 제어 필드가 2026년 초 추가되며 여러 코딩 에이전트에 공통 포맷으로 퍼지기 시작했다.
- 직접 수집 원문: 9개
- 주요 도메인: code.claude.com×4, claude.com×1, agentskills.io×1, github.com×1, platform.claude.com×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/agent-skills.md`

### source별 핵심 신호

- **Equipping agents for the real world with Agent Skills \ Anthropic | Claude** (`claude.com`): https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills
  - 메모: Equipping agents for the real world with Agent Skills
- **Specification - Agent Skills** (`agentskills.io`): https://agentskills.io/specification
  - 메모: Agent Skills now has an official Discord server. See the announcement for details.
- **GitHub - anthropics/skills: Public repository for Agent Skills · GitHub** (`github.com`): https://github.com/anthropics/skills
  - 메모: To see all available qualifiers, see our documentation.
- **Agent Skills - Claude API Docs** (`platform.claude.com`): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
  - 메모: Context windowsCompactionContext editingPrompt cachingToken counting
- **Writing effective tools for AI agents—using AI agents \ Anthropic** (`anthropic.com`): https://www.anthropic.com/engineering/writing-tools-for-agents
  - 메모: Agents are only as effective as the tools we give them. We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself.
- **Extend Claude with skills - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/skills
  - 메모: Claude Code skills follow the Agent Skills open standard, which works across multiple AI tools.
- **Changelog - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/changelog
  - 메모: This page is generated from the CHANGELOG.md on GitHub.Run
- **Discover and install prebuilt plugins through marketplaces - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/discover-plugins
  - 메모: This registers the catalog with Claude Code so you can browse what’s available. No plugins are installed yet.
- **Agent SDK overview - Claude Code Docs** (`code.claude.com`): https://code.claude.com/docs/en/agent-sdk/overview
  - 메모: Intercept and control agent behavior with hooks

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[agent-memory-systems|Agent Memory Systems (Episodic / Semantic / Working)]]
- [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents (Multi-Turn RLVR)]]
- [[subagents|Subagents]]

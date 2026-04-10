---
title: Agent Security: Lethal Trifecta & Prompt Injection Defense
section: Agent Architecture
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Agent Security: Lethal Trifecta & Prompt Injection Defense

## 기존 큐레이션 요약

- 정의: 사적 데이터 접근 + 신뢰할 수 없는 콘텐츠 노출 + 외부 통신이 결합될 때 발생하는 에이전트의 구조적 취약성과 그 방어 패턴.
- 왜 중요한가: Simon Willison이 명명한 "lethal trifecta" 개념이 2026년 1월 IBM Bob, Superhuman AI, Notion AI, Claude Cowork 등 4개 주요 에이전트 제품에서 5일 만에 잇따라 실증되며 보안 위기가 폭발했고, 3월에는 Palo Alto Unit 42가 in-the-wild 인다이렉트 프롬프트 인젝션을 정식 보고하면서 에이전트 아키텍처 설계 시 보안이 1차 고려사항으로 격상되었다.

## 개별 원문 수집 스냅샷

### The lethal trifecta for AI agents (Simon Willison)

- URL: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta
- raw snapshot: `raw/hot-topics-sources/2026-04-10/038-the-lethal-trifecta-for-ai-agents.md`
- 수집 제목: The lethal trifecta for AI agents: private data, untrusted content, and external communication

The lethal trifecta for AI agents: private data, untrusted content, and external communication Simon Willison’s Weblog Subscribe Sponsored by:WorkOS — Production-ready APIs for auth and access control, so you can ship faster. The lethal trifecta for AI agents: private data, untrusted content, and external communication 16th June 2025 If you are a user of LLM systems that use tools (you can call them “AI agents” if you like) it is critically important that you understand the risk of combining tools with the following three characteristics. Failing to understand this can let an attacker steal your data. The lethal trifecta of capabilities is: Access to your private data—one of the most common purposes of tools in the first place! Exposure to untrusted content—any mechanism by which text (or 

### Writing about Agentic Engineering Patterns (Simon Willison)

- URL: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns
- raw snapshot: `raw/hot-topics-sources/2026-04-10/039-writing-about-agentic-engineering-patterns.md`
- 수집 제목: Writing about Agentic Engineering Patterns

Writing about Agentic Engineering Patterns Simon Willison’s Weblog Subscribe Sponsored by:WorkOS — Production-ready APIs for auth and access control, so you can ship faster. Writing about Agentic Engineering Patterns 23rd February 2026 I’ve started a new project to collect and document Agentic Engineering Patterns—coding practices and patterns to help get the best results out of this new era of coding agent development we find ourselves entering. I’m using Agentic Engineering to refer to building software using coding agents—tools like Claude Code and OpenAI Codex, where the defining feature is that they can both generate and execute code—allowing them to test that code and iterate on it independently of turn-by-turn guidance from their human supervisor. I think of vibe coding using its or

### Introducing Claude Opus 4.5 (Prompt Injection Robustness)

- URL: https://www.anthropic.com/news/claude-opus-4-5
- raw snapshot: `raw/hot-topics-sources/2026-04-10/012-introducing-claude-opus-4-5.md`
- 수집 제목: Introducing Claude Opus 4.5 \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing Claude Opus 4.5 Nov 24, 2025 Our newest model, Claude Opus 4.5, is available today. It’s intelligent, efficient, and the best model in the world for coding, agents, and computer use. It’s also meaningfully better at everyday tasks like deep research and working with slides and spreadsheets. Opus 4.5 is a step forward in what AI systems can do, and a preview of larger changes to how work gets done. Claude Opus 4.5 is state-of-the-art on tests of real-world software engineering: Opus 4.5 is available today on our apps, our API, and on all three major cloud platforms. If you’re a developer, simply use claude-opus-4-5-20251101 via the Claude API. Pricing is now $5/$25 per mi

### Effective context engineering for AI agents (Anthropic)

- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/001-effective-context-engineering-for-ai-agents.md`
- 수집 제목: Effective context engineering for AI agents \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Effective context engineering for AI agents Published Sep 29, 2025 Context is a critical but finite resource for AI agents. In this post, we explore strategies for effectively curating and managing the context that powers them. After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: context engineering. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of “what configuration of context is most likely to generate our model’s desired behavior?" Context refers to the set of tokens included when sampling from a l

### Context Engineering for AI Agents in Open-Source Software (AGENTS.md study)

- URL: https://arxiv.org/abs/2510.21413
- raw snapshot: `raw/hot-topics-sources/2026-04-10/040-context-engineering-for-ai-agents-in-open-source-software.md`
- 수집 제목: [2510.21413] Context Engineering for AI Agents in Open-Source Software

[2510.21413] Context Engineering for AI Agents in Open-Source Software Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.21413 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Software Engineering arXiv:2510.21413 (cs) [Submitted on 24 Oct 2025 (v1), last revised 5 Feb 2026 (this version, v4)] Title:Context Engineering for AI Agents in Open-Source Software Authors:Seyedmoein Mohsenimofidi, Matthias Galster, Christoph Treude, Sebastian Baltes Vie

---
title: Generator-Evaluator Harness Architecture
section: Agent Architecture
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Generator-Evaluator Harness Architecture

## 기존 큐레이션 요약

- 정의: 생성 에이전트와 별도의 평가 에이전트를 분리해 자기평가 편향을 외부화하는 GAN 영감의 멀티 에이전트 하니스.
- 왜 중요한가: 2026년 3월 24일 Anthropic의 "Harness design for long-running application development" 글이 Sonnet 4.5의 자기평가 편향과 컨텍스트 불안(context anxiety) 문제를 정면으로 다루며 화제가 되었고, 같은 글에서 Opus 4.5의 등장으로 일부 하니스 컴포넌트를 제거할 수 있다고 밝혀 모델 진화에 따른 하니스 재설계 논의가 본격화됐다.

## 개별 원문 수집 스냅샷

### Harness design for long-running application development (Anthropic)

- URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- raw snapshot: `raw/hot-topics-sources/2026-04-10/011-harness-design-for-long-running-application-development.md`
- 수집 제목: Harness design for long-running application development \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Harness design for long-running application development Published Mar 24, 2026 Harness design is key to performance at the frontier of agentic coding. Here's how we pushed Claude further in frontend design and long-running autonomous software engineering. Written by Prithvi Rajasekaran, a member of our Labs team. Over the past several months I’ve been working on two interconnected problems: getting Claude to produce high-quality frontend designs, and getting it to build complete applications without human intervention. This work originated with earlier efforts on our frontend design skill and long-running coding agent harness, where my colleagues and I were able to improv

### Introducing Claude Opus 4.5

- URL: https://www.anthropic.com/news/claude-opus-4-5
- raw snapshot: `raw/hot-topics-sources/2026-04-10/012-introducing-claude-opus-4-5.md`
- 수집 제목: Introducing Claude Opus 4.5 \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing Claude Opus 4.5 Nov 24, 2025 Our newest model, Claude Opus 4.5, is available today. It’s intelligent, efficient, and the best model in the world for coding, agents, and computer use. It’s also meaningfully better at everyday tasks like deep research and working with slides and spreadsheets. Opus 4.5 is a step forward in what AI systems can do, and a preview of larger changes to how work gets done. Claude Opus 4.5 is state-of-the-art on tests of real-world software engineering: Opus 4.5 is available today on our apps, our API, and on all three major cloud platforms. If you’re a developer, simply use claude-opus-4-5-20251101 via the Claude API. Pricing is now $5/$25 per mi

### Self-Improving AI Agents through Self-Play (Generator-Verifier-Updater)

- URL: https://arxiv.org/html/2512.02731v1
- raw snapshot: `raw/hot-topics-sources/2026-04-10/013-self-improving-ai-agents-through-self-play.md`
- 수집 제목: Self-Improving AI Agents through Self-Play

Self-Improving AI Agents through Self-Play 1 Introduction Relation to Reinforcement Learning. Relation to Geometric Deep Learning. Beyond LLMs and RL. 2 Preliminaries: The Geometric Setting 2.1 Semantic Foundations 2.2 The External Geometry: Batteries 2.3 The Internal Topology: Parameter Manifold 2.4 The Architecture Map 2.5 The Bridge: Observable Representations 3 The Generator-Verifier-Updater (GVU) Operator 1. The Generator (𝒢\mathcal{G}). 2. The Verifier (𝒱\mathcal{V}). 3. The Updater (𝒰\mathcal{U}). 3.1 Monolithic self-improvement: the diagonal regime G=V=UG=V=U 3.2 Ensemble GVU: LLM councils 3.3 Universality of the GVU decomposition 4 Spectral Stability: The Variance Inequality 4.1 Decomposition of the Update Vector 4.2 The Variance Inequality 4.3 Geometric interpretation on the stat

### ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification

- URL: https://arxiv.org/abs/2506.11442
- raw snapshot: `raw/hot-topics-sources/2026-04-10/014-reveal-self-evolving-code-agents-via-iterative-generation-verification.md`
- 수집 제목: [2506.11442] ReVeal: Self-Evolving Code Agents via Reliable Self-Verification

[2506.11442] ReVeal: Self-Evolving Code Agents via Reliable Self-Verification Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2506.11442 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Software Engineering arXiv:2506.11442 (cs) [Submitted on 13 Jun 2025 (v1), last revised 21 Oct 2025 (this version, v2)] Title:ReVeal: Self-Evolving Code Agents via Reliable Self-Verification Authors:Yiyang Jin, Kunzhao Xu, Hang Li, Xueting Han, Yanmin Zhou, Cheng Li, Jing Bai View a PDF of the paper titled ReVeal: Sel

### MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs

- URL: https://arxiv.org/abs/2512.20845
- raw snapshot: `raw/hot-topics-sources/2026-04-10/015-mar-multi-agent-reflexion-improves-reasoning-abilities-in-llms.md`
- 수집 제목: [2512.20845] MAR:Multi-Agent Reflexion Improves Reasoning Abilities in LLMs

[2512.20845] MAR:Multi-Agent Reflexion Improves Reasoning Abilities in LLMs Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2512.20845 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2512.20845 (cs) [Submitted on 23 Dec 2025] Title:MAR:Multi-Agent Reflexion Improves Reasoning Abilities in LLMs Authors:Onat Ozer, Grace Wu, Yuchen Wang, Daniel Dosti, Honghao Zhang, Vivi De La Rue View a PDF of the paper titled MAR:Multi

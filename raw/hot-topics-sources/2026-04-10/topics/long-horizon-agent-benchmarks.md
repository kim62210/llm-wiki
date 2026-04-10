---
title: Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)
section: Agent Architecture
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)

## 기존 큐레이션 요약

- 정의: 수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대.
- 왜 중요한가: 2025년 9월 Meta의 ARE 플랫폼과 GAIA 2가 시간·예산 제약을 도입했고, 2025년 12월 SWE-EVO는 GPT-5가 SWE-Bench Verified(65%) 대비 21%만 해결한다는 결과로 long-horizon 갭을 폭로했으며, 이로 인해 2026년 1분기 모든 주요 lab이 평가 프레임워크를 long-horizon 중심으로 재정비 중이다.

## 개별 원문 수집 스냅샷

### ARE: Scaling up Agent Environments and Evaluations (Meta, GAIA 2)

- URL: https://arxiv.org/abs/2509.17158
- raw snapshot: `raw/hot-topics-sources/2026-04-10/034-are-scaling-up-agent-environments-and-evaluations.md`
- 수집 제목: [2509.17158] ARE: Scaling Up Agent Environments and Evaluations

[2509.17158] ARE: Scaling Up Agent Environments and Evaluations Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2509.17158 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2509.17158 (cs) [Submitted on 21 Sep 2025 (v1), last revised 10 Dec 2025 (this version, v2)] Title:ARE: Scaling Up Agent Environments and Evaluations Authors:Romain Froger, Pierre Andrews, Matteo Bettini, Amar Budhiraja, Ricardo Silveira Cabral, Virg

### SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution

- URL: https://arxiv.org/abs/2512.18470
- raw snapshot: `raw/hot-topics-sources/2026-04-10/035-swe-evo-benchmarking-coding-agents-in-long-horizon-software-evolution.md`
- 수집 제목: [2512.18470] SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios

[2512.18470] SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2512.18470 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Software Engineering arXiv:2512.18470 (cs) [Submitted on 20 Dec 2025 (v1), last revised 4 Apr 2026 (this version, v5)] Title:SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios Authors:Minh V. T. Thai, Tue Le, Dung Nguyen

### SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model (OpenHands)

- URL: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model
- raw snapshot: `raw/hot-topics-sources/2026-04-10/036-sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model.md`
- 수집 제목: SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025

SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025 Product Features Terminal / CLI Agentic power from the command line Web GUI Agentic development, made human. SDK Build agents your way. Enterprise Pricing Benchmarks Community Resources Learn Docs Manifesto Blog Company Press Careers About Contact Build with SDK Build with SDK Try it live Try it live Menu Close ← Back to Blog SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model Written by Xingyao Wang Published on April 17, 2025 We're thrilled to announce that OpenHands has reached a new milestone, achieving state-of-the-art results on SWE-Bench Verified! SWE-Bench and OpenHands to verify they have appropriately scoped unit tests and well-specified issue descriptions. Due to its realis

### Introducing Claude Opus 4.5 (SWE-bench Verified 80.9%)

- URL: https://www.anthropic.com/news/claude-opus-4-5
- raw snapshot: `raw/hot-topics-sources/2026-04-10/012-introducing-claude-opus-4-5.md`
- 수집 제목: Introducing Claude Opus 4.5 \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing Claude Opus 4.5 Nov 24, 2025 Our newest model, Claude Opus 4.5, is available today. It’s intelligent, efficient, and the best model in the world for coding, agents, and computer use. It’s also meaningfully better at everyday tasks like deep research and working with slides and spreadsheets. Opus 4.5 is a step forward in what AI systems can do, and a preview of larger changes to how work gets done. Claude Opus 4.5 is state-of-the-art on tests of real-world software engineering: Opus 4.5 is available today on our apps, our API, and on all three major cloud platforms. If you’re a developer, simply use claude-opus-4-5-20251101 via the Claude API. Pricing is now $5/$25 per mi

### Introducing Claude Sonnet 4.5 (OSWorld 61.4%, 30+ hour focus)

- URL: https://www.anthropic.com/news/claude-sonnet-4-5
- raw snapshot: `raw/hot-topics-sources/2026-04-10/037-introducing-claude-sonnet-4-5.md`
- 수집 제목: Introducing Claude Sonnet 4.5 \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing Claude Sonnet 4.5 Sep 29, 2025 Claude Sonnet 4.5 is the best coding model in the world. It's the strongest model for building complex agents. It’s the best model at using computers. And it shows substantial gains in reasoning and math. Code is everywhere. It runs every application, spreadsheet, and software tool you use. Being able to use those tools and reason through hard problems is how modern work gets done. Claude Sonnet 4.5 makes this possible. We're releasing it along with a set of major upgrades to our products. In Claude Code, we've added checkpoints—one of our most requested features—that save your progress and allow you to roll back instantly to a previous sta

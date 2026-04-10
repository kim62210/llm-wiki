---
title: SWE-bench Pro
section: Model Releases & Benchmarks
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# SWE-bench Pro

## 기존 큐레이션 요약

- 정의: Scale AI가 구축한 장기 호흡(long-horizon) 소프트웨어 엔지니어링 벤치마크.
- 왜 중요한가: 41개 저장소 1,865개 태스크(공개 731 + Held-out 858 + 상용 276)로 GPL/상용 코드 기반 오염 방지 설계, SWE-bench Verified가 80%를 넘어 포화되자 2026년 사실상의 후속 표준으로 부상했고 GLM-5.1 58.4%/GPT-5.4-pro 59.1% 등 최상위 모델도 60% 문턱에서 분투 중이다.

## 개별 원문 수집 스냅샷

### SWE-Bench Pro Paper Landing — Scale Labs

- URL: https://labs.scale.com/papers/swe_bench_pro
- raw snapshot: `raw/hot-topics-sources/2026-04-10/150-swe-bench-pro-paper-landing-scale-labs.md`
- 수집 제목: SWE-Bench Pro: AI on Software Engineering Tasks | Scale Labs

SWE-Bench Pro: AI on Software Engineering Tasks | Scale Labs [PAPERS][BLOG][LEADERBOARDS][SHOWDOWN]⌘K ⌘K BACK AgentsSafety, Evaluation and Alignment9/19/2025 SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? Xiang Deng*, Jeff Da*, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean Hendryx, Zifan Wang, Chen Bo Calvin Zhang, Noah Jacobson, Bing Liu, Brad Kenstler *Co-first author and equal contributions. View paper SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? We introduce SWE-BENCH PRO, a substantially more challenging benchmark that builds upon the best practices of SWE-Bench [25], but is explicitly designed to capture r

### SWE-Bench Pro Leaderboard (Public) — Scale

- URL: https://labs.scale.com/leaderboard/swe_bench_pro_public
- raw snapshot: `raw/hot-topics-sources/2026-04-10/143-swe-bench-pro-leaderboard-scale-labs.md`
- 수집 제목: SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale

SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale [PAPERS][BLOG][LEADERBOARDS][SHOWDOWN]⌘K ⌘K Leaderboard Agentic SWE Atlas - Test Writing SWE Atlas - Codebase QnA MCP Atlas SWE-Bench Pro (Public Dataset) SWE-Bench Pro (Private Dataset) Remote Labor Index (RLI) Safety Frontier Legacy 2025 Scale AI. All rights reserved. BACK SWE-Bench Pro (Public Dataset) Evaluating challenging long-horizon software engineering tasks in public open source repositories SWE-Bench Pro SWE-Bench Pro is a benchmark designed to provide a rigorous and realistic evaluation of AI agents for software engineering. It was developed to address several limitations in existing benchmarks by tackling four key challenges: Data Contamination: Models have likely seen the evaluation code during training, m

### SWE-Bench Pro Leaderboard (Private) — Scale

- URL: https://labs.scale.com/leaderboard/swe_bench_pro_private
- raw snapshot: `raw/hot-topics-sources/2026-04-10/151-swe-bench-pro-leaderboard-scale.md`
- 수집 제목: Scale Labs Leaderboard: SWE-Bench Pro (Private Dataset)

Scale Labs Leaderboard: SWE-Bench Pro (Private Dataset) [PAPERS][BLOG][LEADERBOARDS][SHOWDOWN]⌘K ⌘K Leaderboard Agentic SWE Atlas - Test Writing SWE Atlas - Codebase QnA MCP Atlas SWE-Bench Pro (Public Dataset) SWE-Bench Pro (Private Dataset) Remote Labor Index (RLI) Safety Frontier Legacy 2025 Scale AI. All rights reserved. BACK SWE-Bench Pro (Private Dataset) Evaluating challenging long-horizon software engineering tasks in commercial-grade private repositories Overview SWE-Bench Pro is a benchmark designed to provide a rigorous and realistic evaluation of AI agents for software engineering. It was developed to address several limitations in existing benchmarks by tackling four key challenges: Data Contamination: Models have likely seen the evaluation code during training, making it hard

### SWE-Bench Pro Project — Scale

- URL: https://scaleapi.github.io/SWE-bench_Pro-os
- raw snapshot: `raw/hot-topics-sources/2026-04-10/152-swe-bench-pro-project-scale.md`
- 수집 제목: SWE-Bench Pro

SWE-Bench Pro SWE-Bench Pro Evaluating AI Agents on Challenging Long-Horizon SWE Tasks 🏆 Official Leaderboard📄 Paper💻 Code💾 Data📤 Submit Leaderboard Model% Resolved(+/-)Link🥇SWE-Agent + claude-4-5-Sonnet43.72🔗🥈SWE-Agent + claude-4-Sonnet42.70🔗🥉SWE-Agent + claude-4-5-haiku39.45🔗SWE-Agent + gpt-5-2025-08-07 (High)36.30🔗SWE-Agent + glm-4.535.52🔗SWE-Agent + kimi-k2-instruct27.67🔗SWE-Agent + gpt-oss-120b16.20🔗 Note that these results are initial runs and subject to change, pending an official announcement from Scale. Models are run with an uncapped cost and with a turn limit of 250. The (+/-) column shows the 95% confidence interval (margin of error) for each score, calculated using binomial proportion statistics (total problems: 730). About We introduce SWE-Bench Pro, a substantially more chal

### scaleapi/SWE-bench_Pro-os — GitHub

- URL: https://github.com/scaleapi/SWE-bench_Pro-os
- raw snapshot: `raw/hot-topics-sources/2026-04-10/153-scaleapi-swe-bench-pro-os-github.md`
- 수집 제목: GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub

GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE E

---
title: Context Rot & Effective Context Window
section: RAG & Context Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Context Rot & Effective Context Window

## 기존 큐레이션 요약

- 정의: 입력 길이가 늘수록 LLM 성능이 단조적으로 저하되는 현상.
- 왜 중요한가: 2026년 1M-10M 토큰 윈도우가 쏟아지지만 Chroma·Morph 보고서가 모든 프런티어 모델의 유효 컨텍스트가 광고의 60-70%에 불과함을 재확인하며, "effective context" 측정이 RAG 설계의 핵심 화두가 됐다.

## 개별 원문 수집 스냅샷

### Context Rot: How Increasing Input Tokens Impacts LLM Performance (Chroma)

- URL: https://www.trychroma.com/research/context-rot
- raw snapshot: `raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md`
- 수집 제목: Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma

Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma Products Products SyncDatabaseAgent DocsEnterprisePricingResearch Resources Resources ChangelogUpdatesCommunityGitHubPackage Search Log inSign up Chroma Technical Report July 14, 2025 Context Rot: How Increasing Input Tokens Impacts LLM Performance Kelly Hong Anton Troynikov Jeff Huber Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks. In this report, we evaluate 18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. Our

### RULER: What's the Real Context Size of Your Long-Context Language Models? (NVIDIA)

- URL: https://github.com/NVIDIA/RULER
- raw snapshot: `raw/hot-topics-sources/2026-04-10/163-ruler-what-s-the-real-context-size-of-your-long-context-language-models.md`
- 수집 제목: GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub

GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Sol

### LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks

- URL: https://arxiv.org/abs/2412.15204
- raw snapshot: `raw/hot-topics-sources/2026-04-10/164-longbench-v2-towards-deeper-understanding-and-reasoning-on-realistic-long-contex.md`
- 수집 제목: [2412.15204] LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks

[2412.15204] LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2412.15204 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2412.15204 (cs) [Submitted on 19 Dec 2024 (v1), last revised 3 Jan 2025 (this version, v2)] Title:LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks Authors:Yushi Bai, Shangqing Tu, Jiajie Zhang, Hao Peng, Xiaozhi Wa

### LongBench v2 Project Page

- URL: https://longbench2.github.io
- raw snapshot: `raw/hot-topics-sources/2026-04-10/165-longbench-v2-project-page.md`
- 수집 제목: LongBench v2

LongBench v2 🔥 More Research LongBenchLongAlignLongWriterLongCite LongBench v2 Benchmarking Deeper Understanding and Reasoning on Realistic Long-context Multitasks LongBench Team arXivCode 📊 Dataset 🏆 Leaderboard Introduction LongBench v2 is designed to assess the ability of LLMs to handle long-context problems requiring deep understanding and reasoning across real-world multitasks. LongBench v2 has the following features: (1) Length: Context length ranging from 8k to 2M words, with the majority under 128k. (2) Difficulty: Challenging enough that even human experts, using search tools within the document, cannot answer correctly in a short time. (3) Coverage: Cover various realistic scenarios. (4) Reliability: All in a multiple-choice question format for reliable evaluation. To elaborate, 

### Lost in the Middle: How Language Models Use Long Contexts (TACL)

- URL: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long
- raw snapshot: `raw/hot-topics-sources/2026-04-10/166-lost-in-the-middle-how-language-models-use-long-contexts.md`

_수집 실패: HTTPError: HTTP Error 403: Forbidden_

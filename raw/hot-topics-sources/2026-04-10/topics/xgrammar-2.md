---
title: XGrammar-2 Constrained Decoding for Agentic LLMs
section: Inference Optimization
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# XGrammar-2 Constrained Decoding for Agentic LLMs

## 기존 큐레이션 요약

- 정의: 에이전트 워크플로 대상 동적 JSON/문법 제약 디코딩 엔진.
- 왜 중요한가: 2026년 초 XGrammar-2가 발표되며 토큰당 40마이크로초 이하 마스크 생성과 near-zero overhead를 달성했고, vLLM·SGLang·TRT-LLM 기본 백엔드로 자리잡으며 llguidance와 함께 프로덕션 구조 출력 표준이 되었다.

## 개별 원문 수집 스냅샷

### XGrammar: Flexible and Efficient Structured Generation Engine for LLMs

- URL: https://arxiv.org/abs/2411.15100
- raw snapshot: `raw/hot-topics-sources/2026-04-10/110-xgrammar-flexible-and-efficient-structured-generation-engine-for-llms.md`
- 수집 제목: [2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models

[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2411.15100 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2411.15100 (cs) [Submitted on 22 Nov 2024 (v1), last revised 12 May 2025 (this version, v3)] Title:XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models Authors:Yixin Dong, Charl

### mlc-ai/xgrammar GitHub repository

- URL: https://github.com/mlc-ai/xgrammar
- raw snapshot: `raw/hot-topics-sources/2026-04-10/111-mlc-ai-xgrammar-github-repository.md`
- 수집 제목: GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub

GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams St

### Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar (MLC blog)

- URL: https://blog.mlc.ai/2024/11/22/achieving-efficient-flexible-portable-structured-generation-with-xgrammar
- raw snapshot: `raw/hot-topics-sources/2026-04-10/112-achieving-efficient-flexible-and-portable-structured-generation-with-xgrammar.md`
- 수집 제목: MLC | Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar

MLC | Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar Home Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar Nov 22, 2024 • MLC Community We are witnessing an exciting era for large language models (LLMs). As LLM applications evolve, we are increasingly moving toward LLM agents that not only respond in raw text but can also generate code, call environment functions, and even control robots. To enable these richer LLM agent applications, LLM engines need to produce structured outputs that can be consumed by downstream agent systems. Examples of these structures include JSON, SQL, Python, and more. This paradigm is known as the structured generation in LLM inference. Fundamentally, an ideal LLM structured generation system should 

### guidance-ai/llguidance GitHub repository

- URL: https://github.com/guidance-ai/llguidance
- raw snapshot: `raw/hot-topics-sources/2026-04-10/113-guidance-ai-llguidance-github-repository.md`
- 수집 제목: GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub

GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonpro

### Catalyst: XGrammar (CMU)

- URL: https://catalyst.cs.cmu.edu/projects/xgrammar.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/114-catalyst-xgrammar.md`
- 수집 제목: Catalyst: XGrammar

Catalyst: XGrammar Home People Research Publications XGrammar XGrammar is an open-source library for efficient, flexible, and portable structured generation. It supports general context-free grammar to enable a broad range of structures while bringing careful system optimizations to enable fast executions. XGrammar features a minimal and portable C++ backend that can be easily integrated into multiple environments and frameworks, and is co-designed with the LLM inference engine and enables zero-overhead structured generation in LLM inference. Reference Paper Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, and Tianqi Chen. XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models. MLSys 2025. Overview XGrammar provides full and effic

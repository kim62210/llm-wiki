---
title: DSPy + GEPA optimize_anything
section: Dev Tooling & Frameworks
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# DSPy + GEPA optimize_anything

## 기존 큐레이션 요약

- 정의: 프롬프트·코드·에이전트 아키텍처를 선언적으로 최적화하는 Stanford NLP 프레임워크.
- 왜 중요한가: 2026년 2월 optimize_anything API 공개로 GEPA(Genetic-Pareto) 최적화가 프롬프트를 넘어 코드·에이전트 구조까지 확장됐고, 관련 논문이 ICLR 2026 oral에 채택되며 "프롬프트가 아닌 프로그래밍" 패러다임의 구심점이 됐다.

## 개별 원문 수집 스냅샷

### DSPy Official Docs

- URL: https://dspy.ai
- raw snapshot: `raw/hot-topics-sources/2026-04-10/413-dspy-official-docs.md`
- 수집 제목: DSPy

DSPy Skip to content DSPy Get Started Initializing search stanfordnlp/dspy DSPy in Production Community FAQ Get Started Learn DSPy Tutorials API Reference DSPy stanfordnlp/dspy Get Started Get Started Table of contents 1) Modules help you describe AI behavior as code, not strings. 2) Optimizers tune the prompts and weights of your AI modules. 3) DSPy's Ecosystem advances open-source AI research. Learn DSPy Learn DSPy DSPy Programming DSPy Programming Programming Overview Language Models Signatures Modules Adapters Tools MCP DSPy Evaluation DSPy Evaluation Evaluation Overview Data Handling Metrics DSPy Optimization DSPy Optimization Optimization Overview Optimizers Tutorials Tutorials Build AI Programs with DSPy Build AI Programs with DSPy Managing Conversation History Building AI Agents wi

### dspy.GEPA: Reflective Prompt Optimizer

- URL: https://dspy.ai/api/optimizers/GEPA/overview
- raw snapshot: `raw/hot-topics-sources/2026-04-10/414-dspy-gepa-reflective-prompt-optimizer.md`
- 수집 제목: 1. GEPA Overview - DSPy

1. GEPA Overview - DSPy Skip to content DSPy 1. GEPA Overview Initializing search stanfordnlp/dspy DSPy in Production Community FAQ Get Started Learn DSPy Tutorials API Reference DSPy stanfordnlp/dspy Get Started Learn DSPy Learn DSPy DSPy Programming DSPy Programming Programming Overview Language Models Signatures Modules Adapters Tools MCP DSPy Evaluation DSPy Evaluation Evaluation Overview Data Handling Metrics DSPy Optimization DSPy Optimization Optimization Overview Optimizers Tutorials Tutorials Build AI Programs with DSPy Build AI Programs with DSPy Managing Conversation History Building AI Agents with DSPy Building AI Applications by Customizing DSPy Modules Retrieval-Augmented Generation (RAG) Building RAG as Agent Entity Extraction Classification Multi-Hop RAG Privacy-Conscious D

### stanfordnlp/dspy GitHub

- URL: https://github.com/stanfordnlp/dspy
- raw snapshot: `raw/hot-topics-sources/2026-04-10/415-stanfordnlp-dspy-github.md`
- 수집 제목: GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models · GitHub

GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small an

### optimize_anything: Universal API for Optimizing any Text Parameter

- URL: https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything
- raw snapshot: `raw/hot-topics-sources/2026-04-10/416-optimize-anything-universal-api-for-optimizing-any-text-parameter.md`
- 수집 제목: optimize_anything: A Universal API for Optimizing any Text Parameter - GEPA

optimize_anything: A Universal API for Optimizing any Text Parameter - GEPA Skip to content ShowcaseBlogNewDocsTutorialsAPIAbout Initializing search gepa-ai/gepa GEPA gepa-ai/gepa Showcase About Blog Blog Archive Archive 2026 Guides Guides Quick Start FAQ Creating Adapters Candidate Selection Strategies Acceptance Criterion Using Callbacks Experiment Tracking Using Claude Code as a Proposer gskill Contributing Tutorials Tutorials DSPy Full Program Evolution ARC AGI Example 3D Unicorn Optimization (Seedless) API Reference API Reference optimize_anything optimize_anything optimize_anything GEPAConfig EngineConfig ReflectionConfig MergeConfig RefinerConfig TrackingConfig Evaluator OptimizationState LogContext log get_log_context set_log_context make_litellm_lm Core Core optimize GEPAAdapter E

### gepa-ai/gepa GitHub

- URL: https://github.com/gepa-ai/gepa
- raw snapshot: `raw/hot-topics-sources/2026-04-10/417-gepa-ai-gepa-github.md`
- 수집 제목: GitHub - gepa-ai/gepa: Optimize prompts, code, and more with AI-powered Reflective Text Evolution · GitHub

GitHub - gepa-ai/gepa: Optimize prompts, code, and more with AI-powered Reflective Text Evolution · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Sma

---
title: vLLM Semantic Router (Iris / Athena)
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# vLLM Semantic Router (Iris / Athena)

## 기존 큐레이션 요약

- 정의: mmBERT 기반 신경 분류기로 요청을 적절한 모델에 라우팅하는 시스템 레벨 Mixture-of-Models.
- 왜 중요한가: 2026년 1월 5일 v0.1 Iris 첫 메이저 릴리스, 3월 10일 v0.2 Athena가 연이어 공개되며 600+ PR을 흡수했고, Athena는 벤치마크에서 86% 요청을 로컬 무료 모델로 라우팅해 토큰 비용 최적화의 새로운 표준을 제시했다.

## 개별 원문 수집 스냅샷

### vLLM Semantic Router v0.1 Iris: The First Major Release (2026-01-05)

- URL: https://blog.vllm.ai/2026/01/05/vllm-sr-iris.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/338-vllm-semantic-router-v0-1-iris-the-first-major-release.md`
- 수집 제목: vLLM Semantic Router v0.1 Iris: The First Major Release | vLLM Blog

vLLM Semantic Router v0.1 Iris: The First Major Release | vLLM Blog Menu Search DocsDocumentationBlogEventsContactCommunityGitHub Theme DocsBlogEventsContactCommunitySearch⌘J Blog vLLM Semantic Router v0.1 Iris: The First Major Release January 5, 20269 min read vLLM Semantic Router Team #ecosystem Why Iris? What's New in v0.1 Iris? 1. Architecture Overhaul: Signal-Decision Plugin Chain Architecture 2. Performance Optimization: Modular LoRA Architecture 3. Safety Enhancement: HaluGate Hallucination Detection 4. UX Improvements: One-Command Installation 5. Ecosystem Integration 6. MoM (Mixture of Models) Family 7. Responses API Support 8. Tool Selection Looking Ahead: v0.2 Roadmap Signal-Decision Architecture Enhancements Model Selection Algorithms Out-of-Box Plugins Multi-turn Algorithm Exp

### Getting started with vLLM Semantic Router Athena release - Red Hat Developer (2026-03-25)

- URL: https://developers.redhat.com/articles/2026/03/25/getting-started-vllm-semantic-router-athena-release
- raw snapshot: `raw/hot-topics-sources/2026-04-10/339-getting-started-with-vllm-semantic-router-athena-release-red-hat-developer.md`
- 수집 제목: Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI | Red Hat Developer

Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI | Red Hat Developer Skip to main content Products Platforms Red Hat Enterprise Linux Red Hat AI Red Hat OpenShift Red Hat Ansible Automation Platform See all Red Hat products Featured Red Hat build of OpenJDK Red Hat Developer Hub Red Hat JBoss Enterprise Application Platform Red Hat OpenShift Dev Spaces Red Hat OpenShift Local Red Hat Developer Sandbox Try Red Hat products and technologies without setup or configuration fees for 30 days with this shared Red Hat OpenShift and Kubernetes cluster. Try at no cost Technologies Featured AI/ML Linux Kubernetes Automation See all technologies Programming languages & frameworks Java Python JavaScript System design & architecture Red Hat arch

### vllm-project/semantic-router GitHub Repository

- URL: https://github.com/vllm-project/semantic-router
- raw snapshot: `raw/hot-topics-sources/2026-04-10/340-vllm-project-semantic-router-github-repository.md`
- 수집 제목: GitHub - vllm-project/semantic-router: System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge · GitHub

GitHub - vllm-project/semantic-router: System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY CO

### vLLM Semantic Router Official Site

- URL: https://vllm-semantic-router.com
- raw snapshot: `raw/hot-topics-sources/2026-04-10/341-vllm-semantic-router-official-site.md`
- 수집 제목: Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router

Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router Skip to main content vLLM-SRDocs About White Paper Vision Paper ResearchBlog Community Governance Working Group Contributing Guide Code of Conduct GitHub Issues English English 简体中文 Latest Latest v0.1 GitHubModels Open-source LLM router Routeevery requestwith one systembrainto thebestmodel Unified routing across local, private, and frontier models—guided by cost, latency, privacy, and safety. Public BetaRead white paper System brain Connect all models with system brain Kimi Zhipu MiniMax ChatGPT Claude Gemini DeepSeek Qwen Llama Mistral Grok Kimi Zhipu MiniMax ChatGPT Claude Gemini DeepSeek Qwen Llama Mistral Grok Kimi Zhipu MiniMax ChatGPT Claude Gemini DeepSeek Qwen Llama Mistral Grok Kimi Zhipu MiniMax ChatGPT Claude Ge

### Intelligent Semantic Routing - vLLM production-stack Docs

- URL: https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/342-intelligent-semantic-routing-vllm-production-stack-docs.md`
- 수집 제목: Intelligent Semantic Routing — production-stack

Intelligent Semantic Routing — production-stack Skip to main content Back to topCtrl+K SearchCtrl+K Getting Started Prerequisite Quick Start FAQ Deployment Deployment Overview Helm Chart Deployment CRD Deployment Gateway Inference Extension Use Cases KV Cache Aware Routing Prefix Aware Routing Disaggregated Prefill Sharing KV Cache Across Instances Benchmarking Distributed Tracing Tool Enabled Installation Pipeline Parallelism with KubeRay Sleep and Wakeup Mode Autoscaling with KEDA Intelligent Semantic Routing Developer Guide Contributing Docker Guide Community Community Meetings Repository Suggest edit .rst .pdf Intelligent Semantic Routing Contents What is vLLM Semantic Router? Benefits of Integration Table of Contents Prerequisites Step 1: Deploy the vLLM Production Stack Step 2: Deplo

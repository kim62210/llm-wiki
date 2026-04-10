---
title: llm-d & Gateway API Inference Extension
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# llm-d & Gateway API Inference Extension

## 기존 큐레이션 요약

- 정의: vLLM+Kubernetes Gateway API Inference Extension 기반의 CNCF 분산 추론 스택.
- 왜 중요한가: 2026년 3월 24일 llm-d가 CNCF Sandbox에 편입되었고 Gateway API Inference Extension v1.4.0이 3월 20일 GA되면서, IBM/Red Hat/Google/NVIDIA가 밀고 있는 쿠버네티스 네이티브 분산 추론의 공식 표준 경로가 되었다.

## 개별 원문 수집 스냅샷

### llm-d/llm-d GitHub Repository

- URL: https://github.com/llm-d/llm-d
- raw snapshot: `raw/hot-topics-sources/2026-04-10/329-llm-d-llm-d-github-repository.md`
- 수집 제목: GitHub - llm-d/llm-d: Achieve state of the art inference performance with modern accelerators on Kubernetes · GitHub

GitHub - llm-d/llm-d: Achieve state of the art inference performance with modern accelerators on Kubernetes · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enter

### llm-d Architecture Documentation

- URL: https://llm-d.ai/docs/architecture
- raw snapshot: `raw/hot-topics-sources/2026-04-10/330-llm-d-architecture-documentation.md`
- 수집 제목: llm-d Architecture | llm-d

llm-d Architecture | llm-d Skip to main content 🎉 llm-d 0.5 is now released! Check out hierarchical KV offloading, cache-aware LoRA routing, resilient networking with UCCL, and scale-to-zero autoscaling. Read the announcement → ArchitectureGuidesUsageCommunityBlogVideos Join Slack llm-d Architecture Latest Release Components Inference Scheduler Model Service Inference Simulator Infrastructure KV Cache Benchmark Tools Workload Variant Autoscaler llm-d Architecture On this page llm-d Architecture Achieve SOTA Inference Performance On Any Accelerator llm-d is a high-performance distributed inference serving stack optimized for production deployments on Kubernetes. We help you achieve the fastest "time to state-of-the-art (SOTA) performance" for key OSS large language models across most hardwa

### kubernetes-sigs/gateway-api-inference-extension GitHub

- URL: https://github.com/kubernetes-sigs/gateway-api-inference-extension
- raw snapshot: `raw/hot-topics-sources/2026-04-10/331-kubernetes-sigs-gateway-api-inference-extension-github.md`
- 수집 제목: GitHub - kubernetes-sigs/gateway-api-inference-extension: Gateway API Inference Extension · GitHub

GitHub - kubernetes-sigs/gateway-api-inference-extension: Gateway API Inference Extension · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and m

### Introducing Gateway API Inference Extension - Kubernetes Blog

- URL: https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension
- raw snapshot: `raw/hot-topics-sources/2026-04-10/332-introducing-gateway-api-inference-extension-kubernetes-blog.md`
- 수집 제목: Introducing Gateway API Inference Extension | Kubernetes

Introducing Gateway API Inference Extension | KubernetesKubernetes Documentation Kubernetes Blog Training Careers Partners Community Versions Release Informationv1.35v1.34v1.33v1.32v1.31 English 中文 (Chinese)বাংলা (Bengali) বাংলা (Bengali) Français (French) Français (French) Deutsch (German) Deutsch (German) हिन्दी (Hindi) हिन्दी (Hindi) Bahasa Indonesia (Indonesian) Bahasa Indonesia (Indonesian) Italiano (Italian) Italiano (Italian) 日本語 (Japanese) 日本語 (Japanese) 한국어 (Korean) 한국어 (Korean) Polski (Polish) Polski (Polish) Português (Portuguese) Português (Portuguese) Русский (Russian) Русский (Russian) Español (Spanish) Español (Spanish) Українська (Ukrainian) Українська (Ukrainian) Tiếng Việt (Vietnamese) Tiếng Việt (Vietnamese) Kubernetes Blog English বাংলা (Bengali) বাংলা (Bengali) 中文 (Chi

### Gateway API Inference Extension Documentation

- URL: https://gateway-api-inference-extension.sigs.k8s.io
- raw snapshot: `raw/hot-topics-sources/2026-04-10/333-gateway-api-inference-extension-documentation.md`
- 수집 제목: Introduction - Kubernetes Gateway API Inference Extension

Introduction - Kubernetes Gateway API Inference Extension Skip to content Kubernetes Gateway API Inference Extension Introduction Initializing search kubernetes-sigs/gateway-api-inference-extension Overview Guides Performance Reference Enhancements Contributing Kubernetes Gateway API Inference Extension kubernetes-sigs/gateway-api-inference-extension Overview Overview Introduction Introduction Table of contents Concepts and Definitions Key Features API Resources Composable Layers Gateway API Implementations Endpoint Picker Model Server Frameworks Request Flow Who is working on Gateway API Inference Extension? Concepts Concepts API Overview Design Principles Conformance Roles and Personas Priority and Capacity Implementations Implementations Gateways Model Servers FAQ Guides Guides User Gui

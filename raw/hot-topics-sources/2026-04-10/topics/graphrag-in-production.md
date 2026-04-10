---
title: GraphRAG / LightRAG / LazyGraphRAG in Production
section: RAG & Context Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# GraphRAG / LightRAG / LazyGraphRAG in Production

## 기존 큐레이션 요약

- 정의: 지식 그래프 + 커뮤니티 요약을 결합해 multi-hop·global QA를 푸는 RAG 계열.
- 왜 중요한가: Microsoft GraphRAG v3.0.8(2026-03-27) 릴리스와 LightRAG의 OpenSearch·Neo4j 백엔드, LazyGraphRAG의 0.1% 인덱싱 비용(vs full GraphRAG 대비 700배 저렴한 global query)이 맞물리며 "비용이 감당 가능한 Graph RAG" 시대가 2026년 초에 본격화됐다.

## 개별 원문 수집 스냅샷

### Microsoft GraphRAG GitHub

- URL: https://github.com/microsoft/graphrag
- raw snapshot: `raw/hot-topics-sources/2026-04-10/202-microsoft-graphrag-github.md`
- 수집 제목: GitHub - microsoft/graphrag: A modular graph-based Retrieval-Augmented Generation (RAG) system · GitHub

GitHub - microsoft/graphrag: A modular graph-based Retrieval-Augmented Generation (RAG) system · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small 

### GraphRAG Documentation (microsoft.github.io)

- URL: https://microsoft.github.io/graphrag
- raw snapshot: `raw/hot-topics-sources/2026-04-10/203-graphrag-documentation.md`
- 수집 제목: Welcome - GraphRAG

Welcome - GraphRAG Skip to content GraphRAG Welcome Initializing search graphrag Home Indexing Prompt Tuning Query Configuration CLI Extras GraphRAG graphrag Home Home Welcome Welcome Table of contents Get Started with GraphRAG 🚀 GraphRAG vs Baseline RAG 🔍 The GraphRAG Process 🤖 Index Query Prompt Tuning Versioning Getting Started Development Guide Indexing Indexing Overview Architecture Dataflow Methods Inputs Outputs Custom Graphs Prompt Tuning Prompt Tuning Overview Auto Tuning Manual Tuning Query Query Overview Global Search Local Search DRIFT Search Question Generation Notebooks Notebooks Overview Global Search Local Search DRIFT Search Configuration Configuration Overview Init Command Detailed Configuration Language Model Selection CLI Extras Extras Microsoft Research Blog Visualizat

### LightRAG: Simple and Fast Retrieval-Augmented Generation (EMNLP 2025)

- URL: https://github.com/hkuds/lightrag
- raw snapshot: `raw/hot-topics-sources/2026-04-10/204-lightrag-simple-and-fast-retrieval-augmented-generation.md`
- 수집 제목: GitHub - HKUDS/LightRAG: [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation" · GitHub

GitHub - HKUDS/LightRAG: [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation" · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small

### LazyGraphRAG: Setting a new standard for quality and cost (Microsoft Research Blog)

- URL: https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost
- raw snapshot: `raw/hot-topics-sources/2026-04-10/205-lazygraphrag-setting-a-new-standard-for-quality-and-cost.md`
- 수집 제목: LazyGraphRAG: Setting a new standard for quality and cost - Microsoft Research

LazyGraphRAG: Setting a new standard for quality and cost - Microsoft Research Skip to main contentResearchPublicationsCode & dataPeopleMicrosoft Research blogArtificial intelligenceAudio & acousticsComputer visionGraphics & multimediaHuman-computer interactionHuman language technologiesSearch & information retrievalData platforms and analyticsHardware & devicesProgramming languages & software engineeringQuantum computingSecurity, privacy & cryptographySystems & networkingAlgorithmsMathematicsEcology & environmentEconomicsMedical, health & genomicsSocial sciencesTechnology for emerging marketsAcademic programsEvents & academic conferencesMicrosoft Research ForumBehind the Tech podcastMicrosoft Research blogMicrosoft Research ForumMicrosoft Research podcastAbout Microsoft ResearchCareers & 

### Project GraphRAG - Microsoft Research

- URL: https://www.microsoft.com/en-us/research/project/graphrag
- raw snapshot: `raw/hot-topics-sources/2026-04-10/206-project-graphrag-microsoft-research.md`
- 수집 제목: Project GraphRAG - Microsoft Research

Project GraphRAG - Microsoft Research Skip to main contentResearchPublicationsCode & dataPeopleMicrosoft Research blogArtificial intelligenceAudio & acousticsComputer visionGraphics & multimediaHuman-computer interactionHuman language technologiesSearch & information retrievalData platforms and analyticsHardware & devicesProgramming languages & software engineeringQuantum computingSecurity, privacy & cryptographySystems & networkingAlgorithmsMathematicsEcology & environmentEconomicsMedical, health & genomicsSocial sciencesTechnology for emerging marketsAcademic programsEvents & academic conferencesMicrosoft Research ForumBehind the Tech podcastMicrosoft Research blogMicrosoft Research ForumMicrosoft Research podcastAbout Microsoft ResearchCareers & internshipsPeopleEmeritus programNews & a

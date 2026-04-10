---
title: Serverless Object-Storage Vector DBs (Turbopuffer 등)
section: RAG & Context Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Serverless Object-Storage Vector DBs (Turbopuffer 등)

## 기존 큐레이션 요약

- 정의: 벡터 + BM25를 S3/GCS 기반으로 저장해 TB급 인덱스 비용을 수십 배 낮춘 벡터DB.
- 왜 중요한가: Turbopuffer가 object-storage 기반 하이브리드 검색(p50 8ms warm, p90 444ms cold)으로 1M+ 컨텍스트 시대의 "first-stage retrieval" 기본값이 됐고, Qdrant는 양자화, LanceDB는 in-process 멀티모달로 각각 틈새를 공고히 하며 "disk-first vector DB" 트렌드가 굳어졌다.

## 개별 원문 수집 스냅샷

### Turbopuffer Documentation

- URL: https://turbopuffer.com/docs
- raw snapshot: `raw/hot-topics-sources/2026-04-10/207-turbopuffer-documentation.md`
- 수집 제목: Introduction

Introduction Query prices reduced by up to 94%We've reduced query prices by up to 94% Navigation turbopuffer DocsPricingCustomersBlogTalk to usLog inSign up Introduction Architecture Concepts Guarantees Tradeoffs Limits Regions Roadmap & Changelog Security Encryption Backups Private Networking Performance Pinning Guides Quickstart Vector Search Full-Text Search Hybrid Search Testing Permissions API Auth & Encoding Write Query Namespace metadata Export Warm cache List namespaces Delete namespace Recall Introduction ╔═ turbopuffer ════════════════════════════╗ ╔════════════╗ ║ ║░ ║ ║░ ║ ┏━━━━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━━━┓ ║░ ║ client ║░───API──▶║ ┃ Memory/ ┃────▶┃ Object ┃ ║░ ║ ║░ ║ ┃ SSD Cache ┃ ┃ Storage (S3) ┃ ║░ ╚════════════╝░ ║ ┗━━━━━━━━━━━━━━━┛ ┗━━━━━━━━━━━━━━┛ ║░ ░░░░░░░░░░░░░░ ║ ║░ ╚

### Qdrant Official Site

- URL: https://qdrant.tech
- raw snapshot: `raw/hot-topics-sources/2026-04-10/208-qdrant-official-site.md`
- 수집 제목: Qdrant - Vector Search Engine

Qdrant - Vector Search Engine Build a Biomedical AI Copilot with Neo4j + Qdrant Join live on April 21 Products Qdrant Vector Database Qdrant Cloud Qdrant Hybrid Cloud Qdrant Enterprise Solutions Qdrant Cloud Inference Qdrant Edge (Beta) Solutions Use Cases RAG Recommendation Systems Advanced Search Data Analysis & Anomaly Detection AI Agents Industries E-commerce Legal Tech Hospitality & Travel HR Tech Healthcare Tech Developers Documentation Community GitHub Roadmap Change Log Certification Resources Benchmarks Blog Articles Demos Startup Program Bug Bounty Program Company About us Customers Partners Careers Contact us Pricing Log inGet Started Products Qdrant Vector Database Qdrant Cloud Qdrant Hybrid Cloud Qdrant Enterprise Solutions Qdrant Cloud Inference Qdrant Edge (Beta) Solutions U

### LanceDB GitHub

- URL: https://github.com/lancedb/lancedb
- raw snapshot: `raw/hot-topics-sources/2026-04-10/209-lancedb-github.md`
- 수집 제목: GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub

GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPA

### Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (Hugging Face Forums)

- URL: https://discuss.huggingface.co/t/vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search-bm25-text-image-vectors/171610
- raw snapshot: `raw/hot-topics-sources/2026-04-10/210-vespa-vs-qdrant-vs-turbopuffer-for-large-scale-hybrid-search.md`
- 수집 제목: Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (BM25 + text & image vectors) - Community Calls - Hugging Face Forums

Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (BM25 + text & image vectors) - Community Calls - Hugging Face ForumsHugging Face Forums Vespa vs Qdrant vs Turbopuffer for large-scale hybrid search (BM25 + text & image vectors) Community Calls sumit-raj-710 December 16, 2025, 4:48am 1 Hi everyone — we’re evaluating search platforms for a hybrid search use case and would appreciate insights from people who’ve used Vespa, Qdrant, or Turbopuffer in real systems. Background Use case: B2B product search Catalog size: ~170 million products Traffic: ~100 QPS (steady-state, higher during peaks) Latency goal: sub-100 ms end-to-end Data: each product has text and images Search requirements: Traditional keyword search (BM25 or equivalent) Text vector search Image vector search Ability to

### A Practical Guide to Training Custom Rerankers (LanceDB Blog)

- URL: https://www.lancedb.com/blog/a-practical-guide-to-training-custom-rerankers
- raw snapshot: `raw/hot-topics-sources/2026-04-10/211-a-practical-guide-to-training-custom-rerankers.md`
- 수집 제목: A Practical Guide to Training Custom Rerankers

A Practical Guide to Training Custom Rerankers Why Multimodal Data Needs a Better Lakehouse? — Download the Research Study Curation Find optimal distributions, deduplicate massive datasets, and surface edge cases—all in one place Feature Engineering Build and scale features with Python UDFs, automatic updates, and no table rewrites Search & Analytics Unified vector, full-text, and hybrid search with SQL filters for production-ready retrieval Training Train directly from curated data with up to 70% MFU and no data movement bottlenecks In ProductionDocsBlog Community Thank you! Your submission has been received! Oops! Something went wrong while submitting the form. Searching in Blog Posts Lance JSON Support: Why You Might Not Really Need Variant Lance's JSONB storage, scalar indexing, data e

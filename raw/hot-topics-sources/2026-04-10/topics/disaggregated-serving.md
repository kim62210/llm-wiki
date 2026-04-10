---
title: Disaggregated Prefill/Decode Serving
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Disaggregated Prefill/Decode Serving

## 기존 큐레이션 요약

- 정의: 프리필과 디코드 단계를 물리적으로 분리된 GPU 풀에서 독립 스케일링.
- 왜 중요한가: 2026년 초 vLLM, SGLang, Ray Serve, Dynamo 등 모든 메이저 프레임워크가 PD 디스어그리게이션을 프로덕션급으로 성숙시켰고, Meta와 Hugging Face 등에서 실제 운영에 투입되며 TTFT와 TPOT를 SLO로 분리 최적화하는 표준 패턴이 되었다.

## 개별 원문 수집 스냅샷

### Disaggregated Prefilling (experimental) - vLLM Docs

- URL: https://docs.vllm.ai/en/latest/features/disagg_prefill
- raw snapshot: `raw/hot-topics-sources/2026-04-10/081-vllm-disaggregated-prefilling-documentation.md`
- 수집 제목: Disaggregated Prefilling (experimental) - vLLM

Disaggregated Prefilling (experimental) - vLLM Skip to content You are viewing the latest developer preview docs. Click here to view docs for the latest stable release. vLLM Disaggregated Prefilling (experimental) Initializing search GitHub Home User Guide Developer Guide Benchmarking API Reference CLI Reference Community vLLM GitHub Home User Guide User Guide Getting Started Getting Started Quickstart Installation Installation GPU CPU TPU Examples Examples Basic Basic Offline Inference Online Serving Offline Inference Offline Inference Async LLM Streaming Audio Language Automatic Prefix Caching Batch LLM Inference Chat With Tools Context Extension Data Parallel Disaggregated Prefill V1 Disaggregated Prefill Encoder Decoder Multimodal Extract Hidden States KV Load Failure Recovery Test LLM

### Prefill/decode disaggregation — Ray Serve Docs

- URL: https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/315-prefill-decode-disaggregation-ray-serve-docs.md`
- 수집 제목: Prefill/decode disaggregation — Ray 2.54.1

Prefill/decode disaggregation — Ray 2.54.1Skip to main content Back to top Ctrl+K Try Ray with $100 credit — Start now× Site Navigation Get Started Use Cases Example Gallery Library Ray CoreScale general Python applications Ray DataScale data ingest and preprocessing Ray TrainScale machine learning training Ray TuneScale hyperparameter tuning Ray ServeScale model serving Ray RLlibScale reinforcement learning Docs Resources Discussion ForumGet your Ray questions answered TrainingHands-on learning BlogUpdates, best practices, user-stories EventsWebinars, meetups, office hours Success StoriesReal-world workload examples EcosystemLibraries integrated with Ray CommunityConnect with us Try Managed Ray Site Navigation Get Started Use Cases Example Gallery Library Ray CoreScale general Python appl

### DistServe: Disaggregating Prefill and Decoding for Goodput-optimized LLM Serving (arXiv)

- URL: https://arxiv.org/abs/2401.09670
- raw snapshot: `raw/hot-topics-sources/2026-04-10/316-distserve-disaggregating-prefill-and-decoding-for-goodput-optimized-llm-serving.md`
- 수집 제목: [2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving

[2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2401.09670 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Distributed, Parallel, and Cluster Computing arXiv:2401.09670 (cs) [Submitted on 18 Jan 2024 (v1), last revised 6 Jun 2024 (this version, v3)] Title:DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language 

### DistServe USENIX OSDI 2024 Paper

- URL: https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf
- raw snapshot: `raw/hot-topics-sources/2026-04-10/317-distserve-usenix-osdi-2024-paper.md`

%PDF-1.5 %¿÷¢þ 1 0 obj << /Names 3 0 R /Outlines 4 0 R /Pages 5 0 R /Type /Catalog >> endobj 2 0 obj << /Author () /CreationDate (D:20240605030250Z) /Creator (LaTeX with hyperref) /Keywords () /ModDate (D:20240612184623Z) /PTEX.Fullbanner (This is pdfTeX, Version 3.141592653-2.6-1.40.25 \(TeX Live 2023\) kpathsea version 6.3.5) /Producer (pdfTeX-1.40.25; modified using iText® Core 8.0.0 \(AGPL version\) ©2000-2023 Apryse Group NV) /Subject () /Title () /Trapped /False >> endobj 3 0 obj << /Dests 6 0 R >> endobj 4 0 obj << /Count 12 /First 7 0 R /Last 8 0 R /Type /Outlines >> endobj 5 0 obj << /Count 19 /Kids [ 9 0 R 10 0 R 11 0 R 12 0 R 13 0 R 14 0 R 15 0 R 16 0 R 17 0 R 18 0 R 19 0 R 20 0 R 21 0 R 22 0 R 23 0 R 24 0 R 25 0 R 26 0 R 27 0 R ] /Type /Pages >> endobj 6 0 obj << /Kids [ 28 0 R

### Disaggregated Prefill and Decode - Perplexity Engineering Blog

- URL: https://www.perplexity.ai/hub/blog/disaggregated-prefill-and-decode
- raw snapshot: `raw/hot-topics-sources/2026-04-10/318-disaggregated-prefill-and-decode-perplexity-engineering-blog.md`
- 수집 제목: Disaggregated Prefill and Decode

Disaggregated Prefill and Decode Blog Research Careers Help Center Ask anything Written by AI Team Published on Aug 1, 2025 Disaggregated Prefill and Decode In order to generate output tokens from an input prompt, LLM inference is split into two stages: prefill and decode. Prefill runs on the input tokens, populating KV caches, before entering the decode stage that generates tokens one-by-one. While a single decode step typically runs for tens of milliseconds, prefill takes substantially longer. If run on the same devices, mixing prefill with decode degrades decode performance. In this article we explore an established solution in the form of disaggregated prefill and decode, running them on separate devices to maximize both prefill throughput and decode latencies. Prefill vs Decode Perfor

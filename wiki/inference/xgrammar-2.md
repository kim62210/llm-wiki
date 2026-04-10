---
title: XGrammar-2 Constrained Decoding for Agentic LLMs
category: inference
page_type: entity
project: XGrammar-2 Constrained Decoding for Agentic LLMs
tags: [inference, entity, xgrammar, 2]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/xgrammar-2.md, raw/hot-topics-sources/2026-04-10/110-xgrammar-flexible-and-efficient-structured-generation-engine-for-llms.md, raw/hot-topics-sources/2026-04-10/111-mlc-ai-xgrammar-github-repository.md, raw/hot-topics-sources/2026-04-10/112-achieving-efficient-flexible-and-portable-structured-generation-with-xgrammar.md, raw/hot-topics-sources/2026-04-10/113-guidance-ai-llguidance-github-repository.md, raw/hot-topics-sources/2026-04-10/114-catalyst-xgrammar.md]
created: 2026-04-10
updated: 2026-04-10
---
# XGrammar-2 Constrained Decoding for Agentic LLMs

에이전트 워크플로 대상 동적 JSON/문법 제약 디코딩 엔진.

## 왜 지금 중요한가

2026년 초 XGrammar-2가 발표되며 토큰당 40마이크로초 이하 마스크 생성과 near-zero overhead를 달성했고, vLLM·SGLang·TRT-LLM 기본 백엔드로 자리잡으며 llguidance와 함께 프로덕션 구조 출력 표준이 되었다.

## 대표 레퍼런스

- [XGrammar: Flexible and Efficient Structured Generation Engine for LLMs](https://arxiv.org/abs/2411.15100)
- [mlc-ai/xgrammar GitHub repository](https://github.com/mlc-ai/xgrammar)
- [Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar (MLC blog)](https://blog.mlc.ai/2024/11/22/achieving-efficient-flexible-portable-structured-generation-with-xgrammar)
- [guidance-ai/llguidance GitHub repository](https://github.com/guidance-ai/llguidance)
- [Catalyst: XGrammar (CMU)](https://catalyst.cs.cmu.edu/projects/xgrammar.html)

## 2026년 4월 큐레이션 요약

- 정의: 에이전트 워크플로 대상 동적 JSON/문법 제약 디코딩 엔진.
- 왜 중요한가: 2026년 초 XGrammar-2가 발표되며 토큰당 40마이크로초 이하 마스크 생성과 near-zero overhead를 달성했고, vLLM·SGLang·TRT-LLM 기본 백엔드로 자리잡으며 llguidance와 함께 프로덕션 구조 출력 표준이 되었다.
- 직접 수집 원문: 5개
- 주요 도메인: github.com×2, arxiv.org×1, blog.mlc.ai×1, catalyst.cs.cmu.edu×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/xgrammar-2.md`

### source별 핵심 신호

- **[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models** (`arxiv.org`): https://arxiv.org/abs/2411.15100
  - 메모: The applications of LLM Agents are becoming increasingly complex and diverse, leading to a high demand for structured outputs that can be parsed into code, structured function calls, and embodied agent commands.
- **GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub** (`github.com`): https://github.com/mlc-ai/xgrammar
  - 메모: To see all available qualifiers, see our documentation.
- **MLC | Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar** (`blog.mlc.ai`): https://blog.mlc.ai/2024/11/22/achieving-efficient-flexible-portable-structured-generation-with-xgrammar
  - 메모: We are witnessing an exciting era for large language models (LLMs).
- **GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub** (`github.com`): https://github.com/guidance-ai/llguidance
  - 메모: To see all available qualifiers, see our documentation.
- **Catalyst: XGrammar** (`catalyst.cs.cmu.edu`): https://catalyst.cs.cmu.edu/projects/xgrammar.html
  - 메모: supports general context-free grammar to enable a broad range of structures while bringing careful

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[kv-cache-compression|Chunk-Semantic KV Cache Compression]]

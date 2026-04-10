---
title: Circuit Tracing & Attribution Graphs
category: concepts
page_type: concept
tags: [concepts, concept, circuit, tracing]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/circuit-tracing.md, raw/hot-topics-sources/2026-04-10/363-circuit-tracing-revealing-computational-graphs-in-language-models.md, raw/hot-topics-sources/2026-04-10/364-on-the-biology-of-a-large-language-model.md, raw/hot-topics-sources/2026-04-10/365-open-sourcing-circuit-tracing-tools.md, raw/hot-topics-sources/2026-04-10/366-tracing-the-thoughts-of-a-large-language-model.md, raw/hot-topics-sources/2026-04-10/367-tracing-attention-computation-through-feature-interactions.md]
created: 2026-04-10
updated: 2026-04-10
---
# Circuit Tracing & Attribution Graphs

Cross-layer transcoder로 모델 내부 연산을 특징 단위 그래프로 복원하는 해석성 기법.

## 왜 중요한가

2025년 Anthropic이 오픈소스로 공개한 circuit tracing이 MIT Tech Review 2026 10대 혁신 기술로 선정됐고, 2026년 transformer-circuits 최신 논문들이 감정 개념, QK 어텐션 분해 등으로 확장되며 해석성의 주류 방법론으로 자리잡았다.

## 대표 레퍼런스

- [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)
- [Open-sourcing circuit-tracing tools (Anthropic)](https://www.anthropic.com/research/open-source-circuit-tracing)
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)
- [Tracing Attention Computation Through Feature Interactions](https://transformer-circuits.pub/2025/attention-qk/index.html)

## 2026년 4월 큐레이션 요약

- 정의: Cross-layer transcoder로 모델 내부 연산을 특징 단위 그래프로 복원하는 해석성 기법.
- 왜 중요한가: 2025년 Anthropic이 오픈소스로 공개한 circuit tracing이 MIT Tech Review 2026 10대 혁신 기술로 선정됐고, 2026년 transformer-circuits 최신 논문들이 감정 개념, QK 어텐션 분해 등으로 확장되며 해석성의 주류 방법론으로 자리잡았다.
- 직접 수집 원문: 5개
- 주요 도메인: transformer-circuits.pub×3, anthropic.com×2

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/circuit-tracing.md`

### source별 핵심 신호

- **Circuit Tracing: Revealing Computational Graphs in Language Models** (`transformer-circuits.pub`): https://transformer-circuits.pub/2025/attribution-graphs/methods.html
  - 메모: We introduce a method to uncover mechanisms underlying behaviors of language models.
- **On the Biology of a Large Language Model** (`transformer-circuits.pub`): https://transformer-circuits.pub/2025/attribution-graphs/biology.html
  - 메모: We investigate the internal mechanisms used by Claude 3.5 Haiku — Anthropic's lightweight production model — in a variety of contexts, using our circuit tracing methodology.
- **Open-sourcing circuit-tracing tools \ Anthropic** (`anthropic.com`): https://www.anthropic.com/research/open-source-circuit-tracing
  - 메모: In our recent interpretability research, we introduced a new method to trace the thoughts of a large language model. Today, we’re open-sourcing the method so that anyone can build on our research.
- **Tracing the thoughts of a large language model \ Anthropic** (`anthropic.com`): https://www.anthropic.com/research/tracing-thoughts-language-model
  - 메모: Tracing the thoughts of a large language model
- **Tracing Attention Computation Through Feature Interactions** (`transformer-circuits.pub`): https://transformer-circuits.pub/2025/attention-qk/index.html
  - 메모: We describe and apply a method to explain attention patterns in terms of feature interactions, and integrate this information into attribution graphs.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[deliberative-alignment|Deliberative Alignment & Anti-Scheming Training]]
- [[alignment-faking|Alignment Faking in LLMs]]
- [[context-engineering|Context Engineering]]

---
title: Circuit Tracing & Attribution Graphs
section: Safety & Alignment
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Circuit Tracing & Attribution Graphs

## 기존 큐레이션 요약

- 정의: Cross-layer transcoder로 모델 내부 연산을 특징 단위 그래프로 복원하는 해석성 기법.
- 왜 중요한가: 2025년 Anthropic이 오픈소스로 공개한 circuit tracing이 MIT Tech Review 2026 10대 혁신 기술로 선정됐고, 2026년 transformer-circuits 최신 논문들이 감정 개념, QK 어텐션 분해 등으로 확장되며 해석성의 주류 방법론으로 자리잡았다.

## 개별 원문 수집 스냅샷

### Circuit Tracing: Revealing Computational Graphs in Language Models

- URL: https://transformer-circuits.pub/2025/attribution-graphs/methods.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/363-circuit-tracing-revealing-computational-graphs-in-language-models.md`
- 수집 제목: Circuit Tracing: Revealing Computational Graphs in Language Models

Circuit Tracing: Revealing Computational Graphs in Language Models × Transformer Circuits Thread Circuit Tracing: Revealing Computational Graphs in Language Models Circuit Tracing: Revealing Computational Graphs in Language Models We introduce a method to uncover mechanisms underlying behaviors of language models. We produce graph descriptions of the model’s computation on prompts of interest by tracing individual computational steps in a “replacement model”. This replacement model substitutes a more interpretable component (here, a “cross-layer transcoder”) for parts of the underlying model (here, the multi-layer perceptrons) that it is trained to approximate. We develop a suite of visualization and validation tools we use to investigate these “attribution graphs” supporting simple behavi

### On the Biology of a Large Language Model

- URL: https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/364-on-the-biology-of-a-large-language-model.md`
- 수집 제목: On the Biology of a Large Language Model

On the Biology of a Large Language Model × Transformer Circuits Thread On the Biology of a Large Language Model On the Biology of a Large Language Model We investigate the internal mechanisms used by Claude 3.5 Haiku — Anthropic's lightweight production model — in a variety of contexts, using our circuit tracing methodology. Introductory Example: Multi-step ReasoningPlanning in PoemsMultilingual CircuitsAdditionMedical DiagnosesEntity Recognition and HallucinationsRefusalsLife of a JailbreakChain-of-thought FaithfulnessUncovering Hidden Goals in a Misaligned ModelCommonly Observed Circuit Components and StructureLimitations Authors Jack Lindsey†,Wes Gurnee*,Emmanuel Ameisen*,Brian Chen*,Adam Pearce*,Nicholas L. Turner*,Craig Citro*, David Abrahams,Shan Carter,Basil Hosmer,Jonathan Marcus,M

### Open-sourcing circuit-tracing tools (Anthropic)

- URL: https://www.anthropic.com/research/open-source-circuit-tracing
- raw snapshot: `raw/hot-topics-sources/2026-04-10/365-open-sourcing-circuit-tracing-tools.md`
- 수집 제목: Open-sourcing circuit-tracing tools \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Interpretability Open-sourcing circuit tracing tools May 29, 2025 In our recent interpretability research, we introduced a new method to trace the thoughts of a large language model. Today, we’re open-sourcing the method so that anyone can build on our research. Our approach is to generate attribution graphs, which (partially) reveal the steps a model took internally to decide on a particular output. The open-source library we’re releasing supports the generation of attribution graphs on popular open-weights models—and a frontend hosted by Neuronpedia lets you explore the graphs interactively. This project was led by participants in our Anthropic Fellows program, in collaboration with Decode Rese

### Tracing the thoughts of a large language model

- URL: https://www.anthropic.com/research/tracing-thoughts-language-model
- raw snapshot: `raw/hot-topics-sources/2026-04-10/366-tracing-the-thoughts-of-a-large-language-model.md`
- 수집 제목: Tracing the thoughts of a large language model \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Interpretability Tracing the thoughts of a large language model Mar 27, 2025 Read the paper Language models like Claude aren't programmed directly by humans—instead, they‘re trainedon large amounts of data. During that training process, they learn their own strategies to solve problems. These strategies are encoded in the billions of computations a model performs for every word it writes. They arrive inscrutable to us, the model’s developers. This means that we don’t understand how models do most of the things they do. Knowing how models like Claude think would allow us to have a better understanding of their abilities, as well as help us ensure that they’re doing what we intend them to. For exam

### Tracing Attention Computation Through Feature Interactions

- URL: https://transformer-circuits.pub/2025/attention-qk/index.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/367-tracing-attention-computation-through-feature-interactions.md`
- 수집 제목: Tracing Attention Computation Through Feature Interactions

Tracing Attention Computation Through Feature Interactions Transformer Circuits Thread Tracing Attention Computation Through Feature Interactions We describe and apply a method to explain attention patterns in terms of feature interactions, and integrate this information into attribution graphs. Authors Harish Kamath*,Emmanuel Ameisen*,Isaac Kauvar,Rodrigo Luger,Wes Gurnee,Adam Pearce,Sam Zimmerman,Joshua Batson,Thomas Conerly,Chris Olah,Jack Lindsey‡ Affiliations Anthropic Published July 31st, 2025 * Core Research Contributor;‡ Correspondence to jacklindsey@anthropic.com Transformer-based language models involve two main kinds of computations: multi-layer perceptron (MLP) layers that process information within a context position, and attention layers that conditionally move and process in

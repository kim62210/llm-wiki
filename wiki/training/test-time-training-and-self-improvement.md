---
title: Test-Time Training & Self-Improvement
aliases: ["test-time-training"]
category: training
page_type: concept
tags: [training, concept, test, time, training, and, self]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/test-time-training-and-self-improvement.md, raw/hot-topics-sources/2026-04-10/300-self-improving-llm-agents-at-test-time.md, raw/hot-topics-sources/2026-04-10/301-in-place-test-time-training.md, raw/hot-topics-sources/2026-04-10/302-test-time-learning-for-large-language-models.md, raw/hot-topics-sources/2026-04-10/303-continuous-self-improvement-of-llms-by-test-time-training-with-verifier-driven-s.md, raw/hot-topics-sources/2026-04-10/304-why-we-think.md]
created: 2026-04-10
updated: 2026-04-10
---
# Test-Time Training & Self-Improvement

추론 시점에 모델 파라미터를 실시간으로 업데이트해 성능을 높이는 기법.

## 왜 중요한가

오프라인 fine-tuning 없이 테스트 분포에 즉시 적응하는 TTT가 장기 컨텍스트와 에이전트 태스크에서 검증되며, 2026년 In-Place TTT 등 후속 논문이 쏟아지고 있다.

## 대표 레퍼런스

- [Self-Improving LLM Agents at Test-Time](https://arxiv.org/abs/2510.07841)
- [In-Place Test-Time Training](https://arxiv.org/abs/2604.06169)
- [Test-Time Learning for Large Language Models](https://arxiv.org/abs/2505.20633)
- [Continuous Self-Improvement of LLMs by Test-time Training with Verifier-Driven Sample Selection](https://arxiv.org/abs/2505.19475)
- [Why We Think (Lilian Weng, Lil'Log)](https://lilianweng.github.io/posts/2025-05-01-thinking/)

## 2026년 4월 큐레이션 요약

- 정의: 추론 시점에 모델 파라미터를 실시간으로 업데이트해 성능을 높이는 기법.
- 왜 중요한가: 오프라인 fine-tuning 없이 테스트 분포에 즉시 적응하는 TTT가 장기 컨텍스트와 에이전트 태스크에서 검증되며, 2026년 In-Place TTT 등 후속 논문이 쏟아지고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×4, lilianweng.github.io×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/test-time-training-and-self-improvement.md`

### source별 핵심 신호

- **[2510.07841] Self-Improving LLM Agents at Test-Time** (`arxiv.org`): https://arxiv.org/abs/2510.07841
  - 메모: One paradigm of language model (LM) fine-tuning relies on creating large training datasets, under the assumption that high quantity and diversity will enable models to generalize to novel tasks after post-training.
- **[2604.06169] In-Place Test-Time Training** (`arxiv.org`): https://arxiv.org/abs/2604.06169
  - 메모: The static ``train then deploy" paradigm fundamentally limits Large Language Models (LLMs) from dynamically adapting their weights in response to continuous streams of new information inherent in real-world tasks.
- **[2505.20633] Test-Time Learning for Large Language Models** (`arxiv.org`): https://arxiv.org/abs/2505.20633
  - 메모: While Large Language Models (LLMs) have exhibited remarkable emergent capabilities through extensive pre-training, they still face critical limitations in generalizing to specialized domains and handling diverse linguist
- **[2505.19475] Continuous Self-Improvement of Large Language Models by Test-time Training with Verifier-Driven Sample Selection** (`arxiv.org`): https://arxiv.org/abs/2505.19475
  - 메모: Learning to adapt pretrained language models to unlabeled, out-of-distribution data is a critical challenge, as models often falter on structurally novel reasoning tasks even while excelling within their training distrib
- **Why We Think | Lil'Log** (`lilianweng.github.io`): https://lilianweng.github.io/posts/2025-05-01-thinking/
  - 메모: Does the Model Tell What it Thinks Faithfully

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[agentic-rl|Agentic RL (Tool-Integrated Reasoning 학습)]]
- [[open-post-training-recipes|Open Post-Training Recipes (Tülu 3 / OLMo 3)]]

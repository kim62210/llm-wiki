---
title: Corpus-Grounded Self-Play (SPICE 계열)
category: training
page_type: concept
tags: [training, concept, corpus, grounded, self, play, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/corpus-grounded-self-play.md, raw/hot-topics-sources/2026-04-10/291-spice-self-play-in-corpus-environments-improves-reasoning.md, raw/hot-topics-sources/2026-04-10/292-towards-understanding-self-play-for-llm-reasoning.md, raw/hot-topics-sources/2026-04-10/293-spell-self-play-reinforcement-learning-for-evolving-long-context-language-models.md, raw/hot-topics-sources/2026-04-10/294-self-play-only-evolves-when-self-synthetic-pipeline-ensures-learnable-informatio.md, raw/hot-topics-sources/2026-04-10/295-language-self-play-for-data-free-training.md]
created: 2026-04-10
updated: 2026-04-10
---
# Corpus-Grounded Self-Play (SPICE 계열)

이 페이지는 Corpus-Grounded Self-Play (SPICE 계열)를 다룬다. 핵심은 외부 문서 코퍼스를 근거로 한 모델이 문제를 만들고 풀며 자기개선하는 RL이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

외부 문서 코퍼스를 근거로 한 모델이 문제를 만들고 풀며 자기개선하는 RL.

## 왜 지금 중요한가

순수 self-play가 몇 라운드 후 붕괴하는 문제를 코퍼스 접지(grounding)로 해결해, 라벨 없는 지속적 self-improvement의 현실적 경로로 주목받고 있다.

## 대표 자료

- [SPICE: Self-Play In Corpus Environments Improves Reasoning](https://arxiv.org/abs/2510.24684)
- [Towards Understanding Self-play for LLM Reasoning](https://arxiv.org/abs/2510.27072)
- [SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models](https://arxiv.org/html/2509.23863)
- [Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain](https://arxiv.org/html/2603.02218)
- [Language Self-Play For Data-Free Training](https://arxiv.org/pdf/2509.07414)

## 2026년 4월 큐레이션 요약

- 정의: 외부 문서 코퍼스를 근거로 한 모델이 문제를 만들고 풀며 자기개선하는 RL.
- 왜 중요한가: 순수 self-play가 몇 라운드 후 붕괴하는 문제를 코퍼스 접지(grounding)로 해결해, 라벨 없는 지속적 self-improvement의 현실적 경로로 주목받고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×5

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/corpus-grounded-self-play.md`

### source별 핵심 신호

- **[2510.24684] SPICE: Self-Play In Corpus Environments Improves Reasoning** (`arxiv.org`): https://arxiv.org/abs/2510.24684
  - 메모: Self-improving systems require environmental interaction for continuous adaptation.
- **[2510.27072] Towards Understanding Self-play for LLM Reasoning** (`arxiv.org`): https://arxiv.org/abs/2510.27072
  - 메모: Recent advances in large language model (LLM) reasoning, led by reinforcement learning with verifiable rewards (RLVR), have inspired self-play post-training, where models improve by generating and solving their own probl
- **SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models** (`arxiv.org`): https://arxiv.org/html/2509.23863
  - 메모: SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language ModelsReport GitHub Issue×
- **Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain** (`arxiv.org`): https://arxiv.org/html/2603.02218
  - 메모: Through experiments on a self-play coding task, we reveal that
- **Language Self-Play For Data-Free Training** (`arxiv.org`): https://arxiv.org/pdf/2509.07414
  - 메모: << /Author (Jakub Grudzien Kuba; Mengting Gu; Qi Ma; Yuandong Tian; Vijai Mohan; Jason Chen) /Creator (arXiv GenPDF \(tex2pdf:57610bf\)) /DOI (https://doi.org/10.48550/arXiv.2509.07414) /License (http://arxiv.org/license

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[rl-scaling-laws]]
- [[agentic-rl]]

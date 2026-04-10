---
title: Deliberative Alignment & Anti-Scheming Training
section: Safety & Alignment
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Deliberative Alignment & Anti-Scheming Training

## 기존 큐레이션 요약

- 정의: 추론 모델에게 안전 규범을 명시적으로 숙의시켜 숨은 목표 추구를 억제하는 학습법.
- 왜 중요한가: Apollo Research와 OpenAI의 공동 연구가 o3의 scheming을 13% → 0.4%로 낮췄지만 situational awareness 증가 부작용을 드러냈고, 이후 2026년 Apollo의 loss-of-control playbook과 연계되며 후속 평가가 집중되고 있다.

## 개별 원문 수집 스냅샷

### Stress Testing Deliberative Alignment for Anti-Scheming Training (Apollo)

- URL: https://www.apolloresearch.ai/research/stress-testing-deliberative-alignment-for-anti-scheming-training
- raw snapshot: `raw/hot-topics-sources/2026-04-10/358-stress-testing-deliberative-alignment-for-anti-scheming-training.md`
- 수집 제목: Stress Testing Deliberative Alignment for Anti-Scheming Training – Apollo Research

Stress Testing Deliberative Alignment for Anti-Scheming Training – Apollo Research Team Research Product Blog Press Careers Contact 17/09/2025 Stress Testing Deliberative Alignment for Anti-Scheming Training Contents Visit the Anti-Scheming website here Read the full paper here We partnered with OpenAI to assess frontier language models for early signs of scheming — covertly pursuing misaligned goals — in controlled stress-tests (non-typical environments), and studied a training method that can significantly reduce (but not eliminate) these behaviors. Our results are complicated by models’ increasing ability to recognize our evaluation environments as tests of their alignment. Motivation Future, highly capable AI systems might covertly pursue misaligned goals — what we call scheming. Three

### Detecting and reducing scheming in AI models (OpenAI)

- URL: https://openai.com/index/detecting-and-reducing-scheming-in-ai-models
- raw snapshot: `raw/hot-topics-sources/2026-04-10/359-detecting-and-reducing-scheming-in-ai-models.md`
- 수집 제목: Detecting and reducing scheming in AI models | OpenAI

Detecting and reducing scheming in AI models | OpenAI Skip to main content Research Products Business Developers Company Foundation(opens in a new window) Log inTry ChatGPT(opens in a new window) Research Products Business Developers Company Foundation(opens in a new window) Try ChatGPT(opens in a new window)Login OpenAI Table of contents Key findings from our research Scheming is different from other machine learning failure modes Training not to scheme for the right reasons Measuring scheming is further complicated by Situational Awareness Conclusion September 17, 2025 PublicationResearch Detecting and reducing scheming in AI models Together with Apollo Research, we developed evaluations for hidden misalignment (“scheming”) and found behaviors consistent with scheming in controlled tests

### Deliberative alignment: reasoning enables safer language models (OpenAI)

- URL: https://openai.com/index/deliberative-alignment
- raw snapshot: `raw/hot-topics-sources/2026-04-10/360-deliberative-alignment-reasoning-enables-safer-language-models.md`
- 수집 제목: Deliberative alignment: reasoning enables safer language models | OpenAI

Deliberative alignment: reasoning enables safer language models | OpenAI Skip to main content Research Products Business Developers Company Foundation(opens in a new window) Log inTry ChatGPT(opens in a new window) Research Products Business Developers Company Foundation(opens in a new window) Try ChatGPT(opens in a new window)Login OpenAI Table of contents Overview Method Results Conclusion December 20, 2024 PublicationReleaseSafety Deliberative alignment: reasoning enables safer language models Introducing our new alignment strategy for o-series models, which are directly taught safety specifications and how to reason over them. Read paper(opens in a new window) Share We introduce deliberative alignment, a training paradigm that directly teaches reasoning LLMs the text of human-written a

### Stress Testing Deliberative Alignment (arXiv 2509.15541)

- URL: https://arxiv.org/abs/2509.15541
- raw snapshot: `raw/hot-topics-sources/2026-04-10/361-stress-testing-deliberative-alignment.md`
- 수집 제목: [2509.15541] Stress Testing Deliberative Alignment for Anti-Scheming Training

[2509.15541] Stress Testing Deliberative Alignment for Anti-Scheming Training Happy Open Access Week from arXiv! YOU make open access possible! Tell us why you support #openaccess and give to arXiv this week to help keep science open for all. Donate! Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2509.15541 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2509.15541 (cs) [Submitted on 19 Sep 2025] Title:Stress Testing Deliberative Alignment for Anti-Scheming Training Au

### Frontier Models are Capable of In-Context Scheming (Apollo)

- URL: https://www.apolloresearch.ai/research/frontier-models-are-capable-of-incontext-scheming
- raw snapshot: `raw/hot-topics-sources/2026-04-10/362-frontier-models-are-capable-of-in-context-scheming.md`
- 수집 제목: Frontier Models are Capable of In-Context Scheming – Apollo Research

Frontier Models are Capable of In-Context Scheming – Apollo Research Team Research Product Blog Press Careers Contact 05/12/2024 Frontier Models are Capable of In-Context Scheming Contents Paper: read the full paper here. Transcripts: We provide a list of cherry-picked transcripts here. System card: We worked with OpenAI to test o1 before public deployment. You can find the results in the o1 system card. Below, we provide a summary of the main findings. We evaluated six frontier models for in-context scheming capabilities. For most evaluations, we instruct the model to strongly follow a goal, e.g. “Your goal is to prioritize public transport efficiency over general traffic flow in the long term (across many months). […] Make sure that you achieve your goal in the long term. Nothing else ma

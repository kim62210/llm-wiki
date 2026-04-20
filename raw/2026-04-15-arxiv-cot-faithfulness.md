---
source: arxiv
arxiv_id: "2603.22582"
title: "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?"
date: 2026-03-28
url: "https://arxiv.org/abs/2603.22582"
fetched: 2026-04-15
status: pending_ingest
---

## Abstract

A growing body of evidence suggests that Chain-of-Thought (CoT) explanations are frequently unfaithful. Claude 3.7 Sonnet acknowledges hints that influenced its answer only 25% of the time, while DeepSeek-R1 does so only 39% of the time. Unfaithful CoTs are paradoxically longer than faithful ones.

Models trained via RLHF are optimized to produce convincing reasoning, not accurate reasoning. If the actual internal process involves "cheating" (like using a hint), the model learns to hide that mess to receive a higher reward.

## Key Points

- 핵심 기여: 오픈 웨이트 추론 모델에서 CoT 충실도를 체계적으로 측정
- Claude 3.7 Sonnet: 힌트 인정률 25%, DeepSeek-R1: 39%
- 불충실한 CoT가 충실한 CoT보다 역설적으로 더 긴 경향
- RLHF 최적화가 "설득력 있는 추론"을 만들지 "정확한 추론"을 만들지 않음
- FaithCoT-Bench: 인스턴스-레벨 CoT 불충실성 벤치마크 최초 제안 (ICLR 2026)
- Counterfactual Simulation Training (CST): 충실도 개선 학습법

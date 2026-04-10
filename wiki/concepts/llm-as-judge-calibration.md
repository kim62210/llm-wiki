---
title: LLM-as-Judge Calibration & Reliability
category: concepts
page_type: concept
tags: [concepts, concept, llm, as, judge, calibration]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# LLM-as-Judge Calibration & Reliability

LLM 평가자의 과신·편향을 진단하고 확신도를 보정하는 기법.

## 왜 중요한가

2025-2026년 LLM 심사관의 과잉 확신(overconfidence)과 비전이적(non-transitive) 선호가 프로덕션 eval의 가장 큰 병목으로 부각되면서, 선형 프로브·Brier 스코어·통계적 보정 프레임워크가 연달아 제안되고 있다.

## 대표 레퍼런스

- [Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation (arXiv:2512.22245)](https://arxiv.org/abs/2512.22245)
- [How to Correctly Report LLM-as-a-Judge Evaluations (arXiv:2511.21140)](https://arxiv.org/abs/2511.21140)
- [Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution (arXiv:2508.06225)](https://arxiv.org/abs/2508.06225)
- [Evaluating the Effectiveness of LLM-Evaluators (Eugene Yan)](https://eugeneyan.com/writing/llm-evaluators/)
- [A Survey on LLM-as-a-Judge (arXiv:2411.15594)](https://arxiv.org/abs/2411.15594)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[error-analysis-for-evals|Error Analysis as the Eval Foundation]]
- [[context-engineering|Context Engineering]]

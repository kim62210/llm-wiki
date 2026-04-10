---
title: LLM-as-Judge Calibration & Reliability
category: concepts
page_type: concept
tags: [concepts, concept, llm, as, judge, calibration]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/llm-as-judge-calibration.md, raw/hot-topics-sources/2026-04-10/212-calibrating-llm-judges-linear-probes-for-fast-and-reliable-uncertainty-estimatio.md, raw/hot-topics-sources/2026-04-10/213-how-to-correctly-report-llm-as-a-judge-evaluations.md, raw/hot-topics-sources/2026-04-10/214-overconfidence-in-llm-as-a-judge-diagnosis-and-confidence-driven-solution.md, raw/hot-topics-sources/2026-04-10/215-evaluating-the-effectiveness-of-llm-evaluators.md, raw/hot-topics-sources/2026-04-10/216-a-survey-on-llm-as-a-judge.md]
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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 4건, eugeneyan.com 1건

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/llm-as-judge-calibration.md`
- [[2512.22245] Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation](https://arxiv.org/abs/2512.22245) — `raw/hot-topics-sources/2026-04-10/212-calibrating-llm-judges-linear-probes-for-fast-and-reliable-uncertainty-estimatio.md`
  - 메모: --- title: [2512.22245] Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation source_url: https://arxiv.org/abs/2512.22245 final_url: https://arxiv.org/abs/2512.22245 status: 200 content_type: text/html; charset=utf-8 topics: [LLM-as-Judge Calibration
- [[2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations](https://arxiv.org/abs/2511.21140) — `raw/hot-topics-sources/2026-04-10/213-how-to-correctly-report-llm-as-a-judge-evaluations.md`
  - 메모: --- title: [2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations source_url: https://arxiv.org/abs/2511.21140 final_url: https://arxiv.org/abs/2511.21140 status: 200 content_type: text/html; charset=utf-8 topics: [LLM-as-Judge Calibration & Reliability] sections: [Evals
- [[2508.06225] Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution](https://arxiv.org/abs/2508.06225) — `raw/hot-topics-sources/2026-04-10/214-overconfidence-in-llm-as-a-judge-diagnosis-and-confidence-driven-solution.md`
  - 메모: --- title: [2508.06225] Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution source_url: https://arxiv.org/abs/2508.06225 final_url: https://arxiv.org/abs/2508.06225 status: 200 content_type: text/html; charset=utf-8 topics: [LLM-as-Judge Calibration & Relia
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators) — `raw/hot-topics-sources/2026-04-10/215-evaluating-the-effectiveness-of-llm-evaluators.md`
  - 메모: --- title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge) source_url: https://eugeneyan.com/writing/llm-evaluators final_url: https://eugeneyan.com/writing/llm-evaluators/ status: 200 content_type: text/html; charset=utf-8 topics: [LLM-as-Judge Calibration & Re
- [[2411.15594] A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) — `raw/hot-topics-sources/2026-04-10/216-a-survey-on-llm-as-a-judge.md`
  - 메모: --- title: [2411.15594] A Survey on LLM-as-a-Judge source_url: https://arxiv.org/abs/2411.15594 final_url: https://arxiv.org/abs/2411.15594 status: 200 content_type: text/html; charset=utf-8 topics: [LLM-as-Judge Calibration & Reliability] sections: [Evals & Observability] fetche

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[error-analysis-for-evals|Error Analysis as the Eval Foundation]]
- [[context-engineering|Context Engineering]]

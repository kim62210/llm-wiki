---
title: LLM-as-Judge Calibration & Reliability
section: Evals & Observability
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# LLM-as-Judge Calibration & Reliability

## 기존 큐레이션 요약

- 정의: LLM 평가자의 과신·편향을 진단하고 확신도를 보정하는 기법.
- 왜 중요한가: 2025-2026년 LLM 심사관의 과잉 확신(overconfidence)과 비전이적(non-transitive) 선호가 프로덕션 eval의 가장 큰 병목으로 부각되면서, 선형 프로브·Brier 스코어·통계적 보정 프레임워크가 연달아 제안되고 있다.

## 개별 원문 수집 스냅샷

### Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation (arXiv:2512.22245)

- URL: https://arxiv.org/abs/2512.22245
- raw snapshot: `raw/hot-topics-sources/2026-04-10/212-calibrating-llm-judges-linear-probes-for-fast-and-reliable-uncertainty-estimatio.md`
- 수집 제목: [2512.22245] Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation

[2512.22245] Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2512.22245 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Machine Learning arXiv:2512.22245 (cs) [Submitted on 23 Dec 2025] Title:Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation Authors:Bhaktipriya Radharapu, Eshika Saxena, Kenneth Li, Chenxi Whitehouse, Adina Williams, Nicola Cancedda View a PDF of the paper titled Calibr

### How to Correctly Report LLM-as-a-Judge Evaluations (arXiv:2511.21140)

- URL: https://arxiv.org/abs/2511.21140
- raw snapshot: `raw/hot-topics-sources/2026-04-10/213-how-to-correctly-report-llm-as-a-judge-evaluations.md`
- 수집 제목: [2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations

[2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2511.21140 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Machine Learning arXiv:2511.21140 (cs) [Submitted on 26 Nov 2025 (v1), last revised 9 Feb 2026 (this version, v3)] Title:How to Correctly Report LLM-as-a-Judge Evaluations Authors:Chungpa Lee, Thomas Zeng, Jongwon Jeong, Jy-yong Sohn, Kangwook Lee View a PDF of the paper titled H

### Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution (arXiv:2508.06225)

- URL: https://arxiv.org/abs/2508.06225
- raw snapshot: `raw/hot-topics-sources/2026-04-10/214-overconfidence-in-llm-as-a-judge-diagnosis-and-confidence-driven-solution.md`
- 수집 제목: [2508.06225] Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution

[2508.06225] Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2508.06225 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2508.06225 (cs) [Submitted on 8 Aug 2025 (v1), last revised 18 Aug 2025 (this version, v3)] Title:Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution Authors:Zailong Tian, Zhuoheng Han, Yanzhe Chen, Haoz

### Evaluating the Effectiveness of LLM-Evaluators (Eugene Yan)

- URL: https://eugeneyan.com/writing/llm-evaluators
- raw snapshot: `raw/hot-topics-sources/2026-04-10/215-evaluating-the-effectiveness-of-llm-evaluators.md`
- 수집 제목: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)

Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge) eugeneyan Start Here Writing Speaking Prototyping About Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge) [ llmevalproductionsurvey🔥 ] · 49 min read LLM-evaluators, also known as “LLM-as-a-Judge”, are large language models (LLMs) that evaluate the quality of another LLM’s response to an instruction or query. Their growing adoption is partly driven by necessity. LLMs can now solve increasingly complex and open-ended tasks such as long-form summarization, translation, and multi-turn dialogue. As a result, conventional evals that rely on n-grams, semantic similarity, or a gold reference have become less effective at distinguishing good responses from the bad. And while we can rely on human evaluation or finetune

### A Survey on LLM-as-a-Judge (arXiv:2411.15594)

- URL: https://arxiv.org/abs/2411.15594
- raw snapshot: `raw/hot-topics-sources/2026-04-10/216-a-survey-on-llm-as-a-judge.md`
- 수집 제목: [2411.15594] A Survey on LLM-as-a-Judge

[2411.15594] A Survey on LLM-as-a-Judge Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2411.15594 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2411.15594 (cs) [Submitted on 23 Nov 2024 (v1), last revised 19 Oct 2025 (this version, v6)] Title:A Survey on LLM-as-a-Judge Authors:Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie Ma, Honghao Liu, Saizhuo Wang, K

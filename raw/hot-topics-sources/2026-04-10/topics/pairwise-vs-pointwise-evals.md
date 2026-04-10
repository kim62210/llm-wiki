---
title: Pairwise vs Pointwise Eval Protocol Bias
section: Evals & Observability
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Pairwise vs Pointwise Eval Protocol Bias

## 기존 큐레이션 요약

- 정의: 선호 비교와 절대 점수 프로토콜의 편향·안정성 비교.
- 왜 중요한가: 2025년 연구들이 페어와이즈 비교가 35% 뒤집힘률을 보이며 편향을 증폭한다는 것을 입증하면서, "어떤 프로토콜을 선택할 것인가"가 reward modeling·LLM judge 설계의 핵심 논쟁이 되었다.

## 개별 원문 수집 스냅샷

### Pairwise or Pointwise? Evaluating Feedback Protocols for Bias (arXiv:2504.14716)

- URL: https://arxiv.org/abs/2504.14716
- raw snapshot: `raw/hot-topics-sources/2026-04-10/242-pairwise-or-pointwise-evaluating-feedback-protocols-for-bias.md`
- 수집 제목: [2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation

[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2504.14716 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Machine Learning arXiv:2504.14716 (cs) [Submitted on 20 Apr 2025 (v1), last revised 21 Aug 2025 (this version, v2)] Title:Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation Authors:Tuhina Tripathi, Manya Wadhwa

### Aligning with Human Judgement: Pairwise Preference in LLM Evaluators (arXiv:2403.16950)

- URL: https://arxiv.org/abs/2403.16950
- raw snapshot: `raw/hot-topics-sources/2026-04-10/243-aligning-with-human-judgement-pairwise-preference-in-llm-evaluators.md`
- 수집 제목: [2403.16950] Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators

[2403.16950] Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2403.16950 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2403.16950 (cs) [Submitted on 25 Mar 2024 (v1), last revised 17 Jan 2025 (this version, v5)] Title:Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators Authors:Yinhong Liu, Han Zhou, Zhijiang Guo, Ehsan Sharegh

### The Comparative Trap: Pairwise Comparisons Amplify Biased Preferences (arXiv:2406.12319)

- URL: https://arxiv.org/html/2406.12319v4
- raw snapshot: `raw/hot-topics-sources/2026-04-10/244-the-comparative-trap-pairwise-comparisons-amplify-biased-preferences.md`
- 수집 제목: The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators

The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators 1 Introduction 2 Related Work 3 Analyzing LLM Evaluators on Adversarial Evaluation Samples 3.1 Meta-Evaluation Datasets 3.2 Setup 3.3 Results 4 PRePair: Pointwise Reasoning for Pairwise Evaluation 5 Experiments 5.1 Setup 5.2 Results 5.3 Analysis 5.3.1 Evaluating PrePair to Open-source LLMs 5.3.2 Evaluating PrePair to a Finetuned LLM Evaluator 5.3.3 Extending PrePair with Different Reasoning Strategies 5.3.4 Impacts of Different Aggregation Strategies in Pointwise Approach 5.3.5 Qualitative Result The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators Hawon Jeong 1 ChaeHun Park11footnotemark: 11 Jimin Hong12 Hojoon Lee1 Jaegul Choo1 1 KAIST AI 2 KRAFTON {hawon,ddehun,

### ELSPR: Evaluator LLM Training Data Self-Purification on Non-Transitive Preferences (arXiv:2505.17691)

- URL: https://arxiv.org/html/2505.17691
- raw snapshot: `raw/hot-topics-sources/2026-04-10/245-elspr-evaluator-llm-training-data-self-purification-on-non-transitive-preference.md`
- 수집 제목: ELSPR: Evaluator LLM Training Data Self-Purification on Non-Transitive Preferences via Tournament Graph Reconstruction

ELSPR: Evaluator LLM Training Data Self-Purification on Non-Transitive Preferences via Tournament Graph Reconstruction 1 Introduction 2 Related Work 2.1 LLM-as-a-Judge and Its Non-Transitive Preferences 2.2 Data Selection for LLM Fine-tuning 3 Methodology 3.1 Background 3.2 Quality Analysis Framework for Evaluator LLM Training Data 3.3 Filtering Strategy for Preference Data That Induce Non-Transitivity 4 Experiment Setup 4.1 Dataset 4.2 Preference Data Collection 4.3 Experiment Details 5 Results and Analysis 5.1 Main Results 5.2 Ablation Studies 6 Conclusion A Algorithm Detail B Additional Experimental Results B.1 Experimental Results of Different Prompt Forms. B.2 “Unseen” question validation C Evaluate Prompts C.1 CoT Comparison C.2 CoT Comparison (Tie Allowed) D Limitations and Future W

### Language Model Preference Evaluation with Multiple Weak Evaluators (arXiv:2410.12869)

- URL: https://arxiv.org/html/2410.12869v3
- raw snapshot: `raw/hot-topics-sources/2026-04-10/246-language-model-preference-evaluation-with-multiple-weak-evaluators.md`
- 수집 제목: Language Model Preference Evaluation with Multiple Weak Evaluators

Language Model Preference Evaluation with Multiple Weak Evaluators 1 Introduction 2 Related Work Preference evaluation of LLMs. Weak supervision. 3 Methodologies 3.1 Preference Graph 3.2 GED: Preference Graph Ensemble and Denoise Graph ensemble. Graph denoising. Graph to ranking. 3.3 Applications Response selection. Model Ranking. Model Alignment. 4 Theoretical Analysis 5 Experiments on Response Selection Experiment Setup. Main results. Ablation study. 6 Experiments on Model Ranking Experiment Setup. Main results. 7 Experiments on Instruct Tuning Experiment Setup. Main results. 8 Evaluating GED on More Metrics 9 Conclusion A Implementation Details A.1 Experimental Setup A.2 Details of Evaluator Selection Across Different Tasks Response Selection. Model Ranking. Instruction Tuning. A.3 Defi

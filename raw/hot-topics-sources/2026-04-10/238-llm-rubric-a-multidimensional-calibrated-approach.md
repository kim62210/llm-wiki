---
title: LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts†
source_url: https://arxiv.org/html/2501.00274v1
final_url: https://arxiv.org/html/2501.00274v1
status: 200
content_type: text/html; charset=utf-8
topics: [Rubric-Based Evaluation Frameworks]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:59.691518+00:00
---

# LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts†

## 원본 URL

https://arxiv.org/html/2501.00274v1

## 추출 본문

LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts†
1 Introduction

2 The LLM-Rubric Method
Evaluation Rubric Construction.

Multi-Dimensional Evaluation with LLMs.

Aggregated Evaluation with Personalized Calibration.

Decoding.

Calibration Network Architecture.

Multi-Task Learning.

Using the Predictions.

Future Extensions.

3 Data
3.1 Mining Topics for RAG

3.2 Synthetic Dialogue Generation

3.3 Real Dialogue Collection and Evaluation

4 Experiments
Hyperparameter Selection.

Synthetic Data Evaluation.

Real Data Evaluation.

Baseline Methods.

Oracle Methods.

5 Results

6 Analysis
Calibration.

Ablation Studies.

Oracle study.

On which dimensions do zero-shot LLMs need improvement?

How much human judge data is needed to train calibration?

7 Related Work
LLM Evaluation

Calibration of LLM evaluators.

Subjectivity in Evaluation.

8 Conclusions

Robustness.

Efficiency.

Downstream Evaluation.

Fine-Grained Evaluation.

Beyond User Satisfaction.

Fairness Auditing.

Human Data.

Harmful Uses.

Environmental Costs.

A Aggregating Predicted Scores
Dashboards.

B Handling Other Types of Datasets
Additional Features.

Missing Features.

Irregular Datasets.

Heterogeneous Response Types.

Comparative Judging.

C LLM-Rubric Questions

D Evaluation Prompt for LLM

E Evaluation Prompt and Preliminary Data Quality Questions for Humans

F Synthetic Dialogue Generation
DS1: LLM-Only Assistant with Simulated User.

DS2: Oracle RAG Assistant with Oracle Simulated User.

DS3: RAG Assistant with Oracle Simulated User.

DS4: RAG Assistant with Simulated User.

DS5: Retrieval-Augmented Dialogue Generation + Query Generation with Simulated User.

G Quality of the Generated Synthetic Dialogues
Questions on the naturalness of dialogues (DQQ1, DQQ2, Q1subscript𝑄1Q_{1}italic_Q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT).

Questions on citations (Q2subscript𝑄2Q_{2}italic_Q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT, Q3subscript𝑄3Q_{3}italic_Q start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT, Q4subscript𝑄4Q_{4}italic_Q start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT, Q5subscript𝑄5Q_{5}italic_Q start_POSTSUBSCRIPT 5 end_POSTSUBSCRIPT).

Questions on conciseness (Q6subscript𝑄6Q_{6}italic_Q start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT, Q7subscript𝑄7Q_{7}italic_Q start_POSTSUBSCRIPT 7 end_POSTSUBSCRIPT, Q8subscript𝑄8Q_{8}italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT).

Question on overall satisfaction (Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT).

H The User Interface for Human-Agent Dialogue Collection and Evaluation

I Evaluating the Collected Human-Agent Dialogues

J How much human judge data is needed to train calibration?

K Calibration Plots (Reliability Diagrams)

LLM-Rubric: A Multidimensional, Calibrated Approach 

to Automated Evaluation of Natural Language Texts†

Helia Hashemi∗ 
Jason Eisner∗ 
Corby Rosset 
Benjamin Van Durme 
Chris Kedzie

Microsoft 

{hhashemi,jeisner,corbyrosset,ben.vandurme,chriskedzie}@microsoft.com

Abstract
This paper introduces a framework for the automated evaluation of natural language texts. A manually constructed rubric describes how to assess multiple dimensions of interest. To evaluate a text, a large language model (LLM) is prompted with each rubric question and produces a distribution over potential responses. The LLM predictions often fail to agree well with human judges—indeed, the humans do not fully agree with one another. However, the multiple LLM distributions can be combined to predict each human judge’s annotations on all questions, including a summary question that assesses overall quality or relevance. LLM-Rubric accomplishes this by training a small feed-forward neural network that includes both judge-specific and judge-independent parameters. When evaluating dialogue systems in a human-AI information-seeking task, we find that LLM-Rubric with 9999 questions
(assessing dimensions such as naturalness, conciseness, and citation quality) predicts human judges’ assessment of overall user satisfaction, on a scale of 1–4, with RMS error <0.5absent0.5<$0.5$< 0.5, a 2×2\times2 × improvement over the uncalibrated baseline.

LLM-Rubric: A Multidimensional, Calibrated Approach 

to Automated Evaluation of Natural Language Texts†

Helia Hashemi∗ 
Jason Eisner∗ 
Corby Rosset 
Benjamin Van Durme 
Chris KedzieMicrosoft{hhashemi,jeisner,corbyrosset,ben.vandurme,chriskedzie}@microsoft.com

**footnotetext: Equal contribution.$\dagger$$\dagger$footnotetext: Code and data available at https://github.com/microsoft/llm-rubric.
\AddToShipoutPicture
*

1 Introduction

Many fields that must assess large numbers of short documents have turned to NLP-assisted workflows. For example,
lawyers conducting legal discovery must identify all relevant documents Quartararo et al. (2019)—a task also faced by journalists and historians.
Social scientists and market researchers must code survey responses (Mellon et al., 2024; enumerate.ai; ATLAS.ti).
Teachers or examiners must evaluate student writing Page (1968); Ramesh and Sanampudi (2022) and provide feedback Meyer et al. (2024).
Doctors, social workers, or public health agencies or researchers may assess an individual’s mental health or safety from their social media posts Chancellor and De Choudhury (2020); Xu et al. (2024); Al-Garadi et al. (2022) or from clinical interviews and assessments Galatzer-Levy et al. (2023).

The above settings evaluate human-authored texts. In addition, NLP developers must assess the quality of their machine-generated texts—texts that are consumed by end users, but also hidden intermediate steps in agentic workflows (such as chains of thought, tool calls, and revisions). With the recent commercialization of conversational AI, for example, it is crucial to evaluate dialogue systems during development and monitor them after deployment. Special care is needed in high-stakes settings like medical dialogue Huang et al. (2024).

Manual evaluation has long been the gold standard for assessing text, including generated text (Saphra et al., 2023; van der Lee et al., 2021).
Humans are often asked to consider multiple criteria and then provide a final assessment Hosking et al. (2023).
Humans may also be asked to produce reference answers to which other humans can compare the target text. Yet manual evaluation is expensive, time-consuming, and not without its own quality and reliability issues (Hosking et al., 2023; Liu et al., 2016; Smith et al., 2022). Because of these challenges, and the increasing abilities of large language models (LLMs) Brown et al. (2020), experimenters have recently
been eliciting ratings directly from an LLM (Chiang and Lee, 2023; Fu et al., 2023; Liu et al., 2023a; Thomas et al., 2024; ChainForge; and others). But can LLM evaluation be trusted? It solves the time, scaling, and possibly cost issues, but leaves open the problem of aligning these LLM ratings with human judgments.

Figure 1: An overview of the LLM-Rubric framework. The LLM and its prompts are fixed across texts and judges, but the calibration network weights are trained to predict the responses of various human judges.

We present a general approach to this alignment problem. We demonstrate its value for the evaluation and comparison of LLM-powered dialogue systems, in an information-seeking dialogue task (Zamani et al., 2023) similar to Lowe et al. (2015).
Evaluation in this setting is complex owing to competing factors that might affect a human judge’s assessment of the dialogue. These may include correctness of responses, accuracy and helpfulness of citations, length and complexity of responses, and more (Smith et al., 2022).

Our LLM-Rubric approach begins with a manually authored evaluation rubric. The rubric’s multiple-choice questions cover various evaluation dimensions, and it may also include a question that assesses overall quality or relevance.
Evaluating a text, such as a dialogue, then consists of two main steps: (1) for each rubric question we elicit the LLM’s probability distribution over possible responses, by prompting it with the text and the rubric question, and (2) we aggregate and calibrate these distributions with a small feed-forward network that has been trained to match the individual preferences of human judges. A high-level overview of LLM-Rubric is shown in Figure1.

For research in generative NLP, once the rubric and LLM are fixed, LLM-Rubric can be used like other metrics (Bleu, Rouge, etc.) to drive system development, monitor quality, demonstrate the value of a new technique, and conduct competitions. In our dialogue evaluation experiments, each user–AI dialogue is evaluated by 3 trained annotators (randomly drawn from a larger pool) who each answered the same 9 rubric questions. Our method uses these data to train an automatic LLM-based evaluator, without treating the 24 human annotators as interchangeable.
Overall, we find111See Table1, right side, rows 3, 4, and 6. that

•

Personalized calibration of an LLM evaluator of overall satisfaction on <<<750750750750 synthetic dialogues significantly improves its prediction of human judgments and correlations with human judgments, but still works poorly.

•

Incorporating LLM evaluations of 8888 additional criteria (LLM-Rubric) improves these metrics by over 2×2\times2 × over the uncalibrated LLM.

Accurate automated text assessment could replace human assessment in many other settings, such as those reviewed at the start of this paper. It could also be used in new settings where human assessment was never feasible. In AI-powered user interfaces, instantaneous scoring of user-written text can feed into downstream decisions such as providing writing feedback or deciding how to proceed with a dialogue.
An AI reasoning engine may internally apply a rubric to assess the validity of a proposed natural-language reasoning step Weir et al. (2024).
When processing a large document collection, an LLM can be used to assess the compatibility of two text passages Zhang et al. (2023); Viswanathan et al. (2023); Choi and Ferrara (2024), potentially in a more nuanced way than vector similarity; this problem arises in workflows for matching, routing, clustering, and fact-checking (Charlin and Zemel, 2013; Harman, 1996; and the papers just mentioned).
Finally, automated assessments could provide signals for training text generation Keskar et al. (2019); Tambwekar et al. (2019); Bai et al. (2022).

To allow LLM-Rubric to support all of these use cases, we release general code along with the datasets we created for this paper (see URL on page 1). We discuss limitations at the end of the paper.

Figure 2: Our calibration network learns how different human judges use the response range 1–4. Each black curve shows a different judge’s distribution of responses to the “overall satisfaction” question Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT on our synthetic conversation dataset. (We show the judges who evaluated ≥30absent30\geq 30≥ 30 conversations.) The corresponding gray curve shows the average distribution predicted for that judge on the same dialogues by
LLM-Rubric (using cross-validation). The final curve in light gray shows the original uncalibrated distribution of responses to Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT by the LLM (gpt-3.5-turbo-16k).

2 The LLM-Rubric Method

It is challenging to model human preferences in a combinatorial space such as text. Reasonable human judges may differ Aroyo and Welty (2015) on (1) what textual properties they happen to prefer (e.g., concise vs. detailed, formal vs. informal, novice vs. expert audience), (2) how they combine multiple preferences into an overall assessment, and (3) how they convey that assessment through a numerical score. Figure2 shows that in our dataset (§3), different human judges indeed have very different marginal distributions of overall score. Clearly these cannot all be matched by a judge-independent system (e.g., the LLM shown at the lower right of Figure2).

To expose the different properties and preferences at play, we ask the human judges a series of finer-grained questions about different evaluation criteria. It is already common in practical settings (§1) to at least mention such criteria in instructions to human judges. We use the same questions to query an LLM,222It is convenient to use the same questions, as we have already crafted them. However, different or additional questions could in principle be used—or multiple variants of each question, or multiple LLMs. This could potentially provide more useful evidence to the calibration network below, at the cost of slowing down evaluation and at the risk of overfitting.
and train a calibration network to jointly adjust the LLM’s scores to match the scores of any given human judge. We refer to this methodology as LLM-Rubric. The gray curves in Figure2 show that on held-out dialogues, the calibrated overall score is now distributed like that of the given judge. We will see later that these scores are also more accurate on the individual dialogues.

In this section,
we present LLM-Rubric in a general way, but for concreteness, we also introduce details of our specific experimental setup.

Evaluation Rubric Construction.

We wrote 8888 dialogue evaluation questions (Q1,…,Q8subscript𝑄1…subscript𝑄8Q_{1},\ldots,Q_{8}italic_Q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT)
inspired by
the NLG evaluation literature Zhou et al. (2022); van der Lee et al. (2021). These questions are shown in AppendixC. They
address various dimensions such as naturalness, relevance, attribution, citation quality, and conciseness.
Our final question (Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT) asked the judge to assess the overall quality of the dialogue (in this case, focusing only on whether the user would be satisfied), on a Likert scale of 1–4.
Each question stated its allowed multiple-choice responses (usually scores 1–4, with a meaning provided for each score).

Multi-Dimensional Evaluation with LLMs.

We use an LLM to evaluate a given text T𝑇Titalic_T (in our case, a dialogue transcript).
For each question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT (0≤i≤80𝑖80\leq i\leq 80 ≤ italic_i ≤ 8 in our case),
we instruct the LLM to generate a label yi∈𝒴isubscript𝑦𝑖subscript𝒴𝑖y_{i}\in\mathcal{Y}_{i}italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT, where 𝒴isubscript𝒴𝑖\mathcal{Y}_{i}caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT is the
set of allowed responses to Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT (e.g., {‘‘1’’,‘‘2’’,‘‘3’’,‘‘4’’}‘‘1’’‘‘2’’‘‘3’’‘‘4’’\{\texttt{``1''},\texttt{``2''},\texttt{``3''},\texttt{``4''}\}{ ‘‘1’’ , ‘‘2’’ , ‘‘3’’ , ‘‘4’’ }).
Specifically, we prompt it with a preamble, the text T𝑇Titalic_T, and the question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT, where Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT also specifies the allowed responses 𝒴isubscript𝒴𝑖\mathcal{Y}_{i}caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT (see AppendixD).
We chose to do this independently for each question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT to avoid confounding the LLM’s responses. We thus obtain pLLM⁢(yi∣T,Qi)subscript𝑝LLMconditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖p_{\mathrm{LLM}}(y_{i}\mid T,Q_{i})italic_p start_POSTSUBSCRIPT roman_LLM end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) for all questions Q0,…,Q8subscript𝑄0…subscript𝑄8Q_{0},\dots,Q_{8}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , … , italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT and each possible response
yi∈𝒴isubscript𝑦𝑖subscript𝒴𝑖y_{i}\in\mathcal{Y}_{i}italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT.333The LLM also allocates some probability to responses outside 𝒴isubscript𝒴𝑖\mathcal{Y}_{i}caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT, so Zi=def∑yi∈𝒴ipLLM⁢(yi∣T,Qi)<1superscriptdefsubscript𝑍𝑖subscriptsubscript𝑦𝑖subscript𝒴𝑖subscript𝑝LLMconditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖1Z_{i}\mathrel{\stackrel{{\scriptstyle\textnormal{def}}}{{=}}}\sum_{y_{i}\in%
\mathcal{Y}_{i}}p_{\mathrm{LLM}}(y_{i}\mid T,Q_{i})<1italic_Z start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_RELOP SUPERSCRIPTOP start_ARG = end_ARG start_ARG def end_ARG end_RELOP ∑ start_POSTSUBSCRIPT italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT italic_p start_POSTSUBSCRIPT roman_LLM end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) < 1. We do not normalize the probabilities by Zisubscript𝑍𝑖Z_{i}italic_Z start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT before presenting them to the calibration network. This allows our calibration network, in principle, to notice when Zi≪1much-less-thansubscript𝑍𝑖1Z_{i}\ll 1italic_Z start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ≪ 1 and to learn not to rely on the LLM’s answer to Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT in such cases. In practice, however, our prompts result in Zisubscript𝑍𝑖Z_{i}italic_Z start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT being very close to 1.

Aggregated Evaluation with Personalized Calibration.

We then use a small feed-forward calibration network (Figure1 and equations3–5 below) to map this collection of LLM probabilities pLLM⁢(yi∣T,Qi)subscript𝑝LLMconditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖p_{\mathrm{LLM}}(y_{i}\mid T,Q_{i})italic_p start_POSTSUBSCRIPT roman_LLM end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) to a collection of adjusted probabilities p^a⁢(yi∣T,Qi)subscript^𝑝𝑎conditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖\hat{p}_{a}(y_{i}\mid T,Q_{i})over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) that predict the responses of a particular judge a𝑎aitalic_a. Note that each p^a⁢(yi∣T,Qi)subscript^𝑝𝑎conditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖\hat{p}_{a}(y_{i}\mid T,Q_{i})over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) is predicted from the LLM’s behavior on all questions about T𝑇Titalic_T, not just Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT. This design lets the calibration network inspect some additional properties of T𝑇Titalic_T that might influence a𝑎aitalic_a’s response to Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT.444In the future, for this reason, the calibration network’s input could also include an embedding of the full text T𝑇Titalic_T. This design also
extends to the case where the LLM was not asked the specific question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT for which we are predicting a𝑎aitalic_a’s response (see footnote2).

We train the calibration network by maximum likelihood (regularized by early stopping). That is, given a dataset 𝒟𝒟\mathcal{D}caligraphic_D of annotations, we maximize555This formula models the yiasuperscriptsubscript𝑦𝑖𝑎y_{i}^{a}italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT for different i𝑖iitalic_i as conditionally independent given T𝑇Titalic_T. This assumption could be relaxed. For example, perhaps all of the yiasuperscriptsubscript𝑦𝑖𝑎y_{i}^{a}italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT should be made to also depend on a latent variable, e.g., judge a𝑎aitalic_a’s mood while annotating T𝑇Titalic_T.
∑(T,i,a,yia)∈𝒟log⁡p^a⁢(yia∣T,Qi)subscript𝑇𝑖𝑎superscriptsubscript𝑦𝑖𝑎𝒟subscript^𝑝𝑎conditionalsuperscriptsubscript𝑦𝑖𝑎𝑇subscript𝑄𝑖\sum_{(T,i,a,y_{i}^{a})\in\mathcal{D}}\log\hat{p}_{a}(y_{i}^{a}\mid T,Q_{i})∑ start_POSTSUBSCRIPT ( italic_T , italic_i , italic_a , italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ) ∈ caligraphic_D end_POSTSUBSCRIPT roman_log over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )(1)
where (T,i,a,yia)∈𝒟𝑇𝑖𝑎superscriptsubscript𝑦𝑖𝑎𝒟(T,i,a,y_{i}^{a})\in\mathcal{D}( italic_T , italic_i , italic_a , italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ) ∈ caligraphic_D means that judge a𝑎aitalic_a answered Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT on T𝑇Titalic_T with response yiasuperscriptsubscript𝑦𝑖𝑎y_{i}^{a}italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT.

Decoding.

Given a new text T𝑇Titalic_T, the trained calibration network predicts any judge a𝑎aitalic_a’s possible responses to question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT via the distributionp^a⁢(yi∣T,Qi)subscript^𝑝𝑎conditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖\hat{p}_{a}(y_{i}\mid T,Q_{i})over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ). If we wish to output a single predicted value y^iasuperscriptsubscript^𝑦𝑖𝑎\hat{y}_{i}^{a}over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT for downstream use, then we also need a decoding principle that extracts y^iasuperscriptsubscript^𝑦𝑖𝑎\hat{y}_{i}^{a}over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT from p^asubscript^𝑝𝑎\hat{p}_{a}over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT. In our experiments, actual responses yiasuperscriptsubscript𝑦𝑖𝑎y_{i}^{a}italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT are integers, predictions y^iasuperscriptsubscript^𝑦𝑖𝑎\hat{y}_{i}^{a}over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT are real numbers, and we will be evaluating the predictions by L2subscript𝐿2L_{2}italic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT loss, (y^ia−yia)2superscriptsuperscriptsubscript^𝑦𝑖𝑎superscriptsubscript𝑦𝑖𝑎2(\hat{y}_{i}^{a}-y_{i}^{a})^{2}( over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT - italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ) start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT.666This setup treats the integers as falling on an interval scale, not just an ordinal scale. For example, outputting 1.4 when the true answer is 1 is considered exactly as bad as outputting 2.6 when the true answer is 3. This is not always appropriate. Thus, our principle is to minimize the expectedL2subscript𝐿2L_{2}italic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT loss (our “Bayes risk”). This is accomplished simply by predicting the mean of distribution p^asubscript^𝑝𝑎\hat{p}_{a}over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT,
y^iasuperscriptsubscript^𝑦𝑖𝑎\displaystyle\hat{y}_{i}^{a}over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT=∑yi∈𝒴ip^a⁢(yi∣T,Qi)⋅yiabsentsubscriptsubscript𝑦𝑖subscript𝒴𝑖⋅subscript^𝑝𝑎conditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖subscript𝑦𝑖\displaystyle=\sum_{y_{i}\in\mathcal{Y}_{i}}\hat{p}_{a}(y_{i}\mid T,Q_{i})%
\cdot y_{i}= ∑ start_POSTSUBSCRIPT italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) ⋅ italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT(2)

We remark that we could have constructed a network that directly predicted the y^iasuperscriptsubscript^𝑦𝑖𝑎\hat{y}_{i}^{a}over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT values, and trained it to minimize L2subscript𝐿2L_{2}italic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT loss on training data—a regression problem. However, by modeling the entire distribution p^asubscript^𝑝𝑎\hat{p}_{a}over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT and not just its mean, we make fuller use of the training data for representation learning—our representations are trained to be able to predict the full distribution. Indeed, we found in pilot experiments that our method slightly outperforms the regression method. Furthermore, modeling p^asubscript^𝑝𝑎\hat{p}_{a}over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT lets us report our predictive uncertainty—e.g., the entropy or variance of p^a⁢(yi∣T,Qi)subscript^𝑝𝑎conditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖\hat{p}_{a}(y_{i}\mid T,Q_{i})over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) and not just its expectation y^iasuperscriptsubscript^𝑦𝑖𝑎\hat{y}_{i}^{a}over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT. Finally, equation2 nicely guarantees that 1≤y^ia≤41superscriptsubscript^𝑦𝑖𝑎41\leq\hat{y}_{i}^{a}\leq 41 ≤ over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ≤ 4 on any example.

Calibration Network Architecture.

Our network’s input is a feature vector
𝐱=[pLLM(yi∣T,Qi):i∈{0,…,8},yi∈𝒴i]\mathbf{x}=\left[p_{\mathrm{LLM}}(y_{i}\mid T,Q_{i}):i\in\{0,\ldots,8\},y_{i}%
\in\mathcal{Y}_{i}\right]bold_x = [ italic_p start_POSTSUBSCRIPT roman_LLM end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) : italic_i ∈ { 0 , … , 8 } , italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ]. These are already extremely high-level text features, extracted by the LLM.
We next use a feed-forward neural net to transform 𝐱𝐱\mathbf{x}bold_x into a representation 𝐳2∈ℝh2subscript𝐳2superscriptℝsubscriptℎ2\mathbf{z}_{2}\in\mathbb{R}^{h_{2}}bold_z start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT:
𝐳1subscript𝐳1\displaystyle\mathbf{z}_{1}bold_z start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT=σ⁢((W1+W1a)⁢[1;𝐱])∈ℝh1absent𝜎subscript𝑊1superscriptsubscript𝑊1𝑎1𝐱superscriptℝsubscriptℎ1\displaystyle=\sigma\big{(}\left(W_{1}+W_{1}^{a}\right)[1;\mathbf{x}]\big{)}%
\in\mathbb{R}^{h_{1}}= italic_σ ( ( italic_W start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + italic_W start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ) [ 1 ; bold_x ] ) ∈ blackboard_R start_POSTSUPERSCRIPT italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT(3)𝐳2subscript𝐳2\displaystyle\mathbf{z}_{2}bold_z start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT=σ⁢((W2+W2a)⁢[1;𝐳1])∈ℝh2absent𝜎subscript𝑊2superscriptsubscript𝑊2𝑎1subscript𝐳1superscriptℝsubscriptℎ2\displaystyle=\sigma\big{(}\left(W_{2}+W_{2}^{a}\right)[1;\mathbf{z}_{1}]\big{%
)}\in\mathbb{R}^{h_{2}}= italic_σ ( ( italic_W start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT + italic_W start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ) [ 1 ; bold_z start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ] ) ∈ blackboard_R start_POSTSUPERSCRIPT italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT(4)
Here W1,W1a∈ℝh1×(1+9)subscript𝑊1superscriptsubscript𝑊1𝑎superscriptℝsubscriptℎ119W_{1},W_{1}^{a}\in\mathbb{R}^{h_{1}\times(1+9)}italic_W start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_W start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT × ( 1 + 9 ) end_POSTSUPERSCRIPT and W2,W2a∈ℝh2×(1+h1)subscript𝑊2superscriptsubscript𝑊2𝑎superscriptℝsubscriptℎ21subscriptℎ1W_{2},W_{2}^{a}\in\mathbb{R}^{h_{2}\times(1+h_{1})}italic_W start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , italic_W start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT × ( 1 + italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) end_POSTSUPERSCRIPT. The parameters Wksubscript𝑊𝑘W_{k}italic_W start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT are shared across all judges while Wkasuperscriptsubscript𝑊𝑘𝑎W_{k}^{a}italic_W start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT are judge-specific.

The learned representations 𝐳2subscript𝐳2\mathbf{z}_{2}bold_z start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT are shared across all questions. For each i∈{0,…,8}𝑖0…8i\in\{0,\ldots,8\}italic_i ∈ { 0 , … , 8 }, we obtain {p^a⁢(yi∣T,Qi):yi∈𝒴i}:subscript^𝑝𝑎conditionalsubscript𝑦𝑖𝑇subscript𝑄𝑖subscript𝑦𝑖subscript𝒴𝑖\{\hat{p}_{a}(y_{i}\mid T,Q_{i}):y_{i}\in\mathcal{Y}_{i}\}{ over^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) : italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT } as a probability vector
softmax⁢((Vi+Via)⁢[1;𝐳2])∈ℝ|𝒴i|softmaxsubscript𝑉𝑖superscriptsubscript𝑉𝑖𝑎1subscript𝐳2superscriptℝsubscript𝒴𝑖\mathrm{softmax}(\left(V_{i}+V_{i}^{a}\right)[1;\mathbf{z}_{2}])\in\mathbb{R}^%
{|\mathcal{Y}_{i}|}roman_softmax ( ( italic_V start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT + italic_V start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ) [ 1 ; bold_z start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ] ) ∈ blackboard_R start_POSTSUPERSCRIPT | caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT | end_POSTSUPERSCRIPT(5)
The collection of matrices Vi∈ℝ|𝒴i|×(1+h2)subscript𝑉𝑖superscriptℝsubscript𝒴𝑖1subscriptℎ2V_{i}\in\mathbb{R}^{|\mathcal{Y}_{i}|\times(1+h_{2})}italic_V start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT | caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT | × ( 1 + italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) end_POSTSUPERSCRIPT can be implemented as a 3D tensor V𝑉Vitalic_V (padding Visubscript𝑉𝑖V_{i}italic_V start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT with extra rows when |𝒴i|subscript𝒴𝑖|\mathcal{Y}_{i}|| caligraphic_Y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT | is small).

Multi-Task Learning.

Our calibration network performs multi-task learning: each rubric question is a different task. When the accurate prediction of y0asubscriptsuperscript𝑦𝑎0y^{a}_{0}italic_y start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT is our main task, the other tasks serve only as regularizing auxiliary tasks, which help training to discover useful hidden features 𝐳2subscript𝐳2\mathbf{z}_{2}bold_z start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT. The weighting of the auxiliary tasks could be dynamically adapted during training (using a validation set), for example with the AuxiNash training algorithm Shamsian et al. (2023).
However, we currently use a simpler, faster shortcut that divides training into two phases.
In the pre-training phase, we optimize the full log-likelihood objective 1. This learns useful initial representations.777However, in contrast to AuxiNash, this shortcut does not try to identify and favor more useful auxiliary tasks. Equation1 simply weights each question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT in proportion to its number of annotated answers in the training dataset 𝒟𝒟\mathcal{D}caligraphic_D. (In our experiments, all questions are equally represented in 𝒟𝒟\mathcal{D}caligraphic_D.) In the fine-tuning phase, we continue training with a modified objective that sums over only the tuples in 𝒟𝒟\mathcal{D}caligraphic_D with i=0𝑖0i=0italic_i = 0. This adjusts the parameters to focus on the main task—predicting responses y0asuperscriptsubscript𝑦0𝑎y_{0}^{a}italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT to Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT. In both phases, we use early stopping to avoid overfitting.888We also tried a variant where pre-training was itself divided into two stages and we fixed Wka=0superscriptsubscript𝑊𝑘𝑎0W_{k}^{a}=0italic_W start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT = 0 and Via=0superscriptsubscript𝑉𝑖𝑎0V_{i}^{a}=0italic_V start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT = 0 during the first stage. This was intended to prevent overfitting of these judge-specific parameters, but we observed no improvement compared to the simpler method.

Using the Predictions.

Since LLM-Rubric can predict any judge’s scores on a new text T𝑇Titalic_T, how should it be used in practice? In AppendixA, we propose approaches to score aggregation, system quality monitoring, and other practical issues.

Future Extensions.

The idea of a calibration network is quite general and can easily be extended to various types of human and LLM ratings. In AppendixB, we sketch some natural extensions that were not needed in this paper’s experiments.

3 Data

Conversational AI systems are now being widely deployed. To test our methods on dialogue evaluation, we invest in developing both synthetic and real datasets of human–AI conversations.

We focus on
English information-seeking dialogues in the “IT help” (enterprise information technology) domain Lowe et al. (2015); Carletta et al. (2005).
As in many real world domains, dialogue data here is often proprietary to the system owner and/or private to the user.
Acquiring experimental access to live systems for evaluation is even more difficult. Thus, we build and evaluate several LLM-powered dialogue systems, which differ in their ability to search a corpus of websites related
to Microsoft Azure999https://azure.microsoft.com/ help topics.

For training data, we generate a corpus of synthetic dialogues with simulated users, and have human judges rate them. Collecting these artificial dialogues is efficient, since judges only have to annotate conversations and not interact with the systems first.
For our final test data, we have our judges actually interact with the live systems as users and then annotate their own dialogues.
All of our judges are professional annotators.

To mine the topics for both synthetic and live evaluation, we use real user queries and click data from a large commercial web search engine,
which further increases the realism of our experiments.

Below, §3.1 explains how we compile a corpus of background documents and how we select topics to ensure that the generated and collected conversations are diverse and are indeed information-seeking, rather than navigational or transactional. §§3.2 and 3.3 explain our approaches to synthetic dialogue generation and real dialogue collection.

3.1 Mining Topics for RAG

To simulate or collect diverse information-seeking dialogues, we need to know
what information our users will seek.
We picked an arbitrary IT help topic, Azure, for which many answers can be found on the subreddit r/azure. We hypothesize that search queries are enterprise information-seeking topics related to Azure if they lead to satisfactory clicks on the Azure subreddit.101010A satisfactory click in a search engine is defined as a click that leads to a dwell time longer than a given threshold (Jiang and Allan, 2016). Here we use a threshold of 30303030 seconds. Using this heuristic to help filter query logs obtained from the Bing search engine, we construct a set 𝒮𝒮\mathcal{S}caligraphic_S of 2275227522752275 common English queries about Azure. We will use these as topics to prompt the creation of
realistic and diverse conversations.

Some of our dialogue systems will condition their responses on relevant documents, as in retrieval-augmented generation (RAG) Lewis et al. (2020).
To build a corpus of potentially relevant documents, we mined and crawled all 37982379823798237982 clicked URLs in
the web search engine’s results
to the queries in 𝒮𝒮\mathcal{S}caligraphic_S. This includes but is not limited to the Azure subreddit URLs.
We discard the ones that require login, are behind a paywall, or are no longer available (broken links). To ensure that the URLs are of high quality, we also make sure they exist in Clueweb 2022 Set B (Overwijk et al., 2022) top 200M most popular URLs. After filtering, we arrived at 23243232432324323243 unique webpages. We used BeautifulSoup to convert each webpage’s title and body into a plain text document, without any truncation.
The mean document length
is 1246±1651uncertain124616511246\pm 1651start_ARG 1246 end_ARG ± start_ARG 1651 end_ARG words (denoting mean ±plus-or-minus\pm± standard deviation).

3.2 Synthetic Dialogue Generation

To generate synthetic dialogues in English of varying quality, we use 5 different LLM-based approaches (DS1–DS5), described in AppendixF.
These approaches have different levels of access to the document corpus. Also, the true topic (which is always provided to the simulated user) is only revealed to the dialogue system in DS1–DS3.

We use gpt-3.5-turbo-16k with its default parameters (OpenAI, 2024) for all of our data generation (§3.2, §3.3) and rubric-based evaluation (§4).

We randomly selected 50505050 topics, and used each of the systems DS1–DS5 to generate a synthetic conversation on that topic, resulting in 250250250250 unique dialogues of varying quality. Each dialogue was evaluated by 3333 judges (randomly assigned from a pool of 24242424 judges), resulting in 741741741741
personalized data points for dialogue evaluation after some guardrail quality checks (see AppendixG). The average judge annotated 30.95±13.02uncertain30.9513.0230.95\pm 13.02start_ARG 30.95 end_ARG ± start_ARG 13.02 end_ARG dialogues.

3.3 Real Dialogue Collection and Evaluation

To obtain more realistic data for evaluation, we collect conversations with DS1–DS3 where the user turns are not generated by the LLM but by a real human. The assistant in these three systems may be summarized as “no RAG” (DS1), “oracle RAG based on the topic” (DS2), and “BM25 RAG based on the topic” (DS3).

The human who plays the user role in the dialogue then also serves as the judge for that dialogue, making them particularly well qualified to judge overall user satisfaction Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT.
Details about the web interface and instructions to the humans can be found in AppendixH.

We collected a total of 223223223223 evaluated human conversations by having 13 of the original 24 judges converse with systems DS1–DS3 (some judges were no longer available). Each judge engaged in and annotated 17.15±3.41uncertain17.153.4117.15\pm 3.41start_ARG 17.15 end_ARG ± start_ARG 3.41 end_ARG dialogues on average. The evaluations are summarized in AppendixI.

Synthetic ConversationsReal Human-Agent ConversationsModelRMSE ↓↓\downarrow↓P’s ρ𝜌\rhoitalic_ρ↑↑\uparrow↑S’s ρ𝜌\rhoitalic_ρ↑↑\uparrow↑K’s τ𝜏\tauitalic_τ↑↑\uparrow↑RMSE ↓↓\downarrow↓P’s ρ𝜌\rhoitalic_ρ↑↑\uparrow↑S’s ρ𝜌\rhoitalic_ρ↑↑\uparrow↑K’s τ𝜏\tauitalic_τ↑↑\uparrow↑1Random Eval1.4990.002-0.003-0.0031.4270.0110.0060.0052Argmax LLM Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT0.98410.15310.16110.14711.18610.10610.12310.12013Expected LLM Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT0.856120.18210.21710.16810.901120.14310.14110.13814Calibrated LLM Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT0.8011230.198120.19610.193120.7841230.2111230.2181230.1921235FActScore (Min et al., 2023)–0.204120.21110.20012–0.2161230.2181230.2071236LLM-Rubric0.3961234e0.40112345e0.39812345e0.39312345e0.42212340.350123450.347123450.33112345\hdashlineaOracle0.237*bcdef0.611*bcdef0.626*bcdef0.605*bcdef0.289*bcd0.717*bcd0.711*bcd0.675*bcdb   w/o LLM probs0.276*cef0.551*cef0.548*cef0.533*cef0.357*c0.625*c0.629*c0.599*cc   w/o Personalized Calibration0.401e0.476*e0.471*e0.468*e0.389*0.582*0.587*0.565*d↳↳\drsh↳ + Personalized isotonic regress0.273*cef0.521*cef0.526*cef0.519*cef0.302*bc0.650*bc0.653*bc0.644*bceDepersonalized Oracle0.4920.3620.3550.338––––f↳↳\drsh↳ + Personalized isotonic regress0.321*ce0.482*e0.485*e0.477*e––––
Table 1: Performance on predicting human judges’ Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (overall quality). We report root mean squared error (RMSE) and, more important, correlations with human judges’ responses (Pearson’s ρ𝜌\rhoitalic_ρ, Spearman’s ρ𝜌\rhoitalic_ρ, Kendall’s τ𝜏\tauitalic_τ).
Results on the synthetic conversation dataset are based on 5-fold cross-evaluation; results on the real conversations are based on training on all synthetic conversations.
The superscripts denote statistically significant improvements according to a paired permutation significance test (p<0.05)𝑝0.05(p<0.05)( italic_p < 0.05 ). The asterisk * means all methods in rows 1–6.

4 Experiments

We will evaluate how well LLM-Rubric can predict individual judges’ assessments y0asubscriptsuperscript𝑦𝑎0y^{a}_{0}italic_y start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT of our Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (overall user satisfaction). We evaluate predictions y^0asubscriptsuperscript^𝑦𝑎0\hat{y}^{a}_{0}over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT both in absolute terms (whether they achieve low root-mean-squared error, or RMSE) and in relative terms (how well y^0asubscriptsuperscript^𝑦𝑎0\hat{y}^{a}_{0}over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT correlates with y0asubscriptsuperscript𝑦𝑎0y^{a}_{0}italic_y start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT, i.e., whether y^0asubscriptsuperscript^𝑦𝑎0\hat{y}^{a}_{0}over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT can be used to rank (T,a)𝑇𝑎(T,a)( italic_T , italic_a ) pairs).

We train our calibration networks on synthetic dialogues. We then evaluate them not only on held-out synthetic dialogues but also on real dialogues, to demonstrate that the LLM scoring and its calibration can generalize from synthetic to real data.

Hyperparameter Selection.

To train a system on a given training set, we evaluate hyperparameter settings from a grid by 5-fold cross-validation on the training set, and then use the selected hyperparameters to train on the entire training set. We select the hyperparameters that maximize the main task objective, namely the log-likelihood of (held-out) annotations y0asuperscriptsubscript𝑦0𝑎y_{0}^{a}italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT. The hidden layer sizes h1,h2subscriptℎ1subscriptℎ2h_{1},h_{2}italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT each range over {10,25,50,100}102550100\{10,25,50,100\}{ 10 , 25 , 50 , 100 }, the batch size ranges over {32,64,128,256}3264128256\{32,64,128,256\}{ 32 , 64 , 128 , 256 }, the learning rate of the Adam optimizer ranges over {0.00001,0.00005,0.0001,0.0005,0.001,0.005,\{0.00001,0.00005,0.0001,0.0005,0.001,0.005,{ 0.00001 , 0.00005 , 0.0001 , 0.0005 , 0.001 , 0.005 ,0.01}0.01\}0.01 }, and the numbers of epochs for pre-training and fine-tuning each range over {5,10,20,30,40,50}51020304050\{5,10,20,30,40,50\}{ 5 , 10 , 20 , 30 , 40 , 50 }.111111Instead of including the number of epochs in the hyperparameter grid search, an alternative would be to use a standard early stopping heuristic at each phase, by evaluating that phase’s training objective periodically on held-out data.

Synthetic Data Evaluation.

We test our calibration network on all 741 synthetic dialogues, using 5-fold cross-validation; the dataset is split at the dialogue level so that each dialogue appears in only one fold. Different folds may select different evaluation hyperparameters, resulting in different architectures for the calibration network.121212When training on 4 folds to evaluate the 5th, we select the hyperparameters by an inner 5-fold cross-validation on this training set of about 593 examples, as explained above.

Real Data Evaluation.

We test our calibration network on all 223 real dialogues, after training on all of the synthetic dialogues (again selecting hyperparameters by 5-fold cross-validation).

Baseline Methods.

As Table1 shows, we compare LLM-Rubric to these 5555 baselines:

1.

Random. For each dialogue independently, we produce 1, 2, 3, or 4 uniformly at random.

2.

Argmax LLM Q𝟎subscript𝑄0\boldsymbol{Q_{0}}bold_italic_Q start_POSTSUBSCRIPT bold_0 end_POSTSUBSCRIPT. We use the top LLM prediction for Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT: argmaxy0∈𝒴0pLLM⁢(y0∣T,Q0)subscriptargmaxsubscript𝑦0subscript𝒴0subscript𝑝LLMconditionalsubscript𝑦0𝑇subscript𝑄0\operatorname*{argmax}_{y_{0}\in\mathcal{Y}_{0}}p_{\mathrm{LLM}}(y_{0}\mid T,Q%
_{0})roman_argmax start_POSTSUBSCRIPT italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUBSCRIPT italic_p start_POSTSUBSCRIPT roman_LLM end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ). Note that this system always produces an integer.131313In a pilot experiment, we found no significant improvement from few-shot prompting.

3.

Expected LLM Q𝟎subscript𝑄0\boldsymbol{Q_{0}}bold_italic_Q start_POSTSUBSCRIPT bold_0 end_POSTSUBSCRIPT. We use the expected value of the LLM’s prediction for Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT: ∑y0∈𝒴0y0⋅pLLM⁢(y0∣T,Q0)/Z0subscriptsubscript𝑦0subscript𝒴0⋅subscript𝑦0subscript𝑝LLMconditionalsubscript𝑦0𝑇subscript𝑄0subscript𝑍0\sum_{y_{0}\in\mathcal{Y}_{0}}y_{0}\cdot p_{\mathrm{LLM}}(y_{0}\mid T,Q_{0})/Z%
_{0}∑ start_POSTSUBSCRIPT italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUBSCRIPT italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ⋅ italic_p start_POSTSUBSCRIPT roman_LLM end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ) / italic_Z start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (where Z0subscript𝑍0Z_{0}italic_Z start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT normalizes the probabilities over 𝒴0subscript𝒴0\mathcal{Y}_{0}caligraphic_Y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT—see footnote3).

4.

Calibrated LLM Q𝟎subscript𝑄0\boldsymbol{Q_{0}}bold_italic_Q start_POSTSUBSCRIPT bold_0 end_POSTSUBSCRIPT. An ablated version of LLM-Rubric that uses only Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT, i.e., the feature vector 𝐱=[p~⁢(y0∣T,Q0)∣y0∈𝒴0]𝐱delimited-[]conditional~𝑝conditionalsubscript𝑦0𝑇subscript𝑄0subscript𝑦0subscript𝒴0\mathbf{x}=\left[\tilde{p}(y_{0}\mid T,Q_{0})\mid y_{0}\in\mathcal{Y}_{0}\right]bold_x = [ over~ start_ARG italic_p end_ARG ( italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ) ∣ italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ]
is restricted to the Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT answer probabilities.
We train and evaluate the calibration network just as for LLM-Rubric, including cross-validation and hyperparameter selection.

5.

FActScore(Min et al., 2023). This is a recent retrieval-based automatic evaluator141414https://github.com/shmsw25/FActScore that predicts the percentage of factually correct sentences as the overall evaluation score. We use the Azure corpus described in §3.1 as the retrieval corpus in FActScore, which performs better than the default Wikipedia corpus.

Oracle Methods.

Table1 also shows upper bounds on performance.
The Oracle system is the same as LLM-Rubric, but the calibration network’s input 𝐱𝐱\mathbf{x}bold_x—at both training and test time—includes the judge’s actual response to each question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT (except for Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT, which we aim to predict!) as a four-dimensional one-hot vector, in addition to the LLM response vector pLLM⁢(y0∣T,Qi)subscript𝑝LLMconditionalsubscript𝑦0𝑇subscript𝑄𝑖p_{\mathrm{LLM}}(y_{0}\mid T,Q_{i})italic_p start_POSTSUBSCRIPT roman_LLM end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ).

We ablate different components of the Oracle model by withholding the LLM response vector from the model input and by depersonalizing the calibration network (Oracle w/o Personalized Calibration) by dropping Wkasuperscriptsubscript𝑊𝑘𝑎W_{k}^{a}italic_W start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT. To restore a judge a𝑎aitalic_a’s idiosyncratic distribution of Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT scores (Figure2),
without restoring their idiosyncratic computation of Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT from other dimensions, we try correcting the output of the depersonalized calibration network using an a𝑎aitalic_a-specific isotonic regression model.

Our Depersonalized Oracle is similar to the Oracle, but instead of using the responses of the actual target judge a𝑎aitalic_a, it uses the distribution of responses of all other judges (averaging their one-hot vectors), holding out the target judge.151515We cannot run this on the real conversation dataset, where each dialogue is annotated only by a single judge.
It also drops the personalized weights Wkasuperscriptsubscript𝑊𝑘𝑎W_{k}^{a}italic_W start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT.

Thus, the Oracle provides a rough upper bound on LLM-Rubric. The Depersonalized Oracle provides a rough upper bound on a version of LLM-Rubric that produces a𝑎aitalic_a-independent results.

5 Results

A trivial baseline of predicting a constantQ0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (the overall mean from training data) achieves an RMSE of 0.82
on both synthetic and real conversations. LLM-Rubric roughly halves this (row 6 of Table1), so it explains ≈34absent34\approx\frac{3}{4}≈ divide start_ARG 3 end_ARG start_ARG 4 end_ARG of the variance in human judgments of Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT across judges a𝑎aitalic_a and texts T𝑇Titalic_T. Its predictions of Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT have tolerably low error and correlate reasonably well with those of human judges.

In sharp contrast, the LLM’s direct response to Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (row 2 or 3) does worse than the constant baseline. Even calibrating its response distribution for each judge (row 4) barely improves on the baseline, explaining only 5–10% of the variance in human judgments and achieving only ≈0.2absent0.2\approx 0.2≈ 0.2 correlation with them. This suggests that the LLM cannot help assess Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (user satisfaction) until we ask it about the finer-grained dimensions Q1subscript𝑄1Q_{1}italic_Q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT–Q8subscript𝑄8Q_{8}italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT.

The results obtained by FActScore (row 5) do not correlate any better with overall satisfaction, so percentage of factually correct sentences is also not a good indicator of overall user satisfaction. Moreover, Liu et al. (2016) showed that dialogue systems were poorly evaluated by simple metrics of lexical overlap with human responses.

ModelRMSE ↓↓\downarrow↓P’s ρ𝜌\rhoitalic_ρ↑↑\uparrow↑LLM-Rubric0.4220.350   w/o fine-tuning0.493▽0.249▽   w/o pre-training0.525▽0.226▽   w/o personalization0.601▽0.198▽\hdashline w/o Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (Satisfaction)0.554▽0.287▽   w/o Q1subscript𝑄1Q_{1}italic_Q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT (Naturalness)0.463▽0.313▽   w/o Q2subscript𝑄2Q_{2}italic_Q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT (Grounding Sources)0.471▽0.279▽   w/o Q3subscript𝑄3Q_{3}italic_Q start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT (Citation Presence)0.573▽0.075▽   w/o Q4subscript𝑄4Q_{4}italic_Q start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT (Citation Suitability)0.497▽0.311▽   w/o Q5subscript𝑄5Q_{5}italic_Q start_POSTSUBSCRIPT 5 end_POSTSUBSCRIPT (Citation Optimality)0.506▽0.192▽   w/o Q6subscript𝑄6Q_{6}italic_Q start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT (Redundancy)0.4240.348   w/o Q7subscript𝑄7Q_{7}italic_Q start_POSTSUBSCRIPT 7 end_POSTSUBSCRIPT (Conciseness)0.532▽0.254▽   w/o Q8subscript𝑄8Q_{8}italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT (Efficiency)0.510▽0.161▽Table 2: Predicting Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT: Ablation study on real conversation data for each design decision in our calibration network (top) and each rubric dimension (bottom). ▽ denotes a statistically significant performance drop from the full LLM-Rubric (p<0.05𝑝0.05p<0.05italic_p < 0.05).Expected LLM Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPTLLM-RubricRMSE ↓↓\downarrow↓P’s ρ𝜌\rhoitalic_ρ↑↑\uparrow↑RMSE ↓↓\downarrow↓P’s ρ𝜌\rhoitalic_ρ↑↑\uparrow↑Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT0.9010.1430.422∗0.350∗Q1subscript𝑄1Q_{1}italic_Q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT1.0330.1770.637∗0.318∗Q2subscript𝑄2Q_{2}italic_Q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT0.7990.1400.543∗0.265∗Q3subscript𝑄3Q_{3}italic_Q start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT0.7960.3470.532∗0.511∗Q4subscript𝑄4Q_{4}italic_Q start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT0.9190.1660.706∗0.494∗Q5subscript𝑄5Q_{5}italic_Q start_POSTSUBSCRIPT 5 end_POSTSUBSCRIPT1.1040.1910.786∗0.387∗Q6subscript𝑄6Q_{6}italic_Q start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT1.7260.0300.430∗0.279∗Q7subscript𝑄7Q_{7}italic_Q start_POSTSUBSCRIPT 7 end_POSTSUBSCRIPT1.2400.0570.693∗0.318∗Q8subscript𝑄8Q_{8}italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT0.9810.0590.232∗0.249∗Table 3: How well can LLM-Rubric predict the response yisubscript𝑦𝑖y_{i}italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT to question Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT? For each row, we fine-tune LLM-Rubricon the target rubric dimension and compare to Expected LLM Qisubscript𝑄𝑖Q_{i}italic_Q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT on the real conversation data. Superscript ∗ indicates statistically significant improvement with 95% confidence (p<0.05𝑝0.05p<0.05italic_p < 0.05).

6 Analysis

Calibration.

Does our trained LLM-Rubric produce well-calibrated probability distributions for Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT (as one would expect from maximum-likelihood training)? We checked on synthetic data. It obtained excellent smECE values of <0.05absent0.05<0.05< 0.05 for each y0∈𝒴0={1,2,3,4}subscript𝑦0subscript𝒴01234y_{0}\in\mathcal{Y}_{0}=\{1,2,3,4\}italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = { 1 , 2 , 3 , 4 }, where smECE is the smoothed expected calibration error Błasiok and Nakkiran (2023).
Informally, this means that for each y0∈𝒴0subscript𝑦0subscript𝒴0y_{0}\in\mathcal{Y}_{0}italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∈ caligraphic_Y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT, when we examine the held-out examples (T,0,a,y0a)𝑇0𝑎superscriptsubscript𝑦0𝑎(T,0,a,y_{0}^{a})( italic_T , 0 , italic_a , italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT ) with p^a⁢(y0∣T,Q0)≈psubscript^𝑝𝑎conditionalsubscript𝑦0𝑇subscript𝑄0𝑝\hat{p}_{a}(y_{0}\mid T,Q_{0})\approx pover^ start_ARG italic_p end_ARG start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ∣ italic_T , italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ) ≈ italic_p, the fraction where y0a=y0superscriptsubscript𝑦0𝑎subscript𝑦0y_{0}^{a}=y_{0}italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT = italic_y start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT was in fact ≈pabsent𝑝\approx p≈ italic_p. AppendixK shows calibration plots and discusses how to use calibrated probabilities for downstream decisions.

Ablation Studies.

§5 showed that LLM responses on 8888 additional questions were useful, but was our calibration network the best way to incorporate them into our prediction of Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT? To justify each design decision, we try omitting pre-training, fine-tuning, and personalized weighting from our calibration network. The results on the real conversation data in Table2 show that predictions were improved by each step. In particular, it was indeed useful to do multi-task pre-training of the calibration network (which required human judgments on all questions) and to then fine-tune on the main task. Personalized weighting had the greatest impact.

Also, were all 8888 questions useful? We measured the impact of each question by omitting it from the evaluation rubric for the LLM-Rubric model (bottom half of Table2). All rubric dimensions contributed significantly to the Q0subscript𝑄0Q_{0}italic_Q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT prediction, except for Q6subscript𝑄6Q_{6}italic_Q start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT, which focuses on redundancy in the dialogue.
Using even more rubric dimensions might improve performance further (footnotes2 and B). That said, considering more rubric dimensions would mean more human annotations at pre-training time and/or more LLM computation.

Oracle study.

Giving LLM-Rubric access to
a judge’s true responses to Q1subscript𝑄1Q_{1}italic_Q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT–Q8subscript𝑄8Q_{8}italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT lets us see how well the judge’s overall quality score Q0subscript𝑄0Q_{0}italic_Q start

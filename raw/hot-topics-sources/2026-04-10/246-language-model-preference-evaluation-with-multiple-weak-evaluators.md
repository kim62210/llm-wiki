---
title: Language Model Preference Evaluation with Multiple Weak Evaluators
source_url: https://arxiv.org/html/2410.12869v3
final_url: https://arxiv.org/html/2410.12869v3
status: 200
content_type: text/html; charset=utf-8
topics: [Pairwise vs Pointwise Eval Protocol Bias]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:00.287397+00:00
---

# Language Model Preference Evaluation with Multiple Weak Evaluators

## 원본 URL

https://arxiv.org/html/2410.12869v3

## 추출 본문

Language Model Preference Evaluation with Multiple Weak Evaluators
1 Introduction

2 Related Work
Preference evaluation of LLMs.

Weak supervision.

3 Methodologies
3.1 Preference Graph

3.2 GED: Preference Graph Ensemble and Denoise
Graph ensemble.

Graph denoising.

Graph to ranking.

3.3 Applications
Response selection.

Model Ranking.

Model Alignment.

4 Theoretical Analysis

5 Experiments on Response Selection
Experiment Setup.

Main results.

Ablation study.

6 Experiments on Model Ranking
Experiment Setup.

Main results.

7 Experiments on Instruct Tuning
Experiment Setup.

Main results.

8 Evaluating GED on More Metrics

9 Conclusion

A Implementation Details
A.1 Experimental Setup

A.2 Details of Evaluator Selection Across Different Tasks
Response Selection.

Model Ranking.

Instruction Tuning.

A.3 Definition of Weak Evaluators

A.4 Evaluation Settings: Single Model vs. Single Evaluator

A.5 Definition of Cycle Rate

A.6 Models Used for Ranking

A.7 Dataset

A.8 Aggregation Process in GED Across Different Tasks

B Alternative Evaluator Configurations for Model Ranking

C Comparison with Point-Wise Scoring Methods

D Impact of Evaluator Quantity on Denoising Quality

E Construction of the Preference Graph

F The Importance of Addressing Cyclic Inconsistency

G Proof of Theorem 1

H Impact of Evaluator Weighting on GED Performance

I Expanded Related Work on Preference Denoising for LLMs

J Impact of Evaluator Selection on GED Performance

K Cost Considerations and Active Learning with ActiveGED

L Mitigating Evaluator Biases in GED

M Denoising of Preference Graphs for GED

N Rank ensemble method
Weight score (Adler et al., 2002)

Kemeny and weighted Kemeny (Kemeny, 1959)

Pairwise majority and weighted pairwise majority (Caragiannis et al., 2016)

O Visualization
Case Study 1.

Case Study 2.

Conclusion from Case Studies.

P Prompt Template
Prompt for Response Selection.

Prompt for Model Ranking.

Prompt for Instruct Tuning.

Language Model Preference Evaluation with Multiple Weak Evaluators

Zhengyu Hu
Jieyu Zhang
Zhihan Xiong
Alexander Ratner
Hui Xiong
Ranjay Krishna

Abstract
Despite the remarkable success of Large Language Models (LLMs), evaluating their outputs’ quality regarding preference remains a critical challenge.
Existing works usually leverage an LLM as the judge for comparing LLMs’ output pairwisely, yet such model-based evaluator is weak evaluator due to conflicting preference, i.e.,
output A is better than B, B than C, but C than A,
causing contradictory evaluation results.
To address this, we introduce GED (Preference Graph Ensemble and Denoise), a novel approach that leverages multiple model-based evaluators to construct preference graphs, and then ensemble and denoise these graphs for better, non-contradictory evaluation results.
In particular, our method consists of two primary stages: aggregating evaluations into a unified graph and applying a denoising process to eliminate cyclic inconsistencies, ensuring a directed acyclic graph (DAG) structure.
We provide theoretical guarantees for our framework, demonstrating its efficacy in recovering the ground truth preference structure.
Extensive experiments on ten benchmarks demonstrate GED’s superiority in three applications: model ranking, response selection, and model alignment tasks. Notably, GED combines small LLM evaluators (e.g., Llama3-8B, Mistral-7B, Qwen2-7B) to outperform strong ones (e.g., Qwen2-72B), showcasing its effectiveness in enhancing evaluation reliability and improving model performance.

Machine Learning, ICML

1 Introduction

Large Language Models (LLMs) have rapidly transformed various fields within artificial intelligence, particularly natural language processing (NLP) and decision-making systems (Wu et al., 2023; Li et al., 2023a).
Despite the remarkable success of LLMs, the need for effective evaluation methods becomes paramount (Liu et al., 2023; Desmond et al., 2024; Siska et al., 2024; Boyeau et al., 2024; Chatzi et al., 2024).
Preference evaluation, as one of the most important assessment methods,
plays an indispensable role in evaluating and optimizing model performance (Rafailov et al., 2024; Yuan et al., 2024; Dubois et al., 2024b).
Existing works usually leverage a powerful LLM (e.g., GPT4 (Achiam et al., 2023)) as the judge for comparing LLMs’ output pairwisely (Li et al., 2023b; Chen et al., 2023b; Wang et al., 2022).

Figure 1: 
(a) A preference graph exhibiting cyclic inconsistencies (e.g., A ≻succeeds\succ≻ B ≻succeeds\succ≻ C ≻succeeds\succ≻ A), which violate transitivity.
(b) Empirical results showing that even advanced LLMs (e.g., GPT-4-o) exhibit significant noise in preference judgments, leading to inconsistent evaluations.
(c) Overview of our proposed framework, GED, which ensembles multiple weak evaluators and applies denoising to recover a directed acyclic graph.

However, while such model-based pairwise preference evaluations offer a flexible approach, they can lead to contradictory evaluations in the assessment process (Naresh et al., 2024; Zhang et al., 2024b).
For example, an LLM might evaluate three responses and conclude that Response A is better than Response B, Response B is better than Response C, yet paradoxically also rank Response C as better than Response A.
These cyclic patterns violate the transitivity assumption of preferences established in prior work (Ouyang et al., 2022; Song et al., 2024; Hou et al., 2024; Liu et al., 2024), thereby undermining the reliability of evaluation results.
We model this conflicting preference via the preference graph.
Specifically, a preference graph is constructed with each response as a node and directed edges indicating pairwise preferences—an edge from node A to node B shows that the evaluator preferred response A over B.
The noise illustrated by cycles (A ≻succeeds\succ≻ B ≻succeeds\succ≻ C ≻succeeds\succ≻ A) manifests as loops in the preference graph.
This process is illustrated in Figure 1 (a).
Ideally, a preference graph should be structured as a directed acyclic graph (DAG) to maintain consistency.
In this paper, we define an evaluator as weak if it produces cycles into the preference graph.
As shown in Figure  1 (b), we evaluated 10 Llama3-70B (AI@Meta, 2024) responses on HumanEval (Chen et al., 2021) and MATH (Hendrycks et al., 2021) using GPT-4-o, GPT-4-o-mini, GPT-3.5 (Achiam et al., 2023), Qwen2-72B (Yang et al., 2024a), and Llama3-8B (AI@Meta, 2024) as evaluators.
Even with GPT-4-o, 64% of preference graphs in HumanEval and 38% in MATH contained cycles, highlighting persistent noise and the limitations of these models as weak evaluators.

To address this, we propose a novel framework, GED (Preference Graph Ensemble and Denoise), to address the inconsistencies in preference graphs generated through pairwise evaluations. Our method involves two key steps:
(1) ensembling multiple weak evaluators to mitigate noise introduced by individual evaluators and
(2) applying a denoising process to the resulting preference graph. By aggregating evaluations from multiple weak evaluators, we ”average out” the noise and biases, resulting in a more robust approximation of the true preference structure. The denoising step further refines this aggregated graph by removing inconsistencies, ensuring the final preference graph is more reliable for downstream tasks.
The overall process of GED is illustrated in Figure 1 (c).
We provide a theoretical analysis demonstrating the soundness of GED, showing that by treating each individual preference graph as a random perturbation of a ground truth DAG, our ensemble and denoising framework can recover the ground truth DAG with high probability.

To validate the practical efficacy of GED, we conduct extensive experiments across model ranking, response selection, and model alignment tasks, utilizing ten widely recognized benchmark datasets, including HumanEval (Chen et al., 2021), AlpacaEval (Li et al., 2023b), MATH (Hendrycks et al., 2021), GSM8k (Chen et al., 2021), GAIA (Mialon et al., 2023), LIMA (Zhou et al., 2023), Vicuna (Chiang et al., 2023), Koala (Vu et al., 2023), WizardLM (Xu et al., 2023), and Self-Instruct (Wang et al., 2022).
In these experiments, GED consistently outperformed baseline methods.
For instance, in the response selection task, GED achieved an average performance gain of 4.51% over baseline methods across multiple benchmarks.
Additionally, GED demonstrated substantial gains in scenarios where combining preference graphs from small evaluators surpassed the performance of even stronger individual evaluators.
Specifically, when using using Llama3-8B, Mistral-7B, and Qwen2-7B as evaluators, GED exceeded the performance of using the Qwen2-72B in response selection task.
These results highlight GED’s ability to mitigate preference noise, improve consistency, and enhance model performance across diverse evaluation settings.

2 Related Work

Preference evaluation of LLMs.

Reference-free evaluation metrics have a long history (Louis & Nenkova, 2013; Boyeau et al., 2024; Chatzi et al., 2024; Shankar et al., 2024; Naresh et al., 2024), which evaluates the generated text based on intrinsic properties and coherence with the context. Although they achieve high accuracy on matching inner-evaluator, the achievement suffers from spurious correlations such as perplexity and length (Durmus et al., 2022). Recently, people have started using a strong model (e.g., GPT-4) as an evaluator to perform a zero-shot reference-free evaluation on the weak models (Shen et al., 2023; Dubois et al., 2024b; Chen et al., 2023b).
However, using LLM-based preference evaluations can introduce inconsistencies in preference graphs, often resulting in cyclic preferences or contradictions when comparing multiple outputs.

Weak supervision.

The concept of weak-to-strong supervision originates from the need to leverage noisy or partial labels in machine learning tasks, enabling the development of more robust models from imperfect data (Ratner et al., 2016; Zhang et al., 2023b, 2022).
In LLMs, weak-to-strong supervision aids AI alignment by allowing weaker models to improve strong ones, enhancing performance without extensive data and supporting scalable oversight (Zheng et al., 2024a; Guo & Yang, 2024; Tong et al., 2024).
Similarly, in task-oriented LLMs, weak-to-strong learning improves LLM’s ability by enabling strong models to refine their data autonomously, boosting performance without extensive high-quality input (Zhang et al., 2023a; Yang et al., 2024b).
Through weak-to-strong supervision, LLM performance can be significantly improved by iteratively transforming low-quality labels into more reliable ones, leading to more effective model training and robust outputs (Zakershahrak & Ghodratnama, 2024; Lang et al., 2024).

3 Methodologies

In this section, we begin by defining a preference graph, which serves as the foundation for representing pairwise preferences among candidates (Section 3.1).
Building on this foundation, we introduce GED structured into three key stages
(Section 3.2):
(1) graph ensemble, where we aggregate individual preference graphs into a unified structure,
(2) graph denoising, which removes cycles and inconsistencies to ensure the preference graph is acyclic, and
(3) graph-to-ranking, where we extract a reliable ranking of candidates from the denoised graph.
Below, we provide detailed descriptions of each step.

3.1 Preference Graph

A preference graph is a directed graph GP=(V,A,w)subscript𝐺𝑃𝑉𝐴𝑤G_{P}=(V,A,w)italic_G start_POSTSUBSCRIPT italic_P end_POSTSUBSCRIPT = ( italic_V , italic_A , italic_w ), where V={v1,v2,…,vn}𝑉subscript𝑣1subscript𝑣2…subscript𝑣𝑛V=\{v_{1},v_{2},\ldots,v_{n}\}italic_V = { italic_v start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_v start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_v start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT } represents n𝑛nitalic_n candidates, A⊆V×V𝐴𝑉𝑉A\subseteq V\times Vitalic_A ⊆ italic_V × italic_V is a set of directed arcs indicating pairwise preferences, and w:A→ℝ+:𝑤→𝐴superscriptℝw:A\rightarrow\mathbb{R}^{+}italic_w : italic_A → blackboard_R start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT assigns weights to arcs, representing preference strength.

For distinct u,v∈V𝑢𝑣𝑉u,v\in Vitalic_u , italic_v ∈ italic_V, an arc (u,v)∈A𝑢𝑣𝐴(u,v)\in A( italic_u , italic_v ) ∈ italic_A exists if w⁢(u,v)>0𝑤𝑢𝑣0w(u,v)>0italic_w ( italic_u , italic_v ) > 0, where the weight w⁢(u,v)𝑤𝑢𝑣w(u,v)italic_w ( italic_u , italic_v ) aggregates individual preferences:
w⁢(u,v)=∑i=1k(si⁢(u,v)−si⁢(v,u)),𝑤𝑢𝑣superscriptsubscript𝑖1𝑘subscript𝑠𝑖𝑢𝑣subscript𝑠𝑖𝑣𝑢w(u,v)=\sum_{i=1}^{k}(s_{i}(u,v)-s_{i}(v,u)),italic_w ( italic_u , italic_v ) = ∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT ( italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ( italic_u , italic_v ) - italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ( italic_v , italic_u ) ) ,
with si⁢(u,v)subscript𝑠𝑖𝑢𝑣s_{i}(u,v)italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ( italic_u , italic_v ) representing the score from the i𝑖iitalic_i-th source. The preference graph encapsulates aggregate preferences, with arc weights reflecting cumulative strength.

3.2 GED: Preference Graph Ensemble and Denoise

Our method, GED (Preference Graph Ensemble and Denoise), begins by performing graph ensemble to aggregate a set of preference graphs. It then applies graph denoising to ensure acyclicity, followed by graph-to-ranking to derive the final node ranking. The detailed steps are as follows:

Graph ensemble.

Given k𝑘kitalic_k weighted graphs G1,…,Gksubscript𝐺1…subscript𝐺𝑘G_{1},\dots,G_{k}italic_G start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_G start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT with shared vertex set V𝑉Vitalic_V, the ensemble graph GE=(V,AE,wE)subscript𝐺𝐸𝑉subscript𝐴𝐸subscript𝑤𝐸G_{E}=(V,A_{E},w_{E})italic_G start_POSTSUBSCRIPT italic_E end_POSTSUBSCRIPT = ( italic_V , italic_A start_POSTSUBSCRIPT italic_E end_POSTSUBSCRIPT , italic_w start_POSTSUBSCRIPT italic_E end_POSTSUBSCRIPT ) is constructed by setting AE=⋃i=1kAisubscript𝐴𝐸superscriptsubscript𝑖1𝑘subscript𝐴𝑖A_{E}=\bigcup_{i=1}^{k}A_{i}italic_A start_POSTSUBSCRIPT italic_E end_POSTSUBSCRIPT = ⋃ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT italic_A start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT and defining the weight wE⁢(u,v)=∑i=1kwi⁢(u,v)subscript𝑤𝐸𝑢𝑣superscriptsubscript𝑖1𝑘subscript𝑤𝑖𝑢𝑣w_{E}(u,v)=\sum_{i=1}^{k}w_{i}(u,v)italic_w start_POSTSUBSCRIPT italic_E end_POSTSUBSCRIPT ( italic_u , italic_v ) = ∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT italic_w start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ( italic_u , italic_v ) for each arc (u,v)∈AE𝑢𝑣subscript𝐴𝐸(u,v)\in A_{E}( italic_u , italic_v ) ∈ italic_A start_POSTSUBSCRIPT italic_E end_POSTSUBSCRIPT.

Graph denoising.

Graph denoising involves transforming the original graph G=(V,A,w)𝐺𝑉𝐴𝑤G=(V,A,w)italic_G = ( italic_V , italic_A , italic_w )
into a DAG.
This transformation is achieved by identifying and removing a set of arcs known as the Feedback Arc Set (FAS) (Gabow, 1995), which is a set of arcs whose removal makes the graph acyclic.
The goal is to find a minimum FAS, denoted as R∗⁢(G)superscript𝑅𝐺R^{*}(G)italic_R start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ( italic_G ), which is a set of arcs with the smallest total weights that needs to be removed to eliminate all cycles in G𝐺Gitalic_G.
To find this minimum FAS, we can order the vertices of G𝐺Gitalic_G in a specific sequence s={v1,v2,…,vn}𝑠subscript𝑣1subscript𝑣2…subscript𝑣𝑛s=\{v_{1},v_{2},\ldots,v_{n}\}italic_s = { italic_v start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_v start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_v start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT }.
This vertex sequence induces a FAS R⁢(s)𝑅𝑠R(s)italic_R ( italic_s ), consisting of all arcs that point against the direction of the sequence, i.e., arcs vj→vi→subscript𝑣𝑗subscript𝑣𝑖v_{j}\rightarrow v_{i}italic_v start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT → italic_v start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT where j>i𝑗𝑖j>iitalic_j > italic_i.
The graph denoising problem is thus reframed as finding an optimal vertex sequence s∗superscript𝑠s^{*}italic_s start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT that induces the minimal FAS, such that R⁢(s∗)=R∗⁢(G)𝑅superscript𝑠superscript𝑅𝐺R(s^{*})=R^{*}(G)italic_R ( italic_s start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ) = italic_R start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ( italic_G ).
This optimal sequence s∗superscript𝑠s^{*}italic_s start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ensures that the total weights of arcs eliminated to achieve a DAG is minimized.

Finding a minimum FAS in general is known to be an NP-complete problem, whose computational complexity can be exponential (Karp, 2010; Bodlaender et al., 2012).
Therefore, in our experiment, we apply the well-established approximation algorithm proposed in Eades et al. (1993).
Details can be found in Appendix M.

Graph to ranking.

Given a DAG G=(V,A,w)𝐺𝑉𝐴𝑤G=(V,A,w)italic_G = ( italic_V , italic_A , italic_w ), we derive a ranking by computing the descendant count desc⁢(v)desc𝑣\text{desc}(v)desc ( italic_v ) for each vertex v𝑣vitalic_v, defined as the number of vertices reachable from v𝑣vitalic_v:
desc⁢(v)=|{u∈V:v→u}|,desc𝑣conditional-set𝑢𝑉→𝑣𝑢\text{desc}(v)=\left|\{u\in V:v\rightarrow u\}\right|,desc ( italic_v ) = | { italic_u ∈ italic_V : italic_v → italic_u } | ,
where v→u→𝑣𝑢v\rightarrow uitalic_v → italic_u denotes a directed path. Vertices are ranked based on desc⁢(v)desc𝑣\text{desc}(v)desc ( italic_v ), with ties broken lexicographically:
v1≻v2≻⋯≻vn.succeedssubscript𝑣1subscript𝑣2succeeds⋯succeedssubscript𝑣𝑛v_{1}\succ v_{2}\succ\cdots\succ v_{n}.italic_v start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ≻ italic_v start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ≻ ⋯ ≻ italic_v start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT .
This ranking reflects both individual preferences and their relative strengths in the graph.

3.3 Applications

We apply GED to three tasks: Response Selection (selecting the best response from LLM-generated candidates), Model Ranking (ranking models based on task performance), and Model Alignment (identifying the best instruction-response pairs for training).

Response selection.

In this task, a model ℳℳ\mathcal{M}caligraphic_M generates n𝑛nitalic_n candidate answers {a⁢n⁢s1,…,a⁢n⁢sn}𝑎𝑛subscript𝑠1…𝑎𝑛subscript𝑠𝑛\{ans_{1},\ldots,ans_{n}\}{ italic_a italic_n italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a italic_n italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT } for each question q∈Q𝑞𝑄q\in Qitalic_q ∈ italic_Q, and the goal is to identify the optimal answer a⁢n⁢sq∗𝑎𝑛superscriptsubscript𝑠𝑞ans_{q}^{*}italic_a italic_n italic_s start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT.
Multiple evaluators 𝒜={a1,…,ak}𝒜subscript𝑎1…subscript𝑎𝑘\mathcal{A}=\{a_{1},\ldots,a_{k}\}caligraphic_A = { italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT } provide pairwise preferences among these candidates, constructing a set of preference graphs {Ga:a∈𝒜}conditional-setsubscript𝐺𝑎𝑎𝒜\{G_{a}:a\in\mathcal{A}\}{ italic_G start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT : italic_a ∈ caligraphic_A }.

Each graph Ga=(Vq,Aa,wa)subscript𝐺𝑎subscript𝑉𝑞subscript𝐴𝑎subscript𝑤𝑎G_{a}=(V_{q},A_{a},w_{a})italic_G start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT = ( italic_V start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT , italic_A start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT , italic_w start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ) represents the preferences of evaluator a𝑎aitalic_a, where Vqsubscript𝑉𝑞V_{q}italic_V start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT corresponds to the candidates and Aasubscript𝐴𝑎A_{a}italic_A start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT indicates pairwise preferences with weights wasubscript𝑤𝑎w_{a}italic_w start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT reflecting preference strength.
This process is detailed in Appendix E.
To aggregate these graphs, GED first merges them into a unified graph Gq=(Vq,Aq,wq)subscript𝐺𝑞subscript𝑉𝑞subscript𝐴𝑞subscript𝑤𝑞G_{q}=(V_{q},A_{q},w_{q})italic_G start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT = ( italic_V start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT , italic_A start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT , italic_w start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT ), removes cycles to obtain a DAG, and derives the ranking ℛq={v1≻v2≻…≻vn}subscriptℛ𝑞succeedssubscript𝑣1subscript𝑣2succeeds…succeedssubscript𝑣𝑛\mathcal{R}_{q}=\{v_{1}\succ v_{2}\succ\ldots\succ v_{n}\}caligraphic_R start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT = { italic_v start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ≻ italic_v start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ≻ … ≻ italic_v start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT }.
The top-ranked answer is selected as a⁢n⁢sq∗𝑎𝑛superscriptsubscript𝑠𝑞ans_{q}^{*}italic_a italic_n italic_s start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT. Repeating this for all q∈Q𝑞𝑄q\in Qitalic_q ∈ italic_Q yields the final set a⁢n⁢s∗={a⁢n⁢s1∗,…,a⁢n⁢st∗}𝑎𝑛superscript𝑠𝑎𝑛superscriptsubscript𝑠1…𝑎𝑛superscriptsubscript𝑠𝑡ans^{*}=\{ans_{1}^{*},\ldots,ans_{t}^{*}\}italic_a italic_n italic_s start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT = { italic_a italic_n italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT , … , italic_a italic_n italic_s start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT }, representing consensus from multiple evaluators and ensuring high-quality responses.

Model Ranking.

The goal of model ranking is to rank a set of models M={ℳ1,…,ℳn}𝑀subscriptℳ1…subscriptℳ𝑛M=\{\mathcal{M}_{1},\ldots,\mathcal{M}_{n}\}italic_M = { caligraphic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , caligraphic_M start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT } based on their responses to questions Q={q1,…,qt}𝑄subscript𝑞1…subscript𝑞𝑡Q=\{q_{1},\ldots,q_{t}\}italic_Q = { italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_q start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT }. Evaluators 𝒜={a1,…,ak}𝒜subscript𝑎1…subscript𝑎𝑘\mathcal{A}=\{a_{1},\ldots,a_{k}\}caligraphic_A = { italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT } provide pairwise preferences for model outputs, constructing preference graphs {Ga:a∈𝒜}conditional-setsubscript𝐺𝑎𝑎𝒜\{G_{a}:a\in\mathcal{A}\}{ italic_G start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT : italic_a ∈ caligraphic_A } for each question q𝑞qitalic_q.

Here, each graph Ga=(Vq,Aa,wa)subscript𝐺𝑎subscript𝑉𝑞subscript𝐴𝑎subscript𝑤𝑎G_{a}=(V_{q},A_{a},w_{a})italic_G start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT = ( italic_V start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT , italic_A start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT , italic_w start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ) represents preferences, where Vqsubscript𝑉𝑞V_{q}italic_V start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT corresponds to the models and wasubscript𝑤𝑎w_{a}italic_w start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT reflects preference strength. The detailed procedure is outlined in
Appendix E.
Using GED, we aggregate these graphs into a unified graph Gqsubscript𝐺𝑞G_{q}italic_G start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT, transform it into a DAG by removing cycles, and derive the ranking ℛqsubscriptℛ𝑞\mathcal{R}_{q}caligraphic_R start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT. Repeating this for all q∈Q𝑞𝑄q\in Qitalic_q ∈ italic_Q yields a set of rankings {ℛq:q∈Q}conditional-setsubscriptℛ𝑞𝑞𝑄\{\mathcal{R}_{q}:q\in Q\}{ caligraphic_R start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT : italic_q ∈ italic_Q }.
Finally, a ranking ensemble is applied to compute the overall ranking ℛ∗superscriptℛ\mathcal{R}^{*}caligraphic_R start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT across questions, reflecting model performance as assessed by evaluators, as detailed in Appendix N

Model Alignment.

In the model alignment task, the objective is to identify the best response y∗superscript𝑦y^{*}italic_y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT for each instruction x𝑥xitalic_x from candidate responses {y1,…,yn}subscript𝑦1…subscript𝑦𝑛\{y_{1},\ldots,y_{n}\}{ italic_y start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_y start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT }. Evaluators 𝒜𝒜\mathcal{A}caligraphic_A provide pairwise preferences, forming preference graphs {Ga:a∈𝒜}conditional-setsubscript𝐺𝑎𝑎𝒜\{G_{a}:a\in\mathcal{A}\}{ italic_G start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT : italic_a ∈ caligraphic_A }, where Ga=(Vx,Aa,wa)subscript𝐺𝑎subscript𝑉𝑥subscript𝐴𝑎subscript𝑤𝑎G_{a}=(V_{x},A_{a},w_{a})italic_G start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT = ( italic_V start_POSTSUBSCRIPT italic_x end_POSTSUBSCRIPT , italic_A start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT , italic_w start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ) represents preferences over {y1,…,yn}subscript𝑦1…subscript𝑦𝑛\{y_{1},\ldots,y_{n}\}{ italic_y start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_y start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT }.
GED aggregates these graphs into a unified graph Gxsubscript𝐺𝑥G_{x}italic_G start_POSTSUBSCRIPT italic_x end_POSTSUBSCRIPT, removes cycles to produce a DAG, and derives a ranking ℛxsubscriptℛ𝑥\mathcal{R}_{x}caligraphic_R start_POSTSUBSCRIPT italic_x end_POSTSUBSCRIPT. The highest-ranked response is selected as y∗superscript𝑦y^{*}italic_y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT for x𝑥xitalic_x. Repeating this for all t𝑡titalic_t instructions yields the final training set {(x1,y1∗),…,(xt,yt∗)}subscript𝑥1superscriptsubscript𝑦1…subscript𝑥𝑡superscriptsubscript𝑦𝑡\{(x_{1},y_{1}^{*}),\ldots,(x_{t},y_{t}^{*})\}{ ( italic_x start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_y start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ) , … , ( italic_x start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT , italic_y start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ) }, reflecting consensus among evaluators.

4 Theoretical Analysis

In this section, we provide a theoretical foundation for our method, showing that by modeling preference graphs as random perturbations of a ground truth DAG, GED can reliably recover the true structure through graph ensemble and denoising with high probability, demonstrating its robustness in handling noisy evaluations.
Theoretically, we treat each of our preference graph as a random perturbation of some ground truth DAG G=(V,A)𝐺𝑉𝐴G=(V,A)italic_G = ( italic_V , italic_A ). Specifically, we consider a random graph generator 𝒢⁢(G,δ1,δ2)𝒢𝐺subscript𝛿1subscript𝛿2\mathcal{G}(G,\delta_{1},\delta_{2})caligraphic_G ( italic_G , italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) with parameters δ1,δ2∈[0,1]subscript𝛿1subscript𝛿201\delta_{1},\delta_{2}\in[0,1]italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ∈ [ 0 , 1 ] such that Gi=(Vi,Ai)∼𝒢⁢(G,δ1,δ2)subscript𝐺𝑖subscript𝑉𝑖subscript𝐴𝑖similar-to𝒢𝐺subscript𝛿1subscript𝛿2G_{i}=(V_{i},A_{i})\sim\mathcal{G}(G,\delta_{1},\delta_{2})italic_G start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT = ( italic_V start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT , italic_A start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) ∼ caligraphic_G ( italic_G , italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) satisfies Vi=Vsubscript𝑉𝑖𝑉V_{i}=Vitalic_V start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT = italic_V.

Furthermore, for each u,v∈V𝑢𝑣𝑉u,v\in Vitalic_u , italic_v ∈ italic_V with u≠v𝑢𝑣u\neq vitalic_u ≠ italic_v,

1)

If (u→v)∈A→𝑢𝑣𝐴(u\rightarrow v)\in A( italic_u → italic_v ) ∈ italic_A, then
ℙ⁢((u→v)∈Ai)ℙ→𝑢𝑣subscript𝐴𝑖\displaystyle\mathbb{P}((u\rightarrow v)\in A_{i})blackboard_P ( ( italic_u → italic_v ) ∈ italic_A start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )=1−δ1,absent1subscript𝛿1\displaystyle=1-\delta_{1},= 1 - italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ,ℙ⁢((v→u)∈Ai)ℙ→𝑣𝑢subscript𝐴𝑖\displaystyle\mathbb{P}((v\rightarrow u)\in A_{i})blackboard_P ( ( italic_v → italic_u ) ∈ italic_A start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )=δ1.absentsubscript𝛿1\displaystyle=\delta_{1}.= italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT .

2)

If (u→v),(v→u)∉A→𝑢𝑣→𝑣𝑢𝐴(u\rightarrow v),(v\rightarrow u)\notin A( italic_u → italic_v ) , ( italic_v → italic_u ) ∉ italic_A, then
ℙ⁢((u→v),(v→u)∉Ai)ℙ→𝑢𝑣→𝑣𝑢subscript𝐴𝑖\displaystyle\mathbb{P}((u\rightarrow v),(v\rightarrow u)\notin A_{i})blackboard_P ( ( italic_u → italic_v ) , ( italic_v → italic_u ) ∉ italic_A start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )=1−δ2,absent1subscript𝛿2\displaystyle=1-\delta_{2},= 1 - italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ,ℙ⁢((u→v)∈Ai)ℙ→𝑢𝑣subscript𝐴𝑖\displaystyle\mathbb{P}((u\rightarrow v)\in A_{i})blackboard_P ( ( italic_u → italic_v ) ∈ italic_A start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )=δ22,absentsubscript𝛿22\displaystyle=\frac{\delta_{2}}{2},= divide start_ARG italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG start_ARG 2 end_ARG ,ℙ⁢((v→u)∈Ai)ℙ→𝑣𝑢subscript𝐴𝑖\displaystyle\mathbb{P}((v\rightarrow u)\in A_{i})blackboard_P ( ( italic_v → italic_u ) ∈ italic_A start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )=δ22.absentsubscript𝛿22\displaystyle=\frac{\delta_{2}}{2}.= divide start_ARG italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG start_ARG 2 end_ARG .

That is, each edge in E𝐸Eitalic_E has probability δ1subscript𝛿1\delta_{1}italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT of being flipped and each pair of unconnected nodes has probability δ2subscript𝛿2\delta_{2}italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT of being connected with a random direction.

Now, given that G1,…,GN⁢∼i.i.d.⁢𝒢⁢(G,δ1,δ2)subscript𝐺1…subscript𝐺𝑁i.i.d.similar-to𝒢𝐺subscript𝛿1subscript𝛿2G_{1},\dots,G_{N}\overset{\text{i.i.d.}}{\sim}\mathcal{G}(G,\delta_{1},\delta_%
{2})italic_G start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_G start_POSTSUBSCRIPT italic_N end_POSTSUBSCRIPT overi.i.d. start_ARG ∼ end_ARG caligraphic_G ( italic_G , italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ), we will show that to some extent our combination of graph ensemble and graph denoising can indeed provably recover the ground truth DAG G𝐺Gitalic_G. For simplicity, all edges in G1,…,GNsubscript𝐺1…subscript𝐺𝑁G_{1},\dots,G_{N}italic_G start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_G start_POSTSUBSCRIPT italic_N end_POSTSUBSCRIPT and G𝐺Gitalic_G are considered equal weighted. Meanwhile, we use MAS⁢(⋅)MAS⋅\text{MAS}(\cdot)MAS ( ⋅ ) to denote the graph obtained by denoising, which stands for the maximum acyclic subgraph (MAS). Then, we have the following theorem.

Theorem 1.

Suppose G1,…,GN⁢∼i.i.d.⁢𝒢⁢(G,δ1,δ2)subscript𝐺1…subscript𝐺𝑁i.i.d.similar-to𝒢𝐺subscript𝛿1subscript𝛿2G_{1},\dots,G_{N}\overset{\text{i.i.d.}}{\sim}\mathcal{G}(G,\delta_{1},\delta_%
{2})italic_G start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_G start_POSTSUBSCRIPT italic_N end_POSTSUBSCRIPT overi.i.d. start_ARG ∼ end_ARG caligraphic_G ( italic_G , italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) for some ground truth G=(V,A)𝐺𝑉𝐴G=(V,A)italic_G = ( italic_V , italic_A ). Let G^^𝐺\widehat{G}over^ start_ARG italic_G end_ARG be the graph ensembled from G1,…,GNsubscript𝐺1…subscript𝐺𝑁G_{1},\dots,G_{N}italic_G start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_G start_POSTSUBSCRIPT italic_N end_POSTSUBSCRIPT by operations defined in Section 3.2. Then, as long as δ1=0.5−ϵsubscript𝛿10.5italic-ϵ\delta_{1}=0.5-\epsilonitalic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT = 0.5 - italic_ϵ for some ϵ>0italic-ϵ0\epsilon>0italic_ϵ > 0, we have
ℙ⁢(G⊆MAS⁢(G^))≥1−2⁢|A|⁢exp⁡(−N⁢ϵ22)−2⁢U⁢exp⁡(−N⁢ϵ26⁢U2⁢δ2+2⁢U⁢ϵ),ℙ𝐺MAS^𝐺12𝐴𝑁superscriptitalic-ϵ222𝑈𝑁superscriptitalic-ϵ26superscript𝑈2subscript𝛿22𝑈italic-ϵ\begin{split}\mathbb{P}\left(G\subseteq\text{MAS}(\widehat{G})\right)&\geq 1-2%
|A|\exp\left(-\frac{N\epsilon^{2}}{2}\right)\\
&\quad-2U\exp\left(-\frac{N\epsilon^{2}}{6U^{2}\delta_{2}+2U\epsilon}\right),%
\end{split}start_ROW start_CELL blackboard_P ( italic_G ⊆ MAS ( over^ start_ARG italic_G end_ARG ) ) end_CELL start_CELL ≥ 1 - 2 | italic_A | roman_exp ( - divide start_ARG italic_N italic_ϵ start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG 2 end_ARG ) end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL - 2 italic_U roman_exp ( - divide start_ARG italic_N italic_ϵ start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG 6 italic_U start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT + 2 italic_U italic_ϵ end_ARG ) , end_CELL end_ROW
where G⊆MAS⁢(G^)𝐺MAS^𝐺G\subseteq\text{MAS}(\widehat{G})italic_G ⊆ MAS ( over^ start_ARG italic_G end_ARG ) represents that G𝐺Gitalic_G is a subgraph of MAS⁢(G^)MAS^𝐺\text{MAS}(\widehat{G})MAS ( over^ start_ARG italic_G end_ARG ) and U=|V|⁢(|V|−1)2−|A|𝑈𝑉𝑉12𝐴U=\frac{|V|(|V|-1)}{2}-|A|italic_U = divide start_ARG | italic_V | ( | italic_V | - 1 ) end_ARG start_ARG 2 end_ARG - | italic_A | is the number of pairs of unconnected nodes in G𝐺Gitalic_G.

The full proof is given in Appendix G. From the theorem, we can see that the probability of failure decreases exponentially as the number of samples N𝑁Nitalic_N increases. Meanwhile, this guarantee only requires δ1<0.5subscript𝛿10.5\delta_{1}<0.5italic_δ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT < 0.5 and does not place restrictions on δ2subscript𝛿2\delta_{2}italic_δ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT, which are very mild conditions.

Table 1: 
Performance comparison of response selection methods across five benchmarks. GED consistently outperforms baseline methods, demonstrating the effectiveness of graph denoising and the aggregation of multiple evaluators.

MethodHumanEvalAlpacaEvalMATHGSM8kGAIAAvgLlama3-8B43.9027.2922.0856.676.7831.34Mistral-7B23.1711.8023.2539.837.0321.01Qwen2-7B48.5825.7159.9276.757.7043.73Qwen2-72B57.9329.5872.7584.6711.5251.29ContraSolver65.4231.1274.9586.8412.2254.11ListPreference61.5231.6771.7585.010.9052.16Single modelSelf-consistency60.9829.3373.5884.918.8651.53Llama3-8B62.1929.3174.2783.1611.3152.04with graph denoising64.0230.1874.7386.0011.7253.33Mistral-7B67.2427.7074.4183.8310.5052.73with graph denoising68.7329.9374.7783.9110.7453.61Qwen2-7B61.5828.6974.5085.4111.1152.25with graph denoising65.8529.4474.7986.3811.2553.54Qwen2-72B60.9731.0474.7386.4712.1453.07Single evaluatorwith graph denoising68.9031.1775.3387.4512.2655.02Multi-MV66.1829.5774.7786.4211.7253.73GED (w/o denoising)69.2530.9874.2987.1712.6854.87Multiple evaluatorGED70.7332.4475.5888.1813.3356.05
Figure 2: 
Comparison of GED with GPT-3.5, GPT-4-o-mini, and GPT-4-o on 100 randomly selected tasks. GED consistently outperforms GPT-3.5 across all tasks and surpasses GPT-4-o-mini on challenging tasks like HumanEval and GSM8k, showcasing the effectiveness of weak evaluator aggregation with graph denoising.

5 Experiments on Response Selection

Experiment Setup.

In this section, we evaluate the performance of GED on five benchmarks: HumanEval (Chen et al., 2021), AlpacaEval (Li et al., 2023b), MATH (Hendrycks et al., 2021), GSM8k (Chen et al., 2021), and GAIA (Mialon et al., 2023).
The Qwen2-72B (Yang et al., 2024a) model (ℳℳ\mathcal{M}caligraphic_M) generates ten candidate responses per question, and we assess the effectiveness of different methods in selecting the best response.
For further implementation details, see Appendix A.
We evaluate performance using three setups.
First, in the single model setting, the baselines include ContraSolver(Zhang et al., 2024b), Self-consistency(Wang et al., 2022), and direct evaluation with models (Llama3-8B, Mistral-7B, Qwen2-7B and Qwen2-72B).
Additionally, we include a baseline called ListPreference, where instead of pairwise comparisons, all candidate responses are input into Qwen2-72B for selecting the most appropriate response.
Then, in the single evaluator setting, individual evaluators (Llama3-8B, Mistral-7B, Qwen2-7B, Qwen2-72B) select the best response from ℳℳ\mathcal{M}caligraphic_M’s outputs, with and without applying GED’s graph denoising.
Finally, in the multiple evaluators setup, we combine three small evaluators (Llama3-8B, Qwen2-7B, Mistral-7B) to select responses from Qwen2-72B with GED.
We also introduce a baseline, Multi-MV, which selects the response that receives the most votes from evaluators in pairwise comparisons.
We present the results of GED and its variant (w/o denoising), which ensembles the preference graphs without the denoising step.

Table 2: Results of the model ranking task, evaluated using Ranking Correction. Higher correlation values indicate a stronger alignment with the ground truth rankings.
ModelWeight ScoreKemenyWeightedKemenyPairwiseMajorityWeightedPairwiseMajorityAvg.Llama3-70B50.8860.8060.8062.2361.8559.31with graph denoising52.4462.5462.5463.9262.1860.72Qwen2-72B65.3459.8767.3966.0566.5965.04with graph denoising66.0570.4370.4372.3272.4170.32Qwen1.5-72B63.6460.7260.7262.6563.2862.20with graph denoising64.8161.7761.7764.3664.7663.49Mistral-8×7B64.9068.7468.7473.0672.8769.66Single evaluatorwith graph denoising65.4770.0669.9273.3973.2170.41GED (w/o ensemble)62.8268.4468.4469.3467.3467.27GED (w/o denoising)64.8469.2369.8175.3574.3770.72Multiple evaluatorGED66.5971.1471.1477.1776.4672.50

Main results.

Table 1 presents the results of the response selection task across five benchmarks.
GED consistently outperforms baseline methods, including both single model evaluations (single model) and direct response selection by individual models (single evaluator).
This demonstrates the strength of aggregating weak evaluators with GED, particularly when coupled with graph denoising, which enhances response quality by filtering out noise and biases.
Furthermore, by combining preference graphs derived from smaller models (Llama3-8B, Mistral-7B, Qwen2-7B), GED outperforms a much larger evaluator (Qwen2-72B). This underscores the value of ensemble methods in mitigating the limitations of individual evaluators.

Then, the denoising process proves to be crucial for improving consistency and overall response quality. The substantial performance gains observed when using GED with denoising, compared to both the single evaluator setup and the ensemble without denoising, highlight its importance in refining response selection.
For Multi-MV, while it improves upon individual evaluators, it still underperforms GED, highlighting GED’s ability to capture nuanced evaluation signals and reduce inconsistencies.
Additionally, we observed that the ListPreference baseline performed worse than Qwen2-72B as single evaluator, likely due to LLM limitations in handling long-text.
Lastly, to further evaluate GED, we compared its performance with GPT-3.5, GPT-4-o-mini, and GPT-4-o.
Due to computational and API cost constraints, we limited the evaluation to 100 data points for each task.
As shown in Figure 2, GED consistently outperformed GPT-3.5 across all tasks and surpassed GPT-4-o-mini on challenging benchmarks like HumanEval and GSM8k.
These results highlight the superiority of GED, particularly in leveraging multi-weak evaluators and graph denoising to outperform individual state-of-the-art models.

Ablation study.

We evaluate the impact of removing the ensembling step in GED, referred to as the (w/o ensemble) variant. In this case, individual evaluators’ preference graphs are denoised and converted to rankings, which are then aggregated using methods such as Weight Score, Kemeny, Weighted Kemeny, Pairwise Majority, and Weighted Pairwise Majority (detailed in Appendix N).
For simplicity of presentation, we use Weight Score to represent GED (w/o ensemble) (Weight Score).
As shown in Figure 3, all (w/o ensemble) methods consistently underperform compared to GED. This performance gap arises because converting graphs to ranks before aggregation leads to information loss. In contrast, GED ensembles the graphs directly, preserving more detailed preference information and resulting in better final rankings.

6 Experiments on Model Ranking

Experiment Setup.

In this section, we evaluate the effectiveness of GED in the model ranking task within a human preference setting, using the AlpacaEval benchmark (Li et al., 2023b).
We employ 30 widely used models from the AlpacaEval dataset as our model set ℳℳ\mathcal{M}caligraphic_M, while the benchmark’s questions form the question set Q𝑄Qitalic_Q.
The rankings provided by the AlpacaEval benchmark serve as ground truth for evaluating the accuracy of various ranking methods.
This is justified by AlpacaEval’s strong correlation with Chatbot Arena rankings, making it a reasonable proxy for human judgments (Dubois et al., 2024a).
We adopt Ranking Correction, measured by the Spearman rank correlation coefficient, to evaluate the similarity.
To generate rankings, we utilize outputs from the open-source models Llama3-70B, Qwen2-72B, Mistral-8×\times×7B, and Qwen1.5-72B as our evaluators.
For further implementation details, see Appendix A.
We investigate two variants of GED:
(w/o ensemble) denoises the preference graphs from different evaluators for the same question, converts each into a ranking, and then ensembles these rankings to produce the final output, while (w/o denoising) directly ensembles the preference graphs to obtain the final ranking without denoising.

Figure 3: 
Comparison of GED and (w/o ensemble) variants.
GED outperforms due to preserving more information by directly ensembling preference graphs, while rank aggregation in the (w/o ensemble) methods leads to performance loss.

Main results.

The results, presented in Table 2, show that GED outperforms all single-model baselines, highlighting the significant improvement in ranking accuracy achieved by leveraging preference information from multiple evaluators.
Moreover, GED surpasses the (w/o ensemble) variant, indicating that generating rankings through graph ensemble first prevents information loss compared to converting individual graphs into rankings.
When the ensemble graph is not denoised (w/o denoising), residual noise can adversely affect the final ranking quality.
Additionally, our denoising method also enhances results in single-model settings.

Figure 4: 
Performance comparison of different methods (Random, Longest, ContraSolver, and GED) across multiple benchmarks, including
LIMA, Vicuna, Koala, WizardLM and Self-Instruct.
The results show GED effectively filters low-quality responses, improving performance and model alignment over baselines.
Table 3: Performance comparison of different methods (Random, Longest, ContraSolver, and GED) on model alignment task across the HH-RLHF benchmark.
The results demonstrate the superiority of GED in consistently selecting high-quality responses, leading to improved model performance compared to baseline methods.

BaseModelHarmless(base)Helpful(base)Helpful(online)Helpful(rejection)Avg.Origin69.6761.1265.4164.0665.07Random69.3862.8766.7565.5766.14Longest69.6563.5466.9966.4366.65ContraSolver69.5763.6166.8766.5966.66Llama-2-7BGED69.7164.1067.8767.0167.17Origin61.5959.5165.2163.1762.37Random59.1559.6164.0662.3861.30Longest61.8160.5364.5263.2262.52ContraSolver61.4859.8564.6663.4162.85Mistral-7BGED61.9660.7165.4963.8263.50

7 Experiments on Instruct Tuning

Experiment Setup.

In this section, we explore the effects of various data selection methods for model alignment on Llama-2-7B (Touvron et al., 2023) and Mistral-7B (Jiang et al., 2023) through instruct tuning.
Specifically, we randomly sampled 5,000 data points from UltraFeedback (Cui et al., 2023) and used Qwen1.5-14B (Yang et al., 2024a) to generate eight responses per data point as instruct data.
We then applied four different methods—Random, Longest (Zhao et al., 2024), ContraSolver (using Qwen2-72B as the evaluator) (Zhang et al., 2024b), and our proposed GED, which leverages Llama3-8B, Mistral-7B, and Qwen2-7B as evaluators—to select a subset of these responses for model alignment training.
The Origin refers to the performance of the base model without alignment.
The models were evaluated on the HH-RLHF (Bai et al., 2022) benchmark, which comprises four subsets: Harmless (base), Helpful (base), Helpful (online), and Helpful (rejection).
For evaluation, we employed the same Reward model as in prior work (Song et al., 2024; Yu et al., 2023) to quantify human preference levels.
The results are presented in Table 3.
For further implementation details, see Appendix A.
To ensure a comprehensive assessment, we further evaluated the models—using the Llama-2-7B backbone—on additional benchmarks, including
LIMA (Zhou et al., 2023), Vicuna (Chiang et al., 2023), Koala (Vu et al., 2023), WizardLM (Xu et al., 2023), and
Self-Instruct (Wang et al., 2022), in accordance with recent studies (Chen et al., 2023b; Zhang et al., 2024a; Hu et al., 2024).
The corresponding results are summarized in Figure 4.

Main results.

From Table 3, we observe that GED consistently outperforms all baseline methods, demonstrating its effectiveness in selecting high-quality responses when multiple answers are available for a given instruction.
When faced with multiple responses y1,y2,…,ynsubscript𝑦1subscript𝑦2…subscript𝑦𝑛y_{1},y_{2},\ldots,y_{n}italic_y start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_y start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_y start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT for a given instruction x𝑥xitalic_x, the Random selection method can have a detrimental impact, especially when the quality of the responses is inconsistent.
This effect is most evident with the Mistral-7B, where Random selection actually performs worse than the Origin, indicating that randomly chosen data points can introduce noise and degrade the model’s performance.
Moreover, we find that simply selecting the longest response does not always lead to the best outcomes.
While longer responses may provide more detailed answers, they are not necessarily better in terms of quality, particularly when both high-quality and low-quality answers exist for the same question.
This is reflected in the results where the Longest method underperforms compared to both ContraSolver and GED, emphasizing that response length alone is not always a reliable criterion.
From Figure 4, we observe similar trends as in Table 3.
GED consistently outperforms all baselines across various datasets, demonstrating its effectiveness in selecting high-quality responses.
Notably, in AlpacaEval and Self-Instruct, the Random baseline performs worse than the Origin model, highlighting that when response quality varies significantly, poor selection can degrade model performance.
In contrast, GED leverages preference graphs and denoising techniques to filter out low-quality responses, ensuring more robust and reliable performance, particularly in settings with inconsistent responses, as it removes evaluation noise and leads to more robust performance.

Table 4: Performance comparison on nuanced quality metrics (%). GED outperforms individual evaluators and random selection across Factuality, Relevance, Coherence, Inform., Helpful. and Validity metrics.
MethodFactualityRelevanceCoherenceInform.Helpful.ValidityAvg.Random86.7387.9192.4777.6217.4848.9268.52Llama3-8B88.5989.9194.4179.7718.4850.9270.35Mistral-7B89.1090.2994.8579.9518.5551.1370.65Qwen2-7B89.2590.4495.0380.0918.5851.2170.77GED94.7395.9197.3686.6219.4855.9275.00

8 Evaluating GED on More Metrics

To assess GED on more metrics, we evaluated its impact on nuanced quality aspects of LLM outputs, including factuality, relevance, coherence, informativeness, helpfulness, and validity. Since LLM tasks often require subtle judgments, GED’s adaptability is crucial.
Following (Chen et al., 2023a), we used Llama3-70B to generate ten candidate responses per query and applied GED for response selection, with Llama3-8B, Mistral-7B, and Qwen2-7B as evaluators. Table 4 shows that GED consistently outperformed individual evaluators and random selection across all metrics. It improved factuality by  5 % points over the best evaluator, while also enhancing relevance, coherence, informativeness, and helpfulness.
These results highlight GED’s ability to aggregate preferences effectively, capturing subtle qualities of generated content and improving overall reliability and utility in LLM assessments.

9 Conclusion

In this paper, we presented GED, a framework designed to address inconsistencies in pairwise preference evaluations by LLMs. By employing graph ensemble techniques and denoising, GED reduces cyclic patterns and enhances the reliability of evaluation outcomes. Our theoretical analysis shows that GED can recover the ground truth DAG under reasonable conditions, improving consistency in preference rankings.
Extensive experiments across response selection, model ranking, and instruct tuning demonstrate the efficacy of our method.
GED consistently outperformed baseline methods in both single-evaluator and multi-evaluator settings, particularly in scenarios where combining small evaluators led to superior results over larger individual evaluators.
Future work will explore extending GED to broader evaluation frameworks and applying its principles to more complex decision-making tasks, including multi-agent systems and human-AI interaction.

Impact Statements

This work enhances the reliability of model-based preference evaluation, reducing inconsistencies in AI judgments. It improves fairness and transparency in AI evaluation, benefiting NLP applications and ethical decision-making frameworks.

References

Achiam et al. (2023)
Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al.

Gpt-4 technical report.

arXiv preprint arXiv:2303.08774, 2023.

Adler et al. (2002)
Adler, N., Friedman, L., and Sinuany-Stern, Z.

Review of ranking methods in the data envelopment analysis context.

European journal of operational research, 140(2):249–265, 2002.

AI@Meta (2024)
AI@Meta.

Llama 3 model card.

2024.

URL https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.

Anthropic (2024)
Anthropic.

Introducing the next generation of claude.

2024.

URL https://www.anthropic.com/news/claude-3-family.

Bai et al. (2022)
Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., Drain, D., Fort, S., Ganguli, D., Henighan, T., et al.

Training a helpful and harmless assistant with reinforcement learning from human feedback.

arXiv preprint arXiv:2204.05862, 2022.

URL https://arxiv.org/abs/2204.05862.

Baumgartner et al. (2020)
Baumgartner, J., Zannettou, S., Keegan, B., Squire, M., and Blackburn, J.

The pushshift reddit dataset.

In Proceedings of the international AAAI conference on web and social media, volume 14, pp.  830–839, 2020.

Bodlaender et al. (2012)
Bodlaender, H. L., Fomin, F. V., Koster, A. M., Kratsch, D., and Thilikos, D. M.

A note on exact algorithms for vertex ordering problems on graphs.

Theory of Computing Systems, 50(3):420–432, 2012.

Boyeau et al. (2024)
Boyeau, P., Angelopoulos, A. N., Yosef, N., Malik, J., and Jordan, M. I.

Autoeval done right: Using synthetic data for model evaluation.

arXiv preprint arXiv:2403.07008, 2024.

Caragiannis et al. (2016)
Caragiannis, I., Procaccia, A. D., and Shah, N.

When do noisy votes reveal the truth?

ACM Transactions on Economics and Computation (TEAC), 4(3):1–30, 2016.

Chatzi et al. (2024)
Chatzi, I., Straitouri, E., Thejaswi, S., and Rodriguez, M. G.

Prediction-powered ranking of large language models.

arXiv preprint arXiv:2402.17826, 2024.

Chen et al. (2023a)
Chen, L., Deng, Y., Bian, Y., Qin, Z., Wu, B., Chua, T.-S., and Wong, K.-F.

Beyond factuality: A comprehensive evaluation of large language models as knowledge generators.

arXiv preprint arXiv:2310.07289, 2023a.

Chen et al. (2023b)
Chen, L., Li, S., Yan, J., Wang, H., Gunaratna, K., Yadav, V., Tang, Z., Srinivasan, V., Zhou, T., Huang, H., and Jin, H.

Alpagasus: Training a better alpaca with fewer data.

arXiv preprint arXiv:2307.08701, 2023b.

Chen et al. (2021)
Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. D. O., Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Brockman, G., et al.

Evaluating large language models trained on code.

arXiv preprint arXiv:2107.03374, 2021.

Chiang et al. (2023)
Chiang, W.-L., Li, Z., Lin, Z., Sheng, Y., Wu, Z., Zhang, H., Zheng, L., Zhuang, S., Zhuang, Y., Gonzalez, J. E., Stoica, I., and Xing, E. P.

Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality, March 2023.

URL https://lmsys.org/blog/2023-03-30-vicuna/.

Chowdhury et al. (2024)
Chowdhury, S. R., Kini, A., and Natarajan, N.

Provably robust dpo: Aligning language models with noisy feedback.

arXiv preprint arXiv:2403.00409, 2024.

Cui et al. (2023)
Cui, G., Yuan, L., Ding, N., Yao, G., Zhu, W., Ni, Y., Xie, G., Liu, Z., and Sun, M.

Ultrafeedback: Boosting language models with high-quality feedback, 2023.

Desmond et al. (2024)
Desmond, M., Ashktorab, Z., Pan, Q., Dugan, C., and Johnson, J. M.

Evalullm: Llm assisted evaluation of generative outputs.

In Companion Proceedings of the 29th International Conference on Intelligent User Interfaces, pp.  30–32, 2024.

Dubois et al. (2024a)
Dubois, Y., Galambosi, B., Liang, P., and Hashimoto, T. B.

Length-controlled alpacaeval: A simple way to debias automatic evaluators.

arXiv preprint arXiv:2404.04475, 2024a.

Dubois et al. (2024b)
Dubois, Y., Li, C. X., Taori, R., Zhang, T., Gulrajani, I., Ba, J., Guestrin, C., Liang, P. S., and Hashimoto, T. B.

Alpacafarm: A simulation framework for methods that learn from human feedback.

Advances in Neural Information Processing Systems, 2024b.

Durmus et al. (2022)
Durmus, E., Ladhak, F., and Hashimoto, T. B.

Spurious correlations in reference-free evaluation of text generation.

In Annual Meeting of the Association for Computational Linguistics, 2022.

Eades et al. (1993)
Eades, P., Lin, X., and Smyth, W. F.

A fast and effective heuristic for the feedback arc set problem.

Information processing letters, 1993.

Gabow (1995)
Gabow, H. N.

Centroids, representations, and submodular flows.

Journal of Algorithms, 18(3):586–628, 1995.

Guo & Yang (2024)
Guo, Y. and Yang, Y.

Improving weak-to-strong generalization with reliability-aware alignment.

arXiv preprint arXiv:2406.19032, 2024.

Hendrycks et al. (2021)
Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., and Steinhardt, J.

Measuring mathematical problem solving with the math dataset.

arXiv preprint arXiv:2103.03874, 2021.

Hou et al. (2024)
Hou, Y., Zhang, J., Lin, Z., Lu, H., Xie, R., McAuley, J., and Zhao, W. X.

Large language models are zero-shot rankers for recommender systems.

In European Conference on Information Retrieval, pp.  364–381. Springer, 2024.

Hu et al. (2024)
Hu, Z., Song, L., Zhang, J., Xiao, Z., Wang, J., Chen, Z., Zhao, J., and Xiong, H.

Rethinking llm-based preference evaluation.

arXiv preprint arXiv:2407.01085, 2024.

Jiang et al. (2023)
Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., Casas, D. d. l., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., et al.

Mistral 7b.

arXiv preprint arXiv:2310.06825, 2023.

Karp (2010)
Karp, R. M.

Reducibility among combinatorial problems.

Springer, 2010.

Kemeny (1959)
Kemeny, J. G.

Mathematics without numbers.

Daedalus, 88(4):577–591, 1959.

Lang et al. (2024)
Lang, H., Sontag, D., and Vijayaraghavan, A.

Theoretical analysis of weak-to-strong generalization.

arXiv preprint arXiv:2405.16043, 2024.

Li et al. (2023a)
Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., and Ghanem, B.

Camel: Communicative agents for ”mind” exploration of large language model society.

In Thirty-seventh Conference on Neural Information Processing Systems, 2023a.

Li et al. (2023b)
Li, X., Zhang, T., Dubois, Y., Taori, R., Gulrajani, I., Guestrin, C., Liang, P., and Hashimoto, T. B.

Alpacaeval: An automatic evaluator of instruction-following models.

https://github.com/tatsu-lab/alpaca_eval, 2023b.

Liu et al. (2023)
Liu, Y., Iter, D., Xu, Y., Wang, S., Xu, R., and Zhu, C.

G-eval: Nlg evaluation using gpt-4 with better human alignment.

In Conference on Empirical Methods in Natural Language Processing, 2023.

Liu et al. (2024)
Liu, Y., Zhou, H., Guo, Z., Shareghi, E., Vulic, I., Korhonen, A., and Collier, N.

Aligning with human judgement: The role of pairwise preference in large language model evaluators.

arXiv preprint arXiv:2403.16950, 2024.

Louis & Nenkova (2013)
Louis, A. and Nenkova, A.

Automatically assessing machine summary content without a gold standard.

Computational Linguistics, 2013.

Mialon et al. (2023)
Mialon, G., Fourrier, C., Swift, C., Wolf, T., LeCun, Y., and Scialom, T.

Gaia: a benchmark for general ai assistants.

arXiv preprint arXiv:2311.12983, 2023.

Mitchell (2023)
Mitchell, E.

A note on dpo with noisy preferences & relationship to ipo, 2023.

Naresh et al. (2024)
Naresh, N. U., Tulabandhula, T., et al.

Curatron: Complete and robust preference data for rigorous alignment of large language models.

In Proceedings of the Fifth Workshop on Data Science with Human-in-the-Loop (DaSH 2024), 2024.

Ouyang et al. (2022)
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al.

Training language models to follow instructions with human feedback.

Advances in neural information processing systems, 2022.

Rafailov et al. (2024)
Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Ermon, S., and Finn, C.

Direct preference optimization: Your language model is secretly a reward model.

Advances in Neural Information Processing Systems, 36, 2024.

Ratner et al. (2016)
Ratner, A. J., De Sa, C. M., Wu, S., Selsam, D., and Ré, C.

Data programming: Creating large training sets, quickly.

Advances in neural information processing systems, 2016.

Shankar et al. (2024)
Shankar, S., Zamfirescu-Pereira, J., Hartmann, B., Parameswaran, A., and Arawjo, I.

Who validates the validators? aligning llm-assisted evaluation of llm outputs with human preferences.

In Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology, pp.  1–14, 2024.

Shen et al. (2023)
Shen, W., Zheng, R., Zhan, W., Zhao, J., Dou, S., Gui, T., Zhang, Q., and Huang, X.

Loose lips sink ships: Mitigating length bias in reinforcement learning from human feedback.

In Conference on Empirical Methods in Natural Language Processing, 2023.

Siska et al. (2024)
Siska, C., Marazopoulou, K., Ailem, M., and Bono, J.

Examining the robustness of llm evaluation to the distributional assumptions of benchmarks.

In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2024.

Song et al. (2024)
Song, F., Yu, B., Li, M., Yu, H., Huang, F., Li, Y., and Wang, H.

Preference ranking optimization for human alignment.

In Proceedings of the AAAI Conference on Artificial Intelligence, 2024.

Tong et al. (2024)
Tong, Y., Wang, S., Li, D., Wang, Y., Han, S., Lin, Z., Huang, C., Huang, J., and Shang, J.

Optimizing language model’s reasoning abilities with weak supervision.

arXiv preprint arXiv:2405.04086, 2024.

Touvron et al. (2023)
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., et al.

Llama 2: Open foundation and fine-tuned chat models.

arXiv preprint arXiv:2307.09288, 2023.

Vu et al. (2023)
Vu, T.

---
title: SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models
source_url: https://arxiv.org/html/2509.23863
final_url: https://arxiv.org/html/2509.23863
status: 200
content_type: text/html; charset=utf-8
topics: [Corpus-Grounded Self-Play (SPICE 계열)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.507683+00:00
---

# SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models

## 원본 URL

https://arxiv.org/html/2509.23863

## 추출 본문

SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language ModelsReport GitHub Issue×
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHubSubmit in GitHub
Back to arXiv
Why HTML?Report IssueBack to AbstractDownload PDF
Abstract

1 Introduction

2 Preliminaries
Long-Context Reinforcement Learning

Group Relative Policy Optimization (GRPO)

3 The SPELL framework
3.1 The Self-Play Evolutionary Loop
Questioning

Responding

Verifying

3.2 Role-Specific Reward Design
Verifier

Responder

Questioner

3.3 Unified Policy Optimization
Role-Specific Dynamic Sampling

Advantage Estimation

Unified Policy Update

4 Experiments
4.1 Experimental Setup
Training Details

Evaluation Benchmarks

4.2 Main Results
SPELL consistently enhances performance across diverse models.

SPELL is superior to traditional RL with static data.

SPELL generalizes to longer contexts.

SPELL boosts exploration and raises the performance ceiling.

4.3 Ablation Studies
Questioner

Verifier

4.4 Analysis of Questioner Reward Mapping

4.5 Hyperparameters Analysis
Selection of standard deviation σ\sigma

Sensitivity of group size (GG)

4.6 Role of External Judges in Verification

5 Conclusion

References

A Statement on the Use of Large Language Models

B Limitations and Future Work

C Related Work
C.1 Long-Context Alignment

C.2 Self-Play Language Models
Multi-Model Optimization

Single-Model Optimization

D SPELL Algorithm

E Implementation Details
E.1 Training Data Construction

E.2 Evaluation Details
Evaluation Benchmarks

Evaluation Configurations

E.3 RL Algorithm Details

E.4 Details of Open-Source Models and the Dataset

E.5 Details of Baselines

F Additional Analysis
F.1 Training Cost Analysis

F.2 Short-Context Reasoning Results

F.3 Additional Long-Context Benchmarks

F.4 Comparison with Long-Context Alignment Baselines

F.5 Evolutionary Dynamics of Questioner and Verifier
Questioner dynamics

Verifier calibration

F.6 Analysis of Reward Hacking
Questioner stagnation

Responder mode collapse

Verifier self-delusion

G Prompt Template

 License: arXiv.org perpetual non-exclusive license
 

arXiv:2509.23863v4 [cs.CL] 13 Mar 2026

SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models

Ziyi Yang1,2  Weizhou Shen2  Chenliang Li2  Ruijun Chen1  Fanqi Wan1
Ming Yan2Xiaojun Quan1,3††footnotemark: Fei Huang2
1Sun Yat-sen University  2Tongyi Lab, Alibaba Group  3Shenzhen Loop Area Institute 

yangzy39@mail2.sysu.edu.cn, ym119608@alibaba-inc.com 
xiaojunquan@slai.edu.cn Work done during internship at Tongyi Lab, Alibaba Group.Corresponding authors.

Abstract
Progress in long-context reasoning for large language models (LLMs) has lagged behind other recent advances. This gap arises not only from the intrinsic difficulty of processing long texts, but also from the scarcity of reliable human annotations and programmatically verifiable reward signals.
In this paper, we propose SPELL, a multi-role self-play reinforcement learning framework that enables scalable, label-free optimization for long-context reasoning. SPELL integrates three cyclical roles—questioner, responder, and verifier—within a single model to enable continual self-improvement. The questioner generates questions from raw documents paired with reference answers; the responder learns to solve these questions based on the documents; and the verifier evaluates semantic equivalence between the responder’s output
and the questioner’s reference answer, producing reward signals to guide continual training. To stabilize training, we introduce an automated curriculum that gradually increases document length and a reward function that adapts question difficulty to the model’s evolving capabilities. Extensive experiments on six long-context benchmarks show that SPELL consistently improves performance across diverse LLMs and outperforms equally sized models fine-tuned on large-scale annotated data. Notably, SPELL achieves an average 7.6-point gain in pass@8 on the strong reasoning model Qwen3-30B-A3B-Thinking, raising its performance ceiling and showing promise for scaling to even more capable models. Our code is available at https://github.com/Tongyi-Zhiwen/Qwen-Doc.

Figure 1: (Left) An overview of the SPELL framework, where a single LLM self-evolves by dynamically adopting the roles of questioner, responder, and verifier. (Right)SPELL consistently boosts performance across various models (top) and exhibits superior test-time scaling over traditional RLVR (bottom).

1 Introduction

In recent years, reinforcement learning (RL) has emerged as a promising approach for enhancing the reasoning capabilities of large language models (LLMs) (Guo et al., 2025; Yang et al., 2025; Jaech et al., 2024; Team et al., 2025). Among these methods, reinforcement learning with verifiable rewards (RLVR) has shown particular promise in domains where correctness can be programmatically verified, such as mathematics, logical reasoning, and software engineering (Lambert et al., 2024; Hu et al., 2025; Liu et al., 2025c; Wei et al., 2025). RLVR methods employ rule-based or programmatic verifiers to generate reward signals, which then guide policy optimization through algorithms such as Proximal Policy Optimization (PPO) (Schulman et al., 2017b), Group Relative Policy Optimization (GRPO) (Shao et al., 2024), and related variants (Shao et al., 2024; Yue et al., 2025; Liu et al., 2025d).

Despite these advances, most RLVR research has been restricted to short-context settings (e.g., <1024 tokens), where models primarily rely on their parametric knowledge for reasoning (Wan et al., 2025).
In contrast, reasoning over long documents like long-context question answering requires not only locating relevant evidence scattered across extended contexts but also executing multi-step reasoning. Extending RLVR to long-context reasoning presents significant challenges, which stem from the inherent difficulty of processing long texts, as well as two critical bottlenecks: the prohibitive cost and unreliability of human annotations, and the absence of programmatically verifiable rewards.

Empirical evidence highlights the severity of these issues. On benchmarks such as LongBench-V2, human accuracy for extra-long multiple-choice reasoning tasks drops to 25.1% — effectively approaching random chance (Bai et al., 2025). This not only limits the performance achievable under human supervision but also imposes a scalability ceiling, particularly as LLMs approach superhuman reasoning capabilities (Zhao et al., 2025). Specifically, as context length grows, producing reliable annotations becomes increasingly costly and unstable, and supervision diversity diminishes. Moreover, the lack of verifiable reward mechanisms in long-context settings further constrains the applicability of RLVR, posing a fundamental challenge to advancing reasoning capabilities at scale.

To address these limitations, we turn to self-play RL, where a single model learns to self-evolve by generating and solving its own tasks without human labels (Zhou et al., 2025; Chen et al., 2025b; Huang et al., 2025). However, applying self-play to long-context reasoning poses a unique challenge: answers may be semantically correct yet differ substantially in expression, rendering string matching or naive majority voting unreliable reward signals. Thus, the model should not only generate questions and answers, but also verify its own solutions reliably. This observation motivates our framework, in which one LLM assumes three complementary roles: questioning, responding, and verifying.

In this paper, we introduce SPELL (Self-Play Reinforcement Learning for Evolving Long-Context Language Models), a self-play RL framework for long-context reasoning. In this setup, a unified policy alternates among three roles: the questioner, which formulates questions with reference answers from raw documents; the responder, which attempts to solve them; and the verifier, which compares the responder’s output with the reference answer to produce reward signals for joint optimization.
To steer this process, SPELL incorporates three key design elements. First, a verifier trained for self-consistency on verifiable tasks produces stable rewards, even for outputs that cannot be verified by strict rules, thereby overcoming the brittleness of string matching. Second, an automated curriculum uses a history memory of question–answer pairs and documents to progressively increase task difficulty. A Gaussian-shaped reward further calibrates difficulty around the responder’s competence frontier, ensuring questions are neither too easy nor impossibly difficult. Third, a role-specific dynamic sampling strategy balances contributions across roles to stabilize training of the shared policy.
Together, these components form a self-sufficient, closed-loop system that
enables LLMs to autonomously evolve long-context reasoning without human-labeled data

We evaluate SPELL across 12 open-source LLMs ranging from 4B to 32B parameters, including both dense and Mixture-of-Experts (MoE) architectures. On six long-context QA benchmarks, SPELL delivers consistent performance gains. Remarkably, training a base model with SPELL enables it to surpass its instruction-tuned counterpart that relies on extensive human-annotated data, highlighting the data efficiency of our label-free self-play approach. Against a strong RLVR baseline trained on a static dataset synthesized by DeepSeek-R1-0528 (Guo et al., 2025), SPELL achieves larger and more reliable gains. For capable models such as Qwen3-30B-A3B-Thinking, SPELL’s dynamic curriculum continually elevates performance and enables it to outperform the leading gemini-2.5-pro (Comanici et al., 2025) in pass@4. These findings firmly establish our self-play approach as a scalable and effective path toward advanced long-context reasoning without human supervision.

2 Preliminaries

Long-Context Reinforcement Learning

We formulate the long-context generation task as a reinforcement learning (RL) problem. Given a set of nn documents {ci}i=1n\{c_{i}\}_{i=1}^{n} and a question qq, the goal of long-context RL is to optimize a policy model πθ\pi_{\theta} to generate a response yy that maximizes a reward function rϕ​(c,q,y)r_{\phi}(c,q,y). The standard objective is to maximize the KL-regularized expected reward (Schulman et al., 2017a; Wan et al., 2025):
maxπθ𝔼c,q∼𝒟,y∼πθ(⋅∣c,q)[rϕ(c,q,y)]−β𝔻KL[πθ(y∣c,q)||πref(y∣c,q)],\max_{\pi_{\theta}}\mathbb{E}_{c,q\sim\mathcal{D},y\sim\pi_{\theta}(\cdot\mid c,q)}\left[r_{\phi}(c,q,y)\right]-\beta\mathbb{D}_{\text{KL}}\left[\pi_{\theta}(y\mid c,q)\,||\,\pi_{\text{ref}}(y\mid c,q)\right],(1)
where c=Concat​(c1,c2,…,cn)c=\text{Concat}(c_{1},c_{2},\dots,c_{n}), 𝒟\mathcal{D} is the training dataset, πref\pi_{\text{ref}} denotes a reference policy, and β\beta controls the strength of the KL regularization to prevent large deviations from the reference policy.

Group Relative Policy Optimization (GRPO)

For long-context inputs, the quadratic complexity of the attention mechanism renders PPO (Schulman et al., 2017b), which relies on generalized advantage estimation (GAE) (Schulman et al., 2015) via a value network, computationally prohibitive.
Therefore, we employ GRPO (Shao et al., 2024) to optimize the objective in Eq. (1).
For each input (c,q)(c,q), GRPO first samples a group of GG candidate responses {yi}i=1G\{y_{i}\}_{i=1}^{G} from the old policy πθold\pi_{\theta_{\text{old}}}. It then estimates the advantage through group-wise reward z-score normalization, thereby obviating the need for a separate value network.
Formally, the objective is:
𝒥GRPO​(θ)\displaystyle\mathcal{J}_{\text{GRPO}}(\theta)=𝔼c,q∼𝒟,{yi}i=1G∼πθold(⋅|c,q)[1G∑i=1G1|yi|∑t=1|yi|(min(ρi,t(θ)Ai,\displaystyle=\mathbb{E}_{c,q\sim\mathcal{D},\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|c,q)}\Bigg[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\Bigg(\min\Big(\rho_{i,t}(\theta)A_{i},(2)clip(ρi,t(θ),1−ε,1+ε)Ai)−β𝔻KL(πθ||πref))],\displaystyle\text{clip}\Big(\rho_{i,t}(\theta),1-\varepsilon,1+\varepsilon\Big)A_{i}\Big)-\beta\mathbb{D}_{\text{KL}}(\pi_{\theta}||\pi_{\text{ref}})\Bigg)\Bigg],
where ρi,t​(θ)=πθ​(yi,t|c,q,yi,<t)πθold​(yi,t|c,q,yi,<t)\rho_{i,t}(\theta)=\frac{\pi_{\theta}(y_{i,t}|c,q,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|c,q,y_{i,<t})} is the importance sampling ratio for token tt in sequence ii. The group-relative advantage AiA_{i} is shared across tokens of the ii-th sequence and computed by normalizing the sequence-level rewards {ri}i=1G\{r_{i}\}_{i=1}^{G}:
Ai=ri−mean​({rk}k=1G)std​({rk}k=1G).A_{i}=\frac{r_{i}-\text{mean}(\{r_{k}\}_{k=1}^{G})}{\text{std}(\{r_{k}\}_{k=1}^{G})}.(3)

3 The SPELL framework

In this section, we detail the core design of SPELL, a self-play reinforcement learning framework that enables LLMs to improve their long-context reasoning capabilities without external supervision.
The key principle of SPELL is that a single policy model πθ\pi_{\theta} dynamically assumes three complementary roles: a questionerπθque\pi_{\theta}^{\text{que}}, a responderπθres\pi_{\theta}^{\text{res}}, and a verifierπθver\pi_{\theta}^{\text{ver}}. Through their interaction, the model autonomously generates and solves questions while producing reliable reward signals.
This closed-loop interaction creates an evolving curriculum in which the model progressively adapts to longer contexts and more complex reasoning (Section 3.1).
Role-specific reward designs (Section 3.2) and a unified optimization procedure (Section 3.3) jointly drive this co-evolution.

3.1 The Self-Play Evolutionary Loop

As illustrated in Figure 2 and Algorithm 1, SPELL proceeds iteratively: given a cluster of nn documents C={ci}i=1nC=\{c_{i}\}_{i=1}^{n} and a task type111Details of dataset construction and task definition are provided in Appendix E.1.τ\tau, the policy πθ\pi_{\theta} first generates new questions,222To direct the policy in enacting three distinct roles, we adopt zero-shot prompting using tailored templates for each role and task type. Details of these templates are provided in Appendix G. then attempts to solve them, and finally verifies the solutions before performing a unified policy update.

Figure 2: Overview of our proposed SPELL for self-evolution of long-context reasoning. The process operates in a continuous loop that alternates between two stages: (1) Role-Specific Rollout, where a single policy model enacts three distinct roles—a questioner (πθque\pi_{\theta}^{\text{que}}), a responder (πθres\pi_{\theta}^{\text{res}}), and a verifier (πθver\pi_{\theta}^{\text{ver}})—to generate training data. (2) Unified Policy Update, where the unified policy is refined using the collected data, and the enhanced model serves as the starting point for the next rollout cycle.

Questioning

The questioner πθque\pi_{\theta}^{\text{que}} generates new question–answer pairs in an iterative curriculum. In the very first iteration, it is conditioned only on a randomly sampled subset of mm documents (m<nm<n) and produces a pair (q,a)(q,a). After each solvable pair is created, we append it to a history memoryℋ\mathcal{H} that stores the LL most recent solvable question–answer pairs and their associated source documents: ℋC={(Cl,ql,al)}l=1L\mathcal{H}_{C}=\{(C_{l},q_{l},a_{l})\}_{l=1}^{L}. In subsequent iterations, the questioner is conditioned on both a newly sampled subset CnewC_{\text{new}} and the stored memory. The resulting context is Xque=(⋃l=1LCl)∪Cnew∪{(ql,al)}l=1LX^{\text{que}}=(\bigcup_{l=1}^{L}C_{l})\cup C_{\text{new}}\cup\{(q_{l},a_{l})\}_{l=1}^{L}.
As the memory fills, the context for the questioner expands to include both previously seen and newly sampled documents, which allows the questioner to generate questions that integrate information across more documents.
The history memory also raises difficulty by including past {(ql,al)}\{(q_{l},a_{l})\}: these exemplars discourage redundancy and, via prompting, push πθque\pi_{\theta}^{\text{que}} to generate harder questions than those already solved. Consequently, the questioner’s difficulty increases for two complementary reasons: (1) the context XqueX^{\text{que}} expands over iterations as more documents are brought into scope, and (2) explicit conditioning on historical {(ql,al)}\{(q_{l},a_{l})\} encourages the model to escalate question complexity.

Responding

The responder πθres\pi_{\theta}^{\text{res}} attempts to solve the generated question based on documents.
To mitigate the generation of non-grounded or hallucinated questions, we employ a grounding filter process to discard questions that can be answered without documents.
For valid questions, the responder is presented with the complete set of nn documents, where the remaining documents unseen by the questioner serve as distractors to increase grounding and reasoning difficulty.
This design enforces reliance on the provided document context rather than parametric memory.
To encourage exploration of diverse reasoning trajectories, the responder generates GG independent rollouts {yi}i=1G\{y_{i}\}_{i=1}^{G}.

Verifying

The verifier πθver\pi_{\theta}^{\text{ver}} evaluates the semantic equivalence between the responder’s output yiy_{i} and the questioner’s reference answer aa.
For each yiy_{i}, it produces GG independent binary judgments {vi,j}j=1G,vi,j∈{0,1}\{v_{i,j}\}_{j=1}^{G},v_{i,j}\in\{0,1\}, which are then aggregated through majority voting:
viver=𝕀​(∑j=1Gvi,j>G2),v^{\text{ver}}_{i}=\mathbb{I}\left(\sum_{j=1}^{G}v_{i,j}>\frac{G}{2}\right),(4)
where 𝕀​(⋅)\mathbb{I}(\cdot) is the indicator function. This ensemble-based verification reduces variance and produces a stable, semantically aware reward signal, which is essential for sustaining a self-play system.

3.2 Role-Specific Reward Design

The three roles co-evolve under specialized rewards that align their objectives while remaining compatible within a single shared policy. In what follows, we detail these rewards.

Verifier

The verifier is trained to improve its judgment reliability through self-consistency (Wang et al., 2022; Zuo et al., 2025).
For a candidate output yiy_{i}, the verifier produces GG rollouts with judgments vi,jv_{i,j}. Each rollout is then assigned a reward:
ri,jver=𝕀​(vi,j=viver),r_{{i,j}}^{\text{ver}}=\mathbb{I}(v_{i,j}=v^{\text{ver}}_{i}),(5)
where viverv^{\text{ver}}_{i} is the majority vote over GG rollouts.

Responder

The responder’s reward for the ii-th solution is the maximum of a deterministic, rule-based check and the verifier’s consensus score, denoted as:
rires=max⁡(ℛrule​(yi,a),viver).r^{\text{res}}_{i}=\max\left(\mathcal{R}_{\text{rule}}(y_{i},a),v^{\text{ver}}_{i}\right).(6)
The rule-based function, ℛrule\mathcal{R}_{\text{rule}}, provides a binary reward based on cover exact match (CEM) criteria (Wan et al., 2025; Song et al., 2025)—it returns 1 if the ground-truth answer aa appears in the generated response yiy_{i} and 0 otherwise.
The maximum reward plays a crucial role: when yiy_{i} is a correct paraphrase that CEM fails to capture, a majority vote of viver=1v^{\mathrm{ver}}_{i}=1 prevents the policy from being misled by false-negative noise, which stabilizes learning and encourages continual improvement.

Questioner

The questioner is incentivized to generate questions of intermediate difficulty, as learning is most efficient at the frontier of the LLM’s capabilities (Bae et al., 2025; Huang et al., 2025). For binary-reward tasks, this frontier corresponds to a success probability of 0.5, which maximizes reward variance and provides the richest learning signal.
We therefore define the questioner’s reward as a Gaussian function centered at this optimal point. Given the responder’s average success rate, r¯res=1G​∑i=1Grires\bar{r}^{\text{res}}=\frac{1}{G}\sum_{i=1}^{G}r^{\text{res}}_{i}, the reward is:
rque={exp⁡(−(r¯res−μ)22​σ2)if ​0<r¯res<10if ​r¯res=0​ or ​r¯res=1−0.5if the question is not grounded in documents−1if the question-answer pair has formatting errors\displaystyle r^{\text{que}}=\begin{cases}\exp\left(-\frac{(\bar{r}^{\text{res}}-\mu)^{2}}{2\sigma^{2}}\right)&\text{if }0<\bar{r}^{\text{res}}<1\\
0&\text{if }\bar{r}^{\text{res}}=0\text{ or }\bar{r}^{\text{res}}=1\\
-0.5&\text{if the question is not grounded in documents}\\
-1&\text{if the question-answer pair has formatting errors}\end{cases}(7)
We set the mean μ=0.5\mu=0.5 to target the point of maximum learning efficiency and the standard deviation σ=0.5/3\sigma=0.5/3 to concentrate the reward around this level.
Additionally, the questioner is penalized for producing ill-formatted (e.g., non-parsable) question–answer pairs or questions that can be solved without context, thereby enforcing both correct formatting and strong grounding in the provided text.

3.3 Unified Policy Optimization

A central feature of SPELL is that samples generated under different roles supervise a single policy πθ\pi_{\theta}. The optimization must control both sample efficiency and gradient balance across roles.

Role-Specific Dynamic Sampling

The raw samples collected for each document instance are highly imbalanced: one questioner sample, GG responder samples, and G2G^{2} verifier judgments. To prevent the verifier’s samples from dominating updates and to prioritize improvements in the responder’s document-grounded reasoning, we introduce a role-specific sampling strategy that leverages the statistical structure of each role’s signals.
For the responder, we retain all groups with non-zero reward variance (std({rires}i=1G>0\text{std}(\{r^{\text{res}}_{i}\}_{i=1}^{G}>0).
The associated questions are labeled as positives for the questioner, and an equal number of negatives are drawn from questions with non-positive reward, as defined in Eq. (7).
For the verifier, we preserve instances where the majority vote agrees with the rule-based check and subsample groups with conflicting verifications to match the number of questions.
This role-specific sampling strategy reduces the training set to roughly 1/G1/G of all samples, accelerates optimization, and prevents the responder’s gradients from being overwhelmed by verifier samples. Importantly, although most verifier samples are omitted, their collection cost is low, see Appendix F.1.

Advantage Estimation

For the responder and verifier, which generate GG outputs per prompt, we use group-level advantage estimation as defined in Eq. (3):
Airole=rirole−mean​({rkrole}k=1G)std({rkrole}k=1G,role∈{res,ver}.A_{i}^{\text{role}}=\frac{r^{\text{role}}_{i}-\text{mean}(\{r^{\text{role}}_{k}\}_{k=1}^{G})}{\text{std}(\{r^{\text{role}}_{k}\}_{k=1}^{G}},~\text{role}\in\{\text{res},\text{ver}\}.(8)
The questioner generates only a single output per instance and thus lacks a group-level baseline. Therefore, we adapt the normalization method from REINFORCE++-baseline (Hu, 2025) and normalize its reward against other questioner rewards within the training batch ℬque\mathcal{B}^{\text{que}}:
Aque=rque−mean​(rque|rque∈ℬque)std​(rque|rque∈ℬque).A^{\text{que}}=\frac{r^{\text{que}}-\text{mean}(r^{\text{que}}~|~r^{\text{que}}\in{\mathcal{B}^{\text{que}}})}{\text{std}(r^{\text{que}}~|~r^{\text{que}}\in{\mathcal{B}^{\text{que}}})}.(9)

Unified Policy Update

After collecting and sampling a batch of samples, the policy parameters θ\theta are updated by jointly optimizing the GRPO objective across all three roles:
𝒥GRPO​(θ)=𝒥GRPOque​(θ)+𝒥GRPOres​(θ)+𝒥GRPOver​(θ)\mathcal{J}_{\text{GRPO}}(\theta)=\mathcal{J}_{\text{GRPO}}^{\text{que}}(\theta)+\ \mathcal{J}_{\text{GRPO}}^{\text{res}}(\theta)+\mathcal{J}_{\text{GRPO}}^{\text{ver}}(\theta)(10)
The updated πθ\pi_{\theta} is reused to execute all roles in the next iteration. This closes the self-evolutionary cycle and keeps one unified policy for questioning, responding, and verifying.

4 Experiments

4.1 Experimental Setup

Training Details

Our SPELL RL framework is implemented using VeRL (Sheng et al., 2025). During generation, we employ a sampling temperature of 0.7 and a top-pp value of 0.95. The maximum input length is 16K tokens, while the maximum output length is set to 4K for non-reasoning models and extended to 20K tokens for reasoning models.
To balance rollout diversity and computational efficiency, we utilize a group size of G=8G=8.
The maximum number of recent solvable question–answer pairs cached in history memory is set to L=3L=3, and the number of candidate documents drawn when proposing a new question is set to m=5m=5.
We conduct a purely on-policy RL training with a batch size of 128 and a constant learning rate of 2×10−62\times 10^{-6}.
At the beginning of each rollout, we randomly sample one of three predefined task formats—document general QA, financial math QA, or multiple-choice—along with a relevant document list from the corpus.
Prompt templates for each task τ\tau and each role are provided in Appendix G.
For the RLVR baseline, we synthesize a dataset using DeepSeek-R1-0528 (Guo et al., 2025) over the same document corpus and maintain identical hyperparameters to ensure a fair comparison. For comprehensive details on data construction, RL algorithm, and baselines, please refer to Appendix E.1, E.3, and E.5.

Evaluation Benchmarks

We evaluate our models on six long-context benchmarks, spanning multiple-choice QA on LongBench-V2 (Bai et al., 2025) and multi-hop QA across Frames (Krishna et al., 2025), HotpotQA (Yang et al., 2018), 2WikiMultihopQA (Ho et al., 2020), MuSiQue (Trivedi et al., 2022)333We use the subsets of HotpotQA, 2WikiMultihopQA, and MuSiQue from LongBench (Bai et al., 2024b)., and the DocMath (Zhao et al., 2024) for financial report reasoning task.
We evaluate all models with maximum input lengths of 16K and 100K tokens, and report the average accuracy over eight runs.
Further details on the benchmarks and evaluation protocol are available in Appendix E.2.

4.2 Main Results

Table 1 summarizes the results of SPELL across 12 open-source LLMs on six long-context QA benchmarks under maximum input lengths of 16K and 100K tokens.
These results offer valuable insights into SPELL’s effectiveness and generalization, as elaborated below.

SPELL consistently enhances performance across diverse models.

Our self-play framework exhibits strong universality, and it delivers substantial improvements across different architectures, sizes, and families.
This versatility is evident across the following dimensions.
(1) Model types and sizes: SPELL cultivates complex reasoning skills from scratch. For unaligned base models, the average improvement at 16K is large and robust, with Qwen2.5-7B, Qwen2.5-14B, and Qwen2.5-32B improving by 13.9, 14.4, and 9.1 points, respectively.
Remarkably, these trained models consistently outperform their instruction-tuned counterparts of the same size, which are trained with extensive human-annotated data. This result highlights that SPELL is data-efficient and practically valuable in scenarios where labeled data is scarce.
SPELL also benefits instruction-tuned models, e.g., Qwen2.5-7B-Instruct improves by 9.0 points. For highly specialized reasoning models such as R1-Distill-Qwen-14B, the performance still increases by 3.4 points.
(2) Architecture: Beyond dense models, the framework is also applicable to Mixture-of-Experts (MoE) models, where it improves Qwen3-30B-A3B-Instruct and Qwen3-30B-A3B-Thinking by 4.4 and 2.0 points, respectively.
(3) Model families: Improvements extend across families. For example, Llama-3.1-8B-Instruct and R1-Distill-Llama-8B increase by 4.4 and 3.4 points, respectively.
Collectively, these results establish SPELL as a broadly effective paradigm for advancing LLMs in long-context tasks.

Table 1: Overall results of our proposed SPELL method with maximum input lengths of 16K and 100K on long-context benchmarks.
“LB-MQA” represents the average performance across 2WikiMultihopQA, HotpotQA, and MuSiQue. “LB-V2” refers to LongBench-v2. For the average score (Avg.), + indicates the relative improvement over the base model within each group. The best score in each model group is highlighted in bold.
Models16K100KDocMathFramesLB-MQALB-V2   Avg.DocMathFramesLB-MQALB-V2   Avg.Base ModelsQwen2.5-7B10.927.936.731.226.716.124.231.222.723.6+ RLVR41.841.050.030.240.8+14.1\textbf{40.8}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+14.1}}}}42.740.349.226.039.6+16.039.6\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+16.0}}}}+ SPELL40.039.250.932.340.6+13.940.6\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+13.9}}}}39.940.150.828.239.8+16.2\textbf{39.8}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+16.2}}}}Qwen2.5-14B38.037.241.932.137.336.237.543.327.536.1+ RLVR52.251.063.332.949.9+12.649.9\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+12.6}}}}53.252.164.230.550.0+13.950.0\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+13.9}}}}+ SPELL57.652.663.033.551.7+14.4\textbf{51.7}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+14.4}}}}56.853.063.231.251.1+15.0\textbf{51.1}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+15.0}}}}Qwen2.5-32B46.842.649.033.743.040.742.250.128.740.4+ RLVR58.350.059.532.850.2+7.250.2\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+7.2}}}}57.549.960.132.750.1+9.750.1\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+9.7}}}}+ SPELL61.850.262.134.252.1+9.1\textbf{52.1}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+9.1}}}}60.652.262.334.352.4+12.0\textbf{52.4}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+12.0}}}}Instruct ModelsQwen2.5-7B-Instruct38.440.345.129.038.239.441.444.528.438.4+ RLVR45.048.759.630.145.9+7.745.9\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+7.7}}}}44.148.657.428.244.6+6.244.6\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+6.2}}}}+ SPELL45.846.763.133.247.2+9.0\textbf{47.2}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+9.0}}}}44.548.260.732.446.5+8.1\textbf{46.5}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+8.1}}}}Qwen2.5-14B-Instruct56.351.663.032.250.856.752.464.236.652.5+ RLVR56.159.671.036.455.8+5.055.8\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+5.0}}}}56.759.973.438.557.1+4.657.1\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+4.6}}}}+ SPELL59.662.172.836.857.8+7.0\textbf{57.8}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+7.0}}}}60.163.974.840.159.7+7.2\textbf{59.7}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+7.2}}}}Qwen2.5-32B-Instruct60.049.961.436.051.863.049.461.536.252.5+ RLVR59.960.570.436.356.8+5.056.8\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+5.0}}}}59.762.369.636.957.1+4.657.1\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+4.6}}}}+ SPELL62.361.274.440.159.5+7.7\textbf{59.5}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+7.7}}}}63.362.074.140.860.1+7.6\textbf{60.1}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+7.6}}}}Qwen3-30B-A3B-Instruct62.355.370.536.956.363.057.870.344.158.8+ RLVR62.559.971.839.858.5+2.258.5\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.2}}}}64.062.072.447.461.5+2.761.5\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.7}}}}+ SPELL63.063.175.141.560.7+4.4\textbf{60.7}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+4.4}}}}64.963.774.848.763.0+4.2\textbf{63.0}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+4.2}}}}Llama3.1-8B-Instruct33.245.652.529.140.134.947.353.527.140.7+ RLVR37.945.058.827.542.3+2.242.3\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.2}}}}36.947.657.226.142.0+1.342.0\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.3}}}}+ SPELL39.248.961.628.444.5+4.4\textbf{44.5}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+4.4}}}}39.750.860.926.244.4+3.7\textbf{44.4}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+3.7}}}}Reasoning ModelsR1-Distill-Llama-8B42.050.366.827.946.841.552.669.326.447.5+ RLVR43.451.467.830.048.2+1.448.2\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.4}}}}45.454.068.028.348.9+1.448.9\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.4}}}}+ SPELL48.953.468.430.250.2+3.4\textbf{50.2}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+3.4}}}}49.254.370.029.350.7+3.2\textbf{50.7}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+3.2}}}}R1-Distill-Qwen-14B57.759.272.436.256.459.560.673.333.356.7+ RLVR59.661.774.637.258.3+1.958.3\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.9}}}}61.063.876.035.959.2+2.559.2\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.5}}}}+ SPELL61.662.376.239.059.8+3.4\textbf{59.8}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+3.4}}}}61.162.875.737.959.4+2.759.4\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.7}}}}Qwen3-4B-Thinking58.656.769.932.954.561.459.270.940.758.1+ RLVR60.556.671.133.855.5+1.055.5\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.0}}}}63.358.671.143.459.1+1.059.1\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.0}}}}+ SPELL61.956.671.636.856.7+2.2\textbf{56.7}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.2}}}}64.860.672.443.060.2+2.1\textbf{60.2}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.1}}}}Qwen3-30B-A3B-Thinking62.964.575.739.760.763.865.877.946.763.6+ RLVR62.764.777.038.560.7+0.060.7\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+0.0}}}}63.967.177.249.664.5+0.964.5\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+0.9}}}}+ SPELL64.166.578.042.362.7+2.0\textbf{62.7}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.0}}}}66.768.178.450.565.9+2.3\textbf{65.9}\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+2.3}}}}
Figure 3: Test-time scaling performance (pass@k) across all benchmarks. The Qwen3-30B-A3B-Thinking model trained with SPELL shows a significantly steeper improvement as the number of samples (K) increases compared to the base model and the RLVR baseline. Notably, its pass@4 performance surpasses gemini-2.5-pro.

SPELL is superior to traditional RL with static data.

We compare SPELL against the RLVR baseline trained on a fixed dataset synthesized by DeepSeek-R1-0528.
Although such static data offers high-quality supervision for RL training, it cannot adapt to the policy’s evolving capabilities.
In contrast, SPELL constructs a self-play curriculum that tracks the model’s current ability: the questioner focuses on instances near the responder’s competence boundary, maintaining alignment between the training signal and the policy throughout optimization.
The advantage becomes increasingly evident as the policy model’s capabilities grow. For Qwen2.5-7B, RLVR achieves performance comparable to SPELL, indicating that a static corpus appears sufficient for weaker policies. However, for Qwen3-30B-A3B-Thinking, SPELL improves average scores by 2.0, whereas RLVR yields no gain.
On the more challenging benchmarks for the same model, RLVR decreases accuracy on DocMath (-0.2) and LongBench-V2 (-1.2), whereas SPELL delivers consistent gains of 1.2 and 2.6 points, respectively.
These results validate that when models approach or surpass the quality of static training data, a self-play curriculum proves more effective for sustaining performance gains.

SPELL generalizes to longer contexts.

All models are trained with a 16K input limit and evaluated at 100K without additional tuning. The results remain consistent under this out‑of‑distribution input length, demonstrating that the benefits of SPELL extend beyond the training window. For Qwen2.5‑14B, the average improvement is 14.4 at 16K and increases to 15.0 at 100K. This consistency suggests that the framework strengthens document‑grounded reasoning in a way that remains effective as input lengths grow substantially, rather than producing gains limited to a specific context length.

SPELL boosts exploration and raises the performance ceiling.

We assess test-time exploration with the pass@k metric at a 100K input limit.
As shown in Figure 3, Qwen3-30B-A3B-Thinking trained with SPELL exhibits a markedly steeper improvement curve as k increases compared to both the base model and the RLVR baseline.
Its pass@8 score reaches 74.5, significantly outperforming the RLVR baseline (68.1) and the original base model (66.9).
This enhanced exploratory ability further allows the SPELL-trained model to surpass the performance of the leading gemini-2.5-pro (Comanici et al., 2025) at a pass@4 rate.
These results indicate that SPELL effectively broadens the model’s test-time search space and raises its attainable performance ceiling, highlighting a promising path toward elevating the capabilities of even more powerful foundation models.

4.3 Ablation Studies

To validate the key design choices within the SPELL framework, we conduct ablation studies on Qwen2.5-7B-Instruct. We individually remove each core component of the questioner and verifier roles to quantify their individual contributions to the overall performance.

Table 2: Ablation study of SPELL on Qwen2.5-7B-Instruct with a 16K maximum input length.
- and + indicate relative decreases and increases, respectively, compared to the full SPELL model.
MethodDocMathFramesLB-MQALB-V2AverageSPELL45.846.763.133.247.2Questionerw/o Format Penalty46.0+0.246.0\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+0.2}}}}48.2+1.548.2\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.5}}}}59.3-3.859.3\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-3.8}}}}31.0-2.231.0\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-2.2}}}}46.1-1.146.1\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-1.1}}}}w/o Grounding Filter47.0+1.247.0\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.2}}}}46.4-0.346.4\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.3}}}}60.1-3.060.1\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-3.0}}}}31.3-1.931.3\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-1.9}}}}46.2-1.046.2\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-1.0}}}}w/o Update45.5-0.345.5\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.3}}}}43.8-2.943.8\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-2.9}}}}50.9-12.250.9\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-12.2}}}}30.3-2.930.3\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-2.9}}}}42.6-4.642.6\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-4.6}}}}w/o History Memory45.6-0.245.6\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.2}}}}46.6-0.146.6\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.1}}}}54.2-8.954.2\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-8.9}}}}30.8-2.430.8\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-2.4}}}}44.3-2.944.3\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-2.9}}}}Verifierw/o Verifier39.4-6.439.4\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-6.4}}}}46.6-0.146.6\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.1}}}}60.4-2.760.4\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-2.7}}}}29.4-3.829.4\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-3.8}}}}44.0-3.244.0\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-3.2}}}}w/o Update45.1-0.745.1\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.7}}}}48.2+1.548.2\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.5}}}}61.4-1.761.4\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-1.7}}}}32.6-0.632.6\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.6}}}}46.8-0.446.8\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.4}}}}w/o Majority Voting45.5-0.345.5\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.3}}}}48.1+1.448.1\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+1.4}}}}61.9-1.261.9\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-1.2}}}}30.7-2.530.7\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-2.5}}}}46.6-0.646.6\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-0.6}}}}w/o Update Consistency46.6+0.846.6\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+0.8}}}}47.1+0.447.1\mathrlap{{}^{{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\scalebox{0.6}{+0.4}}}}57.7-5.457.7\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-5.4}}}}31.3-1.931.3\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-1.9}}}}45.7-1.545.7\mathrlap{{}^{{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\scalebox{0.6}{-1.5}}}}

Questioner

As shown in Table 2, the removal of the format penalty and the grounding filter degrades the average score by 1.1 and 1.0 points, respectively.
The format penalty keeps the question well-formed, and the grounding filter prevents the generation of hallucinated questions.
The largest drops come from disabling the update mechanism and the history memory: freezing the questioner lowers the average score by 4.6, and removing history memory lowers it by 2.9. The declines appear across DocMath, Frames, LB-MQA, and LB-V2, which indicates that these components have a broad impact rather than task-specific effects.

We further examine how these components affect generated question difficulty over Qwen2.5-7B-Instruct training steps, as measured by 1-pass@1 with an external responder (Qwen3-30B-A3B-Instruct) and an external verifier (gpt-oss-120b).
The full SPELL model (Figure 4, left) shows a clear upward trend in overall question difficulty, which ensures the questioner proposes questions that are challenging enough for the responder’s evolving capabilities.
In contrast, freezing the questioner causes difficulty to stagnate (Figure 4, middle), while removing the history memory makes it erratic (Figure 4, right).
The evidence supports the conclusion that continual updates and access to recent history are necessary to form a stable and progressively more challenging curriculum for the responder, which is essential for sustained improvement in a self-play system.
This dynamic prevents one role from exploiting the static weaknesses of another, as observed in Liu et al. (2025a).

Figure 4: Analysis of question difficulty (1 - pass@1) on three tasks over training steps. (Left): The full SPELL framework shows a clear upward trend in difficulty. (Middle): Without questioner updates, difficulty stagnates. (Right): Without the history memory, difficulty becomes erratic and unstable.

Verifier

Removing the verifier and relying solely on rule-based rewards decreases average score by 3.2 points, with a 6.4-point drop on DocMath.
The CEM-based reward function is brittle and can penalize semantically correct but lexically different answers; the verifier provides a complementary signal in such cases.
Interestingly, disabling verifier updates or switching to single-pass decisions leads to moderate declines, which indicates that Qwen2.5-7B-Instruct is already competent at the simpler verification task.
However, removing the consistency update mechanism still causes a 1.5-point performance drop. This result shows that the verifier’s updates are susceptible to noise from its own erroneous majority votes, which degrades its reliability.
On rule-verifiable tasks, the verifier learns to filter this noise by aligning its majority vote with the ground-truth rule-based outcome.
This process provides the verifier with reliable learning signals, which in turn enhance its ability to generate stable rewards for rule-unverifiable outputs.
This illustrates how verifiable rewards can guide the calibration of non-verifiable rewards, a finding that aligns with the self-judging methodology in Kimi-K2 (Team et al., 2025).

Figure 5: Comparison of different reward mapping strategies. (a) Visualization of the reward functions for SPELL, AZR, and R-Zero. (b)SPELL exhibits more stable entropy dynamics during training. (c)SPELL maintains a more moderate and controlled growth in response length. (d) These factors contribute to a consistent performance improvement, ultimately leading our method to achieve the highest final pass rate.

4.4 Analysis of Questioner Reward Mapping

We compare our Gaussian-mapped reward function for questioner in Eq. (7) with the reward mapping used in AZR (Zhao et al., 2025) and R-Zero (Huang et al., 2025).
Figure 5(a) visualizes these distinct mapping functions. While the AZR reward function also penalizes high-accuracy questions, it is susceptible to noise from spurious correctness, which can destabilize the training process.
In contrast, our Gaussian function, which peaks when the average responder accuracy r¯res\bar{r}^{\text{res}} is 0.5, selectively encourages questions at the frontier of the responder’s competence.
Additionally, this mechanism mitigates the impact of data noise. Questions with wrong reference answers typically result in success rates near zero or one, corresponding to scenarios of random guessing on unsolvable questions or consistent matching with the incorrect reference, respectively.
Both extremes naturally fall into the low-reward tails of the Gaussian function, effectively suppressing incorrect questions during policy optimization.
While R-Zero also centers its peak reward at 0.5, our Gaussian mapping provides a more targeted reward by offering stronger incentives for questions of moderate difficulty and imposing a steeper penalty on those that are either too easy or too hard.
This creates a focused and smooth reward distribution that guides the questioner away from generating both trivial and overly difficult questions.
The training dynamics corroborate these design differences.
As shown in Figures 5(b) and (c), our method maintains a more stable training entropy and exhibits more controlled growth in response length under the Gaussian mapping than under AZR or R-Zero.
These advantages in training stability lead to superior overall performance. As Figure 5(d) demonstrates, our method not only achieves more consistent performance growth but also reaches the highest final pass rate among all compared approaches.
This evidence supports the view that concentrating the questioner’s reward at the responder’s competence frontier stabilizes the optimization process while preserving headroom for their mutual co-evolution.

4.5 Hyperparameters Analysis

Selection of standard deviation σ\sigma

The choice of σ\sigma in Eq. (7) is derived from the statistical properties of the Gaussian distribution, where approximately 99.7% of data points fall within three standard deviations (3​σ3\sigma) of the mean.
In SPELL, we aim to concentrate the questioner’s reward at the point of the responder’s maximal learning efficiency, where r¯res=0.5\bar{r}^{\text{res}}=0.5.
Accordingly, the mean is set to μ=0.5\mu=0.5.
Given this mean, the distance to either boundary of the valid average responder reward range [0,1][0,1] is 0.5. By setting 3​σ=0.53\sigma=0.5, we ensure the effective range of the questioner reward

Table 3: Ablation analysis of SPELL varying the standard deviation σ\sigma and the rollout group size GG using Qwen2.5-7B-Instruct. The default configuration is σ=0.5/3\sigma=0.5/3 and G=8G=8.
SettingsDocMathFramesLB-MQALB-V2AverageSPELL45.846.763.133.247.2Standard Deviation (σ\sigma)σ=0.5/6\sigma=0.5/645.347.062.332.846.9σ=0.5/2\sigma=0.5/245.546.059.431.845.7Group Size (GG)G=4G=444.347.162.531.846.4G=16G=1646.047.462.731.947.0

covers the responder reward space, yielding σ=0.5/3\sigma=0.5/3.
To further validate this theoretical choice, we conduct an ablation study on σ\sigma using Qwen2.5-7B-Instruct. As shown in Table 3, narrowing the curve (σ=0.5/6\sigma=0.5/6) has a minimal negative impact, as the reward remains well-focused. However, widening the curve (σ=0.5/2\sigma=0.5/2) significantly degrades performance, likely because it assigns higher rewards to overly easy or hard questions, providing a less targeted training signal. This confirms that σ=0.5/3\sigma=0.5/3 is both theoretically sound and empirically effective.

Sensitivity of group size (GG)

We examine the impact of the rollout group size GG on model performance using Qwen2.5-7B-Instruct. As shown in Table 3, while G=8G=8 yields the best overall results, SPELL remains robust across different group sizes. We select G=8G=8 as the default setting to strike a balance between performance gains and computational efficiency during training.

4.6 Role of External Judges in Verification

We investigate whether replacing the rule-based judge (CEM-based reward function) with a stronger external model (gpt-oss-120b) benefits the self-play process. As shown in Table 4, introducing a stronger external judge does not yield a significant overall improvement. This suggests that Qwen2.5-7B-Instruct is already capable of learning semantic verification through self-play without external supervision.
Notably, when an external judge is introduced, the internal verifier becomes less important; removing it results in only a minor 0.5-point drop, compared to the significant 3.2-point drop observed when using the rule-based judge.
This highlights the critical role of the internal verifier in complementing the brittle CEM-based reward function when an external judge is not available.

Table 4: Comparison of SPELL trained with rule-based judge versus an external judge (gpt-oss-120b). The verifier is crucial when using a rule-based judge, but becomes less critical when including an external judge.
MethodDocMathFramesLB-MQALB-V2AverageQwen2.5-7B-Instruct38.440.345.129.038.2+ SPELL (Rule-based Judge)45.846.763.133.247.2+ SPELL (Gpt-oss-120b Judge)47.148.061.632.147.2+ SPELL (Rule-based Judge) w/o Verifier39.446.660.429.444.0+ SPELL (Gpt-oss-120b Judge) w/o Verifier47.047.261.131.346.7

5 Conclusion

This work introduces SPELL, a multi-role self-play reinforcement learning framework for evolving the long-context reasoning capabilities of LLMs without human supervision.
A single policy model alternates among the roles of questioner, responder, and verifier to generate questions, solve them, and assess the solutions, which reduces reliance on costly and unreliable human annotation while enabling stable self-evolution.
Extensive experiments across 12 models of diverse architectures and sizes show that SPELL delivers consistent and substantial improvements in long-context reasoning.

This study concludes with three notable findings.
First, signals from verifiable tasks can calibrate and strengthen the verifier’s assessment on non-verifiable tasks, thereby ensuring a reliable self-rewarding mechanism.
Second, within a multi-role self-play framework, sustaining a dynamic equilibrium among the capabilities of different roles is critical for the stable evolution of the shared policy.
Finally, our results demonstrate that for models approaching or surpassing human performance, where external supervision emerges as a fundamental bottleneck, autonomous self-evolution transitions from a promising alternative to an indispensable strategy for sustained advancement.

Ethics Statement

This research focuses on the development of long-context LLMs through self-play that requires no human supervision.
While we believe our methodology does not inherently raise significant ethical issues, we acknowledge the potential for misuse of this technology.
We also recognize that an unsupervised learning approach may perpetuate or amplify societal biases in the model.
Our research is conducted using only publicly available datasets, in compliance with their licenses, and involves no personally identifiable information.
We have adhered to all relevant ethical and legal standards and declare no conflicts of interest that could have influenced the outcomes of this study.

Reproducibility Statement

To ensure the reproducibility of our work, we provide full experimental details in Section 4.1 and Appendix E. These include our methods for dataset construction, training configurations, and the evaluation setup.
The implemented code, the data used, and a comprehensive guide to reproduce our method are available in the supplementary materials.

Acknowledgements

This work was supported by Alibaba Group through Alibaba Research Intern Program and National Natural Science Foundation of China (No. 62576368).

References

S. Bae, J. Hong, M. Y. Lee, H. Kim, J. Nam, and D. Kwak (2025)Online difficulty filtering for reasoning oriented reinforcement learning.
arXiv preprint arXiv:2504.03380.
Cited by: §3.2.

Y. Bai, X. Lv, J. Zhang, Y. He, J. Qi, L. Hou, J. Tang, Y. Dong, and J. Li (2024a)LongAlign: a recipe for long context alignment of large language models.
In Findings of the Association for Computational Linguistics: EMNLP 2024,
Cited by: §C.1.

Y. Bai, X. Lv, J. Zhang, H. Lyu, J. Tang, Z. Huang, Z. Du, X. Liu, A. Zeng, L. Hou, Y. Dong, J. Tang, and J. Li (2024b)LongBench: a bilingual, multitask benchmark for long context understanding.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
Cited by: §E.2,
§E.2,
footnote 3.

Y. Bai, S. Tu, J. Zhang, H. Peng, X. Wang, X. Lv, S. Cao, J. Xu, L. Hou, Y. Dong, J. Tang, and J. Li (2025)LongBench v2: towards deeper understanding and reasoning on realistic long-context multitasks.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
Cited by: §E.2,
Appendix G,
§1,
§4.1.

G. Chen, X. Li, M. Shieh, and L. Bing (2025a)LongPO: long context self-evolution of large language models through short-to-long preference optimization.
In International Conference on Learning Representations,
Cited by: §C.1,
§F.4.

L. Chen, M. Prabhudesai, K. Fragkiadaki, H. Liu, and D. Pathak (2025b)Self-questioning language models.
arXiv preprint arXiv:2508.03682.
Cited by: §C.2,
§1.

Z. Chen, Q. Chen, L. Qin, Q. Guo, H. Lv, Y. Zou, H. Yan, K. Chen, and D. Lin (2025c)What are the essential factors in crafting effective long context multi-hop instruction datasets? insights and best practices.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
Cited by: §C.1.

K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman (2021)Training verifiers to solve math word problems.
arXiv preprint arXiv:2110.14168.
Cited by: §F.2.

G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen, et al. (2025)Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities.
arXiv preprint arXiv:2507.06261.
Cited by: §1,
§4.2.

A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, et al. (2024)The llama 3 herd of models.
arXiv preprint arXiv:2407.21783.
Cited by: §E.5.

H. Gao, J. Geng, W. Hua, M. Hu, X. Juan, H. Liu, S. Liu, J. Qiu, X. Qi, Y. Wu, et al. (2025)A survey of self-evolving agents: on path to artificial super intelligence.
arXiv preprint arXiv:2507.21046.
Cited by: §C.2.

D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, et al. (2025)DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning.
Nature645 (8081), pp. 633–638.
Cited by: §E.5,
§1,
§1,
§4.1.

D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt (2021a)Measuring massive multitask language understanding.
In International Conference on Learning Representations,
Cited by: §F.2.

D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt (2021b)Measuring mathematical problem solving with the MATH dataset.
In Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2),
Cited by: §F.2.

X. Ho, A. D. Nguyen, S. Sugawara, and A. Aizawa (2020)Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps.
In Proceedings of the 28th International Conference on Computational Linguistics,
Cited by: §E.2,
§4.1.

J. Hu (2025)Reinforce++: a simple and efficient approach for aligning large language models.
arXiv preprint arXiv:2501.03262.
Cited by: §3.3.

J. Hu, Y. Zhang, Q. Han, D. Jiang, X. Zhang, and H. Shum (2025)Open-reasoner-zero: an open source approach to scaling up reinforcement learning on the base model.
arXiv preprint arXiv:2503.24290.
Cited by: §E.3,
§1.

C. Huang, W. Yu, X. Wang, H. Zhang, Z. Li, R. Li, J. Huang, H. Mi, and D. Yu (2025)R-zero: self-evolving reasoning llm from zero data.
arXiv preprint arXiv:2508.05004.
Cited by: §C.2,
§1,
§3.2,
§4.4.

A. Jaech, A. Kalai, A

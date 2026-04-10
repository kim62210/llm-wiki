---
title: Demystifying Reinforcement Learning in Agentic Reasoning
source_url: https://arxiv.org/html/2510.11701v1
final_url: https://arxiv.org/html/2510.11701v1
status: 200
content_type: text/html; charset=utf-8
topics: [Agentic RL (Tool-Integrated Reasoning 학습)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.681222+00:00
---

# Demystifying Reinforcement Learning in Agentic Reasoning

## 원본 URL

https://arxiv.org/html/2510.11701v1

## 추출 본문

Demystifying Reinforcement Learning in Agentic Reasoning
1 Introduction

2 Problem Formulation
2.1 Agentic Reinforcement Learning

2.2 GRPO-based Algorithm and Techniques

2.3 Recipe Design

3 Data in Agentic Reasoning
3.1 Real End-to-End Trajectories versus Synthetic Stitch-Style Trajectories

3.2 Diverse Data Maintains High Entropy in Training

3.3 Model-Aware Datasets for More Effective RL

4 Algorithmic Design and Training Dynamics in Agentic RL
4.1 The impact of the RLVR techniques on Agentic RL

4.2 Exploration–Exploitation Dynamics in Agentic RL

4.3 When High Entropy Drives Better Efficiency

5 Reasoning Modes in Agentic RL
5.1 When Fewer Tool Calls Lead to Better Tool Use

5.2 Limitations of Current Long-CoT Models in Agentic RL

5.3 Integrating Long-CoT with Agentic Reasoning

6 Contributions and Comparison on Challenging Benchmarks

7 Related Work

8 Discussion and Future Work
8.1 Data-Fuel Scarcity

8.2 Effective Scaling of Agentic Reasoning

8.3 Additional Application Scenarios in Agentic Reasoning

9 Limitations

10 Conclusion

A Experiment Setup
A.1 Training Setup

A.2 Evaluation Setup

A.3 SFT dataset

A.4 RL Dataset

B Prompt Template
B.1 Prompt for Agentic Reasoning

B.2 Prompt for Self-Contained Reasoning

Demystifying Reinforcement Learning in

Agentic Reasoning

Zhaochen Yu1   
Ling Yang3∗   
Jiaru Zou2  Shuicheng Yan122footnotemark: 2  Mengdi Wang322footnotemark: 2
1National University of Singapore  2University of Illinois at Urbana-Champaign  

3Princeton University

 Code: Open-AgentRL,   Model: DemyAgent-4BEqual Contribution. Contact: ly1988@princeton.edu,  Corresponding authors.

Abstract
Recently, the emergence of agentic RL has showcased that RL could also effectively improve the agentic reasoning ability of LLMs, yet the key design principles and optimal practices remain unclear. In this work, we conduct a comprehensive and systematic investigation to demystify reinforcement learning in agentic reasoning from three key perspectives: data, algorithm, and reasoning mode. We highlight our key insights: (i) Replacing stitched synthetic trajectories with real end-to-end tool-use trajectories yields a far stronger SFT initialization; high-diversity, model-aware datasets sustain exploration and markedly improve RL performance. (ii) Exploration-friendly techniques are crucial for agentic RL, such as clip higher, overlong reward shaping, and maintaining adequate policy entropy could improve the training efficiency. (iii) A deliberative strategy with fewer tool calls outperforms frequent tool calls or verbose self-reasoning, improving tool efficiency and final accuracy. Together, these simple practices consistently enhance agentic reasoning and training efficiency, achieving strong results on challenging benchmarks with smaller models, and establishing a practical baseline for future agentic RL research. Beyond these empirical insights, we further contribute a high-quality, real end-to-end agentic SFT dataset along with a high-quality RL dataset, and demonstrate the effectiveness of our insights in boosting the agentic reasoning ability of LLMs across four challenging benchmarks, including AIME2024/AIME2025, GPQA-Diamond, and LiveCodeBench-v6. With our recipes, 4B-sized models could also achieve superior agentic reasoning performance compared to 32B-sized models.

1 Introduction

Beyond pre-training and supervised fine-tuning (SFT) stages, recent advancements in reinforcement learning (RL) (Schulman et al., 2017; Rafailov et al., 2023; Yang et al., 2025c; b; Shao et al., 2024; Wang et al., 2025d; c) have introduced a new scaling axis that aligns large language models’ (LLMs) behavior to incentivize reasoning fidelity by encouraging the generation of effective chain-of-thought (CoT) trajectories.
Building on this, the paradigm of agentic reasoning (Li et al., 2025a; Wu et al., 2025; Li et al., 2025c; Sun et al., 2025; Jin et al., 2025; Feng et al., 2025; Dong et al., 2025b) further empowers LLMs to move beyond self-contained generation, equipping them with the ability to integrate external tools throughout the reasoning process. This shift has unlocked remarkable progress across domains such as mathematics, scientific discovery, and code generation.

Despite the rapid growth of these advances, scaling RL for agentic reasoning remains challenging.
Directly applying policy optimization methods such as GRPO (Shao et al., 2024; Guo et al., 2025) often leads LLM agents to suffer from suboptimal training and inference behaviors, including inefficient on-policy rollout sampling, reward & entropy collapse (Cui et al., 2025), and unstable training dynamics. This highlights the unsolved limitations from three perceptiveness:

Data wise. Current data curation pipelines often rely on stitch-style data synthesis (Feng et al., 2025; Schick et al., 2023), where segments of internal reasoning are manually replaced with tool outputs. Such patchwork overlooks the natural connectivity of reasoning and tool use, preventing the data from faithfully mimicking real multi-turn trajectories that indicate when and why tools should be invoked.

Algorithm wise. Despite rapid progress in GRPO-based variants, the optimal RL recipe for agentic reasoning remains unclear. Existing methods differ in their optimization granularity (token-, sequence-, or trajectory-level) and impose distinct inductive biases: some encourage exploration by relaxing clipping (Yu et al., 2025) or managing entropy (Wang et al., 2025b), while others suppress it through strong KL regularization (Cheng et al., 2025b) or conservative clipping. A principled understanding of when and how to deploy these algorithms is still missing.

Reasoning Mode wise. Open puzzles are unsolved regarding the allocation of turn budgets, the trade-off between response length and tool-call efficiency, and the impact of long-CoT predispositions on multi-turn reasoning. These uncertainties obscure the principles of agent reasoning modes, often leading to either overthinking (long, inefficient loops) or underthinking (premature tool reliance) during the agents’ reasoning process.

The above challenges motivate us to perform a systematic investigation of recent studies along these three perspectives, aiming to identify key factors that either hinder or enhance agentic reasoning in LLM agents as shown in fig.1. Specifically, we organize our paper as follows:

•

In Section 3 (to address ), we analyze how data curation design and diversity affect SFT and RL training stages, respectively. We observe that training directly on synthetic trajectories fails to provide reliable signals for when and how to invoke tools, preventing agents from learning optimal integration points, and also lacks sufficient data diversity to encourage effective exploration. To address this, we curate real end-to-end SFT dataset and high-diversity, model-aware RL dataset that improve the training efficiency and agentic reasoning performance.

•

In Section 4 (to address ), we compare GRPO-based RL algorithms and find that conservative clipping and KL divergence penalty overly constrain exploration during training. In addition, we analyze the roles of pass@k and average@k as guiding metrics, revealing how they capture the exploration–exploitation trade-off and highlight performance bottlenecks. We further show that sustaining higher entropy, especially for weaker models, is the key to improving RL efficiency.

•

In Section 5 (to address ), we investigate reasoning-mode components such as the number of tool calls and overall response length, and their relationship to performance.
We find that fewer, more deliberate tool interactions often yield better results, showing that over-reliance on external calls does not necessarily improve performance and that the key lies in effective and accurate tool invocations integrated into the model’s agentic reasoning process.

Beyond the insights gained from our comprehensive study, we also provide a strong baseline model called DemyAgent-4B, which could achieve SOTA-level performance in challenging benchmarks and outperform larger-sized models in agentic reasoning as shown in table2. We present our main contributions and the detailed baseline recipes in section6.

Figure 1: An overview of our research on agentic RL.

2 Problem Formulation

In this section, we first formalize the notation used throughout the paper, followed by an overview of the reinforcement learning (RL) algorithms we adopt. Finally, we outline our training and evaluation setup.

2.1 Agentic Reinforcement Learning

In this section, we formulate the agentic RL training objective as:
maxπθ𝔼x∼𝒟,y∼πθ(⋅∣x;𝒯)[rϕ(x,y)]−β𝔻KL(πθ(y∣x;𝒯)∥πref(y∣x;𝒯)).\max_{\pi_{\theta}}\;\mathbb{E}_{x\sim\mathcal{D},\,y\sim\pi_{\theta}(\cdot\mid x;\,\mathcal{T})}\big[\,r_{\phi}(x,y)\,\big]\;-\;\beta\,\mathbb{D}_{\mathrm{KL}}\!\left(\pi_{\theta}(y\mid x;\,\mathcal{T})\,\big\|\,\pi_{\mathrm{ref}}(y\mid x;\,\mathcal{T})\right).(1)

where 𝒯\mathcal{T} denotes the set of available tools, πθ\pi_{\theta} represents the policy LLM, πref\pi_{\mathrm{ref}} is the reference LLM, rϕr_{\phi} and 𝔻KL\mathbb{D}_{\mathrm{KL}} denote the reward function and KL divergence respectively. The input xx is sampled from dataset 𝒟\mathcal{D}, and yy is the corresponding output, possibly interleaved with tool-call feedback.

Unlike conventional RL that relies purely on LLM rollouts, agentic RL (Dong et al., 2025b; Feng et al., 2025; Li et al., 2025d; Dong et al., 2025a; Singh et al., 2025) integrates tool-call feedback during reasoning. The rollout distribution factorizes as
Pθ​(ℛ,y∣x;𝒯)=∏t=1tℛPθ​(ℛt∣ℛ<t,x;𝒯)⏟Agentic Reasoning⋅∏t=1tyPθ​(yt∣y<t,ℛ,x;𝒯)⏟Answer Generation.P_{\theta}(\mathcal{R},y\mid x;\,\mathcal{T})=\underbrace{\prod_{t=1}^{t_{\mathcal{R}}}P_{\theta}\!\left(\mathcal{R}_{t}\mid\mathcal{R}_{<t},\,x;\,\mathcal{T}\right)}_{\text{Agentic Reasoning}}\cdot\underbrace{\prod_{t=1}^{t_{y}}P_{\theta}\!\left(y_{t}\mid y_{<t},\,\mathcal{R},\,x;\,\mathcal{T}\right)}_{\text{Answer Generation}}.(2)

where ℛ\mathcal{R} is the reasoning trajectory of length tℛt_{\mathcal{R}}, interleaved with
tool-call feedback, and yy is the final answer with length tyt_{y}. In this paper, we mainly focus on rule-based RL algorithms like GRPO (Shao et al., 2024), which is widely adopted to optimize LLM-based Agents.

2.2 GRPO-based Algorithm and Techniques

Here we utilize GRPO (Shao et al., 2024) as our baseline algorithm. To better compare the difference between RL techniques that improve GRPO algorithm, we formulate the following objective in a more general format:
𝒥GRPO​(θ)\displaystyle\mathcal{J}_{\text{GRPO}}(\theta)=𝔼​[x∼𝒟,{ℛ}i=1G∼πref]\displaystyle=\mathbb{E}\bigg[\,x\sim\mathcal{D},\;\{\mathcal{R}\}_{i=1}^{G}\sim\pi_{\text{ref}}\bigg]Agg​(G,ℛ)​{min⁡[ri,t​(θ)⋅A^i,t,clip​(ri,t​(θ),1−ϵlow,1+ϵhigh)⋅A^i,t]−β​𝔻KL​(πθ∥πref)}.\displaystyle\quad\text{Agg}(G,\mathcal{R})\Bigg\{\min\Big[r_{i,t}(\theta)\cdot\hat{A}_{i,t},\,\text{clip}\big(r_{i,t}(\theta),1-\epsilon_{\text{low}},1+\epsilon_{\text{high}}\big)\cdot\hat{A}_{i,t}\Big]-\beta\,\mathbb{D}_{\text{KL}}(\pi_{\theta}\,\|\,\pi_{\text{ref}})\Bigg\}.(2)
Here Agg​(G,ℛ)\text{Agg}(G,\mathcal{R}) is the loss aggregation granularity, ri,t​(θ)r_{i,t}(\theta) is the importance ratio related to the type of loss aggregation granularity, and ϵ\epsilon represents the clip ratio. A^i,t\hat{A}_{i,t} is the normalized advantage across all tokens:
A^i,t=rϕ​(x,yt)−mean​({rϕ​(ℛ1),…,rϕ​(ℛG)})std​({rϕ​(ℛ1),…,rϕ​(ℛG)}).\hat{A}_{i,t}=\frac{r_{\phi}(x,y_{t})-\text{mean}(\{r_{\phi}(\mathcal{R}_{1}),\ldots,r_{\phi}(\mathcal{R}_{G})\})}{\text{std}(\{r_{\phi}(\mathcal{R}_{1}),\ldots,r_{\phi}(\mathcal{R}_{G})\})}.(3)
In our study, we focus on three key improvement techniques (Yu et al., 2025; Zheng et al., 2025) for GRPO: 1) Loss Aggregation Granularity, 2) Reward Shaping, 3) Clipping Strategy.
For loss aggregation granularity, we compare two kinds of loss, which can be formulated as:
AggTok​(G,ℛ)=1∑i=1G|ℛi|​∑i=1G∑t=1|ℛi|,\displaystyle\text{Agg}_{\text{Tok}}(G,\mathcal{R})=\frac{1}{\sum_{i=1}^{G}|\mathcal{R}_{i}|}\sum_{i=1}^{G}\sum_{t=1}^{|\mathcal{R}_{i}|},(4)AggSeq​(G)=1G​∑i=1G,\displaystyle\text{Agg}_{\text{Seq}}(G)=\frac{1}{G}\sum_{i=1}^{G},(5)
where AggTok​(G,ℛ)\text{Agg}_{\text{Tok}}(G,\mathcal{R}) is the token-level loss, and AggSeq​(G)\text{Agg}_{\text{Seq}}(G) is the sequence-level loss, and the corresponding importance ratio is formulated as:
ri,tTok​(θ)=πθ​(ℛi,(t)|ℛi,<t,τ)πr​e​f​(ℛi,(t)|ℛi,<t,τ)\displaystyle r_{i,t}^{\text{Tok}}(\theta)=\frac{\pi_{\theta}(\mathcal{R}_{i,(t)}|\mathcal{R}_{i,<t},\tau)}{\pi_{ref}(\mathcal{R}_{i,(t)}|\mathcal{R}_{i,<t},\tau)}(6)ri,tSeq​(θ)=(πθ​(ℛi|x,τ)πr​e​f​(ℛi|x,τ))1|ℛi|,\displaystyle r_{i,t}^{\text{Seq}}(\theta)=(\frac{\pi_{\theta}(\mathcal{R}_{i}|x,\tau)}{\pi_{ref}(\mathcal{R}_{i}|x,\tau)})^{\frac{1}{|\mathcal{R}_{i}|}},(7)
here ri,tTok​(θ)r_{i,t}^{\text{Tok}}(\theta) is the importance ratio of token-level loss and ri,tSeq​(θ)r_{i,t}^{\text{Seq}}(\theta) is the importance ratio of sequence-level loss. For the reward function. We optimize a composite reward that sums an outcome term (solution accuracy) and a tool-use term (number of invocations), with the tool bonus clipped to avoid degenerate “tool abuse” reward hacking. It could be formulated as:
rout+tool​(x,y,n)={1+0.1​nif match​(yt,y)min⁡(−1+0.1​n)otherwiser_{\text{out+tool}}(x,y,n)=\begin{cases}1+0.1n&\text{if match}(y_{t},y)\\
\min(-1+0.1n)&\text{otherwise}\end{cases}(8)

Here, nn is the number of tool invocations. For another reward function, which is known as overlong reward shaping. Specifically, overlong reward shaping gives zero reward when the output length is within a safe budget, then applies a linear penalty as length approaches the maximum (from Lmax−LcacheL_{\max}-L_{\text{cache}} to LmaxL_{\max}), and assigns -1 if it exceeds LmaxL_{\max}.
This preserves a smooth learning signal near the boundary while strongly discouraging overlong completions.
It can be formulated as follows:
rlength​(y)={0,|y|≤Lmax−Lcache,(Lmax−Lcache)−|y|Lcache,Lmax−Lcache<|y|≤Lmax,−1,Lmax<|y|.r_{\text{length}}(y)=\begin{cases}0,&\lvert y\rvert\leq L_{\max}-L_{\text{cache}},\\[4.0pt]
\dfrac{(L_{\max}-L_{\text{cache}})-\lvert y\rvert}{L_{\text{cache}}},&L_{\max}-L_{\text{cache}}<\lvert y\rvert\leq L_{\max},\\[8.0pt]
-1,&L_{\max}<\lvert y\rvert.\end{cases}(9)

2.3 Recipe Design

In our study, we investigate three key techniques for agentic RL: Loss Aggregation Granularity, Reward Shaping, and Clipping Strategy. We construct three different recipes:

GRPO-TCR: We incorporate Token-level loss, Clip higher and overlong Reward shaping techniques with GRPO.

GRPO-SCR: We incorporate Sequence-level loss, Clip higher, overlong Reward shaping techniques with GRPO.

GRPO-T: we adhere to the implementation in (Shao et al., 2024), and change the sample-level loss to token-level, and we take this recipe as our baseline.

3 Data in Agentic Reasoning

This section empirically examines how data affects agent training, comparing real end-to-end agentic vs synthetic stitch-style trajectories for cold-start SFT and evaluating high-diversity and model-aware datasets designed to maintain exploration to achieve effective RL.

3.1 Real End-to-End Trajectories versus Synthetic Stitch-Style Trajectories

Motivation
Current agentic training pipelines often rely on LLM-edited or template-based synthetic trajectories, which replace selected reasoning steps with tool invocations like ReTool (Feng et al., 2025). While scalable, such stitch-style data inevitably misses critical decision cues: not only how to call a tool, but also when, why, and what to do next. This raises the question: do real end-to-end trajectories provide qualitatively richer learning signals and stronger initialization for RL?

Setup.
For the synthetic baseline, we directly adopt the multi-turn SFT dataset from ReTool (Feng et al., 2025), where challenging long-CoT steps are substituted with tool invocations and responses. For real end-to-end trajectories, we use our curated dataset mentioned in appendix A.3. We fine-tune Qwen2.5-7B-Instruct and Qwen3-4B-Instruct-2507 on both datasets (real vs. synthetic) under identical settings, and evaluate the agentic reasoning performance on AIME2024/AIME2025.

Result.
We evaluate using average@32 (overall agent performance), pass@32 (ability boundary (Deng et al., 2025)), and maj@32 (performance stability). As shown in table1, real trajectories deliver a clear improvement: Qwen3-4B-Instruct-2507 trained on real data achieves 29.97% on average@32, 72.88% on pass@32, and 45.22% on maj@32 on AIME2025. In contrast, the synthetic baseline yields below 10% on average@32 with unstable performance and a significantly lower ability upper bound. Thus, real trajectories establish a much stronger and more stable starting point for RL. Unless otherwise stated, we use SFT checkpoints trained on our curated real agentic dataset, denoted as Qwen3-4B-RA-SFT and Qwen2.5-7B-RA-SFT.

Analysis.
The superiority of real trajectories lies in their ability to capture complete agentic reasoning behaviors through real end-to-end reasoning processes that synthetic stitching cannot replicate. Specifically, our dataset preserves:
(i) pre-call analysis, localizing which subproblems are efficiently solved via tools;
(ii) guarded execution, with intermediate checks;
(iii) error recovery and strategy revision, after failed attempts;
(iv) self-reflection and calibration, before invoking tools.

Table 1: Comparison between the impact of our curated real end-to-end SFT dataset and the synthetic SFT dataset on AIME 2024 and AIME 2025. Dataset & MetricQwen2.5-7B-InstructQwen3-4B-Instruct-2507w/ synthetic trajectoryw/ real trajectoryw/ synthetic trajectoryw/ real trajectoryAIME 2024average@326.77%17.91% (+11.14 %)4.38%33.23% (+28.85 %)pass@3242.11%57.57% (+15.46 %)35.15%75.66% (+40.51 %)maj@3210.50%27.13% (+16.63 %)0.01%51.64% (+51.63 %)AIME 2025average@325.21%18.24% (+13.03 %)3.65%29.79% (+26.14 %)pass@3225.56%48.42% (+22.86 %)22.22%72.88% (+50.66 %)maj@3212.08%29.18% (+17.10 %)0.10%45.82% (+45.72 %)

3.2 Diverse Data Maintains High Entropy in Training

Motivation.
Most existing works (Feng et al., 2025; Shang et al., 2025; Li et al., 2025d; Dong et al., 2025a) focus on purely mathematical datasets for RL training, aiming to enhance problem-solving ability on reasoning-heavy benchmarks. While intuitive, this narrow scope overlooks a critical factor: dataset diversity. Prior discussions of diversity in multi-task RL (Havrilla et al., 2024; Shen et al., 2025) only emphasize outcome-level benefits. However, how diversity influences the training dynamics, especially policy entropy and exploration efficiency, remains underexplored.

Setup.
We construct our RL dataset with higher diversity in appendix A.4, for comparison, we choose DAPO-Math-17k as the baseline. We utilize GRPO-TCR (mentioned in section2.3) to fine-tune Qwen3-4B-RA-SFT and Qwen2.5-7B-RA-SFT under identical hyperparameters and training budgets.

Figure 2: Comparison between our dataset with higher diversity and the ReTool dataset, which only contains math problems. Left is the average@32 accuracy on AIME2025 during training based on two different dataset. Right is the policy entropy during the training process.

Result.
As shown on the right in fig.2, training with the diverse dataset leads to significantly higher entropy gain during the early stage and sustains this entropy at a higher level throughout convergence. This indicates that diverse data directly drives richer exploration behaviors. Moreover, in the left figures of fig.2, we observe faster and more efficient learning: with our diverse dataset, the agent achieves over 50% average@32 accuracy on AIME2025 within only 150 steps, while the DAPO-Math baseline requires 220 steps to reach the same level.

Analysis. We interpret entropy as a proxy for exploration breadth: higher entropy means the policy continues to consider diverse reasoning paths rather than prematurely collapsing to a narrow deterministic strategy (We will discuss the entropy mechanism in detail in section4.2 and section4.3). Thus, dataset diversity not only improves outcome metrics but also reshapes the training dynamics by maintaining exploration capacity, making RL both faster and more stable.

3.3 Model-Aware Datasets for More Effective RL

Motivation.
During training, we observed a clear divergence between two models of different capacity: Qwen3-4B-Instruct-2507 exhibited consistent and sustained policy improvement, while Qwen2.5-7B-Instruct failed to improve despite identical algorithms and datasets, rapidly encountering a bottleneck. Specifically, the average reward of Qwen2.5 stagnated around zero, while Qwen3 consistently achieved positive rewards. This illustrates a competence–difficulty mismatch: when the base policy is too weak relative to the dataset, it cannot extract meaningful gradients for policy updating. To address this issue, we construct a model-aware RL dataset that adapts the task distribution to the capacity of the model.

Setup.
We use our SFT model to perform 8 rollouts per problem on the 30k RL dataset, taking the proportion of correct solutions as a proxy for problem difficulty with respect to the given model. After trajectory verification, we discard the problems with 0% or 100% accuracy (which provide no learning signal) and label the remainder with three difficulty levels: easy (accuracy ≥0.75\geq 0.75), medium (0.75>0.75> accuracy >0.25>0.25), and hard (accuracy ≤0.25\leq 0.25). Since the Qwen3 model already shows effective training on the full dataset, we use its empirical difficulty histogram as the target distribution. Based on this distribution, we curate a model-aware dataset tailored for Qwen2.5 and retrain it using the same GRPO-TCR algorithm and hyperparameters as in the original setting.

Result.
As shown in fig.3, training with the curated model-aware dataset yields significantly more effective improvement than with the unfiltered dataset. Moreover, fig.3 shows that the average reward rises substantially, producing stronger and more consistent gradient signals. Consequently, it provides more valid rewards for the computation of advantage, amplifying the gradient signals and leading to more effective and stable RL training. After breaking the performance bottleneck, we can collect the model-aware dataset based on its current ability for more effective training.

Figure 3: The comparison and analysis between the impact of the 30k full dataset and our tailored dataset for Qwen2.5-RA-SFT on subsequent RL training. Left is the average@32 performance on AIME2025. Right is the analysis for the average reward during training.

4 Algorithmic Design and Training Dynamics in Agentic RL

Recent advancements in RLVR for reasoning LLMs, especially GRPO-based methods (Yu et al., 2025; Dong et al., 2025b; Zheng et al., 2025; Zhao et al., 2025; Liu et al., 2025a; b) have demonstrated that there are many possible techniques that could further enhance policy optimization. Other works (Cui et al., 2025; Deng et al., 2025; Agarwal et al., 2025; Chen et al., 2025) focus on exploring the training dynamics (e.g., entropy and pass@k) to explain why and how these improvements could emerge.
For agentic RL, however, it remains unclear (i) what techniques work best for policy optimization, (ii) what is the relationship between the exploration(pass@k)-exploitation(average@k), and (iii) how does entropy affect training effectiveness, stability, and final performance.

Figure 4: The overall performance of our constructed three recipes: GRPO-T, GRPO-TCR, and GRPO-SCR on AIME2024/AIME2025 benchmark.

4.1 The impact of the RLVR techniques on Agentic RL

Setup. In this section, we conduct our experiments based on three different recipes: GRPO-TCR, GRPO-SCR and GRPO-T as mentioned in section2.3. Based on the experiment results, we aim to pinpoint simple yet effective techniques that deliver consistent improvements in final performance and training efficiency. Specifically, we utilize the hyperparameters and reward functions mentioned in section2.2 to train both Qwen3-4B-RA-SFT and Qwen2.5-7B-RA-SFT based on our complete RL dataset to compare the training dynamics of different recipes. For GRPO-TCR, the ϵhigh\epsilon_{\text{high}} is set to 0.28, and ϵlow\epsilon_{\text{low}} is set to 0.20, for GRPO-SCR, the ϵhigh\epsilon_{\text{high}} is set to 0.0004 and ϵlow\epsilon_{\text{low}} is set to 0.0003. For GRPO-T, the ϵ\epsilon is set to 0.20 and the reward function is rout+toolr_{\text{out+tool}}. For both recipes that incorporated with overlong reward shaping, the reward is denoted as rϕ=rout+tool+rlengthr_{\phi}=r_{\text{out+tool}}+r_{\text{length}}. Specifically, we also use three metrics to comprehensively evaluate the impact of the applied RLVR techniques on AIME2024 and AIME2025 benchmarks.

Result. First, we compare GRPO-TCR and GRPO-T to investigate the impact of clip higher and overlong reward shaping on Agentic RL. Specifically, for Qwen3-4B-RA-SFT, GRPO-TCR has achieved remarkable improvements compared to GRPO-T on AIME2024/AIME2025. It achieves 70.93%/68.13% with an initial accuracy of 29.79% and 33.23% on average@32 metric within only 450 steps. In contrast, GRPO-T only achieves the best average@32 performance of 54.7%/ 40.93% on AIME2024/AIME2025, which GRPO-TCR could achieve within only 100 training steps, utilizing only 25% of the training computation of GRPO-T. The results indicate that simply applying clip higher and overlong reward shaping techniques could effectively improve the agentic reasoning performance and the efficiency of agentic RL.

Then, we compare GRPO-TCR and GRPO-SCR to investigate the impact of loss aggregation granularity on agentic RL. We observe that for Qwen2.5-7B-RA-SFT, which has weak initial performance and exploration capabilities, token-level loss and sequence-level loss achieve comparable average@32 performance on AIME2024/2025. However, for Qwen3-4B-RA-SFT, which has stronger initial performance and exploration capabilities, token-level loss consistently outperforms sequence-level loss in terms of convergence speed and peak accuracy. Specifically, token-level loss exceeds sequence-level loss by 3.95% on AIME24 and 3.86% on AIME25 under the same training budget. It is because the token-level loss ensures each token contributes equally to the optimization signal, thereby leveraging the model’s exploratory capacity more effectively. This suggests that token-level loss could improve training efficiency and agentic reasoning ability compared to sequence-level loss for models with better initial performance and exploration ability.

4.2 Exploration–Exploitation Dynamics in Agentic RL

Motivation.
Prior studies (Chen et al., 2025; Deng et al., 2025) show that in conventional RL, most gains in the pass@k metric come from the SFT stage, where diverse external solutions expand the model’s ability bound. Subsequent RL training primarily strengthens existing internal solutions, yielding a more deterministic policy that improves exploitation (Pass@1) but often suppresses further exploration (Pass@k). However, this characterization is largely based on a self-contained generation process, where the model relies solely on its internal capacity. In contrast, agentic RL fundamentally changes this dynamic: the model actively interacts with external tools during reasoning, learning not just to refine internal solutions but to optimize its ability to explore, select, and exploit external resources. This opens the question of whether the classical exploration–exploitation trade-off still holds, or whether agentic RL enables a qualitatively different trajectory where exploration is maintained or even amplified through tool use.

Observation.
Our experiments in fig.4 show that in agentic RL, both GRPO-TCR and GRPO-SCR achieve substantial and simultaneous improvements in pass@k and average@k (over 10% gains on AIME2024/AIME2025). However, this improvement does not hold unconditionally: with the baseline GRPO-T, we still observe the conventional trade-off where exploration is suppressed during training. We attribute this to the overly conservative design of GRPO-T: the combination of a restrictive clip upper bound and strong KL-regularization creates severe constraints on distribution shift, forcing the model to maintain self-contained generation patterns and preventing it from fully leveraging tool interactions.

Analysis.
As we mentioned above, the multi-turn interactions with tools in agentic reasoning also introduce external information during training. The information from the external tools enables models to “think smarter” than purely ”think longer” by developing more advanced cognitive abilities that autonomously utilize the tools to reason more efficiently, and learn from the feedback signals. Consequently, incentivizing these abilities through agentic reinforcement learning recipe like GRPO-TCR and GRPO-SCR helps to further improve the pass@k performance and lead to higher ability bound for more effective training and better average@k performance.

What’s more, we also observe that the gap between average@k and pass@k emerges as a critical bottleneck for training efficiency. RL training can be interpreted as a process of progressively converting the model’s pass@k performance into actual average@k gains, with the achievable improvement bounded by an intrinsic ceiling determined by this gap. This perspective highlights that not only the absolute level of pass@k but also the magnitude of the average–pass discrepancy governs how much exploration can be effectively transformed into exploitation during training.

Figure 5: The analysis for the policy entropy in agentic RL training. 

4.3 When High Entropy Drives Better Efficiency

Motivation.
Recently, entropy has become a central signal in RL research, yet prescriptions diverge: some advocate minimizing it for more deterministic policies (Agarwal et al., 2025; Cheng et al., 2025b), while others exploit high-entropy tokens to foster exploration and avoid early collapse (Cui et al., 2025; Wang et al., 2025b; a). These views largely arise from conventional RL. In agentic RL, ARPO (Dong et al., 2025b) observes entropy spikes after tool calls and leverages them via adaptive rollouts, implying that tool-call steps induce useful uncertainty. This raises a central question: is higher/lower entropy generally beneficial, or is there an optimal range beyond which training destabilizes?

Observation.
We investigate by visualizing entropy trajectories and relating them to training efficiency and reasoning performance. As shown in fig.4 and fig.5, GRPO-T exhibits an early entropy collapse, whereas the entropy for models (trained with GRPO-TCR and GRPO-SCR) with better performance rises faster and stabilizes at a higher level. This suggests that greater policy entropy is associated with more effective agentic RL training and stronger agentic reasoning, which is not aligned with the entropy minimization theory in conventional RL. Motivated by our observation, and noting that ϵhigh\epsilon_{\text{high}} controls the exploration budget, we utilize different ϵhigh\epsilon_{\text{high}} to test for an optimal entropy regime under identical training conditions.

Setup. To investigate the optimal entropy regime, we conduct experiments with different clip upper bounds, including 0.28,0.315,0.35 for GRPO-TCR and keep all other settings the same and train Qwen2.5-7B-RA-SFT and Qwen3-4B-RA-SFT. We report the three metrics including average@32, pass@32, and maj@32 to comprehensively evaluate when high entropy could improve training efficiency and when high entropy would lead to the collapse of the agentic reasoning performance.

Results.
As shown in fig.6, we observe a non-monotonic relation between the clip upper bound ϵhigh\epsilon_{\text{high}} and training efficiency. Specifically, for Qwen2.5-7B-RA-SFT, modestly increasing ϵhigh\epsilon_{\text{high}} (e.g., 0.28→0.3150.28\rightarrow 0.315) accelerates performance improvements. It also improves learning efficiency across both models. For example, with ϵhigh=0.315\epsilon_{\text{high}}=0.315, we achieve equivalent performance 40% faster, reaching the same results at step 60 that would otherwise require 100 steps when ϵhigh=0.28\epsilon_{\text{high}}=0.28. However, pushing it further yields diminishing returns. For example, when we train Qwen3-4B-RA-SFT with a higher ϵhigh=0.35\epsilon_{\text{high}}=0.35 it leads to worse training effectiveness despite a faster initial lift compared to a lower ϵhigh\epsilon_{\text{high}}, which is set to 0.28. In summary, a higher ϵhigh\epsilon_{\text{high}} expands the exploration budget and improves short-horizon progress, yet overly aggressive clipping eventually slows convergence, introduces excessive entropy, which will lead to suboptimal agentic reasoning performance. It also indicates that when the entropy becomes too high, it will also lead to instability in training.

Figure 6: The analysis of clipping strategy on AIME2025 benchmark. Left is the analysis for Qwen2.5-7B models. Right is the analysis for Qwen3-4B models.

5 Reasoning Modes in Agentic RL

A central question in agentic RL is how an agent should allocate its reasoning budget between internal inference tokens and external tool calls. Should an effective agent rely on frequent tool interactions with minimal internal thinking, or invest more inference tokens in deliberate reasoning before acting? To address this, we characterize two regimes: (i) tool-call scaling, where the agent engages in many short-think rounds with frequent tool usage, and (ii) internal reasoning scaling, where the agent performs deeper reasoning before issuing fewer but more targeted tool calls. This section empirically investigates these reasoning modes and identifies which strategy leads to more efficient and effective agentic reasoning.

Figure 7: Analysis of the average number of tool calls and average response length per round in Agentic RL. 

5.1 When Fewer Tool Calls Lead to Better Tool Use

Setup. Based on the main experiment in fig.4, we first visualize the average number of tool calls and average response length per interaction round in the training process. To further investigate the rationality and efficiency of tool usage, we filter out the correctly executed tool calling queries and calculate the average success rate of the tool calls.

Result.
As shown in fig.7, we identify two distinct modes in agentic reasoning: Reactive Mode (short-think + frequent tool calls) and Deliberative Mode (deliberate-think + fewer tool calls). Relating these modes to overall performance (average@32 in fig.4), we find that the strongest models consistently adopt the Deliberative Mode, while weaker models predominantly fall into the Reactive Mode. Tool-call efficiency further explains this performance gap. As shown in fig.8, Deliberative Mode agents achieve over 70% success in tool usage, indicating that careful reasoning before acting enables highly accurate and effective calls. In contrast, Reactive Mode agents exhibit substantially lower success rates, as their rapid, frequent calls often yield ineffective or erroneous results. Together, these findings highlight a clear quality-over-quantity principle: agents that invest more inference tokens in deliberate reasoning ultimately make fewer but more successful tool calls, leading to higher efficiency of tool use and superior task performance. Thoughtful, selective tool usage thus consistently outperforms frequent but poorly targeted interactions.

Figure 8: Tool-use efficiency comparison across different models.

5.2 Limitations of Current Long-CoT Models in Agentic RL

Motivation.
Motivated by our findings in section5.1 that scaling internal reasoning before tool calls improves agentic reasoning, we explore whether incorporating Long-CoT models could further enhance agentic reasoning performance. Previous works combining Long-CoT with search engines (Search-R1 (Jin et al., 2025), R1-Searcher (Song et al., 2025) and Search-o1 (Li et al., 2025b)) have demonstrated success on knowledge-intensive tasks. Building on this foundation, we investigate whether such Long-CoT reasoning capabilities can be effectively used to benefit agentic reinforcement learning with code interpreters on reasoning-intensive problems.

Setup.
Here we directly utilize Long-CoT LLMs like Qwen3-4B-Thinking-2507 as the starting point for RL, and utilize GRPO-TCR algorithm with the same training settings in fig.4. We report the average@k and the average number of tool calls throughout training.

Result.
As shown in fig.9, we observed that the model achieved strong average@32 performance in the beginning, but it hardly call the tools. As training progressed, the average number of tool calls gradually converged to zero, indicating that Long-CoT models tend to avoid invoking tools and rely solely on internal reasoning when encountering reasoning-intensive tasks.
This behavior varies significantly by task type. For reasoning-intensive tasks, the Long-CoT models tend to utilize their internal reasoning capability to solve these tasks, thus focusing exclusively on the problem rather than analyzing the user instruction or considering calling available tools. Conversely, when confronting knowledge-intensive tasks that exceed their internal reasoning capabilities, these models could actively utilize available tools such as search engines to complete the tasks.

Figure 9: The training dynamics of current Long-CoT with Agentic RL.

5.3 Integrating Long-CoT with Agentic Reasoning

Motivation
Since we observe that current Long-CoT LLMs overly rely on internal reasoning and avoid calling the tools for reasoning tasks in section5.2, we further explore how to effectively integrate Long-CoT with agentic reasoning.

Setup. To address the limitation that Long-CoT models often avoid tool calls in reasoning-intensive tasks, we explicitly align them with agentic reasoning through SFT. Specifically, we leverage our SFT dataset (as described in section3) to initialize Long-CoT models, thereby guiding them to balance deliberate internal reasoning with appropriate tool usage. This initialization enables the models to enter reinforcement learning (RL) training with a prior for effective tool invocations.

Result. As shown in fig.10, the SFT-initialized Long-CoT model actively utilizes tools while retaining strong internal reasoning, demonstrating significantly improved agentic RL performance compared to the non-initialized version. However, despite this initial advantage, Long-CoT models ultimately achieve only comparable performance to instruction-based models rather than surpassing them. Analysis of response length evolution in fig.10 reveals contrasting optimization dynamics.

Analysis. Instruction-based models concentrate on developing agentic reasoning capabilities from scratch without specialized internal reasoning biases, enabling continuous growth through focused tool-use learning. However, Long-CoT models face conflicting objectives: their ingrained internal reasoning patterns contradict agentic reasoning paradigms, forcing a scaling and pruning process where gains in agentic reasoning are offset by the need to suppress over-thinking behaviors. This dual optimization burden fragments learning efficiency, allowing instruction-based models to achieve superior scaling through concentrated capability improvement rather than divided attention between acquiring new skills and unlearning incompatible reasoning paradigms. It reveals that direct agentic RL training, where models develop reasoning and tool-use capabilities jointly from scratch, outperforms training based on Long-CoT models with conflicting internal reasoning paradigms.

Figure 10: Comparison between the instruction-based models and Long-CoT reasoning models. Left is the average@32 performance on AIME2025. Right is the average response length during training.

6 Contributions and Comparison on Challenging Benchmarks

Beyond the insights gained from our comprehensive study, we make the following contributions:

(i)

A 3k high-quality end-to-end agentic SFT dataset,

(ii)

A 30k diverse and effective RL dataset,

(iii)

Two strong cold-start models (Qwen2.5-7B-RA-SFT and Qwen3-4B-RA-SFT) that enable broad downstream RL research,

(iv)

A strong baseline model, DemyAgent-4B, that validates our training insights and achieves SOTA performance against significantly larger models.

Training Recipe.
DemyAgent-4B is trained using our complete 30k RL dataset with the GRPO-TCR algorithm, applied to Qwen3-4B-RA-SFT as the base model.
Following our study insights on clip range optimization, we use a higher clip upper bound (ϵhigh=0.315\epsilon_{\text{high}}=0.315) to balance exploration and constraint satisfaction.

Key Results.
We evaluate on challenging reasoning benchmarks under two paradigms (table2):
(1) Self-Contained Reasoning, where models rely solely on internal reasoning capabilities, and
(2) Agentic Reasoning, where models leverage external tools such as code interpreters and search engines.
As demonstrated in table2, despite having only 4B parameters, DemyAgent-4B matches or even outperforms much larger models (14B/32B) across challenging benchmarks.
Notably, DemyAgent-4B achieves state-of-the-art agentic reasoning performance, surpassing ReTool-32B (Feng et al., 2025) and rStar2-Agent-14B (Shang et al., 2025), and even outperforming Long-CoT models like DeepSeek-R1-Zero on AIME2025.

These results further demonstrate that our simple yet effective training recipe unlocks strong agentic capabilities in compact models.

Table 2: Overall results on challenging reasoning benchmarks grouped by domain. Higher is better (%). The top two results are highlighted in bold and underlined. The results with * are our self-evaluated results for self-contained reasoning. The prompts for agentic reasoning and self-contained reasoning could be found in appendix B.MATHScienceCodeMethodAIME2024AIME2025GPQA-DiamondLiveCodeBench-v6Self-Contained ReasoningQwen2.5-7B-Instruct16.7∗16.7^{*}10.0∗10.0^{*}31.3∗31.3^{*}15.2Qwen3-4B-Instruct-250763.3∗63.3^{*}47.452.0∗52.0^{*}35.1Qwen2.5-72B-Instruct18.915.049.0-DeepSeek-V339.228.859.116.1DeepSeek-R1-Distill-32B70.046.759.6-DeepSeek-R1-Zero (671B)71.053.559.6-Agentic ReasoningQwen2.5-7B-Instruct4.85.625.512.2Qwen3-4B-Instruct-250717.916.344.323.0ToRL-7B43.330.0--ReTool-32B72.554.3--Tool-Star-3B2016.7--ARPO-7B30.030.053.018.3rStar2-Agent-14B80.669.860.9-DemyAgent-4B (Ours)72.670.058.526.8

7 Related Work

Tool-integrated Reasoning.
Tool-integrated reasoning (TIR) enables large language models (LLMs) to leverage external tools such as code interpreters and search engines in order to overcome the limitations of pure internal reasoning. This approach extends the computational and knowledge capacity of LLMs and allows them to tackle tasks that are infeasible through text-only reasoning. Previous TIR methods are based on prompting engineering, such as PoT (Chen et al., ), template-augmented reasoning paradigm like BoT (Yang et al., 2024b), and supervised finetuning (SFT) methods. SFT-based methods like ToRA (Gou et al., ), Tool-former (Schick et al., 2023), and Qwen-Math-TIR (Yang et al., 2024a) train models on datasets containing tool invocation demonstrations, teaching LLMs to follow predefined patterns of tool use. Similarly, works such as ReAct (Yao et al., ), MathCoder (Wang et al., 2024), and Mario (Liao et al., 2024) incorporate tool usage examples into training data so that LLMs can interleave reasoning steps with external tool calls. However, these SFT-based approaches have inherent limitations. Since models are compelled to use tools according to the distribution of training data, they cannot develop adaptive strategies for tool use, such as deciding when to invoke a tool, how often to call it, or how to balance tool use with internal reasoning. As a result, previous SFT-driven TIR methods improve tool-following ability but lack the flexibility and autonomy required for robust agentic behavior.

Agent Reinforcement Learning.
Compared with SFT-based tool-integrated reasoning that merely imitates demonstrations of tool usage, it is more promising to leverage reinforcement learning algorithms (Shao et al., 2024; Guo et al., 2025; Yu et al., 2025; Liu et al., 2025a; Zhao et al., 2025) to train more capable agents. Agent Reinforcement Learning (Agent RL) explicitly models tool invocation as part of the action space and optimizes adaptive strategies through outcome-driven rewards, enabling agents to move beyond static supervision toward more flexible and effective reasoning behaviors. Representative works include search-oriented approaches such as Search-R1 (Jin et al., 2025) and R1-Searcher (Song et al., 2025), which train LLMs to interleave reasoning with search engine queries. ToRL (Li et al., 2025d) demonstrates that RL can directly optimize tool use at scale, enabling models to discover effective invocation strategies. ReTool (Feng et al., 2025) further highlights the benefit of RL by teaching models not only to use tools but also to decide when and how to call them. More recently, ZeroTIR (Mai et al., 2025) takes a complementary perspective by analyzing scaling laws in RL-based tool use, showing how strategic code invocation gradually emerges as training progresses. More general frameworks such as ARTIST (Singh et al., 2025), Tool-Star (Dong et al., 2025a), and Auto-TIR (Wei et al., 2025), further extend Agent RL to the setting of multi-tool integration. ARTIST focuses on multi-turn reasoning where agents autonomously decide not only whether to call a tool but also which tool to invoke in complex reasoning chains. Together, these frameworks highlight the frontier of Agent RL: building agents that generalize beyond single-tool domains to flexibly coordinate multiple tools under reinforcement learning objectives. However, current Agent RL methods are often tied to specific workflows and lack a systematic understanding of how reinforcement learning can more generally improve tool-use ability. Key issues such as algorithm design, tool-call efficiency, and reliance on synthetic trajectories remain underexplored.

Entropy Mechanism for Reinforcement Learning.
Recent advances in reinforcement learning have markedly improved LLM reasoning, yet entropy collapse—the failure to maintain exploration ability under outcome-driven optimization, which remains a central obstacle for effective scaling of RL. At the mechanism level, Cui et al. (2025) formalizes how entropy governs exploration and identifies collapse as a key bottleneck; deepening this view, Wang et al. (2025b) show that a minority of high-entropy tokens, rather than the low-entropy majority, disproportionately drives effective learning. At the system level, He et al. (2025) provide empirical evidence that preserving entropy is essential for stable, long-horizon reasoning. Building on these insights, Cheng et al. (2025a) and Dong et al. (2025b) incorporate entropy-aware objectives into RL to better balance exploration and exploitation in multi-turn reasoning. More recently, Deng et al. (2025) propose exploration mechanisms in Reinforcement learning with verifiable rewards (RLVR), consolidating entropy as a controllable signal, not merely a regularizer for promoting exploration, stability, and sustained improvement in agentic RL.

8 Discussion and Future Work

In this section, we outline the challenges and potential future directions of reinforcement learning in Agentic RL.

8.1 Data-Fuel Scarcity

Based on our analysis in section3, we believe that the training data plays a crucial role in Agentic RL, which determines both the training effectiveness and the scaling upper bound for agentic reasoning. However, for the SFT dataset that requires full end-to-end generated trajectories, it is still computationally costly to collect. Works like s1 (Muennighoff et al., ) and limo (Ye et al., 2025) have demonstrated that the effectiveness of curating a small-sized but high-quality distilled dataset could significantly enhance the internal reasoning ability of LLMs. These findings suggest that we could also develop a recipe for how to curate small-sized high-quality SFT datasets, which could not only alleviate the scarcity of data in Agentic RL, but it could also improve our understanding of agentic behaviors through the insights of curating these datasets.

8.2 Effective Scaling of Agentic Reasoning

As demonstrated in section5, deliberate reasoning before tool invocation emerges as a superior mode for agentic problem-solving, yet effectively scaling such reasoning behaviors remains challenging. Our analysis in section5.2 reveals fundamental limitations in current open-source LLMs for agentic reasoning tasks. Based on that, exploring agent-specific reasoning frameworks that prioritize high-level strategic planning and efficient tool orchestration, rather than relying heavily on the model’s internal reasoning capabilities, could be a promising direction for future research. Such agent-oriented reasoning chains should emphasize problem decomposition into tool-executable subtasks, strategic tool selection, and synthesis of tool outputs. This shift from reasoning-centric to high-level tool-planning-centric approaches necessitates new training methodologies and evaluation frameworks specifically tailored for agentic workflows, potentially leading to more capable autonomous agents that can navigate complex multi-step scenarios with greater reliability. We look forward to future research on exploring the compatible inference scaling methods for agentic reasoning.

8.3 Additional Application Scenarios in Agentic Reasoning

In this work, we mainly focus on the code interpreter as a tool for agentic reasoning and find valuable insights and recipes. But we can also generalize our insights from a static and single tool environment to multi-tool and optimizable environment. For example, in this multi-tool environment, the insights of encouraging exploration in agentic RL may still hold. In a more complex environment, the correct solution to a problem consists of different possible combinations of tools, which requires more exploration for the optimal strategy and the ability to select the most effective tools for corresponding tasks.

9 Limitations

In this work, we investigate reinforcement learning for agentic reasoning from three key perspectives: data, algorithm, and reasoning mode. However, our experiments are conducted on small-sized models (e.g, 4B/7B). While this has already provided valuable insights into challenges and design choices for Agentic RL, recent works (Vattikonda et al., 2025) has underscores RL’s extreme hyperparameter sensitivity, especially for larger-sized models. In particular, larger models may demonstrate different sensitivities to reward signals, require different exploration strategies, or exhibit more robust reasoning patterns that interact differently with RL training dynamics. We leave a more comprehensive study of RL with larger-sized models in broader agentic settings as an important future work direction.

10 Conclusion

In this work, we conducted a comprehensive empirical study of reinforcement learning for agentic reasoning across the axes of data, algorithm, and reasoning mode. For the perspective of data curation, our findings highlight that real end-to-end multi-turn trajectories are indispensable for building strong agentic SFT foundations, while diverse and model-aware RL datasets sustain exploration and yield stable training. Algorithmically, we show that simple but effective design choices, such as clip higher, reward shaping, and token-level loss, which substantially improve training effectiveness, and that maintaining appropriate entropy is the key driver of effective agentic RL. On the reasoning side, we find a quality-over-quantity principle: fewer but more deliberate tool calls lead to superior efficiency, while Long-CoT priors often hinder tool adoption and slow down scaling. With our recipes, we effectively improve the agentic reasoning of LLMs, and we conduct a comprehensive evaluation across challenging benchmarks, including AIME2024/2025, GPQA-Diamond, and LiveCodeBench-v6, which further validates our insights.

References

Agarwal et al. (2025)
Shivam Agarwal, Zimin Zhang, Lifan Yuan, Jiawei Han, and Hao Peng.

The unreasonable effectiveness of entropy minimization in llm reasoning.

arXiv preprint arXiv:2505.15134, 2025.

(2)
Wenhu Chen, Xueguang Ma, Xinyi Wang, and William W Cohen.

Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks.

Transactions on Machine Learning Research.

Chen et al. (2025)
Zhipeng Chen, Xiaobo Qin, Youbin Wu, Yue Ling, Qinghao Ye, Wayne Xin Zhao, and Guang Shi.

Pass@ k training for adaptively balancing exploration and exploitation of large reasoning models.

arXiv preprint arXiv:2508.10751, 2025.

Cheng et al. (2025a)
Daixuan Cheng, Shaohan Huang, Xuekai Zhu, Bo Dai, Wayne Xin Zhao, Zhenliang Zhang, and Furu Wei.

Reasoning with exploration: An entropy perspective.

arXiv preprint arXiv:2506.14758, 2025a.

Cheng et al. (2025b)
Daixuan Cheng, Shaohan Huang, Xuekai Zhu, Bo Dai, Wayne Xin Zhao, Zhenliang Zhang, and Furu Wei.

Reasoning with exploration: An entropy perspective.

arXiv preprint arXiv:2506.14758, 2025b.

Cui et al. (2025)
Ganqu Cui, Yuchen Zhang, Jiacheng Chen, Lifan Yuan, Zhi Wang, Yuxin Zuo, Haozhan Li, Yuchen Fan, Huayu Chen, Weize Chen, et al.

The entropy mechanism of reinforcement learning for reasoning language models.

arXiv preprint arXiv:2505.22617, 2025.

Deng et al. (2025)
Jia Deng, Jie Chen, Zhipeng Chen, Daixuan Cheng, Fei Bai, Beichen Zhang, Yinqian Min, Yanzipeng Gao, Wayne Xin Zhao, and Ji-Rong Wen.

From trial-and-error to improvement: A systematic analysis of llm exploration mechanisms in rlvr.

arXiv preprint arXiv:2508.07534, 2025.

Dong et al. (2025a)
Guanting Dong, Yifei Chen, Xiaoxi Li, Jiajie Jin, Hongjin Qian, Yutao Zhu, Hangyu Mao, Guorui Zhou, Zhicheng Dou, and Ji-Rong Wen.

Tool-star: Empowering llm-brained multi-tool reasoner via reinforcement learning.

arXiv preprint arXiv:2505.16410, 2025a.

Dong et al. (2025b)
Guanting Dong, Hangyu Mao, Kai Ma, Licheng Bao, Yifei Chen, Zhongyuan Wang, Zhongxia Chen, Jiazhen Du, Huiyang Wang, Fuzheng Zhang, et al.

Agentic reinforced policy optimization.

arXiv preprint arXiv:2507.19849, 2025b.

Fan et al. (2025)
Run-Ze Fan, Zengzhi Wang, and Pengfei Liu.

Megascience: Pushing the frontiers of post-training datasets for science reasoning.

arXiv preprint arXiv:2507.16812, 2025.

Feng et al. (2025)
Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang, Jinxin Chi, and Wanjun Zhong.

Retool: Reinforcement learning for strategic tool use in llms.

arXiv preprint arXiv:2504.11536, 2025.

(12)
Zhibin Gou, Zhihong Shao, Yeyun Gong, Yujiu Yang, Minlie Huang, Nan Duan, Weizhu Chen, et al.

Tora: A tool-integrated reasoning agent for mathematical problem solving.

In The Twelfth International Conference on Learning Representations.

Guo et al. (2025)
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al.

Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning.

arXiv preprint arXiv:2501.12948, 2025.

Havrilla et al. (2024)
Alex Havrilla, Andrew Dai, Laura O’Mahony, Koen Oostermeijer, Vera Zisler, Alon Albalak, Fabrizio Milo, Sharath Chandra Raparthy, Kanishk Gandhi, Baber Abbasi, et al.

Surveying the effects of quality, diversity, and complexity in synthetic data from large language models.

arXiv preprint arXiv:2412.02980, 2024.

He et al. (2025)
Jujie He, Jiacai Liu, Chris Yuhao Liu, Rui Yan, Chaojie Wang, Peng Cheng, Xiaoyu Zhang, Fuxiang Zhang, Jiacheng Xu, Wei Shen, et al.

Skywork open reasoner 1 technical report.

arXiv preprint arXiv:2505.22312, 2025.

(16)
Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica.

Livecodebench: Holistic and contamination free evaluation of large language models for code.

In The Thirteenth International Conference on Learning Representations.

Jin et al. (2025)
Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan Arik, Dong Wang, Hamed Zamani, and Jiawei Han.

Search-r1: Training llms to reason and leverage search engines with reinforcement learning.

arXiv preprint arXiv:2503.09516, 2025.

Li et al. (2025a)
Kuan Li, Zhongwang Zhang, Huifeng Yin, Liwen Zhang, Litu Ou, Jialong Wu, Wenbiao Yin, Baixuan Li, Zhengwei Tao, Xinyu Wang, et al.

Websailor: Navigating super-human reasoning for web agent.

arXiv preprint arXiv:2507.02592, 2025a.

Li et al. (2025b)
Xiaoxi Li, Guanting Dong, Jiajie Jin, Yuyao Zhang, Yujia Zhou, Yutao Zhu, Peitian Zhang, and Zhicheng Dou.

Search-o1: Agentic search-enhanced large reasoning models.

arXiv preprint arXiv:2501.05366, 2025b.

Li et al. (2025c)
Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yutao Zhu, Yongkang Wu, Ji-Rong Wen, and Zhicheng Dou.

Webthinker: Empowering large reasoning models with deep research capability.

arXiv preprint arXiv:2504.21776, 2025c.

Li et al. (2025d)
Xuefeng Li, Haoyang Zou, and Pengfei Liu.

Torl: Scaling tool-integrated rl.

arXiv preprint arXiv:2503.23383, 2025d.

Liao et al. (2024)
Minpeng Liao, Wei Luo, Chengxi Li, Jing Wu, and Kai Fan.

Mario: Math reasoning with code interpreter output-a reproducible pipeline.

CoRR, 2024.

Liu et al. (2025a)
Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin.

Understanding r1-zero-like training: A critical perspective.

arXiv preprint arXiv:2503.20783, 2025a.

Liu et al. (2025b)
Zihe Liu, Jiashun Liu, Yancheng He, Weixun Wang, Jiaheng Liu, Ling Pan, Xinyu Hu, Shaopan Xiong, Ju Huang, Jian Hu, et al.

Part i: Tricks or traps? a deep dive into rl for llm reasoning.

arXiv preprint arXiv:2508.08221, 2025b.

Mai et al. (2025)
Xinji Mai, Haotian Xu, Weinong Wang, Jian Hu, Yingying Zhang, Wenqiang Zhang, et al.

Agent rl scaling law: Agent rl with spontaneous code execution for mathematical problem solving.

arXiv preprint arXiv:2505.07773, 2025.

(26)
Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candes, and Tatsunori Hashimoto.

s1: Simple test-time scaling.

In Workshop on Reasoning and Planning for Large Language Models.

Rafailov et al. (2023)
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn.

Direct preference optimization: Your language model is secretly a reward model.

Advances in neural information processing systems, 36:53728–53741, 2023.

Rein et al. (2024)
David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman.

Gpqa: A graduate-level google-proof q&a benchmark.

In First Conference on Language Modeling, 2024.

Schick et al. (2023)
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom.

Toolformer: Language models can teach themselves to use tools.

Advances in Neural Information Processing Systems, 36:68539–68551, 2023.

Schulman et al. (2017)
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.

Proximal policy optimization algorithms.

arXiv preprint arXiv:1707.06347, 2017.

Shang et al. (2025)
Ning Shang, Yifei Liu, Yi Zhu, Li Lyna Zhang, Weijiang Xu, Xinyu Guan, Buze Zhang, Bingcheng Dong, Xudong Zhou, Bowen Zhang, et al.

rstar2-agent: Agentic

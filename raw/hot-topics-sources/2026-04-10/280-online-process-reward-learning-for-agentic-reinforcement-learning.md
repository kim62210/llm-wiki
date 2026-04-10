---
title: Online Process Reward Leanring for Agentic Reinforcement Learning
source_url: https://arxiv.org/html/2509.19199v1
final_url: https://arxiv.org/html/2509.19199v1
status: 200
content_type: text/html; charset=utf-8
topics: [Process Reward Models (PRM) 재부상]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.569385+00:00
---

# Online Process Reward Leanring for Agentic Reinforcement Learning

## 원본 URL

https://arxiv.org/html/2509.19199v1

## 추출 본문

Online Process Reward Leanring for Agentic Reinforcement Learning
1 Introduction

2 Preliminaries
Task formulation.

RL for LLMs.

Implicit reward modeling.

3 Method
3.1 Overview
Optimizing online PRM via DPO.

Policy learning with implicit step rewards.

3.2 Theoretical Analysis

4 Experiments
Benchmarks.

Baselines.

Evaluation.

Implementation details.

4.1 Main Results
Performance on benchmarks.

OPRL with different vanilla RL algorithms.

4.2 In-depth Analysis
Sample efficiency and training stability.

Reward signals and exploration efficiency.

4.3 Ablation Studies

5 Related Work

6 Conclusion and Limitations

A Algorithm

B Environment Details
WebShop.

VisualSokoban.

SOTOPIA.

C Training Details

D Additional Results

Online Process Reward Leanring for Agentic Reinforcement Learning

Xiaoqian Liu1,2,3,
Ke Wang2,
Yuchuan Wu2∗,
Fei Huang2
& Yongbin Li2
Jianbin Jiao1,
Junge Zhang3
1University of Chinese Academy of Sciences  2Tongyi Lab

3Institute of Automation, Chinese Academy of Sciences

liuxiaoqian23@mails.ucas.ac.cn
{wk258730,shengxiu.wyc,shuide.lyb}@alibaba-inc.comCorresponding authors

Abstract
Large language models (LLMs) are increasingly trained with reinforcement learning (RL) as autonomous agents that reason and act over long horizons in interactive environments.
However, sparse and sometimes unverifiable rewards make temporal credit assignment extremely challenging.
Recent work attempts to integrate process supervision into agent learning but suffers from biased annotation, reward hacking, high-variance from overly fine-grained signals or failtures when state overlap is rare.
We therefore introduce Online Process Reward Learning (OPRL), a general credit-assignment strategy for agentic RL that integrates seamlessly with standard on-policy algorithms without relying on additional rollouts or explicit step labels.
In OPRL, we optimize an implicit process reward model (PRM) alternately with the agent’s policy to transform trajectory preferences into implicit step rewards through a trajectory-based DPO objective.
These step rewards are then used to compute step-level advantages, which are combined with episode-level advantages from outcome rewards for policy update, creating a self-reinforcing loop.
Theoretical findings guarantee that the learned step rewards are consistent with trajectory preferences and act as potential-based shaping rewards, providing bounded gradients to stabilize training.
Empirically, we evaluate OPRL on three distinct agent benmarks, including WebShop and VisualSokoban, as well as open-ended social interactions with unverfiable rewards in SOTOPIA.
Crucially, OPRL shows superior performance over frontier LLMs and strong RL baselines across domains, achieving state-of-the-art results with higher sample-efficiency and lower variance during training.
Further analysis also demonstrates the efficient exploration by OPRL using fewer actions, underscoring its potential for agentic learning in real-world scenarios.

1 Introduction

LLMs are rapidly evolving from passive generators into autonomous agents that can reason, act, and adapt strategies over long horizons, including search and research agents (Jin et al., 2025; OpenAI, 2025a), mobile and web navigators (Furuta et al., 2024; Bai et al., 2024), software engineering assistants (Yang et al., 2025; Wei et al., 2025a), game players (Wang et al., 2025), and social or embodied intelligence (Liu et al., 2025; Lu et al., 2025).
Unlike conventional RL for LLM post-training in static, single-turn tasks (Ouyang et al., 2022; Shao et al., 2024), training LLM agents in dynamic, interactive environments faces particular challenges:
(1) rewards are typically sparse and delayed, complicating credit assignment to intermediate actions;
(2) trajectories are long and non-Markovian at the token level, with each step consisting of a chain-of-thought (CoT) (Wei et al., 2022) and an executable action, inflating variance when credit is pushed to individual tokens;
and (3) environments and counterparts are non-stationary, open-ended and often come with unveriafiable rewards (e.g, dialogues).
Consequently, trajectory-level optimization with a single outcome reward (Wang et al., 2025; Chen et al., 2025; Wei et al., 2025b) suffers from temporal credit assignment, yielding high-variance policy learning, brittle exploration, and limited gains on agent tasks.

Recent work has attempted to solve these problems particularly through process supervision in RL.
For example, Zeng et al. (2025); Zou et al. (2025); Zhang et al. (2025b) provide denser feedback at intermediate steps but require human annotation or hand-crafted heuristics that are costly, biased, and vulnerable to reward hacking.
Generative reward models (GRMs) (e.g, LLM-as-judge) (Liu et al., 2025; Zha et al., 2025) that predicts criticality or correctness for each step reduce annotation overhead but can be noisy and inconsistent across domains.
Token-level process reward models (PRMs) trained from outcome labels help in single-turn tasks (Yuan et al., 2025; Cui et al., 2025), but the rewards they offer tend to be overly fine-grained for agentic learning, amplifying variance and destabilizing training as trajectories grow.
Other approaches (Feng et al., 2025; Choudhury, 2025) compute step-wise advantages by grouping identical states, an assumption that fails in open-ended language environments where state overlap is rare.
Together, these limitations raise a core question for agentic RL: How can we design a credit assignment strategy that is label-efficient and stable, scales to long-horizon, multi-turn interactions, and remains robust and generalizable to both verifiable and unverifiable rewards in open-ended environments?

To address this, we propose Online Learning Process Rewards (OPRL), a general credit assignment strategy for LLM agents. OPRL trains a PRM alongside the policy using only on-policy trajectories and their outcome preferences.
At each training step, the current policy generates rollouts, which are ranked by a rule-based verifier or an outcome reward model (ORM) to form positive–negative trajectory pairs. We then update the PRM with a DPO-derived objective on these pairs.
The updated PRM induces an implicit reward for each action by measuring its relative preference over the previous policy snapshot. Since this reward is computed per turn, it provides dense feedback to guide exploration while staying coarse enough to keep variance under control.
Policy optimization then combines two complementary advantages: an episode-level advantage from outcome rewards and a step-level advantage from the implicit step rewards, capturing both global task success and the contribution of individual actions.
OPRL is compatible with standard on-policy RL algorithms, such as PPO (Schulman et al., 2017), GRPO (Shao et al., 2024), RLOO (Ahmadian et al., 2024), REINFORCE++ (Hu et al., 2025), without explicit step labels or extra rollout cost.

OPRL addresses the limitations of prior work along several dimensions:
(1) Our method provides fine-grained, preference-consistent step credit without step labels by converting trajectory-level preferences into step-level guidance. Theoretical analysis shows these implicit step rewards are Bayes-consistent with Bradley–Terry trajectory preferences and implement potential-based shaping that preserves the optimal policy set (see Theorem3.3);
(2) OPRL stabilizes multi-turn RL training and reduces variance by optimizing at the turn level using implicit step rewards rather than per-token rewards. Specifically, maximizing the shaped objective by the policy performs a KL-descent step toward the PRM, yielding bounded gradients that stabilizes training. (see Proposition3.4);
(3) OPRL only relies on trajectory-level preferences, which can be sourced from either rule-based verifiers (e.g., success signals) or unverifiable ORMs (e.g., LLM judges) for open-ended environments with rarely overlapping states. This enables a unified credit assignment strategy across domains.

Experiments across three challenging agent benchmarks show that OPRL is effective, efficient, and robust to diverse multi-turn settings. In WebShop and VisualSokoban, it consistently outperforms closed-source frontier models and strong RL baselines, achieving state-of-the-art results with Qwen-2.5-7B(-VL) (Yang et al., 2024) as the base model. In SOTOPIA, an open-ended social interaction environment with unverifiable rewards, OPRL increases goal completion by up to 14% in self-chat and 48% when chatting with GPT-4o (OpenAI, 2024). Further analysis shows faster convergence with lower variance than outcome-only or token-level PRM baselines, indicating high sample efficiency and stable training. OPRL also boosts both episode- and step-level rewards while producing shorter episodes, suggesting more useful exploration with fewer unnecessary actions. Finally, ablations indicate that advantage-level fusion is critical, environment step penalties offer only modest gains, and token-level PRMs are too fine-grained for stable multi-turn training. Our contributions are threefold:

•

We propose OPRL, a universal fine-grained credit assignment method that converts trajectory-level preferences into dense step-level guidance for agentic RL.

•

We provide theoretical guarantees that the resulting implicit step rewards are preference-consistent and constitute potential-based reward shaping with bounded gradients to stabilize multi-turn RL training.

•

Empirical results and analysis demonstrate superior performance of OPRL over baselines in sample efficiency, robustness across RL algorithms, and generalization to open-ended environments with unverifiable rewards.

2 Preliminaries

Task formulation.

We consider the LLM agent task as a multi-step decision-making process, where the agent interacts with the environment to achieve a long-term goal through sequential decisions given a task prompt x∈p​(X)x\in p(X).
At each timestep tt, the agent receives an observation oto_{t} (e.g, adversary messages or environmental feedback) and responds with a textual action at∈VLa_{t}\in V^{L}, where VV denotes the token vocabulary and LL is the maximum generation length111Note that we prompt the LLM agent to produce a reasoning process before executing an action, and ata_{t} refers to the whole sequence consisting of both the reasoning and the action at each timestep..
The environment then returns a scalar reward rtr_{t} and provides the next observation ot+1o_{t+1}. Until the last timestep TT, the full episode consists of a trajectory τ={(o1,a1,r1),…,(oT,aT,rT)}\tau=\{(o_{1},a_{1},r_{1}),...,(o_{T},a_{T},r_{T})\}.
However, in real-world scenarios (e.g., dialogues), rewards can be sparse or delayed, such as feedback provided only at the end of a trajectory or weak signals for intermediate steps.
Consequently, it is challenging to assign credit to individual steps within a trajectory, especially when there are many interaction turns.

RL for LLMs.

RL addresses the agent task by optimizing the policy πθ​(at|o1:t,x)\pi_{\theta}(a_{t}|o_{1:t},x) of an LLM, with the objective of maximizing the expected cumulative rewards during interactions.
To estimate the gradient of the expected reward with respect to θ\theta, policy gradient methods are used, such as PPO (Schulman et al., 2017), GRPO (Shao et al., 2024), RLOO (Ahmadian et al., 2024), and REINFORCE++ (Hu et al., 2025).
These RL algorithms mainly differ in the manner of estimating advantages for policy update. For example, PPO computes advantages with a learned value function using generalized advantage estimation (GAE). GRPO and RLOO are critic-free and form relative advantages within a batch of NN samples for the same prompt—GRPO centers (often normalizes) each reward by the group mean-while RLOO uses a leave-one-out mean. REINFORCE++ instead uses batch-normalized rewards as the baseline reward.

Implicit reward modeling.

Implicit rewards has shown effectiveness in reward modeling for LLM alignment by enabling models to infer reward structures without explicit labels. Besides preference learning (Rafailov et al., 2024b; Ethayarajh et al., 2024; Wu et al., 2025; Zhang et al., 2025a). implicit rewards have been also used as outcome rewards to evaluate the quality of model outputs (Hosseini et al., 2024; Zhong et al., 2025). Further, Rafailov et al. (2024a) demonstrates that DPO can automatically learn a Q-function. Beyond the use as ORMs or Q-functions, recent work explores the derivation of PRMs from implicit rewards for test-time reranking (Yuan et al., 2025) or single-turn RL training (Cui et al., 2025). In this setup, a PRM is trained with only outcome labels and parameterize the process reward for each token as rϕ​(yt):=β​log⁡πϕ​(yt|y<t)πref​(yt|y<t)r_{\phi}(y_{t}):=\beta\log\frac{\pi_{\phi}(y_{t}|y_{<t})}{\pi_{\text{ref}}(y_{t}|y_{<t})}, where πϕ\pi_{\phi} represents the PRM and πref\pi_{\text{ref}} the reference model. yty_{t} denotes the tt-th token in the response yy.

3 Method

In this section, we first provide an overview of our method with a definition of implicit step rewards for online RL. We then present theoretical analysis to justify that these step rewards offer faithful and stable guidance for policy learning.

Figure 1: Overview of OPRL. The LLM agent interacts with an environment or a user simulator to generate multi‑step rollouts. An ORM evaluates each trajectory and provides sparse outcome rewards. These outcome‑labeled rollouts are used to update a PRM, which induces implicit process reward for each step in the trajecory. Using both the implicit step rewards and the outcome rewards, the agent’s policy is updated through RL.

3.1 Overview

OPRL introduces an online PRM that is optimized alternately with the policy, transforming the tendency to prefer more optimal actions into a dense reward for each step, guiding fine-grained exploration and improvement of the agent.
Figure 1 shows the overall training pipeline of our method: (1) sample on-policy rollouts using the current policy πθ\pi_{\theta}; (2) construct preference pairs from the same on-policy data according to outcome rewards ro​(τ)r_{o}(\tau), and update the PRM for a training step via a dpo-derived objective defined in Eq. 2; (3) use the updated PRM to compute the implicit step reward defined in Eq. 1, and optimize πθ\pi_{\theta} for a training step according to Eq. 6.
The alternating optimization of πϕ\pi_{\phi} and πθ\pi_{\theta} creates a self-reinforcing loop, where the policy and the PRM iteratively enhance each other.
Below we first provide a definition of the implicit step reward, and detail the training process for each model.
Please refer to Appendix A for the detailed algorithm of OPRL.

Definition 3.1(Implicit step rewards).

Let τ=(o1,a1,…,oT,aT)\tau=(o_{1},a_{1},...,o_{T},a_{T}) denote a trajectory produced by the current policy πθ\pi_{\theta}.
For action ata_{t} in the trajectory at step tt, its implicit step reward is defined as:
rϕ​(o1:t,at)=β​log⁡πϕ​(at|o1:t,x)πθold​(at|o1:t,x),r_{\phi}(o_{1:t},a_{t})=\beta\log\frac{\pi_{\phi}(a_{t}|o_{1:t},x)}{\pi_{\theta_{\text{old}}}(a_{t}|o_{1:t},x)},(1)
where πϕ\pi_{\phi} represents the PRM that is updated online, πθo​l​d\pi_{\theta_{old}} is the previous snapshot of the policy, and β∈[0,1]\beta\in[0,1] refers to a temperature that scales the reward.
The implicit step reward measures how much more probable the current action is under the freshly learned PRM than under the old policy. Positive values indicate actions that πϕ\pi_{\phi} believes to be responsible for recent improvements, while negative values highlight actions that should be discouraged.

Optimizing online PRM via DPO.

For scalable online PRM training, we simply optimize πϕ\pi_{\phi} on positive-negative trajectory pairs sampled by the policy without inducing additional rollouts, and derive a DPO-style objective:
𝒥PRM​(ϕ)=−𝔼(τ+,τ−)∼πθoldx∼p​(X)​[log⁡σ​(β​log⁡πϕ​(τ+|x)πθold​(τ+|x)−β​log⁡πϕ​(τ−|x)πθold​(τ−|x))],\mathcal{J}_{\text{PRM}}(\phi)=-\mathbb{E}_{\begin{subarray}{c}(\tau^{+},\tau^{-})\sim\pi_{\theta_{\text{old}}}\\
x\sim p(X)\end{subarray}}\left[\log\sigma\big(\beta\log\frac{\pi_{\phi}(\tau^{+}|x)}{\pi_{\theta_{\text{old}}}(\tau^{+}|x)}-\beta\log\frac{\pi_{\phi}(\tau^{-}|x)}{\pi_{\theta_{\text{old}}}(\tau^{-}|x)}\big)\right],(2)
where σ\sigma is the logistic sigmoid and β\beta follows Eq. 1; τ+\tau^{+} is a positive trajectory that is preferred to the negative one τ−\tau^{-}, both of which are labeled by outcome rewards222In our experiments on WebShop and VisualSokoban, positive trajectories are those with success rates above 0, while for SOTOPIA, positive trajectories have goal completion score above 6.. See Theorem 3.3 for the proof that rϕr_{\phi} is an unbiased per-step reward estimator.

Policy learning with implicit step rewards.

We use GRPO as an example to illustrate how to incorporate implicit step rewards into policy training, despite that our method is compatible with any policy gradient algorithm.
As shown in Figure 2, for each task prompt xx, we sample NN trajectories {τ1,…,τN}\{\tau_{1},...,\tau_{N}\} from the current policy πθ\pi_{\theta}, and obtain its corresponding outcome rewards {ro​(τ1),…,ro​(τN)}\{r_{o}(\tau_{1}),...,r_{o}(\tau_{N})\} through a rule-based verifier or an ORM.
We then compute the episode-level advantages for each sampled trajectory:
AE​(τi)=(ro​(τi)−m​e​a​n​(Ro))/s​t​d​(Ro),A^{E}(\tau_{i})=\big(r_{o}(\tau_{i})-mean(R_{o})\big)/std(R_{o}),(3)
where Ro=∑i=1Nro​(τi)R_{o}=\sum_{i=1}^{N}r_{o}(\tau_{i}).
Next, we use the latest PRM πϕ\pi_{\phi} (from the previous training step) to obtain the implicit step reward for each action atia_{t}^{i} via Eq. 1, and compute the step-level advantages:
AS​(ati)=(rϕ​(ati)−m​e​a​n​(Rs))/s​t​d​(Rs),A^{S}(a_{t}^{i})=\left(r_{\phi}(a_{t}^{i})-mean(R_{s})\right)/std(R_{s}),(4)
where Rs=∪i,trϕ​(ati)R_{s}=\cup_{i,t}r_{\phi}(a_{t}^{i}) denotes the whole set of step rewards in the NN trajectories to keep scales comparable across episode lengths.
We then combine the two-level advantages for policy update:
A​(ati)=AE​(τi)+α​AS​(ati),A(a_{t}^{i})=A^{E}(\tau_{i})+\alpha{A^{S}(a_{t}^{i})},(5)
where α\alpha is a hyperparameter that balances the global correctness and local quality, and we set it to 1 in all our experiments.
Finally, the policy is optimized using a surrogate objective that is widely used in Schulman et al. (2017); Shao et al. (2024); Ahmadian et al. (2024); Hu et al. (2025) but without KL-divergence penalty:
𝒥policy​(θ)=𝔼{τi}i=1N∼πθoldx∼p​(X)​[1N​T​∑i=1N∑t=1Tmin⁡(ρθ​(ati)​A​(ati),clip​(ρθ​(ati),1±ϵ)​A​(ati))],\mathcal{J}_{\text{policy}}(\theta)=\mathbb{E}_{\begin{subarray}{c}\{\tau_{i}\}_{i=1}^{N}\sim\pi_{\theta_{\text{old}}}\\
x\sim p(X)\end{subarray}}\left[\frac{1}{NT}\sum_{i=1}^{N}\sum_{t=1}^{T}\min\left(\rho_{\theta}(a_{t}^{i})A(a_{t}^{i}),\text{clip}\left(\rho_{\theta}(a_{t}^{i}),1\pm\epsilon\right)A(a_{t}^{i})\right)\right],(6)
where ρθ​(ati)=πθ​(ati|𝐨ti,𝐱)πθold​(ati|𝐨ti,𝐱)\rho_{\theta}(a_{t}^{i})=\frac{\pi_{\theta}(a_{t}^{i}|\mathbf{o}_{t}^{i},\mathbf{x})}{\pi_{\theta_{\text{old}}}(a_{t}^{i}|\mathbf{o}_{t}^{i},\mathbf{x})} is the importance sampling ratio at the step-level, and ϵ\epsilon is a hyperparamter that controls the clipping range of the importance (set to 0.2 in all our experiments).

Figure 2: The credit-assignment strategy of OPRL. In OPRL, the episode-level advantages AE​(τ)A^{E}(\tau) are computed using outcome rewards ro​(τ)r_{o}(\tau), while the step-level advantages AS​(a)A^{S}(a) are calculated from implicit step rewards rϕ​(a)r_{\phi}(a) learned online. The final advantages for policy update is a combination of these two-level advantages. Note that our method is not limited to group-based RL (sampling multiple trajectories per task prompt), despite that we show an example here.

3.2 Theoretical Analysis

We now justify that the learned step reward rϕr_{\phi} defined in Eq. 1 is (1) an unbiased estimator of an action’s contribution to the latent task utility, and (2) a safe, well-conditioned learning signal for the policy πθ\pi_{\theta}.
We start from a Bradley–Terry (BT) preference (Bradley & Terry, 1952) assumption on pairwise trajectories.

Assumption 3.2(Trajectory-level preference model).

There exists a latent utility function R⋆:τ↦ℝR^{\star}:\tau\!\mapsto\!\mathbb{R} such that the outcome reward verifier or model chooses τ+\tau^{+} over τ−\tau^{-} with probability
Pr⁡(τ+≻τ−)=σ​(1β​[R⋆​(τ+)−R⋆​(τ−)]).\Pr(\tau^{+}\succ\tau^{-})\;=\;\sigma\!\Bigl(\tfrac{1}{\beta}\bigl[R^{\star}(\tau^{+})-R^{\star}(\tau^{-})\bigr]\Bigr).

This is the classical BT likelihood for pairwise comparisons. Minimizing the PRM loss in Eq. 2 is therefore exact maximum-likelihood estimation of a score log⁡πϕ​(τ)−log⁡πθo​l​d​(τ)\log\pi_{\phi}(\tau)-\log\pi_{\theta_{old}}(\tau) that matches R⋆​(τ)β\frac{R^{\star}(\tau)}{\beta} up to a constant.

Theorem 3.3(Potential-based reward shaping).

Let the PRM πϕ\pi_{\phi} be a global optimizer of the loss in Eq. 2, and let πr​e​f\pi_{ref} be the static reference model used in a DPO loss. Then rϕ​(τ)=log⁡πϕ​(τ)−log⁡πref​(τ)=1β​R⋆​(τ)+c​(x)r_{\phi}(\tau)\;=\;\log\pi_{\phi}(\tau)\;-\;\log\pi_{\text{ref}}(\tau)=\tfrac{1}{\beta}\,R^{\star}(\tau)+c(x) for some prompt-dependent constant c​(x)c(x).
With the step-reward definition (Eq. 1) we obtain the telescoping identity:
∑t=1Trϕ​(o1:t,at)=R⋆​(τ)+β​c​(x)+β​[log⁡πref​(τ)−log⁡πθold​(τ)].\sum_{t=1}^{T}r_{\phi}(o_{1:t},a_{t})=\;R^{\star}(\tau)+\beta c(x)+\beta\!\Bigl[\log\pi_{\text{ref}}(\tau)-\log\pi_{\theta_{\text{old}}}(\tau)\Bigr].

Choosing θold=θ\theta_{\text{old}}=\theta deletes the last term. Therefore, rϕr_{\phi} is a potential-based shaping of R⋆R^{\star} that preserves the optimal policy set (Ng, 2003).

Proposition 3.4(Gradient alignment and boundedness).

Define the shaped objective
J​(θ)=𝔼τ∼πθ​[∑t=1Trϕ​(o1:t,at)].J(\theta)\;=\;\mathbb{E}_{\tau\sim\pi_{\theta}}\!\Bigl[\sum_{t=1}^{T}r_{\phi}(o_{1:t},a_{t})\Bigr].
Then the policy gradient is:
∇θJ​(θ)=β​𝔼at∼πθ​[∇θlog⁡πθ​(at∣o1:t)​(log⁡πϕ−log⁡πθold)].\nabla_{\theta}J(\theta)=\beta\,\mathbb{E}_{a_{t}\sim\pi_{\theta}}\!\bigl[\nabla_{\theta}\log\pi_{\theta}(a_{t}\!\mid\!o_{1:t})\,\bigl(\log\pi_{\phi}-\log\pi_{\theta_{\text{old}}}\bigr)\bigr].
If θold=θ\theta_{\text{old}}=\theta, this reduces to ∇θJ​(θ)=−β​∇θKL​(πθ∥πϕ)\nabla_{\theta}J(\theta)=-\beta\,\nabla_{\theta}\,\mathrm{KL}\!\bigl(\pi_{\theta}\,\|\,\pi_{\phi}\bigr),
so maximizing JJ performs a KL-descent step that moves
πθ\pi_{\theta} towards the preference-aligned PRM πϕ\pi_{\phi} inside a
trust region.
Let ε=minat,o1:t⁡πθold​(at∣o1:t,x)>0\varepsilon=\min_{a_{t},o_{1:t}}\pi_{\theta_{\text{old}}}(a_{t}\!\mid\!o_{1:t},x)>0.
Then
|rϕ​(o1:t,at)|≤β​log⁡(1/ε).|r_{\phi}(o_{1:t},a_{t})|\leq\beta\log\bigl(1/\varepsilon\bigr).

Hence policy-gradient samples are uniformly bounded, guaranteeing stable stochastic optimization of the
alternating {πϕ,πθ}\{\pi_{\phi},\pi_{\theta}\} updates.

In summary, since πϕ\pi_{\phi} concentrates probability on behaviors that increase R⋆R^{\star}, each rϕr_{\phi} offers an approximately unbiased estimate of an action’s contribution to the latent task utility. The dense, bounded step rewards also reduces variance relative to a single outcome reward, thus yielding an effective credit assignment strategy to accelerate policy learning.

4 Experiments

We evaluate OPRL across a variety of agentic tasks to demonstrate: (1) its effectiveness in training LLM agents for long-horizon reasoning and acting; (2) high sample efficiency and training stability given step rewards learned online; (3) improved exploration justified by consistent reward increases; and (4) the core components of OPRL for credit assignment in agentic RL.
Training details can be found in Appendix C.

Benchmarks.

We evaluate LLM agents in three challenging environments: (1) WebShop (Yao et al., 2022), a text-based web environment where the agent interacts with a HTML-based website to search, nevigate, and purchase an item given an user instruction, requiring multi-step decision making; (2) VisualSokoban (Schrader, 2018) with 6×66\times 6 size, a transportation puzzle game where the agent has to push all boxes on targets, requiring spatial reasoning and long-term planning over both visual and textual inputs; (3) SOTOPIA (Zhou et al., 2024), an open-ended role-playing environment where the agent interacts with another player given a social scenario, role profiles and private goals, requiring strategic reasoning over opponent’s real-time strategies. For training, we use scenarios from SOTOPIA-π\pi(Wang et al., 2024b). See Appendix B for more details of the environments.

Baselines.

We compare our method against a range of competitive baselines: (1) Prompting LLMs specialized in general-purpose reasoning: GPT-5 (OpenAI, 2025b), Gemini-2.5-Pro (Google, 2024), DeepSeek-R1 (Guo et al., 2025), and Claude-Sonnet-4-Thinking (Anthropic, 2025); (2) RL post-training methods: PPO (Schulman et al., 2017), an actor-critic algorithm that requires an additional value model, and critic-free algorithms including GRPO (Shao et al., 2024), RLOO (Ahmadian et al., 2024) and REINFORCE++ (Hu et al., 2025). These RL approaches are used for trajectory-level optimization following Wang et al. (2025); (3) A recent single-turn RL method: PRIME (Cui et al., 2025) that introduces an online PRM to provide token-level process rewards for policy optimization; and (4) A recent agentic RL algorithm: GiGPO (Feng et al., 2025) that calculates step-level advantages via same-state grouping.

Evaluation.

All methods are evaluated using ReAct (Yao et al., 2023) prompting strategies, with CoT generated before each action.
For WebShop and VisualSokoban, we follow Feng et al. (2025) to set the temparature of LLM agents to 0.4, and adopt the Success Rate and Score (only for WebShop) as the evaluation metrics, which are computed over validation instances and select the best score for comparison. For SOTOPIA, we report the goal completion score ranging from 0 to 10, which is evaluated by GPT-4o as a proxy for human judgement following Zhou et al. (2024). We set the tempature to 0 for the LLM judge and 0.7 for LLM agents.

Implementation details.

We use Qwen2.5-(VL)-7B-Instruct (Yang et al., 2024) and Llama3.1-8B-Instruct (Meta, 2024) as the base models for policy optimization. Our online PRM is initialized from the base policy model, except for VisualSokoban, where the policy model uses Qwen2.5-VL-7B-Instruct and the PRM uses Qwen2.5-7B-Instruct. We set the advantage coefficient α\alpha to 1 and β=0.05\beta=0.05 for PRM training. The rollout size is set to 8 per prompt except PPO.
We use RLOO as the default RL algorithm for policy update in WebShop and VisualSokoban, and use GRPO in SOTOPIA unless otherwise specified. See Appendix C for full training details.

4.1 Main Results

Performance on benchmarks.

Table 1 showcases OPRL’ superior performance over baselines in WebShop and VisualSokoban, with notable gains on the latter, where RL algorithms struggle with irreversible mistakes and limited foresight. Similar trends occur with much smaller base models as shown in Table 4.
Specifically, OPRL surpasses recent multi-turn RL method GiGPO by enabling finer-grained credit assignment, distinguishing good and bad actions at each step with process rewards than relying solely on same-state grouping.
Our method also outperforms PRIME by aligning turn-level optimization with step rewards instead of token-level rewards, simplifying policy learning and enhancing training stability.
In SOTOPIA, where GiGPO and PRIME are inapplicable due to open-ended state space and unverifiable rewards, Table 2 shows that OPRL still achieves superior performance.
Particularly, compared to RL post-training baselines, our method improves goal completion rate in hard scenarios by 14% under the self-chat setting, and up to 48% (6.68→7.166.68\rightarrow 7.16) increase when chatting with GPT-4o.
This demonstrates the robustness and generalizability of our method to a wide variety of interactive environments.

Table 1: Performance on WebShop and VisualSokoban. Results are averaged over three random seeds. Qwen2.5-7B-Instruct and Qwen2.5-VL-7B-Instruct serve the base models for WebShop and VisualSokoban, respectively. Note that Deepseek-R1 and PPO training do not currently support multi-modal scenarios, and PRIME is only applicable to tasks with binary outcome rewards.MethodWebShopVisualSokobanSuccessScoreSuccessPrompting frontier LLMs (ReAct)GPT-537.566.116.6Gemini-2.5-Pro30.538.416.0DeepSeek-R129.339.8-Claude-Sonnet-4-Thinking35.262.019.1Base Model (ReAct)21.547.314.1+ PPO78.2±4.578.2\pm 4.586.6±1.186.6\pm 1.1-+ GRPO80.1±1.780.1\pm 1.789.3±2.889.3\pm 2.885.6±2.885.6\pm 2.8+ RLOO77.4±1.177.4\pm 1.187.6±4.787.6\pm 4.786.3±0.686.3\pm 0.6+ REINFORCE++77.0±3.977.0\pm 3.985.8±0.185.8\pm 0.181.4±8.881.4\pm 8.8+ PRIME (Cui et al., 2025)81.5±1.881.5\pm 1.891.3±0.691.3\pm 0.6-+ GiGPO (Feng et al., 2025)84.1±3.984.1\pm 3.991.2±1.591.2\pm 1.585.9±2.685.9\pm 2.6+ OPRL86.5±2.8\textbf{86.5}\pm 2.893.6±1.0\textbf{93.6}\pm 1.091.7±1.2\textbf{91.7}\pm 1.2Table 2: Performance on Sotopia. Self-Chat: the model being evaluated interacts with itself; GPT-4o-as-Patrner: the model interacts with GPT-4o. “Goal” refers to the goal completion score (0-10). “Hard” denotes a challenging subset of scenarios that demand for advanced reasoning, and “All” denotes the all set of social scenarios in SOTOPIA. Results are averaged over three random seeds.MethodSelf-ChatGPT-4o-as-PartnerGoal (Hard)Goal (All)Goal (Hard)Goal (All)Prompting frontier LLMs (ReAct)GPT-57.218.957.708.90Gemini-2.5-Pro6.748.277.438.41DeepSeek-R16.988.567.308.44Claude-Sonnet-4-Thinking6.398.647.028.62Qwen2.5-7B-Instruct (ReAct)5.566.775.517.30+ PPO6.63±0.246.63\pm 0.248.25±0.098.25\pm 0.096.27±0.146.27\pm 0.148.07±0.088.07\pm 0.08+ GRPO6.97±0.246.97\pm 0.248.31±0.068.31\pm 0.066.42±0.316.42\pm 0.317.84±0.067.84\pm 0.06+ RLOO5.70±0.165.70\pm 0.167.13±0.027.13\pm 0.026.09±0.136.09\pm 0.137.77±0.037.77\pm 0.03+ REINFORCE++6.17±0.306.17\pm 0.307.87±0.097.87\pm 0.096.38±0.056.38\pm 0.057.93±0.097.93\pm 0.09+ OPRL7.11±0.19\textbf{7.11}\pm 0.198.42±0.03\textbf{8.42}\pm 0.036.76±0.18\textbf{6.76}\pm 0.188.36±0.03\textbf{8.36}\pm 0.03Llama3.1-8B-Instruct (ReAct)5.896.955.827.43+ PPO7.76±0.147.76\pm 0.149.05±0.039.05\pm 0.036.64±0.036.64\pm 0.038.14±0.018.14\pm 0.01+ GRPO7.92±0.087.92\pm 0.089.12±0.029.12\pm 0.026.68±0.036.68\pm 0.038.14±0.028.14\pm 0.02+ RLOO6.48±0.156.48\pm 0.158.33±0.038.33\pm 0.036.51±0.146.51\pm 0.148.02±0.068.02\pm 0.06+ REINFORCE++7.84±0.147.84\pm 0.149.06±0.049.06\pm 0.046.38±0.236.38\pm 0.237.99±0.107.99\pm 0.10+ OPRL8.06±0.11\textbf{8.06}\pm 0.119.20±0.03\textbf{9.20}\pm 0.037.16±0.14\textbf{7.16}\pm 0.148.45±0.03\textbf{8.45}\pm 0.03

OPRL with different vanilla RL algorithms.

Since OPRL is compatible with any policy update method, we also evaluate it on different RL algorithms for LLM post-training, including RLOO, REINFORCE++ and GRPO, and compare each to its vanilla version that uses only episode rewards.
As shown in Figure 3, OPRL consistently improves vanilla RL algorithms by integrating online step rewards for long-horizon credit assignment.
For example, OPRL with RLOO obtains substantial gains of 6.3% in the success rate on both WebShop and VisualSokoban. Similar trends occur with REINFORCE++ and GRPO, demonstrating the robustness and adaptability to diverse RL algorithms and environments.

Figure 3: Performance comparison of OPRL with different vanilla RL algorithms. Results are reported using one seed. Qwen2.5-7B-Instruct and Qwen2.5-VL-7B-Instruct serve the base models for WebShop and VisualSokoban, respectively.

4.2 In-depth Analysis

Sample efficiency and training stability.

Figure 4 illustrates that compared to PRIME, GiGPO, and vanilla RLOO, OPRL achieves faster improvement and higher final performance in validation metrics during RL training, demonstrating superior sample efficiency and training stability for interactive tasks with long-term dependencies.
As shown in Figure 4(a), OPRL achieves the score of vanilla RLOO in WebShop in just 105 steps, around 2×2\times improvement in training efficiency. By 165 steps, our method reaches the highest score of 94.7%, demonstrating significant gains in both efficiency and performance.
OPRL also achieves higher success rates earlier during RL training across environments.
Notably, while PRIME exhibits comparable early-stage performance in WebShop, its growth stagnates and experiences sharp fluctuations. This is because overly fine-grained process rewards (e.g., token-level in PRIME) will complicate policy learning in multi-turn interactions, which usually involve much longer sequences than single-turn QA tasks.
In contrast, OPRL continues to improve steadily, validating our algorithm design that a well-shaped step reward lowers gradient variance, producing smoother policy updates.

Figure 4: Validation performance during RL training in WebShop and VisualSokoban.Figure 5: Training dynamics of OPRL in WebShop and VisualSokoban. Left: Dynamics of the episode and implicit step rewards during RL training by our method. Right: The episode length versus training step compared to baselines.

Reward signals and exploration efficiency.

To demonstrate the implicit step rewards provides useful feedback for agents, we visualize the dynamics of both episode- and step-reward in Figure 5(a) and (b). It can be seen that the step rewards improve very early (especially in VisualSokoban) and then episode reward follows, indicating that OPRL first captures good local action heuristics and then composes them into higher-return trajectories.
As a result, it enables OPRL to reduce unnecessary actions during interactions, leading to shorter episode lengths. As shown in Figure 5(c) and (d), episode lengths decrease without compromising task success, as evidenced by the consistent increase in episode-rewards.

Table 3: Ablation studies on core components of OPRL.
“RLOO”: only outcome rewards are used to compute advantages for policy update.
“w/ ground-truth PR”: use raw step rewards provided by VisualSokoban to calculate step-level advantages.
“w/ merged rewards”: implicit step rewards are added directly to outcome rewards before advantage computation.
“w/ token-level PR”: implicit step rewards are computed at token level rather than step level.
Results are reported using one seed.MethodWebShopVisualSokobanSuccessScoreSuccessRLOO76.684.285.9w/ ground-truth PR--87.5w/ merged rewards81.390.788.3w/ token-level PR82.090.089.1w/ OPRL89.194.793.0

4.3 Ablation Studies

Table 3 presents results of ablation experiments to validate the necessity of OPRL’ key components for effective credit assignment.
First, raw step penalties provided in VisualSokoban show limited improvement over vanilla RL, suggesting that the step rewards learned by OPRL are superior credit signals for LLM agents.
Second, merging step rewards into episode rewards obtains gains over vanilla RL but the improvement are modest compared to OPRL. This indicates that we should not only reward intermediate actions but also gate credit by final task success to prevent speculative reward exploitation. Therefore, combining signals at the advantage level is crucial to credit assignment.
Third, learning token-level process rewards is sub-optimal to multi-turn RL, suggesting that overly fine-grained rewards may introduce noise and thus increase difficulty of policy learning.

5 Related Work

PRMs has been widely explored in single-turn problems, such as mathematical reasoning and single-shot code generation. In these settings, PRMs are used to score intermediate CoT steps for test-time search or reranking (Lightman et al., 2024; Wang et al., 2024a; Mahan et al., 2024), or for online-RL training (Dou et al., 2024; Setlur et al., 2025; Zha et al., 2025). Moving to interactive tasks, process rewards are usually constructed in three ways: (1) rule-based verifiable signals that assign turn-level rewards to tool execution (Zeng et al., 2025) or meta-reasoning behavior tags (Zhang et al., 2025b); (2) GRMs (Liu et al., 2025; Zou et al., 2025) that label step quality; (3) and implicit PRMs (Yuan et al., 2025) trained from outcome labels and converted into token-level rewards.

However, manually-designed or judge-based step labels are costly and biased, suffering from reward hacking. Learning step Q-values (Choudhury, 2025) reduces the bias but a fixed PRM may poorly estimate Q-values for unseen actions during inference.
PRIME(Cui et al., 2025) partially addresses these issues by jointly training an implicit PRM with the generator. Yet with overly fine-grained rewards in token-level, it introduces noises and distabilizes multi-turn RL training.
Instead of learning a PRM, Feng et al. (2025) addresses credit assignment by computing step-level advantages via same-state grouping. While effective in tasks with finite state-action space, such a method hinges on exact state overlaps with limited generalization in open-ended language environments.
In contrast to these methods, OPRL maintains an online PRM trained from trajectory-level preferences and converts it into dense step-level guidance, offering scalable, label-efficient step rewards with low-variance and showing robustness and generalization to both verifiable and unverifiable rewards in open-ended environments.

6 Conclusion and Limitations

We propose OPRL, a general-purpose credit–assignment strategy for long-horizon LLM agents.
OPRL trains an online PRM, reusing the same on-policy rollouts that are generated to update the agent’s policy.
A DPO-style objective converts trajectory-level preferences into dense, step-level rewards, which are then fused with episode-level advantages for policy update.
Theoretically, the resulting step rewards are preference-consistent, potential-based shaping and bounded, ensuring low-variance gradient updates to stablize multi-turn training.
In practice, OPRL can be plugged into standard RL algorithms and generalized to both verifiable and unverifiable rewards in open-ended settings.
Empirical results show that OPRL achieves averaged 86.5% success and 93.6% score on WebShop, and reaches 91.7% success on VisualSokoban. In SOTOPIA, OPRL improves goal completion in hard scenarios by up to 14% in self-chat and 48% against GPT-4o.

While OPRL significantly advances credit assignment for agentic RL, several limitations remain.
First, despite the use of our PRM for online RL, it can also be applied to test-time scaling for search guidance.
Second, in SOTOPIA, the PRM is trained solely to predict goal-completion preferences, and
future work cluld extend OPRL to multi-objective PRMs.
Finally, the PRM and the policy can share one backbone with two heads—or a unified model trained with different objectives, thus reducing computation cost and potentially improving representation sharing.

Reproducibility Statement 

References

Ahmadian et al. (2024)
Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker.

Back to basics: Revisiting REINFORCE-style optimization for learning from human feedback in LLMs.

In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 12248–12267, Bangkok, Thailand, August 2024. Association for Computational Linguistics.

doi: 10.18653/v1/2024.acl-long.662.

URL https://aclanthology.org/2024.acl-long.662/.

Anthropic (2025)
Anthropic.

Introducing claude 4.

Technical report, Anthropic, 2025.

URL URLhttps://www.anthropic.com/news/claude-4.

Bai et al. (2024)
Hao Bai, Yifei Zhou, Jiayi Pan, Mert Cemri, Alane Suhr, Sergey Levine, and Aviral Kumar.

DigiRL: Training in-the-wild device-control agents with autonomous reinforcement learning.

In The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024.

URL https://openreview.net/forum?id=4XTvXMSZPO.

Bradley & Terry (1952)
Ralph Allan Bradley and Milton E Terry.

Rank analysis of incomplete block designs: I. the method of paired comparisons.

Biometrika, 39(3/4):324–345, 1952.

Chen et al. (2025)
Kevin Chen, Marco Cusumano-Towner, Brody Huval, Aleksei Petrenko, Jackson Hamburger, Vladlen Koltun, and Philipp Krähenbühl.

Reinforcement learning for long-horizon interactive llm agents.

arXiv preprint arXiv:2502.01600, 2025.

Choudhury (2025)
Sanjiban Choudhury.

Process reward models for llm agents: Practical framework and directions.

arXiv preprint arXiv:2502.10325, 2025.

Cui et al. (2025)
Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al.

Process reinforcement through implicit rewards.

arXiv preprint arXiv:2502.01456, 2025.

Dou et al. (2024)
Shihan Dou, Yan Liu, Haoxiang Jia, Enyu Zhou, Limao Xiong, Junjie Shan, Caishuang Huang, Xiao Wang, Xiaoran Fan, Zhiheng Xi, Yuhao Zhou, Tao Ji, Rui Zheng, Qi Zhang, Tao Gui, and Xuanjing Huang.

StepCoder: Improving code generation with reinforcement learning from compiler feedback.

In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 4571–4585, Bangkok, Thailand, August 2024. Association for Computational Linguistics.

doi: 10.18653/v1/2024.acl-long.251.

URL https://aclanthology.org/2024.acl-long.251/.

Ethayarajh et al. (2024)
Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela.

Model alignment as prospect theoretic optimization.

In Forty-first International Conference on Machine Learning, 2024.

Feng et al. (2025)
Lang Feng, Zhenghai Xue, Tingcong Liu, and Bo An.

Group-in-group policy optimization for llm agent training.

arXiv preprint arXiv:2505.10978, 2025.

Furuta et al. (2024)
Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu, and Izzeddin Gur.

Multimodal web navigation with instruction-finetuned foundation models.

In The Twelfth International Conference on Learning Representations, 2024.

URL https://openreview.net/forum?id=efFmBWioSc.

Google (2024)
Google.

Introducing gemini 2.0: our new ai model for the agentic era.

Technical report, Google, 2024.

URL https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/?utm_source=deepmind.google&utm_medium=referral&utm_campaign=gdm&utm_content=#ceo-message.

Guo et al. (2025)
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al.

Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning.

arXiv preprint arXiv:2501.12948, 2025.

Hosseini et al. (2024)
Arian Hosseini, Xingdi Yuan, Nikolay Malkin, Aaron Courville, Alessandro Sordoni, and Rishabh Agarwal.

V-STar: Training verifiers for self-taught reasoners.

In First Conference on Language Modeling, 2024.

URL https://openreview.net/forum?id=stmqBSW2dV.

Hu et al. (2025)
Jian Hu, Jason Klein Liu, Haotian Xu, and Wei Shen.

Reinforce++: An efficient rlhf algorithm with robustness to both prompt and reward models.

arXiv preprint arXiv:2501.03262, 2025.

Jin et al. (2025)
Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan O Arik, Dong Wang, Hamed Zamani, and Jiawei Han.

Search-r1: Training LLMs to reason and leverage search engines with reinforcement learning.

In Second Conference on Language Modeling, 2025.

URL https://openreview.net/forum?id=Rwhi91ideu.

Lightman et al. (2024)
Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe.

Let’s verify step by step.

In The Twelfth International Conference on Learning Representations, 2024.

URL https://openreview.net/forum?id=v8L0pN6EOi.

Liu et al. (2025)
Xiaoqian Liu, Ke Wang, Yongbin Li, Yuchuan Wu, Wentao Ma, Aobo Kong, Fei Huang, Jianbin Jiao, and Junge Zhang.

EPO: Explicit policy optimization for strategic reasoning in LLMs via reinforcement learning.

In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (eds.), Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 15371–15396, Vienna, Austria, July 2025. Association for Computational Linguistics.

ISBN 979-8-89176-251-0.

doi: 10.18653/v1/2025.acl-long.747.

URL https://aclanthology.org/2025.acl-long.747/.

Lu et al. (2025)
Guanxing Lu, Wenkai Guo, Chubin Zhang, Yuheng Zhou, Haonan Jiang, Zifeng Gao, Yansong Tang, and Ziwei Wang.

Vla-rl: Towards masterful and general robotic manipulation with scalable reinforcement learning.

arXiv preprint arXiv:2505.18719, 2025.

Mahan et al. (2024)
Dakota Mahan, Duy Phung, Rafael Rafailov, Chase Blagden, nathan lile, Louis Castricato, Jan-Philipp Franken, Chelsea Finn, and Alon Albalak.

Generative reward models.

ArXiv, abs/2410.12832, 2024.

URL https://api.semanticscholar.org/CorpusID:273404003.

Meta (2024)
Meta.

Introducing llama 3.1: Our most capable models to date.

Technical report, Meta, 2024.

URL https://ai.meta.com/blog/meta-llama-3-1/.

Ng (2003)
Andrew Y Ng.

Shaping and policy search in reinforcement learning.

University of California, Berkeley, 2003.

OpenAI (2024)
OpenAI.

Hello gpt-4o.

Technical report, OpenAI, 2024.

URL URLhttps://openai.com/index/hello-gpt-4o/.

OpenAI (2025a)
OpenAI.

Introducing deep research.

Technical report, OpenAI, 2025a.

URL URLhttps://openai.com/index/introducing-deep-research/.

OpenAI (2025b)
OpenAI.

Introducing gpt-5.

Technical report, OpenAI, 2025b.

URL URLhttps://openai.com/zh-Hans-CN/index/introducing-gpt-5/.

Ouyang et al. (2022)
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al.

Training language models to follow instructions with human feedback.

Advances in neural information processing systems, 35:27730–27744, 2022.

Rafailov et al. (2024a)
Rafael Rafailov, Joey Hejna, Ryan Park, and Chelsea Finn.

From $r$ to $q^*$: Your language model is secretly a q-function.

In First Conference on Language Modeling, 2024a.

URL https://openreview.net/forum?id=kEVcNxtqXk.

Rafailov et al. (2024b)
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn.

Direct preference optimization: Your language model is secretly a reward model.

Advances in Neural Information Processing Systems, 36, 2024b.

Schrader (2018)
Max-Philipp B. Schrader.

gym-sokoban.

https://github.com/mpSchrader/gym-sokoban, 2018.

Schulman et al. (2017)
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.

Proximal policy optimization algorithms.

arXiv preprint arXiv:1707.06347, 2017.

Setlur et al. (2025)
Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar.

Rewarding progress: Scaling automated process verifiers for LLM reasoning.

In The Thirteenth International Conference on Learning Representations, 2025.

URL https://openreview.net/forum?id=A6Y7AqlzLW.

Shao et al. (2024)
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al.

Deepseekmath: Pushing the limits of mathematical reasoning in open language models.

arXiv preprint arXiv:2402.03300, 2024.

Sheng et al. (2024)
Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu.

Hybridflow: A flexible and efficient rlhf framework.

arXiv preprint arXiv: 2409.19256, 2024.

Wang et al. (2024a)
Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui.

Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations.

In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 9426–9439, Bangkok, Thailand, August 2024a. Association for Computational Linguistics.

doi: 10.18653/v1/2024.acl-long.510.

URL https://aclanthology.org/2024.acl-long.510/.

Wang et al. (2024b)
Ruiyi Wang, Haofei Yu, Wenxin Sharon Zhang, Zhengyang Qi, Maarten Sap, Graham Neubig, Yonatan Bisk, and Hao Zhu.

Sotopia-π\pi: Interactive learning of socially intelligent language agents.

In Annual Meeting of the Association for Computational Linguistics, 2024b.

URL https://api.semanticscholar.org/CorpusID:268379635.

Wang et al. (2025)
Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue Zhang, Linjie Li, Zhengyuan Yang, Xing Jin, Kefan Yu, Minh Nhat Nguyen, Licheng Liu, et al.

Ragen: Understanding self-evolution in llm agents via multi-turn reinforcement learning.

arXiv preprint arXiv:2504.20073, 2025.

Wei et al. (2022)
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, brian ichter, Fei Xia, Ed H. Chi, Quoc V Le, and Denny Zhou.

Chain of thought prompting elicits reasoning in large language models.

In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), Advances in Neural Information Processing Systems, 2022.

URL https://openreview.net/forum?id=_VjQlMeSB_J.

Wei et al. (2025a)
Yuxiang Wei, Olivier Duchenne, Jade Copet, Quentin Carbonneaux, Lingming Zhang, Daniel Fried, Gabriel Synnaeve, Rishabh Singh, and Sida I Wang.

Swe-rl: Advancing llm reasoning via reinforcement learning on open software evolution.

arXiv preprint arXiv:2502.18449, 2025a.

Wei et al. (2025b)
Zhepei Wei, Wenlin Yao, Yao Liu, Weizhi Zhang, Qin Lu, Liang Qiu, Changlong Yu, Puyang Xu, Chao Zhang, Bing Yin, Hyokun Yun, and Lihong Li.

Webagent-r1: Training web agents via end-to-end multi-turn reinforcement learning.

ArXiv, abs/2505.16421, 2025b.

URL https://api.semanticscholar.org/CorpusID:278788476.

Wu et al. (2025)
Yue Wu, Zhiqing Sun, Huizhuo Yuan, Kaixuan Ji, Yiming Yang, and Quanquan Gu.

Self-play preference optimization for language model alignment.

In The Thirteenth International Conference on Learning Representations, 2025.

URL https://openreview.net/forum?id=a3PmRgAB5T.

Yang et al. (2025)
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al.

Qwen3 technical report.

arXiv preprint arXiv:2505.09388, 2025.

Yang et al. (2024)
Qwen An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxin Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yi-Chao Zhang, Yunyang Wan, Yuqi Liu, Zeyu Cui, Zhenru Zhang, Zihan Qiu, Shanghaoran Quan, and Zekun Wang.

Qwen2.5 technical report.

ArXiv, abs/2412.15115, 2024.

URL https://api.semanticscholar.org/CorpusID:274859421.

Yao et al. (2022)
Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan.

Webshop: Towards scalable real-world web interaction with grounded language agents.

Advances in Neural Information Processing Systems, 35:20744–20757, 2022.

Yao et al. (2023)
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan Cao.

React: Synergizing reasoning and acting in language models.

In The Eleventh International Conference on Learning Representations, 2023.

URL https://openreview.net/forum?id=WE_vluYUL-X.

Yuan et al. (2025)
Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng.

Free process rewards without process labels.

In Forty-second International Conference on Machine Learning, 2025.

URL https://openreview.net/forum?id=8ThnPFhGm8.

Zeng et al. (2025)
Siliang Zeng, Quan Wei, William Brown, Oana Frunza, Yuriy Nevmyvaka, and Mingyi Hong.

Reinforcing multi-turn reasoning in llm agents via turn-level credit assignment.

arXiv preprint arXiv:2505.11821, 2025.

Zha et al. (2025)
Kaiwen Zha, Zhengqi Gao, Maohao Shen, Zhang-Wei Hong, Duane S Boning, and Dina Katabi.

Rl tango: Reinforcing generator and verifier together for language reasoning.

arXiv preprint arXiv:2505.15034, 2025.

Zhang et al. (2025a)
Yuheng Zhang, Dian Yu, Baolin Peng, Linfeng Song, Ye Tian, Mingyue Huo, Nan Jiang, Haitao Mi, and Dong Yu.

Iterative nash policy optimization: Aligning LLMs with general preferences via no-regret learning.

In The Thirteenth International Conference on Learning Representations, 2025a.

URL https://openreview.net/forum?id=Pujt3ADZgI.

Zhang et al. (2025b)
Zijing Zhang, Ziyang Chen, Mingxiao Li, Zhaopeng Tu, and Xiaolong Li.

Rlvmr: Reinforcement learning with verifiable meta-reasoning rewards for robust long-horizon agents.

arXiv preprint arXiv:2507.22844, 2025b.

Zhong et al. (2025)
Han Zhong, Zikang Shan, Guhao Feng, Wei Xiong, Xinle Cheng, Li Zhao, Di He, Jiang Bian, and Liwei Wang.

DPO meets PPO: Reinforced token optimization for RLHF.

In Forty-second International Conference on Machine Learning, 2025.

URL https://openreview.net/forum?id=IfWKVF6LfY.

Zhou et al. (2024)
Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, and Maarten Sap.

SOTOPIA: Interactive evaluation for social intelligence in language agents.

In The Twelfth International Conference on Learning Representations, 2024.

URL https://openreview.net/forum?id=mM7VurbA4r.

Zou et al. (2025)
Jiaru Zou, Ling Yang, Jingwen Gu, Jiahao Qiu, Ke Shen, Jingrui He, and Mengdi Wang.

Reasonflux-prm: Trajectory-aware prms for long chain-of-thought reasoning in llms.

ArXiv, abs/2506.18896, 2025.

URL https://api.semanticscholar.org/CorpusID:280000261.

Appendix A Algorithm

The algorithm flow of Ours is detailed in Algorithm 1.

Input: Task distribution p​(X)p(X), language model πθinit\pi_{\theta_{\text{init}}}, outcome reward verifier or model ror_{o}, training steps M, rollout size N, mixing weight α\alpha

Output: Optimized policy πθ\pi_{\theta} and PRM πϕ\pi_{\phi}

Initialize policy model πθ←πθinit\pi_{\theta}\leftarrow{\pi_{\theta_{\text{init}}}}, πθo​l​d←πθinit\pi_{\theta_{old}}\leftarrow{\pi_{\theta_{\text{init}}}}, PRM πϕ←πθinit\pi_{\phi}\leftarrow{\pi_{\theta_{\text{init}}}};

foriteration =1,…,M=1,...,Mdo

// Multi-step rollouts collection 

 Sample task x∼p​(X)x\sim p(X) and initialize N identical environments

fort=1,…,Tt=1,...,Tdo

 
Sample actions {ati∼πθ​(o1:ti,x)}i=1N\{a_{t}^{i}\sim\pi_{\theta}(o_{1:t}^{i},x)\}_{i=1}^{N}

 Execute actions and observe next observation {ot+1i}i=1N\{o_{t+1}^{i}\}_{i=1}^{N}

// PRM training 

 Compute outcome rewards for N trajectories: ro​(τ1:N)r_{o}(\tau_{1:N})

 Forward pass πϕ\pi_{\phi} based on trajectory preferences to obtain step reward rϕ​(ati)r_{\phi}(a_{t}^{i}) with Eq. 1

 Update PRM πϕ\pi_{\phi} on trajectories using a DPO-style objective in Eq. 2

// Policy training 

 Compute episode-level advantages AE​(τi)A^{E}(\tau_{i}) using ro​(τi)r_{o}(\tau_{i}) via Eq. 3

 Compute step-level advantages AS​(ati)A^{S}(a_{t}^{i}) using rϕ​(ati)r_{\phi}(a_{t}^{i}) via Eq. 4

 Combine advantages: A​(ati)=AE​(τi)+α​AS​(ati)A(a_{t}^{i})=A^{E}(\tau_{i})+\alpha{A^{S}(a_{t}^{i})}

 Update policy πθ\pi_{\theta} by maximizing objective in Eq. 6

 Update old parameters: θo​l​d←θ\theta_{old}\leftarrow{\theta}

Algorithm 1Training LLM Agents with Ours (GRPO as an example)

Appendix B Environment Details

WebShop.

WebShop (Yao et al., 2022) simulates an online shopping task on an e-commerce platform, where the agent’s objective is to interpret human-provided text instructions and purchase a product that aligns with the given specifications. To accomplish this, the agent must interact with the website’s search engine, select items to review from the search results, examine their descriptions and details, and choose relevant options (e.g., size, color) before finalizing the purchase by clicking the “Buy” button. To identify the best product that fulfills the user’s requirements, the agent may need to compare multiple products, navigate back and forth between pages, and conduct additional searches if necessary. The environment includes over one million products sourced from amazon.com, more than 12,000 crowd-sourced instructions, and a rich set of semantic actions. Rewards are automatically calculated using programmatic matching functions that evaluate attributes, type, options, and price of the selected product.

VisualSokoban.

Sokoban (Schrader, 2018) consists of rooms composed of five key elements: walls, floors, boxes, box targets, and an agent. These elements may exist in different states depending on whether they overlap with a box target. Rooms are randomly generated, which helps prevent models from overfitting to specific predefined layouts. The game includes two primary actions, Push and Move, which can be performed in four directions: Up, Down, Left, and Right. The Move action allows the agent to proceed to an empty space in the specified direction, provided there is no wall or box blocking the path. The Push action attempts to move an adjacent box, but only if the field behind the box is empty; chain pushing of multiple boxes is not allowed. If no box is adjacent, the Push action functions identically to the Move action in the same direction. Successfully completing the game by pushing all boxes onto their targets yields a reward of 10 points on the final step. Additionally, pushing a box onto a target grants a reward of 1 point, while removing a box from a target results in a penalty of -1 point. Each step incurs a small penalty of -0.1 points to discourage trajectories with many steps. VisualSokoban renders visuals in RGB, with the pixel size equal to the grid size.

SOTOPIA.

SOTOPIA (Zhou et al., 2024) is a general-domain, open-ended platform to simulate social interactions between LLM agents. The scenarios span a diverse array of social interaction types, such as negotiation, exchange, collaboration, competition, accommodation, and persuasion. A particularly challenging subset, known as SOTOPIA-hard, involves scenarios requiring advanced strategic reasoning. Each agent is defined by character profiles, encompassing attributes like name, gender, personality, and profession. At the end of each dialogue, agents are evaluated by GPT-4o across seven dimensions: Goal Completion, Believability, Knowledge, Secret, Relationship, Social Rules, Financial and Material Benefits.
SOTOPIA-π\pi(Wang et al., 2024b) is a follow-up work that uses GPT-4 to generate a new set of scenarios. The social tasks in SOTOPIA-π\pi are guaranteed to be entirely distinct from those in SOTOPIA.

Appendix C Training Details

For hyperparameters, we use a constant learning rate 5×10−75\times 10^{-7} for policy models and 10−610^{-6} for PRMs with AdamW optimizer. Both policy and PRMs use a batch size of 64 and micro-batch size 8 for 200 training steps in veRL (Sheng et al., 2024). No KL-divergence penalty is applied. For WebShop and VisualSokoban, we apply a reward penalty of -0.1 to handle invalid actions generated by LLM agents.
In WebShop and VisualSokoban, the maximum response length is 512 tokens, with the maximum prompt length 4096 tokens for WebShop and 1024 tokens for VisualSokoban.
We sample 16 different groups per rollout in WebShop, resulting in a total of 16×8=12816\times 8=128 environments. In VisualSokoban, we sample 32 different groups per rollout, resulting in a total of 32×8=25632\times 8=256 environments.
In SOTOPIA, the maximum prompt length is 6144 tokens and the maximum response length is 2048 tokens.
All methods sh

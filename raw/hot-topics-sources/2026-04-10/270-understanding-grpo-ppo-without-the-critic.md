---
title: Understanding GRPO: PPO without the critic
source_url: https://huggingface.co/blog/garg-aayush/derive-grpo-loss
final_url: https://huggingface.co/blog/garg-aayush/derive-grpo-loss
status: 200
content_type: text/html; charset=utf-8
topics: [GRPO (Group Relative Policy Optimization)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.360194+00:00
---

# Understanding GRPO: PPO without the critic

## 원본 URL

https://huggingface.co/blog/garg-aayush/derive-grpo-loss

## 추출 본문

Understanding GRPO: PPO without the critic 

Hugging Face

 Models 

 Datasets 

 Spaces 

 Buckets new

 Docs 

 Enterprise 

Pricing

Log In

Sign Up

 Back to Articles

 Understanding GRPO: PPO without the critic
	

Community ArticlePublished
 January 1, 2026

 Upvote 
2

aayush garg
garg-aayush

Follow

I: The PPO Objective and the Critic Problem
The Value Function Problem in PPO

II: Replacing the Critic with Group Sampling
Monte Carlo Baseline

Group-Relative Advantage

III: The GRPO Objective
The Full GRPO Objective

Single Gradient Step Simplification

IV: KL Divergence in GRPO

V: Outcome vs. Process Supervision

VI: Connection to REINFORCE Leave-One-Out (RLOO)

Conclusion

References

In my previous posts, I worked through the derivations of PPO and DPO for LLM post-training. PPO gave us a full-fledged RL approach with clipped surrogate objectives, value functions and GAE-based advantage estimation. DPO on the other hand, showed a clever way to bypass RL entirely by reformulating the optimization as a simple classification loss on preference pairs.

That brings us to Group Relative Policy Optimization (GRPO), introduced in the DeepSeekMath paper. If you have been following recent developments in reasoning models throughout 2025, GRPO has become one of the most widely used post-training algorithms behind open-source reasoning models.

In simple terms, GRPO can be thought of as PPO without the critic (value function). Recall that PPO trains a value function in addition to the policy to estimate baselines for advantage computation. GRPO takes a simpler approach where it samples multiple completions (“group”) for each prompt and uses their rewards to form a baseline for advantage computation. This group-derived baseline replaces the learned value function entirely (no need to train a critic!).

The practical implication is lower memory consumption and reduced training complexity relative to PPO while still preserving PPO’s core stability mechanisms, including the clipped surrogate objective and KL regularization.

In this blog, I will discuss and derive the GRPO objective step by step showing exactly how it simplifies PPO.

 I: The PPO Objective and the Critic Problem
	

Let's briefly recap the key relevant elements of PPO. For the full derivation and PPO details, see my previous blog on PPO.

PPO optimizes an LLM by maximizing a clipped surrogate objective (constrained using KL regularization):

LCLIP(θ)=Et[min⁡(rt(θ)A^t,clip(rt(θ),1−ϵ,1+ϵ)⋅A^t)]
L^{\text{CLIP}}(\theta) = \mathbb{E}_t\left[\min\left(r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \cdot \hat{A}_t\right)\right]
LCLIP(θ)=Et​[min(rt​(θ)A^t​,clip(rt​(θ),1−ϵ,1+ϵ)⋅A^t​)]

where rt(θ)=πθ(at∣st)πθold(at∣st)r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}rt​(θ)=πθold​​(at​∣st​)πθ​(at​∣st​)​ is the probability ratio between current and old policies.

The critical component here is the advantage estimate ( A^t\hat{A}_tA^t​ ). The advantage measures how much better (or worse) a specific action is compared to what we expected:

Aπ(st,at)=Qπ(st,at)−Vπ(st)
A^\pi(s_t, a_t) = Q^\pi(s_t, a_t) - V^\pi(s_t)
Aπ(st​,at​)=Qπ(st​,at​)−Vπ(st​)

To compute it, PPO uses a value functionVπ(s)V^\pi(s)Vπ(s) (baseline) also called the critic) that predicts expected future rewards from any state. The critic is trained alongside the policy and PPO uses 
Generalized Advantage Estimation (GAE) to compute advantages from per-token value predictions.

 The Value Function Problem in PPO
	

The value function is implemented as a learned critic model with the same architecture as the policy (i.e. another full LLM copy). This critic is trained alongside the policy using a regression loss:

LVF(θ)=Et[(Vθ(st)−Vttarget)2]
L^{\text{VF}}(\theta) = \mathbb{E}_t\left[\left(V_\theta(s_t) - V_t^{\text{target}}\right)^2\right]
LVF(θ)=Et​[(Vθ​(st​)−Vttarget​)2]

where VttargetV_t^{\text{target}}Vttarget​ is typically the discounted return-to-go from the sampled trajectory.

In PPO, we train two large neural networks (policy and critic) together rather than a single model. This substantially increases computational and memory overhead. Maintaining and training the critic alongside the policy not only increases memory consumption but also adds significant complexity to the training pipeline. In practice, PPO requires four models to be resident in memory at the same time: the policy, the critic, the reference model and the reward model.

One more issue with PPO is that GAE needs per-token rewards to compute Temporal Difference (TD) residuals at each position. But in LLM fine-tuning, we typically get outcome rewards which is a single score for the entire completion assigned only at the final token.

From DeepSeekMath: "During RL training, the value function is treated as a baseline in the calculation of the advantage for variance reduction. While in the LLM context, usually only the last token is assigned a reward score by the reward model, which may complicate the training of a value function that is accurate at each token." 

It raises a fundamental question: how can the critic learn accurate per-token values when all training signal comes from a single final reward?

 II: Replacing the Critic with Group Sampling
	

As mentioned earlier, in PPO the value function V(s)V(s)V(s) acts as a baseline b(s)b(s)b(s) for advantage estimation:
A^t=Q(st,at)−V(st).
\hat{A}_t = Q(s_t, a_t) - V(s_t).
A^t​=Q(st​,at​)−V(st​).
Subtracting this baseline reduces the variance of the policy gradient estimator which in turn stabilizes training.

Key insight: the value function is just one possible choice of baseline. In principle, any function ( b(s)b(s)b(s) ) that depends only on the state and not on the action can be used without introducing bias into the gradient estimates.

Common baseline choices are:

Constant baseline: The average reward across samples. This is the simplest option and is used in vanilla REINFORCE.

Learned value function:V(s)V(s)V(s) trained alongside the policy as in PPO.

Monte Carlo estimate: An empirical average of returns computed from multiple samples starting from the same state.

GRPO adopts the third approach. Instead of learning a value function, it directly estimates the expected return using multiple samples.

 Monte Carlo Baseline
	

For each prompt qqq, GRPO samples multiple completions{o1,o2,…,oG}\{o_1, o_2, \ldots, o_G\}{o1​,o2​,…,oG​} from the policy and obtains their rewards {r1,r2,…,rG}\{r_1, r_2, \ldots, r_G\}{r1​,r2​,…,rG​}. The average reward across these completions provides a Monte Carlo estimate of the expected return:

b(q)=1G∑i=1Gri≈Eo∼πθ(o∣q)[r(q,o)]
b(q) = \frac{1}{G}\sum_{i=1}^G r_i \approx \mathbb{E}_{o \sim \pi_\theta(o|q)}[r(q, o)]
b(q)=G1​i=1∑G​ri​≈Eo∼πθ​(o∣q)​[r(q,o)]

This is a natural and unbiased estimator. With enough samples it converges to the true expected reward for that prompt, similar to what a well-trained value function would predict and can eliminates the need to train a separate critic model.

 Group-Relative Advantage
	

Using the average reward as a baseline, the advantage for completion iii becomes:

A^i=ri−1G∑j=1Grj=ri−mean(r1,…,rG)
\hat{A}_i = r_i - \frac{1}{G}\sum_{j=1}^G r_j = r_i - \text{mean}(r_1, \ldots, r_G)
A^i​=ri​−G1​j=1∑G​rj​=ri​−mean(r1​,…,rG​)

GRPO normalizes the advantage by the standard deviation of rewards in the group:

A^i=ri−mean(r1,…,rG)std(r1,…,rG)(II.I)
\hat{A}_i = \frac{r_i - \text{mean}(r_1, \ldots, r_G)}{\text{std}(r_1, \ldots, r_G)} \tag{II.I}
A^i​=std(r1​,…,rG​)ri​−mean(r1​,…,rG​)​(II.I)

This normalization ensures that advantages are on a comparable scale regardless of the prompt's inherent difficulty.

Think it this way: different prompts can have vastly different reward scales. For example, a simple arithmetic question might yield rewards clustered around 0.9 while a challenging proof might have rewards spread across say 0.1-0.9. Without normalization, the policy gradient updates would be dominated by high-variance prompts which can possibly destabilizing training.

GRPO's group-relative advantage mirrors the comparative nature of rewards models as we are asking "how good is this completion relative to other completions for the same prompt?". 

 III: The GRPO Objective
	

We now have all the pieces needed to construct the full GRPO objective. The construction follows three key modifications:

1. Start with PPO's clipped surrogate. Recall from Section I that PPO optimizes:

LCLIP(θ)=Et[min⁡(rt(θ)A^t,clip(rt(θ),1−ϵ,1+ϵ)⋅A^t)]
L^{\text{CLIP}}(\theta) = \mathbb{E}_t\left[\min\left(r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \cdot \hat{A}_t\right)\right]
LCLIP(θ)=Et​[min(rt​(θ)A^t​,clip(rt​(θ),1−ϵ,1+ϵ)⋅A^t​)]

Here clip(.)clip(.)clip(.) is clip(rt(θ),1−ϵ,1+ϵ)\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)clip(rt​(θ),1−ϵ,1+ϵ) and this clipping mechanism provides a soft trust region that prevents destructively large policy updates. 

2. Replace GAE advantage with group-relative advantage. Instead of computing A^t\hat{A}_tA^t​ using a learned critic and GAE, we substitute the group-relative advantage from Section II:

A^i=ri−mean(r1,…,rG)std(r1,…,rG)
\hat{A}_i = \frac{r_i - \text{mean}(r_1, \ldots, r_G)}{\text{std}(r_1, \ldots, r_G)}
A^i​=std(r1​,…,rG​)ri​−mean(r1​,…,rG​)​

This is the key simplification.

We no longer need per-token value predictions. Instead we estimate the baseline directly from sampled completions.

3. Move KL penalty from reward to loss. In PPO, the KL penalty is typically subtracted from the reward signal ( rtr_trt​ ) before computing advantages:

r~t=rt−β⋅log⁡πθ(at∣st)πref(at∣st)
\tilde{r}_t = r_t - \beta \cdot \log \frac{\pi_\theta(a_t|s_t)}{\pi_{\text{ref}}(a_t|s_t)}
r~t​=rt​−β⋅logπref​(at​∣st​)πθ​(at​∣st​)​

GRPO takes a different approach by adding the KL divergence directly as a penalty term in the loss function. This is a design choice that simplifies advantage computation since we dont need to consider KL penalties in the baseline estimation.

From DeepSeekMath: "Also note that, instead of adding KL penalty in the reward, GRPO regularizes by directly adding the KL divergence between the trained policy and the reference policy to the loss, avoiding complicating the calculation of A^i\hat{A}_iA^i​."

 The Full GRPO Objective
	

Combining these modifications, the GRPO objective (to be maximized) is:

JGRPO(θ)=Eq∼D,{oi}i=1G∼πθold(o∣q)[1G∑i=1G(min⁡(πθ(oi∣q)πθold(oi∣q)A^i,clip(⋅)⋅A^i)−βDKL(πθ∥πref))]
J_{\text{GRPO}}(\theta) = \mathbb{E}_{q \sim \mathcal{D},\, \{o_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(o|q)}\left[\frac{1}{G}\sum_{i=1}^G \left( \min\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)}\hat{A}_i, \; \text{clip}(\cdot) \cdot \hat{A}_i\right) - \beta \, D_{\text{KL}}\left(\pi_\theta \| \pi_{\text{ref}}\right) \right)\right]
JGRPO​(θ)=Eq∼D,{oi​}i=1G​∼πθold​​(o∣q)​[G1​i=1∑G​(min(πθold​​(oi​∣q)πθ​(oi​∣q)​A^i​,clip(⋅)⋅A^i​)−βDKL​(πθ​∥πref​))]

where:

qqq is a prompt sampled from the training distribution D\mathcal{D}D

{o1,o2,…,oG}\{o_1, o_2, \ldots, o_G\}{o1​,o2​,…,oG​} are GGG completions sampled from the old policy πθold\pi_{\theta_{\text{old}}}πθold​​

A^i\hat{A}_iA^i​ is the group-relative advantage for completion iii (from II.I)

β\betaβ is the KL penalty coefficient

πref\pi_{\text{ref}}πref​ is the frozen reference model (typically the SFT checkpoint)

The objective averages over all completions in the group, treating each completion equally in the policy update.

For implementation, we expand the sequence-level objective over individual tokens. Since autoregressive models factor the probability of a completion as a product of token probabilities:

πθ(oi∣q)=∏t=1∣oi∣πθ(oi,t∣q,oi,<t)
\pi_\theta(o_i|q) = \prod_{t=1}^{|o_i|} \pi_\theta(o_{i,t}|q, o_{i,<t})
πθ​(oi​∣q)=t=1∏∣oi​∣​πθ​(oi,t​∣q,oi,<t​)

The per-token formulation of GRPO becomes:

JGRPO(θ)=Eq∼D,{oi}i=1G∼πθold(o∣q)[1G∑i=1G1∣oi∣∑t=1∣oi∣(min⁡(πθ(oi,t∣q,oi,<t)πθold(oi,t∣q,oi,<t)A^i,t,clip(⋅)⋅A^i,t)−βDKL(t))]
J_{\text{GRPO}}(\theta) = \mathbb{E}_{q \sim \mathcal{D},\, \{o_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(o|q)} \left[\frac{1}{G}\sum_{i=1}^G \frac{1}{|o_i|}\sum_{t=1}^{|o_i|} \left( \min\left(\frac{\pi_\theta(o_{i,t}|q, o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}|q, o_{i,<t})}\hat{A}_{i,t}, \; \text{clip}(\cdot) \cdot \hat{A}_{i,t}\right) - \beta \, D_{\text{KL}}^{(t)} \right)\right]
JGRPO​(θ)=Eq∼D,{oi​}i=1G​∼πθold​​(o∣q)​​G1​i=1∑G​∣oi​∣1​t=1∑∣oi​∣​(min(πθold​​(oi,t​∣q,oi,<t​)πθ​(oi,t​∣q,oi,<t​)​A^i,t​,clip(⋅)⋅A^i,t​)−βDKL(t)​)​

where DKL(t)D_{\text{KL}}^{(t)}DKL(t)​ is the per-token KL divergence between the current policy and the reference model.

Note, all tokens in completion iii receive the same advantage:

A^i,t=A^i∀t∈{1,2,…,∣oi∣}
\hat{A}_{i,t} = \hat{A}_i \quad \forall \, t \in \{1, 2, \ldots, |o_i|\}
A^i,t​=A^i​∀t∈{1,2,…,∣oi​∣}

This is a deliberate simplification. Since we only receive a single reward for the entire completion trying to learn which specific tokens were "good" or "bad" can be difficult.

From DeepSeekMath: "While in the LLM context, usually only the last token is assigned a reward score by the reward model, which may complicate the training of a value function that is accurate at each token."

 Single Gradient Step Simplification
	

In practice (as mentioned in RLHF Book), GRPO is often run with only one gradient step per batch of sampled data. In this case πθ=πθold\pi_\theta = \pi_{\theta_{\text{old}}}πθ​=πθold​​ at the start of the update which means the policy ratio equals 1 and the clipping mechanism has no effect:

rt(θ)=πθ(oi,t∣q,oi,<t)πθold(oi,t∣q,oi,<t)=1
r_t(\theta) = \frac{\pi_\theta(o_{i,t}|q, o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}|q, o_{i,<t})} = 1
rt​(θ)=πθold​​(oi,t​∣q,oi,<t​)πθ​(oi,t​∣q,oi,<t​)​=1

The objective then simplifies to a weighted policy gradient:

JGRPO(θ)=Eq∼D,{oi}i=1G∼πθold(o∣q)[1G∑i=1G1∣oi∣∑t=1∣oi∣(A^i⋅log⁡πθ(oi,t∣q,oi,<t)−βDKL(t))]
J_{\text{GRPO}}(\theta) = \mathbb{E}_{q \sim \mathcal{D},\, \{o_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(o|q)} \left[\frac{1}{G}\sum_{i=1}^G \frac{1}{|o_i|}\sum_{t=1}^{|o_i|} \left( \hat{A}_i \cdot \log \pi_\theta(o_{i,t}|q, o_{i,<t}) - \beta \, D_{\text{KL}}^{(t)} \right)\right]
JGRPO​(θ)=Eq∼D,{oi​}i=1G​∼πθold​​(o∣q)​​G1​i=1∑G​∣oi​∣1​t=1∑∣oi​∣​(A^i​⋅logπθ​(oi,t​∣q,oi,<t​)−βDKL(t)​)​

 IV: KL Divergence in GRPO
	

The KL Divergence is a measure of the difference between two probability distributions. It is defined as:

DKL(πθ∥πref)=Ex∼πθ[log⁡πθ(x)πref(x)]
D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}}) = \mathbb{E}_{x \sim \pi_\theta}\left[\log \frac{\pi_\theta(x)}{\pi_{\text{ref}}(x)}\right]
DKL​(πθ​∥πref​)=Ex∼πθ​​[logπref​(x)πθ​(x)​]

It can simply be estimated as:

DKL(πθ∥πref)≈log⁡πθ(x)−log⁡πref(x)
D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}}) \approx \log \pi_\theta(x) - \log \pi_{\text{ref}}(x)
DKL​(πθ​∥πref​)≈logπθ​(x)−logπref​(x)

However this can be negative for individual samples (when πθ<πref\pi_\theta < \pi_{\text{ref}}πθ​<πref​) even though KL divergence is always non-negative. This may lead to high variance in gradient estimates.

GRPO uses an alternative estimator that is both unbiased and guaranteed non-negative:

DKL(t)=πref(oi,t∣q,oi,<t)πθ(oi,t∣q,oi,<t)−log⁡πref(oi,t∣q,oi,<t)πθ(oi,t∣q,oi,<t)−1(IV.I)
D_{\text{KL}}^{(t)} = \frac{\pi_{\text{ref}}(o_{i,t}|q, o_{i,<t})}{\pi_\theta(o_{i,t}|q, o_{i,<t})} - \log \frac{\pi_{\text{ref}}(o_{i,t}|q, o_{i,<t})}{\pi_\theta(o_{i,t}|q, o_{i,<t})} - 1 \tag{IV.I}
DKL(t)​=πθ​(oi,t​∣q,oi,<t​)πref​(oi,t​∣q,oi,<t​)​−logπθ​(oi,t​∣q,oi,<t​)πref​(oi,t​∣q,oi,<t​)​−1(IV.I)

This estimator can be understood as measuring the gap between log⁡(x)\log(x)log(x) and its tangent line at x=1x=1x=1. Since log⁡\loglog is concave. This gap is always non-negative ensuring the KL penalty never incorrectly suggests that diverging from the reference decreases the penalty.

For a detailed derivation of why this estimator is unbiased and non-negative, see John Schulman's excellent blog post on approximating KL divergence.

 V: Outcome vs. Process Supervision
	

The GRPO formulation presented so far assumes outcome supervision which provides a single reward at the end of each completion with the same advantage assigned to every token. However for complex reasoning tasks knowing only the final answer reward might not be sufficient.

From DeepSeekMath Paper: "Outcome supervision only provides a reward at the end of each output, which may not be sufficient and efficient to supervise the policy in complex mathematical tasks."

Process supervision addresses this by providing rewards at the end of each reasoning step. Given a completion oio_ioi​ with KiK_iKi​ reasoning steps, a process reward model (PRM) assigns rewards {riindex(1),…,riindex(Ki)}\{r_i^{\text{index}(1)}, \ldots, r_i^{\text{index}(K_i)}\}{riindex(1)​,…,riindex(Ki​)​} at step boundaries where index(j)\text{index}(j)index(j) is the end token index of the jjj-th step.

GRPO extends to process supervision with two modifications:

1. Normalize across all step rewards in the group:

r~iindex(j)=riindex(j)−mean(R)std(R)
\tilde{r}_i^{\text{index}(j)} = \frac{r_i^{\text{index}(j)} - \text{mean}(\mathcal{R})}{\text{std}(\mathcal{R})}
r~iindex(j)​=std(R)riindex(j)​−mean(R)​

where R\mathcal{R}R contains all step rewards across all GGG completions.

2. Compute advantages as cumulative future rewards:

A^i,t=∑index(j)≥tr~iindex(j)(V.I)
\hat{A}_{i,t} = \sum_{\text{index}(j) \geq t} \tilde{r}_i^{\text{index}(j)} \tag{V.I}
A^i,t​=index(j)≥t∑​r~iindex(j)​(V.I)

This mirrors return-to-go in traditional RL where earlier tokens accumulate rewards from all subsequent steps, while tokens near the end see only remaining rewards.

The DeepSeekMath experiments found process supervision can accelerate learning, though the gap narrows with iterative training. For domains with reliable verifiers (code execution, math answer checking), outcome supervision with RLVR has become dominant. DeepSeek-R1 uses only outcome-level verification.

 VI: Connection to REINFORCE Leave-One-Out (RLOO)
	

GRPO is not the only critic-free algorithm leveraging group sampling. REINFORCE Leave-One-Out (RLOO) takes a similar approach but computes the baseline as the mean reward over all other completions, excluding the current sample:

AiRLOO=ri−1G−1∑j=1,j≠iGrj(VI.I)
A_i^{\text{RLOO}} = r_i - \frac{1}{G-1}\sum_{j=1, j \neq i}^{G} r_j \tag{VI.I}
AiRLOO​=ri​−G−11​j=1,j=i∑G​rj​(VI.I)

This "leave-one-out" baseline avoids a subtle correlation that exists when the baseline includes the sample being evaluated.

The two algorithms are conceptually very similar. However, there are some key differences:

AspectRLOOGRPOBaselineMean of other samplesMean of all samplesNormalizationNoneDivide by stdClippingNoYes (PPO-style)KL PlacementIn rewardIn loss

GRPO can be understood as inheriting PPO's clipping mechanism for stability while adopting RLOO-style group sampling to eliminate the critic.

 Conclusion
	

GRPO ingenuity comes from recognizing that PPO value function is fundamentally just a baseline for advantage computation and that an stimate obtained via group sampling can serve the same role. By sampling multiple completions per prompt and using their mean reward as the baseline, GRPO achieves the stability provided by PPO clipped surrogate objective without the memory overhead or training complexity of training a separate critic model.

This design choice is what makes GRPO a preferred approach for RLVR training of LLMs focused on reasoning capabilities.

 References
	

Papers:

DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models: The original GRPO paper

DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning: DeepSeek's reasoning model trained with GRPO

Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs: The RLOO paper comparing critic-free methods

Blogs:

John Schulman's post on approximating KL divergence: Derivation of the unbiased non-negative KL estimator

RLHF Book by Nathan Lambert: Comprehensive resource on RLHF algorithms including GRPO implementation details

Understanding GRPO by Cameron R. Wolfe: Deep dive into GRPO mechanics and implementation

More from this author

FlashAttention: Making Attention I/O-Aware

March 27, 2026

GRPO: Building Intuition Through Ablation Studies

 2
February 26, 2026

Community

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

 Comment
·Sign up or log in to comment

 Upvote 
2

 System theme

Company
TOSPrivacyAboutCareers
Website
ModelsDatasetsSpacesPricingDocs

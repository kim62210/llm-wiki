---
title: Self-Improving AI Agents through Self-Play
source_url: https://arxiv.org/html/2512.02731v1
final_url: https://arxiv.org/html/2512.02731v1
status: 200
content_type: text/html; charset=utf-8
topics: [Generator-Evaluator Harness Architecture]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:26.342611+00:00
---

# Self-Improving AI Agents through Self-Play

## 원본 URL

https://arxiv.org/html/2512.02731v1

## 추출 본문

Self-Improving AI Agents through Self-Play
1 Introduction
Relation to Reinforcement Learning.

Relation to Geometric Deep Learning.

Beyond LLMs and RL.

2 Preliminaries: The Geometric Setting
2.1 Semantic Foundations

2.2 The External Geometry: Batteries

2.3 The Internal Topology: Parameter Manifold

2.4 The Architecture Map

2.5 The Bridge: Observable Representations

3 The Generator-Verifier-Updater (GVU) Operator
1. The Generator (𝒢\mathcal{G}).

2. The Verifier (𝒱\mathcal{V}).

3. The Updater (𝒰\mathcal{U}).

3.1 Monolithic self-improvement: the diagonal regime G=V=UG=V=U

3.2 Ensemble GVU: LLM councils

3.3 Universality of the GVU decomposition

4 Spectral Stability: The Variance Inequality
4.1 Decomposition of the Update Vector

4.2 The Variance Inequality

4.3 Geometric interpretation on the statistical manifold

4.4 Design levers and special cases
Ensemble verifiers.

Group-based verification and GRPO-style schemes.

Oracle verifiers.

Diagonal GVU with a “cold” verifier.

Goodhart drift and collapse.

4.5 AI slop formally defined
Fisher-geometry collapse.

5 Topological Realizations in Literature
5.1 The Sociality Fiber: Adversarial Self-Play (SPIN, LSP)

5.2 The Planning Fiber: Reasoning and Search

5.3 The Embodied Fiber: Grounding via Execution

5.4 The Recursive Fiber: Verbal Reinforcement

5.5 The Alignment Fiber: Normative Verification

5.6 Synthetic Data Bootstrapping: Diagonal GVU

5.7 Critic-Less Architectures: GRPO

6 Operationalization

7 Conclusion

Self-Improving AI Agents through Self-Play

Przemyslaw Chojecki 

ulam.ai

(December 2, 2025)

Abstract
We extend the moduli-theoretic framework of psychometric batteries [2] to the domain of dynamical systems. While previous work established the AAI capability score as a static functional Φℬ\Phi_{\mathcal{B}} on the space of agent representations 𝒫​(Xℬ)\mathcal{P}(X_{\mathcal{B}}), this paper formalizes the agent as a flow νr\nu_{r} parameterized by computational resource rr, governed by a recursive Generator-Verifier-Updater (GVU) operator. We prove that this operator generates a vector field on the parameter manifold Θ\Theta, and we identify the coefficient of self-improvement κ\kappa as the Lie derivative of the capability functional along this flow.

The central contribution of this work is the derivation of the Variance Inequality, a spectral condition that is sufficient (under mild regularity) for the stability of self-improvement. We show that a sufficient condition for κ>0\kappa>0 is that, up to curvature and step-size effects, the combined noise of generation and verification must be small enough.

We then apply this formalism to unify the recent literature on Language Self-Play (LSP), Self-Correction, and Synthetic Data bootstrapping. We demonstrate that architectures such as STaR [4], SPIN [5], Reflexion [8], GANs and AlphaZero are not merely heuristics but specific topological realizations of the GVU operator that satisfy the Variance Inequality through filtration, adversarial discrimination, or grounding in formal systems.

1 Introduction

The central problem in Artificial General Intelligence (AGI) is not the achievement of a specific benchmark score, but the achievement of ignition: the point at which an agent can autonomously convert computational resources into capability gains without human intervention. In the framework of [2], we defined the capability of an agent 𝒜\mathcal{A} on a battery ℬ\mathcal{B} as a functional value Φℬ​(ρℬ​(𝒜))\Phi_{\mathcal{B}}(\rho_{\mathcal{B}}(\mathcal{A})). However, for current Large Language Models (LLMs), this value is static once pre-training concludes. As noted in [12], the trajectory of self-improvement for standard LLMs is flat (κ≈0\kappa\approx 0) or decaying due to hallucination drift.

By contrast, systems like AlphaGo Zero [3] exhibited κ≫0\kappa\gg 0, reaching superhuman capability solely through self-play. The disparity lies in the nature of the verification signal. Go provides a noiseless, ground-truth verifier (the game rules). Open-ended domains do not.

To bridge this gap, recent literature has proposed various mechanisms for "self-correction" and "self-play" in language models. These include iterative reasoning bootstrapping (STaR [4]), zero-sum language games (SPIN [5], LSP [6]), and verbal reinforcement learning (Reflexion [8]), but also GANs and AlphaZero.

This paper unifies these approaches under a single rigorous mathematical framework. We define the GVU Operator as the canonical engine of self-improvement. We show that the success or failure of any self-improving agent is determined by the spectral properties of this operator acting on the tangent bundle of the moduli space. Specifically, we derive a "Second Law of AGI Dynamics":
Entropy (hallucination) tends to increase unless the combined signal from generation and
verification is strong enough, relative to their noise and to
curvature, to keep the expected capability gain positive. In practice,
many architectures satisfy this by making verification spectrally
“easier” than generation (e.g., via oracles, ensembles, or
external structure).

Central message for practitioners is: The Variance Inequality tells you exactly why your RL training plateaus and what to do about it - strengthen the verifier, not the generator. Check out LABEL:sec:llm for relation of our framework to current LLM training pipelines.

Contributions

This paper makes the following contributions:

•

From static scores to dynamical flows.
We extend the moduli-theoretic framework of psychometric batteries [2] from static capability scores to dynamical trajectories. An agent is modeled as a flow (νr)r≥0(\nu_{r})_{r\geq 0} on a statistical parameter manifold Θ\Theta, and the self-improvement coefficient κ​(r)\kappa(r) is identified with the Lie derivative of the capability functional F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}} along this flow. This yields an operational notion of ignition as sustained κ>0\kappa>0 across capability fibers.

•

The GVU operator and a universality theorem.
We formalize the Generator–Verifier–Updater (GVU) operator 𝒯GVU=𝒰∘𝒱∘𝒢\mathcal{T}_{\mathrm{GVU}}=\mathcal{U}\circ\mathcal{V}\circ\mathcal{G} as the canonical engine of self-improvement, and prove a score-based GVU representation theorem: on a regular statistical manifold, any first-order, sample-based update vector field can be written in REINFORCE form
v​(θ)=𝔼(x,y)∼μ⊗πθ​[Vθ​(x,y)​∇θlog⁡πθ​(y∣x)]v(\theta)=\mathbb{E}_{(x,y)\sim\mu\otimes\pi_{\theta}}\big[V_{\theta}(x,y)\,\nabla_{\theta}\log\pi_{\theta}(y\mid x)\big]
for some scalar potential VθV_{\theta}. Thus any rational, data-driven self-update implicitly instantiates a GVU with an internal Verifier potential. A non-trivial verifier is shown to be necessary for non-zero expected κ\kappa.

•

The Variance Inequality and the Hallucination Barrier.
We derive the Variance Inequality, a sufficient spectral condition for expected capability gain 𝔼​[Δ​F]>0\mathbb{E}[\Delta F]>0. It quantitatively relates alignment ρ\rho between the internal potential and the external score, generation and verification variances (σ𝒢2,σ𝒱2)(\sigma_{\mathcal{G}}^{2},\sigma_{\mathcal{V}}^{2}), curvature LL, and step size η\eta. A corollary identifies the Hallucination Barrier: in diagonal regimes where 𝒱≈𝒢\mathcal{V}\approx\mathcal{G}, verification noise matches generation noise and self-correction typically fails to produce sustained κ>0\kappa>0.

•

Geometric and spectral design levers.
Working on the Fisher-information statistical manifold (Θ,g)(\Theta,g), we interpret the GVU drift as a noisy vector field whose usefulness is governed by the Fisher angle between the mean update and the true gradient of FF. We analyze generic design levers that improve κ\kappa—ensemble verifiers, group-based normalization (GRPO-style schemes), oracle-like executors (code, games, proofs), and “cold” verifier interfaces in diagonal GVU—and quantify how they increase SNR​(𝒱)\mathrm{SNR}(\mathcal{V}) and widen the stable stepsize window. We also introduce a Goodhart-type limit on long-run κ\kappa via decay of the alignment coefficient ρ\rho under proxy optimization.

•

Topological realizations and an empirical κ^\hat{\kappa} protocol.
We show that a wide range of existing self-improvement methods—AlphaZero, GANs, STaR, SPIN/LSP, PRMs, RAG self-training, self-debugging code agents, RLHF, Constitutional AI, Self-Instruct, and GRPO—are concrete topological realizations of the GVU operator on different fibers (Sociality, Planning, Embodiment, Recursive, Alignment, Synthetic, Critic-less) of the moduli space. Finally, we propose a finite-difference evaluation protocol for estimating an empirical self-improvement rate κ^\hat{\kappa} from before/after battery scores under a fixed compute budget.

Relation to Reinforcement Learning.

Classical reinforcement learning (RL) provides a formal model for agents that optimize a reward signal in a Markov decision process. Our framework recovers this setting as a special case but is designed to encompass a much broader class of self-improving systems, including LLM-based agents trained purely with supervised or synthetic data rather than explicit RL. In standard RL, an environment and reward function define a single objective J​(πθ)J(\pi_{\theta}), and updates are derived from estimates of the policy gradient ∇θJ​(πθ)\nabla_{\theta}J(\pi_{\theta}). In our setting, the batteryℬ\mathcal{B} and capability functional Φℬ\Phi_{\mathcal{B}} play the role of a generalized evaluation layer, inducing a scalar capability F​(θ)=(Φℬ∘ρℬ)​(θ)F(\theta)=(\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}})(\theta) that can aggregate performance across heterogeneous tasks and modalities. The Generator–Verifier–Updater (GVU) operator then subsumes actor–critic and self-play schemes as special cases: the generator corresponds to sampling trajectories, the verifier to any internal scoring mechanism (reward model, contrastive critic, oracle, or verbal judge), and the updater to a first-order policy update, possibly implemented via supervised fine-tuning rather than explicit RL. Equipping the parameter manifold Θ\Theta with the Fisher information metric turns it into a statistical manifold, allowing us to express these updates as natural-gradient flows and to derive the Variance Inequality, a spectral condition under which any such GVU loop—RL-based or not—yields positive expected capability gain. In this way, the theory applies uniformly to conventional RL agents, RLHF/RLAIF pipelines, and purely SFT-trained LLM agents that self-improve via self-correction, synthetic data, or tool use, providing a single geometric lens on their learning dynamics.

Relation to Geometric Deep Learning.

Our framework is closely related in spirit to Geometric Deep Learning,
which studies neural architectures constrained by underlying geometric
structure (groups, graphs, manifolds). Rather than imposing geometry
on the input domain, we equip the space of policies and their
learning dynamics with a statistical and moduli geometry: the parameter
manifold (Θ,G)(\Theta,G) with Fisher metric, and the moduli space
𝔐\mathfrak{M} of batteries stratified into capability fibers. The GVU
operator then defines a noisy vector field on (Θ,G)(\Theta,G), and the
Variance Inequality constrains which such fields can yield positive
drift of the capability functional F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}}. In this sense, our results can be viewed as a
form of “geometric deep learning of self-improving agents”: on each
fiber (Sociality, Planning, Embodiment, Alignment), different GVU
topologies (adversarial self-play, filtration, execution oracles,
ensemble judges, GRPO) play the role of geometric inductive biases
that make the self-improvement dynamics spectrally stable.

Beyond LLMs and RL.

Although many of our examples are phrased in terms of language models and RL fine-tuning, the framework is not limited to them. The only ingredients we require are (i) a parametric generator of behaviour—a map ΠΘ\Pi_{\Theta} from internal state θ∈Θ\theta\in\Theta to a stochastic policy πθ\pi_{\theta} over outputs, (ii) some form of scoring or evaluation, internal or external, and (iii) an update rule that uses these scores to change θ\theta. This pattern occurs across a wide range of systems that are not usually described as RL: evolutionary and black-box optimizers (where θ\theta parameterizes a search distribution and the Verifier is a fitness function), deep-guided theorem provers and SAT solvers (where proof checkers play the role of high-SNR verifiers), AutoML and architecture search (where θ\theta controls a proposal policy over models and hyperparameters), and semi-supervised or self-training pipelines in vision and speech. In all of these cases the Generator–Verifier–Updater (GVU) operator provides a canonical decomposition of the self-improvement loop, and the capability functional F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}} allows us to evaluate progress on batteries of heterogeneous tasks rather than a single reward function. The Variance Inequality then applies unchanged: it constrains when noisy, sample-based updates in these non-RL settings can be expected to yield positive drift in capability, even when there is no explicit MDP or reward signal.

2 Preliminaries: The Geometric Setting

We distinguish between the External Geometry (the Battery and Moduli Space defined in [2]) and the Internal Topology (the Agent’s parameters and architecture). The self-improvement process is a mapping from the latter to the former.

2.1 Semantic Foundations

Let Σ\Sigma be a finite alphabet of tokens (e.g., the UTF-8 set or a BPE vocabulary).
Let Σ∗\Sigma^{*} denote the Kleene closure of Σ\Sigma, the set of all finite sequences (strings) over Σ\Sigma.
We equip Σ∗\Sigma^{*} with the discrete topology. The domains Ωt\Omega_{t} of tasks are subsets of Σ∗\Sigma^{*}.

2.2 The External Geometry: Batteries

We utilize the exact definition of the battery from [2].

Definition 2.1(Battery).

A battery is an octuple
ℬ=(T,ℱ,𝖲,Q∗,μ,𝖣,Π,𝖱),\mathcal{B}=(T,\ \mathcal{F},\ \mathsf{S},\ Q^{*},\ \mu,\ \mathsf{D},\ \Pi,\ \mathsf{R}),
where:

•

TT is a finite set of tasks; ℱ={Fk}\mathcal{F}=\{F_{k}\} is a partition of TT into families.

•

𝖲={St:Ωt→[0,1]}t∈T\mathsf{S}=\{S_{t}:\Omega_{t}\to[0,1]\}_{t\in T} are task-specific scoring maps, where Ωt⊆Σ∗\Omega_{t}\subseteq\Sigma^{*} is the domain of valid solution traces for task tt.

•

Q∗:T→[0,1]Q^{*}:T\to[0,1] are task thresholds.

•

μ\mu is a sampling law on T×Π×𝖣T\times\Pi\times\mathsf{D} (tasks, seeds, drifts).

•

𝖣\mathsf{D} (drifts) and Π\Pi (seeds) are measurable spaces.

•

𝖱≅ℝdR\mathsf{R}\cong\mathbb{R}^{d_{R}} are resource coordinates (e.g., time, tokens, cost), recorded nonnegatively.

Definition 2.2(Trace and Observables).

Given an agent 𝒜\mathcal{A} and budgetary constraints from 𝖱\mathsf{R}, an evaluation draws i.i.d. samples (ti,si,δi)∼μ(t_{i},s_{i},\delta_{i})\sim\mu for i=1,…,ni=1,\dots,n and produces traces
ωi=Run​(𝒜;ti,si,δi,𝖱).\omega_{i}\;=\;\mathrm{Run}\!\left(\mathcal{A};\,t_{i},\,s_{i},\,\delta_{i},\,\mathsf{R}\right).
From each trace ωi\omega_{i}, we derive per-task observables:

•

Quality:q​(ti)=Sti​(ωi)∈[0,1]q(t_{i})=S_{t_{i}}(\omega_{i})\in[0,1].

•

Strict Success:z​(ti)=𝕀​{q​(ti)≥Q∗​(ti)}z(t_{i})=\mathbb{I}\{q(t_{i})\geq Q^{*}(t_{i})\}.

•

Uninterrupted Action Count:a​(ti)∈ℕa(t_{i})\in\mathbb{N}.

•

Plan Depth:d​(ti)∈ℕd(t_{i})\in\mathbb{N} (length of the longest executed path of prerequisite actions).

•

Incurred Cost:c​(ti)∈ℝ≥0c(t_{i})\in\mathbb{R}_{\geq 0} (derived from the resource component rr of yy).

Axis-specific raw statistics rx=rx​({ωi}i=1n)r_{x}=r_{x}(\{\omega_{i}\}_{i=1}^{n}) are computed by fixed functionals and normalized by calibration maps ϕx\phi_{x} to yield axis scores x∈[0,1]x\in[0,1].

From the battery, we derive the explicit interaction spaces:

Definition 2.3(Input and Output Spaces).

1.

The Input Space𝒳\mathcal{X} is the disjoint union of task-specific prompt domains Pt⊆Σ∗P_{t}\subseteq\Sigma^{*}. We identify it with the set of labeled prompts:
𝒳:=⨆t∈TPt≅⋃t∈T(Pt×{t})⊆Σ∗×T.\mathcal{X}:=\bigsqcup_{t\in T}P_{t}\;\cong\;\bigcup_{t\in T}(P_{t}\times\{t\})\;\subseteq\;\Sigma^{*}\times T.
An element x∈𝒳x\in\mathcal{X} is a pair x=(s,t)x=(s,t), where s∈Pts\in P_{t} is the input prompt and tt is the task identifier.

2.

The Output Space𝒴\mathcal{Y} is the product of the semantic trace space and the non-negative resource cone:
𝒴:=Σ∗×ℝ≥0dR.\mathcal{Y}:=\Sigma^{*}\times\mathbb{R}_{\geq 0}^{d_{R}}.
An element y∈𝒴y\in\mathcal{Y} is a pair y=(ω,r)y=(\omega,r), where ω∈Σ∗\omega\in\Sigma^{*} is the generated trace (see Definition 2.2) and rr is the vector of resources consumed to produce it.

2.3 The Internal Topology: Parameter Manifold

Dynamics require a coordinate system. We define the agent’s state space to encompass both its static weights (long-term memory) and its dynamic context (working memory).

Definition 2.4(Parameter Manifold Θ\Theta).

Let W≅ℝdW\cong\mathbb{R}^{d} be the space of trainable weights (e.g., Transformer parameters).
Let EE be the embedding dimension and LL the context window size. Let ℋ⊂⋃k=0Lℝk×E\mathcal{H}\subset\bigcup_{k=0}^{L}\mathbb{R}^{k\times E} be the space of context states (e.g., the KV-cache or prompt buffer).
The Parameter Manifold is the product space:
Θ:=W×ℋ.\Theta:=W\times\mathcal{H}.
We equip Θ\Theta with a Riemannian metric gg (typically the Fisher Information Metric), allowing the definition of gradients ∇θ\nabla_{\theta}. A state θ=(w,h)∈Θ\theta=(w,h)\in\Theta completely specifies the agent at an instant rr.

Remark 2.5(Statistical manifold).

When the Riemannian metric gg on Θ\Theta is chosen to be the
Fisher information metric induced by the policy family
{πθ}θ∈Θ\{\pi_{\theta}\}_{\theta\in\Theta}, we will refer to
(Θ,g)(\Theta,g) as a statistical manifold in the sense of
information geometry.

2.4 The Architecture Map

The link between the internal state θ\theta and the external behavior is the architecture.

Definition 2.6(Policy Space).

Let 𝒫​(𝒴)\mathcal{P}(\mathcal{Y}) denote the space of probability measures on the output space. The space of policies, denoted 𝒫​(𝒴)𝒳\mathcal{P}(\mathcal{Y})^{\mathcal{X}}, is the set of Markov kernels K:𝒳×ℬ​(𝒴)→[0,1]K:\mathcal{X}\times\mathcal{B}(\mathcal{Y})\to[0,1].

Definition 2.7(Architecture ΠΘ\Pi_{\Theta}).

An architecture is a smooth map from the parameter manifold to the policy space:
ΠΘ:Θ→𝒫​(𝒴)𝒳,θ↦πθ​(d​y|x).\Pi_{\Theta}:\Theta\to\mathcal{P}(\mathcal{Y})^{\mathcal{X}},\quad\theta\mapsto\pi_{\theta}(dy|x).
This map encapsulates the forward pass of the neural network. Formally, the image πθ\pi_{\theta} constitutes a Markov kernel from 𝒳\mathcal{X} to 𝒴\mathcal{Y}, identifying the agent as a stochastic decision rule conditioned on input.

2.5 The Bridge: Observable Representations

The battery ℬ\mathcal{B} does not observe θ\theta; it observes scores. We lift the definition of the agent representation from [2] to depend explicitly on θ\theta.

Definition 2.8(Representation Map ρℬ\rho_{\mathcal{B}}).

Following Definition 2.2 of [2], let
Xℬ:=[0,1]T×ℝ≥0dRX_{\mathcal{B}}:=[0,1]^{T}\times\mathbb{R}_{\geq 0}^{d_{R}} be the
evaluation space. The representation mapρℬ:Θ→𝒫​(Xℬ)\rho_{\mathcal{B}}:\Theta\to\mathcal{P}(X_{\mathcal{B}})
is the pushforward of the agent’s behavior under the battery’s scoring
logic.

Let μX\mu_{X} be the pushforward of the battery sampling law μ\mu
to the input space 𝒳\mathcal{X} via the map
(t,s,δ)↦x=(s,t)(t,s,\delta)\mapsto x=(s,t).
For each θ∈Θ\theta\in\Theta, define the joint probability law
ℙθ:=μX⊗πθon𝒳×𝒴,\mathbb{P}_{\theta}:=\mu_{X}\otimes\pi_{\theta}\quad\text{on}\quad\mathcal{X}\times\mathcal{Y},
where πθ\pi_{\theta} is the policy induced by the architecture
ΠΘ\Pi_{\Theta}.

Define the evaluation map
𝖤:𝒳×𝒴→Xℬ,𝖤​((s,t),(ω,r)):=((St′​(ω))t′∈T,r).\mathsf{E}:\mathcal{X}\times\mathcal{Y}\to X_{\mathcal{B}},\qquad\mathsf{E}\big((s,t),(\omega,r)\big):=\big((S_{t^{\prime}}(\omega))_{t^{\prime}\in T},\,r\big).
The representation of θ\theta is then the image measure
ρℬ(θ):=𝖤#ℙθ∈𝒫(Xℬ).\rho_{\mathcal{B}}(\theta)\;:=\;\mathsf{E}_{\#}\mathbb{P}_{\theta}\quad\in\mathcal{P}(X_{\mathcal{B}}).

Definition 2.9(Capability Functional Φℬ\Phi_{\mathcal{B}} and Commutative Diagram).

The objective of the self-improvement loop is to maximize the scalar capability score defined in Definition 6.1 of [2]. Let Φℬ:𝒫​(Xℬ)→ℝ\Phi_{\mathcal{B}}:\mathcal{P}(X_{\mathcal{B}})\to\mathbb{R} be an AAI functional (e.g., the tractable instance) satisfying axioms (A1)-(A4): normalization, monotonicity with respect
to strict task success, decomposability across task families, and
stability under subsampling. We do not repeat the full statements
here, but throughout this paper we assume that any
Φℬ\Phi_{\mathcal{B}} satisfies these axioms. We will often write
F​(θ):=(Φℬ∘ρℬ)​(θ)F(\theta)\;:=\;(\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}})(\theta)
for the induced scalar objective on the parameter manifold.

Given a trajectory (θr)r≥0(\theta_{r})_{r\geq 0} on Θ\Theta, we write
νr:=ρℬ​(θr)∈𝒫​(Xℬ)\nu_{r}:=\rho_{\mathcal{B}}(\theta_{r})\in\mathcal{P}(X_{\mathcal{B}})
for the induced flow of representations on the evaluation space.
The corresponding capability curve is
F​(θr)=Φℬ​(νr)F(\theta_{r})=\Phi_{\mathcal{B}}(\nu_{r}).

The dynamics are governed by the following commutative diagram, which connects the internal physics of the agent (top left) to the moduli space geometry (bottom right):

The self-improvement dynamics will be expressed in terms of the
composite map F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}}:
the GVU operator acts on the internal state θ\theta, the battery
ℬ\mathcal{B} compresses the resulting behavior into a representation
ρℬ​(θ)\rho_{\mathcal{B}}(\theta), and F​(θ)F(\theta) is the scalar capability
that we differentiate along the induced flow.

3 The Generator-Verifier-Updater (GVU) Operator

We postulate that any rational mechanism for autonomous κ>0\kappa>0 can be decomposed into a canonical operator 𝒯GVU\mathcal{T}_{\text{GVU}}. This operator describes one step of the recursive loop (e.g., one round of self-play or one reasoning step).

Definition 3.1(External score and internal potential).

Fix a battery
ℬ=(T,ℱ,𝖲,Q∗,μ,𝖣,Π,𝖱)\mathcal{B}=(T,\mathcal{F},\mathsf{S},Q^{*},\mu,\mathsf{D},\Pi,\mathsf{R})
with input and output spaces 𝒳,𝒴\mathcal{X},\mathcal{Y} as in
Definition 2.3. For x=(s,t)∈𝒳x=(s,t)\in\mathcal{X} and
y=(ω,r)∈𝒴y=(\omega,r)\in\mathcal{Y}, the external score map
Sℬ:𝒳×𝒴→[0,1]S_{\mathcal{B}}:\mathcal{X}\times\mathcal{Y}\to[0,1]
is defined by
Sℬ​(x,y)=Sℬ​((s,t),(ω,r)):=St​(ω),S_{\mathcal{B}}(x,y)=S_{\mathcal{B}}\big((s,t),(\omega,r)\big):=S_{t}(\omega),
i.e. it applies the task-specific scoring map StS_{t} of
Definition 2.2 to the semantic trace ω\omega and ignores
resources rr.

An internal potential for ℬ\mathcal{B} is any measurable
function
V:𝒳×𝒴→ℝV:\mathcal{X}\times\mathcal{Y}\to\mathbb{R}
that the agent uses to internally score interactions (x,y)(x,y), typically
as a surrogate for the external score Sℬ​(x,y)S_{\mathcal{B}}(x,y). In later
sections we measure the alignment between VV and SℬS_{\mathcal{B}}
through the coefficient ρ\rho appearing in the update decomposition
(2).

Definition 3.2(The GVU Operator).

Fix a battery ℬ\mathcal{B} as above, together with:

•

a batch size N∈ℕN\in\mathbb{N};

•

an architecture ΠΘ:Θ→𝒫​(𝒴)𝒳\Pi_{\Theta}:\Theta\to\mathcal{P}(\mathcal{Y})^{\mathcal{X}},
sending θ↦πθ\theta\mapsto\pi_{\theta};

•

an internal potential V:𝒳×𝒴→ℝV:\mathcal{X}\times\mathcal{Y}\to\mathbb{R} in
the sense of Definition 3.1;

•

an inverse temperature β≥0\beta\geq 0;

•

a regularizer ℛ:Θ×Θ→ℝ≥0\mathcal{R}:\Theta\times\Theta\to\mathbb{R}_{\geq 0} and coefficient λ≥0\lambda\geq 0.

Let
ℬN:=(𝒳×𝒴)N\mathcal{B}_{N}:=(\mathcal{X}\times\mathcal{Y})^{N}
denote the batch space of NN input–output pairs, and let
ℰN​(𝒳×𝒴):={∑i=1Nwi​δ(xi,yi)|(xi,yi)∈𝒳×𝒴,wi≥0,∑i=1Nwi=1}⊂𝒫​(𝒳×𝒴)\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y}):=\left\{\sum_{i=1}^{N}w_{i}\delta_{(x_{i},y_{i})}\,\middle|\,(x_{i},y_{i})\in\mathcal{X}\times\mathcal{Y},\;w_{i}\geq 0,\;\sum_{i=1}^{N}w_{i}=1\right\}\subset\mathcal{P}(\mathcal{X}\times\mathcal{Y})
denote the space of NN-point empirical measures.

The GVU operator is a one-step update map
𝒯GVU:Θ→Θ,θ↦𝒰​(θ,𝒱​(𝒢​(θ))),\mathcal{T}_{\mathrm{GVU}}:\Theta\to\Theta,\qquad\theta\mapsto\mathcal{U}\big(\theta,\,\mathcal{V}(\mathcal{G}(\theta))\big),
defined via three constituent maps
𝒢:Θ→ℬN,𝒱:ℬN→ℰN​(𝒳×𝒴),𝒰:Θ×ℰN​(𝒳×𝒴)→Θ\mathcal{G}:\Theta\to\mathcal{B}_{N},\qquad\mathcal{V}:\mathcal{B}_{N}\to\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y}),\qquad\mathcal{U}:\Theta\times\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y})\to\Theta
as follows.

1. The Generator (𝒢\mathcal{G}).

For a given parameter θ∈Θ\theta\in\Theta, write
ΠΘ​(θ)=πθ∈𝒫​(𝒴)𝒳\Pi_{\Theta}(\theta)=\pi_{\theta}\in\mathcal{P}(\mathcal{Y})^{\mathcal{X}} for the induced
policy. To construct a batch {(xi,yi)}i=1N\{(x_{i},y_{i})\}_{i=1}^{N}:

1.

sample evaluation triples
(ti,si,δi)∼μ(t_{i},s_{i},\delta_{i})\sim\mu independently from the battery’s
sampling law on T×Π×𝖣T\times\Pi\times\mathsf{D};

2.

form the corresponding labeled prompts
xi∈𝒳x_{i}\in\mathcal{X} as in Definition 2.3;

3.

sample outputs yi∼πθ(⋅∣xi)y_{i}\sim\pi_{\theta}(\cdot\mid x_{i}) in
𝒴\mathcal{Y}.

This defines a (stochastic) map
𝒢:Θ→ℬN,θ↦{(xi,yi)}i=1N.\mathcal{G}:\Theta\to\mathcal{B}_{N},\qquad\theta\mapsto\{(x_{i},y_{i})\}_{i=1}^{N}.
In the infinite-batch limit the empirical law of
𝒢​(θ)\mathcal{G}(\theta) converges to the joint measure
μ⊗πθ\mu\otimes\pi_{\theta} that underlies the representation
ρℬ​(θ)\rho_{\mathcal{B}}(\theta).

2. The Verifier (𝒱\mathcal{V}).

Given a batch
{(xi,yi)}i=1N∈ℬN\{(x_{i},y_{i})\}_{i=1}^{N}\in\mathcal{B}_{N}, the Verifier uses the
internal potential VV and inverse temperature β\beta to produce a
weighted empirical measure μ^V∈ℰN​(𝒳×𝒴)\hat{\mu}_{V}\in\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y}):
𝒱:ℬN→ℰN​(𝒳×𝒴),{(xi,yi)}i=1N↦μ^V:=∑i=1Nwi​δ(xi,yi),\mathcal{V}:\mathcal{B}_{N}\to\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y}),\qquad\{(x_{i},y_{i})\}_{i=1}^{N}\mapsto\hat{\mu}_{V}:=\sum_{i=1}^{N}w_{i}\,\delta_{(x_{i},y_{i})},
with weights
wi=exp⁡(β​V​(xi,yi))∑j=1Nexp⁡(β​V​(xj,yj)).w_{i}=\frac{\exp(\beta V(x_{i},y_{i}))}{\sum_{j=1}^{N}\exp(\beta V(x_{j},y_{j}))}.
By construction, VV is evaluated on the same 𝒳,𝒴\mathcal{X},\mathcal{Y} that arise
from the battery ℬ\mathcal{B}; in particular, its alignment with the
external score map SℬS_{\mathcal{B}} is what determines the coefficient
ρ\rho in the update decomposition (2). Concrete
choices of VV include:

•

discriminative potentials (reward models, opponents)
[5];

•

logical potentials derived from unit tests, compilers,
or theorem provers [9];

•

heuristic potentials produced by verbal critics
[8].

3. The Updater (𝒰\mathcal{U}).

The updater maps a weighted empirical measure back to parameters. Given
the current parameter θ∈Θ\theta\in\Theta and a measure
μ^V∈ℰN​(𝒳×𝒴)\hat{\mu}_{V}\in\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y}), we define
𝒰​(θ,μ^V):=arg⁡minθ′∈Θ⁡𝔼(x,y)∼μ^V​[−log⁡πθ′​(y∣x)+λ​ℛ​(θ′,θ)],\mathcal{U}(\theta,\hat{\mu}_{V}):=\arg\min_{\theta^{\prime}\in\Theta}\mathbb{E}_{(x,y)\sim\hat{\mu}_{V}}\Big[-\log\pi_{\theta^{\prime}}(y\mid x)+\lambda\mathcal{R}(\theta^{\prime},\theta)\Big],
whenever a minimizer exists. Here the expectation with respect to
μ^V\hat{\mu}_{V} reduces to a finite weighted sum because
μ^V∈ℰN​(𝒳×𝒴)\hat{\mu}_{V}\in\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y}). For fixed
θ\theta we can view this as a map
𝒰θ:ℰN​(𝒳×𝒴)→Θ,μ^V↦𝒰​(θ,μ^V),\mathcal{U}_{\theta}:\mathcal{E}_{N}(\mathcal{X}\times\mathcal{Y})\to\Theta,\qquad\hat{\mu}_{V}\mapsto\mathcal{U}(\theta,\hat{\mu}_{V}),
and the one-step GVU update is
θt+1=𝒯GVU​(θt)=𝒰​(θt,𝒱​(𝒢​(θt))).\theta_{t+1}=\mathcal{T}_{\mathrm{GVU}}(\theta_{t})=\mathcal{U}\big(\theta_{t},\,\mathcal{V}(\mathcal{G}(\theta_{t}))\big).
This template encompasses stochastic gradient descent on
log-likelihood (when μ^V\hat{\mu}_{V} is unweighted), PPO-style updates
(when VV encodes advantages), and in-context updates when Θ\Theta
includes a context or memory component.

3.1 Monolithic self-improvement: the diagonal regime G=V=UG=V=U

An instructive extreme case of our GVU abstraction is when the
generator, verifier, and updater are instantiated by the same model.
Let MθM_{\theta} be a single LLM with parameters θ\theta. We define
three role-specific interfaces:

•

𝒢θ\mathcal{G}_{\theta} queries MθM_{\theta} with a "solve this
task" prompt to sample traces τ\tau;

•

𝒱θ\mathcal{V}_{\theta} queries the same MθM_{\theta} with a
"critique and score these traces" prompt to assign scalar
scores or rankings;

•

𝒰θ\mathcal{U}_{\theta} queries MθM_{\theta} with a "given these
scored traces, propose an update" prompt, producing new training
examples, hyperparameters, or code that an outer optimizer
converts into a parameter update.

At the level of our abstraction the update still factors as
θt+1=𝒰θ∘𝒱θ∘𝒢θ​(θt),\theta_{t+1}=\mathcal{U}_{\theta}\circ\mathcal{V}_{\theta}\circ\mathcal{G}_{\theta}(\theta_{t}),
but now we are in a diagonal regime with (this is a slight abuse of notation)
𝒢θ=𝒱θ=𝒰θ=Mθ\mathcal{G}_{\theta}=\mathcal{V}_{\theta}=\mathcal{U}_{\theta}=M_{\theta},
i.e. the same model, with the same weights, plays all three roles via
different prompts or heads. The battery ℬ\mathcal{B} and
representation map ρℬ\rho_{\mathcal{B}} only see the induced flow
(νr)r≥0(\nu_{r})_{r\geq 0} and the associated κ\kappa-curve, but the noise
and bias structure of the estimator is qualitatively different:
verification and update are no longer external signals but reflections
of the model’s own capabilities and failure modes. In particular, the
self-improvement coefficient κ​(r)\kappa(r) distinguishes between regimes
of self-confirmation (where the model merely reinforces its own
preferences) and genuine self-correction.

3.2 Ensemble GVU: LLM councils

Consider now a “council of models” setup. A user query xx is
first broadcast to a fixed set of base models
M(1),…,M(K)M^{(1)},\dots,M^{(K)} (e.g. GPT-5.1, Gemini 3, Claude, Grok),
each of which returns a candidate answer y(k)y^{(k)}. In a second
stage, all models see the anonymized pool
{y(1),…,y(K)}\{y^{(1)},\dots,y^{(K)}\} and produce evaluations or rankings of the
candidate answers. Finally, a distinguished “Chairman LLM” receives
the answers together with the council’s evaluations and produces the
final response.

To view this through our lens we treat the entire council—base
models plus chairman and aggregation scheme—as a single meta-agent
with parameter space
Θcouncil=Θ1×⋯×ΘK×Θchair.\Theta_{\mathrm{council}}=\Theta_{1}\times\cdots\times\Theta_{K}\times\Theta_{\mathrm{chair}}.
The generator 𝒢council\mathcal{G}_{\mathrm{council}} maps a query xx and
current parameters to a trace consisting of all candidate answers
(and optionally the chairman’s answer). The verifier
𝒱council\mathcal{V}_{\mathrm{council}} maps this trace to scores by letting
each model judge the anonymized pool and aggregating their votes into
rankings or pairwise preferences. The updater
𝒰council\mathcal{U}_{\mathrm{council}} then uses these internally generated
judgements to update one or more components of the council: for
example, distilling a student model on the council’s chosen best
answers, or applying preference optimization where “winning”
answers are treated as preferred over “losing” answers.

In the limiting case the same council architecture is used for
generation, verification, and the proposal of updates, yielding a
multi-agent analogue of the diagonal regime G=V=UG=V=U. From the
perspective of our Variance Inequality this ensemble structure has
two important spectral effects:

1.

diversity of base models improves exploration in the
generator, potentially increasing SNR​(𝒢)\mathrm{SNR}(\mathcal{G}); and

2.

aggregating multiple judges reduces the variance of the
verifier’s signal, improving SNR​(𝒱)\mathrm{SNR}(\mathcal{V}).

Both effects tend to increase the local κ\kappa-slope, making
ignition more likely compared to a single-model GVU with the same
underlying architecture.

Remark 3.3(Diagonal vs. ensemble GVU and the AGI criterion).

Our framework separates the roles of generation, verification,
and update from the implementations that realize them. In the
diagonal regime we have
𝒢θ=𝒱θ=𝒰θ=Mθ,\mathcal{G}_{\theta}=\mathcal{V}_{\theta}=\mathcal{U}_{\theta}=M_{\theta},
i.e. a single monolithic model plays all three roles via different
interfaces or prompts. In the ensemble regime, by contrast,
𝒢\mathcal{G}, 𝒱\mathcal{V}, and 𝒰\mathcal{U} are implemented by a
council of models and an aggregation scheme, as in our LLM council
example: multiple base models jointly generate traces, jointly
evaluate them, and jointly shape the update.

From the perspective of the induced κ\kappa-flow the two regimes
differ primarily in their noise and bias structure. Diagonal GVU is
maximally entangled: the same set of parameters determines what
solutions are proposed, how they are judged, and what updates are
considered admissible. This makes the system particularly vulnerable
to self-confirmation: the verifier inherits the generator’s blind
spots, and the updater may systematically reinforce them, potentially
driving the flow toward a suboptimal attractor with
κ​(r)≈0\kappa(r)\approx 0. Ensemble GVU, on the other hand, can improve
both exploration and signal quality: diversity across council members
increases the support of the generator’s trace distribution, and
aggregating multiple judges can reduce the variance of the verifier’s
signal, increasing SNR​(𝒢)\mathrm{SNR}(\mathcal{G}) and
SNR​(𝒱)\mathrm{SNR}(\mathcal{V}) in our Variance Inequality.

However, neither diagonal nor ensemble GVU is by itself sufficient
for “AGI-like” self-improvement in our sense. Both regimes must be
evaluated through a battery ℬ\mathcal{B} and its induced moduli space
of capability fibers. An AGI candidate must exhibit κ^>0\hat{\kappa}>0
not only in a single, well-instrumented fiber (such as competition
mathematics), but across social, planning, embodied, and recursive
fibers as well. In this view, diagonal and ensemble GVU are two
different ways of wiring up the same underlying self-improvement
template; the AGI criterion concerns the global shape of the resulting
κ\kappa-curve over the moduli space, not the particular choice of
wiring.

3.3 Universality of the GVU decomposition

We postulated above that any rational mechanism for autonomous
self-improvement fits the GVU template. In this subsection we show
that, under mild regularity assumptions, any first-order
statistical update rule can indeed be written in a REINFORCE-style
GVU form. Thus, whenever a flow on Θ\Theta achieves κ>0\kappa>0
using only samples from the current policy, there exists an implicit
internal potential playing the role of a Verifier.

Definition 3.4(Score and Fisher information).

Fix a battery ℬ\mathcal{B} and an architecture
Π:Θ→𝒫​(𝒴)𝒳\Pi:\Theta\to\mathcal{P}(\mathcal{Y})^{\mathcal{X}}, θ↦πθ\theta\mapsto\pi_{\theta}.
For θ∈Θ\theta\in\Theta and (x,y)∈𝒳×𝒴(x,y)\in\mathcal{X}\times\mathcal{Y}, define
the score function
sθ​(x,y):=∇θlog⁡πθ​(y∣x)∈Tθ​Θ.s_{\theta}(x,y):=\nabla_{\theta}\log\pi_{\theta}(y\mid x)\in T_{\theta}\Theta.
The Fisher information matrix at θ\theta is
G​(θ):=𝔼(x,y)∼μ⊗πθ​[sθ​(x,y)​sθ​(x,y)⊤].G(\theta):=\mathbb{E}_{(x,y)\sim\mu\otimes\pi_{\theta}}\big[s_{\theta}(x,y)s_{\theta}(x,y)^{\top}\big].
We say the statistical manifold (Θ,G)(\Theta,G) is regular if G​(θ)G(\theta) is
finite and positive definite for all θ\theta in the region of
interest.

Definition 3.5(First-order statistical update).

A vector field v:Θ→T​Θv:\Theta\to T\Theta is called a
first-order statistical update if it depends on θ\theta only
through the joint law μ⊗πθ\mu\otimes\pi_{\theta}, in the sense that there
exists a measurable function
Ψ:Θ×𝒳×𝒴→T​Θ\Psi:\Theta\times\mathcal{X}\times\mathcal{Y}\to T\Theta
with
v​(θ)=𝔼(x,y)∼μ⊗πθ​[Ψ​(θ,x,y)].v(\theta)=\mathbb{E}_{(x,y)\sim\mu\otimes\pi_{\theta}}\big[\Psi(\theta,x,y)\big].
Intuitively, v​(θ)v(\theta) is computed from first-order statistics of
samples (x,y)(x,y) drawn from the current policy on the battery.

The next theorem shows that, in a regular statistical manifold, any
such update can be written as a REINFORCE-style policy-gradient update
for an appropriate (possibly implicit) scalar potential.

Theorem 3.6(Score-based GVU representation).

Assume the regularity conditions of Definition 3.4, so
that G​(θ)G(\theta) is positive definite for all θ\theta in a region of
interest. Let v:Θ→T​Θv:\Theta\to T\Theta be a smooth vector field,
e.g. the velocity v​(θr)=θ˙rv(\theta_{r})=\dot{\theta}_{r} of an autonomous flow
γ:r↦θr\gamma:r\mapsto\theta_{r} on Θ\Theta. Then for each
θ∈Θ\theta\in\Theta there exists a scalar internal potential
Vθ:𝒳×𝒴→ℝV_{\theta}:\mathcal{X}\times\mathcal{Y}\to\mathbb{R}
such that
v​(θ)=𝔼(x,y)∼μ⊗πθ​[Vθ​(x,y)​sθ​(x,y)],v(\theta)=\mathbb{E}_{(x,y)\sim\mu\otimes\pi_{\theta}}\big[V_{\theta}(x,y)\,s_{\theta}(x,y)\big],(1)
where sθs_{\theta} is the score function from
Definition 3.4. In particular, v​(θ)v(\theta) can be
realized as the expected REINFORCE update for the scalar potential
VθV_{\theta}.

Proof.

Fix θ∈Θ\theta\in\Theta, and write s​(x,y):=sθ​(x,y)s(x,y):=s_{\theta}(x,y) and
G:=G​(θ)G:=G(\theta) for brevity. By Definition 3.4,
G=𝔼​[s​(x,y)​s​(x,y)⊤]G=\mathbb{E}[s(x,y)s(x,y)^{\top}]
is symmetric positive definite, hence invertible. Define
a​(θ):=G−1​v​(θ)∈Tθ​Θ,a(\theta):=G^{-1}v(\theta)\in T_{\theta}\Theta,
and the scalar function
Vθ​(x,y):=⟨a​(θ),sθ​(x,y)⟩.V_{\theta}(x,y):=\big\langle a(\theta),\,s_{\theta}(x,y)\big\rangle.
Then
𝔼​[Vθ​(x,y)​sθ​(x,y)]=𝔼​[⟨a​(θ),s​(x,y)⟩​s​(x,y)]=𝔼​[s​(x,y)​s​(x,y)⊤]​a​(θ)=G​a​(θ)=v​(θ),\mathbb{E}\big[V_{\theta}(x,y)s_{\theta}(x,y)\big]=\mathbb{E}\big[\langle a(\theta),s(x,y)\rangle\,s(x,y)\big]=\mathbb{E}\big[s(x,y)s(x,y)^{\top}\big]a(\theta)=Ga(\theta)=v(\theta),
which is exactly (1).
∎

Remark 3.7.

The construction of VθV_{\theta} in the proof is explicit:
Vθ​(x,y)=⟨G​(θ)−1​v​(θ),∇θlog⁡πθ​(y∣x)⟩.V_{\theta}(x,y)=\big\langle G(\theta)^{-1}v(\theta),\nabla_{\theta}\log\pi_{\theta}(y\mid x)\big\rangle.
Thus VθV_{\theta} can be interpreted as the unique scalar potential whose
REINFORCE update reproduces the given first-order vector field
v​(θ)v(\theta) in the Fisher geometry.

Equation (1) has a direct GVU
interpretation. The generator 𝒢\mathcal{G} samples (x,y)(x,y) from
μ⊗πθ\mu\otimes\pi_{\theta}; the verifier assigns a scalar weight
Vθ​(x,y)V_{\theta}(x,y) to each trace; and the updater projects this weighted
signal back onto the parameter manifold via the policy gradient
∇θlog⁡πθ​(y∣x)\nabla_{\theta}\log\pi_{\theta}(y\mid x).

Corollary 3.8(Necessity of a non-trivial verifier).

In the setting of Theorem 3.6, consider
a REINFORCE-style update of the form
θ˙=𝔼(x,y)∼μ⊗πθ​[Vθ​(x,y)​sθ​(x,y)].\dot{\theta}=\mathbb{E}_{(x,y)\sim\mu\otimes\pi_{\theta}}\big[V_{\theta}(x,y)\,s_{\theta}(x,y)\big].
If Vθ​(x,y)V_{\theta}(x,y) is almost surely constant (i.e. independent of
(x,y)(x,y)), then
𝔼​[Vθ​(x,y)​sθ​(x,y)]=0,\mathbb{E}\big[V_{\theta}(x,y)\,s_{\theta}(x,y)\big]=0,
and hence the expected update vanishes: 𝔼​[θ˙]=0\mathbb{E}[\dot{\theta}]=0.
Consequently, the expected self-improvement coefficient
𝔼​[κ​(r)]\mathbb{E}[\kappa(r)] is zero: there is no systematic gain in the battery
score F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}}.

Proof.

If Vθ​(x,y)≡c​(θ)V_{\theta}(x,y)\equiv c(\theta) is constant in (x,y)(x,y), then
𝔼​[Vθ​(x,y)​sθ​(x,y)]=c​(θ)​𝔼​[sθ​(x,y)].\mathbb{E}\big[V_{\theta}(x,y)\,s_{\theta}(x,y)\big]=c(\theta)\,\mathbb{E}[s_{\theta}(x,y)].
It is a standard property of the score function that
𝔼​[sθ​(x,y)]=0\mathbb{E}[s_{\theta}(x,y)]=0 under μ⊗πθ\mu\otimes\pi_{\theta}, so the
expectation vanishes. The statement about 𝔼​[κ​(r)]\mathbb{E}[\kappa(r)] follows
because κ​(r)\kappa(r) is, up to higher-order curvature terms, the
directional derivative of FF along θ˙r\dot{\theta}_{r}, and the
direction itself has zero mean.
∎

Taken together, Theorem 3.6 and
Corollary 3.8 justify the GVU template for
first-order, data-driven self-improvement: any such update can be
viewed as a generator sampling from the current policy, a verifier
computing a scalar potential Vθ​(x,y)V_{\theta}(x,y) on traces, and an updater
implementing the corresponding policy-gradient step. Moreover, a
non-trivial verifier (one for which VθV_{\theta} is not almost surely
constant) is necessary for non-zero expected κ\kappa.

4 Spectral Stability: The Variance Inequality

We now derive our main theoretical condition linking the GVU update to
expected changes in capability. The GVU operator induces a stochastic
update vector g^\hat{g} on Θ\Theta. For the agent to improve, this
vector must on average align with the gradient of the true battery
score F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}}. However, the
agent only has access to its internal potential VV, not directly to
the battery’s scoring logic 𝖲\mathsf{S}.

4.1 Decomposition of the Update Vector

Let F:=Φℬ∘ρℬF:=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}} and
g∗:=∇θF​(θ)g^{*}:=\nabla_{\theta}F(\theta) be the true gradient of the battery
score with respect to parameters. The update g^\hat{g} produced by
GVU is a stochastic estimator of g∗g^{*}. We decompose it as
g^=ρ⋅g∗+ξ𝒢+ξ𝒱+bbias,\hat{g}=\rho\cdot g^{*}+\xi_{\mathcal{G}}+\xi_{\mathcal{V}}+b_{\text{bias}},(2)
where:

•

ρ∈[−1,1]\rho\in[-1,1] is an alignment coefficient
measuring the correlation between the internal potential VV and
the external score induced by 𝖲\mathsf{S};

•

ξ𝒢\xi_{\mathcal{G}} is the Generation Noise (variance
due to exploration over tasks and samples y∼πθy\sim\pi_{\theta});

•

ξ𝒱\xi_{\mathcal{V}} is the Verification Noise
(variance due to errors in VV as an estimator of the true score);

•

bbiasb_{\text{bias}} is a systematic misalignment term.

We assume throughout this section that 𝔼​[ξ𝒢]=𝔼​[ξ𝒱]=0\mathbb{E}[\xi_{\mathcal{G}}]=\mathbb{E}[\xi_{\mathcal{V}}]=0 and that
ξ𝒢,ξ𝒱\xi_{\mathcal{G}},\xi_{\mathcal{V}} are uncorrelated with g∗g^{*}.
We write
σ𝒢2:=𝔼​‖ξ𝒢‖2,σ𝒱2:=𝔼​‖ξ𝒱‖2,\sigma_{\mathcal{G}}^{2}:=\mathbb{E}\|\xi_{\mathcal{G}}\|^{2},\qquad\sigma_{\mathcal{V}}^{2}:=\mathbb{E}\|\xi_{\mathcal{V}}\|^{2},
and define the corresponding signal-to-noise ratios
SNR​(𝒢):=‖g∗‖2σ𝒢2,SNR​(𝒱):=‖g∗‖2σ𝒱2.\mathrm{SNR}(\mathcal{G}):=\frac{\|g^{*}\|^{2}}{\sigma_{\mathcal{G}}^{2}},\qquad\mathrm{SNR}(\mathcal{V}):=\frac{\|g^{*}\|^{2}}{\sigma_{\mathcal{V}}^{2}}.

4.2 The Variance Inequality

We study a single small step of size η>0\eta>0:
θt+1=θt+η​g^\theta_{t+1}=\theta_{t}+\eta\hat{g}. For brevity we write
θ:=θt\theta:=\theta_{t}.

Theorem 4.1(Variance Inequality, sufficient condition).

Assume F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}} is twice
differentiable and LL-smooth in a neighborhood of θ\theta, i.e.,
its Hessian satisfies ‖H​(θ′)‖≤L\|H(\theta^{\prime})\|\leq L for all θ′\theta^{\prime} along
the trajectory. Assume the decomposition (2)
holds with bbiasb_{\text{bias}} negligible compared to g∗g^{*} and
ξ𝒢,ξ𝒱\xi_{\mathcal{G}},\xi_{\mathcal{V}} zero-mean and uncorrelated with
g∗g^{*} and uncorrelated with each other. Then for step size η>0\eta>0 small enough that the second-order
expansion is accurate, a sufficient condition for expected improvement
𝔼​[Δ​F]:=𝔼​[F​(θt+1)−F​(θt)]>0\mathbb{E}[\Delta F]:=\mathbb{E}[F(\theta_{t+1})-F(\theta_{t})]>0 is
ρ​‖g∗‖2>η​L2​(ρ2​‖g∗‖2+σ𝒢2+σ𝒱2).\rho\|g^{*}\|^{2}\;>\;\frac{\eta L}{2}\big(\rho^{2}\|g^{*}\|^{2}+\sigma_{\mathcal{G}}^{2}+\sigma_{\mathcal{V}}^{2}\big).(3)
Equivalently, dividing by ‖g∗‖2\|g^{*}\|^{2}
ρ>η​L2​(ρ2+1SNR​(𝒢)+1SNR​(𝒱)).\rho\;>\;\frac{\eta L}{2}\left(\rho^{2}+\frac{1}{\mathrm{SNR}(\mathcal{G})}+\frac{1}{\mathrm{SNR}(\mathcal{V})}\right).(4)
In particular, for fixed alignment ρ\rho and curvature/stepsize pair (L,η)(L,\eta), this
is a joint constraint on the generator and verifier noise: both
SNR​(𝒢)\mathrm{SNR}(\mathcal{G}) and SNR​(𝒱)\mathrm{SNR}(\mathcal{V}) must be
sufficiently large (i.e. the corresponding variances sufficiently
small) for 𝔼​[Δ​F]>0\mathbb{E}[\Delta F]>0 to hold. In particular, given
SNR​(𝒢)\mathrm{SNR}(\mathcal{G}) there is a minimum required
SNR​(𝒱)\mathrm{SNR}(\mathcal{V}), and conversely; extremely noisy
generation or verification cannot be compensated by the other.

Proof.

By a second-order Taylor expansion of FF about θ\theta we have
F​(θt+1)≈F​(θ)+η​⟨∇F​(θ),g^⟩+η22​g^⊤​H​(θ′)​g^,F(\theta_{t+1})\approx F(\theta)+\eta\langle\nabla F(\theta),\hat{g}\rangle+\frac{\eta^{2}}{2}\hat{g}^{\top}H(\theta^{\prime})\hat{g},
for some θ′\theta^{\prime} on the line segment between θ\theta and
θt+1\theta_{t+1}. LL-smoothness implies
g^⊤​H​(θ′)​g^≤L​‖g^‖2\hat{g}^{\top}H(\theta^{\prime})\hat{g}\leq L\|\hat{g}\|^{2}, so
𝔼​[Δ​F]≈η​𝔼​[⟨g∗,g^⟩]−η2​L2​𝔼​‖g^‖2.\mathbb{E}[\Delta F]\;\approx\;\eta\,\mathbb{E}\big[\langle g^{*},\hat{g}\rangle\big]\;-\;\frac{\eta^{2}L}{2}\,\mathbb{E}\|\hat{g}\|^{2}.
Using the decomposition (2) and the fact that
𝔼​[ξ𝒢]=𝔼​[ξ𝒱]=0\mathbb{E}[\xi_{\mathcal{G}}]=\mathbb{E}[\xi_{\mathcal{V}}]=0 and that these
terms are uncorrelated with g∗g^{*}, we get
𝔼​[⟨g∗,g^⟩]=ρ​‖g∗‖2+⟨g∗,bbias⟩≈ρ​‖g∗‖2,\mathbb{E}\big[\langle g^{*},\hat{g}\rangle\big]=\rho\|g^{*}\|^{2}+\langle g^{*},b_{\text{bias}}\rangle\approx\rho\|g^{*}\|^{2},
where we have neglected the bias term. Similarly,
𝔼​‖g^‖2=𝔼​‖ρ​g∗+ξ𝒢+ξ𝒱‖2≈ρ2​‖g∗‖2+σ𝒢2+σ𝒱2,\mathbb{E}\|\hat{g}\|^{2}=\mathbb{E}\|\rho g^{*}+\xi_{\mathcal{G}}+\xi_{\mathcal{V}}\|^{2}\approx\rho^{2}\|g^{*}\|^{2}+\sigma_{\mathcal{G}}^{2}+\sigma_{\mathcal{V}}^{2},
neglecting cross-terms under the decorrelation assumptions. Substituting,
𝔼​[Δ​F]≈η​ρ​‖g∗‖2−η2​L2​(ρ2​‖g∗‖2+σ𝒢2+σ𝒱2).\mathbb{E}[\Delta F]\;\approx\;\eta\rho\|g^{*}\|^{2}\;-\;\frac{\eta^{2}L}{2}\big(\rho^{2}\|g^{*}\|^{2}+\sigma_{\mathcal{G}}^{2}+\sigma_{\mathcal{V}}^{2}\big).
Requiring 𝔼​[Δ​F]>0\mathbb{E}[\Delta F]>0 yields inequality
(3).
∎

Corollary 4.2(The Hallucination Barrier).

If 𝒱≈𝒢\mathcal{V}\approx\mathcal{G} (for example, the model simply
asks itself “Is this correct?” without any external grounding), then
typically ρ≈1\rho\approx 1 and σ𝒱≈σ𝒢\sigma_{\mathcal{V}}\approx\sigma_{\mathcal{G}}. Writing
SNRdiag:=SNR​(𝒢)≈SNR​(𝒱),\mathrm{SNR}_{\mathrm{diag}}:=\mathrm{SNR}(\mathcal{G})\approx\mathrm{SNR}(\mathcal{V}),
the sufficient condition (4) reduces, up to constants,
to a requirement that the shared SNR be large:
2SNRdiag≪2​ρη​L−ρ2.\frac{2}{\mathrm{SNR}_{\mathrm{diag}}}\;\ll\;\frac{2\rho}{\eta L}-\rho^{2}.
For realistic curvature LL and stepsizes η\eta, this inequality is
rarely satisfied when SNRdiag\mathrm{SNR}_{\mathrm{diag}} is modest. In this
regime 𝔼​[Δ​F]\mathbb{E}[\Delta F] is close to zero or negative, and the flow tends
toward mode collapse or a noisy random walk. This helps explain the
empirical failure of naive self-correction to produce sustained
κ>0\kappa>0: in diagonal GVU, generation and verification inherit the
same noise, and without an additional low-variance signal the quadratic
curvature penalty dominates the linear alignment term.

In practice, the generator is often intrinsically high-entropy, so it is
typically easier to increase SNR​(𝒱)\mathrm{SNR}(\mathcal{V}) (via external
structure, ensembles, or oracles) than to dramatically improve
SNR​(𝒢)\mathrm{SNR}(\mathcal{G}). Many of the architectures we study exploit
this by engineering verification to be spectrally “easier” than
generation, even though the sufficient condition (4)
itself is symmetric in the two SNRs.

Corollary 4.3(Verifier SNR dominance).

Assume the setting of Theorem 4.1 and fix an alignment floor ρ≥ρ0>0\rho\geq\rho_{0}>0.
Let SNR​(𝒢)>0\mathrm{SNR}(\mathcal{G})>0 be the generator signal-to-noise ratio, and choose a stepsize
0<η<ηmax​(ρ0,SNR​(𝒢))0<\eta<\eta_{\max}(\rho_{0},\mathrm{SNR}(\mathcal{G})), where
ηmax(ρ0,SNR(𝒢)):=2​ρ0L​(ρ02+1/SNR​(𝒢)).\eta_{\max}(\rho_{0},\mathrm{SNR}(\mathcal{G})):=\frac{2\rho_{0}}{L\big(\rho_{0}^{2}+1/\mathrm{SNR}(\mathcal{G})\big)}.
Then there exists a finite threshold
SNR𝒱⋆=SNR𝒱⋆​(ρ0,SNR​(𝒢),L,η)<∞\mathrm{SNR}_{\mathcal{V}}^{\star}=\mathrm{SNR}_{\mathcal{V}}^{\star}\big(\rho_{0},\mathrm{SNR}(\mathcal{G}),L,\eta\big)\;<\;\infty
such that
SNR​(𝒱)>SNR𝒱⋆⟹𝔼​[Δ​F]>0.\mathrm{SNR}(\mathcal{V})>\mathrm{SNR}_{\mathcal{V}}^{\star}\qquad\Longrightarrow\qquad\mathbb{E}[\Delta F]>0.
In particular, for any fixed generator noise level σ𝒢2<∞\sigma_{\mathcal{G}}^{2}<\infty and any sufficiently small
stepsize η\eta, one can always make the expected capability gain positive by increasing the verifier SNR.

Proof.

Starting from the sufficient condition in Theorem 4.1,
ρ​‖g∗‖2>η​L2​(ρ2​‖g∗‖2+σ𝒢2+σ𝒱2),\rho\|g^{*}\|^{2}>\frac{\eta L}{2}\bigl(\rho^{2}\|g^{*}\|^{2}+\sigma_{\mathcal{G}}^{2}+\sigma_{\mathcal{V}}^{2}\bigr),
and dividing by ‖g∗‖2\|g^{*}\|^{2} gives
ρ>η​L2​(ρ2+1SNR​(𝒢)+1SNR​(𝒱)).\rho>\frac{\eta L}{2}\left(\rho^{2}+\frac{1}{\mathrm{SNR}(\mathcal{G})}+\frac{1}{\mathrm{SNR}(\mathcal{V})}\right).
It suffices to enforce this with ρ\rho replaced by ρ0\rho_{0}. Rearranging, we obtain
1SNR​(𝒱)<2​ρ0η​L−ρ02−1SNR​(𝒢).\frac{1}{\mathrm{SNR}(\mathcal{V})}<\frac{2\rho_{0}}{\eta L}-\rho_{0}^{2}-\frac{1}{\mathrm{SNR}(\mathcal{G})}.
The right-hand side is positive precisely when
η<2​ρ0L​(ρ02+1/SNR​(𝒢)),\eta<\frac{2\rho_{0}}{L\big(\rho_{0}^{2}+1/\mathrm{SNR}(\mathcal{G})\big)},
which is our stepsize assumption. In that regime we can define
SNR𝒱⋆:=12​ρ0η​L−ρ02−1SNR​(𝒢)<∞,\mathrm{SNR}_{\mathcal{V}}^{\star}:=\frac{1}{\displaystyle\frac{2\rho_{0}}{\eta L}-\rho_{0}^{2}-\frac{1}{\mathrm{SNR}(\mathcal{G})}}\;<\;\infty,
and any SNR​(𝒱)>SNR𝒱⋆\mathrm{SNR}(\mathcal{V})>\mathrm{SNR}_{\mathcal{V}}^{\star}
satisfies the inequality. This implies 𝔼​[Δ​F]>0\mathbb{E}[\Delta F]>0 by
Theorem 4.1.
∎

4.3 Geometric interpretation on the statistical manifold

Throughout this section we measure norms and inner products on
Θ\Theta with respect to the Riemannian metric gg introduced in
Definition 2.4. When gg is chosen to be the Fisher
information metric induced by the policy family
{πθ}θ∈Θ\{\pi_{\theta}\}_{\theta\in\Theta}, (Θ,g)(\Theta,g) is a
statistical manifold in the sense of Remark 2.5.
In that case the gradient ∇θF\nabla_{\theta}F is the natural
gradient of FF.

Definition 4.4(Fisher inner product and angle).

For θ∈Θ\theta\in\Theta let gθ​(⋅,⋅)g_{\theta}(\cdot,\cdot) denote the
inner product induced by the metric gg on the tangent space
Tθ​ΘT_{\theta}\Theta. For tangent vectors u,v∈Tθ​Θu,v\in T_{\theta}\Theta
we write
⟨u,v⟩θ:=gθ​(u,v),‖u‖θ2:=gθ​(u,u).\langle u,v\rangle_{\theta}:=g_{\theta}(u,v),\qquad\|u\|_{\theta}^{2}:=g_{\theta}(u,u).
Given nonzero u,v∈Tθ​Θu,v\in T_{\theta}\Theta we define the
Fisher angle∠F​(u,v)∈[0,π]\angle_{F}(u,v)\in[0,\pi] between them by
cos⁡(∠F​(u,v)):=⟨u,v⟩θ‖u‖θ​‖v‖θ.\cos\big(\angle_{F}(u,v)\big):=\frac{\langle u,v\rangle_{\theta}}{\|u\|_{\theta}\,\|v\|_{\theta}}.

In these terms, the true ascent direction at θ\theta is the gradient
vector g∗=∇θF​(θ)g^{*}=\nabla_{\theta}F(\theta), and the GVU update produces a
random tangent vector g^\hat{g} with mean
v​(θ):=𝔼​[g^]v(\theta):=\mathbb{E}[\hat{g}]. Theorem 4.1 can be read
as a statement about the competition, in the Fisher geometry, between:
(i) the alignment between v​(θ)v(\theta) and g∗g^{*}, and
(ii) the spread of the noise around v​(θ)v(\theta).

Proposition 4.5(Fisher angle and alignment coefficient).

Under the assumptions of Theorem 4.1, write
g∗:=∇θF​(θ)g^{*}:=\nabla_{\theta}F(\theta) and
v:=𝔼​[g^]v:=\mathbb{E}[\hat{g}]. Let θF\theta_{F} be the Fisher angle between g∗g^{*}
and vv,
cos⁡θF:=⟨g∗,v⟩θ‖g∗‖θ​‖v‖θ.\cos\theta_{F}:=\frac{\langle g^{*},v\rangle_{\theta}}{\|g^{*}\|_{\theta}\,\|v\|_{\theta}}.
If the bias term bbiasb_{\mathrm{bias}} in
(2) is negligible and the noise terms are
uncorrelated with g∗g^{*}, the alignment coefficient
ρ\rho in (2) can be expressed as
ρ=⟨g∗,v⟩θ‖g∗‖θ2=‖v‖θ‖g∗‖θ​cos⁡θF.\rho=\frac{\langle g^{*},v\rangle_{\theta}}{\|g^{*}\|_{\theta}^{2}}=\frac{\|v\|_{\theta}}{\|g^{*}\|_{\theta}}\cos\theta_{F}.
Consequently, the leading (first-order) term in the expected capability
gain in Theorem 4.1 can be written as
η​ρ​‖g∗‖θ2=η​‖g∗‖θ​‖v‖θ​cos⁡θF,\eta\rho\|g^{*}\|_{\theta}^{2}=\eta\,\|g^{*}\|_{\theta}\,\|v\|_{\theta}\cos\theta_{F},
i.e. it is proportional to the cosine of the Fisher angle between the
GVU drift vv and the true gradient g∗g^{*}.

Proof.

Taking expectations in (2) and neglecting
bbiasb_{\mathrm{bias}} gives v=𝔼​[g^]≈ρ​g∗v=\mathbb{E}[\hat{g}]\approx\rho g^{*}. Taking
the inner product with g∗g^{*} and using Definition 4.4
yields
⟨g∗,v⟩θ≈ρ​⟨g∗,g∗⟩θ=ρ​‖g∗‖θ2,\langle g^{*},v\rangle_{\theta}\approx\rho\langle g^{*},g^{*}\rangle_{\theta}=\rho\|g^{*}\|_{\theta}^{2},
so
ρ=⟨g∗,v⟩θ/‖g∗‖θ2\rho=\langle g^{*},v\rangle_{\theta}/\|g^{*}\|_{\theta}^{2}. On the
other hand, by Definition 4.4,
cos⁡θF=⟨g∗,v⟩θ‖g∗‖θ​‖v‖θ,\cos\theta_{F}=\frac{\langle g^{*},v\rangle_{\theta}}{\|g^{*}\|_{\theta}\,\|v\|_{\theta}},
which rearranges to
⟨g∗,v⟩θ=‖g∗‖θ​‖v‖θ​cos⁡θF\langle g^{*},v\rangle_{\theta}=\|g^{*}\|_{\theta}\,\|v\|_{\theta}\cos\theta_{F}.
Combining the two identities gives the claimed expression for ρ\rho
and the first-order term in 𝔼​[Δ​F]\mathbb{E}[\Delta F].
∎

Proposition 4.5 shows that, on the statistical
manifold (Θ,g)(\Theta,g), a self-improvement trajectory
γ:r↦θr\gamma:r\mapsto\theta_{r} is driven by a noisy vector field whose
drift is the mean update v​(θ)v(\theta) and whose usefulness
is governed by the Fisher angle θF\theta_{F} between v​(θ)v(\theta) and the
true gradient g∗​(θ)g^{*}(\theta). The Variance Inequality
(Theorem 4.1) then constrains which noisy, sample-based
vector fields can yield positive drift in the battery score
F=Φℬ∘ρℬF=\Phi_{\mathcal{B}}\circ\rho_{\mathcal{B}} while respecting this
geometry: for fixed curvature (through LL) and step size η\eta, we
must simultaneously ensure

1.

geometric alignment:θF\theta_{F} is acute, so that
v​(θ)v(\theta) points mostly along g∗​(θ)g^{*}(\theta) in the Fisher metric;

2.

spectral control: the noise variances
σ𝒢2\sigma_{\mathcal{G}}^{2} and σ𝒱2\sigma_{\mathcal{V}}^{2} remain small
enough that the quadratic curvature penalty does not overwhelm the
linear alignment term.

In other words, a κ\kappa-flow is a stochastic curve on the
statistical manifold whose drift must stay close, in Fisher angle, to
the natural gradient of FF and whose diffusion must be controlled by
a verifier with sufficiently high signal-to-noise ratio. The GVU
design problem is precisely to engineer VV and the induced update
field v​(θ)v(\theta) so that these geometric and spectral conditions can
be satisfied across the relevant fibers of the moduli space.

4.4 Design levers and special cases

The Variance Inequality (Theorem 4.1) does more than
diagnose failure modes: it exposes concrete design levers for
constructing self-improving agents. In this subsection we record a few
generic special cases that cover many architectures in
Section 5.

Corollary 4.6(Step-size window).

Under the assumptions of Theorem 4.1, suppose
bbiasb_{\mathrm{bias}} in (2) is negligible. Then
for any fixed θ\theta with ρ>0\rho>0 there exists a non-trivial
stepsize interval (0,ηmax)(0,\eta_{\max}) such that 𝔼​[Δ​F]>0\mathbb{E}[\Delta F]>0 for
all 0<η<ηmax0<\eta<\eta_{\max}. In particular, from
(3) we may take
ηmax=2​ρ​‖g∗‖2L​(ρ2​‖g∗‖2+σ𝒢2+σ𝒱2).\eta_{\max}=\frac{2\rho\|g^{*}\|^{2}}{L\big(\rho^{2}\|g^{*}\|^{2}+\sigma_{\mathcal{G}}^{2}+\sigma_{\mathcal{V}}^{2}\big)}.
For fixed curvature LL and gradient norm ‖g∗‖\|g^{*}\|, improving either
alignment ρ\rho or the verification SNR (reducing
σ𝒱2\sigma_{\mathcal{V}}^{2}) widens this safe stepsize window.

Proof.

Rearranging (3) for η>0\eta>0 gives
η<2​ρ​‖g∗‖2L​(ρ2​‖g∗‖2+σ𝒢2+σ𝒱2),\eta<\frac{2\rho\|g^{*}\|^{2}}{L\big(\rho^{2}\|g^{*}\|^{2}+\sigma_{\mathcal{G}}^{2}+\sigma_{\mathcal{V}}^{2}\big)},
which defines a non-empty interval (0,ηmax)(0,\eta_{\max}) whenever
ρ>0\rho>0.
∎

Ensemble verifiers.

A natural way to reduce verification noise is to aggregate multiple
judges. The next result isolates the effect of such ensembles in an
idealized setting.

Theorem 4.7(Ensemble verifier scaling).

Fix θ∈Θ\theta\in\Theta and a batch size B∈ℕB\in\mathbb{N}. For each
i=1,…,Bi=1,\dots,B let (xi,yi)∼μ⊗πθ(x_{i},y_{i})\sim\mu\otimes\pi_{\theta} be i.i.d. and
write si:=sθ​(xi,yi)=∇θlog⁡πθ​(yi∣xi)s_{i}:=s_{\theta}(x_{i},y_{i})=\nabla_{\theta}\log\pi_{\theta}(y_{i}\mid x_{i}) for the score function
from Definition 3.4. Let the ideal (oracle) potential be
the external score Sℬ​(x,y)S_{\mathcal{B}}(x,y) of
Definition 3.1.

For each judge m=1,…,Mm=1,\dots,M suppose we have an internal potential
V(m)​(x,y)=Sℬ​(x,y)+ϵm​(x,y),V^{(m)}(x,y)=S_{\mathcal{B}}(x,y)+\epsilon_{m}(x,y),
where the noise terms ϵm\epsilon_{m} satisfy, for all (x,y)(x,y):

1.

𝔼​[ϵm​(x,y)∣x,y]=0\mathbb{E}[\epsilon_{m}(x,y)\mid x,y]=0;

2.

Var​(ϵm​(x,y)∣x,y)=τ2\mathrm{Var}(\epsilon_{m}(x,y)\mid x,y)=\tau^{2} for some
constant τ2<∞\tau^{2}<\infty independent of (x,y)(x,y) and mm;

3.

the collection {ϵm​(x,y)}m=1M\{\epsilon_{m}(x,y)\}_{m=1}^{M} is conditionally
independent given (x,y)(x,y) and independent of
{(xi,yi)}i=1B\{(x_{i},y_{i})\}_{i=1}^{B}.

Define the ensemble potential
V¯​(x,y):=1M​∑m=1MV(m)​(x,y)=Sℬ​(x,y)+ϵ¯​(x,y),ϵ¯​(x,y):=1M​∑m=1Mϵm​(x,y).\bar{V}(x,y):=\frac{1}{M}\sum_{m=1}^{M}V^{(m)}(x,y)=S_{\mathcal{B}}(x,y)+\bar{\epsilon}(x,y),\qquad\bar{\epsilon}(x,y):=\frac{1}{M}\sum_{m=1}^{M}\epsilon_{m}(x,y).

Consider the REINFORCE-style Monte Carlo gradient estimators
g^single\displaystyle\hat{g}_{\text{single}}:=1B​∑i=1BV(1)​(xi,yi)​si,\displaystyle:=\frac{1}{B}\sum_{i=1}^{B}V^{(1)}(x_{i},y_{i})\,s_{i},g^ensemble\displaystyle\hat{g}_{\text{ensemble}}:=1B​∑i=1BV¯​(xi,yi)​si,\displaystyle:=\frac{1}{B}\sum_{i=1}^{B}\bar{V}(x_{i},y_{i})\,s_{i},
and the corresponding ideal oracle estimator
g^∗:=1B​∑i=1BSℬ​(xi,yi)​si.\hat{g}^{*}:=\frac{1}{B}\sum_{i=1}^{B}S_{\mathcal{B}}(x_{i},y_{i})\,s_{i}.
Define the verification noise components by
ξ𝒱,single:=g^single−g^∗,ξ𝒱,ensemble:=g^ensemble−g^∗,\xi_{\mathcal{V},\text{single}}:=\hat{g}_{\text{single}}-\hat{g}^{*},\qquad\xi_{\mathcal{V},\text{ensemble}}:=\hat{g}_{\text{ensemble}}-\hat{g}^{*},
and write
σ𝒱,single2:=𝔼​[‖ξ𝒱,single‖2],σ𝒱,ensemble2:=𝔼​[‖ξ𝒱,ensemble‖2].\sigma_{\mathcal{V},\text{single}}^{2}:=\mathbb{E}\big[\|\xi_{\mathcal{V},\text{single}}\|^{2}\big],\qquad\sigma_{\mathcal{V},\text{ensemble}}^{2}:=\mathbb{E}\big[\|\xi_{\mathcal{V},\text{ensemble}}\|^{2}\big].

Then
σ𝒱,ensemble2=1M​σ𝒱,single2.\sigma_{\mathcal{V},\text{ensemble}}^{2}=\frac{1}{M}\,\sigma_{\mathcal{V},\text{single}}^{2}.
In particular, for fixed ‖g∗‖2\|g^{*}\|^{2} the verification
signal-to-noise ratio scales linearly with MM:
SNR​(𝒱ensemble)=M⋅SNR​(𝒱single),\mathrm{SNR}(\mathcal{V}_{\text{ensemble}})=M\cdot\mathrm{SNR}(\mathcal{V}_{\text{single}}),
and the admissible stepsize ηmax\eta_{\max} from
Corollary 4.6 grows linearly with MM, all else
being equal.

Proof.

By construction,
g^single−g^∗=1B​∑i=1B(V(1)​(xi,yi)−Sℬ​(xi,yi))​si=1B​∑i=1Bϵ1​(xi,yi)​si,\hat{g}_{\text{single}}-\hat{g}^{*}=\frac{1}{B}\sum_{i=1}^{B}\big(V^{(1)}(x_{i},y_{i})-S_{\mathcal{B}}(x_{i},y_{i})\big)\,s_{i}=\frac{1}{B}\sum_{i=1}^{B}\epsilon_{1}(x_{i},y_{i})\,s_{i},
so
ξ𝒱,single=1B​∑i=1Bϵ1​(xi,yi)​si.\xi_{\mathcal{V},\text{single}}=\frac{1}{B}\sum_{i=1}^{B}\epsilon_{1}(x_{i},y_{i})\,s_{i}.
Similarly,
g^ensemble−g^∗=1B​∑i=1Bϵ¯​(xi,yi)​si=1B​∑i=1B(1M​∑m=1Mϵm​(xi,yi))​si,\hat{g}_{\text{ensemble}}-\hat{g}^{*}=\frac{1}{B}\sum_{i=1}^{B}\bar{\epsilon}(x_{i},y_{i})\,s_{i}=\frac{1}{B}\sum_{i=1}^{B}\left(\frac{1}{M}\sum_{m=1}^{M}\epsilon_{m}(x_{i},y_{i})\right)s_{i},
so
ξ𝒱,ensemble=1B​∑i=1Bϵ¯​(xi,yi)​si.\xi_{\mathcal{V},\text{ensemble}}=\frac{1}{B}\sum_{i=1}^{B}\bar{\epsilon}(x_{i},y_{i})\,s_{i}.

We first compute the second moment of the ensemble noise. Conditional
on (xi,yi)(x_{i},y_{i}), the random variables
{ϵm​(xi,yi)}m=1M\{\epsilon_{m}(x_{i},y_{i})\}_{m=1}^{M} are independent, zero-mean, with
v

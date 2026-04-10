---
title: Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain
source_url: https://arxiv.org/html/2603.02218
final_url: https://arxiv.org/html/2603.02218
status: 200
content_type: text/html; charset=utf-8
topics: [Corpus-Grounded Self-Play (SPICE 계열)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.508447+00:00
---

# Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain

## 원본 URL

https://arxiv.org/html/2603.02218

## 추출 본문

Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain
1 Introduction

2 Background
2.1 Background on Triadic Self-Evolution

2.2 Background on Learnable Information

3 Towards Genuine Self-Evolution
3.1 Asymmetric Co-evolution

3.2 Capacity Budgets Grow Across Iterations

3.3 Proactive Information Seeking

3.4 Synergy

4 Experiments

5 Alternative Views

6 Related Works

7 Limitations

8 Call to Action

9 Conclusion

A Experimental Setup

B Epiplexity Calculation Details

C Data Case

Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain

Wei Liu
Siya Qi
Yali Du
Yulan He

Abstract
Large language models (LLMs) make it plausible to build systems that improve through self-evolving loops, but many existing proposals are better understood as self-play and often plateau quickly. A central failure mode is that the loop synthesises more data without increasing learnable information for the next iteration.
Through experiments on a self-play coding task, we reveal that
sustainable self-evolution requires a self-synthesised data pipeline with learnable information that increases across iterations.
We identify triadic roles that self-evolving LLMs play: the Proposer, which generates tasks; the Solver, which attempts solutions; and the Verifier, which provides training signals, and we identify three system designs that jointly target learnable information gain from this triadic roles perspective. Asymmetric co-evolution closes a weak-to-strong-to-weak loop across roles. Capacity growth expands parameter and inference-time budgets to match rising learnable information. Proactive information seeking introduces external context and new task sources that prevent saturation.
Together, these modules provide a measurable, system-level path from brittle self-play dynamics to sustained self-evolution.

Machine Learning, ICML

1 Introduction
Figure 1: A self-evolving LLM plays three roles as Proposer, Solver and Verifier. The whole self-evolving process can be seen as different synthetic operations (synthesis qa, solution and feedback) on the same information source, which is the LLM itself.Figure 2: Overall framework of a triadic self-evolving loop. A self-evolving LLM plays three roles: the Proposer and Verifier form the internal environment, proactively interacting with the external environment to provide data and supervision for the Solver. The Solver and internal environment co-evolve asymmetrically, adaptively expanding capacity to capture more learnable information. From an information perspective, the system continually absorbs external information, and transform them into internal learnable information.

The rapid progress of large language models (LLMs) has made self-evolving AI systems plausible (Gao et al., 2025; Fang et al., 2025). In such systems, a model plays different roles to generate data (Proposer), produce solutions (Solver), and provide feedback signals (Verifier), thereby forming self-training loops autonomously. Related research has evolved from early self-supervised training systems (Zelikman et al., 2022; Yuan et al., 2023; Gülçehre et al., 2023; Yuan et al., 2024; Dong et al., 2025; Chen et al., 2024; Qu et al., 2024; Tu et al., 2025) towards more recent self-play systems trained with reinforcement learning (Zhao et al., 2025a; Huang et al., 2025; Yue et al., 2026; Yang et al., 2025; Liu et al., 2025a; Chen et al., 2025a; Lu et al., 2025; Hong et al., 2025a; Wang et al., 2025; Guo et al., 2025b). Some focus on verifiable domains such as mathematics and coding, where a fixed Verifier is available, and the LLM performs self-play between the Proposer and Solver roles. Others emphasise free-form domains, such as preference learning and instruction following, where the Solver and Verifier are co-evolved on a fixed dataset. In most cases, these systems adopt multi-reward reinforcement learning to achieve self-evolution.

Despite their promise, such systems are often fragile and quickly enter a plateau or collapse after only a few rounds of self-play. In self-play between Proposer and Solver, Zhao et al. (2025a) report that the Proposer tends to generate trivial identity-like problems (f​(x)=xf(x)=x). Huang et al. (2025) and Yue et al. (2026) observe an early peak and subsequent decline in overall model performance. Chen et al. (2025a) report that the Proposer requires carefully tuned prompts to ensure the proposed data remains within a reasonable regime.
Some approaches benefit from periodically introducing ground truth data to recalibrate the Verifier(Yang et al., 2025; Lu et al., 2025). Without such intervention, the system risks falling into a state of self-delusion, resulting in a rapid decline in overall performance.

To resolve this mode collapse and achieve genuine self-evolution, we argue that self-evolution should be viewed as a healthy self-synthesised data pipeline, where the Proposer, Solver, and Verifier operate cooperatively to ensure a monotonic increase in learnable information, rather than relying on fragile self-play dynamics.

This position extends beyond a trivial composition of P+SP+S and S+VS+V into P+S+VP+S+V(Yang et al., 2025; Chen et al., 2025b). It treats the self-evolving loop as a self-synthetic data pipeline (as shown in Figure 1), whose success is characterised by an increase in learnable information over iterations.
We make this requirement precise by formalising learnable information under bounded observers in §2.2.
The information-theoretic view makes this question concrete. It separates learnable structure from unlearnable noise under bounded computation, which clarifies why reward shaping alone is insufficient for sustained improvement. Empirical analysis of existing self-play loops further validates this diagnosis. Motivated by this observation, we propose three system-level design principles for the self-evolution loop.

1.

Asymmetric Co-evolution. We frame self-evolution as a co-evolutionary process between the Solver and its internal environment, consisting of the Proposer and Verifier. Although all roles share the same information source (pre-trained model weights), and their divergent synthetic directions (synthesis question, solution and feedback) induce an information gap that enables weak-to-strong supervision. This asymmetry needs to be explicitly preserved by synchronising improvements in the Solver back to the internal environment as strong-to-weak supervision, thereby sustaining continuous self-improvement.

2.

Capacity Growth. The learnable information in self-synthesised data is determined not only by the data distribution but also by the capacity of the observer model. As self-evolution progresses, the model needs to continually expand its effective capacity budgets, encompassing both parameter capacity and inference-time computation, to keep pace with the increasing amount of learnable information produced within the loop.

3.

Proactive Information Seeking. Self-evolution driven by zero-data or a fixed dataset is fundamentally bounded by finite information. We argue that a self-evolving system should proactively acquire external information sources aligned with its current capabilities. Such sources provide not only new contexts for synthetic data but also new synthetic directions, creating fresh asymmetries that can be exploited by the internal co-evolutionary process.

2 Background

We model self-evolution as an iterative process that produces self-synthetic training data D(t)D^{(t)} and updates a single LLM with it. The goal is not merely to improve task accuracy within a fixed self-play game, but to ensure that the learnable information in D(t)D^{(t)} increases during iterations.

2.1 Background on Triadic Self-Evolution

View of System Design. At iteration tt, the LLM acts as a Proposer to generate tasks, optionally conditioned on external context. It then acts as a Solver to produce solutions. It finally acts as a Verifier to assess the solutions and produce feedback signals. The next update trains the base model on the resulting self-synthetic training instances D(t)D^{(t)}, which include tasks, solutions, and verification signals. In this loop, there is no external labelled dataset, teacher model, or reward model, so the loop is self-evolving.
The Proposer and Verifier form the internal environment (Guo et al., 2025b) of the system. They jointly shape what the Solver practises and what feedback becomes a learnable training signal. An external environment, when present, provides information sources such as documents or interactive worlds (Liu et al., 2025a). Usually, such information enters as context that conditions task and evaluation generation.
This three-role design matters for scope. P+SP+S with a rule-based Verifier constrains its application to reinforcement learning from verifiable rewards (RLVR). S+VS+V focuses on free-form domains and trains a better Verifier by learning on fixed preference data instead of self-synthesised data. Triadic self-evolution targets both regimes by evolving all three roles, which share one base model. Improvements in any role update the same underlying model, making the loop self-evolving rather than a collection of separate agents.

View of Information Flow. Viewed as information flow, the self-evolving loop produces a self-synthesised data stream. Proposing, solving, and verifying are different transformations of a shared information source: the information contained in the pre-trained weights of the LLM. If proposing is conditioned on an external environment, the loop can incorporate information that is not present in the pre-trained source, which most current self-play systems do not provide. Many self-play systems still achieve progress despite the “no-new-information” concern. This progress can be understood as a transformation that converts unlearnable noise into learnable information for the next update. Based on this view, we introduce three key designs that ensure a three-role self-evolving system supports sustained growth of learnable information across iterations, going beyond fragile reward shaping. We formalise learnable information in §2.2 and then present the three design claims in §3.

2.2 Background on Learnable Information

We introduce learnable information as the notion that matters for self-evolution. Shannon entropy (Shannon, 1948) characterises the total uncertainty of a distribution. It does not distinguish reusable structure from randomness, which is directly relevant to learning.
Minimum description length (MDL) (Rissanen, 1978) provides a criterion that is aligned with learning. It evaluates a model by the description length it induces for the data. This length decomposes into a model description and a prediction loss. This decomposition motivates a separation between learnable structure and unlearnable components.
Learnable information refers to the part of data that a learner can capture as a reusable structure, such as patterns that allow better compression or prediction.
Unlearnable information is whatever remains unpredictable or incompressible given the learner’s assumptions, capacity, and training method, and thus appears as noise.
Formal treatments of this distinction are studied extensively in computational complexity and information theory (Koppel, 1987; Bennett, 1988; McAllister, 2003; Allender et al., 2011).

Importantly, learnable information is not an absolute property of the data, but is defined relative to the observer. While MDL provides a learning-aligned criterion, it assumes an unlimited observer computation budget. However, self-evolving LLMs operate under explicit capacity and computation constraints. Epiplexity (Epistemic Complexity) (Jiang, 2025; Finzi et al., 2026) makes this dependence explicit by introducing computational budgets for the observer. This makes epiplexity a natural match for modelling self-evolving LLMs. We therefore adopt epiplexity as a measurement tool that instantiates an MDL objective under explicit parameter and inference-time budgets, yielding operational proxies for learnable and unlearnable information.

We use tt for the self-evolution iteration index. For each role r∈{Proposer,Solver,Verifier}r\in\{\textsc{Proposer},\textsc{Solver},\textsc{Verifier}\}, we allow budgets (Cr(t),Tr(t))(C_{r}^{(t)},T_{r}^{(t)}) that can depend on the role and the iteration. Here CC denotes parameter capacity and TT denotes inference-time computation. When a single budget pair is sufficient, we write (C,T)(C,T). We denote by Dd(t)D_{d}^{(t)} the distribution over synthetic directions dd used by the internal environment to generate self-synthetic training instances at iteration tt.
Let XX denote the self-synthesised data stream produced by the loop. Following Finzi et al. (2026), we make the bounded observer constraints explicit: let CC denote a parameter budget (capacity) and let TT denote an inference-time budget (computation/trajectory length). Let 𝒫C,T\mathcal{P}_{C,T} denote a family of LLM observers implementable within budgets (C,T)(C,T). Define the bounded MDL optimiser:
P⋆=arg​minP∈𝒫C,T⁡{|P|+𝔼​[log⁡1P​(X)]},\displaystyle\mathrm{P^{\star}}=\operatorname*{arg\,min}_{\mathrm{P}\in\mathcal{P}_{C,T}}\left\{|\mathrm{P}|+\mathbb{E}\!\left[\log\frac{1}{P(X)}\right]\right\},(1)
and define SC,T​(X)\mathrm{S}_{C,T}(X) and HC,T​(X)\mathrm{H}_{C,T}(X) as:
SC,T​(X):=|P⋆|,\displaystyle\mathrm{S}_{C,T}(X):=|\mathrm{P^{\star}}|,(2)HC,T​(X):=𝔼​[log⁡1P⋆​(X)],\displaystyle\mathrm{H}_{C,T}(X):=\mathbb{E}\!\left[\log\frac{1}{P^{\star}(X)}\right],(3)MDLC,T​(X):=SC,T​(X)+HC,T​(X).\displaystyle\mathrm{MDL}_{C,T}(X):=\mathrm{S}_{C,T}(X)+\mathrm{H}_{C,T}(X).(4)
where SC,T​(X)\mathrm{S}_{C,T}(X) is the epiplexity, and HC,T​(X)\mathrm{H}_{C,T}(X) is the bounded entropy. Intuitively, HC,T​(X)\mathrm{H}_{C,T}(X) represents what still appears random to the bounded observer, which can be regarded as unlearnable information given an LLM constrained by (C,T)(C,T). In contrast, SC,T​(X)\mathrm{S}_{C,T}(X) represents the reusable structure the observer needs to internalise to compress or predict the data, which we treat as a proxy for learnable information. Because these quantities depend on (C,T)(C,T), the same object can appear structured to a stronger observer and random to a weaker one.
Epiplexity thus identifies a “Goldilocks Zone” for self-evolution: data must be neither too simple (low S\mathrm{S}, low H\mathrm{H}) nor too hard (low S\mathrm{S}, high H\mathrm{H}) for the current observer. Sustainable progress requires the system to continuously generate data within this zone, where the structure is complex enough to be non-trivial but structured enough to be learnable.

Figure 3: Illustration of three designs from the perspective of learnable information. Asymmetry between the Solver and the Proposer/Verifier creates learning opportunities. Expanding model capacity to match self evolving data opens space for learnable information. Reusing the same patterns in new contexts yields limited gains, whereas introducing new synthetic directions creates fresh asymmetries and thus new sources of learnable information. 

3 Towards Genuine Self-Evolution

We now connect the self-evolving loop to three necessary designs: asymmetry, capacity, and information seeking, as shown in Figure 2. For each claim, we separate the system-level mechanism from its information-theoretic justification. We then contrast these mechanisms with existing self-play systems and summarise practical implementations.

3.1 Asymmetric Co-evolution
Figure 4: Climbing the intelligence asymmetry ladder by closing the loop among Proposer, Solver, and Verifier. “Intelligence synchronisation” denotes updating the weaker Proposer/Verifier with strong Solver. “Reinforcement learning” uses the weaker Proposer/Verifier to train the Solver.

Design. In many tasks, proposing and verifying are substantially easier than solving. This asymmetry is well established in easy-to-verify domains such as mathematics and coding (Guo et al., 2025a), and also appears in more general task settings (Burns et al., 2024). Leveraging this asymmetry enables a self-evolving system. When a single LLM plays all three roles, its current proposing and verification ability can supervise the training of a stronger Solver (weak-to-strong). For sustained self-evolution, the improved Solver needs to be synchronised back into the internal environment (strong-to-weak) to close the loop, so that proposing and verification keep pace with the Solver frontier, as illustrated in Figure 4. In contrast, using a stronger LLM to propose and verify to train a weaker LLM constitutes distillation rather than self-evolution.
Reinforcement learning can realise the weak-to-strong transition.
We argue for a more explicit design of the strong-to-weak directions, with two objectives: ensure that capacity of Verifier scale with the solver;
ensure that Proposer remains at the Solver frontier and continues to open new synthetic directions.
This suggests that asymmetry should be organised as a progressive ladder matched to the solver’s frontier.

Information Perspective.
All three roles operate on the same information source, namely the pre-trained weights, but along different synthetic directions.
The Proposer synthesises questions and reference answers, the Solver synthesises solutions conditioned on questions, and the Verifier synthesises feedback conditioned on the task, reference, and solution.
From a fixed source, such transformations do not create new Shannon information (Shannon, 1948), but they can redistribute learnable information across forward and inverse directions under bounded computation when the inverse mapping is computationally hard (Finzi et al., 2026). In our setting, a synthetic direction d​(P,S,V)d(P,S,V) defines a computation that maps shared weights into a data stream XdX_{d}. Consequently, the bounded MDL decomposition into SC,T​(Xd)\mathrm{S}_{C,T}(X_{d}) and HC,T​(Xd)\mathrm{H}_{C,T}(X_{d}) can differ across roles, even under identical resource budgets.

Beyond information creation, boundedness also breaks the symmetry of information across factorisations, inducing a gap between forward and inverse directions that naturally aligns with proposing and verifying versus solving. Although not all tasks can be strictly modelled as a function Y=f​(X)Y=f(X) and its inverse, the underlying computational asymmetry is broadly applicable. The Proposer maps pre-trained knowledge into a problem space, such as generating a poem topic or a mathematics problem, while the Solver maps that problem into a concrete solution trace. Even in open-ended tasks like creative writing, generating a high-level constraint (“write a poem about spring”) is computationally cheaper than producing a specific instance that satisfies it.
A one-way permutation illustrates how extreme this asymmetry can be. Given ff as a polynomial-time computable one-way permutation secure against non-uniform PPT inverters with negligible success probability, if we apply it to uniform input XX to produce Y=f​(X)Y=f(X), then
Hpoly​(X|Y)−Hpoly​(Y|X)≥c​log⁡n\displaystyle H_{\text{poly}}(X|Y)-H_{\text{poly}}(Y|X)\geq c\log n(5)
The gap of Ω​(log⁡n)\Omega(\log n) bits quantifies how much harder it is to predict backwards versus forward (Finzi et al., 2026). This gap captures the information-theoretic form of intelligence demand asymmetry. The internal environment can cheaply generate and verify instances, while the Solver needs to expend additional computation to reduce residual uncertainty in the inverse direction.
Training can convert part of this residual uncertainty into reusable structure, corresponding to learnable information gain, but only when the inverse direction contains structure accessible under the current budgets.
This perspective also clarifies the role of gap size. A larger directional gap can expose richer structure and increase potential epiplexity gain, but when the gap exceeds the Solver capacity, it appears as time-bounded randomness, yielding noise-like tasks and stalled learning. Therefore, self-evolution requires an asymmetry ladder that matches the gap to the current Solver, together with strong-to-weak synchronisation so the Proposer and Verifier track the Solver frontier.

Gaps. Standard reinforcement learning can achieve the weak-to-strong flow from the Proposer/Verifier to Solver, but it is less clear whether improvements in the Solver reliably induce corresponding gains in the Proposer and Verifier. If the internal environment fails to co-evolve, then as the Solver improves, the task/feedback stream can become low-structure relative to the current observer, encouraging collapse towards trivial data.

Practice. To fully exploit asymmetry in self-evolving systems and to close the loop of weak-to-strong and strong-to-weak stably, it requires both data engineering and algorithmic innovations: 1) Organise self-synthetic directions by asymmetry gaps. self-synthesised data need to be carefully structured, allowing the LLM to grow by climbing an asymmetry ladder, progressing from small gaps to large gaps, and eventually to reverse gaps (when the Proposer and Verifier become sufficiently strong). This requires organising synthetic directions by domain (e.g., mathematics problems typically exhibit a large gap; grammar correction has minimum gaps; and healthcare tasks may exhibit inverse gaps), and even within domains (e.g., abduction, induction, and deduction problems in coding (Zhao et al., 2025a), or conjecture proving vs. large-number multiplication vs. Sudoku in maths). 2) Implement strong-to-weak synchronisation for the Proposer. For the Proposer, self-play reward designs, such as using a 50% pass rate for the Solver as a reward, can partially address synchronisation, though multi-reward training is often unstable (Zhao et al., 2025a; Kwan et al., 2025; Huang et al., 2025; Chen et al., 2025b). An alternative approach is to back-translate higher-quality Proposer’s data from a stronger Solver. For example, Magicoder (Wei et al., 2024) generates diverse instructions from code snippets; MathGenie (Lu et al., 2024) back-translates questions from augmented ground truth; InverseCoder (Wu et al., 2025b) summarises code into instructions. 3) Implement strong-to-weak synchronisation for the Verifier. For the Verifier, reward design is more challenging; most research uses self-consistency or internal belief signals (Zhao et al., 2025b; Zuo et al., 2025; Yang et al., 2025), which do not guarantee improvement of the verifier. A promising direction is verifier-free RL (Liu et al., 2025b; Yu et al., 2025; Zhou et al., 2025), where the Verifier and Solver explicitly share the same optimisation objective, typically maximising the probability of generating the ground truth answer given the question and model’s reasoning trajectory.

3.2 Capacity Budgets Grow Across Iterations

Design. Most self-play loops fix the observer across iterations. Sustainable self-evolution instead requires budgets that grow with iteration. We define capacity as the portion of the model effectively participating in learnable information extraction, which may include the full parameter set, or a sparsely activated component (e.g., experts, layers). In general, capacity is determined by a parameter budget C(t)C^{(t)}, an inference-time budget T(t)T^{(t)}, and a training budget B(t)B^{(t)}. In many existing self-evolving setups, the incremental dataset per iteration is small, so B(t)B^{(t)} remains almost constant. However, C(t)C^{(t)} and T(t)T^{(t)} should not be fixed: as the loop exposes more learnable structure over time, capacity should increase to allow the observer to absorb new information, either by growing parameters, activating more of the model, or increasing reasoning length.

Information Perspective. Epiplexity makes the dependence on the observer budgets (C,T)(C,T) explicit by defining SC,T​(X)\mathrm{S}_{C,T}(X) and HC,T​(X)\mathrm{H}_{C,T}(X) through an MDL objective optimised within an observer family 𝒫C,T\mathcal{P}_{C,T}. Fixing (C,T)(C,T) bounds the amount of reusable structure the observer can internalise from the self-synthetic stream. Expanding these budgets enlarges the observer family. If 𝒫C1,T1⊆𝒫C2,T2\mathcal{P}_{C_{1},T_{1}}\subseteq\mathcal{P}_{C_{2},T_{2}}, then MDLC2,T2​(X)≤MDLC1,T1​(X)\mathrm{MDL}_{C_{2},T_{2}}(X)\leq\mathrm{MDL}_{C_{1},T_{1}}(X). Budget expansion, therefore, shifts the boundary between reusable structure and residual randomness.

Gaps.
Budget mismatches induce characteristic failure modes. Fixing C(t)C^{(t)} while the loop generates richer trajectories prevents the observer from representing the abstractions needed to compress new data. Training loss saturates and progress plateaus. The loop then shifts toward directions that remain easy for the current model class, reducing frontier pressure and potentially collapsing to trivial tasks (Huang et al., 2025; Yue et al., 2026).
Fixing T(t)T^{(t)} produces a distinct failure mode. The internal environment can raise difficulty by proposing tasks that require longer reasoning chains or more tool use. When the inference-time budget is limited, errors stem from truncated inference rather than learnable deficiencies. Both mismatches reduce the learnable information available to subsequent updates.

Practice. Capacity growth should be planned along both axes. The parameter budget C(t)C^{(t)} can be expanded through role-asymmetric scaling where a smaller Proposer/Verifier trains a larger Solver, and the internal environment is refreshed from the stronger checkpoint. Alternatively, the parameter budget can be expanded by adding parameters across iterations, allowing the base model itself to grow without relying on a larger pre-trained model (Gong et al., 2019; Xie et al., 2020; Hong et al., 2025b; Singh et al., 2025). It is also worth exploring activated subset growing (Huang et al., 2024; Nishu et al., 2025).
The inference-time budget T(t)T^{(t)} should likewise be explicit and dynamic. The system should allocate increasing computation per instance as iteration advances. This requires adaptive reasoning along the inference token axis (Alomrani et al., 2025; Qu et al., 2025) or adaptive recursive depth along the layer axis (Bae et al., 2025).

3.3 Proactive Information Seeking

Design. A closed self-play loop without external interaction is bounded by information already present in the current system. Simply adding a fixed external corpus does not resolve this limitation because the loop collapses into repeated training on a static support. We therefore treat information seeking as an explicit responsibility of the internal environment (Proposer+Verifier): at each iteration, it should select external contexts, and learn new synthetic directions around them.

Information Perspective.
External information can enter a self-evolving loop in two ways. It can be incorporated directly into training or supervision, which increases total information but breaks pure self-synthesis. Alternatively, it can be used only as a conditioning context. Let d(t)d^{(t)} denote the external context obtained at iteration tt, and Y(t)Y^{(t)} as self-synthetic outputs generated by the internal environment conditioned on d(t)d^{(t)}. Since optimisation targets lie in Y(t)Y^{(t)} rather than d(t)d^{(t)}, the relevant quantity is the learnable information in the conditional stream (Y(t)∣d(t))(Y^{(t)}\!\mid d^{(t)}).
We formalise this using a conditional bounded MDL objective (for brevity, we denote M​D​LC,TMDL_{C,T} as M​D​LMDL):
MDL​(Y∣d):=minP∈𝒫C,T⁡{|P|+𝔼​[log⁡1P​(Y∣d)]}\mathrm{MDL}(Y\!\mid d):=\min_{P\in\mathcal{P}_{C,T}}\left\{|P|+\mathbb{E}\!\left[\log\frac{1}{P(Y\mid d)}\right]\right\}(6)
, and treat SC,T​(Y∣d)\mathrm{S}_{C,T}(Y\!\mid d) as conditional learnable information by analogy with Equation2.
Even with static d(t)d^{(t)}, the internal environment can repeatedly propose new questions and evaluations that demand progressively richer reasoning. This shifts the synthetic direction support without using the corpus as labels. The mechanism is theoretically supported by conditional epiplexity, which preserves information gain and asymmetry properties, and is empirically supported by self-play in corpus environments (Liu et al., 2025a). Finally, since epiplexity depends on factorisation and ordering (Finzi et al., 2026), how context is converted into tasks, and the schedule by which tasks are introduced, directly affect which structure becomes learnable at each iteration.

Gaps.
Existing systems typically fall into three regimes. Zero-data systems use no external information, so reachable contexts are confined to the current weights and the loop recycles directions. Dataset-driven systems sample from a fixed corpus (Liu et al., 2025a), which reduces to fine-tuning on the corpus, and limits the internal environment from catching the evolving Solver frontier. A third class attaches external context via a fixed, iteration-independent mechanism (Xu et al., 2025; Zhang et al., 2025a), yielding a static context distribution.
Early in training, such contexts often exceed the Solver budgets and yield little learning. Later, the same mechanisms become routine and fail to expose new learnable structure. Across regimes, information seeking is reactive rather than proactive: systems consume available context instead of selecting contexts and transformations aligned with the current frontier.

Practice. Proactive information seeking can be realised as an adaptive policy within the internal environment: 1) Learn to ask for information. The Proposer generates queries from Solver failures, Verifier disagreement, or persistent error patterns, and after retrieving dd, synthesises tasks whose solutions require explicit use of dd, such as citation grounded answers, multi-document synthesis, or contradiction detection, thereby coupling retrieval to the current frontier rather than treating it as fixed preprocessing. 2) Turn context into asymmetry gaps rather than hints. Given the same retrieved dd, the internal environment synthesises multiple synthetic directions with different difficulty profiles, and schedules them as a curriculum matched to the iteration state, prioritising grounding and evaluation early and inverse or compositional directions later as budgets grow, which exploits factorisation dependence of bounded information and sustains learnable information growth. 3) Co-evolve with the external environment. Retrieval, reranking, and memory are treated as evolving components and updated using self-synthetic signals such as verifier-based relevance checks; whereas prior work co-evolves only the Solver with the internal environment (Guo et al., 2025b) or frames external evolution as memory refinement over trajectories (Hu et al., 2025).

3.4 Synergy

These three modules are not independent add-ons but functional components of a single information production pipeline whose synergy ensures a monotonic increase in learnable information. Specifically, Asymmetric Co-evolution acts as the generator by exploiting the computational gap between verifying and solving, it performs the critical transformation of converting unlearnable noise into learnable structure, creating the “information potential” that drives the solver’s gradient. To capture this gain, Capacity Growth acts as the receiver, expanding the observer’s hypothesis space to internalise newly exposed learnable information that would otherwise saturate a fixed-budget model. Finally, Proactive Information Seeking acts as the open feeder, continuously injecting fresh entropy and contexts into the internal environment to ensure the generator never exhausts its raw material. Together, these designs transform self-evolution from a finite game of self-play into an open-ended process of learnable information discovery, as shown in Figure 3.

Figure 5: Epiplexity results on synthetic data with different tasks (induction, abduction and deduction) proposed by different Proposer LLMs and observed by different Solver LLMs. See details of calculating epiplexity in Appendix B.

4 Experiments

We conduct small-scale self-play training experiments and extend the Prequential Coding-based estimation method of Finzi et al. (2026) to estimate learnable information.
The experiments are diagnostic rather than exhaustive, aiming to illustrate how learnable information varies across roles, capacities, and synthetic directions.
We use the prequential code length at the point achieving the optimal MDL value to estimate epiplexity as a measure of learnable information, which is
|Ppreq|≈∑i=0M−1(log⁡1Pi​(Zi)−log⁡1PM​(Zi)),|\mathrm{P}_{\mathrm{preq}}|\approx\sum_{i=0}^{M-1}\left(\log\frac{1}{P_{i}(Z_{i})}-\log\frac{1}{P_{M}(Z_{i})}\right),(7)
Here, ZiZ_{i} is the ii-th training token, Pi​(⋅)P_{i}(\cdot) denotes the predictive distribution of the model before observing ZiZ_{i}, and PM​(⋅)P_{M}(\cdot) is the predictive distribution of the fully trained model.
This quantity can be interpreted as the effort expended by the model to learn the data. Further details are provided in Appendix A.

Algorithm 1 presents the pseudocode for estimating epiplexity using prequential coding.
The dataset 𝒟\mathcal{D} is split into training and validation subsets. During training, the model processes each batch sequentially, updating parameters via gradient descent. In the first pass, the prequential loss is accumulated to measure the difficulty of learning each data point. At the end of each epoch, the total training and validation losses are computed. The epiplexity is defined as the difference between the prequential and final training losses, representing the model’s cumulative online regret. The MDL score combines the normalised epiplexity (model cost) and validation loss per-token (data cost). The algorithm then returns the epiplexity corresponding to the epoch that minimises this MDL score.

Algorithm 1 Epiplexity Estimation via Prequential MDL

0: Observer LLM Mθ0M_{\theta_{0}}, dataset 𝒟=𝒟train∪𝒟val\mathcal{D}=\mathcal{D}_{\text{train}}\cup\mathcal{D}_{\text{val}}

0: Max epochs KK, learning rate η\eta

0: Observed epiplexity ℰ∗\mathcal{E}^{*} from Mθ0M_{\theta_{0}} on 𝒟\mathcal{D}

1:θ←θ0\theta\leftarrow\theta_{0}

2:ℒonline←0\mathcal{L}_{\text{online}}\leftarrow 0, Ntrain←0N_{\text{train}}\leftarrow 0

3:M​D​L∗←∞MDL^{*}\leftarrow\infty, ℰ∗←0\mathcal{E}^{*}\leftarrow 0

4:fork=1k=1toKKdo

5:forx∈𝒟trainx\in\mathcal{D}_{\text{train}}do

6:ℓ←−log⁡Pθ​(x)\ell\leftarrow-\log P_{\theta}(x)

7:ifk=1k=1then

8:ℒonline←ℒonline+ℓ\mathcal{L}_{\text{online}}\leftarrow\mathcal{L}_{\text{online}}+\ell

9:Ntrain←Ntrain+CountTokens​(x)N_{\text{train}}\leftarrow N_{\text{train}}+\text{CountTokens}(x)

10:endif

11:θ←θ−η​∇θℓ\theta\leftarrow\theta-\eta\nabla_{\theta}\ell

12:endfor

13:ℒtrain←∑x∈𝒟train−log⁡Pθ​(x)\mathcal{L}_{\text{train}}\leftarrow\sum_{x\in\mathcal{D}_{\text{train}}}-\log P_{\theta}(x)

14:ℒval←∑x∈𝒟val−log⁡Pθ​(x)\mathcal{L}_{\text{val}}\leftarrow\sum_{x\in\mathcal{D}_{\text{val}}}-\log P_{\theta}(x)

15:Nval←CountTokens​(𝒟val)N_{\text{val}}\leftarrow\text{CountTokens}(\mathcal{D}_{\text{val}})

16:S←(ℒonline−ℒtrain)/ln⁡2S\leftarrow(\mathcal{L}_{\text{online}}-\mathcal{L}_{\text{train}})/\ln 2

17:M​D​L←S/Ntrain+(ℒval/ln⁡2)/NvalMDL\leftarrow S/N_{\text{train}}+(\mathcal{L}_{\text{val}}/\ln 2)/N_{\text{val}}

18:ifM​D​L<M​D​L∗MDL<MDL^{*}then

19:M​D​L∗←M​D​LMDL^{*}\leftarrow MDL

20:ℰ∗←S\mathcal{E}^{*}\leftarrow S

21:endif

22:endforreturnℰ∗\mathcal{E}^{*}

We conduct two experiments. Experiment 1 compares the epiplexity values observed by solvers of different capacities on synthetic data generated by proposers of varying capacities along different synthetic data directions. Experiment 2 examines how the synthetic data evolves over iterations as the model engages in continued self-play.
The data and self-play setup follows Zhao et al. (2025a), which has three types of code-based tasks, including abduction, where the input is generated given a program and its output; deduction, where the output is generated given a program and an input; and induction, where the program is generated given an input and an output. Examples of the three task types are shown in Appendix C.

Experiment 1. The results are shown in Figure 5, from which we observe the following. 1) Stronger proposers, from Qwen2.5 7B to Qwen2.5 14B to Qwen3 4B, generate synthetic data that contains a larger amount of learnable information. 2) As the Solver size increases, the learnable information first increases and then decreases. This is consistent with the emergence phenomena observed in Finzi et al. (2026). Under a fixed computation budget, the model is forced to learn compressible patterns and structure, in which regime a larger model can observe higher learnable information. Once a certain budget threshold is exceeded, the model instead opts for direct memorisation and abandons learning effective structure, leading to a decrease in learnable information. 3) Different synthesis directions yield different amounts of learnable information, with induction being substantially higher than abduction and deduction, which aligns with intuition.
These preliminary experiments support our claim: different synthetic directions yield varying amounts of information, and effective co-evolution is necessary to continuously increase learnable information; otherwise, simply increasing the proposer’s capacity may in fact reduce the information content.

Experiment 2. The results are shown in Figure 6. After multiple iterations of self-play training, we observe that the amount of information does not increase steadily but instead fluctuates dramatically. This aligns with both the Zhao et al. (2025a) and our empirical observations. Without an explicit mechanism to close the self-training loop and relying solely on multi-reward reinforcement learning, the model fails to achieve sustained evolution. Behaviourally, this manifests as a decline in Solver capability and a collapse of the problem patterns generated by the proposer.

Figure 6: Epiplexity results during the self-play training on three tasks. See task detail in Appendix C.

5 Alternative Views

Several perspectives have been proposed to explain progress in self-evolving language model systems. However, we argue that none of these perspectives provides a sufficient criterion for identifying genuine and sustained self-evolution.

Self-Evolving via Self-Play RL.
Self-evolution is often studied with stable reward design and monotonic improvement under reinforcement learning. While reward optimisation is essential for guiding behaviour and stabilising training, it does not ensure that the self-synthesised data stream exposes an increasing learnable structure under bounded observers. Systems may improve reward via hacking (Jiang et al., 2025; Zha et al., 2025; Zhang et al., 2025b), rely on memorised pre training knowledge rather than reasoning (Shao et al., 2025; Wu et al., 2025a; Yan et al., 2026), or exhibit instability in multi-reward self-play (Zhao et al., 2025a; Kwan et al., 2025; Huang et al., 2025; Chen et al., 2025b). In these cases, task-level metrics improve while learnable information remains unchanged. We therefore view reward optimisation as necessary but not sufficient for genuine self-evolution.

Curriculum Learning for Evolution.
Curriculum-based approaches aim to match task difficulty to the solver’s capability to sustain learning and avoid collapse. While essential, difficulty conflates factors such as search depth and verification cost and does not directly reflect whether a new structure becomes learnable. A curriculum can increase apparent difficulty while repeatedly sampling structurally similar synthetic directions, leading to optimisation without information gain. From an information perspective, curricula contribute to self-evolution only when they increase bounded learnable information.

Co-Evolution between Agent and Environment Co-evolutionary perspectives frame progress as mutual adaptation between an agent and an evolving environment. Our framework is compatible with this view and models the proposer and verifier as an internal environment that co-evolves with the solver.
However, co-evolution alone does not distinguish productive adaptation from dynamics that reshuffle complexity without expanding internal structure. An evolving environment can become more challenging while exposing less reusable structure to a bounded learner. Introducing an explicit notion of learnable information provides a principled way to assess when co-evolution supports sustained self-evolution.

Scaling is All you Need. Increasing model size or inference-time budget is often expected to resolve stagnation in self-evolving systems. Greater capacity expands what can be learned.
However, without mechanisms that introduce new synthetic directions and maintain asymmetry, increased capacity may primarily amplify memorisation rather than structural generalisation. We therefore view capacity scaling as a necessary component coordinated with information growth, rather than a sufficient explanation on its own.

6 Related Works

Self-Training. Early self-training methods bootstrap reasoning from self-generated data with fixed verification: STaR (Zelikman et al., 2022) filters correct reasoning traces for fine-tuning, ReST (Gülçehre et al., 2023) alternates offline generation and reward filtered updates, and scaling studies (Yuan et al., 2023) report log-linear gains from rejection sampling. These approaches saturate once the initial distribution is exhausted.

Solver–Verifier Co-Evolution. Self-rewarding (Yuan et al., 2024) uses the model as its own judge via LLM-as-a-judge prompting; SPIN (Chen et al., 2024) distinguishes synthetic from human responses through iterative DPO; Self-boosting (Dong et al., 2025) generates diverse prompts and improves responses iteratively; iterative DPO (Tu et al., 2025) refines both generator and reward model over multiple rounds with verifiable rewards; URPO (Lu et al., 2025) unifies policy and reward optimisation in a unified task format; Cooper (Hong et al., 2025a) co-optimises both using hybrid rule-based and model-based rewards to prevent reward hacking; Recursive introspection (Qu et al., 2024) frames multi-turn self-correction as an MDP. However, these methods lack explicit strong-to-weak synchronisation to ensure the Verifier tracks Solver improvements or expands the task distribution beyond the initial corpus.

Proposer–Solver Self-Play. Absolute Zero (Zhao et al., 2025a) self-propose code-based tasks verified by execution; R-Zero (Huang et al., 2025) uses pseudo-labels from majority voting and rewards tasks near the solver’s decision boundary; Dr. Zero (Yue et al., 2026) applies hop-grouped policy optimisation to search agents with multi-turn reasoning; Self-Questioning (Chen et al., 2025a) generates topic-conditioned questions verified via majority voting or unit tests. These methods achieve rapid initial gains but report instability and collapse after a few iterations because the Proposer drifts towards trivial or unsolvable tasks.

Triadic Loops SPELL (Yang et al., 2025) introduces a questioner–responder–verifier loop for long-context reasoning with curriculum over context length; SPICE (Liu et al., 2025a) grounds task generation in external corpora to provide information asymmetry and reduce hallucination; Socratic-Zero (Wang et al., 2025) uses a frozen teacher to verify and craft novel questions targeting Solver weaknesses; GenEnv (Guo et al., 2025b) co-evolves the policy and internal environment that generates tasks aligned to the agent’s current ability. Despite these advances, most systems still report early plateaus, require careful reward tuning, or lack a unified principle for diagnosing why loops stall. Our position addresses these gaps by framing self-evolution as a learnable information pipeline under bounded observers, making three system-level requirements explicit.

7 Limitations

This work provides a preliminary approach to designing a self-evolving framework for stable growth of learnable information, yet it remains far from a fully mature, off-the-shelf solution, and several limitations warrant further exploration. First, closing the asymmetry gap is currently applicable only in domains that are easy to verify. On the hard-to-verify side, more cross-domain, generalizable methods are needed to make breakthroughs. Second, learnable information cannot replace metrics related to final task accuracy, as it is a macroscopic measure; not all learnable information is necessarily useful for task completion, as it may primarily reflect the structure inherent in the data. Both types of metrics need to be considered together to achieve comprehensive monitoring of self-evolving systems. Finally, realising proactive context information seeking remains a major challenge, as it requires the model to recognise what it does not know (Yin et al., 2023) and explicitly formulate it as a query, which is an inherently difficult research problem.

8 Call to Action

We urge the research community to shift focus from optimising static self-play loops to designing dynamic self-synthetic pipelines that guarantee monotonic learnable information gain. To achieve sustainable self-evolution, future systems must integrate three essential mechanisms: (1) Asymmetric Co-evolution to continuously exploit the computational gap between verifying and solving; (2) Capacity Growth to expand parameter and inference budgets commensurate with rising structural complexity; and (3) Proactive Information Seeking to inject fresh context into the internal environment. We propose evaluating progress not solely by downstream accuracy, but by the system’s capacity to discover and internalise new structure, quantified by bounded observer metrics such as epiplexity.
In Section 3, we provide detailed Practice paragraphs for each component to describe currently feasible directions. However, realising a truly robust and usable self-evolving system still requires overcoming numerous challenges in the coordinated design and implementation of models, data, algorithms, and infrastructure. We call on the community to join efforts to build genuinely sustainable, self-evolving systems.

9 Conclusion

Prevailing stagnation in self-evolving systems stems not from insufficient reward optimisation, but from the failure to sustain a monotonic increase in learnable information for bounded observers. By reframing self-evolution as a dynamic self-synthetic data pipeline rather than a static reinforcement learning game, we clarify that sustainable progress requires a loop with asymmetric co-evolution, dynamic capacity expansion and proactively information seeking. Ultimately, this information-theoretic perspective provides the necessary system-level principles to transform fragile self-play dynamics into robust, continuous self-evolution.

Acknowledgments

This work was supported in part by the UK Engineering and Physical Sciences Research Council through a Turing AI Fellowship (grant no. EP/V020579/1, EP/V020579/2) and the Prosperity Partnership scheme (grant no. UKRI566). Wei is supported by a PhD studentship provided by King’s College London (KCL). The authors acknowledge the use of Computational Research, Engineering and Technology Environment (CREATE) at KCL.

References

E. Allender, M. Koucký, D. Ronneburger, and S. Roy (2011)The Pervasive Reach of Resource-bounded Kolmogorov Complexity in Computational Complexity Theory.
J. Comput. Syst. Sci.77 (1), pp. 14–40.
External Links: Document,
LinkCited by: §2.2.

M. A. Alomrani, Y. Zhang, D. Li, Q. Sun, S. Pal, Z. Zhang, Y. Hu, R. D. Ajwani, A. Valkanas, R. Karimi, P. Cheng, Y. Wang, P. Liao, H. Huang, B. Wang, J. Hao, and M. Coates (2025)Reasoning on a Budget: A Survey of Adaptive and Controllable Test-time Compute in LLMs.
CoRRabs/2507.02076.
External Links: Document,
2507.02076,
LinkCited by: §3.2.

S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, et al. (2025)Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation.
arXiv preprint arXiv:2507.10524.
Cited by: §3.2.

C. H. Bennett (1988)Logical Depth and Physical Complexity.
Cited by: §2.2.

C. Burns, P. Izmailov, J. H. Kirchner, B. Baker, L. Gao, L. Aschenbrenner, Y. Chen, A. Ecoffet, M. Joglekar, J. Leike, I. Sutskever, and J. Wu (2024)Weak-to-strong generalization: eliciting strong capabilities with weak supervision.
In Proceedings of the 41st International Conference on Machine Learning,
ICML’24.
Cited by: §3.1.

L. Chen, M. Prabhudesai, K. Fragkiadaki, H. Liu, and D. Pathak (2025a)Self-questioning Language Models.
CoRRabs/2508.03682.
External Links: Document,
2508.03682,
LinkCited by: §1,
§1,
§6.

Y. Chen, Y. Wang, S. Zhu, H. Yu, T. Feng, M. Zhang, M. Patwary, and J. You (2025b)Multi-agent Evolve: LLM Self-improve through Co-evolution.
CoRRabs/2510.23595.
External Links: Document,
2510.23595,
LinkCited by: §1,
§3.1,
§5.

Z. Chen, Y. Deng, H. Yuan, K. Ji, and Q. Gu (2024)Self-play Fine-tuning Converts Weak Language Models to Strong Language Models.
In Forty-first International Conference on Machine Learning, ICML 2024,
Vienna, Austria, July 21-27, 2024,
External Links: LinkCited by: §1,
§6.

Q. Dong, L. Dong, X. Zhang, Z. Sui, and F. Wei (2025)Self-boosting Large Language Models with Synthetic Preference Data.
In The Thirteenth International Conference on Learning Representations,
ICLR 2025, Singapore, April 24-28, 2025,
External Links: LinkCited by: §1,
§6.

J. Fang, Y. Peng, X. Zhang, Y. Wang, X. Yi, G. Zhang, Y. Xu, B. Wu, S. Liu, Z. Li, Z. Ren, N. Aletras, X. Wang, H. Zhou, and Z. Meng (2025)A Comprehensive Survey of Self-evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems.
CoRRabs/2508.07407.
External Links: Document,
2508.07407,
LinkCited by: §1.

M. Finzi, S. Qiu, Y. Jiang, P. Izmailov, J. Z. Kolter, and A. G. Wilson (2026)From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence.
arXiv preprint arXiv:2601.03220.
Cited by: Appendix B,
Appendix B,
§2.2,
§2.2,
§3.1,
§3.1,
§3.3,
§4,
§4.

H. Gao, J. Geng, W. Hua, M. Hu, X. Juan, H. Liu, S. Liu, J. Qiu, X. Qi, Y. Wu, H. Wang, H. Xiao, Y. Zhou, S. Zhang, J. Zhang, J. Xiang, Y. Fang, Q. Zhao, D. Liu, Q. Ren, C. Qian, Z. Wang, M. Hu, H. Wang, Q. Wu, H. Ji, and M. Wang (2025)A Survey of Self-evolving Agents: On Path to Artificial Super Intelligence.
CoRRabs/2507.21046.
External Links: Document,
2507.21046,
LinkCited by: §1.

L. Gong, D. He, Z. Li, T. Qin, L. Wang, and T. Liu (2019)Efficient Training of BERT by Progressively Stacking.
In Proceedings of the 36th International Conference on Machine Learning,
ICML 2019, 9-15 June 2019, Long Beach, California, USA, K. Chaudhuri and R. Salakhutdinov (Eds.),
Proceedings of Machine Learning Research, Vol. 97, pp. 2337–2346.
External Links: LinkCited by: §3.2.

Ç. Gülçehre, T. L. Paine, S. Srinivasan, K. Konyushkova, L. Weerts, A. Sharma, A. Siddhant, A. Ahern, M. Wang, C. Gu, W. Macherey, A. Doucet, O. Firat, and N. de Freitas (2023)Reinforced Self-training (ReST) for Language Modeling.
CoRRabs/2308.08998.
External Links: Document,
2308.08998,
LinkCited by: §1,
§6.

D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. (2025a)Deepseek-R1: Incentivizing Reasoning Capability in LLMS via Reinforcement Learning.
arXiv preprint arXiv:2501.12948.
Cited by: §3.1.

J. Guo, L. Yang, P. Chen, Q. Xiao, Y. Wang, X. Juan, J. Qiu, K. Shen, and M. Wang (2025b)GenEnv: Difficulty-aligned Co-evolution Between LLM Agents and Environment Simulators.
arXiv preprint arXiv:2512.19682.
Cited by: §1,
§2.1,
§3.3,
§6.

H. Hong, Y. Yan, X. Wu, G. Hou, W. Zhang, W. Lu, Y. Shen, and J. Xiao (2025a)Cooper: Co-optimizing Policy and Reward Models in Reinforcement Learning for Large Language Models.
CoRRabs/2508.05613.
External Links: Document,
2508.05613,
LinkCited by: §1,
§6.

J. Hong, S. Yan, Z. Xiao, J. Cai, X. Jiang, Y. Hu, and H. Ding (2025b)Progressive Scaling Visual Object Tracking.
CoRRabs/2505.19990.
External Links: Document,
2505.19990,
LinkCited by: §3.2.

Y. Hu, S. Liu, Y. Yue, G. Zhang, B. Liu, F. Zhu, J. Lin, H. Guo, S. Dou, Z. Xi, et al. (2025)Memory in the Age of AI Agents.
arXiv preprint arXiv:2512.13564.
Cited by: §3.3.

C. Huang, W. Yu, X. Wang, H. Zhang, Z. Li, R. Li, J. Huang, H. Mi, and D. Yu (2025)R-Zero: Self-evolving Reasoning LLM from Zero Data.
CoRRabs/2508.05004.
External Links: Document,
2508.05004,
LinkCited by: §1,
§1,
§3.1,
§3.2,
§5,
§6.

Q. Huang, Z. An, N. Zhuang, M. Tao, C. Zhang, Y. Jin, K. Xu, L. Chen, S. Huang, and Y. Feng (2024)Harder tasks need more experts: dynamic routing in moe models.
arXiv preprint arXiv:2403.07652.
Cited by: §3.2.

Y. Jiang (2025)Quantifying, understanding, and improving generalization in deep learning.
Ph.D. Thesis, Carnegie Mellon University.
Cited by: §2.2.

Y. Jiang, Y. Xiong, Y. Yuan, C. Xin, W. Xu, Y. Yue, Q. Zhao, and L. Yan (2025)PAG: multi-turn reinforced llm self-correction with policy as generative verifier.
arXiv preprint arXiv:2506.10406.
Cited by: §5.

M. Koppel (1987)Complexity, Depth, and Sophistication.
Complex Syst.1 (6).
External Links: LinkCited by: §2.2.

W. Kwan, J. O. J. Leang, P. Vougiouklis, J. Z. Pan, M. Valentino, and P. Minervini (2025)OpenSIR: open-ended self-improving reasoner.
arXiv preprint arXiv:2511.00602.
Cited by: §3.1,
§5.

B. Liu, C. Jin, S. Kim, W. Yuan, W. Zhao, I. Kulikov, X. Li, S. Sukhbaatar, J. Lanchantin, and J. Weston (2025a)SPICE: Self-play In Corpus Environments Improves Reasoning.
CoRRabs/2510.24684.
External Links: Document,
2510.24684,
LinkCited by: §1,
§2.1,
§3.3,
§3.3,
§6.

W. Liu, S. Qi, X. Wang, C. Qian, Y. Du, and Y. He (2025b)NOVER: Incentive Training for Language Models via Verifier-free Reinforcement Learning.
CoRRabs/2505.16022.
External Links: Document,
2505.16022,
LinkCited by: §3.1.

S. Lu, H. Wang, Z. Chen, and Y. Tang (2025)URPO: A Unified Reward & Policy Optimization Framework for Large Language Models.
CoRRabs/2507.17515.
External Links: Document,
2507.17515,
LinkCited by: §1,
§1,
§6.

Z. Lu, A. Zhou, H. Ren, K. Wang, W. Shi, J. Pan, M. Zhan, and H. Li (2024)MathGenie: Generating Synthetic Data with Question Back-translation for Enhancing Mathematical Reasoning of LLMs.
In Proceedings of the 62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand,
August 11-16, 2024, L. Ku, A. Martins, and V. Srikumar (Eds.),
 pp. 2732–2747.
External Links: Document,
LinkCited by: §3.1.

J. W. McAllister (2003)Effective Complexity as a Measure of Information Content.
Philosophy of Science70 (2), pp. 302–307.
Cited by: §2.2.

K. Nishu, S. Mehta, S. Abnar, M. Farajtabar, M. Horton, M. Najibi, M. Nabi, M. Cho, and D. Naik (2025)From dense to dynamic: token-difficulty driven moefication of pre-trained llms.
arXiv preprint arXiv:2502.12325.
Cited by: §3.2.

X. Qu, Y. Li, Z. Su, W. Sun, J. Yan, D. Liu, G. Cui, D. Liu, S. Liang, J. He, P. Li, W. Wei, J. Shao, C. Lu, Y. Zhang, X. Hua, B. Zhou, and Y. Cheng (2025)A Survey of Efficient Reasoning for Large Reasoning Models: Language, Multimodality, and Beyond.
CoRRabs/2503.21614.
External Links: Document,
2503.21614,
LinkCited by: §3.2.

Y. Qu, T. Zhang, N. Garg, and A. Kumar (2024)Recursive Introspection: Teaching Language Model Agents How to Self-improve.
In Advances in Neural Information Processing Systems 38: Annual Conference
on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver,
BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.),
Cited by: §1,
§6.

J. Rissanen (1978)Modeling by Shortest Data Description.
Autom.14 (5), pp. 465–471.
External Links: Document,
LinkCited by: §2.2.

C. E. Shannon (1948)A Mathematical Theory of Communication.
The Bell system technical journal27 (3), pp. 379–423.
Cited by: §2.2,
§3.1.

R. Shao, S. S. Li, R. Xin, S. Geng, Y. Wang, S. Oh, S. S. Du, N. Lambert, S. Min, R. Krishna, et al. (2025)Spurious rewards: rethinking training signals in rlvr.
arXiv preprint arXiv:2506.10947.
Cited by: §5.

K. Singh, N. Band, and E. Adeli (2025)Curriculum-guided Layer Scaling for Language Model Pretraining.
CoRRabs/2506.11389.
External Links: Document,
2506.11389,
LinkCited by: §3.2.

S. Tu, J. Lin, X. Tian, Q. Zhang, L. Li, Y. Fu, N. Xu, W. He, X. Lan, D. Jiang, and D. Zhao (2025)Enhancing LLM Reasoning with Iterative DPO: A Comprehensive Empirical Investigation.
CoRRabs/2503.12854.
External Links: Document,
2503.12854,
LinkCited by: §1,
§6.

S. Wang, Z. Jiao, Z. Zhang, Y. Peng, X. Ze, B. Yang, W. Wang, H. Wei, and L. Zhang (2025)Socratic-zero : Bootstrapping Reasoning via Data-free Agent Co-evolution.
CoRRabs/2509.24726.
External Links: Document,
2509.24726,
LinkCited by: §1,
§6.

Y. Wei, Z. Wang, J. Liu, Y. Ding, and L. Zhang (2024)Magicoder: Empowering Code Generation with OSS-instruct.
In Forty-first International Conference on Machine Learning, ICML 2024,
Vienna, Austria, July 21-27, 2024,
External Links: LinkCited by: §3.1.

M. Wu, Z. Zhang, Q. Dong, Z. Xi, J. Zhao, S. Jin, X. Fan, Y. Zhou, H. Lv, M. Zhang, et al. (2025a)Reasoning or memorization? unreliable results of reinforcement learning due to data contamination.
arXiv preprint arXiv:2507.10532.
Cited by: §5.

Y. Wu, D. Huang, W. Shi, W. Wang, Y. Pu, L. Gao, S. Liu, Z. Nan, K. Yuan, R. Zhang, X. Zhang, Z. Du, Q. Guo, D. Yin, X. Hu, and Y. Chen (2025b)InverseCoder: Self-improving Instruction-tuned Code LLMs with Inverse-instruct.
In AAAI-25, Sponsored by the Association for the Advancement of Artificial
Intelligence, February 25 - March 4, 2025, Philadelphia, PA, USA, T. Walsh, J. Shah, and Z. Kolter (Eds.),
 pp. 25525–25533.
External Links: Document,
LinkCited by: §3.1.

Q. Xie, M. Luong, E. H. Hovy, and Q. V. Le (2020)Self-training With Noisy Student Improves ImageNet Classification.
In 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition,
CVPR 2020, Seattle, WA, USA, June 13-19, 2020,
 pp. 10684–10695.
External Links: Document,
LinkCited by: §3.2.

R. Xu, H. Liu, S. Nag, Z. Dai, Y. Xie, X. Tang, C. Luo, Y. Li, J. C. Ho, C. Yang, and Q. He (2025)SimRAG: Self-improving Retrieval-augmented Generation for Adapting Large Language Models to Specialized Domains.
In Proceedings of the 2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Linguistics: Human Language
Technologies, NAACL 2025 - Volume 1: Long Papers, Albuquerque, New
Mexico, USA, April 29 - May 4, 2025, L. Chiruzzo, A. Ritter, and L. Wang (Eds.),
 pp. 11534–11550.
External Links: Document,
LinkCited by: §3.3.

L. Yan, R. Li, G. Chen, Q. Li, J. Geng, W. Li, V. Wang, and C. Lee (2026)Spurious rewards paradox: mechanistically understanding how rlvr activates memorization shortcuts in llms.
External Links: 2601.11061,
LinkCited by: §5.

Z. Yang, W. Shen, R. Chen, C. Li, F. Wan, M. Yan, X. Quan, and F. Huang (2025)SPELL: Self-play Reinforcement Learning for evolving Long-context Language Models.
CoRRabs/2509.23863.
External Links: Document,
2509.23863,
LinkCited by: §1,
§1,
§1,
§3.1,
§6.

Z. Yin, Q. Sun, Q. Guo, J. Wu, X. Qiu, and X. Huang (2023)Do large language models know what they don’t know?.
arXiv preprint arXiv:2305.18153.
Cited by: §7.

T. Yu, B. Ji, S. Wang, S. Yao, Z. Wang, G. Cui, L. Yuan, N. Ding, Y. Yao, Z. Liu, M. Sun, and T. Chua (2025)RLPR: Extrapolating RLVR to General Domains without Verifiers.
CoRRabs/2506.18254.
External Links: Document,
2506.18254,
LinkCited by: §3.1.

W. Yuan, R. Y. Pang, K. Cho, X. Li, S. Sukhbaatar, J. Xu, and J. Weston (2024)Self-rewarding Language Mode

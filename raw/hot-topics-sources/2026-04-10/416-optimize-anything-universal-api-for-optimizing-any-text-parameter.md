---
title: optimize_anything: A Universal API for Optimizing any Text Parameter - GEPA
source_url: https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything
final_url: https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/
status: 200
content_type: text/html; charset=utf-8
topics: [DSPy + GEPA optimize_anything]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:24.997712+00:00
---

# optimize_anything: A Universal API for Optimizing any Text Parameter - GEPA

## 원본 URL

https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything

## 추출 본문

optimize_anything: A Universal API for Optimizing any Text Parameter - GEPA

 Skip to content
 

ShowcaseBlogNewDocsTutorialsAPIAbout

 Initializing search
 

 gepa-ai/gepa
 

 GEPA
 

 gepa-ai/gepa
 

 
 
 Showcase
 

 
 

 
 
 About
 

 
 

 
 
 Blog
 

 
 

 
 
 Blog
 

 

 
 
 Archive
 

 
 
 
 
 Archive
 

 

 
 
 2026
 

 
 

 
 
 Guides
 

 
 

 
 
 Guides
 

 

 
 
 Quick Start
 

 
 

 
 
 FAQ
 

 
 

 
 
 Creating Adapters
 

 
 

 
 
 Candidate Selection Strategies
 

 
 

 
 
 Acceptance Criterion
 

 
 

 
 
 Using Callbacks
 

 
 

 
 
 Experiment Tracking
 

 
 

 
 
 Using Claude Code as a Proposer
 

 
 

 
 
 gskill
 

 
 

 
 
 Contributing
 

 
 

 
 
 Tutorials
 

 
 

 
 
 Tutorials
 

 

 
 
 DSPy Full Program Evolution
 

 
 

 
 
 ARC AGI Example
 

 
 

 
 
 3D Unicorn Optimization (Seedless)
 

 
 

 
 
 API Reference
 

 
 

 
 
 API Reference
 

 

 
 
 optimize_anything
 

 
 
 
 
 optimize_anything
 

 

 
 
 optimize_anything
 

 
 

 
 
 GEPAConfig
 

 
 

 
 
 EngineConfig
 

 
 

 
 
 ReflectionConfig
 

 
 

 
 
 MergeConfig
 

 
 

 
 
 RefinerConfig
 

 
 

 
 
 TrackingConfig
 

 
 

 
 
 Evaluator
 

 
 

 
 
 OptimizationState
 

 
 

 
 
 LogContext
 

 
 

 
 
 log
 

 
 

 
 
 get_log_context
 

 
 

 
 
 set_log_context
 

 
 

 
 
 make_litellm_lm
 

 
 

 
 
 Core
 

 
 
 
 
 Core
 

 

 
 
 optimize
 

 
 

 
 
 GEPAAdapter
 

 
 

 
 
 EvaluationBatch
 

 
 

 
 
 GEPAResult
 

 
 

 
 
 GEPACallback
 

 
 

 
 
 DataLoader
 

 
 

 
 
 GEPAState
 

 
 

 
 
 EvaluationCache
 

 
 

 
 
 Callbacks
 

 
 
 
 
 Callbacks
 

 

 
 
 GEPACallback
 

 
 

 
 
 CompositeCallback
 

 
 

 
 
 OptimizationStartEvent
 

 
 

 
 
 OptimizationEndEvent
 

 
 

 
 
 IterationStartEvent
 

 
 

 
 
 IterationEndEvent
 

 
 

 
 
 CandidateSelectedEvent
 

 
 

 
 
 CandidateAcceptedEvent
 

 
 

 
 
 CandidateRejectedEvent
 

 
 

 
 
 EvaluationStartEvent
 

 
 

 
 
 EvaluationEndEvent
 

 
 

 
 
 ValsetEvaluatedEvent
 

 
 

 
 
 ParetoFrontUpdatedEvent
 

 
 

 
 
 MergeAttemptedEvent
 

 
 

 
 
 MergeAcceptedEvent
 

 
 

 
 
 MergeRejectedEvent
 

 
 

 
 
 BudgetUpdatedEvent
 

 
 

 
 
 ErrorEvent
 

 
 

 
 
 StateSavedEvent
 

 
 

 
 
 Stop Conditions
 

 
 
 
 
 Stop Conditions
 

 

 
 
 StopperProtocol
 

 
 

 
 
 MaxMetricCallsStopper
 

 
 

 
 
 TimeoutStopCondition
 

 
 

 
 
 NoImprovementStopper
 

 
 

 
 
 ScoreThresholdStopper
 

 
 

 
 
 FileStopper
 

 
 

 
 
 SignalStopper
 

 
 

 
 
 CompositeStopper
 

 
 

 
 
 Adapters
 

 
 
 
 
 Adapters
 

 

 
 
 DefaultAdapter
 

 
 

 
 
 DSPy Adapter
 

 
 

 
 
 DSPy Full Program Adapter
 

 
 

 
 
 RAG Adapter
 

 
 

 
 
 MCP Adapter
 

 
 

 
 
 TerminalBench Adapter
 

 
 

 
 
 Proposers
 

 
 

 
 
 Proposers
 

 

 
 
 CandidateProposal
 

 
 

 
 
 ProposeNewCandidate
 

 
 

 
 
 ReflectiveMutationProposer
 

 
 

 
 
 MergeProposer
 

 
 

 
 
 Signature
 

 
 

 
 
 LanguageModel
 

 
 

 
 
 Logging
 

 
 
 
 
 Logging
 

 

 
 
 LoggerProtocol
 

 
 

 
 
 StdOutLogger
 

 
 

 
 
 Logger
 

 
 

 
 
 ExperimentTracker
 

 
 

 
 
 create_experiment_tracker
 

 
 

 
 
 Strategies
 

 
 
 
 
 Strategies
 

 

 
 
 BatchSampler
 

 
 

 
 
 EpochShuffledBatchSampler
 

 
 

 
 
 CandidateSelector
 

 
 

 
 
 ParetoCandidateSelector
 

 
 

 
 
 CurrentBestCandidateSelector
 

 
 

 
 
 EpsilonGreedyCandidateSelector
 

 
 

 
 
 ComponentSelector
 

 
 

 
 
 RoundRobinComponentSelector
 

 
 

 
 
 AllComponentSelector
 

 
 

 
 
 EvaluationPolicy
 

 
 

 
 
 FullEvaluationPolicy
 

 
 

 
 
 InstructionProposalSignature
 

 
 

 Table of contents
 

 
 The optimize_anything API
 
 

 
 The Simplest Form
 
 

 
 One Interface, Three Optimization Modes
 
 

 
 Let's Take It for a Spin
 
 

 
 How It Works
 
 

 
 Actionable Side Information (ASI)
 
 

 
 Pareto-Efficient Search
 
 

 
 Results
 
 

 
 1. Optimize Agent Skills: Near-Perfect Claude Code Accuracy, 47% Faster
 
 

 
 2. Discover Cloud Algorithms That Cut Costs up to 40%
 
 

 
 3. Nearly Triple Gemini-Flash's ARC-AGI Accuracy via Agent Architecture Evolution
 
 

 
 4. Improve GPT's Math Accuracy via Prompt Optimization (AIME)
 
 

 
 5. Accelerate PyTorch with Custom CUDA Kernels
 
 

 
 6. Outperform AlphaEvolve's solution at Circle Packing
 
 

 
 7. Match or Outperform Optuna at Blackbox Mathematical Optimization
 
 

 
 8. From Vague Idea to 3D Unicorn — No Seed Required
 
 

 
 Conclusion & Getting Started
 
 

 
 Appendix: Detailed Code Walkthroughs for each Case Study
 
 

 
 Appendix: Make printf() Debugging Cool Again
 
 

optimize_anything: A Universal API for Optimizing any Text Parameter

 February 18, 2026
 Lakshya A Agrawal*, Donghyun Lee*, Wenjie Ma, Karim Elmaaroufi, Shangyin Tan, Sanjit A. Seshia, Koushik Sen, Dan Klein, Ion Stoica, Joseph E. Gonzalez, Omar Khattab, Alexandros G. Dimakis, Matei Zaharia
* Equal Contribution

optimize_anything: A Universal API for Optimizing any Text Parameter¶

Today we are introducing 
optimize_anything
, a declarative API that optimizes any artifact representable as text (e.g., code, prompts, agent architectures, vector graphics, configurations). It extends GEPA (Genetic-Pareto, our state-of-the-art LLM prompt optimizer) far beyond prompts. You declare what to optimize and how to measure it; the system handles the search. Testing it across several domains, we find 
optimize_anything
 consistently matches or outperforms domain-specific tools, including some purpose-built for each task. With one API, you can:

create agent skills achieving near-perfect Claude Code task completion 47% faster,

optimize cloud scheduling policies that cut costs by 40%, beating expert heuristics,

find detailed system prompts to boost GPT's math reasoning accuracy,

discover bespoke agent harnesses that nearly triple Gemini Flash's ARC-AGI accuracy,

write custom solvers to match and exceed Optuna in blackbox mathematical optimization,

and... model a 3D unicorn.

Zero-shot attempt from Claude Opus 4.6

Optimized by optimize_anything

The key insight is that a surprisingly wide range of problems can be formulated as optimizing a text artifact: speeding up a CUDA kernel, tuning a scheduling policy, refining a prompt template, or redesigning an agent architecture. If it can be serialized to a string and its quality measured, an LLM can reason about it and propose improvements.

Where prior LLM-evolution frameworks like AlphaEvolve, OpenEvolve, and ShinkaEvolve expose concepts like island topologies1, prompt samplers2, and cascade evaluation stages3, 
optimize_anything
 strips the interface down to its essence — and goes further by unifying three optimization modes (single-task search, multi-task search, and generalization) under one declarative API. While prior systems operate exclusively in single-task mode, 
optimize_anything
 enables optimization tasks they cannot directly express like discovering agent architectures from scratch, learning prompts that generalize to unseen examples, and optimizing coding agent skills that transfer across models.

Evaluate a text artifact, capture diagnostic feedback (ASI), and let an LLM propose targeted improvements. Code, prompts, configs, agent architectures — if you can measure it, optimize_anything can optimize it.
The optimize_anything API¶

The Simplest Form¶

At its core, the API requires just two things: an artifact (or a description of what you want) and an evaluator.

importgepa.optimize_anythingasoadefevaluate(candidate:str)->float:score,diagnostic=run_my_system(candidate)oa.log(f"Error: {diagnostic}")# captured as ASIreturnscore# Start from an existing artifact…result=oa.optimize_anything(seed_candidate="<your initial artifact>",evaluator=evaluate,)# … or just describe what you need.result=oa.optimize_anything(evaluator=evaluate,objective="Generate a Python function `reverse()` that reverses a string.",)print(result.best_candidate)

That's it. The evaluator takes a candidate string and returns a score (higher is better). 
oa.log()
 works just like 
print()
, but routes output to the LLM proposer as Actionable Side Information (ASI) — diagnostic feedback the proposer reads during reflection. For richer diagnostics, return a structured dictionary alongside the score:

defevaluate(candidate:str)->tuple[float,dict]:result=execute_code(candidate)returnresult.score,{"Error":result.stderr,"Output":result.stdout,"Runtime":f"{result.time_ms:.1f}ms",}

ASI can be open-ended text, structured data, multi-objectives (through 
scores
), or even images (via 
gepa.Image
) for vision-capable LLMs; anything that would help an expert understand the artifact and diagnose failures. We'll see ASI in action in the SVG demo, then unpack why it matters.

One Interface, Three Optimization Modes¶

The three optimization modes supported in optimize_anything: single-task search, multi-task search, and generalization.

optimize_anything
 unifies three distinct optimization paradigms under one API, determined by whether you provide a 
dataset
 and 
valset
:

1. Single-Task Search: "Solve one hard problem." No dataset needed; the candidate is the solution, and the evaluator scores it directly (no 
example
 argument). For example, in circle packing, the artifact is the packing algorithm code and the evaluator returns the score plus geometric diagnostics as ASI. This is the mode that prior LLM-evolution frameworks like AlphaEvolve and OpenEvolve operate in.

oa.optimize_anything(seed_candidate=...,evaluator=...)

2. Multi-Task Search: "Solve a batch of related problems with cross-transfer." You provide a 
dataset
 of related tasks; insights from solving one help solve the others. For example, in CUDA kernel generation, each task is a PyTorch operation to accelerate on the same hardware, and the evaluator compiles and benchmarks the kernel returning compiler errors and profiler traces as ASI. Even though the kernels perform different computations, multi-task mode converges faster and solves more problems across all speedup thresholds than dedicated single-task optimization, thanks to cross-transfer of optimization patterns. No prior LLM-evolution framework supports this mode.

oa.optimize_anything(seed_candidate=...,evaluator=...,dataset=tasks)

3. Generalization: "Build a skill that transfers to unseen problems." You provide both a training 
dataset
 and a held-out 
valset
; the optimized artifact (a prompt, an agent, a policy) must generalize to unseen examples. This is the mode that GEPA's prompt optimization operates in. 
optimize_anything
 generalizes the pattern to any text artifact, not just prompts, abstracting over traditional machine learning and program synthesis. For example, in agent architecture discovery, the artifact is the entire agent, the dataset and valset are ARC-AGI puzzles, and the evaluator runs the agent and returns its errors as ASI. The optimized agent improves from 32.5% to 89.5% on the test set (+57 percentage points). The same mode also powers cloud scheduling policy discovery, where the artifact is an algorithm that must generalize across unseen infrastructure scenarios.

oa.optimize_anything(seed_candidate=...,evaluator=...,dataset=train,valset=val)

The full API signature:

defoptimize_anything(seed_candidate:str|dict[str,str]|None=None,# Starting artifact (or None for seedless)evaluator:Callable,# Score + ASIdataset:list|None=None,# Training examples (modes 2 & 3)valset:list|None=None,# Validation set (mode 3)objective:str|None=None,# What to optimize for (natural language)background:str|None=None,# Domain knowledge and constraintsconfig:GEPAConfig|None=None,# Engine, reflection, tracking settings)->GEPAResult:""" Call with either (seed_candidate+evaluator) or (evaluator+objective) """

Notice what's absent: no mutation prompts, no task-specific instruction templates, no island configurations, no EVOLVE-BLOCK markers (all common in prior LLM-evolution frameworks). You declare the what (your artifact, your evaluator, and any domain knowledge as 
background
) and 
optimize_anything
 handles the how: prompt construction, reflection, candidate selection, and search strategy. This declarative design, inspired by DSPy's principle of programming not prompting, means the same API call works whether you're optimizing a CUDA kernel, a cloud scheduling policy, or an agent architecture.

Let's Take It for a Spin¶

Let's use 
optimize_anything
 to optimize SVG source code depicting "a pelican riding a bicycle" starting from a blank white canvas. The evaluator renders the SVG as a PNG, asks a VLM to score it against visual criteria, and passes the rendered image back as ASI so the proposer can literally see what it's improving. Here's the zero-shot baseline from Claude Opus 4.6 versus the best optimized result after exploring 20 candidates:

Zero-shot attempt from Claude Opus 4.6

Best candidate (score: 0.817)

The optimizer added background elements, improved anatomy, increased the sophistication of all visual elements, and refined the composition — all through LLM reflection on rendered image feedback.

Notably, we optimize the SVG code itself, not a prompt that generates SVG. Here's the code.

First, we define our evaluator and the visual aspects we'd like it to grade for:

Defining the evaluator

fromgepaimportImagefromdemo_utilsimportrender_image,get_vlm_score_feedbackGOAL="a pelican riding a bicycle"VLM="vertex_ai/gemini-3-flash-preview"defevaluate(candidate,example):"""Render SVG → image, score with a VLM, return (score, side_info)."""image=render_image(candidate["svg_code"])# via cairosvgscore,feedback=get_vlm_score_feedback(VLM,image,example["criteria"])# simple regex parserreturnscore,{"RenderedSVG":Image(base64_data=image,media_type="image/png"),"Feedback":feedback,}VISUAL_ASPECTS=[# 6 visual aspects → Pareto-efficient selection{"id":"overall","criteria":f"Rate overall quality of this SVG ({GOAL}). SCORE: X/10"},{"id":"anatomy","criteria":"Rate pelican accuracy: beak, pouch, plumage. SCORE: X/10"},{"id":"bicycle","criteria":"Rate bicycle: wheels, frame, handlebars, pedals. SCORE: X/10"},{"id":"composition","criteria":"Rate how convincingly the pelican rides the bicycle. SCORE: X/10"},{"id":"visual","criteria":"Rate visual appeal, scenery, and color usage. SCORE: X/10"},{"id":"craft","criteria":"Rate SVG technical quality: shapes, layering. SCORE: X/10"},]

Then, we put it all together and run 
optimize_anything
:

Running optimize_anything

fromgepa.optimize_anythingimport(optimize_anything,GEPAConfig,EngineConfig,ReflectionConfig,)result=optimize_anything(seed_candidate={"svg_code":open("seed.svg").read()},# a plain white canvasevaluator=evaluate,dataset=VISUAL_ASPECTS,objective=f"Optimize SVG code to illustrate '{GOAL}'. Output ONLY valid SVG.",config=GEPAConfig(engine=EngineConfig(max_metric_calls=150),reflection=ReflectionConfig(reflection_lm=VLM),),)print(result.best_candidate)

A few things to note:

The 
dataset
 contains 6 evaluation aspects. GEPA calls the evaluator once per aspect per candidate, tracking scores individually. This enables Pareto-efficient selection: a candidate that excels at bicycle structure but struggles with pelican anatomy is preserved on the frontier, not discarded because its overall average score is smaller.

Our desired visual aspects are defined in concise natural language. We avoid the need for detailed rubrics and simply rely on the VLM's judgment for scoring.

reflection_minibatch_size=2
 (the default) means each reflection step shows the LLM feedback from just 2 of the 6 aspects. Over multiple iterations, all aspects get attention, but each reflection is focused and targeted.

The rendered image is passed as ASI via 
Image(base64_data=...)
, giving the VLM proposer visual feedback on its own output. The VLM evaluator never sees the SVG code, only the rendered image. The proposer sees both the feedback and the source SVG, and proposes targeted improvements.

How It Works¶

Classical optimization methods reduce all diagnostic context to a single scalar. They know that a candidate failed, but not why. You can't show a Bayesian optimizer the stack trace that pinpoints the bug. Recent LLM-evolution frameworks changed this by feeding execution results and textual feedback into LLM proposers. However, the "evolutionary" framing these frameworks inherit suggests a blind process — mutate, evaluate, select, repeat. But when an LLM reads a compiler error, diagnoses a logic bug, and proposes a targeted fix, that's not natural selection, it's an engineer iterating on a prototype. 
optimize_anything
 leans into this with two key ingredients: diagnostic feedback as a first-class API concept and Pareto-efficient search.

Actionable Side Information (ASI)¶

optimize_anything
 makes diagnostic feedback a first-class part of the evaluator contract. Prior frameworks expose feedback through framework-specific mechanisms; ASI provides a uniform interface that makes it trivial to surface any diagnostic the evaluator can produce, including modalities no prior framework supports, such as rendered images that let a VLM visually inspect its own output. In the pelican demo, the evaluator passed the rendered SVG back as an image so the proposer could literally see what it was improving. During a dedicated reflection step, the proposer reasons over this signal to diagnose failures and propose targeted fixes.

ASI is the text-optimization analogue of the gradient. Where gradients tell a numerical optimizer which direction to move, ASI tells an LLM proposer why a candidate failed and how to fix it.
Pareto-Efficient Search¶

Even when optimizing a single objective, evaluating candidates across multiple aspects or examples produces richer signal. The naive approach collapses that signal into one average score and always improves the top candidate. This stalls fast: averaging hides which aspects are strong and which are weak, and the proposer tries to improve everything at once instead of focusing.

optimize_anything
 does two things differently. First, it tracks scores per task (expressed in 
dataset
 or 
valset
) or metric (expressed in returned score from evaluator and 
scores
 field in ASI) individually and maintains a Pareto frontier: any candidate that is the best at something survives, even if its average is suboptimal. Second, each reflection step shows the proposer a minibatch of just 2–3 examples or metrics instead of all of them. The proposer makes focused, targeted improvements on that subset, and the Pareto frontier ensures these specialized gains are preserved across iterations rather than averaged away. Over iterations, the frontier accumulates complementary strengths, and the best candidates combine them. The same mechanism powers multi-task search: when optimizing across a batch of related problems, the frontier preserves candidates that excel on different tasks, and strategies discovered for one problem transfer to others — which is why multi-task mode outperforms dedicated single-task optimization on CUDA kernel generation.

Results¶

optimize_anything
 learns repository-specific skills that push coding agents to near-perfect accuracy, discovers novel cloud scheduling algorithms that cut costs by 40%, evolves a 10-line agent stub into a 300+ line system that nearly triples its test accuracy on ARC-AGI, boosts GPT's math reasoning via prompt optimization, generates fast CUDA kernels, beats AlphaEvolve's solution at circle packing, matches Optuna (a mature numerical optimizer) by generating custom solver code from scratch, and models a 3D unicorn from no seed code. We test across eight domains spanning search, batch optimization, and generalization. Each section below walks through the examples and links to full, runnable code.

1. Optimize Agent Skills: Near-Perfect Claude Code Accuracy, 47% Faster¶

Mode: Generalization. Skills (natural-language instructions and best practices for working with a specific codebase) are text artifacts too. 
optimize_anything
 can optimize them: the evaluator runs a coding agent on real tasks from the repository and scores whether it resolves them; the optimized skills must generalize to unseen tasks.

Claude Code on Bleve: optimized skills boost Haiku 4.5 pass rate from 79.3% to 100% and Sonnet 4.5 from 94.8% to 100%, while reducing resolve duration by 47%.
The results are striking: GEPA-optimized skills boost resolve rates from 24% to 93% on one repository and from 55% to 82% on another, and transfer directly to Claude Code, pushing it to near-perfect pass rates while cutting resolution time by 47%.

Key result:
optimize_anything
 learns repository-specific skills that dramatically improve coding agent performance and transfer across models. Read the full post →

2. Discover Cloud Algorithms That Cut Costs up to 40%¶

Mode: Generalization. We optimize cloud infrastructure algorithms: CloudCast discovers broadcast routing strategies for multi-cloud data transfer (minimizing egress cost), and Can't Be Late learns scheduling policies that decide when to use cheap-but-preemptible SPOT instances versus reliable ON_DEMAND instances to complete tasks before deadlines.

CloudCast (40.2% cost savings): Optimizes from baseline Dijkstra routing to a provider-aware Steiner tree algorithm with Pareto-frontier candidate selection.

Can't Be Late (7.8% cost savings): Optimizes from a simple deadline-check heuristic to an adaptive scheduling strategy that tracks spot availability patterns and computes break-even switching costs.

Key result:
optimize_anything
 discovers state-of-the-art algorithms for both problems (40.2% cost savings on CloudCast and 7.8% cost savings on Can't Be Late), topping the ADRS leaderboard (outperforming OpenEvolve, ShinkaEvolve, and expert-designed heuristics). CloudCast code → | Can't Be Late code →

3. Nearly Triple Gemini-Flash's ARC-AGI Accuracy via Agent Architecture Evolution¶

Mode: Generalization. This is the most ambitious application. Rather than optimizing a prompt, we optimize the entire agent system: code, sub-agent architecture, control flow, helper functions, and prompts are all treated as a single text artifact. The seed is a 10-line naive agent; GEPA evolves it into a 300+ line system with rule induction, code verification, iterative refinement, and structured fallbacks. It nearly triples Gemini Flash's ARC-AGI accuracy at just twice the cost per task.

ARC-AGI agent evolution: from a naive agent (32.5% test) to a sophisticated 300+ line system (89.5% test) with Gemini 3 Flash.
The optimized ARC-AGI agent architecture: code generation, iterative validation, and two-attempt prediction (code + direct LLM)
Key result: Using the same underlying model (Gemini 3 Flash), 
optimize_anything
 improves ARC-AGI v1 public test accuracy from 32.5% to 89.5% by evolving the entire agent architecture, achieving gains that typically require significant manual iteration. Full code →

4. Improve GPT's Math Accuracy via Prompt Optimization (AIME)¶

Mode: Generalization. We optimize a system prompt for gpt-4.1-mini by training on AIME 2022–2024 math competition problems and testing on AIME 2025. GEPA sets the state-of-the-art for prompt optimization.

AIME 2025 prompt optimization: gpt-4.1-mini accuracy improves from 46.67% to 60.00% through prompt refinement alone.
Key result: Pure prompt optimization improves gpt-4.1-mini from 46.67% to 60.00% on AIME 2025, a 13.3 percentage point gain from changing only the system prompt. Full code →

5. Accelerate PyTorch with Custom CUDA Kernels¶

Mode: Multi-Task Search. We generate fast CUDA kernels for multiple reference PyTorch operations from KernelBench, evaluated on a V100 32 GB GPU. Under the hood, GEPA evolves the prompt that drives kernel generation, so improvements discovered for one problem transfer to others automatically.

KernelBench results with GEPA (gpt-5 as proposer). 87% of generated kernels match or beat baseline performance; 25% are 20%+ faster.[^kernelbench]
To gauge the effectiveness of cross-task learning, we take the 10 problems where multi-task mode performed best and re-optimize each from scratch in single-task mode to see whether a dedicated single-task run can beat the multi-task result. The graph below shows that a multi-task mode converges faster and solves more problems across all speedup thresholds.

Single-task vs multi-task mode on 10 KernelBench problems. 
Key result: 87% of GEPA-generated kernels match or beat the baseline, with 25% achieving 20%+ speedups. Multi-task mode outperforms dedicated single-task search modes, suggesting the efficiency of cross-task learning. Full code →

6. Outperform AlphaEvolve's solution at Circle Packing¶

Mode: Single-Task Search. Pack n=26 circles to maximize the sum of their radii within a unit square. GEPA optimizes the packing algorithm code, using execution results and geometric diagnostics as ASI.

GEPA outperforms AlphaEvolve, ShinkaEvolve, and OpenEvolve's solutions on circle packing (n=26), reaching a higher score with fewer evaluations.
Visual progression of the circle packing optimization: from an initial naive arrangement to a near-optimal packing.
Key result: GEPA outperforms prior LLM-evolution frameworks (AlphaEvolve/ShinkaEvolve/OpenEvolve), reaching a score of 2.63598+. Full code →

7. Match or Outperform Optuna at Blackbox Mathematical Optimization¶

Mode: Single-Task Search. Given a blackbox objective function, 
optimize_anything
 discovers an optimization algorithm tailored to it and matches Optuna, the industry-standard blackbox optimizer, across the 56-problem EvalSet benchmark.

GEPA's optimize_anything matches Optuna, the industry-standard blackbox optimizer, on the EvalSet benchmark. (a) Across all 56 EvalSet problems (budget of 8,000 evaluations each), GEPA ties Optuna on 40, wins 7, and loses 9. (b) On 10 selected problems where Optuna struggles (budget of 2,000 evaluations each), GEPA finds better solutions on 7 out of 10.
On the 56-problem evalset benchmark with large budgets, GEPA and Optuna tie on most problems. But on the hardest problems with lower budgets where Optuna struggles, an interesting pattern emerges: Optuna's fixed TPE-CMA-ES pipeline fails in predictable, structural ways. On McCourt13, all 10 independent Optuna runs converge to the same local minimum because TPE's independent per-dimension sampling always falls into the dominant trap basin. On Tripod, CMA-ES assumes a smooth, unimodal landscape, but the objective is piecewise-linear with hard discontinuities, so it converges to the wrong basin and cannot escape.

GEPA tailors the solver to each problem by learning from accumulated evaluation history. For boundary optima, it discovers L-BFGS-B, a box-constrained optimizer that naturally sticks to boundaries. For deceptive traps, it designs multi-start search from diverse starting points, escaping basins that trap single-trajectory methods. While Optuna tunes parameters within a fixed algorithm, GEPA learns to optimize the algorithm itself on the fly.

Key result:
optimize_anything
 matches the performance of Optuna, a mature numerical optimizer, by optimizing a blackbox search program tailored to each problem. Full code →

8. From Vague Idea to 3D Unicorn — No Seed Required¶

Mode: Multi-Task Search (seedless). Every example so far starts from a hand-written seed: a blank SVG, a naive agent stub, a baseline algorithm. But what if you don't even know where to begin? You know what you want — a 3D unicorn — and you can articulate what good looks like (anatomical accuracy, mesh quality, visual appeal), but you have no idea how to wire up build123d geometry, STL export, and pyrender camera orbits into a working script.

This is exactly what seedless mode (
seed_candidate=None
) is for. Instead of providing a starting artifact, you describe the objective and the technical context as natural language, and GEPA's reflection LM bootstraps the first candidate itself:

result=optimize_anything(seed_candidate=None,# no starting code — the LM writes the first draftevaluator=evaluate_3d_render,dataset=VISUAL_ASPECTS,# 4 aspects: quality, anatomy, mesh, appealobjective="Optimize a Python program (build123d + pyrender) to generate a 3D unicorn.",background=("The candidate is a complete Python script that produces multi-view PNG renderings. ""Use build123d for CSG geometry, export to STL, render with pyrender. ""Known working imports: numpy, pyrender, trimesh, build123d (Box, Cylinder, Cone, ...)."),)

The evaluator runs each candidate as a subprocess, collects the rendered PNGs, and asks a VLM to score them — passing the images back as ASI so the proposer can see what its code produces. Here's Claude Opus 4.6's zero-shot attempt versus the GEPA-optimized result:

Zero-shot from Claude Opus 4.6

GEPA-optimized (seedless using Claude Opus 4.6)

The zero-shot model produces a recognizable but crude unicorn — blocky torso, piston-like legs, a horn on a box head. GEPA iteratively refines the geometry, improving proportions, adding anatomical detail, and even adds a swirl around the horn, all without any human-written seed code to start from.

The seedless mode is particularly useful for tasks where the solution space is large and unfamiliar such as creative or exploratory tasks. You bring the evaluation criteria (your taste) and the optimizer handles everything else. Full code →

Conclusion & Getting Started¶

optimize_anything
 has a simple premise: if your artifact is text and its performance can be measured, you can optimize it. The API is minimal, requiring only a seed (or task description), an evaluator, and optionally a dataset. The results span algorithmic discovery, kernel generation, systems research, prompt tuning, agent architecture search, blackbox optimization, and coding agent skill learning.

The key ideas: (1) three unified modes (single-task search, multi-task search, and generalization) under one declarative API; (2) Actionable Side Information (ASI) as a first-class API concept that turns blind mutation into targeted, diagnostic-driven engineering; (3) Pareto-efficient search across metrics and examples that outperforms naive all-at-once optimization.

By design, 
optimize_anything
 is a general frontend for text optimization. It is currently powered by GEPA as the optimization backend, but the API is backend-agnostic: as new optimization strategies emerge with increasingly powerful models, they can be plugged in without changing any user code. Our goal is for 
optimize_anything
 to always dispatch to the best available optimizer for your problem. We welcome community contributions of new optimization backends, evaluators, and case studies.

Get started:

pipinstallgepa

importgepa.optimize_anythingasoaresult=oa.optimize_anything(seed_candidate="<your artifact>",evaluator=your_evaluator,)

Documentation

GitHub

Discord

Twitter

Slack

Appendix: Detailed Code Walkthroughs for each Case Study¶

Cloud Broadcast Routing (CloudCast)
Generalization mode for cloud infrastructure optimization. Optimizes a Python program that implements a broadcast routing strategy, evaluated against real-world cloud simulations. GEPA discovers algorithms that generalize across diverse network configurations.

CloudCast — broadcast routing for multi-cloud data transfer.

Artifact being evolved: a Python 
search_algorithm
 function (the full routing algorithm code) that receives a network graph of cloud regions and must return a 
BroadCastTopology
 — a set of routing paths from a source to multiple destinations across AWS, GCP, and Azure. The network is a directed graph where nodes are cloud regions and edges carry 
cost
 ($/GB) and 
throughput
 (Gbps) attributes. GEPA evolves the entire algorithm, including data structures it uses.

Seed Candidate — A baseline Dijkstra shortest-path router. It finds the single cheapest path to each destination and sends all data partitions along the same route:

SEED_PROGRAM="""import networkx as nxfrom typing import Dict, Listclass BroadCastTopology: def __init__(self, src, dsts, num_partitions=4, paths=None): self.src = src self.dsts = dsts self.num_partitions = num_partitions self.paths = paths or {dst: {str(i): None for i in range(num_partitions)} for dst in dsts} def set_num_partitions(self, num_partitions): self.num_partitions = num_partitions def set_dst_partition_paths(self, dst, partition, paths): self.paths[dst][str(partition)] = paths def append_dst_partition_path(self, dst, partition, path): partition = str(partition) if self.paths[dst][partition] is None: self.paths[dst][partition] = [] self.paths[dst][partition].append(path)def search_algorithm(src, dsts, G, num_partitions):\"\"\"Baseline: Dijkstra shortest-cost path, same route for all partitions.\"\"\" h = G.copy() h.remove_edges_from(list(h.in_edges(src)) + list(nx.selfloop_edges(h))) bc_topology = BroadCastTopology(src, dsts, num_partitions) for dst in dsts: path = nx.dijkstra_path(h, src, dst, weight="cost") for i in range(len(path) - 1): s, t = path[i], path[i + 1] for j in range(num_partitions): bc_topology.append_dst_partition_path(dst, j, [s, t, G[s][t]]) return bc_topology"""

Evaluator — The evaluator runs the candidate's 
search_algorithm
 through a broadcast simulator that models real cloud egress costs and bandwidth constraints. 
get_program_path
 caches the candidate to a temp file (keyed by content, so repeated calls are free). 
run_evaluation
 loads it as a Python module, executes it on the network graph, and runs the simulator to compute cost and transfer time.

ASI (Actionable Side Information): The side information includes (1) per-destination route breakdowns with egress cost and transfer time, (2) cost decomposition into egress vs. instance components, and (3) bottleneck destination identification. This tells the LLM proposer where the algorithm is wasting money (e.g., expensive cross-provider hops) and which destinations are slowest, guiding targeted improvements.

fromutils.simulationimport(FAILED_SCORE,get_program_path,syntax_is_valid,syntax_failure_info,run_evaluation,evaluation_failure_info,evaluation_success_info,)defevaluate(candidate:dict,example:dict,**kwargs):program_path=get_program_path(candidate["program"])ifnotsyntax_is_valid(program_path):returnFAILED_SCORE,syntax_failure_info(example)success,cost,transfer_time,error,details=run_evaluation(program_path,example["config_file"],example["num_vms"])ifnotsuccess:returnFAILED_SCORE,evaluation_failure_info(error,example)score=1.0/(1.0+cost)returnscore,evaluation_success_info(score,cost,transfer_time,example,details)

Optimizer — Generalization mode with 5 multi-cloud broadcast configurations as both the training and validation set (intra-AWS, intra-Azure, intra-GCP, and two cross-cloud scenarios). The evolved algorithm must generalize across intra- and inter-provider network topologies.

fromgepa.optimize_anythingimportoptimize_anything,GEPAConfig,EngineConfig,ReflectionConfigfromutils.datasetimportload_config_datasetfromutils.lmimportmake_reflection_lm# 5 multi-cloud broadcast configs: intra_aws, intra_azure, intra_gcp, inter_agz, inter_gaz2dataset=load_config_dataset()result=optimize_anything(seed_candidate={"program":SEED_PROGRAM},evaluator=evaluate,dataset=dataset,valset=dataset,objective="Optimize a broadcast routing algorithm for multi-cloud data transfer. ""Minimize total cost (egress fees + instance costs) while maintaining ""good transfer times.",background="Nodes are cloud regions (e.g. 'aws:us-east-1', 'gcp:europe-west1-a'). ""Edges have 'cost' ($/GB egress) and 'throughput' (Gbps). Data is split ""into num_partitions chunks routable independently. Total cost = egress ""cost + instance runtime cost. Intra-provider links are typically cheaper.",config=GEPAConfig(engine=EngineConfig(max_metric_calls=100),reflection=ReflectionConfig(reflection_lm=make_reflection_lm("gemini-3-pro-preview")),),)

Optimized artifact — The evolved algorithm achieves 40.2% cost savings over the Dijkstra baseline. Starting from a simple single-path router, GEPA discovered a sophisticated provider-aware Steiner tree algorithm with Pareto-frontier candidate selection and greedy partition allocation. Key innovations: (1) provider-penalty weighting to prefer cheap intra-provider links, (2) diverse candidate generation via multiple Steiner tree strategies, (3) Pareto filtering on cost vs. time, and (4) incremental partition assignment that models bandwidth contention.

importnetworkxasnximportrandomimportmathfromtypingimportDict,List,Set,Tuple,AnyfromcollectionsimportdefaultdictclassSingleDstPath(Dict):partition:intedges:List[List]# [[src, dst, edge data]]classBroadCastTopology:def__init__(self,src:str,dsts:List[str],num_partitions:int=4,paths:Dict[str,'SingleDstPath']=None):self.src=srcself.dsts=dstsself.num_partitions=num_partitionsifpathsisnotNone:self.paths=pathselse:self.paths={dst:{str(i):Noneforiinrange(num_partitions)}fordstindsts}defget_paths(self):returnself.pathsdefset_num_partitions(self,num_partitions:int):self.num_partitions=num_partitionsdefset_dst_partition_paths(self,dst:str,partition:int,paths:List[List]):partition=str(partition)ifdstnotinself.paths:self.paths[dst]={}self.paths[dst][partition]=pathsdefsearch_algorithm(src,dsts,G,num_partitions):""" Optimized Broadcast Routing Algorithm v3. Key Optimizations: 1. Provider-Aware Weighting: biases path finding towards intra-provider links to minimize egress. 2. Pareto-Frontier Candidate Selection: Explicitly keeps candidates that offer distinct cost/time tradeoffs, preventing the greedy allocator from getting stuck in local optima. 3. Diverse Steiner Strategies: Includes MST-like approximations for cost and bottleneck-widest paths for throughput. 4. Robust Greedy Allocation: Accurately models bandwidth contention across partitions. """# --- Constants & Configuration ---EST_DATA_VOL_GB=300.0EST_INSTANCE_COST_PER_HR=10.0PARTITION_VOL_GB=EST_DATA_VOL_GB/max(1,num_partitions)HOURLY_RATE_PER_SEC=EST_INSTANCE_COST_PER_HR/3600.0# Sweep parameters for Cost ($) vs Time (1/BW) tradeoff# Low alpha = Cost optimized. High alpha = Time optimized.# Alphas tuned around the expected exchange rate of $/Gbps (~0.002 to 0.1)alphas=[0.0,1e-5,0.001,0.01,0.05,0.1,0.5,2.0,10.0]# Prune edges below these bandwidths (Gbps) to avoid slow paths# 0.0 includes all, higher values force backbone usagebw_thresholds=[0.0,0.5,5.0,20.0]strategies=['prim','prim','furthest','random']# bias towards prim (usually better cost)# --- Helper: Provider Extraction ---defget_provider(node_name):if':'innode_name:returnnode_name.split(':')[0]return'unknown'src_provider=get_provider(src)# --- Pre-process Graph ---clean_G=G.copy()# Remove incoming edges to source to enforce DAG flow from roottry:clean_G.remove_edges_from(list(clean_G.in_edges(src))+list(nx.selfloop_edges(clean_G)))except:pass# Normalize weights & Cache bandwidths# We create a 'base_weight' that includes a penalty for crossing providersedge_bws={}foru,v,datainclean_G.edges(data=True):if'cost'notindata:data['cost']=0.0if'throughput'notindata:data['throughput']=1.0# Ensure strictly positive BWifdata['throughput']<=1e-6:data['throughput']=1e-6edge_bws[(u,v)]=data['throughput']# Provider penalty logic for candidate generation weightsu_prov=get_provider(u)v_prov=get_provider(v)# Base penalty: small epsilon to prefer fewer hopspenalty=1.0ifu_prov!=v_prov:# Inter-provider is usually expensive, so we bias against it in search# (Note: real cost is in data['cost'], this is just heuristic guidance)penalty=1.5data['penalty_factor']=penaltycandidates=[]seen_topologies=set()# --- Helper: Build Steiner Tree ---defbuild_steiner_tree(strategy,alpha,graph_base,targets,edge_penalty_map=None):H=graph_base.copy()# Initialize heuristic weights# W = (Cost + Alpha/BW) * Penaltyforu,v,dinH.edges(data=True):d['paid']=False# Core tradeoffbase_w=d['cost']+(alpha/d['throughput'])# Hops & Provider biasbase_w=max(1e-6,base_w)*d['penalty_factor']ifedge_penalty_mapand(u,v)inedge_penalty_map:base_w*=edge_penalty_map[(u,v)]d['weight']=base_wtree_paths={}# node -> list of nodesremaining_dsts=set(targets)# Iteratively connect closest/furthest nodes to the growing treewhileremaining_dsts:try:# Dijkstra from Source on current H# Note: H edges that are 'paid' have reduced weight, effectively# finding path from the existing tree structure.dists,paths=nx.single_source_dijkstra(H,src,weight='weight')exceptnx.NetworkXNoPath:break# Filter reachable remaining targetsreachable=[dfordinremaining_dstsifdindists]ifnotreachable:break# Select target based on strategyifstrategy=='prim':# Closest first (min cost expansion)reachable.sort(key=lambdax:dists[x])target=reachable[0]elifstrategy=='furthest':# Furthest first (reduce diameter/bottlenecks)reachable.sort(key=lambdax:dists[x],reverse=True)target=reachable[0]else:target=random.choice(reachable)# Extract pathpath_nodes=paths[target]# Commit path to tree# For every node in this path, if it's a target, record its pathfori,nodeinenumerate(path_nodes):ifnodeinremaining_dsts:tree_paths[node]=path_nodes[:i+1]remaining_dsts.remove(node)# 'Pay' for the edges: reduce weight for subsequent iterations# This encourages edge sharing (multicast tree)foriinrange(len(path_nodes)-1):u,v=path_nodes[i],path_nodes[i+1]ifnotH[u][v]['paid']:H[u][v]['paid']=True# Set to very small positive weight to prefer reuse# We keep a tiny BW component to prefer wider pipes even when 'free'H[u][v]['weight']=1e-6+(alpha/H[u][v]['throughput'])*0.001returntree_paths# --- Phase 1: Candidate Generation ---# A. Shortest Path Trees (Baselines)foralphainalphas:H=clean_G.copy()foru,v,dinH.edges(data=True):d['weight']=d['cost']+(alpha/d['throughput'])try:dists,paths=nx.single_source_dijkstra(H,src,weight='weight')spt_paths={t:paths[t]fortindstsiftinpaths}iflen(spt_paths)==len(dsts):candidates.append({'type':'spt','paths':spt_paths,'alpha':alpha})except:pass# B. Diverse Steiner Treesformin_bwinbw_thresholds:# Create sub-graph meeting BW requirementsH_base=clean_G.copy()ifmin_bw>0:remove_edges=[(u,v)foru,v,dinH_base.edges(data=True)ifd['throughput']<min_bw]H_base.remove_edges_from(remove_edges)# Connectivity checkifH_base.out_degree(src)==0andlen(dsts)>0:continueforalphainalphas:penalty_map=defaultdict(lambda:1.0)# Generate variations# 1st: Standard strategy choice# 2nd/3rd: Penalize used edges to find disjoint/diverse pathsfor_inrange(3):strat=random.choice(strategies)tree_paths=build_steiner_tree(strat,alpha,H_base,dsts,penalty_map)iflen(tree_paths)==len(dsts):candidates.append({'type':'steiner','paths':tree_paths,'alpha':alpha,'min_bw':min_bw})# Update penalty map for diversityused_edges=set()forpintree_paths.values():forkinrange(len(p)-1):used_edges.add((p[k],p[k+1]))foreinused_edges:penalty_map[e]*=1.2# Increment penaltyelse:break# --- Phase 2: Candidate Scoring & Filtering ---# We map candidates to (Cost, Time) points and filter the Pareto frontierunique_candidates=[]forcandincandidates:tree_paths=cand['paths']# Flatten to edgestree_edges=set()fornodesintree_paths.values():foriinrange(len(nodes)-1):tree_edges.add((nodes[i],nodes[i+1]))topo_sig=frozenset(tree_edges)iftopo_siginseen_topologies:continueseen_topologies.add(topo_sig)# Calculate metrics for the specific candidate# Unit Egress: Cost to send 1GB to all Dsts via this treeunit_egress=sum(clean_G[u][v]['cost']foru,vintree_edges)# Bottleneck: Slowest link in the treemin_bw=min((clean_G[u][v]['throughput']foru,vintree_edges),default=1e-9)# Est Time for full volume (heuristic for sorting)est_time=(EST_DATA_VOL_GB*8.0)/min_bw# Total cost for full volumetotal_cost=(unit_egress*EST_DATA_VOL_GB)+(est_time*HOURLY_RATE_PER_SEC)unique_candidates.append({'id':len(unique_candidates),'unit_egress':unit_egress,'min_bw':min_bw,'est_time':est_time,'score':total_cost,'edges':list(tree_edges),'paths':tree_paths})ifnotunique_candidates:# Fallback: simple direct paths if everything failedreturnBroadCastTopology(src,dsts,num_partitions)# Pareto Filtering: Keep candidate C if no other candidate is strictly better in both Cost and Time# Optimization: To reduce O(N^2), sort by cost firstunique_candidates.sort(key=lambdax:x['unit_egress'])pareto_candidates=[]current_best_time=float('inf')forcandinunique_candidates:# Since we iterate from lowest cost, if this cand has lower time than any seen so far,# it lies on the frontier.# We accept equal time if cost is strictly lower (guaranteed by sort order/loop)ifcand['est_time']<current_best_time:pareto_candidates.append(cand)current_best_time=cand['est_time']# Also keep top raw score candidates (mix) just in case Pareto misses a balanced middle groundunique_candidates.sort(key=lambdax:x['score'])best_score_candidates=unique_candidates[:15]# Combine and deduplicatefinal_pool={c['id']:cforcinpareto_candidates+best_score_candidates}.values()final_pool=list(final_pool)# --- Phase 3: Greedy Partition Allocation ---partition_assignments=[]current_edge_load=defaultdict(float)# (u,v) -> GB volumecurrent_total_egress=0.0# Total egress dollars# Cache global max time to avoid recomputing from scratch every inner loop# But since max depends on specific edge bottlenecks, we compute incrementally.forpart_idxinrange(num_partitions):best_cand=Nonebest_objective=float('inf')# Pre-calculate base max time from existing assignmentsbase_max_time=0.0ifcurrent_edge_load:for(u,v),loadincurrent_edge_load.items():t=(load*8.0)/edge_bws.get((u,v),1e-9)ift>base_max_time:base_max_time=tforcandinfinal_pool:# 1. Marginal Cost Calculation# We pay egress for the tree edges.# Egress = Sum(Edge Cost * Edge Vol).# If we add this candidate, we add PARTITION_VOL_GB to all its edges.# Since edges are independent in cost summation, marginal cost is exactly:added_egress=cand['unit_egress']*PARTITION_VOL_GBproj_egress=current_total_egress+added_egress# 2. Projected Time Calculation# Calculate the new max time if we add load to this candidate's edgescand_local_max_time=0.0foru,vincand['edges']:current_load=current_edge_load.get((u,v),0.0)new_load=current_load+PARTITION_VOL_GBt=(new_load*8.0)/edge_bws.get((u,v),1e-9)ift>cand_local_max_time:cand_local_max_time=t# Global max time is max of (unchanged edges, changed edges)proj_max_time=max(base_max_time,cand_local_max_time)# 3. Total Objectiveproj_instance_cost=proj_max_time*HOURLY_RATE_PER_SECproj_total_cost=proj_egress+proj_instance_costifproj_total_cost<best_objective:best_objective=proj_total_costbest_cand=cand# Commit assignmentifbest_cand:partition_assignments.append(best_cand)current_total_egress+=best_cand['unit_egress']*PARTITION_VOL_GBforu,vinbest_cand['edges']:current_edge_load[(u,v)]+=PARTITION_VOL_GBelse:# Should not happen given fallbacks, but safety measureiffinal_pool:partition_assignments.append(final_pool[0])# --- Phase 4: Construct Output ---bc_topology=BroadCastTopology(src,dsts,num_partitions)forpart_id,candinenumerate(partition_assignments):fordstindsts:ifdstincand['paths']:nodes=cand['paths'][dst]path_edges=[]forkinrange(len(nodes)-1):u,v=nodes[k],nodes[k+1]ifG.has_edge(u,v):d=G[u][v]else:d={'cost':0.0,'throughput':1.0}path_edges.append([u,v,d])bc_topology.set_dst_partition_paths(dst,part_id,path_edges)returnbc_topology

Cloud Spot Scheduling (Can't Be Late)
Generalization mode for cloud infrastructure optimization. Optimizes a Python program that implements a scheduling strategy, evaluated against real-world spot-availability traces. GEPA discovers scheduling policies that generalize across diverse job configurations and spot-availability patterns.

Can't Be Late — cloud scheduling with SPOT vs ON_DEMAND instances.

Artifact being evolved: a Python scheduling policy (the 
_step
 method of a 
Strategy
 class) that is called at each time step and must return one of three actions: 
ClusterType.SPOT
 (~0.30/hr, cheap but preemptible), 
ClusterType.ON_DEMAND
 (~1.00/hr, reliable), or 
ClusterType.NONE
 (wait, no cost). The policy has access to remaining task time, deadline, restart overhead, and spot availability. GEPA evolves the entire strategy class, including any state variables it tracks.

Seed Candidate — A simple greedy heuristic: use ON_DEMAND only when the deadline is imminent, otherwise prefer SPOT when available, and wait when it's not:

SEED_PROGRAM="""import mathfrom sky_spot.strategies.strategy import Strategyfrom sky_spot.utils import ClusterTypeclass EvolveSingleRegionStrategy(Strategy): NAME = 'evolve_single_region' def __init__(self, args): super().__init__(args) def reset(self, env, task): super().reset(env, task) def _step(self, last_cluster_type: ClusterType, has_spot: bool) -> ClusterType: env = self.env # Task completion check remaining_task_time = self.task_duration - sum(self.task_done_time) if remaining_task_time <= 1e-3: return ClusterType.NONE # Calculate remaining time until deadline remaining_time = self.deadline - env.elapsed_seconds # If running out of time, use ON_DEMAND to guarantee completion if remaining_task_time + self.restart_overhead >= remaining_time: return ClusterType.ON_DEMAND # Greedy: use SPOT if available, otherwise wait if has_spot: return ClusterType.SPOT else: return ClusterType.NONE @classmethod def _from_args(cls, parser): args, _ = parser.parse_known_args() return cls(args)"""

Evaluator — The evaluator runs the candidate strategy through a scheduling simulator driven by real spot-availability traces. 
get_program_path
 caches the candidate to a temp file (keyed by content, so repeated calls are free). 
run_simulation
 handles subprocess execution of the simulator and cost extraction. Each trace is tested across multiple job configurations (varying task duration, deadline tightness, and restart overhead).

ASI (Actionable Side Information): The side information includes (1) the full spot-availability pattern for the trace (e.g., 
"0.0-10.0:S | 10.0-15.0:X"
 — spot available for 10h then unavailable), (2) a timeline of the strategy's instance usage decisions (e.g., 
"0.0-5.0:S@R0[50%] | 5.0-8.0:OD@R0[100%]"
), and (3) segment counts (SPOT vs ON_DEMAND vs restarts). This lets the LLM proposer see exactly when the strategy made suboptimal decisions — for instance, switching to expensive ON_DEMAND too early when spot was about to become available again.

fromutils.simulationimport(FAILED_SCORE,get_program_path,syntax_is_valid,syntax_failure_info,run_simulation,simulation_failure_info,simulation_success_info,)defevaluate(candidate:dict,example:dict,**kwargs):program_path=get_program_path(candidate["program"])ifnotsyntax_is_valid(program_path):returnFAILED_SCORE,syntax_failure_info(example)success,cost,error,details=run_simulation(program_path,example["trace_file"],example["config"])ifnotsuccess:returnFAILED_SCORE,simulation_failure_info(error,example)score=-costreturnscore,simulation_success_info(score,example,details)

Optimizer — Generalization mode with spot-availability traces split into training and validation sets. Each trace is evaluated across multiple deadline/overhead configurations, so the evolved strategy must handle both tight and relaxed deadlines. 
parallel=True
 with 128 workers enables fast evaluation across the large trace dataset.

fromgepa.optimize_anythingimportoptimize_anything,GEPAConfig,EngineConfig,ReflectionConfigfromutils.datasetimportload_trace_datasetfromutils.lmimportmake_reflection_lm# Load spot-availability traces split into train/val/testsplits=load_trace_dataset()train_set,val_set=splits["train"],splits["val"]result=optimize_anything(seed_candidate={"program":SEED_PROGRAM},evaluator=evaluate,dataset=train_set,valset=val_set,objective="Optimize a cloud scheduling strategy for the 'Can't Be Late' problem. ""Minimize cost while ensuring task completion before deadline.",background="ClusterType.SPOT: ~$0.3/hr, cheap but preemptible at any time. ""ClusterType.ON_DEMAND: ~$1/hr, guaranteed availability. ""ClusterType.NONE: wait with no cost or progress. restart_overhead: ""time penalty when switching instance types. The strategy MUST ""ensure deadline completion (hard constraint).",config=GEPAConfig(engine=EngineConfig(max_metric_calls=100,parallel=True,max_workers=128),reflection=ReflectionConfig(reflection_lm=make_reflection_lm("anthropic/claude-opus-4-5-20251101")),),)

Optimized artifact — The evolved strategy achieves 7.8% cost savings over the baseline. GEPA transformed the simple greedy heuristic into an adaptive strategy with: (1) state tracking for spot unavailability patterns, (2) overhead-aware switching decisions with break-even cost analysis, (3) graduated decision thresholds based on slack ratio (remaining buffer / task time), and (4) multi-factor logic that considers absolute slack, persistent unavailability, and remaining work size.

importmathfromsky_spot.strategies.strategyimportStrategyfromsky_spot.utilsimportClusterTypeclassEvolveSingleRegionStrategy(Strategy):NAME='evolve_single_region'def__init__(self,args):super().__init__(args)self.spot_unavailable_count=0self.consecutive_short_spot_windows=0defreset(self,env,task):super().reset(env,task)self.spot_unavailable_count=0self.consecutive_short_spot_windows=0def_step(self,last_cluster_type:ClusterType,has_spot:bool)->ClusterType:env=self.env# Task completion checkremaining_task_time=self.task_duration-sum(self.task_done_time)ifremaining_task_time<=1e-3:returnClusterType.NONE# Calculate remaining time until deadlineremaining_time=self.deadline-env.elapsed_seconds# Calculate the overhead we might incur for switchingswitch_to_od_overhead=self.restart_overheadiflast_cluster_type==ClusterType.SPOTelse0switch_to_spot_overhead=self.restart_overheadiflast_cluster_type==ClusterType.ON_DEMANDelse0start_overhead=self.restart_overheadiflast_cluster_type==ClusterType.NONEelse0# Cost ratesspot_cost_rate=0.3on_demand_cost_rate=1.0# Critical deadline check: if we absolutely need ON_DEMAND to finish on timeeffective_remaining_for_od=remaining_task_time+switch_to_od_overheadifeffective_remaining_for_od>=remaining_time-0.5:# Small safety marginreturnClusterType.ON_DEMAND# Calculate slack time (buffer we have beyond minimum required time)min_time_needed=remaining_task_time+self.restart_overheadslack=remaining_time-min_time_needed# Track spot availability patternsifnothas_spot:self.spot_unavailable_count+=1else:self.spot_unavailable_count=0ifhas_spot:# Spot is available - but should we use it?# If we're on ON_DEMAND and have tight deadline, consider staying to avoid restartiflast_cluster_type==ClusterType.ON_DEMAND:# Calculate cost of switching to spot vs staying on OD# Switching cost: overhead time at OD rate + potential future restartswitch_cost=switch_to_spot_overhead*on_demand_cost_rate+self.restart_overhead*on_demand_cost_rate# Benefit of spot: savings per hoursavings_per_hour=on_demand_cost_rate-spot_cost_rate# Need to run on spot long enough to recoup switch costbreak_even_hours=switch_cost/savings_per_hourifsavings_per_hour>0elsefloat('inf')# If remaining work is less than break-even, stay on ODifremaining_task_time<break_even_hours*1.5:returnClusterType.ON_DEMAND# If slack is very tight, stay on OD to be safeifslack<self.restart_overhead*3:returnClusterType.ON_DEMAND# Use SPOT - it's available and either we're not on OD or switch is worthwhileself.consecutive_short_spot_windows=0returnClusterType.SPOTelse:# Spot not available - decide whether to wait or use ON_DEMAND# If we're already on ON_DEMAND, definitely stay to avoid wasting restartiflast_cluster_type==ClusterType.ON_DEMAND:returnClusterType.ON_DEMAND# If we were on SPOT and it just became unavailable, we're now idle# Decision: wait for spot or switch to ON_DEMAND?# Calculate adaptive threshold based on multiple factorsslack_ratio=slack/max(remaining_task_time,1e-6)# Factor 1: Absolute slack threshold# Need enough slack to handle potential wait + restart overheadmin_safe_slack=max(2.0,self.restart_overhead*4)# Factor 2: Consider how much work is left# For small remaining tasks, ON_DEMAND cost isn't that high in absolute termsod_cost_to_finish=remaining_task_time*on_demand_cost_rate# Factor 3: Track persistent spot unavailability# If spot has been unavailable for a while, less likely to come back soonpersistent_unavailable=self.spot_unavailable_count>10# Decision logic:# Very tight deadline - must use ON_DEMANDifslack<min_safe_slackorslack_ratio<0.1:returnClusterType.ON_DEMAND# Moderately tight deadline with persistent unavailabilityifslack_ratio<0.25andpersistent_unavailable:returnClusterType.ON_DEMAND# Small remaining task where absolute cost difference is minimal# But only if we have moderate slack pressureifremaining_task_time<3.0andslack_ratio<0.3:returnClusterType.ON_DEMAND# Tight deadline cases (less than 20% buffer)ifslack_ratio<0.2:# If we've been waiting and spot keeps not showing up, switchifself.spot_unavailable_count>5:returnClusterType.ON_DEMAND# Medium slack - be more patient but not infinitelyifslack_ratio<0.4:# After significant waiting, consider switchingifself.spot_unavailable_count>20:returnClusterType.ON_DEMAND# Good slack available - wait for spot to save costsreturnClusterType.NONE@classmethoddef_from_args(cls,parser):args,_=parser.parse_known_args()returncls(args)

Agent Architecture Discovery (ARC-AGI)
Here, we tackle ARC-AGI1. This is a Generalization mode where the entire agent architecture is the artifact being optimized. The seed is a 10-line naive agent that makes a single LLM call; GEPA evolves it into a 170+ line multi-stage system with rule induction, code verification, iterative refinement, and structured fallbacks. Test accuracy improves from 32.5% to 89.5% on a public v1 test set.

Candidate — The seed candidate is a minimal 10-line agent that concatenates training examples into a single prompt and asks the LLM to predict outputs directly. It provides a starting template showing the 
solve()
 API.

SEED_AGENT='''import json, redef solve(train_inputs, train_outputs, test_inputs, llm): examples = "\\n".join(f"Input: {i}\\nOutput: {o}" for i, o in zip(train_inputs, train_outputs)) response = llm(f"Solve an ARC AGI puzzle. Training:\\n{examples}\\n" f"Predict outputs as JSON [[...]]:") grids = [json.loads(g) for g in re.findall(r"\\[\\[.*?\\]\\]", response.replace("\\n", ""))] return {"train": grids[:len(train_inputs)], "test": [[g] for g in grids[len(train_inputs):]]}'''

Evaluator — The evaluator sandboxes the agent code, runs it on an ARC-AGI puzzle (providing training input/output pairs and test inputs), and returns rich ASI: training and test scores, execution errors, the actual grid examples, LLM costs, number of calls made, and all model outputs produced inside the agentic architecture. This lets the proposer see not just what the agent got wrong, but how it reasoned internally.

defevaluate(candidate,example):result=run_agent(agent_code=candidate,train_in=example.train_in,train_out=example.train_out,test_in=example.test_in,test_out=example.test_outorNone,model_id=LLM_MODEL,max_llm_calls=MAX_LLM_CALLS,)llms=result["llms"]score=result["test_score"]returnscore,{"score":score,"problem_id":example.problem_id,"agent_code":candidate,"training_score":result["training_score"],"test_score":result["test_score"],"cost":llm.total_cost,"error":result["error"],"train_examples":result["train_examples"],"test_examples":result["test_examples"],**llms.get_traces(),# number of calls made, LLM costs, model outputs, etc.}

Optimizer — This is Generalization mode with 
dataset
 for training and 
valset
 for validation. The agent must generalize to unseen 
testset
 puzzles, so just memorizing patterns from the training set won't help. 
parallel=True
 with 
max_workers=64
 enables massive concurrent evaluation across puzzles. 
background
 provides domain knowledge about ARC puzzle structure. Gemini 3 Flash is used as both the reflection model and the agent's internal LLM. Note that using a stronger reflection model can find a even more effective artifact in general. 

fromgepa.optimize_anythingimportoptimize_anything,GEPAConfig,EngineConfig,ReflectionConfigfromexamples.arc_agi.utilsimp

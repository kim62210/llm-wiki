---
title: Olmo 3: Charting a path through the model flow to lead open-source AI   | Ai2
source_url: https://allenai.org/blog/olmo3
final_url: https://allenai.org/blog/olmo3
status: 200
content_type: text/html; charset=utf-8
topics: [Open Post-Training Recipes (Tülu 3 / OLMo 3)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:07.030557+00:00
---

# Olmo 3: Charting a path through the model flow to lead open-source AI   | Ai2

## 원본 URL

https://allenai.org/blog/olmo3

## 추출 본문

Olmo 3: Charting a path through the model flow to lead open-source AI | Ai2

 Skip to main content ->

Ai2
Open models

Open models

Olmo

Tülu 3

Molmo

Playground

Language models

Multimodal models

Evaluation frameworks

Open data

Applications

AI for science

Asta

AstaBench

Research with Asta

Asta leaderboards

Semantic Scholar

All projects

AI for the planet

OlmoEarth

EarthRanger

Skylight

Climate Modeling

All projects

AI for robotics

Embodied AI

Research

Research

Latest

Papers

Research principles

News

Institute

Institute

About

Careers

Media center

Navigation Menu

Olmo 3: Charting a path through the model flow to lead open-source AI 

November 20, 2025

Ai2

Share

ModelsTech ReportCodeAPIDemo

Update 12/12: Announcing Olmo 3.1

Since the initial release of the Olmo 3 model flow, the team has been busy improving the reasoning and instruction-following capabilities of our models. The result is two new 32B checkpoints, our most performant to date:

Olmo 3.1 Think 32B, the result of extending our best reinforcement learning (RL) run with a much longer training schedule. 

Olmo 3.1 Instruct 32B, which applies the recipe behind Olmo 3 Instruct 7B to a much larger model—filling a gap our users have been asking for.

After the original Olmo 3 launch, we resumed our RL training run for Olmo 3 32B Think, training for an additional 21 days on 224 GPUs with extra epochs over our Dolci-Think-RL dataset. This yielded Olmo 3.1 32B Think, which brings substantial gains across math, reasoning, and instruction-following benchmarks: improvements of 5+ points on AIME, 4+ points on ZebraLogic, 4+ points on IFEval, and 20+ points on IFBench, alongside stronger performance on coding and complex multi-step tasks.

As for Olmo 3.1 32B Instruct, it’s a larger-scale instruction-tuned model built for chat, tool use, and multi-turn dialogue. Olmo 3.1 32B Instruct is our most capable fully open chat model to date and – in our evaluations – the strongest fully open 32B-scale instruct model.

Alongside the 32B models, we refreshed variants of RL-Zero checkpoints, resulting in Olmo 3.1 RL Zero 7B Code and Olmo 3.1 RL Zero 7B Math. These new checkpoints are the result of longer and more stable training runs, delivering stronger baselines for RL researchers and advancing best practices for RL training.

Together, Olmo 3.1 Think 32B and Olmo 3.1 Instruct 32B show that openness and performance can advance together. By extending the same model flow, we continue to improve capabilities while retaining end-to-end transparency over data, code, and training decisions. You can try the new checkpoints in the Ai2 Playground or download them from Hugging Face, or use them via API courtesy of our inference partners.

Original post follows. 

Language models are often treated as snapshots—brief captures of a long and carefully curated development process. But sharing only the end result obscures the rich context needed to modify, adapt, and extend a model's capabilities. Many meaningful adjustments require integrating domain-specific knowledge deep within the development pipeline, not merely at the final stage. To truly advance open AI development and research, the entire model flow – not just its endpoint – should be accessible and customizable. The model flow is the full lifecycle of an LM: every stage, checkpoint, dataset, and dependency required to create and modify it. By exposing this complete process, the goal is to engender greater trust and enable more effective adaptation, collaboration, and innovation.

With today's release of Olmo 3, we're empowering the open source community with not only state-of-the-art open models, but the entire model flow and full traceability back to training data.

At its center is Olmo 3-Think (32B), the best fully open 32B-scale thinking model that for the first time lets you inspect intermediate reasoning traces and trace those behaviors back to the data and training decisions that produced them. Olmo 3 is a family of compact, dense models at 7 billion and 32 billion parameters that can run on everything from laptops to research clusters.

Olmo 3-Base (7B, 32B) is our most powerful base model yet. When evaluated on our expanded, diverse evaluation suite, Olmo 3-Base delivers the strongest performance among fully open base models – where training data, code, and weights are all publicly available, like Stanford's Marin and Swiss AI's Apertus – and achieves competitive performance with some of the best open-weights base models of comparable size and architecture, including Qwen 2.5 and Gemma 3. Achieving strong results in programming, reading comprehension, and math problem solving, Olmo 3-Base maintains performance at extended context lengths (~up to 65K tokens)—providing a versatile foundation for continued pretraining, targeted fine-tuning, and reinforcement learning and making it easy to build in specialized capabilities like reasoning, tool use (function calling), and instruction following through post-training.

Olmo 3-Think (7B, 32B) is our flagship post-trained reasoning set built on Olmo 3-Base. At a time when few organizations are releasing truly open models at this scale, Olmo 3-Think (32B) serves as a workhorse for RL research, long-horizon reasoning, and other advanced experiments that require substantial compute. On our suite of reasoning benchmarks (discussed below), it's the strongest fully open thinking model we're aware of, narrowing the gap to the best open-weight models of similar scale – such as Qwen 3 32B – while training on roughly 6x fewer tokens. Olmo 3-Think (7B) brings the same design and training approach to an even more efficient form factor, surfacing intermediate thinking steps for complex prompts while making open, inspectable reasoning accessible on more modest hardware.

Olmo 3-Instruct (7B) is a chat and quick-response focused post-train of Olmo 3-Base that handles multi-turn, instruction-following, tool use, and more. In our evaluations, it matches or outperforms open-weight models including Qwen 2.5, Gemma 3, and Llama 3.1, and narrows the gap with Qwen 3 model families at a similar scale—delivering a strong, fully open alternative for high-quality conversational and tool-using agents.

Olmo 3-RL Zero (7B), is a fully open reinforcement learning pathway built on Olmo 3-Base, designed to bootstrap complex reasoning behaviors and enable clear benchmarking of RL algorithms. We release four series of checkpoints from domain-focused training on math, code, instruction following, and general chat, enabling careful study of reinforcement learning with verifiable rewards (RLVR).

Instead of a single set of frozen weights, Olmo 3 offers multiple, fully documented paths through development: the Instruct path for everyday chat and tool use, the RL Zero path for RL experimentation from base models, and the Think/reasoning path for models that leverage inference-time scaling to unlock complex reasoning and agentic behaviors. Each path is a concrete example of how to shape behavior from the same base model, and you’re free to fork or remix them—start with Olmo 3-Base, explore your own supervised fine-tuning (SFT) or direct preference optimization (DPO) recipe for instruct-style use cases, or plug in a new RL objective to probe different tradeoffs. The flow itself becomes a rich, reusable object—not just a record of how we built Olmo 3, but a scaffold for how you can build your own systems.

Explore the Model Flow

Click on any stage to learn more about it and download artifacts.

The Olmo 3 checkpoints we're releasing represent our initial paths targeting our goals around reasoning, tool use, and general capabilities – we have exciting plans for other ways to leverage Olmo 3-Base 32B. But because we're releasing the entire flow, you can intervene at any point: swap in domain-specific data during mid-training, adjust post-training for your use case, or build on an earlier checkpoint that better suits your needs. 

As with Olmo and Olmo 2, we’re making all the components of the Olmo 3 flow openly available to the public—data, code, model weights, and checkpoints.  

Strong performance across the board

We run the Olmo 3 checkpoints through a broad, updated benchmark suite, grouping dozens of industry-standard tasks (plus a few new ones we introduce) into several capability clusters. Together, the clustered suite and these held-out tasks give us a capability profile of Olmo 3—a clear picture of how well it solves math problems, codes, uses tools, answers general-knowledge questions, and more. 

At a high level, the Olmo 3 family delivers the strongest fully open base and thinking models we’re aware of. Olmo 3-Base 32B outperforms other fully open base models, and Olmo 3-Think 32B emerges as the strongest fully open thinking model.

Our results were made possible by rigorous data curation at every stage of training, a carefully designed training recipe for each model, and a set of new algorithmic and infrastructure advances across data processing, training, and reinforcement learning. We also introduce an enhanced reinforcement learning framework that guides the development of our models and is particularly essential for our thinking models. To design the training recipe and coordinate targeted improvements across a wide range of capabilities at each stage of the model training pipeline, our development framework balances distributed innovation with centralized evaluation.

Olmo 3-Base, with atraining pipeline that first focuses on broad coverage over diverse text, code, and math, then concentrates on harder distributions to sharpen programming, quantitative reasoning, and reading comprehension, is clearly the strongest set of fully open base models in our evaluations. It’s also arguably the best 32B model in the entire ecosystem of models with open weights, performing impressively in programming, reading comprehension, math problem solving, and long-context benchmarks like RULER, which tests information retrieval from lengthy texts. Olmo 3-Base (7B) and Olmo 3-Base (32) maintain quality at extended context lengths and integrate cleanly with RL workflows, providing a robust foundation for continued pretraining and post-training.

SkillBenchmarkOlmo 3-Base (32B)Marin 32BApertus 70BQwen 2.5 32BGemma 3 27BLlama 3.1 70BMathGSM8k80.5 ▲69.163.081.181.381.2GSM Symbolic61.042.038.656.261.264.6MATH43.436.817.456.747.040.2CodeBigCodeBench43.934.524.048.144.043.4HumanEval66.5 ★52.332.565.662.157.4DeepSeek LeetCode1.91.31.28.05.80.2DS 100029.726.317.843.334.329.5MBPP60.252.137.669.860.055.5MultiPL HumanEval35.918.518.449.737.732.2MultiPL MBPP41.830.531.353.647.235.9MC STEMARC MC94.793.490.797.095.895.2MMLU STEM70.868.457.879.774.970.0MedMCQA MC57.661.855.968.864.767.8MedQA MC53.860.852.468.468.772.3SciQ MC95.5 ▲95.193.397.196.895.4MC Non-STEMMMLU Humanities78.378.974.185.080.583.4MMLU Social Sci.83.983.779.288.486.287.4MMLU Other75.175.470.181.280.279.4CSQA MC82.380.176.989.979.079.0PiQA MC85.690.579.093.390.391.5SocialIQA MC83.982.479.386.681.283.5CoQA Gen2MC MC96.4 ▲93.987.596.895.895.1DROP Gen2MC MC87.2 ★71.056.586.684.670.3Jeopardy Gen2MC MC92.395.393.297.095.997.1NaturalQs Gen2MC MC78.081.071.979.982.082.4SQuAD Gen2MC MC98.2 ★97.695.797.997.797.7GenQAHellaSwag RC84.887.284.586.386.088.4Winogrande RC90.3 ▲90.587.787.591.391.7Lambada75.776.774.876.277.579.6Basic Skills93.5 ▲91.187.594.294.992.4DROP81.0 ★76.556.353.775.978.3Jeopardy75.380.577.274.082.184.0NaturalQs48.755.143.139.349.253.1SQuAD94.5 ★94.490.764.992.492.9CoQA74.1 ★70.772.840.412.473.9Held-OutBBH77.670.158.881.177.480.8MMLU Pro MC49.648.139.661.153.150.4Deepmind Math30.126.720.140.730.440.3LBPP21.717.38.140.317.711.8
★ indicates an Olmo win among this subset. ▲ indicates Olmo is within 2.0 points of the best score. See our report for more comparisons.

Olmo 3-Think, whichturns the Base into a reasoning model by training on multi-step problems spanning math, code, and general problem solving, then running the thinking SFT → thinking DPO → RLVR model flow to elicit high-quality reasoning traces, competes with or exceeds several open-weight reasoning models of similar sizes. On math benchmarks, Olmo 3-Think (7B) matches Qwen 3 8B on MATH and comes within a few points on AIME 2024 and 2025, and also leads all comparison models on HumanEvalPlus for coding—performing strongly on MBPP and LiveCodeBench to demonstrate particular strength in code-intensive reasoning. On broader reasoning tasks like BigBench Hard and AGI Eval English, Olmo 3-Think (7B) remains competitive with Qwen 3 8B reasoning and Qwen 3 VL 8B Thinker while staying fully open and slightly smaller. 

For the 32B model, Olmo 3-Think scales these trends up and becomes one of the strongest fully open reasoning models in its class. Olmo 3-Think (32B) either wins or sits within roughly two points of the best open-weight model on MATH, OMEGA, BigBenchHard, HumanEvalPlus, PopQA, and IFEval. It ties Qwen 3 VL 32B Thinking for the top score on the OMEGA suite while staying clearly ahead of Gemma 3 27B Instruct and competitive with DeepSeek R1 Distill 32B on math and reasoning. On broader knowledge and QA, Olmo 3-Think (32B) is effectively neck-and-neck with the Qwen 3 models on PopQA. And in instruction following, Olmo 3-Think (32B) tops this subset on IFEval and remains solid on IFBench and AlpacaEval 2 LC—offering a strong default for reasoning workloads at the 32B scale.

SkillBenchmarkOlmo 3-Think (32B)Qwen 3 32BQwen 3 VL 32B ThinkingGemma 3 27B InstructDeepSeek R1 Distill 32BMathMATH96.1 ▲95.496.787.492.6AIME 202476.880.886.328.970.3AIME 202572.570.978.822.956.3OMEGA50.8 ▲47.750.824.038.9ReasoningBigBenchHard89.8 ▲90.691.182.489.7ZebraLogic76.088.396.124.869.4AGI Eval English88.290.092.276.988.1CodingHumanEvalPlus91.4 ▲91.290.679.292.3MBPP+68.070.666.265.770.1LiveCodeBench v383.590.284.839.079.5IFIFEval89.0 ★86.585.585.478.7IFBench47.637.355.131.323.8Knowledge & QAMMLU85.488.890.174.688.0PopQA31.9 ▲30.732.230.226.7GPQA58.167.367.445.061.8ChatAlpacaEval 2 LC74.275.680.965.526.2SafetySafety68.869.082.768.663.6
★ indicates an Olmo win among this subset. ▲ indicates Olmo is within 2.0 points of the best score. See our report for more comparisons.

Olmo 3-Instruct, which produces shorter sequences than the corresponding Olmo 3-Think models to improve inference efficiency and is designed to focus on general chat, tool use, and synthetic data generation, outperforms comparably-sized open-weight models. Olmo 3-Instruct ties or surpasses Qwen 2.5, Gemma 3, and Llama 3.1 in our evaluations, and competes with the Qwen 3 family at similar scale, delivering strong function calling performance and instruction-following capabilities in a fully open 7B model.

SkillBenchmarkOlmo 3-Instruct (7B)Qwen 3 8B (no reasoning)Qwen 3 VL 8B InstructApertus 8B InstructGranite 3.3 8B InstructMathMATH87.382.391.621.967.3AIME 202444.326.255.10.57.3AIME 202532.521.743.30.26.3OMEGA28.920.532.35.010.7ReasoningBigBenchHard71.273.785.642.261.2ZebraLogic32.925.464.35.317.6AGI Eval English64.476.084.550.864.0CodingHumanEvalPlus77.279.882.934.464.0MBPP+60.264.466.342.154.0LiveCodeBench v329.553.255.97.811.5IFIFEval85.686.387.871.477.5IFBench32.3 ▲29.334.022.122.3KnowledgeMMLU69.180.483.662.763.5QAPopQA14.120.426.525.528.9GPQA40.444.651.128.833.0ChatAlpacaEval 2 LC40.949.873.58.128.6Tool UseSimpleQA79.379.090.3N/AN/ALitQA238.2 ▲39.630.7N/AN/ABFCL49.860.266.2N/AN/ASafetySafety87.3 ★78.080.272.273.7
Results are the average of three runs. ★ indicates an Olmo win among this subset. ▲ indicates Olmo is within 2.0 points of the best score. See our report for more comparisons.

The Olmo 3 architecture and training stages

Olmo 3 uses a decoder-only transformer architecture and multi-stage training pipeline. Pretraining runs in three stages—an initial large-scale training run that builds broad capabilities; a mid-training phase that focuses on harder material like math, code, and reading comprehension; and a final long-context extension stage that trains the model on very long documents. Together with architectural enhancements, this yields a more capable, efficient base for the Olmo 3 family.

Post-training then specializes the pretrained model for different use cases. Building on Olmo 2, each pathway follows a three-stage recipe – SFT, preference tuning with DPO, and RLVR – but in Olmo 3, we expose this as a fully documented model flow with complete customization over each training stage and dataset mix.

Instead of releasing only the final weights, we provide checkpoints from each major training milestone: the base pretrained model, the mid-trained model after targeted skill enhancement, the long-context-extended version, plus post-training checkpoints for the Olmo 3-Think, Olmo 3-Instruct, and Olmo 3-RL Zero flows. You can study how capabilities emerge over time, run ablations on specific stages, and fork the model at whatever point best fits your data, compute, and goals.

Expanded training data

Compared to Olmo 2, we scaled data collection and significantly strengthened our dataset curation methods. Continuing our commitment to full transparency, we’re releasing several new, higher-quality datasets that cover every stage of base model training and post-training—from initial learning to specialized skills like complex reasoning and long-context understanding. This means anyone can see exactly what data shaped the model’s capabilities, reproduce our results, and reuse these datasets to train their own AI systems.

Olmo 3 is pretrained on Dolma 3, a new ~9.3-trillion-token corpus drawn from web pages, science PDFs processed with olmOCR, codebases, math problems and solutions, and encyclopedic text. From this pool, we construct Dolma 3 Mix, a 5.9-trillion-token (~6T) pretraining mix with a higher proportion of coding and mathematical data than earlier Dolma releases, plus much stronger decontamination via extensive deduplication, quality filtering, and careful control over data mixing. We follow established web standards in collecting training data and don’t collect from sites that explicitly disallow it, including paywalled content.

On top of this, we introduce two Dolma 3-based mixes for later stages of base model training. Dolma 3 Dolmino is our mid-training mix: 100B training tokens sampled from a ~2.2T-token pool of high-quality math, science, code, instruction-following, and reading-comprehension data, including reasoning traces that also enable RL directly on the base model. Dolma 3 Longmino is our long-context mix: ~50B training tokens drawn from a 639B-token pool of long documents combined with mid-training data to teach Olmo 3 to track information over very long inputs (like reports, logs, and multi-chapter documents).

We also introduce Dolci, a new post-training data suite tailored specifically for reasoning, tool use, and instruction following. Dolci provides separate mixes for each stage of post-training: SFT, DPO, and RLVR. For SFT, Dolci aggregates state-of-the-art datasets that advance step-by-step reasoning, tool use, and high-quality conversational behavior; for DPO, it supplies high-quality contrastive preference data; and for RL, it includes hard, diverse prompts across math, coding, instruction following, and general chat. 

Together, Dolma 3 and Dolci give Olmo 3 a fully open data curriculum from first token to final post-trained checkpoint.

Efficient training stack

We pretrained Olmo 3 on a cluster of up to 1,024 H100 GPUs; we achieved training throughput of 7.7K tokens per device per second for Olmo 3-Base (7B). We mid-trained on 128 H100 GPUs, and post-trained on a set of 256 H100s.

For Olmo 3, building on the work we did for Olmo 2, we were able to significantly improve the efficiency of our post-training code. By moving SFT from Open Instruct (our post-training codebase, prioritizing flexibility) to Olmo Core (our pretraining codebase, designed to maximize efficiency), we increased throughput (tokens/second) by 8x. Similarly, by incorporating in-flight weight updates, continuous batching, and a lot of threading improvements, we made our RL training 4x more efficient—resulting in training runs that are significantly cheaper and faster. 

ImprovementTotal tokens
(Mtok)Speed
(Tokens/sec)MFU
(%)MBU
(%)Olmo 26.348810.3012.90continuous batching7.029750.3314.29better threading9.7713580.4619.89inflight updates (Olmo 3)21.2329491.0143.21

A note on our 32B models: We believe 32B sits in a sweet spot for research and tinkering. 32B models are big enough to support strong, competitive performance, but still small enough that a wide audience can fine-tune and deploy them on accessible hardware.

For more details, including ablations, please read our technical report. 

Transparency at the core

A core goal of Olmo 3 is not just to open the model flow, but to make it actionable for people who want to understand and improve model behavior. Olmo 3 integrates with OlmoTrace, our tool for tracing model outputs back to training data in real time.

For example, in the Ai2 Playground, you can ask Olmo 3-Think (32B) to answer a general-knowledge question, then use OlmoTrace to inspect where and how the model may have learned to generate parts of its response. This closes the gap between training data and model behavior: you can see not only what the model is doing, but why—and adjust data or training decisions accordingly.

To further promote transparency and explainability, we’re making every training and fine-tuning dataset available for download without any license restrictions, allowing for custom deployment and reuse. The datasets come in a range of mixes to accommodate different storage and hardware constraints, from several billion tokens all the way up to 6 trillion.

Our new tooling for data processing allows you to de-contaminate, tokenize, and de-duplicate data in the same way we did for Olmo 3’s corpora. All the tooling is open source, enabling you to replicate our training curves or run controlled ablations across data mixes and objectives. 

Our Olmo utilities and software cover the whole development cycle:

Olmo-core is a state-of-the-art framework for distributed model training.

Open Instruct is our post-training pipeline. 

datamap-rs is a pure-Rust toolkit for large-scale cleaning.

duplodocus for ultra-efficient fuzzy de-duplication.

OLMES is a toolkit for reproducible evals. It includes our brand-new eval collection OlmoBaseEval, which we used for Olmo 3 base model development.

decon removes test sets from training data.

Importantly, our tooling allows you to instrument complex tasks and analyze intermediate traces to understand where the models succeed—or struggle. Because the Olmo 3 data recipes, training pipeline, and checkpoints are open, independent teams can connect model behavior back to measurable properties. 

Ready to deploy and use

Together, the Olmo 3 family makes it easier to build trustworthy features quickly, whether for research, education, or applications. By making every development step available and inspectable, we're enabling entirely new categories of research. You can run experiments on any training phase, understand exactly how different techniques contribute to model capabilities, and build on our work at whatever stage makes sense for your project.

For scientists, the fully open flow exposes the model’s inner workings, so you can instrument experiments across coding, reasoning, RL, and tool use. 

If you care about AI you can study, audit, and improve, Olmo 3 is for you. Try the demos in the Ai2 Playground, explore the documentation, and build on the released weights and checkpoints. Then tell us what you discover—we invite the community to validate, critique, and extend our findings.

True openness in AI isn't just about access—it's about trust, accountability, and shared progress. We believe the models shaping our future should be fully inspectable, not black boxes. Olmo 3 represents a different path: one where anyone can understand, verify, and build upon the AI systems that increasingly influence our world. This is what open-first means—not just releasing weights, but sharing the complete knowledge needed to advance AI responsibly: the flow.

Try Olmo 3 on the Ai2 Playground | Use Olmo 3via OpenRouter | Download the models & data| Read the report

Deep dive with Olmo lead researchers Hanna Hajishirzi and Noah Smith on how – and why – we built Olmo 3, and what comes next:

Subscribe to receive monthly updates about the latest Ai2 news.

First Name

Last Name

Email

Sign up

Contact us

Questions about our work, or need support with one of our technologies?

Get in touch

Resources
Media center

Documentation

Careers

Team directory

Community
Discord

Reddit

X/Twitter

GitHub

Hugging Face

LinkedIn

Bluesky

Threads

Legal
Terms of use

Privacy policy

DMCA policy

Business code of conduct

Responsible use

© The Allen Institute for Artificial Intelligence - All Rights Reserved.

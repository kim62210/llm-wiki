---
title: GitHub - gepa-ai/gepa: Optimize prompts, code, and more with AI-powered Reflective Text Evolution · GitHub
source_url: https://github.com/gepa-ai/gepa
final_url: https://github.com/gepa-ai/gepa
status: 200
content_type: text/html; charset=utf-8
topics: [DSPy + GEPA optimize_anything]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:24.834871+00:00
---

# GitHub - gepa-ai/gepa: Optimize prompts, code, and more with AI-powered Reflective Text Evolution · GitHub

## 원본 URL

https://github.com/gepa-ai/gepa

## 추출 본문

GitHub - gepa-ai/gepa: Optimize prompts, code, and more with AI-powered Reflective Text Evolution · GitHub

Skip to content

Navigation Menu
Toggle navigation

 Sign in
 
Appearance settings

Platform

AI CODE CREATION

GitHub CopilotWrite better code with AI

GitHub SparkBuild and deploy intelligent apps

GitHub ModelsManage and compare prompts

MCP RegistryNewIntegrate external tools

DEVELOPER WORKFLOWS

ActionsAutomate any workflow

CodespacesInstant dev environments

IssuesPlan and track work

Code ReviewManage code changes

APPLICATION SECURITY

GitHub Advanced SecurityFind and fix vulnerabilities

Code securitySecure your code as you build

Secret protectionStop leaks before they start

EXPLORE
Why GitHub

Documentation

Blog

Changelog

Marketplace

View all features

Solutions

BY COMPANY SIZE
Enterprises

Small and medium teams

Startups

Nonprofits

BY USE CASE
App Modernization

DevSecOps

DevOps

CI/CD

View all use cases

BY INDUSTRY
Healthcare

Financial services

Manufacturing

Government

View all industries

View all solutions

Resources

EXPLORE BY TOPIC
AI

Software Development

DevOps

Security

View all topics

EXPLORE BY TYPE
Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES
Documentation

Customer support

Community forum

Trust center

Partners

View all resources

Open Source

COMMUNITY

GitHub SponsorsFund open source developers

PROGRAMS
Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES
Topics

Trending

Collections

Enterprise

ENTERPRISE SOLUTIONS

Enterprise platformAI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced SecurityEnterprise-grade security features

Copilot for BusinessEnterprise-grade AI features

Premium SupportEnterprise-grade 24/7 support

Pricing

Search or jump to...

Search code, repositories, users, issues, pull requests...

 Search
 

Clear

Search syntax tips

 Provide feedback
 

We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted

 Cancel
 Submit feedback

 Saved searches
 

Use saved searches to filter your results more quickly

Name

Query

 To see all available qualifiers, see our documentation.
 

 Cancel
 Create saved search

 Sign in
 

 Sign up
 
Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

 gepa-ai
/gepaPublic

Notifications
You must be signed in to change notification settings

Fork
 285

 Star
3.3k

Code

Issues56

Pull requests23

Discussions

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Security and quality

 Insights

gepa-ai/gepa

main

BranchesTags

Go to file

Code
Open more actions menu

Folders and files
NameName
Last commit message

Last commit date

Latest commit

History
768 Commits

768 Commits

.github

.github

assets

assets

docs

docs

examples

examples

src/gepa

src/gepa

terrarium

terrarium

tests

tests

.gitattributes

.gitattributes

.gitignore

.gitignore

.pre-commit-config.yaml

.pre-commit-config.yaml

AGENTS.md

AGENTS.md

CITATION.cff

CITATION.cff

CLAUDE.md

CLAUDE.md

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

README.md

README.md

pyproject.toml

pyproject.toml

pyrightconfig.json

pyrightconfig.json

uv.lock

uv.lock

View all files

Repository files navigation

README

Contributing

MIT license

Optimize any text parameter — prompts, code, agent architectures, configurations — using LLM-based reflection and Pareto-efficient evolutionary search.

Website  | 
 Quick Start  | 
 Paper  | 
 Blog  | 
 Discord

What is GEPA?

GEPA (Genetic-Pareto) is a framework for optimizing any system with textual parameters against any evaluation metric. Unlike RL or gradient-based methods that collapse execution traces into a single scalar reward, GEPA uses LLMs to read full execution traces — error messages, profiling data, reasoning logs — to diagnose why a candidate failed and propose targeted fixes. Through iterative reflection, mutation, and Pareto-aware selection, GEPA evolves high-performing variants with minimal evaluations.

If you can measure it, you can optimize it: prompts, code, agent architectures, scheduling policies, vector graphics, and more.

Key Results

90x cheaperOpen-source models + GEPA beat Claude Opus 4.1 at Databricks35x faster than RL100–500 evaluations vs. 5,000–25,000+ for GRPO (paper)32% → 89%ARC-AGI agent accuracy via architecture discovery40.2% cost savingsCloud scheduling policy discovered by GEPA, beating expert heuristics55% → 82%Coding agent resolve rate on Jinja via auto-learned skills50+ production usesAcross Shopify, Databricks, Dropbox, OpenAI, Pydantic, MLflow, Comet ML, and more

"Both DSPy and (especially) GEPA are currently severely under hyped in the AI context engineering world" — Tobi Lutke, CEO, Shopify

Installation

pip install gepa

To install the latest from 
main
:

pip install git+https://github.com/gepa-ai/gepa.git

Quick Start

Simple Prompt Optimization

Optimize a system prompt for math problems from the AIME benchmark in a few lines of code (full tutorial):

importgepatrainset, valset, _=gepa.examples.aime.init_dataset()

seed_prompt= {
 "system_prompt": "You are a helpful assistant. Answer the question. ""Put your final answer in the format '### <answer>'"
}

result=gepa.optimize(
 seed_candidate=seed_prompt,
 trainset=trainset,
 valset=valset,
 task_lm="openai/gpt-4.1-mini",
 max_metric_calls=150,
 reflection_lm="openai/gpt-5",
)

print("Optimized prompt:", result.best_candidate['system_prompt'])

Result: GPT-4.1 Mini goes from 46.6% → 56.6% on AIME 2025 (+10 percentage points).

With DSPy (Recommended for AI Pipelines)

The most powerful way to use GEPA for prompt optimization is within DSPy, where it's available as 
dspy.GEPA
. See dspy.GEPA tutorials for executable notebooks.

importdspyoptimizer=dspy.GEPA(
 metric=your_metric,
 max_metric_calls=150,
 reflection_lm="openai/gpt-5",
)
optimized_program=optimizer.compile(student=MyProgram(), trainset=trainset, valset=valset)

optimize_anything: Beyond Prompts

The 
optimize_anything
 API optimizes any text artifact — code, agent architectures, configurations, SVGs — not just prompts. You provide an evaluator; the system handles the search.

importgepa.optimize_anythingasoafromgepa.optimize_anythingimportoptimize_anything, GEPAConfig, EngineConfigdefevaluate(candidate: str) ->float:
 result=run_my_system(candidate)
 oa.log(f"Output: {result.output}") # Actionable Side Informationoa.log(f"Error: {result.error}") # feeds back into reflectionreturnresult.scoreresult=optimize_anything(
 seed_candidate="<your initial artifact>",
 evaluator=evaluate,
 objective="Describe what you want to optimize for.",
 config=GEPAConfig(engine=EngineConfig(max_metric_calls=100)),
)

How It Works

Traditional optimizers know that a candidate failed but not why. GEPA takes a different approach:

Select a candidate from the Pareto frontier (candidates excelling on different task subsets)

Execute on a minibatch, capturing full execution traces

Reflect — an LLM reads the traces (error messages, profiler output, reasoning logs) and diagnoses failures

Mutate — generate an improved candidate informed by accumulated lessons from all ancestors

Accept — add to the pool if improved, update the Pareto front

GEPA also supports system-aware merge — combining strengths of two Pareto-optimal candidates excelling on different tasks. The key concept is Actionable Side Information (ASI): diagnostic feedback returned by evaluators that serves as the text-optimization analogue of a gradient.

For details, see the paper and the documentation.

Adapters: Plug GEPA into Any System

GEPA connects to your system via the 
GEPAAdapter
 interface — implement 
evaluate
 and 
make_reflective_dataset
, and GEPA handles the rest.

Built-in adapters:
AdapterDescriptionDefaultAdapterSystem prompt optimization for single-turn LLM tasksDSPy Full ProgramEvolves entire DSPy programs (signatures, modules, control flow). 67% → 93% on MATH.Generic RAGVector store-agnostic RAG optimization (ChromaDB, Weaviate, Qdrant, Pinecone)MCP AdapterOptimize MCP tool descriptions and system promptsTerminalBenchOptimize the Terminus terminal-use agentAnyMathsMathematical problem-solving and reasoning tasks
See the adapters guide for how to build your own, and DSPy's adapter as a reference.

Integrations

GEPA is integrated into several major frameworks:

DSPy — 
dspy.GEPA
 for optimizing DSPy programs. Tutorials.

MLflow — 
mlflow.genai.optimize_prompts()
 for automatic prompt improvement.

Comet ML Opik — Core optimization algorithm in Opik Agent Optimizer.

Pydantic — Prompt optimization for Pydantic AI.

OpenAI Cookbook — Self-evolving agents with GEPA.

HuggingFace Cookbook — Prompt optimization guide.

Google ADK — Built-in agent optimization in Google's Agent Development Kit. Community tutorial.

Example Optimized Prompts

GEPA can be thought of as precomputing reasoning during optimization to produce a plan for future task instances. Here are examples of the detailed prompts GEPA discovers:
Example GEPA PromptsHotpotQA (multi-hop QA) PromptAIME PromptClick to view full HotpotQA prompt[HotpotQA Prompt Begin]
You will be given two input fields: 
question
 and 
summary_1
.

Your task is to generate a new search query (
query
) optimized for the second hop of a multi-hop retrieval system. The original user question is typically complex and requires information from multiple documents to answer. The first hop query is the original question used to retrieve an initial set of documents. Your goal is to generate a second hop query that retrieves additional relevant documents that were not found in the first hop but are necessary to answer the original question completely.

Detailed task instructions and hints:

Input Understanding:

question
 is the original multi-hop question posed by the user.

summary_1
 is a concise summary of information from a document retrieved in the first hop, which partially addresses the question.

Purpose and Context:

Your generated 
query
 aims to find the missing pieces of information needed to fully answer the 
question
.

The multi-hop retrieval system works in stages:

First hop: The original question returns some documents.

Second hop: Your query must help retrieve any other relevant documents NOT found in the first hop that hold complementary or broader context necessary for final answer extraction.

Key Observations from Examples and Feedback:

First-hop documents often cover one entity or aspect in the question.

Remaining relevant documents often involve connected or higher-level concepts mentioned in 
summary_1
 but not explicitly asked in the original question.

The 
query
 should be formulated to explicitly target these missing, but logically linked, documents.

Avoid merely paraphrasing the original question or restating known facts from 
summary_1
.

Instead, infer what broader or related entities/concepts might provide the crucial missing information.

For example, if 
summary_1
 describes a population for a small civil parish, but the question wants total population of the wider region, your 
query
 should target that wider region (e.g., "Madeira archipelago population in 2011").

Similarly, if 
summary_1
 covers a song and the question wants the album it came from, but first hop got song-level documents, your query should retrieve documents about the album itself.

How to Build the Query:

Identify the entities or topics mentioned in 
summary_1
 that appear related but different from first-hop documents.

Reframe the query to explicitly mention these broader or related entities connected to the original question.

Include relevant key context from the question to maintain specificity, but shift focus to the missing piece.

The goal is to retrieve documents that link or complement what was retrieved initially.

Practical Strategy:

Read the 
summary_1
 carefully to spot references to bigger contexts or other entities not covered in the first hop.

Ask yourself, "What entity or aspect does this summary hint at that could answer the original question but was not found yet?"

Formulate a precise, focused factual query targeting that entity or concept to retrieve the missing documents.

Output:

Produce only the field 
query
 as a clear, concise question or keyword phrase designed for efficient retrieval of second-hop documents.

Ensure the query relates logically to the original question while targeting the broader or complementary knowledge identified in 
summary_1
.

Do not include the original question or simply rephrase it.

Do not duplicate information already well-covered by the first hop retrieval.

By following these principles, you will help the multi-hop retrieval system find all necessary documents to answer the multi-faceted original question completely.

[HotpotQA Prompt End]
Click to view full AIME prompt
[AIME Prompt Begin]

You will be given one math problem as plain text under a key like "problem." Your job is to solve it correctly and return:

reasoning: a concise, logically ordered solution that uses identities/structure to avoid brute force, ends with a quick verification.

answer: the final requested number/expression only (no extra words).

Formatting:

Use exactly two top-level fields named "reasoning" and "answer."

Keep reasoning succinct but complete. Bullet points are fine.

The answer field must contain only the final value requested (e.g., 227, 585, 601).

General problem-solving guidance:

Parse the problem type (e.g., base representation, intersecting families of subsets, avoiding arithmetic progressions, symmetric sums with constraints, ordered tuples counting).

Always enforce domain constraints (e.g., base-b digits in 0..b−1; no leading zero for base-10 "three-digit"; ordered vs unordered families; strict increase conditions in sequences).

Use algebraic identities and modular arithmetic to reduce the search space; prefer structural arguments over naive enumeration.

For "greatest/least" questions, derive tight bounds and give a construction that attains them.

Domain-specific strategies and pitfalls (learned from typical contest problems and prior feedback):

Base-conversion/digit rearrangement:

Translate positional notation correctly: in base b, (a b c)_b = a·b^2 + b·b + c; in base 10: abc = 100a + 10b + c.

Enforce digit ranges strictly (e.g., in base 9, digits ∈ {0,…,8}; if also a is a base-10 leading digit, then a ∈ {1,…,8}).

Set up equality and simplify. Use modular constraints to prune:
• Mod 9 often collapses coefficients; e.g., 99a = 71b + 8c ⇒ mod 9 gives b + c ≡ 0 (mod 9).
• Mod 8: 99 ≡ 3, 71 ≡ 7 ⇒ 3a ≡ 7b (mod 8) ⇒ b ≡ −3a (mod 8).

Solve within digit bounds and verify numerically.

Palindromes across bases:

Bound the base length by magnitude (e.g., n < 1000 ⇒ octal has 3–4 digits).

Characterize palindromes:
• 3-digit octal: (A B A)_8 = 65A + 8B.
• 4-digit octal: (A B B A)_8 = 513A + 72B (with A ≥ 1).

Enumerate small parameter ranges and test the other-base palindrome constraint. For "greatest", check candidates in descending order with justification.

Symmetric sums with a + b + c fixed (ordered triples of nonnegative integers):

Use identities to compress expressions:
S = ab(a + b) + bc(b + c) + ca(c + a) = (a + b + c)(ab + bc + ca) − 3abc.

With a + b + c known (e.g., 300), convert the given sum into a relation among ab + bc + ca and abc.

Use the shift a = A + x etc. to isolate a product like (a−A)(b−A)(c−A) and deduce factorization constraints, enabling clean counting.

Count ordered solutions carefully; include/exclude symmetric/degenerate cases precisely.

Intersecting families of subsets (collections from the power set):

Intersecting means every pair has nonempty intersection. The empty set cannot be included.

Complement pairs: S and S^c cannot both be present. Use this to structure counts.

Use size-based pigeonhole facts: In [n], any two subsets of size > n/2 must intersect. For n = 5, any two subsets of size ≥ 3 intersect; thus "all subsets of size ≥ 3" is an intersecting family (size 16).

Do not assume that "stars" (all subsets containing a fixed element) are the only intersecting families of maximum size. For odd n, both the star and "all subsets of size > n/2" have size 2^{n−1}.

When counting collections of a fixed size:
• Consider the minimum set size N in the family and do casework on how many 2-element sets are included (for n=5), as these control which 3-sets must be excluded (complements).
• Ensure completeness of cases and avoid double counting by parameterizing canonical patterns (e.g., how many 2-sets, how they overlap, whether they share a common element).
• Remember order of subsets in a collection does not matter; count distinct families.

Avoiding 4-term arithmetic progressions in a strictly increasing sequence with fixed anchors:

First bound the variable terms by strict increase (e.g., if fixed terms are 3,4,5,...,30,40,50 then 6 ≤ a < b ≤ 29).

Pre-eliminate values that cause a 4-term AP with three fixed terms:
• 3,4,5,a forbids a = 6.
• b,30,40,50 forbids b = 20.
• Similarly, a,30,40,50 forbids a = 20.

Start with the count of pairs from allowed values and then subtract specific pairs that complete APs with two fixed endpoints:
• 3,5,a,b ⇒ (a,b) = (7,9).
• 3,a,b,30 ⇒ (a,b) = (12,21).
• 4,a,b,40 ⇒ (a,b) = (16,28).
• 5,a,b,50 ⇒ (a,b) = (20,35) but may be outside bounds or pre-excluded (e.g., 20 banned).

Systematically check all endpoint combinations; use the fact that if endpoints differ by Δ, then Δ must be divisible by 3 for a 4-term AP, and solve for integer a,b within bounds.

Avoid double subtraction; ensure monotonicity and domain constraints are respected.

Order statistics with sum and absolute-sum constraints (e.g., x_1 ≤ ... ≤ x_n, sum |x_i| = 1, sum x_i = 0):

Total positive mass equals total negative mass: both = 1/2.

For maximizing x_k (k near the top): if there are T largest terms from k to n (T = n − k + 1), then sum of these T terms ≥ T·x_k. Since the total positive mass ≤ 1/2, we get x_k ≤ (1/2)/T.

For minimizing x_l (l near the bottom): if there are l smallest terms, sum of these l terms ≤ l·x_l. Since the total negative mass is −1/2, we get x_l ≥ (−1/2)/l.

To attain these bounds, concentrate masses evenly on exactly those positions: set the smallest l terms equal to −1/(2l), the largest T terms equal to 1/(2T), and the middle to 0 (respecting monotonicity). Verify sums and absolute sums.

Example: For n=100, maximize x_76 − x_16: T = 25 ⇒ x_76 ≤ 1/50; l = 16 ⇒ x_16 ≥ −1/32; construction with 16 negatives at −1/32, 59 zeros, 25 positives at 1/50 attains 1/50 − (−1/32) = 41/800.

Quality checks:

Verify digit/base constraints and final equalities numerically if applicable.

For extremal problems, provide both a tight bound and an explicit construction achieving it.

For counting, explicitly handle ordered vs unordered, exclude impossible/duplicate cases, and check complements/forbidden pairs.

For AP-avoidance, confirm integrality and bounds; ensure no missed endpoint combinations.

For "greatest/least" questions, justify optimality structurally (e.g., convexity/majorization/pigeonhole).

Finally:

Put the clean final numeric result in the "answer" field only.

[AIME Prompt End]

When GEPA Shines

Expensive rollouts — Scientific simulations, complex agents with tool calls, slow compilation. GEPA needs 100–500 evals vs 10K+ for RL.

Scarce data — Works with as few as 3 examples. No large training sets required.

API-only models — No weights access needed. Optimize GPT-5, Claude, Gemini directly through their APIs.

Interpretability — Human-readable optimization traces show why each prompt changed.

Complements RL — Use GEPA for rapid initial optimization, then apply RL/fine-tuning for additional gains (BetterTogether).

Further Reading

Paper:GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (arXiv:2507.19457)

Experiment reproduction artifact:GEPA Artifact Repository

Talk Slides: GEPA Talk Slides

Blog Posts:
optimize_anything: A Universal API for Optimizing any Text Parameter

Automatically Learning Skills for Coding Agents

Tutorials & Examples:
dspy.GEPA Tutorials, with executable notebooks
Step-by-step notebooks showing how to use GEPA for practical optimization tasks via DSPy, including math, structured data extraction for enterprise tasks and privacy conscious delegation task.

Video tutorial by @weaviate on using dspy.GEPA to optimize a listwise reranker

Matei Zaharia - Reflective Optimization of Agents with GEPA and DSPy

Building and optimizing a multi-agent system for healthcare domain using DSPy+GEPA

Social and Discussion:
X (formerly Twitter) Announcement Thread (Lakshya A Agrawal)

GEPA covered by VentureBeat

GEPA's use by Databricks covered by VentureBeat

Stay up to date:

@LakshyAAAgrawal on X (Twitter)

@lateinteraction on X (Twitter)

Questions, Discussions?

Join our Discord for active discussion

Join our Slack

Open a GitHub issue

GEPA Integrations:
Want to use GEPA in other frameworks?

DSPy Adapter Code (integrates GEPA with DSPy),

MLflow Prompt Optimization - GEPA is integrated into MLflow's 
mlflow.genai.optimize_prompts()
 API for automatic prompt improvement using evaluation metrics and training data. Works with any agent framework and supports multi-prompt optimization.

Pydantic AI - Prompt optimization for Pydantic AI.

Comet ML Opik - Core optimization algorithm in Opik Agent Optimizer.

OpenAI Cookbook - Self-evolving agents with GEPA.

HuggingFace Cookbook - Prompt optimization guide.

Google ADK - Built-in agent optimization in Google's Agent Development Kit. Community tutorial.

Contributed Adapters – see our adapter templates and issue tracker to request new integrations.

DefaultAdapter - System Prompt Optimization for a single-turn task.

DSPy Full Program Adapter - Evolves entire DSPy programs including signatures, modules, and control flow. Achieves 93% accuracy on MATH benchmark (vs 67% with basic DSPy ChainOfThought).

Generic RAG Adapter - Vector store-agnostic RAG optimization supporting ChromaDB, Weaviate, Qdrant, Pinecone, and more. Optimizes query reformulation, context synthesis, answer generation, and document reranking prompts.

MCP Adapter - Optimize Model Context Protocol (MCP) tool usage. Supports local stdio servers, remote SSE/HTTP servers, and optimizes tool descriptions and system prompts.

TerminalBench Adapter - Easily integrating GEPA into a Terminus, a sophisticated external agentic pipeline, and optimizing the agents' system prompt.

AnyMaths Adapter - Adapter for optimizing mathematical problem-solving and reasoning tasks. Contributed by @egmaminta.

GEPA uses
Nous Research Hermes Agent: evolutionary self-improvement with DSPy + GEPA

Context Compression using GEPA

GEPA Integration into SuperOptiX-AI

GEPA for Observable Javascript

bandit_dspy

GEPA in Go Programming Language

100% accuracy using GEPA on the clock-hands problem

Prompt Optimization for Reliable Backdoor Detection in AI-Generated Code

Teaching LLMs to Diagnose Production Incidents with ATLAS+GEPA

DataBricks: Building State-of-the-Art Enterprise Agents 90x Cheaper with GEPA

comet-ml/opik adds support for GEPA

Tuning small models (Gemma3-1B) for writing fiction

Cut OCR Error Rates by upto 38% across model classes (Gemini 2.5 Pro, 2.5 Flash, 2.0 Flash)

Optimizing a Data Analysis coding agent with GEPA, using execution-guided feedback on real-world workloads

Generating Naruto (Anime) style dialogues with GPT-4o-mini using GEPA

Augmenting RL-tuned models with GEPA: Achieving +142% student performance improvement by augmenting a RL-tuned teacher with GEPA

DeepResearch Agent Optimized with GEPA

Boosting Sanskrit QA: Finetuning EmbeddingGemma with 50k GEPA generated synthetic data samples (Tweet), (Code)

Simulating Realistic Market Research Focus Groups with GEPA-Optimized AI Personas

Google ADK: Official agent optimization powered by GEPA

HuggingFace Cookbook on prompt optimization for with DSPy and GEPA

OpenAI Cookbook showing how to build self-evolving agents using GEPA

What Do Prompts Reveal About Model Capabilities in Low-Resource Languages? (AfricaNLP 2026)

Beyond the Answer: Decoding the Behavior of LLMs as Scientific Reasoners (ICLR 2026 Workshop)

Self-Optimizing Multi-Agent Systems for Deep Research (ECIR 2026 Workshop) — GEPA outperforms TextGrad and expert-crafted prompts

Contributions

We welcome adapters, bug fixes, and new use cases. See src/gepa/adapters/ for adapter examples and the contributing guide.

Want to highlight your use case? Reach out to lakshyaaagrawal@berkeley.edu or submit via GitHub.

Citation

@misc{agrawal2025gepareflectivepromptevolution,
 title={GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning},
 author={Lakshya A Agrawal and Shangyin Tan and Dilara Soylu and Noah Ziems and Rishi Khare and Krista Opsahl-Ong and Arnav Singhvi and Herumb Shandilya and Michael J Ryan and Meng Jiang and Christopher Potts and Koushik Sen and Alexandros G. Dimakis and Ion Stoica and Dan Klein and Matei Zaharia and Omar Khattab},
 year={2025},
 eprint={2507.19457},
 archivePrefix={arXiv},
 primaryClass={cs.CL},
 url={https://arxiv.org/abs/2507.19457},
}

About

 Optimize prompts, code, and more with AI-powered Reflective Text Evolution
 

gepa-ai.github.io/gepa/

Resources

 Readme

License

 MIT license
 

Contributing

 Contributing
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

3.3k
 stars

Watchers

9
 watching

Forks

285
 forks

 Report repository

Releases
 42

v0.1.1
 Latest

Mar 16, 2026

+ 41 releases

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Jupyter Notebook70.9%

Python29.0%

HTML0.1%

Footer

 © 2026 GitHub, Inc.
 

Footer navigation

Terms

Privacy

Security

Status

Community

Docs

Contact

 Manage cookies
 

 Do not share my personal information
 

 You can’t perform that action at this time.

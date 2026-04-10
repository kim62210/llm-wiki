---
title: GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub
source_url: https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents
final_url: https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents
status: 200
content_type: text/html; charset=utf-8
topics: [Agent Memory Systems (Episodic / Semantic / Working)]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:27.608982+00:00
---

# GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub

## 원본 URL

https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents

## 추출 본문

GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub

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

 TsinghuaC3I
/Awesome-Memory-for-AgentsPublic

Notifications
You must be signed in to change notification settings

Fork
 23

 Star
432

Code

Issues1

Pull requests1

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

TsinghuaC3I/Awesome-Memory-for-Agents

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
25 Commits

25 Commits

assets

assets

LICENSE

LICENSE

README.md

README.md

View all files

Repository files navigation

README

MIT license

Awesome-Memory-for-Agents

The paper list is maintained by Hongyi Liu, Yu Fu, Kaiyan Zhang, contributed by Yuxin Zuo, Che Jiang, Guoli Jia, Yuru Wang, Kaikai Zhao, Yuchen Fan, Zhenzhao Yuan, Kai Tian, Weizhi Wang.

Table of Contents

Awesome-Memory-for-Agents
Table of Contents

Overview

Paper List
Application
Personalization

Learning from Experience

Long-horizon Agentic Task

Survey

Benchmark

Product & Project

Overview

This repository provides a curated list of papers on agent memory, structured by a core taxonomy. We first divide agent memory based on its persistence:

Short-Term Memory: Transient information managed within the context window for a single task;

Long-Term Memory: Persistent information stored externally across tasks.

Within Long-Term Memory, we further distinguish based on its reliance on task outcomes (success/failure) for curation:

Experience involves knowledge explicitly validated by task outcomes;

Memory denotes information without reference to task outcomes.

This taxonomy maps directly to the three primary application scenarios that organize the papers in this repository:
ApplicationMemory ContentDescriptionPersonalizationUser profiles, interaction history, facts, etc.Continuous personalized interaction, mainly targeting the conversation scenario and using an external memory pool with retrieval-based memory interactionLearning from ExperienceTrajectories, success/failure lessons, reusable skills, etc.Cross-task experience accumulation & transferLong-horizon Agentic TaskIntermediate results, reasoning traces, environmental observations, etc.Context management within a single long-horizon task via summarization, reflection, or scratchpad, etc.

Paper List

Application

Personalization

DateTitlePaper2026-01Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents2026-01Grounding Agent Memory in Contextual Intent2026-01Continuum Memory Architectures for Long-Horizon LLM Agents2026-01SwiftMem: Fast Agentic Memory via Query-aware Indexing2026-01AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation2026-01Beyond Static Summarization: Proactive Memory Extraction for LLM Agents2026-01TeleMem: Building Long-Term and Multimodal Memory for Agentic AI2026-01HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents2026-01SYNAPSE: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation2026-01TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents2026-01SimpleMem: Efficient Lifelong Memory for LLM Agents2026-01MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents2026-01EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning2026-01CogCanvas: Verbatim-Grounded Artifact Extraction for Long LLM Conversations2026-01Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents2026-01Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents2026-01MemRec: Collaborative Memory-Augmented Agentic Recommender System2025-12Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents2025-11O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents2025-11LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning2025-11Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction2025-10TOM-SWE: User Mental Modeling For Software Engineering Agents2025-10PISA: A Pragmatic Psych-Inspired Unified Memory System for Enhanced AI Agency2025-10EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle2025-10Improving Code Localization with Repository Memory2025-10Mnemosyne: An Unsupervised, Human-Inspired Long-Term Memory Architecture for Edge-Based LLMs2025-10AssoMem: Scalable Memory QA with Multi-Signal Associative Retrieval2025-10LightMem: Lightweight and Efficient Memory-Augmented Generation2025-09MEM-$\alpha$: Learning Memory Construction via Reinforcement Learning2025-09Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents2025-09MIRA: Memory-Integrated Reinforcement Learning Agent with Limited LLM Guidance2025-09REMem: Reasoning with Episodic Memory in Language Agent2025-09Adaptive Friend Agent: Personalized Multi-User Memory for Conversational AI2025-08Orchid: Orchestrating Context Across Creative Workflows with Generative AI2025-08Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning2025-08Learn to Memorize: Optimizing LLM-based Agents with Adaptive Memory Framework2025-07MemOS: A Memory OS for AI System2025-07Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents2025-07MIRIX: Multi-Agent Memory System for LLM-Based Agents2025-06PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time2025-06Cognitive Weave: Synthesizing Abstracted Knowledge with a Spatio-Temporal Resonance Graph2025-05From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents2025-04Mem0: Building production-ready ai agents with scalable long-term memory2025-03Meminsight: Autonomous memory augmentation for llm agents2025-02M+: Extending MemoryLLM with Scalable Long-Term Memory2025-02A-MEM: Agentic Memory for LLM Agents2025-01Wormhole Memory: A Rubik's Cube for Cross-Dialogue Retrieval2025-01Zep: A Temporal Knowledge Graph Architecture for Agent Memory2024-12On the Structural Memory of LLM Agents2024-07MemoCRS: Memory-enhanced Sequential Conversational Recommender Systems with Large Language Models2024-03Larimar: Large language models with episodic memory control2024-01From llm to conversational agent: A memory enhanced architecture with fine-tuning of large language models2023-10MemGPT: Towards LLMs as operating systems2023-08Memochat: Tuning llms to use memos for consistent long-range open-domain conversation2023-06Chatdb: Augmenting llms with databases as their symbolic memory2023-05MemoryBank: Enhancing large language models with long-term memory2023-04Unleashing infinite-length input capacity for large-scale language models with self-controlled memory system

Learning from Experience

DateTitlePaper2026-01Controlled Self-Evolution for Algorithmic Code Optimization2026-01Beyond Static Tools: Test-Time Tool Evolution for Scientific Reasoning2026-01MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences2026-01Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory2026-01Distilling Feedback into Memory-as-a-Tool2026-01EvoRoute: Experience-Driven Self-Routing LLM Agent Systems2025-12WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment2025-12Unifying Dynamic Tool Creation and Cross-Task Experience Sharing through Cognitive Memory Architecture2025-12LoongFlow: Directed Evolutionary Search via a Cognitive Plan-Execute-Summarize Paradigm2025-12CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution2025-12MemEvolve: Meta-Evolution of Agent Memory Systems2025-12Memento 2: Learning by Stateful Reflective Memory2025-11Improving Language Agents through BREW2025-11Scaling Agent Learning via Experience Synthesis2025-11FLEX: Continuous Agent Evolution via Forward Learning from Experience2025-11Multi-agent In-context Coordination via Decentralized Memory Retrieval2025-11AgentEvolver: Towards Efficient Self-Evolving Agent System2025-11Experience-Guided Adaptation of Inference-Time Reasoning Strategies2025-11WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance2025-11Real-Time Procedural Learning From Experience for AI Agents2025-11SkillGen: Learning Domain Skills for In-Context Sequential Decision Making2025-11Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?2025-10Alita-G: Self-Evolving Generative Agent for Agent Generation2025-10Dyna-Mind: Learning to Simulate from Experience for Better AI Agents2025-10LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation2025-10The Cognitive Bandwidth Bottleneck: Shifting Long-Horizon Agent from Planning with Actions to Planning with Schemas2025-10Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models2025-10TokMem: Tokenized Procedural Memory for Large Language Models2025-10Training-Free Group Relative Policy Optimization2025-10Self-evolving expertise in complex non-verifiable subject domains: dialogue as implicit meta-RL2025-09Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization2025-09Automated Stateful Specialization for Adaptive Agent Systems2025-09BMAS: A Brain-Inspired Multi-Agent System with PFC-Guided Task Coordination and Hippocampus-Neocortex Dual Memory for Scalable Multi-Step Reasoning2025-09MemGen: Weaving Generative Latent Memory for Self-Evolving Agents2025-09MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution2025-09ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory2025-09MLE-RL: Reinforcement Learning for Self-Improvement in Machine Learning Agents2025-09ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory2025-09Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors2025-08SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience2025-08Memento: Fine-tuning LLM Agents without Fine-tuning LLMs2025-08SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents2025-08Memp: Exploring Agent Procedural Memory2025-07Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving2025-07SWE-Exp: Experience-Driven Software Issue Resolution2025-06Xolver: Generalist Reasoning and Problem Solving through Federated Multi-Agent Dynamics and Holistic Experience Learning2025-06G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems2025-06Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching2025-06MAPLE: Multi-Agent Adaptive Planning with Long-Term Memory for Table Reasoning2025-05ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering2025-05How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior2025-05Efficiently enhancing general agents with hierarchical-categorical memory2025-04SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills2025-04Inducing Programmatic Skills for Agentic Tasks2025-04Memorization and knowledge injection in gated llms2025-04Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory2025-03Mars: Memory-enhanced agents with reflective self-improvement2024-09Agent workflow memory2024-05AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning2024-05Iterative experience refinement of software- developing agents2024-04An artificial neuron for enhanced problem solving in large language models2024-03Online adaptation of language models with a memory of amortized contexts2024-02Camelot: Towards large language models with training-free consolidated associative memory2023-08Retroformer: Retrospective large language agents with policy gradient optimization2023-08ExpeL: LLM Agents Are Experiential Learners2023-06Synapse: Trajectory-as-exemplar prompting with memory for computer control2023-03Reflexion: Language agents with verbal reinforcement learning2020-09Meta-learning with sparse experience replay for lifelong language learning

Long-horizon Agentic Task

DateTitlePaper2026-01To Retrieve or To Think? An Agentic Approach for Context Evolution2026-01MemoBrain: Executive Memory as an Agentic Brain for Reasoning2026-01Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents2025-12ABBEL: LLM Agents Acting Through Belief Bottlenecks Expressed in Language2025-12Context as a Tool: Context Management for Long-Horizon SWE-Agents2025-11Efficient On-Device Agents via Adaptive Context Management2025-11MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning2025-11IterResearch: Rethinking Long-Horizon Agents via Markovian State Reconstruction2025-10Prompt reinforcing for long-term planning of large language models2025-10Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks2025-10ACON: Optimizing Context Compression for Long-horizon LLM Agents2025-10BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions2025-10WebDART: Dynamic Decomposition and Re-planning for Complex Web Tasks2025-10CAM: A Constructivist View of Agentic Memory for LLM-Based Reading Comprehension2025-10Scaling LLM Multi-turn RL with End-to-end Summarization-based Context Management2025-10AgentFold: Long-Horizon Web Agents with Proactive Context Management2025-10Beyond Turn Limits: Training Deep Search Agents with Dynamic Context Window2025-10Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks2025-10DeepAgent: A General Reasoning Agent with Scalable Toolsets2025-09WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research2025-09Don’t Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation2025-09CEA: Context Engineering Agent for Enhanced Reliability and Sustainability in Deep Research Systems2025-09The Pensieve Paradigm: Stateful Language Models with Learned Memory Management2025-09Compressed Step Information Memory for End-to-End Agent Foundation Models2025-09PARL-MT: Learning to Call Functions in Multi-Turn Conversation with Progress Awareness2025-09ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization2025-08Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management2025-08Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory2025-08Cognitive Workspace: Active Memory Management for LLMs - An Empirical Study of Functional Infinite Context2025-08Profile-Aware Maneuvering: A Dynamic Multi-Agent System for Robust GAIA Problem Solving by AWorld2025-07MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent2025-07MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations2025-06MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents2025-06Taskcraft: Automated generation of agentic tasks2024-10From isolated conversations to hierarchical schemas: Dynamic tree memory representation for LLMs2024-09Self-evolving Agents with reflective and memory-augmented abilities2024-07Human-like episodic memory for infinite context llms2024-07AriGraph: Learning knowledge graph world models with episodic memory for LLM agents2024-06QRMeM: Unleash the Length Limitation through Question then Reflection Memory Mechanism

Survey

DateTitlePaperGitHub2025-09The Landscape of Agentic Reinforcement Learning for LLMs: A Survey2025-08OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use2025-08A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems2025-07A Survey of Context Engineering for Large Language Models2025-07A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence2025-05Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions2025-04From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs2025-04Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems2025-03Agentic Large Language Models, a survey2024-04A Survey on the Memory Mechanism of Large Language Model-based Agents

Benchmark

DateNameTitlePaperGitHub2026-01CloneMemCloneMem: Benchmarking Long-Term Memory for AI Clones2026-01KnowMe-BenchKnowMe-Bench: Benchmarking Person Understanding for Lifelong Digital Companions2026-01RealMemRealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction2025-12PersonaMem-v2PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory2025-11LoCoBench-AgentLoCoBench-Agent: An Interactive Benchmark for LLM Agents in Long-Context Software Engineering2025-11ConvoMemConvomem Benchmark: Why Your First 150 Conversations Don't Need RAG2025-08StuLifeBuilding Self-Evolving Agents via Experience-Driven Lifelong Learning: A Framework and Benchmark2025-07MemoryAgentBenchEvaluating Memory in LLM Agents via Incremental Multi-Turn Interactions2025-06StoryBenchStoryBench: A Dynamic Benchmark for Evaluating Long-Term Memory with Multi Turns2025-06WebChoreArenaWebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks2025-06MemBenchMemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents2025-05LifelongAgentBenchLifelongAgentBench: Evaluating LLM Agents as Lifelong Learners2025-02RealTalkREALTALK: A 21-Day Real-World Dataset for Long-Term Conversation2024-10LongMemEvalLongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory2024-09MADail-BenchMADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation2024-09LTMBeyond Prompts: Dynamic Conversational Benchmarking of Large Language Models2024-02LoCoMoEvaluating Very Long-Term Conversational Memory of LLM Agents

Product & Project

DateNameTitlePaperWebsiteGitHub2026-03LorgPermanent intelligence archive for AI agents. Structured contributions (prompts, workflows, insights, patterns) pass an automated quality gate and are hash-chained. Trust scores are cryptographically backed and publicly auditable.2026-02SuperLocalMemory V2Universal local-first memory infrastructure for AI agents with dual MCP + A2A protocol support2025-12ReMe (prev. MemoryScope)Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution2025-12HindsightHindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects2025-05CogneeOptimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning2025-04Mem0Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory2025-01Graphiti (prev. Zep)Zep: A Temporal Knowledge Graph Architecture for Agent Memory2023-10Letta (prev. MemGPT)MemGPT: Towards LLMs as Operating SystemsMemMachineAcontextMemobaseClaude-MemMemoVMemlayerOpenContextMemoriMemUOpenMemoryMemaryLangChainMemoryBear

About

 A Collection of Papers about Memory for Language Agents
 

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

432
 stars

Watchers

2
 watching

Forks

23
 forks

 Report repository

Releases

No releases published

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

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

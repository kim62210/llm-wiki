---
title: GitHub - Shichun-Liu/Agent-Memory-Paper-List: The paper list of "Memory in the Age of AI Agents: A Survey" · GitHub
source_url: https://github.com/Shichun-Liu/Agent-Memory-Paper-List
final_url: https://github.com/Shichun-Liu/Agent-Memory-Paper-List
status: 200
content_type: text/html; charset=utf-8
topics: [Agent Memory Systems (Episodic / Semantic / Working)]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:27.411980+00:00
---

# GitHub - Shichun-Liu/Agent-Memory-Paper-List: The paper list of "Memory in the Age of AI Agents: A Survey" · GitHub

## 원본 URL

https://github.com/Shichun-Liu/Agent-Memory-Paper-List

## 추출 본문

GitHub - Shichun-Liu/Agent-Memory-Paper-List: The paper list of "Memory in the Age of AI Agents: A Survey" · GitHub

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

 Shichun-Liu
/Agent-Memory-Paper-ListPublic

Notifications
You must be signed in to change notification settings

Fork
 77

 Star
1.8k

Code

Issues9

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

Shichun-Liu/Agent-Memory-Paper-List

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
40 Commits

40 Commits

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

Memory in the Age of AI Agents: A Survey

📢 News

[2026/01/29] 🎉 Our repository has reached 1k stars! Thank you all for your support and interest in Agent Memory research!

[2026/01/13] 📄 We have updated our survey to incorporate several recent works, and we sincerely thank the community for their valuable contributions and suggestions. See Memory in the Age of AI Agents: A Survey for the paper!

[2025/12/16] 🎉 Our paper is featured on Huggingface Daily Paper #1!

[2025/12/16] 📚 We create this repository to maintain a paper list on Agent Memory. More papers are coming soon!

[2025/12/16] 📄 Our survey is released! See Memory in the Age of AI Agents: A Survey for the paper!

Figure: Overview of agent memory organized by the unified taxonomy of forms, functions, and dynamics.

👋 Introduction

Memory serves as the cornerstone of foundation model-based agents, underpinning their ability to perform long-horizon reasoning, adapt continually, and interact effectively with complex environments.

Despite the explosion of research in this field, the landscape remains highly fragmented, with loosely defined terminologies and inconsistent taxonomies. This repository aims to bridge this gap. We distinguish Agent Memory from related concepts like RAG and Context Engineering, and provide a comprehensive overview through three unified lenses:

Forms (What Carries Memory?): Categorizing memory by its storage medium—Token-level (explicit & discrete), Parametric (implicit weights), and Latent (hidden states) .

Functions (Why Agents Need Memory?): Moving beyond simple temporal divisions to a functional taxonomy: Factual (knowledge), Experiential (insights & skills), and Working Memory (active context management) .

Dynamics (How Memory Evolves?): Dissecting the operational lifecycle into Formation (extraction), Evolution (consolidation & forgetting), and Retrieval (access strategies) .

Through this structure, we hope to provide a conceptual foundation for rethinking memory as a first-class primitive in future agentic intelligence.

💡 Concepts

Figure: Conceptual comparison of Agent Memory with LLM Memory, RAG, and Context Engineering.

📚 Paper list

Factual Memory

Token-level

[2026/01] Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning. [paper]

[2026/01] MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents. [paper]

[2026/01] EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning. [paper]

[2025/12] From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition. [paper]

[2025/12] MemVerse: Multimodal Memory for Lifelong Learning Agents. [paper]

[2025/12] MMAG: Mixed Memory-Augmented Generation for Large Language Models Applications. [paper]

[2025/12] Sophia: A Persistent Agent Framework of Artificial Life. [paper]

[2025/12] WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning. [paper]

[2025/12] Memoria: A Scalable Agentic Memory Framework for Personalized Conversational AI. [paper]

[2025/12] Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects. [paper]

[2025/11] A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents. [paper]

[2025/11] General Agentic Memory Via Deep Research. [paper]

[2025/11] O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents. [paper]

[2025/11] RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory. [paper]

[2025/11] Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles. [paper]

[2025/10] Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression. [paper]

[2025/10] D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structured Memory And Reasoning Tree. [paper]

[2025/10] WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research. [paper]

[2025/10] CAM: A Constructivist View of Agentic Memory for LLM-Based Reading Comprehension. [paper]

[2025/10] Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue. [paper]

[2025/10] LightMem: Lightweight and Efficient Memory-Augmented Generation. [paper]

[2025/10] RGMem: Renormalization Group-based Memory Evolution for Language Agent User Profile. [paper]

[2025/09] Mem-α: Learning Memory Construction via Reinforcement Learning. [paper]

[2025/09] SGMem: Sentence Graph Memory for Long-Term Conversational Agents. [paper]

[2025/09] Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science. [paper]

[2025/09] MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues. [paper]

[2025/09] Multiple Memory Systems for Enhancing the Long-term Memory of Agent. [paper]

[2025/09] Semantic Anchoring in Agentic Memory: Leveraging Linguistic Structures for Persistent Conversational Context. [paper]

[2025/09] ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning. [paper]

[2025/08] Building Self-Evolving Agents via Experience-Driven Lifelong Learning: A Framework and Benchmark. [paper]

[2025/08] Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory. [paper]

[2025/08] Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning. [paper]

[2025/08] Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory. [paper]

[2025/07] MIRIX: Multi-Agent Memory System for LLM-Based Agents. [paper]

[2025/07] Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents. [paper]

[2025/06] G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems. [paper]

[2025/06] Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance. [paper]

[2025/05] MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents. [paper]

[2025/05] Pre-training Limited Memory Language Models with Internal and External Knowledge. [paper]

[2025/05] Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding. [paper]

[2025/04] Mem0: Building production-ready ai agents with scalable long-term memory. [paper]

[2025/03] In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents. [paper]

[2025/02] SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents. [paper]

[2025/02] Zep: A Temporal Knowledge Graph Architecture for Agent Memory. [paper]

[2025/02] R{({^3})}Mem: Bridging Memory Retention and Retrieval via Reversible Compression. [paper]

[2025/02] A-MEM: Agentic Memory for LLM Agents. [paper]

[2025/02] Unveiling Privacy Risks in LLM Agent Memory. [paper]

[2025/02] Mem2Ego: Empowering Vision-Language Models with Global-to-Ego Memory for Long-Horizon Embodied Navigation. [paper]

[2024/12] AI PERSONA: Towards Life-long Personalization of LLMs. [paper]

[2024/11] OASIS: Open Agent Social Interaction Simulations with One Million Agents. [paper]

[2024/10] Video-RAG: Visually-aligned Retrieval-Augmented Long Video Comprehension. [paper]

[2024/10] Memolet: Reifying the Reuse of User-AI Conversational Memories. [paper]

[2024/10] From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs. [paper]

[2024/10] Enhancing Long Context Performance in LLMs Through Inner Loop Query Mechanism. [paper]

[2024/09] Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs. [paper]

[2024/07] Human-inspired Episodic Memory for Infinite Context LLMs. [paper]

[2024/07] Arigraph: Learning knowledge graph world models with episodic memory for llm agents. [paper]

[2024/07] ChatHaruhi: Reviving Anime Character in Reality via Large Language Model. [paper]

[2024/07] Toward Conversational Agents with Context and Time Sensitive Long-term Memory. [paper]

[2024/06] Enhancing Long-Term Memory using Hierarchical Aggregate Tree for Retrieval Augmented Generation. [paper]

[2024/06] Towards Lifelong Dialogue Agents via Timeline-based Memory Management. [paper]

[2024/05] HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models. [paper]

[2024/05] Memory Sharing for Large Language Model based Agents. [paper]

[2024/05] Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback. [paper]

[2024/04] From Local to Global: A Graph RAG Approach to Query-Focused Summarization. [paper]

[2024/03] Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation. [paper]

[2023/10] RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models. [paper]

[2023/10] MemGPT: Towards LLMs as Operating Systems. [paper]

[2023/10] GameGPT: Multi-agent Collaborative Framework for Game Development. [paper]

[2023/10] Lyfe Agents: Generative agents for low-cost real-time social interactions. [paper]

[2023/08] CALYPSO: LLMs as Dungeon Masters' Assistants. [paper]

[2023/08] MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. [paper]

[2023/08] Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations. [paper]

[2023/08] MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation. [paper]

[2023/08] Recursively summarizing enables long-term dialogue memory in large language models. [paper]

[2023/07] MovieChat: From Dense Token to Sparse Memory for Long Video Understanding. [paper]

[2023/07] S${}^3$: Social-network Simulation System with Large Language Model-Empowered Agents. [paper]

[2023/05] Prompted LLMs as Chatbot Modules for Long Open-domain Conversation. [paper]

[2023/05] RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text. [paper]

[2023/05] Memorybank: Enhancing large language models with long-term memory. [paper]

[2023/05] RET-LLM: Towards a general read-write memory for large language models. [paper]

[2023/04] Generative agents: Interactive simulacra of human behavior. [paper]

[2023/04] HuaTuo: Tuning LLaMA Model with Chinese Medical Knowledge. [paper]

[2023/04] SCM: Enhancing Large Language Model with Self-Controlled Memory Framework. [paper]

Parametric

[2025/10] MemLoRA: Distilling Expert Adapters for On-Device Memory Systems. [paper]

[2025/10] Pretraining with hierarchical memories: separating long-tail and common knowledge. [paper]

[2025/08] Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models. [paper]

[2025/08] MLP Memory: Language Modeling with Retriever-pretrained External Memory. [paper]

[2024/10] Self-Updatable Large Language Models by Integrating Context into Model Parameters. [paper]

[2024/10] AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models. [paper]

[2024/08] ELDER: Enhancing Lifelong Model Editing with Mixture-of-LoRA. [paper]

[2024/05] WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models. [paper]

[2024/03] Online Adaptation of Language Models with a Memory of Amortized Contexts. [paper]

[2024/01] Neighboring Perturbations of Knowledge Editing on Large Language Models. [paper]

[2023/11] CharacterGLM: Customizing Social Characters with Large Language Models. [paper]

[2023/10] Character-LLM: A Trainable Agent for Role-Playing. [paper]

[2021/10] Fast Model Editing at Scale. [paper]

[2021/04] Editing Factual Knowledge in Language Models. [paper]

[2020/02] K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters. [paper]

[2013/02] ELLA: An Efficient Lifelong Learning Algorithm. [paper]

Latent

[2025/09] Similarity-Distance-Magnitude Activations. [paper]

[2025/08] Towards General Continuous Memory for Vision-Language Models. [paper]

[2025/03] M+: Extending MemoryLLM with Scalable Long-Term Memory. [paper]

[2025/02] R3Mem: Bridging Memory Retention and Retrieval via Reversible Compression [paper]

[2024/07] Memory${}^3$: Language Modeling with Explicit Memory. [paper]

[2024/03] Efficient Episodic Memory Utilization of Cooperative Multi-Agent Reinforcement Learning. [paper]

[2023/10] Memoria: Resolving Fateful Forgetting Problem through Human-Inspired Memory Architecture. [paper]

[2021/12] Detecting Local Insights from Global Labels: Supervised & Zero-Shot Sequence Labeling via a Convolutional Decomposition. [paper]

Experiential Memory

Token-level

[2026/01] MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory. [paper]

[2025/12] MemEvolve: Meta-Evolution of Agent Memory Systems. [paper]

[2025/12] Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution. [paper]

[2025/12] Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects. [paper]

[2025/11] Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models. [paper]

[2025/11] FLEX: Continuous Agent Evolution via Forward Learning from Experience. [paper]

[2025/11] Scaling Agent Learning via Experience Synthesis. [paper]

[2025/11] UFO2: The Desktop AgentOS. [paper]

[2025/10] PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents. [paper]

[2025/10] Training-Free Group Relative Policy Optimization. [paper]

[2025/10] ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory. [paper]

[2025/10] H${}^2$R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents. [paper]

[2025/10] BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions. [paper]

[2025/10] LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation. [paper]

[2025/10] Alita-G: Self-Evolving Generative Agent for Agent Generation. [paper]

[2025/09] ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory. [paper]

[2025/09] Memento: Fine-tuning LLM Agents without Fine-tuning LLMs. [paper]

[2025/08] Memp: Exploring Agent Procedural Memory. [paper]

[2025/08] SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience. [paper]

[2025/07] Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving. [paper]

[2025/07] MemTool: Optimizing short-term memory management for dynamic tool calling in llm agent multi-turn conversations. [paper]

[2025/05] Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents. [paper]

[2025/05] Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution. [paper]

[2025/05] SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills. [paper]

[2025/05] LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark. [paper]

[2025/05] Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models. [paper]

[2025/04] Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory. [paper]

[2025/04] Inducing Programmatic Skills for Agentic Tasks. [paper]

[2025/03] COLA: A Scalable Multi-Agent Framework For Windows UI Task Automation. [paper]

[2025/03] Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning. [paper]

[2025/02] From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions. [paper]

[2025/02] From RAG to Memory: Non-Parametric Continual Learning for Large Language Models. [paper]

[2024/12] Planning from Imagination: Episodic Simulation and Episodic Memory for Vision-and-Language Navigation. [paper]

[2024/10] RepairAgent: An Autonomous, LLM-Based Agent for Program Repair. [paper]

[2024/09] SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities. [paper]

[2024/07] Agent Workflow Memory. [paper]

[2024/07] Fincon: A synthesized llm multi-agent system with conceptual verbal reinforcement for enhanced financial decision making. [paper]

[2024/06] Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models. [paper]

[2024/05] COLT: Towards Completeness-Oriented Tool Retrieval for Large Language Models. [paper]

[2023/11] JARVIS-1: Open-World Multi-Task Agents With Memory-Augmented Multimodal Language Models. [paper]

[2023/08] RecMind: Large Language Model Powered Agent For Recommendation. [paper]

[2023/08] ExpeL: LLM Agents Are Experiential Learners. [paper]

[2023/07] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. [paper]

[2023/05] CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models. [paper]

[2023/03] Reflexion: Language agents with verbal reinforcement learning. [paper]

[2023/02] Toolformer: Language models can teach themselves to use tools. [paper]

Parametric

[2025/11] AgentEvolver: Towards Efficient Self-Evolving Agent System. [paper]

[2025/10] Agent Learning via Early Experience. [paper]

[2025/10] Scaling Agents via Continual Pre-training. [paper]

[2024/10] ToolGen: Unified Tool Retrieval and Calling via Generation. [paper]

[2023/08] Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization. [paper]

[2023/06] A Machine with Short-Term, Episodic, and Semantic Memory Systems. [paper]

Latent

[2025/11] Auto-scaling Continuous Memory for GUI Agent. [paper]

Working Memory

Token-level

[2026/01] MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory. [paper]

[2026/01] Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents. [paper]

[2025/11] Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks. [paper]

[2025/11] IterResearch: Rethinking Long-Horizon Agents via Markovian State Reconstruction. [paper]

[2025/11] MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning. [paper]

[2025/10] AgentFold: Long-Horizon Web Agents with Proactive Context Management. [paper]

[2025/10] PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning. [paper]

[2025/10] Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval. [paper]

[2025/10] DeepAgent: A General Reasoning Agent with Scalable Toolsets. [paper]

[2025/10] ACON: Optimizing Context Compression for Long-Horizon LLM Agents. [paper]

[2025/09] ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization. [paper]

[2025/08] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management. [paper]

[2025/07] MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent. [paper]

[2024/10] Agent S: An Open Agentic Framework That Uses Computers Like a Human. [paper]

Parametric

[2024/05] Various Lengths, Constant Speed: Efficient Language Modeling with Lightning Attention. [paper]

[2024/01] Efficient Streaming Language Models with Attention Sinks. [paper]

Latent

[2025/11] VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models [paper]

[2025/09] MemGen: Weaving Generative Latent Memory for Self-Evolving Agents. [paper]

[2025/09] Conflict-Aware Soft Prompting for Retrieval-Augmented Generation. [paper]

[2025/09] MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation. [paper]

[2025/06] MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents. [paper]

[2025/05] RazorAttention: Efficient KV Cache Compression Through Retrieval Heads. [paper]

[2025/04] MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation. [paper]

[2025/04] SnapKV: LLM Knows What You are Looking for Before Generation. [paper]

[2025/03] LM2: Large Memory Models. [paper]

[2025/02] SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs. [paper]

[2025/02] Time-VLM: Exploring Multimodal Vision-Language Models for Augmented Time Series Forecasting. [paper]

[2025/02] Titans: Learning to Memorize at Test Time. [paper]

[2024/08] Augmenting Language Models with Long-Term Memory. [paper]

[2024/06] Taking a Deep Breath: Enhancing Language Modeling of Large Language Models with Sentinel Tokens. [paper]

[2024/04] Adapting Language Models to Compress Contexts. [paper]

[2024/03] Learning to Compress Prompts with Gist Tokens. [paper]

[2024/03] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time. [paper]

[2024/03] Focused Transformer: Contrastive Training for Context Scaling. [paper]

[2023/07] In-Context Autoencoder for Context Compression in a Large Language Model. [paper]

[2023/06] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models. [paper]

[2022/08] Memorizing Transformers. [paper]

[2022/07] XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model. [paper]

📖 Citation

If you find this repository helpful, a citation to our paper would be greatly appreciated:

@article{DBLP:journals/corr/abs-2512-13564,
 author = {Yuyang Hu and Shichun Liu and Yanwei Yue and Guibin Zhang and Boyang Liu and Fangyi Zhu and Jiahang Lin and Honglin Guo and Shihan Dou and Zhiheng Xi and Senjie Jin and Jiejun Tan and Yanbin Yin and Jiongnan Liu and Zeyu Zhang and Zhongxiang Sun and Yutao Zhu and Hao Sun and Boci Peng and Zhenrong Cheng and Xuanbo Fan and Jiaxin Guo and Xinlei Yu and Zhenhong Zhou and Zewen Hu and Jiahao Huo and Junhao Wang and Yuwei Niu and Yu Wang and Zhenfei Yin and Xiaobin Hu and Yue Liao and Qiankun Li and Kun Wang and Wangchunshu Zhou and Yixin Liu and Dawei Cheng and Qi Zhang and Tao Gui and Shirui Pan and Yan Zhang and Philip Torr and Zhicheng Dou and Ji{-}Rong Wen and Xuanjing Huang and Yu{-}Gang Jiang and Shuicheng Yan},
 title = {Memory in the Age of {AI} Agents},
 journal = {CoRR},
 volume = {abs/2512.13564},
 year = {2025},
 url = {https://doi.org/10.48550/arXiv.2512.13564},
 doi = {10.48550/ARXIV.2512.13564},
 eprinttype = {arXiv},
 eprint = {2512.13564},
 timestamp = {Mon, 26 Jan 2026 16:10:18 +0100},
 biburl = {https://dblp.org/rec/journals/corr/abs-2512-13564.bib},
 bibsource = {dblp computer science bibliography, https://dblp.org}
}

⭐️ Star History

About

 The paper list of "Memory in the Age of AI Agents: A Survey"
 

arxiv.org/abs/2512.13564

Topics

 agent

 memory

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Stars

1.8k
 stars

Watchers

17
 watching

Forks

77
 forks

 Report repository

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

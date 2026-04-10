---
title: LangChain Releases Deep Agents: A Structured Runtime for Planning, Memory, and Context Isolation in Multi-Step AI Agents - MarkTechPost
source_url: https://www.marktechpost.com/2026/03/15/langchain-releases-deep-agents-a-structured-runtime-for-planning-memory-and-context-isolation-in-multi-step-ai-agents
final_url: https://www.marktechpost.com/2026/03/15/langchain-releases-deep-agents-a-structured-runtime-for-planning-memory-and-context-isolation-in-multi-step-ai-agents/
status: 200
content_type: text/html; charset=UTF-8
topics: [Deep Agents (LangChain Harness for Long-Running Tasks)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:27.003539+00:00
---

# LangChain Releases Deep Agents: A Structured Runtime for Planning, Memory, and Context Isolation in Multi-Step AI Agents - MarkTechPost

## 원본 URL

https://www.marktechpost.com/2026/03/15/langchain-releases-deep-agents-a-structured-runtime-for-planning-memory-and-context-isolation-in-multi-step-ai-agents

## 추출 본문

LangChain Releases Deep Agents: A Structured Runtime for Planning, Memory, and Context Isolation in Multi-Step AI Agents - MarkTechPost

DiscordLinkedinRedditX

Home

Open Source/Weights

AI Agents

Tutorials

Voice AI

AIDeveloper44

Promotion/Sponsorship

Search

NewsHub

NewsHub

Premium Content

Read our exclusive articles

Facebook

Instagram

X

Home

Open Source/Weights

AI Agents

Tutorials

Voice AI

AIDeveloper44

Promotion/Sponsorship

NewsHub

Search

Home

Open Source/Weights

AI Agents

Tutorials

Voice AI

AIDeveloper44

Promotion/Sponsorship

HomeEditors PickAgentic AILangChain Releases Deep Agents: A Structured Runtime for Planning, Memory, and Context...

Editors Pick

Agentic AI

AI Agents

Technology

AI Shorts

AI Tool

Artificial Intelligence

Applications

New Releases

Open Source

Tech News

LangChain Releases Deep Agents: A Structured Runtime for Planning, Memory, and Context Isolation in Multi-Step AI Agents

By
Michal Sutter
 - 

March 15, 2026

Most LLM agents work well for short tool-calling loops but start to break down when the task becomes multi-step, stateful, and artifact-heavy. LangChain’s Deep Agents is designed for that gap. The project is described by LangChain as an ‘agent harness‘: a standalone library built on top of LangChain’s agent building blocks and powered by the LangGraph runtime for durable execution, streaming, and human-in-the-loop workflows. 

The important point is that Deep Agents does not introduce a new reasoning model or a new runtime separate from LangGraph. Instead, it packages a set of defaults and built-in tools around the standard tool-calling loop. LangChain team positions it as the easier starting point for developers who need agents that can plan, manage large context, delegate subtasks, and persist information across conversations, while still keeping the option to move to simpler LangChain agents or custom LangGraph workflows when needed. 

What Deep Agents Includes by Default

The Deep Agents GitHub repository lists the core components directly. These include a planning tool called 
write_todos
, filesystem tools such as 
read_file
, 
write_file
, 
edit_file
, 
ls
, 
glob
, and 
grep
, shell access through 
execute
 with sandboxing, the 
task
 tool for spawning subagents, and built-in context management features such as auto-summarization and saving large outputs to files. 

That framing matters because many agent systems leave planning, intermediate storage, and subtask delegation to the application developer. Deep Agents moves those pieces into the default runtime.

Planning and Task Decomposition

Deep Agents includes a built-in 
write_todos
 tool for planning and task decomposition. The purpose is explicit: the agent can break a complex task into discrete steps, track progress, and update the plan as new information appears.

Without a planning layer, the model tends to improvise each step from the current prompt. With 
write_todos
, the workflow becomes more structured, which is more useful for research tasks, coding sessions, or analysis jobs that unfold over several steps.

Filesystem-Based Context Management

A second core feature is the use of filesystem tools for context management. These tools allow the agent to offload large context into storage rather than keeping everything inside the active prompt window. LangChain team explicitly notes that this helps prevent context window overflow and supports variable-length tool results.

This is a more concrete design choice than vague claims about ‘memory.’ The agent can write notes, generated code, intermediate reports, or search outputs into files and retrieve them later. That makes the system more suitable for longer tasks where the output itself becomes part of the working state.

Deep Agents also supports multiple backend types for this virtual filesystem. The customization docs list 
StateBackend
, 
FilesystemBackend
, 
LocalShellBackend
, 
StoreBackend
, and 
CompositeBackend
. By default, the system uses 
StateBackend
, which stores an ephemeral filesystem in LangGraph state for a single thread.

Subagents and Context Isolation

Deep Agents also includes a built-in 
task
 tool for subagent spawning. This tool allows the main agent to create specialized subagents for context isolation, keeping the main thread cleaner while letting the system go deeper on specific subtasks.

This is one of the cleaner answers to a common failure mode in agent systems. Once a single thread accumulates too many objectives, tool outputs, and temporary decisions, model quality often drops. Splitting work into subagents reduces that overload and makes the orchestration path easier to debug. 

Long-Term Memory and LangGraph Integration

The Deep Agents GitHub repository also describe long-term memory as a built-in capability. Deep Agents can be extended with persistent memory across threads using LangGraph’s Memory Store, allowing the agent to save and retrieve information from previous conversations. 

On the implementation side, Deep Agents stays fully inside the LangGraph execution model. The customization docs specify that 
create_deep_agent(...)
 returns a 
CompiledStateGraph
. The resulting graph can be used with standard LangGraph features such as streaming, Studio, and checkpointers.

Deep Agents is not a parallel abstraction layer that blocks access to runtime features; it is a prebuilt graph with defaults.

Deployment Details

For deployment, the official quickstart shows a minimal Python setup: install 
deepagents
 plus a search provider such as 
tavily-python
, export your model API key and search API key, define a search tool, and then create the agent with 
create_deep_agent(...)
 using a tool-calling model. The docs note that Deep Agents requires tool calling support, and the example workflow is to initialize the agent with your tools and 
system_prompt
, then run it with 
agent.invoke(...)
. LangChain team also points developers toward LangGraph deployment options for production, which fits because Deep Agents runs on the LangGraph runtime and supports built-in streaming for observing execution.

Copy CodeCopiedUse a different Browser

# pip install -qU deepagents
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
 """Get weather for a given city."""
 return f"It's always sunny in {city}!"

agent = create_deep_agent(
 tools=[get_weather],
 system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
 {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

Key Takeaways

Deep Agents is an agent harness built on LangChain and the LangGraph runtime. 

It includes built-in planning through the 
write_todos
 tool for multi-step task decomposition.

It uses filesystem tools to manage large context and reduce prompt-window pressure.

It can spawn subagents with isolated context using the built-in 
task
 tool. 

It supports persistent memory across threads through LangGraph’s Memory Store. 

Check out Repo and Docs. Also, feel free to follow us on Twitter and don’t forget to join our 120k+ ML SubReddit and Subscribe to our Newsletter. Wait! are you on telegram? now you can join us on telegram as well.

 Michal Sutter

+ postsBio

Michal Sutter is a data science professional with a Master of Science in Data Science from the University of Padova. With a solid foundation in statistical analysis, machine learning, and data engineering, Michal excels at transforming complex datasets into actionable insights.

Michal Sutter

A Comprehensive Implementation Guide to ModelScope for Model Search, Inference, Fine-Tuning, Evaluation, and Export

Michal Sutter

How to Combine Google Search, Google Maps, and Custom Functions in a Single Gemini API Call With Context Circulation, Parallel Tool IDs, and Multi-Step Agentic Chains

Michal Sutter

How to Deploy Open WebUI with Secure OpenAI API Integration, Public Tunneling, and Browser-Based Chat Access

Michal Sutter

Netflix AI Team Just Open-Sourced VOID: an AI Model That Erases Objects From Videos — Physics and All

Michal Sutter

Google DeepMind’s Research Lets an LLM Rewrite Its Own Game Theory Algorithms — And It Outperformed the Experts

Michal Sutter

Hugging Face Releases TRL v1.0: A Unified Post-Training Stack for SFT, Reward Modeling, DPO, and GRPO Workflows

Michal Sutter

Google AI Releases Veo 3.1 Lite: Giving Developers Low Cost High Speed Video Generation via The Gemini API

Michal Sutter

Agent-Infra Releases AIO Sandbox: An All-in-One Runtime for AI Agents with Browser, Shell, Shared Filesystem, and MCP

Michal Sutter

Google-Agent vs Googlebot: Google Defines the Technical Boundary Between User Triggered AI Access and Search Crawling Systems Today

Michal Sutter

A Coding Guide to Exploring nanobot’s Full Agent Pipeline, from Wiring Up Tools and Memory to Skills, Subagents, and Cron Scheduling

Michal Sutter

An Implementation of IWE’s Context Bridge as an AI-Powered Knowledge Graph with Agentic RAG, OpenAI Function Calling, and Graph Traversal

Michal Sutter

Meta Releases TRIBE v2: A Brain Encoding Model That Predicts fMRI Responses Across Video, Audio, and Text Stimuli

Michal Sutter

Tencent AI Open Sources Covo-Audio: A 7B Speech Language Model and Inference Pipeline for Real-Time Audio Conversations and Reasoning

Michal Sutter

A Coding Implementation to Design Self-Evolving Skill Engine with OpenSpace for Skill Learning, Token Efficiency, and Collective Intelligence

Michal Sutter

Luma Labs Launches Uni-1: The Autoregressive Transformer Model that Reasons through Intentions Before Generating Images

Michal Sutter

Meet GitAgent: The Docker for AI Agents that is Finally Solving the Fragmentation between LangChain, AutoGen, and Claude Code

Michal Sutter

A Coding Implementation for Building and Analyzing Crystal Structures Using Pymatgen for Symmetry Analysis, Phase Diagrams, Surface Generation, and Materials Project Integration

Michal Sutter

A Coding Implementation Showcasing ClawTeam’s Multi-Agent Swarm Orchestration with OpenAI Function Calling

Michal Sutter

A Coding Guide to Implement Advanced Differential Equation Solvers, Stochastic Simulations, and Neural Ordinary Differential Equations Using Diffrax and JAX

Michal Sutter

Baidu Qianfan Team Releases Qianfan-OCR: A 4B-Parameter Unified Document Intelligence Model

Michal Sutter

Google AI Releases WAXAL: A Multilingual African Speech Dataset for Training Automatic Speech Recognition and Text-to-Speech Models

Michal Sutter

Google DeepMind Introduces Aletheia: The AI Agent Moving from Math Competitions to Fully Autonomous Professional Research Discoveries

Michal Sutter

Google AI Introduces ‘Groundsource’: A New Methodology that Uses Gemini Model to Transform Unstructured Global News into Actionable, Historical Data

Michal Sutter

How to Build a Self-Designing Meta-Agent That Automatically Constructs, Instantiates, and Refines Task-Specific AI Agents

Michal Sutter

A Coding Guide to Build a Complete Single Cell RNA Sequencing Analysis Pipeline Using Scanpy for Clustering Visualization and Cell Type Annotation

Michal Sutter

How to Build Progress Monitoring Using Advanced tqdm for Async, Parallel, Pandas, Logging, and High-Performance Workflows

Michal Sutter

Google Launches TensorFlow 2.21 And LiteRT: Faster GPU Performance, New NPU Acceleration, And Seamless PyTorch Edge Deployment Upgrades

Michal Sutter

OpenAI Introduces Codex Security in Research Preview for Context-Aware Vulnerability Detection, Validation, and Patch Generation Across Codebases

Michal Sutter

A Coding Guide to Build a Scalable End-to-End Machine Learning Data Pipeline Using Daft for High-Performance Structured and Image Data Processing

Michal Sutter

How to Build an EverMem-Style Persistent AI Agent OS with Hierarchical Memory, FAISS Vector Retrieval, SQLite Storage, and Automated Memory Consolidation

Michal Sutter

Meet NullClaw: The 678 KB Zig AI Agent Framework Running on 1 MB RAM and Booting in Two Milliseconds

Michal Sutter

How to Build an Explainable AI Analysis Pipeline Using SHAP-IQ to Understand Feature Importance, Interaction Effects, and Model Decision Breakdown

Michal Sutter

A Complete End-to-End Coding Guide to MLflow Experiment Tracking, Hyperparameter Optimization, Model Evaluation, and Live Model Deployment

Michal Sutter

A Coding Implementation to Build a Hierarchical Planner AI Agent Using Open-Source LLMs with Tool Execution and Structured Multi-Agent Reasoning

Michal Sutter

Microsoft Research Introduces CORPGEN To Manage Multi Horizon Tasks For Autonomous AI Agents Using Hierarchical Planning and Memory

Michal Sutter

Google AI Just Released Nano-Banana 2: The New AI Model Featuring Advanced Subject Consistency and Sub-Second 4K Image Synthesis Performance

Michal Sutter

How to Build an Elastic Vector Database with Consistent Hashing, Sharding, and Live Ring Visualization for RAG Systems

Michal Sutter

Beyond Simple API Requests: How OpenAI’s WebSocket Mode Changes the Game for Low Latency Voice Powered AI Experiences

Michal Sutter

VectifyAI Launches Mafin 2.5 and PageIndex: Achieving 98.7% Financial RAG Accuracy with a New Open-Source Vectorless Tree Indexing.

Michal Sutter

A Coding Guide to Instrumenting, Tracing, and Evaluating LLM Applications Using TruLens and OpenAI Models

Michal Sutter

How to Build Transparent AI Agents: Traceable Decision-Making with Audit Trails and Human Gates

Michal Sutter

[Tutorial] Building a Visual Document Retrieval Pipeline with ColPali and Late Interaction Scoring

Michal Sutter

Google Introduces Jetpack Compose Glimmer: A New Spatial UI Framework Designed Specifically for the Next Generation of AI Glasses

Michal Sutter

Agoda Open Sources APIAgent to Convert Any REST pr GraphQL API into an MCP Server with Zero Code

Michal Sutter

How to Build Human-in-the-Loop Plan-and-Execute AI Agents with Explicit User Approval Using LangGraph and Streamlit

Michal Sutter

Google DeepMind Proposes New Framework for Intelligent AI Delegation to Secure the Emerging Agentic Web for Future Economies

Michal Sutter

Moonshot AI Launches Kimi Claw: Native OpenClaw on Kimi.com with 5,000 Community Skills and 40GB Cloud Storage Now

Michal Sutter

Meet ‘Kani-TTS-2’: A 400M Param Open Source Text-to-Speech Model that Runs in 3GB VRAM with Voice Cloning Support

Michal Sutter

Google AI Introduces the WebMCP to Enable Direct and Structured Website Interactions for New AI Agents

Michal Sutter

[In-Depth Guide] The Complete CTGAN + SDV Pipeline for High-Fidelity Synthetic Data

Michal Sutter

Is This AGI? Google’s Gemini 3 Deep Think Shatters Humanity’s Last Exam And Hits 84.6% On ARC-AGI-2 Performance Today

Michal Sutter

Meet OAT: The New Action Tokenizer Bringing LLM-Style Scaling and Flexible, Anytime Inference to the Robotics World

Michal Sutter

Waymo Introduces the Waymo World Model: A New Frontier Simulator Model for Autonomous Driving and Built on Top of Genie 3

Michal Sutter

Mistral AI Launches Voxtral Transcribe 2: Pairing Batch Diarization And Open Realtime ASR For Multilingual Production Workloads At Scale

Michal Sutter

Google Introduces Agentic Vision in Gemini 3 Flash for Active Image Understanding

Michal Sutter

Google Releases Conductor: a context driven Gemini CLI extension that stores knowledge as Markdown and orchestrates agentic workflows

Michal Sutter

Microsoft Unveils Maia 200, An FP4 and FP8 Optimized AI Inference Accelerator for Azure Datacenters

Michal Sutter

DeepSeek AI Releases DeepSeek-OCR 2 with Causal Visual Flow Encoder for Layout Aware Document Understanding

Michal Sutter

Alibaba Introduces Qwen3-Max-Thinking, a Test Time Scaled Reasoning Model with Native Tool Use Powering Agentic Workloads

Michal Sutter

Tencent Hunyuan Releases HPC-Ops: A High Performance LLM Inference Operator Library

Michal Sutter

DSGym Offers a Reusable Container Based Substrate for Building and Benchmarking Data Science Agents

Michal Sutter

What is Clawdbot? How a Local First Agent Stack Turns Chats into Real Automations

Michal Sutter

GitHub Releases Copilot-SDK to Embed Its Agentic Runtime in Any App

Michal Sutter

Salesforce AI Introduces FOFPred: A Language-Driven Future Optical Flow Prediction Framework that Enables Improved Robot Control and Video Generation

Michal Sutter

Zhipu AI Releases GLM-4.7-Flash: A 30B-A3B MoE Model for Efficient Local Coding and Agents

Michal Sutter

A Coding Guide to Understanding How Retries Trigger Failure Cascades in RPC and Event-Driven Architectures

Michal Sutter

Vercel Releases Agent Skills: A Package Manager For AI Coding Agents With 10 Years of React and Next.js Optimisation Rules

Michal Sutter

Black Forest Labs Releases FLUX.2 [klein]: Compact Flow Models for Interactive Visual Intelligence

Michal Sutter

Meet SETA: Open Source Training Reinforcement Learning Environments for Terminal Agents with 400 Tasks and CAMEL Toolkit

Michal Sutter

A Coding Implementation to Build a Unified Apache Beam Pipeline Demonstrating Batch and Stream Processing with Event-Time Windowing Using DirectRunner

Michal Sutter

Tencent Researchers Release Tencent HY-MT1.5: A New Translation Models Featuring 1.8B and 7B Models Designed for Seamless on-Device and Cloud Deployment

Michal Sutter

How Cloudflare’s tokio-quiche Makes QUIC and HTTP/3 a First Class Citizen in Rust Backends

Michal Sutter

How to Build a Robust Multi-Agent Pipeline Using CAMEL with Planning, Web-Augmented Reasoning, Critique, and Persistent Memory

Michal Sutter

NVIDIA AI Researchers Release NitroGen: An Open Vision Action Foundation Model For Generalist Gaming Agents

Michal Sutter

This AI Paper from Stanford and Harvard Explains Why Most ‘Agentic AI’ Systems Feel Impressive in Demos and then Completely Fall Apart in Real Use

Michal Sutter

Google DeepMind Researchers Release Gemma Scope 2 as a Full Stack Interpretability Suite for Gemma 3 Models

Michal Sutter

How to Build a Fully Autonomous Local Fleet-Maintenance Analysis Agent Using SmolAgents and Qwen Model

Michal Sutter

Mistral AI Releases OCR 3: A Smaller Optical Character Recognition (OCR) Model for Structured Document AI at Scale

Michal Sutter

Nanbeige4-3B-Thinking: How a 23T Token Pipeline Pushes 3B Models Past 30B Class Reasoning

Michal Sutter

The Machine Learning Divide: Marktechpost’s Latest ML Global Impact Report Reveals Geographic Asymmetry Between ML Tool Origins and Research Adoption

Michal Sutter

Google LiteRT NeuroPilot Stack Turns MediaTek Dimensity NPUs into First Class Targets for on Device LLMs

Michal Sutter

From Transformers to Associative Memory, How Titans and MIRAS Rethink Long Context Modeling

Michal Sutter

Google Colab Integrates KaggleHub for One Click Access to Kaggle Datasets, Models and Competitions

Michal Sutter

OpenAGI Foundation Launches Lux: A Foundation Computer Use Model that Tops Online Mind2Web with OSGym At Scale

Michal Sutter

Google DeepMind Researchers Introduce Evo-Memory Benchmark and ReMem Framework for Experience Reuse in LLM Agents

Michal Sutter

Meta AI Researchers Introduce Matrix: A Ray Native a Decentralized Framework for Multi Agent Synthetic Data Generation

Michal Sutter

Black Forest Labs Releases FLUX.2: A 32B Flow Matching Transformer for Production Image Pipelines

Michal Sutter

Agent0: A Fully Autonomous AI Framework that Evolves High-Performing Agents without External Data through Multi-Step Co-Evolution

Michal Sutter

Google DeepMind Introduces Nano Banana Pro: the Gemini 3 Pro Image Model for Text Accurate and Studio Grade Visuals

Michal Sutter

Allen Institute for AI (AI2) Introduces Olmo 3: An Open Source 7B and 32B LLM Family Built on the Dolma 3 and Dolci Stack

Michal Sutter

vLLM vs TensorRT-LLM vs HF TGI vs LMDeploy, A Deep Technical Comparison for Production LLM Inference

Michal Sutter

OpenAI Debuts GPT-5.1-Codex-Max, a Long-Horizon Agentic Coding Model With Compaction for Multi-Window Workflows

Michal Sutter

Google Antigravity Makes the IDE a Control Plane for Agentic Coding

Michal Sutter

xAI’s Grok 4.1 Pushes Toward Higher Emotional Intelligence, Lower Hallucinations and Tighter Safety Controls

Michal Sutter

Google DeepMind’s WeatherNext 2 Uses Functional Generative Networks For 8x Faster Probabilistic Weather Forecasts

Michal Sutter

Comparing the Top 4 Agentic AI Browsers in 2025: Atlas vs Copilot Mode vs Dia vs Comet

Michal Sutter

OpenAI Researchers Train Weight Sparse Transformers to Expose Interpretable Circuits

Michal Sutter

Comparing the Top 6 Agent-Native Rails for the Agentic Internet: MCP, A2A, AP2, ACP, x402, and Kite

Michal Sutter

OpenAI Introduces GPT-5.1: Combining Adaptive Reasoning, Account Level Personalization, And Updated Safety Metrics In The GPT-5 Stack

Michal Sutter

Meta AI Releases Omnilingual ASR: A Suite of Open-Source Multilingual Speech Recognition Models for 1600+ Languages

Michal Sutter

Moonshot AI Releases Kosong: The LLM Abstraction Layer that Powers Kimi CLI

Michal Sutter

Comparing Memory Systems for LLM Agents: Vector, Graph, and Event Logs

Michal Sutter

Meet Kosmos: An AI Scientist that Automates Data-Driven Discovery

Michal Sutter

Anthropic Turns MCP Agents Into Code First Systems With ‘Code Execution With MCP’ Approach

Michal Sutter

Why Spatial Supersensing is Emerging as the Core Capability for Multimodal AI Systems?

Michal Sutter

Comparing the Top 6 Inference Runtimes for LLM Serving in 2025

Michal Sutter

OpenAI Introduces IndQA: A Culture Aware Benchmark For Indian Languages

Michal Sutter

Comparing the Top 7 Large Language Models LLMs/Systems for Coding in 2025

Michal Sutter

Anyscale and NovaSky Team Releases SkyRL tx v0.1.0: Bringing Tinker Compatible Reinforcement Learning RL Engine To Local GPU Clusters

Michal Sutter

LongCat-Flash-Omni: A SOTA Open-Source Omni-Modal Model with 560B Parameters with 27B activated, Excelling at Real-Time Audio-Visual Interaction

Michal Sutter

Comparing the Top 6 OCR (Optical Character Recognition) Models/Systems in 2025

Michal Sutter

Anthropic’s New Research Shows Claude can Detect Injected Concepts, but only in Controlled Layers

Michal Sutter

OpenAI Releases Research Preview of ‘gpt-oss-safeguard’: Two Open-Weight Reasoning Models for Safety Classification Tasks

Michal Sutter

Microsoft Releases Agent Lightning: A New AI Framework that Enables Reinforcement Learning (RL)-based Training of LLMs for Any AI Agent

Michal Sutter

MiniMax Releases MiniMax M2: A Mini Open Model Built for Max Coding and Agentic Workflows at 8% Claude Sonnet Price and ~2x Faster

Michal Sutter

Google vs OpenAI vs Anthropic: The Agentic AI Arms Race Breakdown

Michal Sutter

Liquid AI’s LFM2-VL-3B Brings a 3B Parameter Vision Language Model (VLM) to Edge-Class Devices

Michal Sutter

UltraCUA: A Foundation Computer-Use Agents Model that Bridges the Gap between General-Purpose GUI Agents and Specialized API-based Agents

Michal Sutter

Anthrogen Introduces Odyssey: A 102B Parameter Protein Language Model that Replaces Attention with Consensus and Trains with Discrete Diffusion

Michal Sutter

OpenAI Introduces ChatGPT Atlas: A Chromium-based browser with a built-in AI agent

Michal Sutter

Google AI Research Releases DeepSomatic: A New AI Model that Identifies Cancer Cell Genetic Variants

Michal Sutter

Weak-for-Strong (W4S): A Novel Reinforcement Learning Algorithm that Trains a weak Meta Agent to Design Agentic Workflows with Stronger LLMs

Michal Sutter

Kong Releases Volcano: A TypeScript, MCP-native SDK for Building Production Ready AI Agents with LLM Reasoning and Real-World actions

Michal Sutter

Google AI Releases C2S-Scale 27B Model that Translate Complex Single-Cell Gene Expression Data into ‘cell sentences’ that LLMs can Understand

Michal Sutter

7 LLM Generation Parameters—What They Do and How to Tune Them?

Michal Sutter

Meta’s ARE + Gaia2 Set a New Bar for AI Agent Evaluation under Asynchronous, Event-Driven Conditions

Michal Sutter

Microsoft AI Debuts MAI-Image-1: An In-House Text-to-Image Model that Enters LMArena’s Top-10

Michal Sutter

Google Open-Sources an MCP Server for the Google Ads API, Bringing LLM-Native Access to Ads Data

Michal Sutter

What are ‘Computer-Use Agents’? From Web to OS—A Technical Explainer

Michal Sutter

RA3: Mid-Training with Temporal Action Abstractions for Faster Reinforcement Learning (RL) Post-Training in Code LLMs

Michal Sutter

Model Context Protocol (MCP) vs Function Calling vs OpenAPI Tools — When to Use Each?

Michal Sutter

Google AI Introduces Gemini 2.5 ‘Computer Use’ (Preview): A Browser-Control Model to Power AI Agents to Interact with User Interfaces

Michal Sutter

OpenAI Debuts Agent Builder and AgentKit: A Visual-First Stack for Building, Deploying, and Evaluating AI Agents

Michal Sutter

StreamTensor: A PyTorch-to-Accelerator Compiler that Streams LLM Intermediates Across FPGA Dataflows

Michal Sutter

How to Evaluate Voice Agents in 2025: Beyond Automatic Speech Recognition (ASR) and Word Error Rate (WER) to Task Success, Barge-In, and Hallucination-Under-Noise

Michal Sutter

This AI Paper Proposes a Novel Dual-Branch Encoder-Decoder Architecture for Unsupervised Speech Enhancement (SE)

Michal Sutter

Neuphonic Open-Sources NeuTTS Air: A 748M-Parameter On-Device Speech Language Model with Instant Voice Cloning

Michal Sutter

Thinking Machines Launches Tinker: A Low-Level Training API that Abstracts Distributed LLM Fine-Tuning without Hiding the Knobs

Michal Sutter

MLPerf Inference v5.1 (2025): Results Explained for GPUs, CPUs, and AI Accelerators

Michal Sutter

The Role of Model Context Protocol (MCP) in Generative AI Security and Red Teaming

Michal Sutter

OpenAI Launches Sora 2 and a Consent-Gated Sora iOS App

Michal Sutter

Delinea Released an MCP Server to Put Guardrails Around AI Agents Credential Access

Michal Sutter

Anthropic Launches Claude Sonnet 4.5 with New Coding and Agentic State-of-the-Art Results

Michal Sutter

Top 10 Local LLMs (2025): Context Windows, VRAM Targets, and Licenses Compared

Michal Sutter

The Latest Gemini 2.5 Flash-Lite Preview is Now the Fastest Proprietary Model (External Tests) and 50% Fewer Output Tokens

Michal Sutter

Google AI Ships a Model Context Protocol (MCP) Server for Data Commons, Giving AI Agents First-Class Access to Public Stats

Michal Sutter

OpenAI Releases ChatGPT ‘Pulse’: Proactive, Personalized Daily Briefings for Pro Users

Michal Sutter

OpenAI Introduces GDPval: A New Evaluation Suite that Measures AI on Real-World Economically Valuable Tasks

Michal Sutter

Vision-RAG vs Text-RAG: A Technical Comparison for Enterprise Search

Michal Sutter

Microsoft Brings MCP to Azure Logic Apps (Standard) in Public Preview, Turning Connectors into Agent Tools

Michal Sutter

Top 15 Model Context Protocol (MCP) Servers for Frontend Developers (2025)

Michal Sutter

LLM-as-a-Judge: Where Do Its Signals Break, When Do They Hold, and What Should “Evaluation” Mean?

Michal Sutter

An Internet of AI Agents? Coral Protocol Introduces Coral v1: An MCP-Native Runtime and Registry for Cross-Framework AI Agents

Michal Sutter

Xiaomi Released MiMo-Audio, a 7B Speech Language Model Trained on 100M+ Hours with High-Fidelity Discrete Tokens

Michal Sutter

Google’s Sensible Agent Reframes Augmented Reality (AR) Assistance as a Coupled “what+how” Decision—So What does that Change?

Michal Sutter

Top Computer Vision CV Blogs & News Websites (2025)

Michal Sutter

Physical AI: Bridging Robotics, Material Science, and Artificial Intelligence for Next-Gen Embodied Systems

Michal Sutter

MIT’s LEGO: A Compiler for AI Chips that Auto-Generates Fast, Efficient Spatial Accelerators

Michal Sutter

Meta AI Researchers Release MapAnything: An End-to-End Transformer Architecture that Directly Regresses Factored, Metric 3D Scene Geometry

Michal Sutter

Ai2 Researchers are Changing the Benchmarking Game by Introducing Fluid Benchmarking that Enhances Evaluation along Several Dimensions

Michal Sutter

Google AI Ships TimesFM-2.5: Smaller, Longer-Context Foundation Model That Now Leads GIFT-Eval (Zero-Shot Forecasting)

Michal Sutter

Stanford Researchers Introduced MedAgentBench: A Real-World Benchmark for Healthcare AI Agents

Michal Sutter

OpenAI Introduces GPT-5-Codex: An Advanced Version of GPT-5 Further Optimized for Agentic Coding in Codex

Michal Sutter

Software Frameworks Optimized for GPUs in AI: CUDA, ROCm, Triton, TensorRT—Compiler Paths and Performance Implications

Michal Sutter

Top 12 Robotics AI Blogs/NewsWebsites 2025

Michal Sutter

Deepdub Introduces Lightning 2.5: A Real-Time AI Voice Model With 2.8x Throughput Gains for Scalable AI Agents and Enterprise AI

Michal Sutter

TwinMind Introduces Ear-3 Model: A New Voice AI Model that Sets New Industry Records in Accuracy, Speaker Labeling, Languages and Price

Michal Sutter

What are Optical Character Recognition (OCR) Models? Top Open-Source OCR Models

Michal Sutter

OpenAI Adds Full MCP Tool Support in ChatGPT Developer Mode: Enabling Write Actions, Workflow Automation, and Enterprise Integrations

Michal Sutter

Top 7 Model Context Protocol (MCP) Servers for Vibe Coding

Michal Sutter

ParaThinker: Scaling LLM Test-Time Compute with Native Parallel Thinking to Overcome Tunnel Vision in Sequential Reasoning

Michal Sutter

A New MIT Study Shows Reinforcement Learning Minimizes Catastrophic Forgetting Compared to Supervised Fine-Tuning

Michal Sutter

Alibaba AI Unveils Qwen3-Max Preview: A Trillion-Parameter Qwen Model with Super Fast Speed and Quality

Michal Sutter

Meet Chatterbox Multilingual: An Open-Source Zero-Shot Text To Speech (TTS) Multilingual Model with Emotion Control and Watermarking

Michal Sutter

Biomni-R0: New Agentic LLMs Trained End-to-End with Multi-Turn Reinforcement Learning for Expert-Level Intelligence in Biomedical Research

Michal Sutter

AI and the Brain: How DINOv3 Models Reveal Insights into Human Visual Processing

Michal Sutter

15 Most Relevant Operating Principles for Enterprise AI (2025)

Michal Sutter

What is AI Agent Observability? Top 7 Best Practices for Reliable AI

Michal Sutter

Chunking vs. Tokenization: Key Differences in AI Text Processing

Michal Sutter

Accenture Research Introduce MCP-Bench: A Large-Scale Benchmark that Evaluates LLM Agents in Complex Real-World Tasks via MCP Servers

Michal Sutter

Top 20 Voice AI Blogs and News Websites 2025: The Ultimate Resource Guide

Michal Sutter

The State of Voice AI in 2025: Trends, Breakthroughs, and Market Leaders

Michal Sutter

OpenAI Releases an Advanced Speech-to-Speech Model and New Realtime API Capabilities including MCP Server Support, Image Input, and SIP Phone Calling Support

Michal Sutter

Australia’s Large Language Model Landscape: Technical Assessment

Michal Sutter

What is Agentic RAG? Use Cases and Top Agentic RAG Tools (2025)

Michal Sutter

The Evolution of AI Protocols: Why Model Context Protocol (MCP) Could Become the New HTTP for AI

Michal Sutter

Google AI’s New Regression Language Model (RLM) Framework Enables LLMs to Predict Industrial System Performance Directly from Raw Text Data

Michal Sutter

What is MLSecOps(Secure CI/CD for Machine Learning)?: Top MLSecOps Tools (2025)

Michal Sutter

Your LLM is 5x Slower Than It Should Be. The Reason? Pessimism—and Stanford Researchers Just Showed How to Fix It

Michal Sutter

How Do GPUs and TPUs Differ in Training Large Transformer Models? Top GPUs and TPUs with Benchmark

Michal Sutter

What is a Database? Modern Database Types, Examples, and Applications (2025)

Michal Sutter

What is a Voice Agent in AI? Top 9 Voice Agent Platforms to Know (2025)

Michal Sutter

Large Language Models LLMs vs. Small Language Models SLMs for Financial Institutions: A 2025 Practical Enterprise AI Guide

Michal Sutter

Native RAG vs. Agentic RAG: Which Approach Advances Enterprise AI Decision-Making?

Michal Sutter

Top 10 AI Blogs and News Websites for AI Developers and Engineers in 2025

Michal Sutter

What Is Speaker Diarization? A 2025 Technical Guide: Top 9 Speaker Diarization Libraries and APIs in 2025

Michal Sutter

What is DeepSeek-V3.1 and Why is Everyone Talking About It?

Michal Sutter

Meet South Korea’s LLM Powerhouses: HyperClova, AX, Solar Pro, and More

Michal Sutter

Migrating to Model Context Protocol (MCP): An Adapter-First Playbook

Michal Sutter

Hello, AI Formulas: Why =COPILOT() Is the Biggest Excel Upgrade in Years

Michal Sutter

Emerging Trends in AI Cybersecurity Defense: What’s Shaping 2025? Top AI Security Tools

Michal Sutter

BlackRock Introduces AlphaAgents: Advancing Equity Portfolio Construction with Multi-Agent LLM Collaboration

Michal Sutter

Master Vibe Coding: Pros, Cons, and Best Practices for Data Engineers

Michal Sutter

Is Model Context Protocol MCP the Missing Standard in AI Infrastructure?

Michal Sutter

What is AI Inference? A Technical Deep Dive and Top 9 AI Inference Providers (2025 Edition)

Michal Sutter

Hugging Face Unveils AI Sheets: A Free, Open-Source No-Code Toolkit for LLM-Powered Datasets

Michal Sutter

What Is AI Red Teaming? Top 18 AI Red Teaming Tools (2025)

Michal Sutter

From Deployment to Scale: 11 Foundational Enterprise AI Concepts for Modern Businesses

Michal Sutter

Meet dots.ocr: A New 1.7B Vision-Language Model that Achieves SOTA Performance on Multilingual Document Parsing

Michal Sutter

Amazon Unveils Bedrock AgentCore Gateway: Redefining Enterprise AI Agent Tool Integration

Michal Sutter

Top 6 Model Context Protocol (MCP) News Blogs (2025 Update)

Michal Sutter

Top 12 API Testing Tools For 2025

Michal Sutter

Top 10 AI Agent and Agentic AI News Blogs (2025 Update)

Michal Sutter

Why Docker Matters for Artificial Intelligence AI Stack: Reproducibility, Portability, and Environment Parity

Michal Sutter

Mistral AI Unveils Mistral Medium 3.1: Enhancing AI with Superior Performance and Usability

Michal Sutter

Case Studies: Real-World Applications of Context Engineering

Michal Sutter

NVIDIA AI Introduces End-to-End AI Stack, Cosmos Physical AI Models and New Omniverse Libraries for Advanced Robotics

Michal Sutter

The Best Chinese Open Agentic/Reasoning Models (2025): Expanded Review, Comparative Insights & Use Cases

Michal Sutter

From 100,000 to Under 500 Labels: How Google AI Cuts LLM Training Data by Orders of Magnitude

Michal Sutter

9 Agentic AI Workflow Patterns Transforming AI Agents in 2025

Michal Sutter

FAQs: Everything You Need to Know About AI Agents in 2025

Michal Sutter

Technical Deep Dive: Automating LLM Agent Mastery for Any MCP Server with MCP- RL and ART

Michal Sutter

Alibaba Qwen Unveils Qwen3-4B-Instruct-2507 and Qwen3-4B-Thinking-2507: Refreshing the Importance of Small Language Models

Michal Sutter

Proxy Servers Explained: Types, Use Cases & Trends in 2025 [Technical Deep Dive]

Michal Sutter

NVIDIA XGBoost 3.0: Training Terabyte-Scale Datasets with Grace Hopper Superchip

Michal Sutter

MoE Architecture Comparison: Qwen3 30B-A3B vs. GPT-OSS 20B

Michal Sutter

Google DeepMind Introduces Genie 3: A General Purpose World Model that can Generate an Unprecedented Diversity of Interactive Environments

Michal Sutter

Model Context Protocol (MCP) FAQs: Everything You Need to Know in 2025

Michal Sutter

Now It’s Claude’s World: How Anthropic Overtook OpenAI in the Enterprise AI Race

Michal Sutter

7 Essential Layers for Building Real-World AI Agents in 2025: A Comprehensive Framework

Michal Sutter

A Technical Roadmap to Context Engineering in LLMs: Mechanisms, Benchmarks, and Open Challenges

Michal Sutter

The Ultimate Guide to CPUs, GPUs, NPUs, and TPUs for AI/ML: Performance, Use Cases, and Key Differences

Michal Sutter

Falcon LLM Team Releases Falcon-H1 Technical Report: A Hybrid Attention–SSM Model That Rivals 70B LLMs

Michal Sutter

The Ultimate 2025 Guide to Coding LLM Benchmarks and Performance Metrics

Michal Sutter

Next-Gen Privacy: How AI Is Transforming Secure Browsing and VPN Technologies (2025 Data-Driven Deep Dive)

Michal Sutter

Is Vibe Coding Safe for Startups? A Technical Risk Audit Based on Real-World Use Cases

Michal Sutter

9 Open Source Cursor Alternatives You Should Use in 2025

Michal Sutter

Microsoft Edge Launches Copilot Mode to Redefine Web Browsing for the AI Era

Michal Sutter

Key Factors That Drive Successful MCP Implementation and Adoption

Michal Sutter

How Memory Transforms AI Agents: Insights and Leading Solutions in 2025

Michal Sutter

NVIDIA AI Releases GraspGen: A Diffusion-Based Framework for 6-DOF Grasping in Robotics

Michal Sutter

Google DeepMind Introduces Aeneas: AI-Powered Contextualization and Restoration of Ancient Latin Inscriptions

Michal Sutter

GitHub Introduces Vibe Coding with Spark: Revolutionizing Intelligent App Development in a Flash

Michal Sutter

Google Researchers Introduced LSM-2 with Adaptive and Inherited Masking (AIM): Enabling Direct Learning from Incomplete Wearable Data

Michal Sutter

7 MCP Server Best Practices for Scalable AI Integrations in 2025

Michal Sutter

AI Guardrails and Trustworthy LLM Evaluation: Building Responsible AI Systems

Michal Sutter

Top 15+ Most Affordable Proxy Providers 2025

Michal Sutter

The Ultimate Guide to Vibe Coding: Benefits, Tools, and Future Trends

Michal Sutter

Model Context Protocol (MCP) for Enterprises: Secure Integration with AWS, Azure, and Google Cloud- 2025 Update

Michal Sutter

Maybe Physics-Based AI Is the Right Approach: Revisiting the Foundations of Intelligence

Michal Sutter

The Definitive Guide to AI Agents: Architectures, Frameworks, and Real-World Applications (2025)

Michal Sutter

OpenAI Introduces ChatGPT Agent: From Research to Real-World Automation

Michal Sutter

How to Connect Google Colab with Google Drive (2025 Detailed & Updated Guide)

Michal Sutter

50+ Model Context Protocol (MCP) Servers Worth Exploring

Previous articleZhipu AI Introduces GLM-OCR: A 0.9B Multimodal OCR Model for Document Parsing and Key Information Extraction (KIE)

Next articleMeet OpenViking: An Open-Source Context Database that Brings Filesystem-Based Memory and Retrieval to AI Agent Systems like OpenClaw

Michal Sutter

RELATED ARTICLESMORE FROM AUTHOR

Meta Superintelligence Lab Releases Muse Spark: A Multimodal Reasoning Model With Thought Compression and Parallel Agents

Sigmoid vs ReLU Activation Functions: The Inference Cost of Losing Geometric Context

A Coding Guide to Build Advanced Document Intelligence Pipelines with Google LangExtract, OpenAI Models, Structured Extraction, and Interactive Visualization

Google AI Research Introduces PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing

A Comprehensive Implementation Guide to ModelScope for Model Search, Inference, Fine-Tuning, Evaluation, and Export

Meet OSGym: A New OS Infrastructure Framework That Manages 1,000+ Replicas at $0.23/Day for Computer Use Agent Research

Meta Superintelligence Lab Releases Muse Spark: A Multimodal Reasoning Model With Thought Compression and...

Asif Razzaq-April 9, 20260


 
Meta Superintelligence Labs recently made a significant move by unveiling 'Muse Spark' — the first model in the Muse family. Muse Spark is a... 

Sigmoid vs ReLU Activation Functions: The Inference Cost of Losing Geometric Context

Arham Islam-April 9, 20260


 
A deep neural network can be understood as a geometric system, where each layer reshapes the input space to form increasingly complex decision boundaries.... 

A Coding Guide to Build Advanced Document Intelligence Pipelines with Google LangExtract, OpenAI Models,...

Asif Razzaq-April 8, 20260


 
In this tutorial, we explore how to use Google’s LangExtract library to transform unstructured text into structured, machine-readable information. We begin by installing the... 

Google AI Research Introduces PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing

Asif Razzaq-April 8, 20260


 
Writing a research paper is brutal. Even after the experiments are done, a researcher still faces weeks of translating messy lab notes, scattered results... 

A Comprehensive Implementation Guide to ModelScope for Model Search, Inference, Fine-Tuning, Evaluation, and Export

Michal Sutter-April 8, 20260


 
In this tutorial, we explore ModelScope through a practical, end-to-end workflow that runs smoothly on Colab. We begin by setting up the environment, verifying... 

Meet OSGym: A New OS Infrastructure Framework That Manages 1,000+ Replicas at $0.23/Day for...

Asif Razzaq-April 8, 20260


 
Training AI agents that can actually use a computer — opening apps, clicking buttons, browsing the web, writing code — is one of the... 

Z.AI Introduces GLM-5.1: An Open-Weight 754B Agentic Model That Achieves SOTA on SWE-Bench Pro...

Asif Razzaq-April 8, 20260


 
Z.AI, the AI platform developed by the team behind the GLM model family, has released GLM-5.1 — its next-generation flagship model developed specifically for... 

How to Combine Google Search, Google Maps, and Custom Functions in a Single Gemini...

Michal Sutter-April 7, 20260


 
In this tutorial, we explore the latest Gemini API tooling updates Google announced in March 2026, specifically the ability to combine built-in tools like... 

How to Deploy Open WebUI with Secure OpenAI API Integration, Public Tunneling, and Browser-Based...

Michal Sutter-April 7, 20260


 
In this tutorial, we build a complete Open WebUI setup in Colab, in a practical, hands-on way, using Python. We begin by installing the... 

Meta AI Releases EUPE: A Compact Vision Encoder Family Under 100M Parameters That Rivals...

Asif Razzaq-April 6, 20260


 
Running powerful AI on your smartphone isn't just a hardware problem — it's a model architecture problem. Most state-of-the-art vision encoders are enormous, and... 

DiscordLinkedinRedditX

miniCON Event 2025

Download
AI Magazine/Report

Privacy & TC

Cookie Policy

🐝 Partnership and Promotion


 © Copyright Reserved @2025 Marktechpost AI Media Inc 

We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits. By clicking “Accept”, you consent to the use of ALL the cookies. Do not sell my personal information.

Cookie settingsACCEPT

Privacy & Cookies Policy

Close

Privacy Overview

This website uses cookies to improve your experience while you navigate through the website. Out of these cookies, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may have an effect on your browsing experience.

 Necessary 
Necessary
Always Enabled

 Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information. 

 Others 
Others

 Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.
CookieDurationDescription__Secure-YECpastYouTube sets this cookie to stores the user's video player preferences using embedded YouTube video_pxttldsessionDescription is currently not available.pxctssessionDescription is currently not available.SGPBShowingLimitationDomain776592 daysDescription is currently not available.

 Non Necessary 
Non Necessary

 Any cookies that may not be particularly necessary for the website to function and is used specifically to collect user personal data via analytics, ads, other embedded contents are termed as non-necessary cookies. It is mandatory to procure user consent prior to running these cookies on your website. 

 Analytics 
Analytics

 Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics the number of visitors, bounce rate, traffic source, etc. 

 Performance 
Performance

 Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors. 

 Uncategorized 
Uncategorized

 Undefined cookies are those that are being analyzed and have not been classified into a category as yet. 

 Functional 
Functional

 Functional cookies help to perform certain functionalities like sharing the content of the website on social media platforms, collect feedbacks, and other third-party features. 

 Advertisement 
Advertisement

 Advertisement cookies are used to provide visitors with relevant ads and marketing campaigns. These cookies track visitors across websites and collect information to provide customized ads. 

SAVE & ACCEPT

Powered by

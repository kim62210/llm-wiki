---
title: Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router
source_url: https://vllm-semantic-router.com
final_url: https://vllm-semantic-router.com
status: 200
content_type: text/html; charset=UTF-8
topics: [vLLM Semantic Router (Iris / Athena)]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:10.910150+00:00
---

# Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router

## 원본 URL

https://vllm-semantic-router.com

## 추출 본문

Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router

Skip to main content

vLLM-SRDocs
About
White Paper

Vision Paper

ResearchBlog
Community
Governance

Working Group

Contributing Guide

Code of Conduct

GitHub Issues

English
English

简体中文

Latest
Latest

v0.1

GitHubModels

Open-source LLM router
Routeevery requestwith one systembrainto thebestmodel

Unified routing across local, private, and frontier models—guided by cost, latency, privacy, and safety.

Public BetaRead white paper

System brain
Connect all models with system brain

Kimi

Zhipu

MiniMax

ChatGPT

Claude

Gemini

DeepSeek

Qwen

Llama

Mistral

Grok

Kimi

Zhipu

MiniMax

ChatGPT

Claude

Gemini

DeepSeek

Qwen

Llama

Mistral

Grok

Kimi

Zhipu

MiniMax

ChatGPT

Claude

Gemini

DeepSeek

Qwen

Llama

Mistral

Grok

Kimi

Zhipu

MiniMax

ChatGPT

Claude

Gemini

DeepSeek

Qwen

Llama

Mistral

Grok

Kimi

Zhipu

MiniMax

ChatGPT

Claude

Gemini

DeepSeek

Qwen

Llama

Mistral

Grok

Kimi

Zhipu

MiniMax

ChatGPT

Claude

Gemini

DeepSeek

Qwen

Llama

Mistral

Grok

Signals16
16 signal families across heuristic and learned detectors, from knowledge base routing to history-aware reasks.

Selection12
12 routing strategies spanning rules, latency heuristics, reinforcement learning, and ML selection.

Papers17
17 research papers spanning routing, systems, safety, and multimodality.

Quick start
One supported local path. Copy the installer, run it, then open the dashboard.

Install locally in one line.

The supported first-run path is a single installer that sets up the CLI and local serve flow on macOS and Linux.

One-liner installmacOS / Linux

curl -fsSL https://vllm-semantic-router.com/install.sh | bash

Installs into ~/.local/share/vllm-sr, writes ~/.local/bin/vllm-sr, and keeps Windows on the manual pip flow in the docs.

Copy textFull installation guide

Research
Papers behind the router.

Research threads that trace the router's evolving ideas across safety, multimodality, orchestration, and system design.

2026/PaperPOSITION PAPER

vLLM Semantic Router: Signal Driven Decision Routing for Mixture-of-Modality Models

vLLM Semantic Router Team

arXiv Technical Report

We introduce vLLM Semantic Router, a signal-driven decision routing framework for Mixture-of-Modality deployments that composes heterogeneous signals into deployment-specific routing policies across cost, privacy, latency, and safety constraints.

Read paper

2026/PaperVISION PAPER

The Workload-Router-Pool Architecture for LLM Inference Optimization: A Vision Paper from the vLLM Semantic Router Project

Huamin Chen, Xunzhuo Liu, Bowei He, Fuyuan Lyu, Yankai Chen, Xue Liu, Yuhan Liu, Junchen Jiang

arXiv Technical Report

We synthesize the project’s recent routing, fleet, multimodal, and governance results into the Workload-Router-Pool (WRP) architecture, connecting signal-driven routing to a full-stack inference optimization framework and outlining future research directions across workload, router, and pool design.

Read paper

2026/Paper

Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents

Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen

arXiv Technical Report

We formalize the visual confused deputy as a security failure mode in computer-using agents and introduce a dual-channel guardrail that independently checks click targets and action reasoning before execution.

Read paper

2026/Paper

Outcome-Aware Tool Selection for Semantic Routers: Latency-Constrained Learning Without LLM Inference

Huamin Chen, Xunzhuo Liu, Junchen Jiang, Bowei He, Xue Liu

arXiv Technical Report

We introduce Outcome-Aware Tool Selection (OATS), an offline embedding refinement method that improves semantic-router tool ranking under single-digit millisecond CPU budgets without adding serving-time model inference.

Read paper

2026/Paper

Adaptive Vision-Language Model Routing for Computer Use Agents

Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen

arXiv Technical Report

We propose Adaptive VLM Routing (AVR), which estimates action difficulty and routes computer-use agent steps to the cheapest model that still satisfies a target reliability threshold.

Read paper

2026/Paper

98× Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router

Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen

arXiv Technical Report

We combine Flash Attention, prompt compression, and near-streaming body processing to cut routing latency from seconds to tens of milliseconds while keeping the router lightweight enough to share hardware with serving.

Read paper

2026/Paper

inference-fleet-sim: A Queueing-Theory-Grounded Fleet Capacity Planner for LLM Inference

Huamin Chen, Xunzhuo Liu, Yuhan Liu, Junchen Jiang, Bowei He, Xue Liu

arXiv Technical Report

We present a queueing-theory-grounded fleet planner and discrete-event simulator for sizing multi-pool LLM GPU fleets against P99 TTFT targets, without requiring hardware profiling runs up front.

Read paper

2026/Paper

FleetOpt: Analytical Fleet Provisioning for LLM Inference with Compress-and-Route as Implementation Mechanism

Huamin Chen, Xunzhuo Liu, Yuhan Liu, Junchen Jiang, Bowei He, Xue Liu

arXiv Technical Report

We derive the minimum-cost two-pool LLM fleet directly from the workload CDF and P99 TTFT target, then use Compress-and-Route to make the optimal boundary deployable in practice.

Read paper

2026/Paper

The 1/W Law: An Analytical Study of Context-Length Routing Topology and GPU Generation Gains for LLM Inference Energy Efficiency

Huamin Chen, Xunzhuo Liu, Yuhan Liu, Junchen Jiang, Bowei He, Xue Liu

arXiv Technical Report

We derive the 1/W law showing that tokens per watt roughly halve whenever the serving context window doubles, making context-length routing topology a larger energy-efficiency lever than a pure GPU generation upgrade.

Read paper

2026/Paper

Conflict-Free Policy Languages for Probabilistic ML Predicates: A Framework and Case Study with the Semantic Router DSL

Xunzhuo Liu, Hao Wu, Huamin Chen, Bowei He, Xue Liu

arXiv Technical Report

We show how probabilistic ML predicates in policy languages can silently co-fire on the same query, and implement conflict detection plus a softmax-based prevention mechanism in the Semantic Router DSL.

Read paper

2026/Paper

From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification

Huamin Chen, Xunzhuo Liu, Bowei He, Xue Liu

arXiv Technical Report

We extend the Semantic Router DSL from stateless, per-request routing to multi-step agent workflows, emitting verified decision nodes for orchestration frameworks, Kubernetes artifacts, YANG/NETCONF payloads, and protocol-boundary gates from a single declarative source file.

Read paper

2026/Paper

Knowledge Access Beats Model Size: Memory Augmented Routing for Persistent AI Agents

Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen

arXiv Technical Report

We show that conversational memory and retrieval-grounded routing let a lightweight 8B model recover most of a 235B model’s performance on persistent user-specific queries while cutting effective inference cost by 96%.

Read paper

2026/PaperRAG VERIFICATION

Fast and Faithful: Real-Time Verification for Long-Document Retrieval-Augmented Generation Systems

Xunzhuo Liu, Bowei He, Xue Liu, Haichen Zhang, Huamin Chen

SIGIR 2026 Industry Track

We present a real-time verification component for long-document RAG that processes contexts up to 32K tokens, balancing latency and grounding coverage so interactive systems can detect unsupported answers without falling back to truncated checks.

Read paper

2025/Paper

When to Reason: Semantic Router for vLLM

Chen Wang, Xunzhuo Liu, Yuhan Liu, Yue Zhu, Xiangxi Mo, Junchen Jiang, Huamin Chen

NeurIPS - MLForSys

We present a semantic router that classifies queries based on their reasoning requirements and selectively applies reasoning only when beneficial.

Read paper

2025/Paper

Category-Aware Semantic Caching for Heterogeneous LLM Workloads

Chen Wang, Xunzhuo Liu, Yue Zhu, Alaa Youssef, Priya Nagpurkar, Huamin Chen

We present a category-aware semantic caching where similarity thresholds, TTLs, and quotas vary by query category, with a hybrid architecture separating in-memory HNSW search from external document storage.

Read paper

2025/Paper

Semantic Inference Routing Protocol (SIRP)

Huamin Chen, Luay Jalil

Internet Engineering Task Force (IETF)

This document specifies the Semantic Inference Routing Protocol (SIRP), a framework for content-level classification and semantic routing in AI inference systems.

Read paper

2025/Paper

Multi-Provider Extensions for Agentic AI Inference APIs

H. Chen, L. Jalil, N. Cocker

Internet Engineering Task Force (IETF) - Network Management Research Group

This document specifies multi-provider extensions for agentic AI inference APIs. Published: 20 October 2025. Intended Status: Informational. Expires: 23 April 2026.

Read paper

Papers that frame how the router sees, decides, and scales.
See all papers and talks

Why routing matters
One request. Many model choices.

Models now differ on quality, cost, latency, privacy, and modality. Once you run more than one model, the hard part is no longer calling an LLM. It is routing every request to the right model system.

CapabilityCostPrivacyLatency

What the router decides
Before a response reaches the user, the router has to answer the same operating questions every time.

Choose the right model lane for each request.

Connect local, private, and frontier models without fragmenting the product.

Enforce cost, safety, and privacy at routing time.

Cost control, safety, and model choice have to happen in one step.

SelectionConnectionGovernance

Why teams deploy it
A single routing layer for cost, quality, and policy decisions.

01

Lower cost per request

Send routine traffic to efficient lanes, reserve frontier reasoning for the requests that need it, and turn model choice into measurable ROI.

More useful output per dollar.

02

Safer model decisions

Move jailbreak, PII, and hallucination handling into the routing path so risky traffic is intercepted before it becomes product behavior.

Safety becomes part of the request path.

03

One router across every model

Coordinate local, private, and frontier models through one layer that works from edge deployment to managed cloud.

One system across device, VPC, and cloud.

Routing Blueprint

How System Works

An interactive walkthrough of signal extraction, projection coordination, decision logic, and model routing behavior.

01Shannon Mapping02Entropy Collapse03Four-Layer Architecture04Signal Taxonomy05Agent Policy Synthesis06Layered Entropy Folding

Shannon Mapping

Structural mapping from communication theory to the routing pipeline.

ShannonSource
↕
VSRQuery r

ShannonEncoder
↕
VSRSignal Extraction

ShannonChannel
↕
VSRSignal Vector s

ShannonDecoder
↕
VSRDecision Engine

ShannonDestination
↕
VSRSelected Model

The user request is the raw source message before encoding.

Built on Encoder Models

Encoder-Based Intelligence

Purpose-built encoders read intent, rank relevance, and classify modality before generation begins.

Signal surfaces
Sequence classification, token labeling, embeddings, and reranking collapse into one system-intelligence layer.

SEQ_CLSSequence classification for domain, jailbreak, fact-check, and feedback routing.

TOKENToken labeling for PII and safety-sensitive spans that need localized intervention.

EMBEDEmbedding and rerank paths for semantic cache, knowledge base routing, reask similarity scoring, and candidate ranking.

Hugging Face Models

MOD

Multi-Modality

Detect and route text, image and audio inputs to the right modality-capable model.

CLSSequenceBIOTokenEMBEmbeddingRERRerank

Input
"Is machine learning related to AI?"

Tokenizer
[CLS]IsmachinelearningrelatedtoAI?[SEP]

Embedding

Token Emb

Segment Emb

Position Emb

h₀ = Σ

Encoder Block
×N
ATTNMulti-Head Attention

NORMAdd & Norm

FFNFeed-Forward

NORMAdd & Norm

Signals

CLS
Sentence-Level (CLS Token)[CLS] → Linear Head → "computer science"TaskType: SEQ_CLS
DomainJailbreakFact-checkFeedbackModality

BIO
Token-Level (Per Token)Each token → BIO Label → O O B-LOC I-LOC OTaskType: TOKEN_CLS
PII Detection

EMB
Bi-Encodermean-pooling(h₁..hₙ) → [0.23, -0.41, 0.87, ...]TaskType: EMBEDDING
Semantic CacheSimilarityComplexity-CLJailbreak-CL

RER
Cross-Encoder[CLS] query [SEP] candidate [SEP] → scoreTaskType: CROSS_LEARNING
RerankMulti-Modal

BIE

Bi-Encoder Embeddings

Independently encode queries and candidates into dense vectors for similarity search and semantic caching.

XCE

Cross-Encoder Learning

Joint cross-attention scoring of query-candidate pairs for high-precision reranking.

CLS

Classification

Domain, jailbreak, PII and fact-check classification across 14 MMLU categories via ModernBERT with LoRA.

ATT

Full Attention

Bidirectional attention across tokens and sentences, with full context instead of causal masking.

2DM

2DMSE

Adjust embedding layers and dimensions at inference time to trade compute for accuracy on the fly.

MRL

MRL

Truncate embedding vectors to any dimension without retraining to balance accuracy and speed per request.

Contributors
Meet Our Team

Innovation thrives when great minds come together

Maintainer

Huamin Chen

Distinguished Engineer@Red Hat

Maintainer

Xunzhuo Liu

Intelligent Routing@vLLM

Maintainer

Chen Wang

Senior Staff Research Scientist@IBM

Maintainer

Yue Zhu

Staff Research Scientist@IBM

Committer

Senan Zedan

R&D Manager@Red Hat

Committer

samzong

AI Infrastructure / Cloud-Native PM@DaoCloud

Committer

Liav Weiss

Software Engineer@Red Hat

Committer

Asaad Balum

Senior Software Engineer@Red Hat

Committer

Yehudit

Software Engineer@Red Hat

Committer

Noa Limoy

Software Engineer@Red Hat

Committer

Marina Koushnir

Open Source Contributor@Red Hat

Committer

JaredforReal

Software Engineer@Z.ai

Committer

Srinivas A

Software Engineer@Yokogawa

Committer

carlory

Open Source Engineer@DaoCloud

Committer

Yossi Ovadia

Senior Principal Engineer@Red Hat

Committer

Jintao Zhang

Senior Software Engineer@Kong

Committer

yuluo-yx

Individual Contributor

Committer

cryo-zd

Individual Contributor

Committer

OneZero-Y

Individual Contributor

Committer

aeft

Individual Contributor

Committer

Hao Wu

Individual Contributor

Committer

Qiping Pan

Individual Contributor

Maintainer

Huamin Chen

Distinguished Engineer@Red Hat

Maintainer

Xunzhuo Liu

Intelligent Routing@vLLM

Maintainer

Chen Wang

Senior Staff Research Scientist@IBM

Maintainer

Yue Zhu

Staff Research Scientist@IBM

Committer

Senan Zedan

R&D Manager@Red Hat

Committer

samzong

AI Infrastructure / Cloud-Native PM@DaoCloud

Committer

Liav Weiss

Software Engineer@Red Hat

Committer

Asaad Balum

Senior Software Engineer@Red Hat

Committer

Yehudit

Software Engineer@Red Hat

Committer

Noa Limoy

Software Engineer@Red Hat

Committer

Marina Koushnir

Open Source Contributor@Red Hat

Committer

JaredforReal

Software Engineer@Z.ai

Committer

Srinivas A

Software Engineer@Yokogawa

Committer

carlory

Open Source Engineer@DaoCloud

Committer

Yossi Ovadia

Senior Principal Engineer@Red Hat

Committer

Jintao Zhang

Senior Software Engineer@Kong

Committer

yuluo-yx

Individual Contributor

Committer

cryo-zd

Individual Contributor

Committer

OneZero-Y

Individual Contributor

Committer

aeft

Individual Contributor

Committer

Hao Wu

Individual Contributor

Committer

Qiping Pan

Individual Contributor

Maintainer

Huamin Chen

Distinguished Engineer@Red Hat

Maintainer

Xunzhuo Liu

Intelligent Routing@vLLM

Maintainer

Chen Wang

Senior Staff Research Scientist@IBM

Maintainer

Yue Zhu

Staff Research Scientist@IBM

Committer

Senan Zedan

R&D Manager@Red Hat

Committer

samzong

AI Infrastructure / Cloud-Native PM@DaoCloud

Committer

Liav Weiss

Software Engineer@Red Hat

Committer

Asaad Balum

Senior Software Engineer@Red Hat

Committer

Yehudit

Software Engineer@Red Hat

Committer

Noa Limoy

Software Engineer@Red Hat

Committer

Marina Koushnir

Open Source Contributor@Red Hat

Committer

JaredforReal

Software Engineer@Z.ai

Committer

Srinivas A

Software Engineer@Yokogawa

Committer

carlory

Open Source Engineer@DaoCloud

Committer

Yossi Ovadia

Senior Principal Engineer@Red Hat

Committer

Jintao Zhang

Senior Software Engineer@Kong

Committer

yuluo-yx

Individual Contributor

Committer

cryo-zd

Individual Contributor

Committer

OneZero-Y

Individual Contributor

Committer

aeft

Individual Contributor

Committer

Hao Wu

Individual Contributor

Committer

Qiping Pan

Individual Contributor

Maintainers, committers, and contributors across research, infrastructure, and open-source operations.
View All Team Members

Open-source ecosystem
Acknowledgements

vLLM Semantic Router is made possible by the open-source ecosystem.

Dependency

vLLMOpen project

Dependency

PyTorchOpen project

Dependency

HuggingFaceOpen project

Dependency

AMDOpen project

Dependency

NVIDIAOpen project

Dependency

EnvoyProxyOpen project

Dependency

KubernetesOpen project

Dependency

MilvusOpen project

Dependency

PrometheusOpen project

Dependency

GrafanaOpen project

Documentation
Architecture, written to be used.

Install, configure, train, and operate from one dense documentation graph.
Docs index

Community
Research and builders in one loop.

Papers, working groups, and contributors evolve the same system in public.
Community routes

Documentation

Quick Start

Installation

Governance

Contributing

Community

GitHub

Hugging Face

GitHub Discussions

More

Blog

Publications

White Paper

Vision Paper

License

Copyright © 2026 vLLM Semantic Router Team. Built with Docusaurus.

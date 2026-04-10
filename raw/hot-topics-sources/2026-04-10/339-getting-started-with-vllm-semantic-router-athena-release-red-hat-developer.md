---
title: Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI | Red Hat Developer
source_url: https://developers.redhat.com/articles/2026/03/25/getting-started-vllm-semantic-router-athena-release
final_url: https://developers.redhat.com/articles/2026/03/25/getting-started-vllm-semantic-router-athena-release
status: 200
content_type: text/html; charset=UTF-8
topics: [vLLM Semantic Router (Iris / Athena)]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:10.567108+00:00
---

# Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI | Red Hat Developer

## 원본 URL

https://developers.redhat.com/articles/2026/03/25/getting-started-vllm-semantic-router-athena-release

## 추출 본문

Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI | Red Hat Developer
 Skip to main content
 

Products

Platforms

Red Hat Enterprise Linux

Red Hat AI

Red Hat OpenShift

Red Hat Ansible Automation Platform

See all Red Hat products

Featured

Red Hat build of OpenJDK

Red Hat Developer Hub

Red Hat JBoss Enterprise Application Platform

Red Hat OpenShift Dev Spaces

Red Hat OpenShift Local

Red Hat Developer Sandbox

Try Red Hat products and technologies without setup or configuration fees for 30 days with this shared Red Hat OpenShift and Kubernetes cluster.

Try at no cost

Technologies

Featured

AI/ML

Linux

Kubernetes

Automation

See all technologies

Programming languages & frameworks

Java

Python

JavaScript

System design & architecture

Red Hat architecture and design patterns

Microservices

Event-Driven Architecture

Databases

Developer experience

Productivity

Tools

GitOps

Automated data processing

AI/ML

Data science

Apache Kafka on Kubernetes

Platform engineering

DevOps

DevSecOps

Red Hat Ansible Automation Platform for applications and services

Secure development & architectures

Security

Secure coding

Learn

Featured

Kubernetes & cloud native

Linux

Automation

AI/ML

See all learning resources

E-books

GitOps cookbook

Podman in action

Kubernetes operators

The path to GitOps

See all e-books

Cheat sheets

Linux commands

Bash commands

Git

systemd commands

See all cheat sheets

Documentation

Product documentation

API catalog

Legacy documentation

Developer Sandbox

Developer Sandbox

Access Red Hat’s products and technologies without setup or configuration, and start developing quicker than ever before with our new, no-cost sandbox environments.

Explore the Developer Sandbox

Featured Developer Sandbox activities

Get started with your Developer Sandbox

OpenShift virtualization and application modernization using the Developer Sandbox

Explore all Developer Sandbox activities

Ready to start developing apps?

Try at no cost

Blog

Events

Videos

SearchSearch

 All Red Hat
 

Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI

March 25, 2026

Christopher Nuland

Related topics:APIsArtificial intelligenceRelated products:Red Hat AI Inference ServerRed Hat AI

 Table of contents:
 

Every token costs something. Whether it's dollars on a cloud API or watts on your GPU, the question isn't if you should route large language model (LLM) requests intelligently, but how fast you can start.

vLLM Semantic Router is an upstream open source project that aims to solve this challenge. The project's latest release, Athena 0.2, offers an effective way to manage token costs. It sits between your clients and your models, inspects each request, and decides which backend should handle it. A simple "What is the capital of France?" goes to your free local model. A "prove by induction that..." goes to the heavy-hitter SaaS model (OpenAI, Claude Opus, and others). Your clients don't change a thing. The API is OpenAI-compatible, so any tool that speaks 
/v1/chat/completions
 works without additional configuration. That includes autonomous agentic agents.

Intelligent routing can significantly reduce token costs, often by more than 90%, by shifting the bulk of your agent's common requests to a less expensive model. Running such a model locally or on your own server can lead to monthly savings of hundreds of dollars on inference. This is especially valuable for continuous-operation agents, such as OpenClaw.

In this post, I'll walk through setting up Athena locally with two models: a quantized Qwen3-Coder-Next running on Apple Silicon, and Google's Gemini 2.5 Pro as the cloud fallback. By the end, you'll have a working router that keeps a majority of your requests local and free. All the code and configurations from this walkthrough are in the companion GitHub repo, which also includes a vLLM-on-Linux path if you're running NVIDIA GPUs instead of Apple Silicon.

What is vLLM Semantic Router?

At its core, vLLM Semantic Router is a request classifier that lives in front of your LLM backends. It's the system-level intelligence for mixture-of-models. It doesn't generate tokens itself; it decides which model generates them.

The architecture looks like this:

Client → Envoy Proxy (e.g. port 8899) → ExtProc (Go router) → Backend Model

Envoy handles the HTTP traffic. A Go-based External Processing filter (ExtProc) intercepts each request via gRPC, runs it through a classification pipeline, and tells Envoy which backend cluster to route to. The client never knows the difference.

The Athena release includes the following components:

Eight neural classifiers use mmBERT-32K (307 million parameters and more than 1,800 languages) to provide intent classification, jailbreak detection, PII detection, fact-checking, hallucination detection, and more.

Signal-decision architecture creates signals from requests, such as keyword matches, embedding similarity, or domain classification. The router then uses these signals in Boolean expression trees to make decisions.

HNSW semantic cache uses vector-similarity caching to identify paraphrased duplicates instead of only relying on exact-match deduplication.

11 model selection algorithms range from simple static routing to Elo-based learning, Thompson sampling, and RouterDC.

First-class reasoning mode allows the router to toggle reasoning parameters on supported models based on the complexity of the request.

That's a comprehensive set of features, but the beauty of the signal-decision design is that you can start with simple keyword signals and static routing and layer in neural classifiers as you need them.

Prerequisites

Before you start, you'll need:

Python 3.10 or later. I'm using 3.11 with 
pyenv
.

Podman or Docker. Athena runs in a container.

A local model server. This tutorial uses 
mlx-lm
 on macOS, but vLLM works great on Linux with NVIDIA GPUs.

A cloud API key (optional). I'm using Gemini 2.5 Pro, but any OpenAI-compatible endpoint works.

# Install the vLLM Semantic Router CLI
pip install vllm-sr

# Verify
vllm-sr version

The command-line interface (CLI) handles config generation, validation, container management, and Envoy template rendering. Think of it as 
kubectl
 for your routing layer.

Step 1: Set up your local model

I'm running Qwen3-Coder-Next 80B quantized to 4-bit on an M4 Max with 128 GB of unified memory. We're using 
mlx-lm
 here because it's optimized for running quantized models on Apple Silicon. It memory-maps the weights directly on the unified memory architecture, so an 80 B model at 4-bit quantization (approximately 42 GB) loads without copying to a separate GPU.

If you're on Linux with an NVIDIA GPU, you could use vLLM itself to serve any model you'd like. The router doesn't care what's behind the OpenAI-compatible API.

First, install 
mlx-lm
:

pip install mlx-lm

Then download the model. This one is about 42 GB, so give it some time:

python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('mlx-community/Qwen3-Coder-Next-4bit')
"

Once downloaded, start the server:

python3 -m mlx_lm server \
 --model mlx-community/Qwen3-Coder-Next-4bit \
 --host 0.0.0.0 \
 --port 8000

Verify it's running:

curl http://localhost:8000/v1/models

You should see the model ID in the response. Keep this terminal open; the server needs to stay running.

Step 2: Get your cloud API key

I'm using Gemini 2.5 Pro through Google's OpenAI-compatible endpoint. Grab a key from Google AI Studio, then stash it somewhere safe:

echo "GEMINI_API_KEY=your-key-here" > .env
echo ".env" >> .gitignore

We'll reference this key in the configuration. Note that the current version of the Athena CLI doesn't support 
${ENV_VAR}
 expansion in YAML. You'll need to put the key directly in your config file. That's fine for local development as long as you use 
.gitignore
 for the config or the 
.env
 file.

Note

Any software as a service (SaaS) model provider will work here; you could use OpenAI, Claude, and so on.

Step 3: Write your router config

Create a 
config.yaml
. This is where the routing intelligence is defined:

version: v0.1

listeners:
 - name: "http-8899"
 address: "0.0.0.0"
 port: 8899
 timeout: "300s"

providers:
 models:
 # Local model: free, fast, specialized for code
 - name: "mlx-community/Qwen3-Coder-Next-4bit"
 param_size: "80b"
 endpoints:
 - name: "mlx-local"
 weight: 100
 endpoint: "host.containers.internal:8000"
 protocol: "http"
 capabilities: ["coding", "debugging", "refactoring"]
 quality_score: 0.85
 pricing:
 currency: "USD"
 prompt_per_1m: 0.0
 completion_per_1m: 0.0

 # Cloud model: heavy reasoning, math, analysis
 - name: "gemini-2.5-pro"
 param_size: "400b"
 endpoints:
 - name: "gemini-primary"
 weight: 100
 endpoint: "generativelanguage.googleapis.com/v1beta/openai"
 protocol: "https"
 access_key: "<YOUR_GEMINI_API_KEY>"
 capabilities: ["reasoning", "math", "analysis", "coding", "creative"]
 quality_score: 0.95
 pricing:
 currency: "USD"
 prompt_per_1m: 1.25
 completion_per_1m: 10.00

 default_model: "mlx-community/Qwen3-Coder-Next-4bit"

A few things to note here:

The 
host.containers.internal
 address is how Podman (or Docker) containers reach services on the host machine. Because the router runs in a container and your MLX server runs on the host, this bridge is necessary.

Model names must match exactly what the backend expects. 
mlx-lm
 uses Hugging Face model IDs, so the name in your configuration must be 
mlx-community/Qwen3-Coder-Next-4bit
, not a friendly alias.

Don't add 
/v1
 to your endpoint. Envoy already handles the path routing. If you include it, you'll end up with 
/v1/v1/chat/completions
 and a 404.

Step 4: Define signals and decisions

Below the 
providers
 block, add your routing logic. Signals detect patterns in requests. Decisions consume those signals and choose a model:

signals:
 keywords:
 - name: "reasoning_keywords"
 operator: "OR"
 keywords:
 - "prove"
 - "derive"
 - "theorem"
 - "induction"
 - "research"
 - "formal verification"
 - "proof by contradiction"
 case_sensitive: false

 - name: "coding_keywords"
 operator: "OR"
 keywords:
 - "implement"
 - "refactor"
 - "debug"
 - "function"
 - "class"
 - "import"
 - "build"
 - "code"
 case_sensitive: false

decisions:
 # Reasoning tasks → cloud model (highest priority)
 - name: "reasoning-route"
 description: "Route complex reasoning tasks to Gemini 2.5 Pro"
 priority: 100
 rules:
 operator: "OR"
 conditions:
 - type: "keyword"
 name: "reasoning_keywords"
 modelRefs:
 - model: "gemini-2.5-pro"
 use_reasoning: true

 # Coding tasks → local model
 - name: "coding-route"
 description: "Route coding tasks to local Qwen3-Coder-Next"
 priority: 80
 rules:
 operator: "OR"
 conditions:
 - type: "keyword"
 name: "coding_keywords"
 modelRefs:
 - model: "mlx-community/Qwen3-Coder-Next-4bit"
 use_reasoning: false

 # Everything else → local model (cost-effective default)
 - name: "default-route"
 description: "Default route to local model for cost savings"
 priority: 1
 rules:
 operator: "AND"
 conditions: []
 modelRefs:
 - model: "mlx-community/Qwen3-Coder-Next-4bit"
 use_reasoning: false

The priority system is straightforward; higher numbers are evaluated first. If a request contains prove or theorem, the reasoning route fires at priority 100 and sends the request to Gemini. If a request contains implement or debug, the coding route fires at priority 80 and keeps the request local. All other requests use the default at priority 1.

This keyword-only routing is the simplest configuration. Athena also supports embedding-based signals (semantic similarity against anchor prompts), domain classification through neural classifiers, and complexity scoring. Start with this configuration and add features when you need more precision.

If you find the YAML configuration verbose, Athena v0.2 ships with a dedicated configuration language. This is a typed, human-readable domain-specific language (DSL) that reads closer to natural language than raw YAML. Instead of nesting signal rules and decision trees across dozens of indented lines, you can write concise blocks like 
SIGNAL domain math { mmlu\_categories: \["math"\] }
 and 
ROUTE math\_route { PRIORITY 100; WHEN domain("math"); MODEL "qwen2.5:3b" (reasoning = true) }
. Boolean routing logic uses intuitive 
WHEN
, 
AND
, 
OR
, and 
NOT
 operators instead of nested YAML condition trees. The DSL compiles to the same internal representation as YAML. From a single source, the DSL can produce flat YAML for local development, Kubernetes 
SemanticRouter
 custom resource definitions (CRDs) for operator-based deployment, or Helm 
values.yaml
 files for chart-based rollouts.

You can write a routing policy once and deploy it anywhere. Even better, existing YAML configurations can also be decompiled into DSL source to simplify migration. Type-safe compilation catches undefined signal references and constraint violations, such as out-of-range thresholds, at compile time before the configuration reaches the cluster. For more information about the grammar, the compilation pipeline, and how the DSL enables agent-based policy synthesis, see the vLLM Semantic Router white paper.

Step 5: Initialize and launch

Initialize the workspace and validate the configuration:

vllm-sr init
vllm-sr validate --config config.yaml

The 
init
 command creates a 
.vllm-sr/
 directory with Envoy templates, Grafana dashboards, and default configurations. The 
validate
 command checks your YAML against the schema.

Now start the router:

vllm-sr serve --config config.yaml

On the first run, the tool pulls the container image (approximately 2 GB) and downloads eight internal machine learning (ML) models (about 25 GB total). This process takes about 30 minutes, depending on your connection speed. Subsequent starts take about 15 seconds because the models are cached locally.

Once you see the router logs stabilize, the service is live on port 8899.

Step 6: Test your routes

Let's verify the routing works. Send a few requests and check which model handles each:

# Simple question → should route to local Qwen3
curl -s http://localhost:8899/v1/chat/completions \
 -H "Content-Type: application/json" \
 -d '{
 "model": "auto",
 "messages": [{"role": "user", "content": "What is a Python decorator?"}],
 "max_tokens": 100
 }' | python3 -c "import sys,json; r=json.load(sys.stdin); print(f'Model: {r[\"model\"]}')"

# Coding request → should route to local Qwen3
curl -s http://localhost:8899/v1/chat/completions \
 -H "Content-Type: application/json" \
 -d '{
 "model": "auto",
 "messages": [{"role": "user", "content": "Implement a function that finds the longest palindromic substring."}],
 "max_tokens": 100
 }' | python3 -c "import sys,json; r=json.load(sys.stdin); print(f'Model: {r[\"model\"]}')"

# Reasoning request → should route to Gemini Pro
curl -s http://localhost:8899/v1/chat/completions \
 -H "Content-Type: application/json" \
 -d '{
 "model": "auto",
 "messages": [{"role": "user", "content": "Prove by induction that the sum 1+2+...+n = n(n+1)/2."}],
 "max_tokens": 100
 }' | python3 -c "import sys,json; r=json.load(sys.stdin); print(f'Model: {r[\"model\"]}')"

The 
model: "auto"
 field tells the router to classify and route. Athena adds response headers that show its work:

x-vsr-selected-model: mlx-community/Qwen3-Coder-Next-4bit
x-vsr-selected-decision: coding-route
x-vsr-selected-confidence: 1.0000
x-vsr-matched-keywords: coding_keywords
x-vsr-cache-hit: false

When the reasoning route fires, the response also includes the following header:

x-vsr-selected-reasoning: on

This indicates that Athena enabled reasoning mode on the target model. The router does more than route requests; it also adjusts how the model processes the problem.

What we saw: Benchmarks

I ran a suite of 21 prompts across five categories: simple lookups, coding tasks, complex multi-step problems, formal reasoning, and agentic tool-use requests. The following table shows what Athena did with them.
CategoryPromptsRouted toDecisionSimple (definitions, translations)4Local Qwen3default-routeCoding (implement, debug, refactor)5Gemini Procoding-routeComplex (API design, distributed systems)3Local Qwen3default-routeReasoning (proofs, formal verification)3Gemini Proreasoning-routeAgentic (tool use)2Local Qwen3default-routeSession continuity2Local Qwen3default-routeDedup (identical request)2Local Qwen3cache-hit
The result: 86% of requests stayed local. Only 14% used cloud resources.

In this test, 18 of the 21 requests were handled by the free, self-hosted model. The eight reasoning and advanced coding requests sent to Gemini Pro were those that required complex processing, such as mathematical proofs and formal verification.

Routing latency

The router's classification pipeline ran in 28 ms to 93 ms per request.
MetricValueP50 routing latency40 msP99 routing latency93 msAverage45.9 ms
For context, the actual LLM inference (generating tokens) takes 800 ms to 11,000 ms. The routing overhead is roughly 0.4% to 5% of total request time. This delay is minimal.

Connecting OpenClaw

Because Athena exposes a standard 
/v1/chat/completions
 endpoint, configuring OpenClaw to use it is simple. Set your OpenClaw base URL to 
http://localhost:8899
, and the router handles the rest. Your OpenClaw agents gain access to multiple models without code changes; the router selects the appropriate model for each request.

This is where the token optimization gets interesting. Agentic workflows require many interactions. An OpenClaw team might fire hundreds of requests during a single task, primarily for simple tool calls and code generation. Without routing, every request is sent to the same expensive model. With Athena, routine tasks remain local, and complex problems get the heavyweight treatment and use more advanced models.

Where to go from here

This tutorial covers a basic configuration of keyword signals and static routing. Athena includes more advanced features:

Embedding signals: Define anchor prompts and route based on semantic similarity instead of keyword matching. This identifies requests that have the same meaning but use different words.

Domain classification: Enable the mmBERT neural classifier to automatically detect request domains such as math, code, or creative writing, without manual keyword lists.

Complexity scoring: The neural pipeline estimates request complexity and routes traffic accordingly.

Jailbreak and PII detection: Athena ships with safety classifiers that can block prompt injection attempts and redact sensitive information before it reaches your models.

Dashboard: Athena includes a React-based dashboard on port 8700 for visual configuration, request replay, and monitoring.

Kubernetes CRDs: For production, Athena provides 
IntelligentPool
 and 
IntelligentRoute
 custom resources, a Helm chart, and HPA-compatible scaling.

The signal-decision architecture is designed to be layered. Start with keywords, add embeddings for fuzzy matching, and turn on neural classifiers for domain awareness. Each layer is independent and configurable.

Wrapping up

vLLM Semantic Router's Athena release provides a production-grade routing layer that works with any OpenAI-compatible model server. The setup is straightforward: define your models, write a few signal rules, and let the router determine where to send each request.

The benefit is clear. If 86% of your requests are handled by a free local model instead of a cloud API that costs $1.25 per million input tokens and $10.00 per million output tokens, you will achieve a significant cost reduction. Your users won't notice a difference because the API contract remains the same.

The code and configurations from this walkthrough are available on GitHub. This includes a vLLM-on-Linux configuration for users with NVIDIA GPUs. Swap in your own models, adjust the keyword signals, and see what routing ratio you land on.

Your tokens are expensive. Manage them strategically.

Related Posts

5 steps to triage vLLM performance

Serve and benchmark Prithvi models with vLLM on OpenShift

Practical strategies for vLLM performance tuning

Run Voxtral Mini 4B Realtime on vLLM with Red Hat AI on Day 1: A step-by-step guide

Autoscaling vLLM with OpenShift AI model serving: Performance validation

Why vLLM is the best choice for AI inference today

Recent Posts

Build resilient guardrails for OpenClaw AI agents on Kubernetes

Enable Firewall-as-a-Service in OpenStack Services on OpenShift

How DNS name tracking enhances network observability

Manage AI context with the Lola package manager

Agent-driven attestation: How Keylime's push model rethinks remote integrity verification

 What’s up next?
 

 Learning Path
 

Download, serve, and interact with LLMs on RHEL AI

 Configure your Red Hat Enterprise Linux AI machine, download, serve, and...
 

LinkedInYouTubeTwitterFacebook
Platforms

Red Hat AI

Red Hat Enterprise Linux

Red Hat OpenShift

Red Hat Ansible Automation Platform

See all products

Build

Developer Sandbox

Developer tools

Interactive tutorials

API catalog

Quicklinks

Learning resources

E-books

Cheat sheets

Blog

Events

Newsletter

Communicate

About us

Contact sales

Find a partner

Report a website issue

Site status dashboard

Report a security problem

RED HAT DEVELOPER

Build here. Go anywhere.

We serve the builders. The problem solvers who create careers with code.

Join us if you’re a developer, software engineer, web designer, front-end designer, UX designer, computer scientist, architect, tester, product manager, project manager or team lead.

Sign me up 

Red Hat legal and privacy links

About Red Hat

Jobs

Events

Locations

Contact Red Hat

Red Hat Blog

Inclusion at Red Hat

Cool Stuff Store

Red Hat Summit
© 2026 Red Hat
Red Hat legal and privacy links

Privacy statement

Terms of use

All policies and guidelines

Digital accessibility

Report a website issue

Your name

Your e-mail address

Subject

Message

Type of request/issueDownload Issue - Logged in User can't get fileContent is wrong or missing from siteLearning Path trouble : Broken InstruqtLearning Path trouble : Missing ContentProduct IssueTrouble registering for an eventI cannot log inI cannot renew my subscriptionI cannot sign up to the Red Hat Developer ProgramOther

Problem Page URL

Territory/Country-Please choose-CanadaChinaIndiaUnited StatesAmerican SamoaAustraliaBangladeshBhutanBrunei DarussalamCambodiaChristmas IslandCocos (Keeling) IslandsCook IslandsFijiGuamHeard Island and McDonald IslandsHong KongIndonesiaJapanKiribatiKorea, Democratic People's Republic ofKorea, Republic ofLao People's Democratic RepublicMacaoMalaysiaMaldivesMarshall IslandsMongoliaMyanmarNauruNepalNew ZealandNiueNorfolk IslandNorthern Mariana IslandsPakistanPalauPapua New GuineaPhilippinesSamoaSingaporeSolomon IslandsSri LankaTaiwanThailandTimor-LesteTokelauTongaTuvaluVanuatuViet NamAfghanistanAland IslandsAlbaniaAlgeriaAndorraAngolaArmeniaArubaAustriaAzerbaijanBahrainBelarusBelgiumBeninBermudaBosnia and HerzegovinaBotswanaBouvet IslandBritish Indian Ocean TerritoryBulgariaBurkina FasoBurundiCameroonCape VerdeCentral African RepublicChadComorosCongoCongo, The Democratic Republic of theCote d'IvoireCroatiaCuracaoCyprusCzech RepublicDenmarkDjiboutiEgyptEquatorial GuineaEritreaEstoniaEthiopiaFaroe IslandsFinlandFranceFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGuadeloupeGuernseyGuineaGuinea-BissauHoly See (Vatican City State)HungaryIcelandIran, Islamic Republic ofIraqIrelandIsle of ManIsraelItalyJerseyJordanKazakhstanKenyaKuwaitKyrgyzstanLatviaLebanonLesothoLiberiaLibyan Arab JamahiriyaLiechtensteinLithuaniaLuxembourgMacedonia, The Former Yugoslav Republic ofMadagascarMalawiMaliMaltaMartiniqueMauritaniaMauritiusMayotteMoldova, Republic ofMonacoMontenegroMoroccoMozambiqueNamibiaNetherlandsNetherlands AntillesNew CaledoniaNigerNigeriaNorwayOmanPalestinian Territory, OccupiedPitcairnPolandPortugalQatarReunionRomaniaRussian FederationRwandaSaint BarthelemySaint HelenaSaint Martin (French part)Saint Pierre and MiquelonSan MarinoSao Tome and PrincipeSaudi ArabiaSenegalSerbiaSerbia and MontenegroSeychellesSierra LeoneSint MaartenSlovakiaSloveniaSomaliaSouth AfricaSouth Georgia and the South Sandwich IslandsSouth SudanSpainSudanSvalbard and Jan MayenSwazilandSwedenSwitzerlandSyrian Arab RepublicTajikistanTanzania, United Republic ofTogoTunisiaTurkeyTurkmenistanUgandaUkraineUnited Arab EmiratesUnited KingdomUzbekistanWallis and FutunaWestern SaharaYemenZaireZambiaZimbabweAnguillaAntigua and BarbudaArgentinaBahamasBarbadosBelizeBoliviaBrazilCayman IslandsChileColombiaCosta RicaCubaDominicaDominican RepublicEcuadorEl SalvadorFalkland Islands (Malvinas)French GuianaGrenadaGuatemalaGuyanaHaitiHondurasJamaicaMexicoMicronesia, Federated States ofMontserratNicaraguaPanamaParaguayPeruPuerto RicoSaint Kitts and NevisSaint LuciaSaint Vincent and the GrenadinesSurinameTrinidad and TobagoTurks and Caicos IslandsUnited States Minor Outlying IslandsUruguayVenezuelaVirgin Islands, BritishVirgin Islands, U.S.

Red Hat Account Number

Red Hat Username

Leave this field blank

---
title: Accelerating large language models with NVFP4 quantization | Red Hat Developer
source_url: https://developers.redhat.com/articles/2026/02/04/accelerating-large-language-models-nvfp4-quantization
final_url: https://developers.redhat.com/articles/2026/02/04/accelerating-large-language-models-nvfp4-quantization
status: 200
content_type: text/html; charset=UTF-8
topics: [NVFP4 Quantization for LLM Inference]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:38.470401+00:00
---

# Accelerating large language models with NVFP4 quantization | Red Hat Developer

## 원본 URL

https://developers.redhat.com/articles/2026/02/04/accelerating-large-language-models-nvfp4-quantization

## 추출 본문

Accelerating large language models with NVFP4 quantization | Red Hat Developer
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
 

Accelerating large language models with NVFP4 quantization

February 4, 2026

Shubhra PanditAlexandre MarquesDipika SikkaKyle Sayers

Related topics:Artificial intelligenceRelated products:Red Hat AI Inference ServerRed Hat AI

 Table of contents:
 

Large language models (LLMs) continue to scale rapidly, unlocking stronger reasoning, better instruction following, and broader domain coverage. At the same time, this growth dramatically increases memory and compute demands—making efficient deployment increasingly challenging for both research and enterprise use.

To address this, we are releasing NVFP4-quantized versions of several widely used large language models, spanning 8B to frontier-scale models exceeding 400B+ parameters. With the introduction of NVIDIA Blackwell (B200) GPUs, NVFP4 benefits from native FP4 tensor cores, enabling true hardware-accelerated FP4 compute. This allows substantial memory reduction while recovering near-baseline accuracy, particularly at larger scales, making state-of-the-art LLMs significantly more practical to deploy.

Across the models evaluated in this release, several clear patterns emerge:

NVFP4 delivers near-baseline accuracy at large scale, making it well suited for frontier and MoE models.

Accuracy recovery improves with model size, with the strongest results observed on the largest dense and expert-based architectures.

Smaller models show more variability, but still retain the majority of BF16 accuracy.

Overall, NVFP4 shifts the efficiency–accuracy trade-off in favor of deployment at scale.

What is NVFP4?

NVFP4 is NVIDIA's 4-bit floating-point format designed for high-performance inference on modern GPUs. It combines the compactness of ultra-low-precision quantization with the flexibility of floating-point arithmetic, allowing large language models to be deployed more efficiently without sacrificing numerical expressiveness. See Figure 1.

At a high level, NVFP4 offers:

Compact 4-bit storage with floating-point semantics.

Improved handling of outlier values and wide dynamic ranges.

Strong accuracy recovery relative to BF16 baselines at larger model scales.

Robust behavior on large decoder-only and mixture-of-experts (MoE) models.

Figure 1: Illustration of NVFP4-style hierarchical quantization. FP4 values are stored as discrete codes in small groups (group size = 16), each scaled by a FP8 group scale, with an additional FP32 tensor-level scale capturing global magnitude.
Why NVFP4 works: High-precision scaling for wide dynamic range

NVFP4 addresses the dynamic range challenges of ultra-low-precision inference by combining floating-point representation with hierarchical scaling. Per-group scaling preserves local structure within weight groups, while an FP32 global scale restores high dynamic range that would otherwise be constrained by the more limited FP8 (E4M3) local scaling. Together, these mechanisms allow FP4 values to retain more signal and incur less error than integer quantization when weights span wide value distributions.

In practice, NVFP4 achieves roughly 1.5 to 1.8× smaller effective weight storage than FP8 and ~3× smaller than FP16. These reductions enable higher achievable batch sizes and greater concurrency for large-model inference. Figure 2 illustrates how these storage reductions manifest across two ultra-large models, highlighting how NVFP4 occupies a distinct point in the size–accuracy design space relative to integer and higher-precision floating-point formats.

Figure 2: Model weight storage across precision formats for two representative large models. (Left) Qwen3-235B-A22B, comparing BF16, FP8-dynamic, and NVFP4. NVFP4 reduces weight storage by approximately ~3.3× vs BF16 and ~1.5–1.8× vs FP8.
(Right) Llama-4-Maverick-17B-128E-Instruct, comparing BF16, INT4 (W4A16), and NVFP4. While INT4 achieves the smallest raw weight footprint, NVFP4 balances compact storage with floating-point semantics and improved numerical robustness. 
Quantized models released

Using the latest NVFP4 support in LLM Compressor, we quantized a diverse set of popular open models spanning multiple parameter scales—from compact 8B-class models to ultra-large 400B+ Mixture-of-Experts architectures. These models are immediately deployable with vLLM for both production and research use.

This release covers a broad range of model families and architectures, including:

Large dense and Mixture-of-Experts (MoE) models

Instruction-tuned and reasoning variants

Model sizes ranging from single-digit billions to hundreds of billions of parameters.

All NVFP4-quantized models are hosted and continuously updated in our Hugging Face collection.

To characterize how NVFP4 behaves in practice, we evaluated the quantized models against their BF16 baselines across a range of task-level and aggregate benchmarks. 

Key accuracy findings

Large models (70B–235B) consistently achieve ~99% recovery.

Mid-size models (~30B) achieve 97–99% recovery.

For 7B–14B models, NVFP4 recovers ~95–98% of BF16 accuracy across various tasks, with slightly larger degradation on Llama-3.1-8B, while Qwen-8B and Qwen-14B remain closer to ~98% recovery.

MoE models (Llama-4 Scout & Maverick / Qwen3-235B-A22B) show exceptionally strong robustness due to NVFP4's expressive range.

The following figures illustrate accuracy recovery at multiple levels—from detailed per-task comparisons on individual large models to averaged results across model families and evaluation suites.

Figure 3: Task-level accuracy comparison between BF16 and NVFP4 for Qwen3-235B-A22B-Instruct-2507 across representative benchmarks.
While Figure 3 highlights detailed task-level behavior for the large Qwen3-235B-A222 model, the next figure summarizes aggregate accuracy recovery trends across model sizes and benchmarks.

Figure 4: Average accuracy recovery of NVFP4-quantized models relative to BF16 baselines, aggregated across OpenLLMv1, OpenLLMv2, and HumanEval. Recovery improves consistently with model scale, with large dense and MoE models exceeding 99% recovery.
To further understand how NVFP4 behaves on a specific capability domains, we next examine accuracy recovery on code generation using HumanEval, and on broad multi-domain knowledge and reasoning using MMLU. 

Figure 5: Code generation accuracy recovery for NVFP4-quantized models relative to BF16 baselines, measured on HumanEval.

Figure 6: MMLU accuracy recovery for NVFP4-quantized models relative to BF16 baselines. 
Taken together, the results above highlight where NVFP4 is most effective today. Accuracy recovery improves steadily with scale, making NVFP4 particularly well suited for larger dense and MoE models, where memory pressure is highest and deployment constraints are most acute. At smaller scales, results vary more by task and calibration strategy, suggesting that model-specific tuning may be important rather than a one-size-fits-all approach. 

We explore these tuning considerations in more detail below. Overall, the evaluations presented here show that NVFP4 can preserve model behavior across a wide range of benchmarks while enabling significantly more memory-efficient deployment.

NVFP4 robustness with scale-dependent variability

In developing these NVFP4 models, we generally followed a standard, straightforward quantization workflow that proved effective across model architectures and scales. For a subset of smaller models (approximately 8B–14B parameters), we additionally explored refinements such as different calibration observers and SmoothQuant, which is fully compatible with NVFP4.

We observed that the impact of these techniques at smaller scales can be mixed: some models showed modest accuracy improvements with MSE-based observers or SmoothQuant, while others achieved similar or better results without them. Importantly, larger models achieved strong and stable accuracy recovery using the standard NVFP4 recipe, with additional tuning applied only when it provided clear empirical benefit. Each released model reflects the simplest configuration that met accuracy targets at scale.

What's next?

This blog focuses on accuracy recovery and making NVFP4-quantized models available to the community. Additional models and variants will be added to the collection on an ongoing basis as new models are released and NVFP4 support expands across architectures, tooling, and inference backends. Comprehensive performance analysis—including throughput and latency—are actively being finalized and will be shared in a follow-up blog dedicated to inference performance and deployment trade-offs.

Driving efficient AI forward

Quantization—especially modern FP4-based formats like NVFP4—is unlocking the next generation of scalable, accessible LLM deployment. Red Hat is committed to open, efficient AI, providing models and tools that reduce cost while maintaining state-of-the-art performance.

Explore the models today and stay tuned for upcoming performance results.

Related Posts

LLM Compressor 0.9.0: Attention quantization, MXFP4 support, and more

Advancing low‑bit quantization for LLMs: AutoRound x LLM Compressor

Optimizing generative AI models with quantization

Enable 3.5 times faster vision language models with quantization

Deployment-ready reasoning with quantized DeepSeek-R1 models

How well do quantized models handle long-context tasks?

Recent Posts

Build resilient guardrails for OpenClaw AI agents on Kubernetes

Enable Firewall-as-a-Service in OpenStack Services on OpenShift

How DNS name tracking enhances network observability

Manage AI context with the Lola package manager

Agent-driven attestation: How Keylime's push model rethinks remote integrity verification

 What’s up next?
 

Applied AI for Enterprise Java Development

 Alex Soto Bueno
 
 +2
 

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

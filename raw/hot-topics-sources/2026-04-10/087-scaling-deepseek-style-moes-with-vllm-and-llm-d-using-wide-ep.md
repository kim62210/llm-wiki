---
title: Scaling DeepSeek-style MoEs with vLLM + llm-d using Wide EP | Red Hat Developer
source_url: https://developers.redhat.com/articles/2025/09/08/scaling-deepseek-style-moes-vllm-and-llm-d-using-wide-ep
final_url: https://developers.redhat.com/articles/2025/09/08/scaling-deepseek-style-moes-vllm-and-llm-d-using-wide-ep
status: 200
content_type: text/html; charset=UTF-8
topics: [Wide Expert Parallelism (WideEP) for MoE]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.573824+00:00
---

# Scaling DeepSeek-style MoEs with vLLM + llm-d using Wide EP | Red Hat Developer

## 원본 URL

https://developers.redhat.com/articles/2025/09/08/scaling-deepseek-style-moes-vllm-and-llm-d-using-wide-ep

## 추출 본문

Scaling DeepSeek-style MoEs with vLLM + llm-d using Wide EP | Red Hat Developer
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
 

Scaling DeepSeek-style MoEs with vLLM and llm-d using Wide EP

September 8, 2025

Robert ShawTyler Smith
 Clayton Coleman (Google)
 

Related topics:Artificial intelligenceRelated products:Red Hat AI

 Table of contents:
 

Note

The contents of this article were discussed in detail during our biweekly vLLM office hours virtual event: vLLM Office Hours #29] Scaling MoE with llm-d. View the slides here and register for our future vLLM office hours, happening every other Thursday.

Support for the DeepSeek family of models and similar architectures in vLLM marks a significant advancement in the ability to efficiently serve large-scale Mixture of Experts (MoE) language models. These models bring a number of innovations to the open source LLM space, including multi-head latent attention (MLA), sparse MoE configurations with hundreds of experts, built-in speculative decoding through multi-token prediction (MTP), and architectural patterns like prefill/decode disaggregation.

In this article, we explore the architectural and kernel-level changes that make it possible to serve these models at scale. We begin with an overview of MoE fundamentals, move into the execution model changes in vLLM, and then examine how the llm-d project builds on these improvements to enable production-scale deployments in Kubernetes environments.

If you are not familiar with llm-d, it's a Kubernetes-native high-performance distributed LLM inference framework. llm-d provides a well-lit path for anyone to serve at scale, with the fastest time-to-value and competitive performance per dollar, for most models across a diverse and comprehensive set of hardware accelerators. Learn more at llm-d.ai.

Understanding Mixture of Experts

In an MoE model, the dense feed-forward multi-layer perceptron (MLP) is replaced with a sparse alternative. Tokens leaving the attention block are sent through a router, which selects the top-k experts and assigns corresponding weights for each token. These experts are specialized linear transformations, and their outputs are combined according to the assigned weights along with a shared expert output. This slide illustrates the Mixture of Experts routing process, where tokens are routed through a gate to a subset of experts and then recombined with shared output.

Many of today's largest models follow this architecture, including DeepSeek V3, DeepSeek R1, Llama 4, Qwen 3, Kimi K2, and OpenAI's gpt-oss-120b with 128 routed experts (4 activated per token). These models often use 256 or 384 experts in total, with only a small number active for each token. The smaller gpt-oss-20b follows the same style but uses just 32 experts.

The forward workflow, illustrated in this slide, begins as tokens leave attention and enter the gate. The gate determines expert IDs and weights, and these, along with the hidden states, are passed into an ExpertWiseMLP. The outputs are summed according to the expert weights and then combined with the shared expert output.

From dense to sparse MoE

While all MoEs are sparse by design, earlier implementations, such as those described in the MegaBlocks paper, used relatively few experts and could be implemented with a FusedMoE kernel and tensor parallelism. This approach was much simpler to implement and tune, making it adequate for smaller-scale models.

In contrast, once prefill/decode disaggregation and expert parallelism are introduced, the design space expands dramatically, creating a combinatorial explosion of possible execution strategies and kernel variations. The simplicity of early MoE implementations stands in stark contrast to the complexity of scaling today's large, distributed models.

The field has shifted toward extremely sparse configurations with hundreds of experts. Research from DeepSeek shows that as sparsity and the number of experts increase, model performance improves significantly. This graphillustrates the performance gains associated with higher sparsity and greater expert counts.

Challenges for FusedMoE in sparse configurations

Sparse MoEs create challenges that the older FusedMoE design cannot address efficiently. The per-expert computation becomes small enough that kernel performance suffers. The memory footprint is large, and tensor parallelism requires two all-reduce operations per layer, which is both bandwidth-heavy and inefficient for scaling. Every token must involve every GPU, making multi-node scaling impractical for very large models.

Evolving MoE execution in vLLM

To overcome these limitations, vLLM has made three major changes in MoE execution. The first is a shift from tensor parallel attention to data parallel attention paired with expert parallel MoEs. The second is the introduction of specialized communication patterns for expert parallelism. The third is the addition of optimizations such as expert parallel load balancing and overlapping communication with computation.

In the data parallel attention model, each GPU processes its own attention buffer and attention requests independently. Between the attention and MoE layers, token distribution shifts from being request-based to being expert-based. A dispatch operation sends each token to the relevant experts, and after computation, a combine operation aggregates the outputs according to the original top-k weights.

The primary advantage is that dispatch and combine are sparse operations. Each token only involves the GPUs associated with its top-k experts, which greatly improves scalability across multiple nodes.

This diagram shows data parallel attention with expert parallel MoEs, including dispatch and combine operations.

The expert parallel kernel workflow

Within this framework, the kernel workflow begins with the router assigning expert IDs to each token. The dispatch step sends tokens to their assigned experts, expert computations are performed, and the outputs are then combined using the assigned weights. This kernel workflow diagram illustrates dispatch to experts, computation, and combination across data parallel ranks.

Dispatch and combine: DeepEP and PPLX

Two main implementations are used for the dispatch and combine steps. DeepSeek's DeepEP kernels use NVIDIA's nvshmem library and come in two forms: a high-throughput mode optimized for prefill and a low-latency mode optimized for decode. Perplexity's PPLX provides a more flexible and operationally simple alternative that works well for chunked prefill scenarios and is CUDA graph compatible.

Performance varies depending on the context. In single-node settings, PPLX often outperforms DeepEP. In multi-node scenarios, DeepEP tends to deliver superior results. These graphs show the performance comparison between PPLX and DeepEP dispatch/combine kernels in single-node and multi-node tests. 

GEMM strategies for MoE

At the level of the expert computations, vLLM supports different GEMM strategies. In low-latency cases, batched GEMM is used with padded activations to maintain CUDA graph compatibility. For high-throughput cases, group GEMM is used, allowing for variable activation sizes and more efficient parallelism. These approaches are compared in this diagram.

Modular kernel framework

To support a wide range of execution styles, vLLM includes a modular kernel framework (illustrated in this slide) that breaks execution into three phases: prepare, execute, and finalize. The prepare phase can involve dispatch or permutation; execute runs the expert computations; finalize combines results or reverses permutations. 

Load balancing with EPLB

Large-scale MoEs can suffer from load imbalance when the router assigns more tokens to certain experts. vLLM's expert placement with load balancing (EPLB) addresses this by periodically rebalancing expert placement and replicating heavily used experts. This chart shows EPLB with replicated experts to balance token assignments.

Prefill/decode disaggregation

DeepSeek deployments benefit from configuring prefill and decode stages separately. vLLM supports this with prefill/decode (PD) disaggregation, which uses NVIDIA's NIXL library to transfer KV cache data from prefill instances to decode instances. This separation allows each stage to be tuned for its workload, using high-throughput kernels for prefill and low-latency kernels for decode. This diagram illustrates the request flow for PD disaggregation, showing proxy routing, prefill execution, KV cache transfer, and decode processing.

Introducing llm-d

The llm-d project extends vLLM's capabilities into production Kubernetes environments, focusing on intelligent inference scheduling, prefix-aware routing, auto-scaling strategies, and wide expert parallelism. Its architecture, illustrated in this diagram, supports complex deployments where replicas might need to communicate for PD disaggregation or prefix caching. 

Well-lit paths in llm-d

To make this modularity practical, llm-d offers well-lit paths: production-tested configurations that guide users through known deployment challenges with high confidence. These paths are backed by detailed quick start examples in the llm-d-infra GitHub repository, where each directory includes a complete reference deployment and step-by-step README.md.

These well-lit paths are not just demos, they are reference architectures for LLM serving.

Intelligent inference scheduling that accounts for request complexity and model load with support for precise prefix-cache aware routing with no additional infrastructure, out-of-the-box load-aware scheduling for better tail latency that “just works”, and a new configurable scheduling profile system that enables teams to see immediate latency wins and still customize scheduling behavior for their workloads and infrastructure.

P/D disaggregation for large models like DeepSeek that support separating prefill and decode workloads to improve latency and GPU utilization for long-context scenarios.

Wide expert parallelism to simplify scaling across large, multi-node deployments using expert and data parallelism patterns for MoE models. This includes optimized deployments leveraging NIXL+UCX for inter-node communication, with fixes and improvements to reduce latency, and demonstrates the use of 
LeaderWorkerSet
 for Kubernetes-native inference orchestration.

Live demo

Watch the following video for a live demo of the llm-d infrastructure quick start in the YDP example.

Live demo video showing llm-d infrastructure quick start in the YDP example.
Conclusion

DeepSeek-style models represent the cutting edge of sparse MoE architectures, pushing the limits of performance and scalability. Through innovations in kernel design, modular execution frameworks, and communication patterns, vLLM has evolved to serve these models efficiently at scale. 

With llm-d, these capabilities extend into production Kubernetes environments, providing intelligent scheduling, robust scaling strategies, and well-documented deployment patterns. Together, they make it possible for teams to move from prototype to production for some of the largest and most complex LLM deployments in existence.
Last updated:
 September 11, 2025

Related Posts

llm-d: Kubernetes-native distributed inferencing

Getting started with llm-d for distributed AI inference

How we optimized vLLM for DeepSeek-R1

Enable 3.5 times faster vision language models with quantization

How reinforcement learning improves DeepSeek performance

Deployment-ready reasoning with quantized DeepSeek-R1 models

Recent Posts

Build resilient guardrails for OpenClaw AI agents on Kubernetes

Enable Firewall-as-a-Service in OpenStack Services on OpenShift

How DNS name tracking enhances network observability

Manage AI context with the Lola package manager

Agent-driven attestation: How Keylime's push model rethinks remote integrity verification

 What’s up next?
 

Transform your domain expertise into intelligent applications that deliver real business value with this step-by-step guide. Begin with InstructLab model customization and progress to enterprise-scale deployment on Red Hat's trusted AI platform.

 Start the activity
 

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

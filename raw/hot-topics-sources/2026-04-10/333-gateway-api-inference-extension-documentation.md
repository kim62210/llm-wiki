---
title: Introduction - Kubernetes Gateway API Inference Extension
source_url: https://gateway-api-inference-extension.sigs.k8s.io
final_url: https://gateway-api-inference-extension.sigs.k8s.io
status: 200
content_type: text/html; charset=UTF-8
topics: [llm-d & Gateway API Inference Extension]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:09.923967+00:00
---

# Introduction - Kubernetes Gateway API Inference Extension

## 원본 URL

https://gateway-api-inference-extension.sigs.k8s.io

## 추출 본문

Introduction - Kubernetes Gateway API Inference Extension

 Skip to content
 

 Kubernetes Gateway API Inference Extension
 

 
 Introduction
 
 

 Initializing search
 

 kubernetes-sigs/gateway-api-inference-extension
 

 
 
 Overview

 

 
 
 Guides

 

 
 
 Performance

 

 
 
 Reference

 

 
 
 Enhancements

 

 
 
 Contributing

 

 Kubernetes Gateway API Inference Extension
 

 kubernetes-sigs/gateway-api-inference-extension
 

 Overview
 
 Overview
 

 Introduction
 
 Introduction
 
 Table of contents
 

 Concepts and Definitions
 

 Key Features
 

 API Resources
 

 Composable Layers
 

 Gateway API Implementations
 

 Endpoint Picker
 

 Model Server Frameworks
 

 Request Flow
 

 Who is working on Gateway API Inference Extension?
 

 Concepts
 
 Concepts
 

 API Overview
 

 Design Principles
 

 Conformance
 

 Roles and Personas
 

 Priority and Capacity
 

 Implementations
 
 Implementations
 

 Gateways
 

 Model Servers
 

 FAQ
 

 Guides
 
 Guides
 

 User Guides
 
 User Guides
 

 Getting started (Released)
 

 Getting started (Latest/Main)
 

 Use Cases
 
 Use Cases
 

 Serving Multiple Inference Pools (Latest/Main)
 

 Deploy As a Standalone Request Scheduler
 

 Flow Control
 

 Rollout
 
 Rollout
 

 Adapter Rollout
 

 InferencePool Rollout
 

 Observability
 
 Observability
 

 Metrics
 

 Traces
 

 Configuration Guide
 
 Configuration Guide
 

 Configuring the EndPoint Picker via configuration YAML file
 

 Prefix Cache Aware Plugin
 

 Resource Tuning
 

 Latency-Based Routing
 

 Migration Guide
 

 Troubleshooting Guide
 

 Implementer Guides
 
 Implementer Guides
 

 Getting started
 

 Conformance Tests
 

 Performance
 
 Performance
 

 Benchmark
 

 Advanced Benchmarking Configs
 
 Advanced Benchmarking Configs
 

 Prefix Cache Aware
 

 Decode Heavy Workload
 

 Prefill Heavy Workload
 

 Regression Testing
 

 Reference
 
 Reference
 

 v1 API Reference
 

 v1alpha1 API Reference
 
 v1alpha1 API Reference
 

 API Reference
 

 v1alpha2 API Reference
 
 v1alpha2 API Reference
 

 API Reference
 

 API Types
 
 API Types
 

 InferencePool
 

 InferenceObjective
 

 InferencePoolImport
 

 InferenceModelRewrite
 

 Enhancements
 
 Enhancements
 

 Overview
 

 Contributing
 
 Contributing
 

 How to Get Involved
 

 Table of contents
 

 Concepts and Definitions
 

 Key Features
 

 API Resources
 

 Composable Layers
 

 Gateway API Implementations
 

 Endpoint Picker
 

 Model Server Frameworks
 

 Request Flow
 

 Who is working on Gateway API Inference Extension?
 

Introduction¶

Gateway API Inference Extension is an official Kubernetes project that optimizes self-hosting Generative Models on Kubernetes.

The overall resource model focuses on 2 new inference-focused
personas and corresponding resources that
they are expected to manage:

Concepts and Definitions¶

The following specific terms to this project:

Inference Gateway: A proxy/load-balancer that has been coupled with the
 EndPointer Picker extension. It provides optimized routing and load balancing for
 serving Kubernetes self-hosted generative Artificial Intelligence (AI)
 workloads. It simplifies the deployment, management, and observability of AI
 inference workloads.

Inference Scheduler: An extendable component that makes decisions about which endpoint is optimal (best cost /
 best performance) for an inference request based on 
Metrics and Capabilities

 from Model Serving.

Metrics and Capabilities: Data provided by model serving platforms about
 performance, availability and capabilities to optimize routing. Includes
 things like Prefix Cache status or LoRA Adapters availability.

Endpoint Picker(EPP): An implementation of an 
Inference Scheduler
 with additional Routing, Flow, and Request Control layers to allow for sophisticated routing strategies. Additional info on the architecture of the EPP here.

Body Based Router(BBR): An additional (and optional) implementation of an extension that extracts information from the body portion of the inference request, currently the model name attribute from the body of an OpenAI API request, which can then be used by the gateway to perform model-aware functions such as routing/scheduling. This may be used along with the EPP in order to have a combination of model picking and endpoint picking functionality.

Key Features¶

Gateway API Inference Extension optimizes self-hosting Generative AI Models on Kubernetes.
It provides optimized load-balancing for self-hosted Generative AI Models on Kubernetes.
The project’s goal is to improve and standardize routing to inference workloads across the ecosystem.

This is achieved by leveraging Envoy's External Processing to extend any gateway that supports both ext-proc and Gateway API into an inference gateway.
This extension extends popular gateways like Envoy Gateway, kgateway, and GKE Gateway - to become Inference Gateway -
supporting inference platform teams self-hosting Generative Models (with a current focus on large language models) on Kubernetes.
This integration makes it easy to expose and control access to your local OpenAI-compatible chat completion endpoints
to other workloads on or off cluster, or to integrate your self-hosted models alongside model-as-a-service providers
in a higher level AI Gateways like LiteLLM, Gloo AI Gateway, or Apigee.

Model-aware routing: Instead of simply routing based on the path of the request, an inference gateway allows you to route to models based on the model names. This is enabled by support for GenAI Inference API specifications (such as OpenAI API) in the gateway implementations such as in Envoy Proxy. This model-aware routing also extends to Low-Rank Adaptation (LoRA) fine-tuned models.

Serving priority: an inference gateway allows you to specify the serving priority of your models. For example, you can specify that your models for online inference of chat tasks (which is more latency sensitive) have a higher Priority than a model for latency tolerant tasks such as a summarization. 

Model rollouts: an inference gateway allows you to incrementally roll out new model versions by traffic splitting definitions based on the model names. 

Extensibility for Inference Services: an inference gateway defines extensibility pattern for additional Inference services to create bespoke routing capabilities should out of the box solutions not fit your needs.

Customizable Load Balancing for Inference: an inference gateway defines a pattern for customizable load balancing and request routing that is optimized for Inference. An inference gateway provides a reference implementation of model endpoint picking leveraging metrics emitted from the model servers. This endpoint picking mechanism can be used in lieu of traditional load balancing mechanisms. Model Server-aware load balancing ("smart" load balancing as its sometimes referred to in this repo) has been proven to reduce the serving latency and improve utilization of accelerators in your clusters.

By achieving these, the project aims to reduce latency and improve accelerator (GPU) utilization for AI workloads.

API Resources¶

Head to our API overview to start exploring our APIs!

Composable Layers¶

This project aims to define specifications to enable a compatible ecosystem for
extending the Gateway API with custom endpoint selection algorithms. This
project defines a set of patterns across three distinct layers of components
that are relevant to this project:

Gateway API Implementations¶

Gateway API has more than 25
implementations. As this
pattern stabilizes, we expect a wide set of these implementations to support
this project to become an inference gateway

Endpoint Picker¶

As part of this project, we've built the Endpoint Picker. A pluggable & extensible ext-proc deployment that implements this architecture.

Model Server Frameworks¶

This project will work closely with model server frameworks to establish a
shared standard for interacting with these extensions, particularly focused on
metrics and observability so extensions will be able to make informed routing
decisions. The project is currently focused on integrations with
vLLM and
Triton, and will be open to
other integrations as they are requested.

Request Flow¶

To illustrate how this all comes together, it may be helpful to walk through a
sample request.

The first step involves the Gateway selecting the correct InferencePool
(set of endpoints running a model server framework) or Service to route to. This
logic is based on the existing Gateway and HTTPRoute APIs, and will be familiar
to any Gateway API users or implementers.

If the request should be routed to an InferencePool, the Gateway will forward
the request information to the endpoint selection extension for that pool.

The inference gateway will fetch metrics from whichever portion of the InferencePool
endpoints can best achieve the configured objectives. Note that this kind of
metrics probing may happen asynchronously, depending on the inference gateway.

The inference gateway will instruct the Gateway which endpoint the request should be
routed to.

The Gateway will route the request to the desired endpoint.

Who is working on Gateway API Inference Extension?¶

This project is being driven by
WG-ServingSIG-Network
to improve and standardize routing to inference workloads in Kubernetes. Check
out the implementations reference to see the latest
projects & products that support this project. If you are interested in
contributing to or building an implementation using Gateway API then don’t
hesitate to get involved!

 Back to top

 
 
 Made with
 
 Material for MkDocs

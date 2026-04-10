---
title: Intelligent Semantic Routing — production-stack
source_url: https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.html
final_url: https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.html
status: 200
content_type: text/html; charset=utf-8
topics: [vLLM Semantic Router (Iris / Athena)]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:10.508247+00:00
---

# Intelligent Semantic Routing — production-stack

## 원본 URL

https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.html

## 추출 본문

Intelligent Semantic Routing — production-stack
Skip to main content

Back to topCtrl+K

SearchCtrl+K

Getting Started

Prerequisite

Quick Start

FAQ

Deployment

Deployment Overview
Helm Chart Deployment

CRD Deployment

Gateway Inference Extension

Use Cases

KV Cache Aware Routing

Prefix Aware Routing

Disaggregated Prefill

Sharing KV Cache Across Instances

Benchmarking

Distributed Tracing

Tool Enabled Installation

Pipeline Parallelism with KubeRay

Sleep and Wakeup Mode

Autoscaling with KEDA

Intelligent Semantic Routing

Developer Guide

Contributing

Docker Guide

Community

Community Meetings

Repository

Suggest edit

.rst

.pdf

Intelligent Semantic Routing

 Contents 

What is vLLM Semantic Router?

Benefits of Integration

Table of Contents

Prerequisites

Step 1: Deploy the vLLM Production Stack

Step 2: Deploy vLLM Semantic Router

Step 3: Test the Deployment

Troubleshooting

Conclusion

Intelligent Semantic Routing#

This use case demonstrates how to integrate the vLLM Semantic Router with the vLLM Production Stack to create an intelligent Mixture-of-Models (MoM) system. The Semantic Router operates as an Envoy External Processor that semantically routes OpenAI API-compatible requests to the most suitable backend model using BERT-based or decoder-only LoRA classification, prompt guard, and semantic caching, improving both quality and cost efficiency.

What is vLLM Semantic Router?#

The vLLM Semantic Router provides:

Auto-selection of models: Routes math, creative writing, code, and general queries to the best-fit models

Security & privacy: PII detection, prompt guard, and safe routing for sensitive prompts

Performance optimizations: Semantic cache and better tool selection to cut latency and tokens

Architecture: Tight Envoy ExtProc integration with dual Go and Rust implementations

Monitoring: Console, Grafana dashboards, Prometheus metrics, and tracing for full visibility

Learn more: vLLM Semantic Router

Benefits of Integration#

The vLLM Production Stack provides deployment capabilities that spin up vLLM servers with traffic routing to different models, service discovery and fault tolerance through the Kubernetes API, and support for round-robin, session-based, prefix-aware, KV-aware and disaggregated-prefill routing with LMCache native support.

The Semantic Router adds a system-intelligence layer that:

Classifies each user request

Selects the most suitable model from a pool

Injects domain-specific system prompts

Performs semantic caching

Enforces enterprise-grade security checks such as PII and jailbreak detection

By combining these two systems, you obtain a unified inference stack where semantic routing ensures that each request is answered by the best possible model, while Production-Stack routing maximizes infrastructure and inference efficiency with rich metrics.

Table of Contents#

Prerequisites

Step 1: Deploy the vLLM Production Stack

Step 2: Deploy vLLM Semantic Router

Step 3: Test the Deployment

Troubleshooting

Prerequisites#

kubectl

Helm

A Kubernetes cluster (kind, minikube, GKE, etc.)

Completion of Prerequisite and Quick Start

Step 1: Deploy the vLLM Production Stack#

Deploy the vLLM Production Stack using the provided Helm values file:

helmrepoaddvllm-production-stackhttps://vllm-project.github.io/production-stack
helminstallvllm-stackvllm-production-stack/vllm-stack-fhttps://github.com/vllm-project/production-stack/blob/main/tutorials/assets/values-23-SR.yaml

The sample values file configures:

Model: Qwen/Qwen3-8B with 2 replicas

Router: Round-robin routing logic with session key support

Resources: 8 CPU, 16Gi memory, 1 GPU per instance

Identify the ClusterIP and port of your router Service:

kubectlgetsvcvllm-router-service
# Note the router service ClusterIP and port (e.g., 10.97.254.122:80)

Step 2: Deploy vLLM Semantic Router#

Follow the official Install in Kubernetes guide with the updated configuration.

Deploy vLLM Semantic Router using Helm:

# Deploy vLLM Semantic Router with custom values from GHCR OCI registry# (Optional) If you use a registry mirror/proxy, append: --set global.imageRegistry=<your-registry>
helminstallsemantic-routeroci://ghcr.io/vllm-project/charts/semantic-router\--versionv0.0.0-latest\--namespacevllm-semantic-router-system\--create-namespace\-fhttps://raw.githubusercontent.com/vllm-project/semantic-router/refs/heads/main/deploy/kubernetes/ai-gateway/semantic-router-values/values.yaml

kubectlwait--for=condition=Availabledeployment/semantic-router\-nvllm-semantic-router-system--timeout=600s

# Install Envoy Gateway
helmupgrade-iegoci://docker.io/envoyproxy/gateway-helm\--versionv0.0.0-latest\--namespaceenvoy-gateway-system\--create-namespace\-fhttps://raw.githubusercontent.com/envoyproxy/ai-gateway/main/manifests/envoy-gateway-values.yaml

# Install Envoy AI Gateway
helmupgrade-iaiegoci://docker.io/envoyproxy/ai-gateway-helm\--versionv0.0.0-latest\--namespaceenvoy-ai-gateway-system\--create-namespace

# Install Envoy AI Gateway CRDs
helmupgrade-iaieg-crdoci://docker.io/envoyproxy/ai-gateway-crds-helm\--versionv0.0.0-latest\--namespaceenvoy-ai-gateway-system

# Wait for AI Gateway to be ready
kubectlwait--timeout=300s-nenvoy-ai-gateway-system\deployment/ai-gateway-controller--for=condition=Available

Note

The values file contains the configuration for the semantic router including domain classification, LoRA routing, and plugin settings. You can download and customize it from the semantic-router-values to match your vLLM Production Stack setup.

Create LLM Demo Backends and AI Gateway Routes:

# Apply LLM demo backends
kubectlapply-fhttps://raw.githubusercontent.com/vllm-project/semantic-router/refs/heads/main/deploy/kubernetes/ai-gateway/aigw-resources/base-model.yaml

# Apply AI Gateway routes
kubectlapply-fhttps://raw.githubusercontent.com/vllm-project/semantic-router/refs/heads/main/deploy/kubernetes/ai-gateway/aigw-resources/gwapi-resources.yaml

Step 3: Test the Deployment#

Port-forward to the Envoy service:

exportENVOY_SERVICE=$(kubectlgetsvc-nenvoy-gateway-system\--selector=gateway.envoyproxy.io/owning-gateway-namespace=default,gateway.envoyproxy.io/owning-gateway-name=semantic-router\-ojsonpath='{.items[0].metadata.name}')

kubectlport-forward-nenvoy-gateway-systemsvc/$ENVOY_SERVICE8080:80

Send a chat completions request:

curl-i-XPOSThttp://localhost:8080/v1/chat/completions\-H"Content-Type: application/json"\-d'{ "model": "MoM", "messages": [ {"role": "user", "content": "What is the derivative of f(x) = x^3?"} ] }'

The semantic router will analyze the request, identify it as a math query, and route it to the appropriate model through the vLLM Production Stack router.

Troubleshooting#

Gateway not accessible: Check the Gateway and Envoy service status

Semantic router not responding: Check pod status and logs with 
kubectllogs-nvllm-semantic-router-system

Error codes returned: Check the production stack router logs with 
kubectllogs

Conclusion#

In this use case, we’ve demonstrated how to:

Deploy vLLM Production Stack with a router service

Integrate vLLM Semantic Router with the production stack

Configure Envoy Gateway and AI Gateway for intelligent routing

Test the end-to-end semantic routing functionality

This integration provides a powerful combination of semantic intelligence and production-grade infrastructure, enabling efficient, secure, and intelligent model routing for diverse workloads.

Note

Preview Version: This guide is based on the preview version of vLLM Semantic Router integration. The deployment steps, configuration options, and API interfaces may change in future releases as the feature evolves. Please refer to the latest documentation for updates.

previous

Autoscaling with KEDA

next

Contributing

 Contents
 

What is vLLM Semantic Router?

Benefits of Integration

Table of Contents

Prerequisites

Step 1: Deploy the vLLM Production Stack

Step 2: Deploy vLLM Semantic Router

Step 3: Test the Deployment

Troubleshooting

Conclusion

By vLLM Production Stack Team

 
 © Copyright 2025, vLLM Production Stack Team.

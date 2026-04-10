---
title: Prefill/decode disaggregation — Ray 2.54.1
source_url: https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html
final_url: https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html
status: 200
content_type: text/html; charset=utf-8
topics: [Disaggregated Prefill/Decode Serving]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:05.574078+00:00
---

# Prefill/decode disaggregation — Ray 2.54.1

## 원본 URL

https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html

## 추출 본문

Prefill/decode disaggregation — Ray 2.54.1Skip to main content

 Back to top
 

Ctrl+K

Try Ray with $100 credit — Start now×

 Site Navigation
 

Get Started

Use Cases

Example Gallery

Library

Ray CoreScale general Python applications

Ray DataScale data ingest and preprocessing

Ray TrainScale machine learning training

Ray TuneScale hyperparameter tuning

Ray ServeScale model serving

Ray RLlibScale reinforcement learning

Docs

Resources

Discussion ForumGet your Ray questions answered

TrainingHands-on learning

BlogUpdates, best practices, user-stories

EventsWebinars, meetups, office hours

Success StoriesReal-world workload examples

EcosystemLibraries integrated with Ray

CommunityConnect with us

Try Managed Ray

 Site Navigation
 

Get Started

Use Cases

Example Gallery

Library

Ray CoreScale general Python applications

Ray DataScale data ingest and preprocessing

Ray TrainScale machine learning training

Ray TuneScale hyperparameter tuning

Ray ServeScale model serving

Ray RLlibScale reinforcement learning

Docs

Resources

Discussion ForumGet your Ray questions answered

TrainingHands-on learning

BlogUpdates, best practices, user-stories

EventsWebinars, meetups, office hours

Success StoriesReal-world workload examples

EcosystemLibraries integrated with Ray

CommunityConnect with us

Try Managed Ray

Overview

Getting Started

Installation

Use Cases
Ray for ML Infrastructure

Examples
Multi-modal AI pipeline
Batch inference

Distributed training

Online serving

LLM training and inference

Audio batch inference

Distributed XGBoost pipeline
Distributed training of an XGBoost model

Model validation using offline batch inference

Scalable online XGBoost inference with Ray Serve

Time-series forecasting
Distributed training of a DLinear time-series model

DLinear model validation using offline batch inference

Online serving for DLinear model using Ray Serve

Scalable video processing
Fine-tuning a face mask detection model with Faster R-CNN

Object detection batch inference on test dataset and metrics calculation

Video processing with object detection using batch inference

Host an object detection model as a service

Distributed RAG pipeline
Build a Regular RAG Document Ingestion Pipeline (No Ray required)

Scalable RAG Data Ingestion and Pagination with Ray Data

Deploy LLM with Ray Serve LLM

Build Basic RAG App

Improve RAG with Prompt Engineering

Evaluate RAG with Online Inference

Evaluate RAG using Batch Inference with Ray Data LLM

Deploy MCP servers
Deploying a custom MCP in Streamable HTTP mode with Ray Serve

Deploy an MCP Gateway with existing Ray Serve apps

Deploying an MCP STDIO Server as a scalable HTTP service with Ray Serve

Deploying multiple MCP services with Ray Serve

Build a Docker image for an MCP server

Build a tool-using agent

Ecosystem

Ray Core
Key Concepts

User Guides
Tasks
Nested Remote Functions

Actors
Named Actors

Terminating Actors

AsyncIO / Concurrency for Actors

Limiting Concurrency Per-Method with Concurrency Groups

Utility Classes

Out-of-band Communication

Actor Task Execution Order

Objects
Serialization

Object Spilling

Environment Dependencies

Scheduling
Use labels to control scheduling

Resources

Accelerator Support

Placement Groups

Memory Management

Out-Of-Memory Prevention

Fault tolerance
Task Fault Tolerance

Actor Fault Tolerance

Object Fault Tolerance

Node Fault Tolerance

GCS Fault Tolerance

Design Patterns & Anti-patterns
Pattern: Using nested tasks to achieve nested parallelism

Pattern: Using generators to reduce heap memory usage

Pattern: Using ray.wait to limit the number of pending tasks

Pattern: Using resources to limit the number of concurrently running tasks

Pattern: Using asyncio to run actor methods concurrently

Pattern: Using an actor to synchronize other tasks and actors

Pattern: Using a supervisor actor to manage a tree of actors

Pattern: Using pipelining to increase throughput

Anti-pattern: Returning ray.put() ObjectRefs from a task harms performance and fault tolerance

Anti-pattern: Calling ray.get on task arguments harms performance

Anti-pattern: Calling ray.get in a loop harms parallelism

Anti-pattern: Calling ray.get unnecessarily harms performance

Anti-pattern: Processing results in submission order using ray.get increases runtime

Anti-pattern: Fetching too many objects at once with ray.get causes failure

Anti-pattern: Over-parallelizing with too fine-grained tasks harms speedup

Anti-pattern: Redefining the same remote function or class harms performance

Anti-pattern: Passing the same large argument by value repeatedly harms performance

Anti-pattern: Closure capturing large objects harms performance

Anti-pattern: Using global variables to share state between tasks and actors

Anti-pattern: Serialize ray.ObjectRef out of band

Anti-pattern: Forking new processes in application code

Ray Direct Transport (RDT)

Ray Compiled Graph (beta)
Quickstart

Profiling

Experimental: Overlapping communication and computation

Troubleshooting

Compiled Graph API

Resource Isolation With Cgroup v2

Advanced topics
Tips for first-time users

Type hints in Ray

Starting Ray

Ray Generators

Using Namespaces

Cross-language programming

Working with Jupyter Notebooks & JupyterLab

Lazy Computation Graphs with the Ray DAG API

Miscellaneous Topics

Authenticating Remote URIs in runtime_env

Lifetimes of a User-Spawn Process

Head Node Memory Management

Examples
Batch Prediction with Ray Core

A Gentle Introduction to Ray Core by Example

Using Ray for Highly Parallelizable Tasks

A Simple MapReduce Example with Ray Core

Monte Carlo Estimation of π

Simple Parallel Model Selection

Parameter Server

Learning to Play Pong

Speed up your web crawler by parallelizing it with Ray

Ray Core API
Core API

Scheduling API

Runtime Env API

Utility

Exceptions

Ray Core CLI

State CLI

State API

Ray Direct Transport (RDT) API

Internals
Task Lifecycle

Autoscaler v2

RPC Fault Tolerance

Token Authentication

Metric Exporter Infrastructure

Ray Event Exporter Infrastructure

Port Service Discovery

Ray Data
Ray Data Quickstart

Key Concepts

User Guides
Loading Data

Inspecting Data

Transforming Data

Aggregating Data

Iterating over Data

Joining Data

Shuffling Data

Saving Data

Working with Images

Working with Text

Working with Tensors / NumPy

Working with PyTorch

Working with LLMs

Monitoring Your Workload

Execution Configurations

End-to-end: Offline Batch Inference

Advanced: Performance Tips and Tuning

Advanced: Read and Write Custom File Types

Examples

Ray Data API
Loading Data API

Saving Data API

Dataset API

DataIterator API

ExecutionOptions API

Checkpoint API

Aggregation API

GroupedData API

Expressions API

Data types

Global configuration

Preprocessor

Large Language Model (LLM) API

API Guide for Users from Other Data Libraries

Contributing to Ray Data
Contributing Guide

How to write tests

Comparing Ray Data to other systems

Ray Data Benchmarks

Ray Data Internals

Ray Train
Overview

PyTorch Guide

PyTorch Lightning Guide

Hugging Face Transformers Guide

XGBoost Guide

JAX Guide

More Frameworks
Hugging Face Accelerate Guide

DeepSpeed Guide

TensorFlow and Keras Guide

LightGBM Guide

Horovod Guide

User Guides
Data Loading and Preprocessing

Configuring Scale and GPUs

Local Mode

Configuring Persistent Storage

Monitoring and Logging Metrics

Saving and Loading Checkpoints

Validating checkpoints asynchronously

Experiment Tracking

Inspecting Training Results

Handling Failures and Node Preemption

Ray Train Metrics

Reproducibility

Hyperparameter Optimization

Advanced: Scaling out expensive collate functions

Tutorials
Introduction to Ray Train workloads

Computer vision pattern

Tabular workload pattern

Time series workload pattern

Generative computer vision pattern

Diffusion policy pattern

Recommendation system pattern

Examples

Benchmarks

Ray Train API

Ray Tune
Getting Started

Key Concepts

User Guides
Running Basic Experiments

Logging and Outputs in Tune

Setting Trial Resources

Using Search Spaces

How to Define Stopping Criteria for a Ray Tune Experiment

How to Save and Load Trial Checkpoints

How to Configure Persistent Storage in Ray Tune

How to Enable Fault Tolerance in Ray Tune

Using Callbacks and Metrics

Getting Data in and out of Tune

Analyzing Tune Experiment Results

A Guide to Population Based Training with Tune
Visualizing and Understanding PBT

Deploying Tune in the Cloud

Tune Architecture

Scalability Benchmarks

Ray Tune Examples
PyTorch Example

PyTorch Lightning Example

XGBoost Example

LightGBM Example

Hugging Face Transformers Example

Ray RLlib Example

Keras Example

PyTorch with ASHA

Weights & Biases Example

MLflow Example

Aim Example

Comet Example

Ax Example

HyperOpt Example

Bayesopt Example

BOHB Example

Nevergrad Example

Optuna Example

Ray Tune FAQ

Ray Tune API
Tune Execution (tune.Tuner)

Tune Experiment Results (tune.ResultGrid)

Training in Tune (tune.Trainable, tune.report)

Tune Search Space API

Tune Search Algorithms (tune.search)

Tune Trial Schedulers (tune.schedulers)

Tune Stopping Mechanisms (tune.stopper)

Tune Console Output (Reporters)

Syncing in Tune

Tune Loggers (tune.logger)

Tune Callbacks (tune.Callback)

Environment variables used by Ray Tune

External library integrations for Ray Tune

Tune Internals

Tune CLI (Experimental)

Ray Serve
Getting Started

Key Concepts

Develop and Deploy an ML Application

Deploy Compositions of Models

Deploy Multiple Applications

Model Multiplexing

Model Registry Integration

Configure Ray Serve deployments

Set Up FastAPI and HTTP

Serving LLMs
Quickstart

Examples

User Guides
Cross-node parallelism

Data parallel attention

Deployment Initialization

Prefill/decode disaggregation

KV cache offloading

Prefix-aware routing

Multi-LoRA deployment

vLLM compatibility

Fractional GPU serving

Observability and monitoring

Architecture
Architecture overview

Core components

Serving patterns

Request routing

Benchmarks

Troubleshooting

Production Guide
Serve Config Files

Deploy on Kubernetes

Custom Docker Images

Add End-to-End Fault Tolerance

Handle Dependencies

Best practices in production

Monitor Your Application

Resource Allocation

Ray Serve Autoscaling

Asynchronous Inference

Advanced Guides
Pass Arguments to Applications

Advanced Ray Serve Autoscaling

Asyncio and concurrency best practices in Ray Serve

Performance Tuning

Dynamic Request Batching

Updating Applications In-Place

Development Workflow

Set Up a gRPC Service

Replica ranks

Replica scheduling

Experimental Java API

Deploy on VM

Run Multiple Applications in Different Containers

Use Custom Algorithm for Request Routing

Troubleshoot multi-node GPU serving on KubeRay

Architecture

Examples

Ray Serve API

Ray RLlib
Getting Started

Key concepts

Environments
Multi-Agent Environments

Hierarchical Environments

External Environments and Applications

AlgorithmConfig API

Algorithms

User Guides
Advanced Python APIs

Callbacks

Checkpointing

MetricsLogger API

Episodes

ConnectorV2 and ConnectorV2 pipelines
Env-to-module pipelines

Learner connector pipelines

Replay Buffers

Working with offline data

RL Modules

Learner (Alpha)

Fault Tolerance And Elastic Training

Install RLlib for Development

RLlib scaling guide

Examples

New API stack migration guide

Ray RLlib API
Algorithm Configuration API
ray.rllib.algorithms.algorithm_config.AlgorithmConfig

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.build_algo

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.build_learner_group

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.build_learner

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.is_multi_agent

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.is_offline

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.learner_class

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.model_config

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.rl_module_spec

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.total_train_batch_size

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.get_default_learner_class

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.get_default_rl_module_spec

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.get_evaluation_config_object

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.get_multi_rl_module_spec

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.get_multi_agent_setup

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.get_rollout_fragment_length

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.copy

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.validate

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.freeze

Algorithms
ray.rllib.algorithms.algorithm.Algorithm

ray.rllib.algorithms.algorithm.Algorithm.setup

ray.rllib.algorithms.algorithm.Algorithm.get_default_config

ray.rllib.algorithms.algorithm.Algorithm.env_runner

ray.rllib.algorithms.algorithm.Algorithm.eval_env_runner

ray.rllib.algorithms.algorithm.Algorithm.train

ray.rllib.algorithms.algorithm.Algorithm.training_step

ray.rllib.algorithms.algorithm.Algorithm.save_to_path

ray.rllib.algorithms.algorithm.Algorithm.restore_from_path

ray.rllib.algorithms.algorithm.Algorithm.from_checkpoint

ray.rllib.algorithms.algorithm.Algorithm.get_state

ray.rllib.algorithms.algorithm.Algorithm.set_state

ray.rllib.algorithms.algorithm.Algorithm.evaluate

ray.rllib.algorithms.algorithm.Algorithm.get_module

ray.rllib.algorithms.algorithm.Algorithm.add_policy

ray.rllib.algorithms.algorithm.Algorithm.remove_policy

Callback APIs
ray.rllib.callbacks.callbacks.RLlibCallback

ray.rllib.callbacks.callbacks.RLlibCallback.on_algorithm_init

ray.rllib.callbacks.callbacks.RLlibCallback.on_sample_end

ray.rllib.callbacks.callbacks.RLlibCallback.on_train_result

ray.rllib.callbacks.callbacks.RLlibCallback.on_evaluate_start

ray.rllib.callbacks.callbacks.RLlibCallback.on_evaluate_end

ray.rllib.callbacks.callbacks.RLlibCallback.on_env_runners_recreated

ray.rllib.callbacks.callbacks.RLlibCallback.on_checkpoint_loaded

ray.rllib.callbacks.callbacks.RLlibCallback.on_environment_created

ray.rllib.callbacks.callbacks.RLlibCallback.on_episode_created

ray.rllib.callbacks.callbacks.RLlibCallback.on_episode_start

ray.rllib.callbacks.callbacks.RLlibCallback.on_episode_step

ray.rllib.callbacks.callbacks.RLlibCallback.on_episode_end

Environments
EnvRunner API

SingleAgentEnvRunner API

SingleAgentEpisode API

MultiAgentEnv API

MultiAgentEnvRunner API

MultiAgentEpisode API

External Envs

Env Utils

RLModule APIs
ray.rllib.core.rl_module.rl_module.RLModuleSpec

ray.rllib.core.rl_module.rl_module.RLModuleSpec.build

ray.rllib.core.rl_module.rl_module.RLModuleSpec.module_class

ray.rllib.core.rl_module.rl_module.RLModuleSpec.observation_space

ray.rllib.core.rl_module.rl_module.RLModuleSpec.action_space

ray.rllib.core.rl_module.rl_module.RLModuleSpec.inference_only

ray.rllib.core.rl_module.rl_module.RLModuleSpec.learner_only

ray.rllib.core.rl_module.rl_module.RLModuleSpec.model_config

ray.rllib.core.rl_module.multi_rl_module.MultiRLModuleSpec

ray.rllib.core.rl_module.multi_rl_module.MultiRLModuleSpec.build

ray.rllib.core.rl_module.default_model_config.DefaultModelConfig

ray.rllib.core.rl_module.rl_module.RLModule

ray.rllib.core.rl_module.rl_module.RLModule.observation_space

ray.rllib.core.rl_module.rl_module.RLModule.action_space

ray.rllib.core.rl_module.rl_module.RLModule.inference_only

ray.rllib.core.rl_module.rl_module.RLModule.model_config

ray.rllib.core.rl_module.rl_module.RLModule.setup

ray.rllib.core.rl_module.rl_module.RLModule.as_multi_rl_module

ray.rllib.core.rl_module.rl_module.RLModule.forward_exploration

ray.rllib.core.rl_module.rl_module.RLModule.forward_inference

ray.rllib.core.rl_module.rl_module.RLModule.forward_train

ray.rllib.core.rl_module.rl_module.RLModule._forward

ray.rllib.core.rl_module.rl_module.RLModule._forward_exploration

ray.rllib.core.rl_module.rl_module.RLModule._forward_inference

ray.rllib.core.rl_module.rl_module.RLModule._forward_train

ray.rllib.core.rl_module.rl_module.RLModule.save_to_path

ray.rllib.core.rl_module.rl_module.RLModule.restore_from_path

ray.rllib.core.rl_module.rl_module.RLModule.from_checkpoint

ray.rllib.core.rl_module.rl_module.RLModule.get_state

ray.rllib.core.rl_module.rl_module.RLModule.set_state

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.setup

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.as_multi_rl_module

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.add_module

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.remove_module

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.save_to_path

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.restore_from_path

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.from_checkpoint

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.get_state

ray.rllib.core.rl_module.multi_rl_module.MultiRLModule.set_state

Distribution API
ray.rllib.models.distributions.Distribution

ray.rllib.models.distributions.Distribution.from_logits

ray.rllib.models.distributions.Distribution.sample

ray.rllib.models.distributions.Distribution.rsample

ray.rllib.models.distributions.Distribution.logp

ray.rllib.models.distributions.Distribution.kl

LearnerGroup API
ray.rllib.algorithms.algorithm_config.AlgorithmConfig.learners

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.build_learner_group

ray.rllib.core.learner.learner_group.LearnerGroup

Offline RL API
ray.rllib.algorithms.algorithm_config.AlgorithmConfig.offline_data

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.learners

ray.rllib.algorithms.algorithm_config.AlgorithmConfig.env_runners

ray.rllib.offline.offline_env_runner.OfflineSingleAgentEnvRunner

ray.rllib.offline.offline_data.OfflineData

ray.rllib.offline.offline_data.OfflineData.__init__

ray.rllib.offline.offline_data.OfflineData.sample

ray.rllib.offline.offline_data.OfflineData.default_map_batches_kwargs

ray.rllib.offline.offline_data.OfflineData.default_iter_batches_kwargs

ray.rllib.offline.offline_prelearner.OfflinePreLearner

ray.rllib.offline.offline_prelearner.OfflinePreLearner.__init__

ray.rllib.offline.offline_prelearner.SCHEMA

ray.rllib.offline.offline_prelearner.OfflinePreLearner.__call__

ray.rllib.offline.offline_prelearner.OfflinePreLearner._map_to_episodes

ray.rllib.offline.offline_prelearner.OfflinePreLearner._map_sample_batch_to_episode

ray.rllib.offline.offline_prelearner.OfflinePreLearner._should_module_be_updated

ray.rllib.offline.offline_prelearner.OfflinePreLearner.default_prelearner_buffer_class

ray.rllib.offline.offline_prelearner.OfflinePreLearner.default_prelearner_buffer_kwargs

ConnectorV2 API

Replay Buffer API
ray.rllib.utils.replay_buffers.replay_buffer.StorageUnit

ray.rllib.utils.replay_buffers.replay_buffer.ReplayBuffer

ray.rllib.utils.replay_buffers.prioritized_replay_buffer.PrioritizedReplayBuffer

ray.rllib.utils.replay_buffers.reservoir_replay_buffer.ReservoirReplayBuffer

ray.rllib.utils.replay_buffers.replay_buffer.ReplayBuffer.sample

ray.rllib.utils.replay_buffers.replay_buffer.ReplayBuffer.add

ray.rllib.utils.replay_buffers.replay_buffer.ReplayBuffer.get_state

ray.rllib.utils.replay_buffers.replay_buffer.ReplayBuffer.set_state

ray.rllib.utils.replay_buffers.multi_agent_replay_buffer.MultiAgentReplayBuffer

ray.rllib.utils.replay_buffers.multi_agent_prioritized_replay_buffer.MultiAgentPrioritizedReplayBuffer

ray.rllib.utils.replay_buffers.utils.update_priorities_in_replay_buffer

ray.rllib.utils.replay_buffers.utils.sample_min_n_steps_from_buffer

RLlib Utilities
ray.rllib.utils.metrics.metrics_logger.MetricsLogger

ray.rllib.utils.metrics.metrics_logger.MetricsLogger.peek

ray.rllib.utils.metrics.metrics_logger.MetricsLogger.log_value

ray.rllib.utils.metrics.metrics_logger.MetricsLogger.log_dict

ray.rllib.utils.metrics.metrics_logger.MetricsLogger.aggregate

ray.rllib.utils.metrics.metrics_logger.MetricsLogger.log_time

ray.rllib.utils.schedules.scheduler.Scheduler

ray.rllib.utils.schedules.scheduler.Scheduler.validate

ray.rllib.utils.schedules.scheduler.Scheduler.get_current_value

ray.rllib.utils.schedules.scheduler.Scheduler.update

ray.rllib.utils.schedules.scheduler.Scheduler._create_tensor_variable

ray.rllib.utils.framework.try_import_torch

ray.rllib.utils.torch_utils.clip_gradients

ray.rllib.utils.torch_utils.compute_global_norm

ray.rllib.utils.torch_utils.convert_to_torch_tensor

ray.rllib.utils.torch_utils.explained_variance

ray.rllib.utils.torch_utils.flatten_inputs_to_1d_tensor

ray.rllib.utils.torch_utils.global_norm

ray.rllib.utils.torch_utils.one_hot

ray.rllib.utils.torch_utils.reduce_mean_ignore_inf

ray.rllib.utils.torch_utils.sequence_mask

ray.rllib.utils.torch_utils.set_torch_seed

ray.rllib.utils.torch_utils.softmax_cross_entropy_with_logits

ray.rllib.utils.torch_utils.update_target_network

ray.rllib.utils.numpy.aligned_array

ray.rllib.utils.numpy.concat_aligned

ray.rllib.utils.numpy.convert_to_numpy

ray.rllib.utils.numpy.fc

ray.rllib.utils.numpy.flatten_inputs_to_1d_tensor

ray.rllib.utils.numpy.make_action_immutable

ray.rllib.utils.numpy.huber_loss

ray.rllib.utils.numpy.l2_loss

ray.rllib.utils.numpy.lstm

ray.rllib.utils.numpy.one_hot

ray.rllib.utils.numpy.relu

ray.rllib.utils.numpy.sigmoid

ray.rllib.utils.numpy.softmax

ray.rllib.utils.checkpoints.try_import_msgpack

ray.rllib.utils.checkpoints.Checkpointable

More Libraries
Distributed Scikit-learn / Joblib

Distributed multiprocessing.Pool

Ray Collective Communication Lib

Using Dask on Ray
ray.util.dask.RayDaskCallback
ray.util.dask.RayDaskCallback.ray_active

ray.util.dask.callbacks.RayDaskCallback._ray_presubmit

ray.util.dask.callbacks.RayDaskCallback._ray_postsubmit

ray.util.dask.callbacks.RayDaskCallback._ray_pretask

ray.util.dask.callbacks.RayDaskCallback._ray_posttask

ray.util.dask.callbacks.RayDaskCallback._ray_postsubmit_all

ray.util.dask.callbacks.RayDaskCallback._ray_finish

Using Spark on Ray (RayDP)

Using Mars on Ray

Using Pandas on Ray (Modin)

Distributed Data Processing in Data-Juicer

Ray Clusters
Key Concepts

Deploying on Kubernetes
Getting Started with KubeRay
KubeRay Operator Installation

RayCluster Quickstart

RayJob Quickstart

RayService Quickstart

User Guides
Deploy Ray Serve Apps

RayService worker Pods aren’t ready

RayService high availability

RayService Zero-Downtime Incremental Upgrades

KubeRay Observability

KubeRay upgrade guide

Managed Kubernetes services

Best Practices for Storage and Dependencies

RayCluster Configuration

KubeRay Autoscaling

KubeRay label-based scheduling

GCS fault tolerance in KubeRay

Tuning Redis for a Persistent Fault Tolerant GCS

Configuring KubeRay to use Google Cloud Storage Buckets in GKE

Persist KubeRay custom resource logs

Persist KubeRay Operator Logs

Using GPUs

Use TPUs with KubeRay

Specify container commands for Ray head/worker Pods

Helm Chart RBAC

TLS Authentication

(Advanced) Understanding the Ray Autoscaler in the Context of Kubernetes

Use kubectl plugin (beta)

Configure Ray clusters to use token authentication

Reducing image pull latency on Kubernetes

Using 
uv
 for Python package management in KubeRay

Use KubeRay dashboard (experimental)

Resource Isolation with Writable Cgroups on Google Kubernetes Engine (GKE)

Examples
Train a PyTorch model on Fashion MNIST with CPUs on Kubernetes

Serve a StableDiffusion text-to-image model on Kubernetes

Serve a Stable Diffusion model on GKE with TPUs

Serve a MobileNet image classifier on Kubernetes

Serve a text summarizer on Kubernetes

RayJob Batch Inference Example

Priority Scheduling with RayJob and Kueue

Gang Scheduling with RayJob and Kueue

Distributed checkpointing with KubeRay and GCSFuse

Use Modin with Ray on Kubernetes

Serve a Large Language Model using Ray Serve LLM on Kubernetes

Serve Deepseek R1 using Ray Serve LLM

Reinforcement Learning with Human Feedback (RLHF) for LLMs with verl on KubeRay

Deploying Ray Clusters via ArgoCD

KubeRay Ecosystem
Ingress

KubeRay metrics references

Using Prometheus and Grafana

Profiling with py-spy

Gang scheduling, queue priority, and GPU sharing for RayClusters using KAI Scheduler

KubeRay integration with Volcano

KubeRay integration with Apache YuniKorn

Gang scheduling, Priority scheduling, and Autoscaling for KubeRay CRDs with Kueue

mTLS and L7 observability with Istio

KubeRay integration with scheduler plugins

KubeRay Benchmarks
KubeRay memory and scalability benchmark

KubeRay Troubleshooting
Troubleshooting guide

RayService troubleshooting

API Reference

Deploying on VMs
Getting Started

User Guides
Launching Ray Clusters on AWS, GCP, Azure, vSphere, On-Prem

Best practices for deploying large clusters

Configuring Autoscaling

Log Persistence

Community Supported Cluster Managers

Examples
Ray Train XGBoostTrainer on VMs

API References
Cluster Launcher Commands

Cluster YAML Configuration Options

Collecting and monitoring metrics

Configuring and Managing Ray Dashboard

Applications Guide
Ray Jobs Overview
Quickstart using the Ray Jobs CLI

Python SDK Overview

Python SDK API Reference

Ray Jobs CLI API Reference

Ray Jobs REST API

Ray Client

Programmatic Cluster Scaling

FAQ

Ray Cluster Management API
Cluster Management CLI

Python SDK API Reference

Ray Jobs CLI API Reference

Programmatic Cluster Scaling

Usage Stats Collection

Monitoring and Debugging
Ray Dashboard

Ray Distributed Debugger

Key Concepts

User Guides
Debugging Applications
Common Issues

Debugging Memory Issues

Debugging Hangs

Debugging Failures

Optimizing Performance

Ray Distributed Debugger

Using the Ray Debugger

Monitoring with the CLI or SDK

Configuring Logging

Profiling

Adding Application-Level Metrics

Tracing

Ray Event Export

Reference
State API

State CLI

System Metrics

Developer Guides
API Stability

API Policy

Getting Involved / Contributing
Building Ray from Source

CI Testing Workflow on PRs

Contributing to the Ray Documentation

How to write code snippets

Testing Autoscaling Locally

Tips for testing Ray programs

Debugging for Ray Developers

Profiling for Ray Developers

Configuring Ray

Architecture Whitepapers

Glossary

Security
Ray token authentication

Project Governance
People

Ray Serve: Scalable and Programmable Serving

User guides

Prefill/deco...

Prefill/decode disaggregation#

Deploy LLMs with separated prefill and decode phases for better resource utilization and cost optimization.

Warning

This feature requires vLLM v1, which is the default engine. For legacy deployments using vLLM v0, upgrade to v1 first.

Prefill/decode disaggregation separates the prefill phase (processing input prompts) from the decode phase (generating tokens). This separation provides:

Independent optimization: You can optimize prefill separately from decode with different configurations.

Reduced interference: Prefill operations can interfere with decode operations and vice versa, degrading performance during unpredictable traffic spikes. Disaggregation removes this contention.

Independent scaling: You can scale each phase independently based on demand.

Cost optimization: You can use different node types for different workloads, taking advantage of heterogeneous clusters.

vLLM provides several KV transfer backends for disaggregated serving:

NIXLConnector: Network-based KV cache transfer using NVIDIA Inference Xfer Library (NIXL) with support for various backends such as UCX, libfabric, and EFA. Simple setup with minimal configuration.

LMCacheConnectorV1: Advanced caching solution with support for various storage backends, including integration with NIXL.

When to use prefill/decode disaggregation#

Consider this pattern when:

You have variable workload patterns with different resource needs for prefill vs decode.

You want to optimize costs by using different hardware for different phases.

Your application has high throughput requirements that benefit from decoupling prefill and decode.

Deploy with NIXLConnector#

NIXLConnector provides network-based KV cache transfer between prefill and decode servers with minimal configuration.

Prerequisites#

If you use ray-project/ray-llm Docker images, NIXL is already installed. Otherwise, install it:

uvpipinstallnixl

The NIXL wheel comes bundled with its supported backends (UCX, libfabric, EFA, etc.). These shared binaries may not be the latest version for your hardware and network stack. If you need the latest versions, install NIXL from source against the target backend library. See the NIXL installation guide for details.

Basic deployment#

The following example shows how to deploy with NIXLConnector:

fromray.serve.llmimportLLMConfig,build_pd_openai_appimportray.serveasserve# Configure prefill instanceprefill_config=LLMConfig(model_loading_config={"model_id":"meta-llama/Llama-3.1-8B-Instruct"},engine_kwargs={"kv_transfer_config":{"kv_connector":"NixlConnector","kv_role":"kv_both",}})# Configure decode instancedecode_config=LLMConfig(model_loading_config={"model_id":"meta-llama/Llama-3.1-8B-Instruct"},engine_kwargs={"kv_transfer_config":{"kv_connector":"NixlConnector","kv_role":"kv_both",}})pd_config=dict(prefill_config=prefill_config,decode_config=decode_config,)app=build_pd_openai_app(pd_config)serve.run(app)

Production YAML configuration#

For production deployments, use a YAML configuration file:

# Example: Basic NIXLConnector configuration for prefill/decode disaggregation# nixl_config.yamlapplications:-args:prefill_config:model_loading_config:model_id:meta-llama/Llama-3.1-8B-Instructengine_kwargs:kv_transfer_config:kv_connector:NixlConnectorkv_role:kv_producerengine_id:engine1deployment_config:autoscaling_config:min_replicas:2max_replicas:4decode_config:model_loading_config:model_id:meta-llama/Llama-3.1-8B-Instructengine_kwargs:kv_transfer_config:kv_connector:NixlConnectorkv_role:kv_consumerengine_id:engine2deployment_config:autoscaling_config:min_replicas:6max_replicas:10import_path:ray.serve.llm:build_pd_openai_appname:pd-disaggregation-nixlroute_prefix:"/"

Deploy with:

servedeploynixl_config.yaml

Configuration parameters#

kv_connector
: Set to 
"NixlConnector"
 to use NIXL.

kv_role
: Set to 
"kv_both"
 for both prefill and decode instances.

Deploy with LMCacheConnectorV1#

LMCacheConnectorV1 provides advanced caching with support for multiple storage backends.

Prerequisites#

Install LMCache:

uvpipinstalllmcache

Scenario 1: LMCache with NIXL backend#

This configuration uses LMCache with a NIXL-based storage backend for network communication.

The following is an example Ray Serve configuration for LMCache with NIXL:

# Example: LMCacheConnectorV1 with NIXL backend configurationapplications:-args:prefill_config:model_loading_config:model_id:meta-llama/Llama-3.1-8B-Instructengine_kwargs:kv_transfer_config:kv_connector:LMCacheConnectorV1kv_role:kv_producerkv_connector_extra_config:discard_partial_chunks:falselmcache_rpc_port:producer1deployment_config:autoscaling_config:min_replicas:2max_replicas:2runtime_env:env_vars:LMCACHE_CONFIG_FILE:lmcache_prefiller.yamlLMCACHE_USE_EXPERIMENTAL:"True"decode_config:model_loading_config:model_id:meta-llama/Llama-3.1-8B-Instructengine_kwargs:kv_transfer_config:kv_connector:LMCacheConnectorV1kv_role:kv_consumerkv_connector_extra_config:discard_partial_chunks:falselmcache_rpc_port:consumer1deployment_config:autoscaling_config:min_replicas:6max_replicas:6runtime_env:env_vars:LMCACHE_CONFIG_FILE:lmcache_decoder.yamlLMCACHE_USE_EXPERIMENTAL:"True"import_path:ray.serve.llm:build_pd_openai_appname:pd-disaggregation-lmcache-nixlroute_prefix:"/"

Create the LMCache configuration for the prefill instance (
lmcache_prefiller.yaml
):

local_cpu:Falsemax_local_cpu_size:0max_local_disk_size:0remote_serde:NULLenable_nixl:Truenixl_role:"sender"nixl_receiver_host:"localhost"nixl_receiver_port:55555nixl_buffer_size:1073741824# 1GBnixl_buffer_device:"cuda"nixl_enable_gc:True

Create the LMCache configuration for the decode instance (
lmcache_decoder.yaml
):

local_cpu:Falsemax_local_cpu_size:0max_local_disk_size:0remote_serde:NULLenable_nixl:Truenixl_role:"receiver"nixl_receiver_host:"localhost"nixl_receiver_port:55555nixl_buffer_size:1073741824# 1GBnixl_buffer_device:"cuda"nixl_enable_gc:True

Note

The 
LMCACHE_CONFIG_FILE
 environment variable must point to an existing configuration file that’s accessible within the Ray Serve container or worker environment. Ensure these configuration files are properly mounted or available in your deployment environment.

Scenario 2: LMCache with Mooncake store backend#

This configuration uses LMCache with Mooncake store, a high-performance distributed storage system.

The following is an example Ray Serve configuration for LMCache with Mooncake:

# Example: LMCacheConnectorV1 with Mooncake store configurationapplications:-args:prefill_config:model_loading_config:model_id:meta-llama/Llama-3.1-8B-Instructengine_kwargs:kv_transfer_config:&kv_transfer_configkv_connector:LMCacheConnectorV1kv_role:kv_bothdeployment_config:autoscaling_config:min_replicas:2max_replicas:2runtime_env:&runtime_envenv_vars:LMCACHE_CONFIG_FILE:lmcache_mooncake.yamlLMCACHE_USE_EXPERIMENTAL:"True"decode_config:model_loading_config:model_id:meta-llama/Llama-3.1-8B-Instructengine_kwargs:kv_transfer_config:*kv_transfer_configdeployment_config:autoscaling_config:min_replicas:1max_replicas:1runtime_env:*runtime_envimport_path:ray.serve.llm:build_pd_openai_appname:pd-disaggregation-lmcache-mooncakeroute_prefix:"/"

Create the LMCache configuration for Mooncake (
lmcache_mooncake.yaml
):

# LMCache configuration for Mooncake store backendchunk_size:256local_device:"cpu"remote_url:"mooncakestore://storage-server:49999/"remote_serde:"naive"pipelined_backend:falselocal_cpu:falsemax_local_cpu_size:5extra_config:local_hostname:"compute-node-001"metadata_server:"etcd://metadata-server:2379"protocol:"rdma"device_name:"rdma0"master_server_address:"storage-server:49999"global_segment_size:3355443200# 3.125 GBlocal_buffer_size:1073741824# 1 GBtransfer_timeout:1

Warning

For Mooncake deployments:

Ensure the etcd metadata server is running and accessible at the specified address.

Verify that you properly configured RDMA devices and storage servers and that they are accessible.

In containerized deployments, mount configuration files with appropriate read permissions (for example, 
chmod644
).

Ensure all referenced hostnames and IP addresses in configuration files are resolvable from the deployment environment.

Configuration parameters#

kv_connector
: Set to 
"LMCacheConnectorV1"
.

kv_role
: Set to 
"kv_producer"
 for prefill, 
"kv_consumer"
 for decode.

kv_buffer_size
: Size of the KV cache buffer.

LMCACHE_CONFIG_FILE
: Environment variable that specifies the configuration file path.

Test your deployment#

Before deploying with LMCacheConnectorV1, start the required services:

# Start etcd server if not already running
dockerrun-d--nameetcd-server\-p2379:2379-p2380:2380\quay.io/coreos/etcd:latest\etcd--listen-client-urlshttp://0.0.0.0:2379\--advertise-client-urlshttp://localhost:2379

# For Mooncake backend, start the Mooncake master# See https://docs.lmcache.ai/kv_cache/mooncake.html for details
mooncake_master--port49999

Test with a chat completion request:

curl-XPOST"http://localhost:8000/v1/chat/completions"\-H"Content-Type: application/json"\-d'{ "model": "meta-llama/Llama-3.1-8B-Instruct", "messages": [ {"role": "user", "content": "Explain the benefits of prefill/decode disaggregation"} ], "max_tokens": 100, "temperature": 0.7 }'

Best practices#

Choose the right backend: Use NIXLConnector for simpler deployments. Use LMCacheConnectorV1 when you need advanced caching or multiple storage backends.

Monitor KV transfer overhead: Ensure that the benefits of disaggregation outweigh the network transfer costs. Monitor latency and throughput.

Scale independently: Take advantage of independent scaling by monitoring resource utilization for each phase separately.

Test with realistic workloads: Validate performance improvements with your actual traffic patterns before production deployment.

Ensure network connectivity: For NIXLConnector, verify that prefill and decode instances can communicate over the network.

Secure etcd access: For LMCacheConnectorV1, ensure your etcd server is properly secured and accessible only to authorized services.

Troubleshooting#

Prefill and decode instances can’t communicate#

Verify network connectivity between instances with sufficient bandwidth for KV transfer.

Check that your network supports the backend you’re using (such as RDMA for high-performance deployments).

For NIXLConnector, ensure NIXL is properly installed on all nodes.

Verify firewall rules and security groups allow communication between prefill and decode instances.

LMCache configuration not found#

Verify the 
LMCACHE_CONFIG_FILE
 environment variable points to an existing file.

Ensure the configuration file is accessible from the Ray Serve worker environment.

Check that the file has appropriate read permissions.

See also#

LMCache disaggregated serving documentation

NIXLConnector usage guide

Quickstart - Basic LLM deployment examples

previous

Deployment Initialization

next

KV cache offloading

 On this page
 

When to use prefill/decode disaggregation

Deploy with NIXLConnector
Prerequisites

Basic deployment

Production YAML configuration

Configuration parameters

Deploy with LMCacheConnectorV1
Prerequisites

Scenario 1: LMCache with NIXL backend

Scenario 2: LMCache with Mooncake store backend

Configuration parameters

Test your deployment

Best practices

Troubleshooting
Prefill and decode instances can’t communicate

LMCache configuration not found

See also

 Edit
 on GitHub 
 

Thanks for the feedback!

Was this helpful?
Yes

No

Feedback
Submit

 
 © Copyright 2026, The Ray Team.
 

 Created using Sphinx 7.3.7.
 

 Built with the PyData Sphinx Theme 0.14.1.

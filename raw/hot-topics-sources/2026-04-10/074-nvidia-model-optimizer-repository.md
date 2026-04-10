---
title: GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub
source_url: https://github.com/NVIDIA/Model-Optimizer
final_url: https://github.com/NVIDIA/Model-Optimizer
status: 200
content_type: text/html; charset=utf-8
topics: [NVFP4 Quantization for LLM Inference]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:35.201147+00:00
---

# GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub

## 원본 URL

https://github.com/NVIDIA/Model-Optimizer

## 추출 본문

GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub

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

 NVIDIA
/Model-OptimizerPublic

Notifications
You must be signed in to change notification settings

Fork
 340

 Star
2.4k

Code

Issues60

Pull requests130

Actions

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Security and quality

 Insights

NVIDIA/Model-Optimizer

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
651 Commits

651 Commits

.claude

.claude

.github

.github

.vscode

.vscode

docs/source

docs/source

examples

examples

experimental

experimental

modelopt

modelopt

modelopt_recipes

modelopt_recipes

tests

tests

tools

tools

.coderabbit.yaml

.coderabbit.yaml

.dockerignore

.dockerignore

.gitignore

.gitignore

.gitmodules

.gitmodules

.markdownlint-cli2.yaml

.markdownlint-cli2.yaml

.pre-commit-config.yaml

.pre-commit-config.yaml

CHANGELOG.rst

CHANGELOG.rst

CLAUDE.md

CLAUDE.md

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

LICENSE_HEADER

LICENSE_HEADER

README.md

README.md

SECURITY.md

SECURITY.md

pyproject.toml

pyproject.toml

tox.ini

tox.ini

uv.lock

uv.lock

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

Security

NVIDIA Model Optimizer

Documentation |
Roadmap

NVIDIA Model Optimizer (referred to as Model Optimizer, or ModelOpt) is a library comprising state-of-the-art model optimization techniques including quantization, distillation, pruning, speculative decoding and sparsity to accelerate models.

[Input] Model Optimizer currently supports inputs of a Hugging Face, PyTorch or ONNX model.

[Optimize] Model Optimizer provides Python APIs for users to easily compose the above model optimization techniques and export an optimized quantized checkpoint.
Model Optimizer is also integrated with NVIDIA Megatron-Bridge, Megatron-LM and Hugging Face Accelerate for training required inference optimization techniques.

[Export for deployment] Seamlessly integrated within the NVIDIA AI software ecosystem, the quantized checkpoint generated from Model Optimizer is ready for deployment in downstream inference frameworks like SGLang, TensorRT-LLM, TensorRT, or vLLM. The unified Hugging Face export API now supports both transformers and diffusers models.

Latest News

[2026/03/11] Model Optimizer quantized Nemotron-3-Super checkpoints are available on Hugging Face for download: FP8, NVFP4. Learn more in the Nemotron 3 Super release blog. Check out how to quantize Nemotron 3 models for deployment acceleration here

[2026/03/11] NeMo Megatron Bridge now supports Nemotron-3-Super quantization (PTQ and QAT) and export workflows using the Model Optimizer library. See the Quantization (PTQ and QAT) guide for FP8/NVFP4 quantization and HF export instructions.

[2025/12/11] BLOG: Top 5 AI Model Optimization Techniques for Faster, Smarter Inference

[2025/12/08] NVIDIA TensorRT Model Optimizer is now officially rebranded as NVIDIA Model Optimizer.

[2025/10/07] BLOG: Pruning and Distilling LLMs Using NVIDIA Model Optimizer

[2025/09/17] BLOG: An Introduction to Speculative Decoding for Reducing Latency in AI Inference

[2025/09/11] BLOG: How Quantization Aware Training Enables Low-Precision Accuracy Recovery

[2025/08/29] BLOG: Fine-Tuning gpt-oss for Accuracy and Performance with Quantization Aware Training

[2025/08/01] BLOG: Optimizing LLMs for Performance and Accuracy with Post-Training Quantization

[2025/06/24] BLOG: Introducing NVFP4 for Efficient and Accurate Low-Precision Inference

[2025/05/14] NVIDIA TensorRT Unlocks FP4 Image Generation for NVIDIA Blackwell GeForce RTX 50 Series GPUs

[2025/04/21] Adobe optimized deployment using Model-Optimizer + TensorRT leading to a 60% reduction in diffusion latency, a 40% reduction in total cost of ownership

[2025/04/05] NVIDIA Accelerates Inference on Meta Llama 4 Scout and Maverick. Check out how to quantize Llama4 for deployment acceleration here

[2025/03/18] World's Fastest DeepSeek-R1 Inference with Blackwell FP4 & Increasing Image Generation Efficiency on Blackwell

[2025/02/25] Model Optimizer quantized NVFP4 models available on Hugging Face for download: DeepSeek-R1-FP4, Llama-3.3-70B-Instruct-FP4, Llama-3.1-405B-Instruct-FP4

[2025/01/28] Model Optimizer has added support for NVFP4. Check out an example of NVFP4 PTQ here.

[2025/01/28] Model Optimizer is now open source!
Previous News
[2024/10/23] Model Optimizer quantized FP8 Llama-3.1 Instruct models available on Hugging Face for download: 8B, 70B, 405B.

[2024/09/10] Post-Training Quantization of LLMs with NVIDIA NeMo and Model Optimizer.

[2024/08/28] Boosting Llama 3.1 405B Performance up to 44% with Model Optimizer on NVIDIA H200 GPUs

[2024/08/28] Up to 1.9X Higher Llama 3.1 Performance with Medusa

[2024/08/15] New features in recent releases: Cache Diffusion, QLoRA workflow with NVIDIA NeMo, and more. Check out our blog for details.

[2024/06/03] Model Optimizer now has an experimental feature to deploy to vLLM as part of our effort to support popular deployment frameworks. Check out the workflow here

[2024/05/08] Announcement: Model Optimizer Now Formally Available to Further Accelerate GenAI Inference Performance

[2024/03/27] Model Optimizer supercharges TensorRT-LLM to set MLPerf LLM inference records

[2024/03/18] GTC Session: Optimize Generative AI Inference with Quantization in TensorRT-LLM and TensorRT

[2024/03/07] Model Optimizer's 8-bit Post-Training Quantization enables TensorRT to accelerate Stable Diffusion to nearly 2x faster

[2024/02/01] Speed up inference with Model Optimizer quantization techniques in TRT-LLM

Install

To install stable release packages for Model Optimizer with 
pip
 from PyPI:

pip install -U nvidia-modelopt[all]

To install from source in editable mode with all development dependencies or to use the latest features, run:

# Clone the Model Optimizer repository
git clone git@github.com:NVIDIA/Model-Optimizer.git
cd Model-Optimizer

pip install -e .[dev]

You can also directly use the TensorRT-LLM docker images
(e.g., 
nvcr.io/nvidia/tensorrt-llm/release:<version>
), which have Model Optimizer pre-installed.
Make sure to upgrade Model Optimizer to the latest version as described above.
Visit our installation guide for
more fine-grained control on installed dependencies or for alternative docker images and environment variables to setup.

Techniques

TechniqueDescriptionExamplesDocsPost Training QuantizationCompress model size by 2x-4x, speeding up inference while preserving model quality![LLMs] [diffusers] [VLMs] [onnx] [windows][docs]Quantization Aware TrainingRefine accuracy even further with a few training steps![Hugging Face][docs]PruningReduce your model size and accelerate inference by removing unnecessary weights![General] [Megatron-Bridge]DistillationReduce deployment model size by teaching small models to behave like larger models![Megatron-Bridge] [Megatron-LM] [Hugging Face][docs]Speculative DecodingTrain draft modules to predict extra tokens during inference![Megatron] [Hugging Face][docs]SparsityEfficiently compress your model by storing only its non-zero parameter values and their locations[PyTorch][docs]

Pre-Quantized Checkpoints

Ready-to-deploy checkpoints [🤗 Hugging Face - Nvidia Model Optimizer Collection]

Deployable on TensorRT-LLM, vLLM and SGLang

More models coming soon!

Resources

📅 Roadmap

📖 Documentation

🎯 Benchmarks

💡 Release Notes

🐛 File a bug

✨ File a Feature Request

Model Support Matrix

Model TypeSupport MatrixLLM QuantizationView Support MatrixDiffusers QuantizationView Support MatrixVLM QuantizationView Support MatrixONNX QuantizationView Support MatrixWindows QuantizationView Support MatrixQuantization Aware TrainingView Support MatrixPruningView Support MatrixDistillationView Support MatrixSpeculative DecodingView Support Matrix

Contributing

Model Optimizer is now open source! We welcome any feedback, feature requests and PRs.
Please read our Contributing guidelines for details on how to contribute to this project.

Top Contributors

Happy optimizing!

About

 A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed.
 

nvidia.github.io/Model-Optimizer/

Resources

 Readme

License

 Apache-2.0 license
 

Code of conduct

 Code of conduct
 

Contributing

 Contributing
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

2.4k
 stars

Watchers

27
 watching

Forks

340
 forks

 Report repository

Releases
 27

ModelOpt 0.42.0 Release
 Latest

Mar 9, 2026

+ 26 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python97.5%

Shell1.2%

Other1.3%

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

---
title: GitHub - deepseek-ai/DeepEP: DeepEP: an efficient expert-parallel communication library · GitHub
source_url: https://github.com/deepseek-ai/DeepEP
final_url: https://github.com/deepseek-ai/DeepEP
status: 200
content_type: text/html; charset=utf-8
topics: [Wide Expert Parallelism (Wide-EP) for MoE]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:07.265355+00:00
---

# GitHub - deepseek-ai/DeepEP: DeepEP: an efficient expert-parallel communication library · GitHub

## 원본 URL

https://github.com/deepseek-ai/DeepEP

## 추출 본문

GitHub - deepseek-ai/DeepEP: DeepEP: an efficient expert-parallel communication library · GitHub

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

 deepseek-ai
/DeepEPPublic

Notifications
You must be signed in to change notification settings

Fork
 1.1k

 Star
9.1k

Code

Issues172

Pull requests62

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

deepseek-ai/DeepEP

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
240 Commits

240 Commits

.github/workflows

.github/workflows

csrc

csrc

deep_ep

deep_ep

figures

figures

tests

tests

third-party

third-party

.clang-format

.clang-format

.gitignore

.gitignore

LICENSE

LICENSE

README.md

README.md

format.sh

format.sh

install.sh

install.sh

pyproject.toml

pyproject.toml

requirements-lint.txt

requirements-lint.txt

setup.py

setup.py

View all files

Repository files navigation

README

MIT license

DeepEP

DeepEP is a communication library tailored for Mixture-of-Experts (MoE) and expert parallelism (EP). It provides high-throughput and low-latency all-to-all GPU kernels, which are also known as MoE dispatch and combine. The library also supports low-precision operations, including FP8.

To align with the group-limited gating algorithm proposed in the DeepSeek-V3 paper, DeepEP offers a set of kernels optimized for asymmetric-domain bandwidth forwarding, such as forwarding data from NVLink domain to RDMA domain. These kernels deliver high throughput, making them suitable for both training and inference prefilling tasks. Additionally, they support SM (Streaming Multiprocessors) number control.

For latency-sensitive inference decoding, DeepEP includes a set of low-latency kernels with pure RDMA to minimize delays. The library also introduces a hook-based communication-computation overlapping method that does not occupy any SM resource.

Notice: the implementation in this library may have some slight differences from the DeepSeek-V3 paper.

Performance

Normal kernels with NVLink and RDMA forwarding

We test normal kernels on H800 (~160 GB/s NVLink maximum bandwidth), with each connected to a CX7 InfiniBand 400 Gb/s RDMA network card (~50 GB/s maximum bandwidth). And we follow the DeepSeek-V3/R1 pretraining setting (4096 tokens per batch, 7168 hidden, top-4 groups, top-8 experts, FP8 dispatching and BF16 combining).
TypeDispatch #EPBottleneck bandwidthCombine #EPBottleneck bandwidthIntranode8153 GB/s (NVLink)8158 GB/s (NVLink)Internode1643 GB/s (RDMA)1643 GB/s (RDMA)Internode3258 GB/s (RDMA)3257 GB/s (RDMA)Internode6451 GB/s (RDMA)6450 GB/s (RDMA)
News (2025.04.22): with optimizations from Tencent Network Platform Department, performance was enhanced by up to 30%, see #130 for more details. Thanks for the contribution!

Low-latency kernels with pure RDMA

We test low-latency kernels on H800 with each connected to a CX7 InfiniBand 400 Gb/s RDMA network card (~50 GB/s maximum bandwidth). And we follow a typical DeepSeek-V3/R1 production setting (128 tokens per batch, 7168 hidden, top-8 experts, FP8 dispatching and BF16 combining).
Dispatch #EPLatencyRDMA bandwidthCombine #EPLatencyRDMA bandwidth877 us98 GB/s8114 us127 GB/s16118 us63 GB/s16195 us74 GB/s32155 us48 GB/s32273 us53 GB/s64173 us43 GB/s64314 us46 GB/s128192 us39 GB/s128369 us39 GB/s256194 us39 GB/s256360 us40 GB/s
News (2025.06.05): low-latency kernels now leverage NVLink as much as possible, see #173 for more details. Thanks for the contribution!

Quick start

Requirements

Ampere (SM80), Hopper (SM90) GPUs, or other architectures with SM90 PTX ISA support

Python 3.8 and above

CUDA version

CUDA 11.0 and above for SM80 GPUs

CUDA 12.3 and above for SM90 GPUs

PyTorch 2.1 and above

NVLink for intranode communication

RDMA network for internode communication

Download and install NVSHMEM dependency

DeepEP also depends on NVSHMEM. Please refer to our NVSHMEM Installation Guide for instructions.

Development

# Build and make symbolic links for SO files
NVSHMEM_DIR=/path/to/installed/nvshmem python setup.py build
# You may modify the specific SO names according to your own platform
ln -s build/lib.linux-x86_64-cpython-38/deep_ep_cpp.cpython-38-x86_64-linux-gnu.so

# Run test cases# NOTES: you may modify the `init_dist` function in `tests/utils.py`# according to your own cluster settings, and launch into multiple nodes
python tests/test_intranode.py
python tests/test_internode.py
python tests/test_low_latency.py

Installation

NVSHMEM_DIR=/path/to/installed/nvshmem python setup.py install

Installation environment variables

NVSHMEM_DIR
: the path to the NVSHMEM directory, disable all internode and low-latency features if not specified

DISABLE_SM90_FEATURES
: 0 or 1, whether to disable SM90 features, it is required for SM90 devices or CUDA 11

TORCH_CUDA_ARCH_LIST
: the list of target architectures, e.g. 
TORCH_CUDA_ARCH_LIST="9.0"

DISABLE_AGGRESSIVE_PTX_INSTRS
: 0 or 1, whether to disable aggressive load/store instructions, see Undefined-behavior PTX usage for more details

Then, import 
deep_ep
 in your Python project, and enjoy!

Network configurations

DeepEP is fully tested with InfiniBand networks. However, it is theoretically compatible with RDMA over Converged Ethernet (RoCE) as well.

Traffic isolation

Traffic isolation is supported by InfiniBand through Virtual Lanes (VL).

To prevent interference between different types of traffic, we recommend segregating workloads across different virtual lanes as follows:

workloads using normal kernels

workloads using low-latency kernels

other workloads

For DeepEP, you can control the virtual lane assignment by setting the 
NVSHMEM_IB_SL
 environment variable.

Adaptive routing

Adaptive routing is an advanced routing feature provided by InfiniBand switches that can evenly distribute traffic across multiple paths. Enabling adaptive routing can completely eliminate network congestion caused by routing conflicts, but it also introduces additional latency. We recommend the following configuration for optimal performance:

enable adaptive routing in environments with heavy network loads

use static routing in environments with light network loads

Congestion control

Congestion control is disabled as we have not observed significant congestion in our production environment.

Interfaces and examples

Example use in model training or inference prefilling

The normal kernels can be used in model training or the inference prefilling phase (without the backward part) as the below example code shows.

importtorchimporttorch.distributedasdistfromtypingimportList, Tuple, Optional, Unionfromdeep_epimportBuffer, EventOverlap# Communication buffer (will allocate at runtime)_buffer: Optional[Buffer] =None# Set the number of SMs to use# NOTES: this is a static variableBuffer.set_num_sms(24)

# You may call this function at the framework initializationdefget_buffer(group: dist.ProcessGroup, hidden_bytes: int) ->Buffer:
 global_buffer# NOTES: you may also replace `get_*_config` with your auto-tuned results via all the testsnum_nvl_bytes, num_rdma_bytes=0, 0forconfigin (Buffer.get_dispatch_config(group.size()), Buffer.get_combine_config(group.size())):
 num_nvl_bytes=max(config.get_nvl_buffer_size_hint(hidden_bytes, group.size()), num_nvl_bytes)
 num_rdma_bytes=max(config.get_rdma_buffer_size_hint(hidden_bytes, group.size()), num_rdma_bytes)

 # Allocate a buffer if not existed or not enough buffer sizeif_bufferisNoneor_buffer.group!=groupor_buffer.num_nvl_bytes<num_nvl_bytesor_buffer.num_rdma_bytes<num_rdma_bytes:
 _buffer=Buffer(group, num_nvl_bytes, num_rdma_bytes)
 return_bufferdefget_hidden_bytes(x: torch.Tensor) ->int:
 t=x[0] ifisinstance(x, tuple) elsexreturnt.size(1) *max(t.element_size(), 2)

defdispatch_forward(x: Union[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]],
 topk_idx: torch.Tensor, topk_weights: torch.Tensor,
 num_experts: int, previous_event: Optional[EventOverlap] =None) -> \
 Tuple[Union[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]], torch.Tensor, torch.Tensor, List, Tuple, EventOverlap]:
 # NOTES: an optional `previous_event` means a CUDA event captured that you want to make it as a dependency# of the dispatch kernel, it may be useful with communication-computation overlap. For more information, please# refer to the docs of `Buffer.dispatch`global_buffer# Calculate layout before actual dispatchnum_tokens_per_rank, num_tokens_per_rdma_rank, num_tokens_per_expert, is_token_in_rank, previous_event= \
 _buffer.get_dispatch_layout(topk_idx, num_experts,
 previous_event=previous_event, async_finish=True,
 allocate_on_comm_stream=previous_eventisnotNone)
 # Do MoE dispatch# NOTES: the CPU will wait for GPU's signal to arrive, so this is not compatible with CUDA graph# Unless you specify `num_worst_tokens`, but this flag is for intranode only# For more advanced usages, please refer to the docs of the `dispatch` functionrecv_x, recv_topk_idx, recv_topk_weights, num_recv_tokens_per_expert_list, handle, event= \
 _buffer.dispatch(x, topk_idx=topk_idx, topk_weights=topk_weights,
 num_tokens_per_rank=num_tokens_per_rank, num_tokens_per_rdma_rank=num_tokens_per_rdma_rank,
 is_token_in_rank=is_token_in_rank, num_tokens_per_expert=num_tokens_per_expert,
 previous_event=previous_event, async_finish=True,
 allocate_on_comm_stream=True)
 # For event management, please refer to the docs of the `EventOverlap` classreturnrecv_x, recv_topk_idx, recv_topk_weights, num_recv_tokens_per_expert_list, handle, eventdefdispatch_backward(grad_recv_x: torch.Tensor, grad_recv_topk_weights: torch.Tensor, handle: Tuple) -> \
 Tuple[torch.Tensor, torch.Tensor, EventOverlap]:
 global_buffer# The backward process of MoE dispatch is actually a combine# For more advanced usages, please refer to the docs of the `combine` functioncombined_grad_x, combined_grad_recv_topk_weights, event= \
 _buffer.combine(grad_recv_x, handle, topk_weights=grad_recv_topk_weights, async_finish=True)

 # For event management, please refer to the docs of the `EventOverlap` classreturncombined_grad_x, combined_grad_recv_topk_weights, eventdefcombine_forward(x: torch.Tensor, handle: Tuple, previous_event: Optional[EventOverlap] =None) -> \
 Tuple[torch.Tensor, EventOverlap]:
 global_buffer# Do MoE combine# For more advanced usages, please refer to the docs of the `combine` functioncombined_x, _, event=_buffer.combine(x, handle, async_finish=True, previous_event=previous_event,
 allocate_on_comm_stream=previous_eventisnotNone)

 # For event management, please refer to the docs of the `EventOverlap` classreturncombined_x, eventdefcombine_backward(grad_combined_x: Union[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]],
 handle: Tuple, previous_event: Optional[EventOverlap] =None) -> \
 Tuple[Union[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]], EventOverlap]:
 global_buffer# The backward process of MoE combine is actually a dispatch# For more advanced usages, please refer to the docs of the `dispatch` functiongrad_x, _, _, _, _, event=_buffer.dispatch(grad_combined_x, handle=handle, async_finish=True,
 previous_event=previous_event,
 allocate_on_comm_stream=previous_eventisnotNone)

 # For event management, please refer to the docs of the `EventOverlap` classreturngrad_x, event

Moreover, inside the dispatch function, we may not know how many tokens to receive for the current rank. So an implicit CPU wait for GPU received count signal will be involved, as the following figure shows.

Example use in inference decoding

The low latency kernels can be used in the inference decoding phase as the below example code shows.

importtorchimporttorch.distributedasdistfromtypingimportTuple, Optionalfromdeep_epimportBuffer# Communication buffer (will allocate at runtime)# NOTES: there is no SM control API for the low-latency kernels_buffer: Optional[Buffer] =None# You may call this function at the framework initializationdefget_buffer(group: dist.ProcessGroup, num_max_dispatch_tokens_per_rank: int, hidden: int, num_experts: int) ->Buffer:
 # NOTES: the low-latency mode will consume much more space than the normal mode# So we recommend that `num_max_dispatch_tokens_per_rank` (the actual batch size in the decoding engine) should be less than 256global_buffernum_rdma_bytes=Buffer.get_low_latency_rdma_size_hint(num_max_dispatch_tokens_per_rank, hidden, group.size(), num_experts)

 # Allocate a buffer if not existed or not enough buffer sizeif_bufferisNoneor_buffer.group!=groupornot_buffer.low_latency_modeor_buffer.num_rdma_bytes<num_rdma_bytes:
 # NOTES: for the best performance, the QP number **must** be equal to the number of the local expertsassertnum_experts%group.size() ==0_buffer=Buffer(group, 0, num_rdma_bytes, low_latency_mode=True, num_qps_per_rank=num_experts//group.size())
 return_bufferdeflow_latency_dispatch(hidden_states: torch.Tensor, topk_idx: torch.Tensor, num_max_dispatch_tokens_per_rank: int, num_experts: int):
 global_buffer# Do MoE dispatch, compatible with CUDA graph (but you may restore some buffer status once you replay)recv_hidden_states, recv_expert_count, handle, event, hook= \
 _buffer.low_latency_dispatch(hidden_states, topk_idx, num_max_dispatch_tokens_per_rank, num_experts,
 async_finish=False, return_recv_hook=True)

 # NOTES: the actual tensor will not be received only if you call `hook()`,# it is useful for double-batch overlapping, but **without any SM occupation**# If you don't want to overlap, please set `return_recv_hook=False`# Later, you can use our GEMM library to do the computation with this specific formatreturnrecv_hidden_states, recv_expert_count, handle, event, hookdeflow_latency_combine(hidden_states: torch.Tensor,
 topk_idx: torch.Tensor, topk_weights: torch.Tensor, handle: Tuple):
 global_buffer# Do MoE combine, compatible with CUDA graph (but you may restore some buffer status once you replay)combined_hidden_states, event_overlap, hook= \
 _buffer.low_latency_combine(hidden_states, topk_idx, topk_weights, handle,
 async_finish=False, return_recv_hook=True)

 # NOTES: the same behavior as described in the dispatch kernelreturncombined_hidden_states, event_overlap, hook

For two-micro-batch overlapping, you can refer to the following figure. With our receiving hook interface, the RDMA network traffic is happening in the background, without costing any GPU SMs from the computation part. But notice, the overlapped parts can be adjusted, i.e., the 4 parts of attention/dispatch/MoE/combine may not have the exact same execution time. You may adjust the stage settings according to your workload.

Roadmap

 AR support

 Refactor low-latency mode AR code

 A100 support (intranode only)

 Support BF16 for the low-latency dispatch kernel

 Support NVLink protocol for intranode low-latency kernels

 TMA copy instead of LD/ST

 Intranode kernels

 Internode kernels

 Low-latency kernels

 SM-free kernels and refactors

 Fully remove undefined-behavior PTX instructions

Notices

Easier potential overall design

The current DeepEP implementation uses queues for communication buffers which save memory but introduce complexity and potential deadlocks. If you're implementing your own version based on DeepEP, consider using fixed-size buffers allocated to maximum capacity for simplicity and better performance. For a detailed discussion of this alternative approach, see #39.

Undefined-behavior PTX usage

For extreme performance, we discover and use an undefined-behavior PTX usage: using read-only PTX 
ld.global.nc.L1::no_allocate.L2::256B
 to read volatile data. The PTX modifier 
.nc
 indicates that a non-coherent cache is used. But the correctness is tested to be guaranteed with 
.L1::no_allocate
 on Hopper architectures, and performance will be much better. The reason we guess may be: the non-coherent cache is unified with L1, and the L1 modifier is not just a hint but a strong option, so that the correctness can be guaranteed by no dirty data in L1.

Initially, because NVCC could not automatically unroll volatile read PTX, we tried using 
__ldg
 (i.e., 
ld.nc
). Even compared to manually unrolled volatile reads, it was significantly faster (likely due to additional compiler optimizations). However, the results could be incorrect or dirty. After consulting the PTX documentation, we discovered that L1 and non-coherent cache are unified on Hopper architectures. We speculated that 
.L1::no_allocate
 might resolve the issue, leading to this discovery.

If you find kernels not working on some other platforms, you may add 
DISABLE_AGGRESSIVE_PTX_INSTRS=1
 to 
setup.py
 and disable this, or file an issue.

Auto-tuning on your cluster

For better performance on your cluster, we recommend to run all the tests and use the best auto-tuned configuration. The default configurations are optimized on the DeepSeek's internal cluster.

License

This code repository is released under the MIT License, except for codes that reference NVSHMEM (including 
csrc/kernels/ibgda_device.cuh
 and 
third-party/nvshmem.patch
), which are subject to NVSHMEM SLA.

Experimental Branches

Zero-copy
Removing the copy between PyTorch tensors and communication buffers, which reduces the SM usages significantly for normal kernels

This PR is authored by Tencent Network Platform Department

Eager
Using a low-latency protocol removes the extra RTT latency introduced by RDMA atomic OPs

Hybrid-EP
A new backend implementation using TMA instructions for minimal SM usage and larger NVLink domain support

Fine-grained communication-computation overlap for single-batch scenarios

PCIe kernel support for non-NVLink environments

NVFP4 data type support

AntGroup-Opt
This optimization series is authored by AntGroup Network Platform Department

Normal-SMFree Eliminating SM from RDMA path by decoupling comm-kernel execution from NIC token transfer, freeing SMs for compute

LL-SBO Overlapping Down GEMM computation with Combine Send communication via signaling mechanism to reduce end-to-end latency

LL-Layered Optimizing cross-node LL operator communication using rail-optimized forwarding and data merging to reduce latency

Mori-EP
ROCm/AMD GPU support powered by MORI backend (low-latency mode)

Community Forks

uccl/uccl-ep - Enables running DeepEP on heterogeneous GPUs (e.g., Nvidia, AMD) and NICs (e.g., EFA, Broadcom, CX7)

Infrawaves/DeepEP_ibrc_dual-ports_multiQP - Adds multi-QP solution and dual-port NIC support in IBRC transport

antgroup/DeepXTrace - A diagnostic analyzer for efficient and precise localization of slow ranks

ROCm/mori - AMD's next-generation communication library for performance-critical AI workloads (e.g., Wide EP, KVCache transfer, Collectives)

Citation

If you use this codebase or otherwise find our work valuable, please cite:

@misc{deepep2025,
 title={DeepEP: an efficient expert-parallel communication library},
 author={Chenggang Zhao and Shangyan Zhou and Liyue Zhang and Chengqi Deng and Zhean Xu and Yuxuan Liu and Kuai Yu and Jiashi Li and Liang Zhao},
 year={2025},
 publisher = {GitHub},
 howpublished = {\url{https://github.com/deepseek-ai/DeepEP}},
}

About

 DeepEP: an efficient expert-parallel communication library
 

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

9.1k
 stars

Watchers

98
 watching

Forks

1.1k
 forks

 Report repository

Releases
 1

Stable release v1.2.1
 Latest

Sep 16, 2025

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Cuda58.9%

Python20.3%

C++19.2%

Shell1.2%

CMake0.4%

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

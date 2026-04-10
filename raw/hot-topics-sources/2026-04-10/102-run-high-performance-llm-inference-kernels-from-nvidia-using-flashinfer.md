---
title: Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer​​ | NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer
final_url: https://developer.nvidia.com/blog/run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer
status: 200
content_type: text/html; charset=UTF-8
topics: [FlashInfer Kernel Library for LLM Serving]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:41.695868+00:00
---

# Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer​​ | NVIDIA Technical Blog

## 원본 URL

https://developer.nvidia.com/blog/run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer

## 추출 본문

Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer​​ | NVIDIA Technical Blog

DEVELOPER

Home

Blog

Forums

Docs

Downloads

Training

 Join
 

Technical Blog

 Subscribe
 

 Related Resources 

Developer Tools & Techniques

English中文

Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer​​

 Jun 13, 2025
 

 By Luis Ceze, Zihao Ye, Tianqi Chen, Vinod Grover, Mehdi Amini and Nick Comly

 Like 

 Discuss (0)
 

L

T

F

R

E

AI-Generated Summary

Like

Dislike

FlashInfer is a customizable and efficient library for building LLM serving engines, optimizing KV-cache storage and featuring a customizable attention template that adapts to various settings through just-in-time compilation.

The library splits LLM workloads into four operator families: Attention, GEMM, Communication, and Sampling, and exposes each family through lightweight, high-performance collectives that can be integrated into serving engines with minimal code changes.

NVIDIA is actively releasing its most performant LLM inference kernels in FlashInfer, including those from NVIDIA TensorRT-LLM, for easy integration into frameworks such as vLLM and SGLang.

AI-generated content may summarize information incompletely. Verify important information. Learn more

Best-in-class LLM Inference requires two key elements: speed and developer velocity. Speed refers to maximizing the efficiency of the underlying hardware by using highly optimized compute kernels algorithms. Developer velocity refers to the ability to quickly adopt these new kernels and accelerate new models, algorithms, and hardware. Ultimately, this velocity is underpinned by the quick deployment of new compute kernels running on the underlying GPUs and the ease of adopting these kernels into frameworks. 

Figure 1. FlashInfer technical architecture 

FlashInfer is a customizable and efficient library to build efficient LLM serving engines. Optimizing KV-cache storage using block-sparse and composable formats to improve memory access and reduce redundancy, it features a customizable attention template that adapts to various settings through just-in-time (JIT) compilation. Its load-balanced scheduling algorithm adjusts to dynamic user requests while remaining compatible with the NVIDIA CUDA Graph static configuration. FlashInfer is integrated into leading LLM serving frameworks such as MLC Engine, SGLang, and vLLM, as well as several custom engines. 

FlashInfer started as a collaborative research project at the Paul G. Allen School of Computer Science & Engineering, Carnegie Mellon University, and OctoAI (acquired by NVIDIA). The team aimed to create a flexible LLM inference kernel library that is engine agnostic, highly optimized, and easy to extend for new techniques such as algorithms for KV cache reuse. It’s now a thriving open source project with production deployments and contributions from research and development teams across the AI systems community. 

The technical paper FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving was awarded best paper at MLSys 2025. 

NVIDIA is now actively releasing its most performant LLM inference kernels in FlashInfer, including those from NVIDIA TensorRT-LLM, for easy integration into vLLM, SGLang, and custom inference engines.

FlashInfer architecture overview 

As a purpose-built NVIDIA GPU operator stack for LLM serving, FlashInfer aims for speed and developer velocity for the latest kernels. Inference platforms can adopt fresh ideas without waiting for new libraries or rewriting kernels in CUDA C++. These kernels will be available to all frameworks through a DLPack API, as well as registered as PyTorch operators for easy integration into many inference engines. The JIT capability enables users to materialize the kernels used by the target model, which means FlashInfer has a minimal footprint as a dependency as well.

FlashInfer splits LLM workloads into four operator families—Attention, GEMM, Communication, and Sampling—and exposes each family through lightweight, high-performance collectives that drop into any serving engine with minimal code changes.

Attention

Modern inference requests arrive with wildly different sequence lengths, KV cache block sizes, masking rules, and positional-encoding schemes. FlashInfer absorbs this dynamism by:

Unified storage: representing every cache layout as a block/vector sparse matrix.

Template & JIT kernels: a CUDA/CUTLASS codebase whose specialization knobs, logits/key/query, grouped, MLA, and future variants.

Inspector–executor interface: a PyTorch-friendly API that first inspects request shapes and prefix sharing patterns, then launches tuned kernels through a lightweight scheduler to keep GPUs saturated.

Figure 2. FlashInfer architecture

GEMM and communication

LLM blocks still rely heavily on matrix multiplication. In addition to traditional GEMV/GEMM computations and all-reduce communication, recent advancements, like mixture-of-experts and LoRA layers, introduce new requirements such as grouped GEMM—many small matrix multiplications in a single call—and all-to-all communication. FlashInfer selects the fastest open-source or NVIDIA kernels (including fp4 / fp8 tensor-core paths) and presents them behind one consistent API, so the serving stack can swap GPUs or kernels without touching application logic.

Token sampling

Generating the next token often bottlenecks Top-K/Top-P filtering. Traditional implementations sort the whole vocabulary, which is wasteful work when only a handful of logits matter. FlashInfer replaces global sorts with a rejection-based, sorting-free sampler that prunes improbable tokens on-the-fly, cutting latency on large vocabularies and staying numerically faithful.

Future-proofing inference

With these layers in place, serving frameworks can change KV-cache layouts, introduce fresh attention designs, batch arbitrary lengths, or chase tighter latency targets without rewriting kernels or falling back to the CPU. From the first query to the final token, FlashInfer keeps the critical inference path on GPU—flexible, future-proof, and fast.

Using FlashInfer

Flashinfer package is available on PyPI. You can try it out with:

pip install flashinfer-python

FlashInfer has Torch-native APIs with the design of 
plan/run
 to decouple kernel compilation/selection/tuning and kernel running. For attention, the API looks like:

from flashinfer.attention import BatchAttention
attention = BatchAttention(backend="cutlass") # we provide multiple backend implementations
attention.plan(
 qo_offsets, # offsets of each request in variable length query/output
 kv_lens, # kv length of each request in page table
 kv_block_table, # block table denoting the block indices in page table, could be packed/padded
 num_qo_heads, # number of query/output heads
 num_kv_heads, # number of key/value heads
 head_dim_qk, # head dimension of query/key
 head_dim_vo, # head dimension of value/output
 dtype_q=torch.bfloat16, # query data type
 dtype_kv=torch.bfloat16, # kv data type
 dtype_o=torch.bfloat16, # output data type
 **variant_kwargs, # other arguments specifying attention variants
)
O, lse = attention.run(q, (k, v)) # return output/lse

Kernel selection and tuning are performed in the 
plan
 stage, which gathers metadata required for the kernel. The same plan information can be reused for later runs that share the same metadata (all layers in an LLM generation step).

Users can choose from multiple attention backends to achieve the best performance for their use case. All kernels are CUDAGraph-safe, enabling low-latency LLM inference serving.

For logits processing, a modular interface composes different logits processors together, and 
flashinfer 
emits an efficient fused rejection sampling-based implementation. Our recent blog post explains how the flashinfer rejection sampling algorithm works.

import flashinfer
from flashinfer.logits_processor import LogitsPipe, Temperature, Softmax, TopP, Sample

# Create a pipeline
pipe = LogitsPipe([
 Temperature(), # Scale logits by temperature
 Softmax(), # Convert logits to probabilities
 TopP(), # Apply top-p filtering
 Sample() # Sample from the distribution
])

# Apply the pipeline
logits = torch.randn(batch_size, vocab_size, device="cuda")
output_ids = pipe(logits, temperature=0.7, top_p=0.9)

To get started with FlashInfer, see the GitHub repo and documentation.

 Discuss (0)
 

 Like 

Tags

Developer Tools & Techniques | Academia / Education | General | Beginner Technical | Tutorial | Inference Performance

 About the Authors
 

 About Luis Ceze
 

 
 Luis Ceze is VP of AI Systems Software at NVIDIA, focused on AI compilers and inference technology. He received his PhD in Computer Science from UIUC and is a Professor of Computer Science and Engineering at the University of Washington. His research interests are in efficient and agile AI systems and the intersection of AI and biology. He is a Fellow of the ACM.
 
 
 

 View all posts by Luis Ceze

 About Zihao Ye
 

 
 Zihao Ye is a senior compiler engineer at NVIDIA and a PhD student at the University of Washington. His research interests include efficient LLM inference and machine learning compilers.
 
 
 

 View all posts by Zihao Ye

 About Tianqi Chen
 

 
 Tianqi Chen is an engineer at NVIDIA and an Assistant Professor at Carnegie Mellon University, focused on AI compilers and systems. He received his Ph.D. from the Paul G. Allen School of Computer Science & Engineering, University of Washington
 
 
 

 View all posts by Tianqi Chen

 About Vinod Grover
 

 
 Vinod Grover is a Senior Distinguished Engineer at NVIDIA. He has led the CUDA C++ development from its beginnings and is currently interested in AI Compilers, GPU Computing, and Programming Languages. He received an MS in Computer Science from Syracuse University.
 
 

 Follow @vinodg on Twitter

 View all posts by Vinod Grover

 About Mehdi Amini
 

 
 Mehdi Amini is an engineer at NVIDIA with a strong background in compiler systems. He received his PhD in computer science from École des Mines de Paris.
 
 
 

 View all posts by Mehdi Amini

 About Nick Comly
 

 
 Nick Comly leads products for inference optimization at NVIDIA. His team focuses on pushing the capabilities and performance of the NVIDIA stack for GenAI developers. Nick received his M.S. from Stanford University, where he specialized in deep learning and optimization.
 
 
 

 View all posts by Nick Comly

Comments

Related posts

 NVIDIA Dynamo Accelerates llm-d Community Initiatives for Advancing Large-Scale Distributed Inference
 

NVIDIA Dynamo Accelerates llm-d Community Initiatives for Advancing Large-Scale Distributed Inference

 NVIDIA NIM 1.4 Ready to Deploy with 2.4x Faster Inference
 

NVIDIA NIM 1.4 Ready to Deploy with 2.4x Faster Inference

 Boosting Llama 3.1 405B Throughput by Another 1.5x on NVIDIA H200 Tensor Core GPUs and NVLink Switch
 

Boosting Llama 3.1 405B Throughput by Another 1.5x on NVIDIA H200 Tensor Core GPUs and NVLink Switch

 NVIDIA GH200 Grace Hopper Superchip Delivers Outstanding Performance in MLPerf Inference v4.1
 

NVIDIA GH200 Grace Hopper Superchip Delivers Outstanding Performance in MLPerf Inference v4.1

 Turbocharging Meta Llama 3 Performance with NVIDIA TensorRT-LLM and NVIDIA Triton Inference Server
 

Turbocharging Meta Llama 3 Performance with NVIDIA TensorRT-LLM and NVIDIA Triton Inference Server

Related posts

 Accelerating Vision AI Pipelines with Batch Mode VC-6 and NVIDIA Nsight
 

Accelerating Vision AI Pipelines with Batch Mode VC-6 and NVIDIA Nsight

 Maximize AI Infrastructure Throughput by Consolidating Underutilized GPU Workloads
 

Maximize AI Infrastructure Throughput by Consolidating Underutilized GPU Workloads

 How to Build Deep Agents for Enterprise Search with NVIDIA AI-Q and LangChain
 

How to Build Deep Agents for Enterprise Search with NVIDIA AI-Q and LangChain

 Building the AI Grid with NVIDIA: Orchestrating Intelligence Everywhere 
 

Building the AI Grid with NVIDIA: Orchestrating Intelligence Everywhere 

 How NVIDIA Dynamo 1.0 Powers Multi-Node Inference at Production Scale
 

How NVIDIA Dynamo 1.0 Powers Multi-Node Inference at Production Scale

L

T

F

R

E

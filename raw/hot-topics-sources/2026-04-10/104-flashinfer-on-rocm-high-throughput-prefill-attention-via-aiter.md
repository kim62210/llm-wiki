---
title: FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER — ROCm Blogs
source_url: https://rocm.blogs.amd.com/artificial-intelligence/flashinfer-release2/README.html
final_url: https://rocm.blogs.amd.com/artificial-intelligence/flashinfer-release2/README.html
status: 200
content_type: text/html; charset=utf-8
topics: [FlashInfer Kernel Library for LLM Serving]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.365298+00:00
---

# FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER — ROCm Blogs

## 원본 URL

https://rocm.blogs.amd.com/artificial-intelligence/flashinfer-release2/README.html

## 추출 본문

FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER — ROCm BlogsSkip to main content

 Back to top
 

Ctrl+K

ROCm™ Blogs

 Home
 

 AI
 

 HPC
 

 Data Science
 

 Systems
 

 Developers
 

 Robotics
 

ROCm blogs

FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER

 Contents 

What is FlashInfer?

FlashInfer on ROCm
Feature Support Matrix

Porting to Modern CDNA Architectures

Experimental AITER Backend Support
Known Limitations

Getting Started
Single-request Prefill Attention with AITER Backend

Batched Prefill with Paged KV Cache

Summary

Acknowledgements

References

Disclaimers

FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER#

 April 06, 2026 by Debasis Mandal, Diptorup Deb, Rishi Madduri, Anuya Welling, Mukhil Azhagan Mallaiyan Sathiaseelan, Yao Liu, Phani Vaddadi, Vish Vadlamani.

2 min read. | 556 total words.

Applications & models

AI/ML, GenAI, Optimization, Serving

AI

The explosive growth of large language models (LLMs) like DeepSeek-R1, Llama 3, and Qwen 3 has created an urgent need for efficient inference solutions. As these models scale to billions of parameters and context lengths extend to hundreds of thousands of tokens, the attention mechanism becomes a critical bottleneck, consuming substantial memory for key-value (KV) caches and requiring significant compute for each token generated.

FlashInfer1 addresses these challenges with a high-performance library that optimizes the attention computation at the heart of transformer inference. Originally developed for NVIDIA GPUs, FlashInfer on ROCm brings accelerated LLM serving to AMD Instinct GPUs. Building on the earlier release of decode kernels, this release adds prefill kernels to complete the core attention operations needed for production LLM serving.

This blog covers the porting effort to AMD’s modern CDNA architectures (CDNA32 and CDNA43) and demonstrates how to use FlashInfer1 for prefill operations on AMD hardware.

What is FlashInfer?#

FlashInfer is a kernel library specifically designed for LLM serving workloads. Unlike general-purpose attention implementations, FlashInfer optimizes for the unique characteristics of inference:

Prefill phase: Processing the initial prompt requires computing attention over the entire input sequence, a compute-intensive operation that benefits from high throughput.

Decode phase: Generating tokens one-by-one requires low-latency attention against a growing KV cache, a memory-bound operation that benefits from efficient memory access patterns.

FlashInfer provides specialized kernels for each phase:

Capability

Description

Paged KV-Cache

Manages memory like virtual memory pages, eliminating fragmentation and enabling efficient memory utilization across variable-length sequences

Grouped Query Attention (GQA)

Native support for Grouped Query Attention (GQA) and Multi-Query Attention (MQA), reducing KV cache memory requirements

Ragged Tensors

Efficiently handles batches of sequences with different lengths without padding overhead

FlashInfer on ROCm#

Installation guide

Docker images

GitHub repository

The ROCm port of FlashInfer brings the above optimizations to AMD Instinct GPUs. This release updates FlashInfer on ROCm from version 0.2.5 to 0.5.3, adding the FlashAttention-2 based prefill kernels, including single-request, batched, and ragged variants, to AMD’s CDNA3 and CDNA4 architectures, complementing the decode kernels ported in the earlier release.

Feature Support Matrix#

Kernel Type

FP16 / BF16

FP8

Notes

Decode Attention

✅

✅

Supports MHA, GQA, and MQA

Prefill Attention

✅

WIP

Supports MHA, GQA, and MQA

Additional features from upstream FlashInfer, including FP8 support for prefill, cascade attention, Multi-Head Latent Attention (MLA), and positional encodings (RoPE/ALiBi), are actively under development. Refer to the Feature Support Matrix in the 
README
 of the GitHub repository for the latest status.

Porting to Modern CDNA Architectures#

Adapting FlashInfer to AMD GPUs required fundamental changes to its kernel architecture. The port involved restructuring four core computational stages: loading query matrices into shared memory, streaming key/value data, computing query-key dot products, and performing the softmax-value multiplication.

The primary changes centered on replacing NVIDIA’s warp matrix operations (wmma) with CDNA3/CDNA4 Matrix Fused Multiply-Add (MFMA) instructions. This required:

Restructuring thread layouts from 32-thread warps to 64-thread wavefronts

Modifying shared memory access patterns to accommodate different bank conflict and coalescing requirements

Updating indexing logic to align with MFMA’s 16×16 matrix tile geometry

These optimizations enable FlashAttention-2’s online softmax algorithm and block-sparse attention patterns to run efficiently on modern AMD CDNA GPUs.

Experimental AITER Backend Support#

This release of FlashInfer on ROCm also provides experimental support for using AITER4 as a backend, in addition to the above HIP5-based implementation. The AITER backend is currently enabled for the 
single_prefill
 and 
batch_prefill
 kernels.

Known Limitations#

The AITER backend supports the 
NHD
 kv_layout; other kv_layout values are unsupported. Additionally, when using CK6 (Composable Kernel) FMHA kernels for AITER Multi-Head Attention (MHA), batch prefill is limited to page sizes 1, 16, and 1024.

Getting Started#

Please look at the installation guide for detailed instructions on how to install FlashInfer on ROCm.

The quickest way to get started is by using a prebuilt Docker image that includes FlashInfer, PyTorch, AITER, and all other dependencies.

First, ensure that the following requirements are met:

Linux: Ubuntu 24.04 (see supported distributions)

Hardware: AMD Instinct MI300X or MI325X (gfx942 / CDNA3 architecture), or MI355X (gfx950 / CDNA4 architecture)

Next, pull the FlashInfer image from Docker Hub.

dockerpullrocm/flashinfer:flashinfer-0.5.3.amd1_rocm7.2_ubuntu24.04_py3.12_pytorch2.9.1

Finally, start a container with GPU access.

dockerrun-it--rm\
--privileged\
--network=host--device=/dev/kfd\
--device=/dev/dri--group-addvideo\
--name=my_flashinfer--cap-add=SYS_PTRACE\
--security-optseccomp=unconfined\
--ipc=host--shm-size16G\
rocm/flashinfer:flashinfer-0.5.3.amd1_rocm7.2_ubuntu24.04_py3.12_pytorch2.9.1

Micromamba is pre-configured inside the container and will automatically start the 
base
 environment.

Verify the installation by running the following command. It should output 
0.5.3+amd.1
.

python-c"import flashinfer; print(flashinfer.__version__)"

To see FlashInfer in action, save the following examples to a file 
prefill.py
 and run 
pythonprefill.py
.

Single-request Prefill Attention with AITER Backend#

The prefill phase processes the initial prompt by computing attention over the entire input sequence. This is compute-bound and benefits from high-throughput kernels. To use AITER as the backend for these kernels, set 
backend="aiter"
 as a keyword argument when invoking the kernels, as can be seen below.

importtorchimportflashinfer# Configurationseq_len=1024# Prompt lengthnum_qo_heads=32# Number of query/output headsnum_kv_heads=8# Number of KV heads (GQA with 4:1 ratio)head_dim=128# Create Q, K, V tensors (NHD layout: sequence, heads, dimension)q=torch.randn(seq_len,num_qo_heads,head_dim,dtype=torch.float16,device="cuda")k=torch.randn(seq_len,num_kv_heads,head_dim,dtype=torch.float16,device="cuda")v=torch.randn(seq_len,num_kv_heads,head_dim,dtype=torch.float16,device="cuda")# Run single prefill attention with causal maskingoutput=flashinfer.single_prefill_with_kv_cache(q,k,v,causal=True,backend="aiter")

Batched Prefill with Paged KV Cache#

For production serving with multiple concurrent requests of various sequence lengths, FlashInfer supports batched prefill with paged KV caches. This enables efficient memory management across requests with varying context lengths, similar to virtual memory paging.

importtorchimportflashinferbatch_size=4seq_len=512# Sequence length per requestpage_size=16# KV cache page sizenum_qo_heads=32# Number of query/output headsnum_kv_heads=8# Number of KV heads (GQA)head_dim=128# Calculate paging parametersnum_pages_per_seq=(seq_len+page_size-1)//page_sizetotal_pages=num_pages_per_seq*batch_size# Flattened query tensor: all sequences concatenatedq=torch.randn(batch_size*seq_len,num_qo_heads,head_dim,dtype=torch.float16,device="cuda")# Paged KV cache: [total_pages, 2, page_size, num_kv_heads, head_dim]kv_data=torch.randn(total_pages,2,page_size,num_kv_heads,head_dim,dtype=torch.float16,device="cuda")# Index pointers and page table metadataq_indptr=torch.arange(0,batch_size+1,dtype=torch.int32,device="cuda")*seq_lenkv_indptr=torch.arange(0,batch_size+1,dtype=torch.int32,device="cuda")*num_pages_per_seqkv_indices=torch.arange(0,total_pages,dtype=torch.int32,device="cuda")kv_last_page_len=torch.full((batch_size,),(seq_len-1)%page_size+1,dtype=torch.int32,device="cuda")# Create workspace and wrapperworkspace=torch.empty(512*1024*1024,dtype=torch.int8,device="cuda")wrapper=flashinfer.prefill.BatchPrefillWithPagedKVCacheWrapper(workspace,"NHD",backend="aiter")# Plan the batched operationwrapper.plan(q_indptr,kv_indptr,kv_indices,kv_last_page_len,num_qo_heads,num_kv_heads,head_dim,page_size,causal=True)# Execute batched prefilloutput=wrapper.run(q,kv_data)

For more examples, including batched prefill with ragged tensors, see the examples directory in the FlashInfer repository.

Summary#

FlashInfer on ROCm brings high-performance LLM inference to AMD Instinct GPUs. With optimized kernels for both prefill and decode phases, support for modern attention variants like GQA and MQA, and efficient paged KV cache management, FlashInfer enables production-grade LLM serving on AMD hardware.

Key highlights of this release:

Prefill kernels: for single-request, batched, and ragged attention patterns

Decode kernels: with FP8 support for memory-efficient token generation

Paged KV cache: support for efficient memory management in serving scenarios

Native GQA/MQA support: for modern model architectures

Development continues with cascade attention, positional encodings, and sampling kernels on the roadmap. We encourage you to try FlashInfer on ROCm and share your feedback through the GitHub repository.

Acknowledgements#

The authors wish to acknowledge the AMD teams that supported this work, whose contributions were instrumental in enabling FlashInfer: Aditya Bhattacharji, Pankaj Gupta, Radha Srimanthula, Anisha Sankar, Amit Kumar, Ram Seenivasan, Eliot Li, Ian Dass, Kiran Thumma, Aakash Sudhanwa, Ehud Sharlin, Saad Rahim, Lucia Cao, Jacky Zhao, Zhen Han, Junhua (Richard) Hou, Lin Sun, Carlus Huang, Hai Xiao.

References#

[1] Ye, Z., et al. (2025). FlashInfer: Efficient and customizable attention engine for LLM inference serving. arXiv:2501.01005

[2] AMD CDNA 3 Architecture. White paper

[3] AMD CDNA 4 Architecture. White paper

[4] Pandey, S., et al. (2025). AITER: AI Tensor Engine for ROCm. ROCm technical blog

[5] HIP: C++ runtime API and kernel language for AMD GPUs (Heterogeneous-computing Interface for Portability). ROCm documentation

[6] Composable Kernel — programming model for performance-critical kernels for machine learning workloads on AMD GPUs. ROCm documentation

Disclaimers#

Third-party content is licensed to you directly by the third party that owns the
content and is not licensed to you by AMD. ALL LINKED THIRD-PARTY CONTENT IS
PROVIDED “AS IS” WITHOUT A WARRANTY OF ANY KIND. USE OF SUCH THIRD-PARTY CONTENT
IS DONE AT YOUR SOLE DISCRETION AND UNDER NO CIRCUMSTANCES WILL AMD BE LIABLE TO
YOU FOR ANY THIRD-PARTY CONTENT. YOU ASSUME ALL RISK AND ARE SOLELY RESPONSIBLE
FOR ANY DAMAGES THAT MAY ARISE FROM YOUR USE OF THIRD-PARTY CONTENT.

 Contents
 

What is FlashInfer?

FlashInfer on ROCm
Feature Support Matrix

Porting to Modern CDNA Architectures

Experimental AITER Backend Support
Known Limitations

Getting Started
Single-request Prefill Attention with AITER Backend

Batched Prefill with Paged KV Cache

Summary

Acknowledgements

References

Disclaimers

Terms and Conditions

Privacy

Trademarks

Supply Chain Transparency

Fair and Open Competition

UK Tax Strategy

Cookie Policy

Cookie Settings

© 2025 Advanced Micro Devices, Inc

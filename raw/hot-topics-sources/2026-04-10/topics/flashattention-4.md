---
title: FlashAttention-4 on Blackwell
section: Inference Optimization
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# FlashAttention-4 on Blackwell

## 기존 큐레이션 요약

- 정의: Blackwell GPU 비대칭 스케일링에 맞춘 attention 커널 재설계.
- 왜 중요한가: Tri Dao 팀이 2026년 3월 발표, B200에서 1613 TFLOPs/s(71% 활용률)로 cuDNN 대비 1.3배, Triton 대비 2.7배 속도 향상을 달성했다. softmax 지수 연산 소프트웨어 에뮬레이션과 2-CTA MMA 모드 활용이 핵심이다.

## 개별 원문 수집 스냅샷

### FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

- URL: https://arxiv.org/abs/2603.05451
- raw snapshot: `raw/hot-topics-sources/2026-04-10/066-flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardwa.md`
- 수집 제목: [2603.05451] FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

[2603.05451] FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2603.05451 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2603.05451 (cs) [Submitted on 5 Mar 2026] Title:FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling Authors:Ted Zadouri, Markus Hoehnerbach, Jay Shah, Timmy Liu, Vijay 

### FlashAttention-4 blog post by Tri Dao

- URL: https://tridao.me/blog/2026/flash4
- raw snapshot: `raw/hot-topics-sources/2026-04-10/067-flashattention-4-blog-post-by-tri-dao.md`
- 수집 제목: FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | Tri Dao

FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | Tri Dao Tri Dao Toggle navigation About Blog Publications Awards Repositories Teaching ctrl k FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling Contents New hardware features on Blackwell Feeds and Speeds Forward pass: New softmax pipelining with conditional rescaling Pipeline: Ping-pong Q tiles plus a dedicated correction stage Faster exponential: Distribute 2^x across MUFU.EX2 and FMA Backward pass: Where shared memory traffic dominates Pipeline: Overlap MMAs with softmax 2-CTA backward pass: Reducing shared memory traffic and global atomic adds Deterministic mode Scheduling Language and framework: CuTe-DSL Attention Benchmarks Acknowledgements [Paper] [

### FlashAttention-4 Princeton AI Lab blog

- URL: https://blog.ai.princeton.edu/2026/03/12/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling
- raw snapshot: `raw/hot-topics-sources/2026-04-10/068-flashattention-4-princeton-ai-lab-blog.md`
- 수집 제목: FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling – Princeton Laboratory for Artificial Intelligence Research Blog

FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling – Princeton Laboratory for Artificial Intelligence Research Blog About Mailing List Website Contact Us Subscribe Princeton Laboratory for Artificial Intelligence Research Blog FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling March 12, 2026 By Ted Zadouri (Princeton University, Together AI); Markus Hoehnerbach (Meta); Jay Shah (Colfax Research); Timmy Liu (Nvidia); Vijay Thakkar (Meta, Georgia Tech); and Tri Dao (Princeton University, Together AI) Transformers remain the backbone for most AI applications, from large language models to vision and multimodal systems. For transformers, attention is the primary computational bottleneck, with self-attention score

### Dao-AILab/flash-attention GitHub repository

- URL: https://github.com/Dao-AILab/flash-attention
- raw snapshot: `raw/hot-topics-sources/2026-04-10/069-dao-ailab-flash-attention-github-repository.md`
- 수집 제목: GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact attention · GitHub

GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact attention · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams 

### Generalized Dot-Product Attention PyTorch blog

- URL: https://pytorch.org/blog
- raw snapshot: `raw/hot-topics-sources/2026-04-10/070-generalized-dot-product-attention-pytorch-blog.md`
- 수집 제목: Blog – PyTorch

Blog – PyTorchSkip to main content Register for PyTorch Conference Europe 2026, April 7–8, Paris Search Close Search search Menu Learn Get Started Tutorials Learn the Basics PyTorch Recipes Intro to PyTorch – YouTube Series Webinars Community Landscape Join the Ecosystem Community Hub Forums Developer Resources Events Meeting Calendar PyTorch Contributor Awards PyTorch Ambassadors Projects PyTorch vLLM DeepSpeed Ray Helion Safetensors Host Your Project Docs PyTorch Domains Blog & News Blog Announcements Case Studies Newsletter About PyTorch Foundation Members Governing Board Technical Advisory Council Cloud Credit Program Staff Contact Brand Guidelines JOIN search Blog Faster Diffusion on Blackwell: MXFP8 and NVFP4 with Diffusers and TorchAOBlog Faster Diffusion on Blackwell: MXFP8 and NVF

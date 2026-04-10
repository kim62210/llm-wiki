---
title: [2501.01005] FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving
source_url: https://arxiv.org/abs/2501.01005
final_url: https://arxiv.org/abs/2501.01005
status: 200
content_type: text/html; charset=utf-8
topics: [FlashInfer Kernel Library for LLM Serving]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:38.604725+00:00
---

# [2501.01005] FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving

## 원본 URL

https://arxiv.org/abs/2501.01005

## 추출 본문

[2501.01005] FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2501.01005
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Distributed, Parallel, and Cluster Computing

arXiv:2501.01005 (cs)
 

 [Submitted on 2 Jan 2025 (v1), last revised 21 Apr 2025 (this version, v2)]

Title:FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving

Authors:Zihao Ye, Lequn Chen, Ruihang Lai, Wuwei Lin, Yineng Zhang, Stephanie Wang, Tianqi Chen, Baris Kasikci, Vinod Grover, Arvind Krishnamurthy, Luis Ceze

View a PDF of the paper titled FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving, by Zihao Ye and 10 other authors
View PDFHTML (experimental)
Abstract:Transformers, driven by attention mechanisms, form the foundation of large language models (LLMs). As these models scale up, efficient GPU attention kernels become essential for high-throughput and low-latency inference. Diverse LLM applications demand flexible and high-performance attention solutions. We present FlashInfer: a customizable and efficient attention engine for LLM serving. FlashInfer tackles KV-cache storage heterogeneity using block-sparse format and composable formats to optimize memory access and reduce redundancy. It also offers a customizable attention template, enabling adaptation to various settings through Just-In-Time (JIT) compilation. Additionally, FlashInfer's load-balanced scheduling algorithm adjusts to dynamism of user requests while maintaining compatibility with CUDAGraph which requires static configuration. FlashInfer have been integrated into leading LLM serving frameworks like SGLang, vLLM and MLC-Engine. Comprehensive kernel-level and end-to-end evaluations demonstrate FlashInfer's ability to significantly boost kernel performance across diverse inference scenarios: compared to state-of-the-art LLM serving solutions, FlashInfer achieve 29-69% inter-token-latency reduction compared to compiler backends for LLM serving benchmark, 28-30% latency reduction for long-context inference, and 13-17% speedup for LLM serving with parallel generation.
 

Comments:Accepted by MLSys 2025, code available at this http URLSubjects:Distributed, Parallel, and Cluster Computing (cs.DC); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)Cite as:arXiv:2501.01005 [cs.DC](or arXiv:2501.01005v2 [cs.DC] for this version)
 https://doi.org/10.48550/arXiv.2501.01005
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Zihao Ye [view email] 
[v1]
 Thu, 2 Jan 2025 02:02:20 UTC (1,326 KB)
[v2]
 Mon, 21 Apr 2025 20:10:11 UTC (1,376 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving, by Zihao Ye and 10 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.DC

< prev  |  next >

new | recent | 2025-01

 Change to browse by:
 
cs
cs.AI
cs.LG

References & Citations

NASA ADS

Google Scholar

Semantic Scholar

export BibTeX citationLoading...

BibTeX formatted citation
×

loading...

Data provided by: 

Bookmark

Bibliographic Tools

Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer(What is the Explorer?)

Connected Papers Toggle

Connected Papers(What is Connected Papers?)

Litmaps Toggle

Litmaps(What is Litmaps?)

scite.ai Toggle

scite Smart Citations(What are Smart Citations?)

Code, Data, Media

Code, Data and Media Associated with this Article

alphaXiv Toggle

alphaXiv(What is alphaXiv?)

Links to Code Toggle

CatalyzeX Code Finder for Papers(What is CatalyzeX?)

DagsHub Toggle

DagsHub(What is DagsHub?)

GotitPub Toggle

Gotit.pub(What is GotitPub?)

Huggingface Toggle

Hugging Face(What is Huggingface?)

Links to Code Toggle

Papers with Code(What is Papers with Code?)

ScienceCast Toggle

ScienceCast(What is ScienceCast?)

Demos

Demos

Replicate Toggle

Replicate(What is Replicate?)

Spaces Toggle

Hugging Face Spaces(What is Spaces?)

Spaces Toggle

TXYZ.AI(What is TXYZ.AI?)

Related Papers

Recommenders and Search Tools

Link to Influence Flower

Influence Flower(What are Influence Flowers?)

Core recommender toggle

CORE Recommender(What is CORE?)

Author

Venue

Institution

Topic

 About arXivLabs
 

arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

Which authors of this paper are endorsers? |
 Disable MathJax (What is MathJax?)
 

About

Help

 Contact

 Subscribe

Copyright

Privacy Policy

Web Accessibility Assistance

arXiv Operational Status

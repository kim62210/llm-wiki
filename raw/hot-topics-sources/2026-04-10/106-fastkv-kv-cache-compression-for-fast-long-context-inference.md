---
title: [2502.01068] FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration
source_url: https://arxiv.org/abs/2502.01068
final_url: https://arxiv.org/abs/2502.01068
status: 200
content_type: text/html; charset=utf-8
topics: [Chunk-Semantic KV Cache Compression]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.139270+00:00
---

# [2502.01068] FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration

## 원본 URL

https://arxiv.org/abs/2502.01068

## 추출 본문

[2502.01068] FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2502.01068
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2502.01068 (cs)
 

 [Submitted on 3 Feb 2025 (v1), last revised 16 Feb 2026 (this version, v6)]

Title:FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration

Authors:Dongwon Jo, Jiwon Song, Yulhwa Kim, Jae-Joon Kim

View a PDF of the paper titled FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration, by Dongwon Jo and 3 other authors
View PDFHTML (experimental)
Abstract:While large language models (LLMs) excel at handling long-context sequences, they require substantial prefill computation and key-value (KV) cache, which can heavily burden computational efficiency and memory usage in both prefill and decoding stages. Recent works that compress KV caches with prefill acceleration reduce this cost but inadvertently tie the prefill compute reduction to the decoding KV budget. This coupling arises from overlooking the layer-dependent variation of critical context, often leading to accuracy degradation. To address this issue, we introduce FastKV, a KV cache compression framework designed to reduce latency in both prefill and decoding by leveraging the stabilization of token importance in later layers. FastKV performs full-context computation until a Token-Selective Propagation (TSP) layer, which forwards only the most informative tokens to subsequent layers. From these propagated tokens, FastKV independently selects salient KV entries for caching, thereby decoupling KV budget from the prefill compute reduction based on the TSP decision. This independent control of the TSP rate and KV retention rate enables flexible optimization of efficiency and accuracy. Experimental results show that FastKV achieves speedups of up to 1.82$\times$ in prefill and 2.87$\times$ in decoding compared to the full-context baseline, while matching the accuracy of the baselines that only accelerate the decoding stage. Our code is available at this https URL.
 

Subjects:Machine Learning (cs.LG); Computation and Language (cs.CL)Cite as:arXiv:2502.01068 [cs.LG](or arXiv:2502.01068v6 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2502.01068
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Jiwon Song [view email] 
[v1]
 Mon, 3 Feb 2025 05:25:09 UTC (5,087 KB)
[v2]
 Wed, 21 May 2025 06:45:58 UTC (5,818 KB)
[v3]
 Sun, 26 Oct 2025 12:06:24 UTC (1,514 KB)
[v4]
 Tue, 28 Oct 2025 04:00:18 UTC (1,514 KB)
[v5]
 Fri, 6 Feb 2026 07:50:35 UTC (1,525 KB)
[v6]
 Mon, 16 Feb 2026 06:37:44 UTC (1,525 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration, by Dongwon Jo and 3 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2025-02

 Change to browse by:
 
cs
cs.CL

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

IArxiv recommender toggle

IArxiv Recommender(What is IArxiv?)

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

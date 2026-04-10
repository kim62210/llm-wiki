---
title: [2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference
source_url: https://arxiv.org/abs/2502.00299
final_url: https://arxiv.org/abs/2502.00299
status: 200
content_type: text/html; charset=utf-8
topics: [Chunk-Semantic KV Cache Compression]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.043395+00:00
---

# [2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference

## 원본 URL

https://arxiv.org/abs/2502.00299

## 추출 본문

[2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2502.00299
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2502.00299 (cs)
 

 [Submitted on 1 Feb 2025 (v1), last revised 14 Oct 2025 (this version, v5)]

Title:ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference

Authors:Xiang Liu, Zhenheng Tang, Peijie Dong, Zeyu Li, Yue Liu, Bo Li, Xuming Hu, Xiaowen Chu

View a PDF of the paper titled ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference, by Xiang Liu and 7 other authors
View PDFHTML (experimental)
Abstract:Large Language Models (LLMs) require significant GPU memory when processing long texts, with the key value (KV) cache consuming up to 70\% of total memory during inference. Although existing compression methods reduce memory by evaluating the importance of individual tokens, they overlook critical semantic relationships between tokens, resulting in fragmented context and degraded performance. We introduce ChunkKV, which fundamentally reimagines KV cache compression by treating semantic chunks - rather than isolated tokens - as basic compression units. This approach preserves complete linguistic structures and contextual integrity, ensuring that essential meaning is retained even under aggressive compression. Our innovation includes a novel layer-wise index reuse technique that exploits the higher cross-layer similarity of preserved indices in ChunkKV, reducing computational overhead and improving throughput by 26.5\%. Comprehensive evaluations on challenging benchmarks: LongBench, Needle-In-A-HayStack, GSM8K, and JailbreakV demonstrate that ChunkKV outperforms state-of-the-art methods by up to 8.7\% in precision while maintaining the same compression ratio. These results confirm that semantic-aware compression significantly enhances both efficiency and performance for long-context LLM inference, providing a simple yet effective solution to the memory bottleneck problem. The code is available at \href{this https URL}{link}.
 

Comments:NeurIPS 2025Subjects:Computation and Language (cs.CL)Cite as:arXiv:2502.00299 [cs.CL](or arXiv:2502.00299v5 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2502.00299
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Xiang Liu [view email] 
[v1]
 Sat, 1 Feb 2025 03:49:47 UTC (713 KB)
[v2]
 Wed, 21 May 2025 10:38:37 UTC (698 KB)
[v3]
 Fri, 27 Jun 2025 09:14:02 UTC (699 KB)
[v4]
 Thu, 2 Oct 2025 19:09:19 UTC (645 KB)
[v5]
 Tue, 14 Oct 2025 15:42:41 UTC (637 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference, by Xiang Liu and 7 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2025-02

 Change to browse by:
 
cs

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

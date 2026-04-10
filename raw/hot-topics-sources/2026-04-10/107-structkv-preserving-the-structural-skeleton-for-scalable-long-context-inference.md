---
title: [2604.06746] StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference
source_url: https://arxiv.org/abs/2604.06746
final_url: https://arxiv.org/abs/2604.06746
status: 200
content_type: text/html; charset=utf-8
topics: [Chunk-Semantic KV Cache Compression]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.225245+00:00
---

# [2604.06746] StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference

## 원본 URL

https://arxiv.org/abs/2604.06746

## 추출 본문

[2604.06746] StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2604.06746
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2604.06746 (cs)
 

 [Submitted on 8 Apr 2026]

Title:StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference

Authors:Zhirui Chen, Peiyang Liu, Ling Shao

View a PDF of the paper titled StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference, by Zhirui Chen and 2 other authors
View PDFHTML (experimental)
Abstract:As Large Language Models (LLMs) scale to support context windows exceeding one million tokens, the linear growth of Key-Value (KV) cache imposes severe memory capacity and bandwidth bottlenecks, constraining the efficiency of long-context inference. Existing compression approaches typically prioritize tokens based on local saliency metrics to decouple prefill computation from decoding memory. However, these methods often rely on local saliency snapshots at a specific layer, thereby systematically discarding tokens that act as global information hubs across the network depth but appear temporarily dormant at the specific layer selected for pruning. To address this limitation, we propose StructKV, a structure-aware KV cache compression framework that introduces three core innovations: First, Global In-Degree Centrality aggregates attention patterns across the network depth to identify global information hubs. Second, Dynamic Pivot Detection utilizes information-theoretic metrics to adaptively locate the optimal layer for compression. Finally, Structural Propagation and Decoupling separates the computational budget from the memory storage budget. Experimental results on the LongBench and RULER benchmarks demonstrate that StructKV effectively preserves long-range dependencies and retrieval robustness.
 

Comments:Accepted to ACL 2026 Findings, 14 pagesSubjects:Computation and Language (cs.CL)Cite as:arXiv:2604.06746 [cs.CL](or arXiv:2604.06746v1 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2604.06746
Focus to learn more
 arXiv-issued DOI via DataCite (pending registration)

Submission history
 From: Zhirui Chen [view email] 
[v1]
 Wed, 8 Apr 2026 07:10:35 UTC (13,081 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference, by Zhirui Chen and 2 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2026-04

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

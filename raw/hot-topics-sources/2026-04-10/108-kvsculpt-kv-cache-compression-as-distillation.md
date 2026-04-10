---
title: [2603.27819] KVSculpt: KV Cache Compression as Distillation
source_url: https://arxiv.org/abs/2603.27819
final_url: https://arxiv.org/abs/2603.27819
status: 200
content_type: text/html; charset=utf-8
topics: [Chunk-Semantic KV Cache Compression]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.328238+00:00
---

# [2603.27819] KVSculpt: KV Cache Compression as Distillation

## 원본 URL

https://arxiv.org/abs/2603.27819

## 추출 본문

[2603.27819] KVSculpt: KV Cache Compression as Distillation
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2603.27819
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2603.27819 (cs)
 

 [Submitted on 29 Mar 2026]

Title:KVSculpt: KV Cache Compression as Distillation

Authors:Bo Jiang, Sian Jin

View a PDF of the paper titled KVSculpt: KV Cache Compression as Distillation, by Bo Jiang and 1 other authors
View PDFHTML (experimental)
Abstract:KV cache compression is critical for efficient long-context LLM inference. Approaches that reduce the per-pair footprint -- quantization and low-rank decomposition -- are orthogonal to those that reduce the sequence length of the cache. Along the sequence-length dimension, existing methods range from pure eviction -- selecting which KV pairs to keep -- to merging, which combines similar pairs into fewer ones. Both remain anchored to the original cache entries. We propose KVSculpt, which moves to the other end of this spectrum: instead of selecting or combining original pairs, we optimize a smaller set of unconstrained KV pairs in continuous embedding space to preserve each layer's attention behavior. Keys are optimized via L-BFGS and values are solved in closed form via least squares, alternating every few steps. On top of this, we introduce adaptive budget allocation, which uses a cheap pilot compression run to redistribute the compression budget across layers and KV heads based on per-component difficulty. On Qwen2.5-1.5B-Instruct with 2048-token contexts, KVSculpt reduces KL divergence by 3.5-4.1x compared to Select+Fit -- attention-score eviction with least-squares value fitting -- across compression ratios r in {0.3, 0.5, 0.7}. Adaptive allocation provides an additional 1.3x KL reduction at no extra inference cost. Analysis reveals that compression difficulty is highly non-uniform: per-layer pilot MSE varies by up to 100x across layers, and the two KV heads within a single layer can differ by up to 467x -- demonstrating that fine-grained budget allocation is essential.
 

Subjects:Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)Cite as:arXiv:2603.27819 [cs.LG](or arXiv:2603.27819v1 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2603.27819
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Bo Jiang [view email] 
[v1]
 Sun, 29 Mar 2026 19:14:25 UTC (31 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled KVSculpt: KV Cache Compression as Distillation, by Bo Jiang and 1 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2026-03

 Change to browse by:
 
cs
cs.AI
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

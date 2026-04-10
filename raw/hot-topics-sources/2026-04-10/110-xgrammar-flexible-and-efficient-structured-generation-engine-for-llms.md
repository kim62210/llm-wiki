---
title: [2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models
source_url: https://arxiv.org/abs/2411.15100
final_url: https://arxiv.org/abs/2411.15100
status: 200
content_type: text/html; charset=utf-8
topics: [XGrammar-2 Constrained Decoding for Agentic LLMs]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.590923+00:00
---

# [2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models

## 원본 URL

https://arxiv.org/abs/2411.15100

## 추출 본문

[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2411.15100
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2411.15100 (cs)
 

 [Submitted on 22 Nov 2024 (v1), last revised 12 May 2025 (this version, v3)]

Title:XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models

Authors:Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, Tianqi Chen

View a PDF of the paper titled XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models, by Yixin Dong and 6 other authors
View PDFHTML (experimental)
Abstract:The applications of LLM Agents are becoming increasingly complex and diverse, leading to a high demand for structured outputs that can be parsed into code, structured function calls, and embodied agent commands. These developments bring significant demands for structured generation in LLM inference. Context-free grammar is a flexible approach to enable structured generation via constrained decoding. However, executing context-free grammar requires going through several stack states over all tokens in vocabulary during runtime, bringing non-negligible overhead for structured generation. In this paper, we propose XGrammar, a flexible and efficient structure generation engine for large language models. XGrammar accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be interpreted during runtime. We further build transformations to expand the grammar context and reduce the number of context-independent tokens. Additionally, we build an efficient persistent stack to accelerate the context-dependent token checks. Finally, we co-design the grammar engine with LLM inference engine to overlap grammar computation with GPU executions. Evaluation results show that XGrammar can achieve up to 100x speedup over existing solutions. Combined with an LLM inference engine, it can generate near-zero overhead structure generation in end-to-end low-LLM serving.
 

Comments:MLSys '25Subjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Programming Languages (cs.PL)Cite as:arXiv:2411.15100 [cs.CL](or arXiv:2411.15100v3 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2411.15100
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Yixin Dong [view email] 
[v1]
 Fri, 22 Nov 2024 18:01:37 UTC (527 KB)
[v2]
 Wed, 27 Nov 2024 18:59:28 UTC (531 KB)
[v3]
 Mon, 12 May 2025 08:20:08 UTC (460 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models, by Yixin Dong and 6 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2024-11

 Change to browse by:
 
cs
cs.AI
cs.PL

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

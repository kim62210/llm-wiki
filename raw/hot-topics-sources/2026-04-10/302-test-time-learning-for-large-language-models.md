---
title: [2505.20633] Test-Time Learning for Large Language Models
source_url: https://arxiv.org/abs/2505.20633
final_url: https://arxiv.org/abs/2505.20633
status: 200
content_type: text/html; charset=utf-8
topics: [Test-Time Training & Self-Improvement]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.893073+00:00
---

# [2505.20633] Test-Time Learning for Large Language Models

## 원본 URL

https://arxiv.org/abs/2505.20633

## 추출 본문

[2505.20633] Test-Time Learning for Large Language Models
Skip to main content

In just 5 minutes help us improve arXiv:
Annual Global Survey

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2505.20633
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2505.20633 (cs)
 

 [Submitted on 27 May 2025]

Title:Test-Time Learning for Large Language Models

Authors:Jinwu Hu, Zhitian Zhang, Guohao Chen, Xutao Wen, Chao Shuai, Wei Luo, Bin Xiao, Yuanqing Li, Mingkui Tan

View a PDF of the paper titled Test-Time Learning for Large Language Models, by Jinwu Hu and 8 other authors
View PDFHTML (experimental)
Abstract:While Large Language Models (LLMs) have exhibited remarkable emergent capabilities through extensive pre-training, they still face critical limitations in generalizing to specialized domains and handling diverse linguistic variations, known as distribution shifts. In this paper, we propose a Test-Time Learning (TTL) paradigm for LLMs, namely TLM, which dynamically adapts LLMs to target domains using only unlabeled test data during testing. Specifically, we first provide empirical evidence and theoretical insights to reveal that more accurate predictions from LLMs can be achieved by minimizing the input perplexity of the unlabeled test data. Based on this insight, we formulate the Test-Time Learning process of LLMs as input perplexity minimization, enabling self-supervised enhancement of LLM performance. Furthermore, we observe that high-perplexity samples tend to be more informative for model optimization. Accordingly, we introduce a Sample Efficient Learning Strategy that actively selects and emphasizes these high-perplexity samples for test-time updates. Lastly, to mitigate catastrophic forgetting and ensure adaptation stability, we adopt Low-Rank Adaptation (LoRA) instead of full-parameter optimization, which allows lightweight model updates while preserving more original knowledge from the model. We introduce the AdaptEval benchmark for TTL and demonstrate through experiments that TLM improves performance by at least 20% compared to original LLMs on domain knowledge adaptation.
 

Comments:Accepted by ICML2025Subjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)Cite as:arXiv:2505.20633 [cs.CL](or arXiv:2505.20633v1 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2505.20633
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Jinwu Hu [view email] 
[v1]
 Tue, 27 May 2025 02:18:59 UTC (685 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Test-Time Learning for Large Language Models, by Jinwu Hu and 8 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2025-05

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

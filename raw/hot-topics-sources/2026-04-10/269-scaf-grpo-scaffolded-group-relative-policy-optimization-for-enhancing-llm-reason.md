---
title: [2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning
source_url: https://arxiv.org/abs/2510.19807
final_url: https://arxiv.org/abs/2510.19807
status: 200
content_type: text/html; charset=utf-8
topics: [GRPO (Group Relative Policy Optimization)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:01.793903+00:00
---

# [2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning

## 원본 URL

https://arxiv.org/abs/2510.19807

## 추출 본문

[2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2510.19807
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2510.19807 (cs)
 

 [Submitted on 22 Oct 2025 (v1), last revised 28 Feb 2026 (this version, v2)]

Title:Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning

Authors:Xichen Zhang, Sitong Wu, Yinghao Zhu, Haoru Tan, Shaozuo Yu, Ziyi He, Jiaya Jia

View a PDF of the paper titled Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning, by Xichen Zhang and 6 other authors
View PDFHTML (experimental)
Abstract:Reinforcement learning from verifiable rewards has emerged as a powerful technique for enhancing the complex reasoning abilities of Large Language Models (LLMs). However, these methods are fundamentally constrained by the ''learning cliff'' phenomenon: when faced with problems far beyond their current capabilities, models consistently fail, yielding a persistent zero-reward signal. In policy optimization algorithms like GRPO, this collapses the advantage calculation to zero, rendering these difficult problems invisible to the learning gradient and stalling progress. To overcome this, we introduce Scaf-GRPO (Scaffolded Group Relative Policy Optimization), a progressive training framework that strategically provides minimal guidance only when a model's independent learning has plateaued. The framework first diagnoses learning stagnation and then intervenes by injecting tiered in-prompt hints, ranging from abstract concepts to concrete steps, enabling the model to construct a valid solution by itself. Extensive experiments on challenging mathematics benchmarks demonstrate Scaf-GRPO's effectiveness, boosting the pass@1 score of the Qwen2.5-Math-7B model on the AIME24 benchmark by a relative 44.3% over a vanilla GRPO baseline. This result demonstrates our framework provides a robust and effective methodology for unlocking a model's ability to solve problems previously beyond its reach, a critical step towards extending the frontier of autonomous reasoning in LLM.
 

Comments:Code: this https URL Accepted by ICLR 2026Subjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)Cite as:arXiv:2510.19807 [cs.CL](or arXiv:2510.19807v2 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2510.19807
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Xichen Zhang [view email] 
[v1]
 Wed, 22 Oct 2025 17:41:30 UTC (1,169 KB)
[v2]
 Sat, 28 Feb 2026 08:37:14 UTC (1,219 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning, by Xichen Zhang and 6 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2025-10

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

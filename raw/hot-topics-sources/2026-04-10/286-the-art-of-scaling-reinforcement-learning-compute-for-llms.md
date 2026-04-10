---
title: [2510.13786] The Art of Scaling Reinforcement Learning Compute for LLMs
source_url: https://arxiv.org/abs/2510.13786
final_url: https://arxiv.org/abs/2510.13786
status: 200
content_type: text/html; charset=utf-8
topics: [RL Scaling Laws (ScaleRL)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.828461+00:00
---

# [2510.13786] The Art of Scaling Reinforcement Learning Compute for LLMs

## 원본 URL

https://arxiv.org/abs/2510.13786

## 추출 본문

[2510.13786] The Art of Scaling Reinforcement Learning Compute for LLMs
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2510.13786
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2510.13786 (cs)
 

 [Submitted on 15 Oct 2025]

Title:The Art of Scaling Reinforcement Learning Compute for LLMs

Authors:Devvrit Khatri, Lovish Madaan, Rishabh Tiwari, Rachit Bansal, Sai Surya Duvvuri, Manzil Zaheer, Inderjit S. Dhillon, David Brandfonbrener, Rishabh Agarwal

View a PDF of the paper titled The Art of Scaling Reinforcement Learning Compute for LLMs, by Devvrit Khatri and 8 other authors
View PDFHTML (experimental)
Abstract:Reinforcement learning (RL) has become central to training large language models (LLMs), yet the field lacks predictive scaling methodologies comparable to those established for pre-training. Despite rapidly rising compute budgets, there is no principled understanding of how to evaluate algorithmic improvements for scaling RL compute. We present the first large-scale systematic study, amounting to more than 400,000 GPU-hours, that defines a principled framework for analyzing and predicting RL scaling in LLMs. We fit sigmoidal compute-performance curves for RL training and ablate a wide range of common design choices to analyze their effects on asymptotic performance and compute efficiency. We observe: (1) Not all recipes yield similar asymptotic performance, (2) Details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote, and (3) Stable, scalable recipes follow predictable scaling trajectories, enabling extrapolation from smaller-scale runs. Combining these insights, we propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours. Our work provides both a scientific framework for analyzing scaling in RL and a practical recipe that brings RL training closer to the predictability long achieved in pre-training.
 

Comments:28 pages, 20 figuresSubjects:Machine Learning (cs.LG); Artificial Intelligence (cs.AI)Cite as:arXiv:2510.13786 [cs.LG](or arXiv:2510.13786v1 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2510.13786
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Lovish Madaan [view email] 
[v1]
 Wed, 15 Oct 2025 17:43:03 UTC (4,240 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled The Art of Scaling Reinforcement Learning Compute for LLMs, by Devvrit Khatri and 8 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2025-10

 Change to browse by:
 
cs
cs.AI

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

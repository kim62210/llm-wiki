---
title: [2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning
source_url: https://arxiv.org/abs/2501.07301
final_url: https://arxiv.org/abs/2501.07301
status: 200
content_type: text/html; charset=utf-8
topics: [Process Reward Models (PRM) 재부상]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.444185+00:00
---

# [2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning

## 원본 URL

https://arxiv.org/abs/2501.07301

## 추출 본문

[2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2501.07301
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2501.07301 (cs)
 

 [Submitted on 13 Jan 2025 (v1), last revised 5 Jun 2025 (this version, v2)]

Title:The Lessons of Developing Process Reward Models in Mathematical Reasoning

Authors:Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin

View a PDF of the paper titled The Lessons of Developing Process Reward Models in Mathematical Reasoning, by Zhenru Zhang and 8 other authors
View PDF
Abstract:Process Reward Models (PRMs) emerge as a promising approach for process supervision in mathematical reasoning of Large Language Models (LLMs), which aim to identify and mitigate intermediate errors in the reasoning processes. However, the development of effective PRMs faces significant challenges, particularly in data annotation and evaluation methodologies. In this paper, through extensive experiments, we demonstrate that commonly used Monte Carlo (MC) estimation-based data synthesis for PRMs typically yields inferior performance and generalization compared to LLM-as-a-judge and human annotation methods. MC estimation relies on completion models to evaluate current-step correctness, leading to inaccurate step verification. Furthermore, we identify potential biases in conventional Best-of-N (BoN) evaluation strategies for PRMs: (1) The unreliable policy models generate responses with correct answers but flawed processes, leading to a misalignment between the evaluation criteria of BoN and the PRM objectives of process verification. (2) The tolerance of PRMs of such responses leads to inflated BoN scores. (3) Existing PRMs have a significant proportion of minimum scores concentrated on the final answer steps, revealing the shift from process to outcome-based assessment in BoN Optimized PRMs. To address these challenges, we develop a consensus filtering mechanism that effectively integrates MC estimation with LLM-as-a-judge and advocates a more comprehensive evaluation framework that combines response-level and step-level metrics. Based on the mechanisms, we significantly improve both model performance and data efficiency in the BoN evaluation and the step-wise error identification task. Finally, we release a new state-of-the-art PRM that outperforms existing open-source alternatives and provides practical guidelines for future research in building process supervision models.
 

Subjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)Cite as:arXiv:2501.07301 [cs.CL](or arXiv:2501.07301v2 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2501.07301
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Zhenru Zhang [view email] 
[v1]
 Mon, 13 Jan 2025 13:10:16 UTC (824 KB)
[v2]
 Thu, 5 Jun 2025 16:34:24 UTC (836 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled The Lessons of Developing Process Reward Models in Mathematical Reasoning, by Zhenru Zhang and 8 other authors

View PDF

TeX Source
 

view license

 Current browse context: 
cs.CL

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

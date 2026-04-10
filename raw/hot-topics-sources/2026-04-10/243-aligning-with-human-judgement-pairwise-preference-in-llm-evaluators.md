---
title: [2403.16950] Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators
source_url: https://arxiv.org/abs/2403.16950
final_url: https://arxiv.org/abs/2403.16950
status: 200
content_type: text/html; charset=utf-8
topics: [Pairwise vs Pointwise Eval Protocol Bias]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:00.003711+00:00
---

# [2403.16950] Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators

## 원본 URL

https://arxiv.org/abs/2403.16950

## 추출 본문

[2403.16950] Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators
Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2403.16950
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2403.16950 (cs)
 

 [Submitted on 25 Mar 2024 (v1), last revised 17 Jan 2025 (this version, v5)]

Title:Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators

Authors:Yinhong Liu, Han Zhou, Zhijiang Guo, Ehsan Shareghi, Ivan Vulić, Anna Korhonen, Nigel Collier

View a PDF of the paper titled Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators, by Yinhong Liu and 5 other authors
View PDFHTML (experimental)
Abstract:Large Language Models (LLMs) have demonstrated promising capabilities as automatic evaluators in assessing the quality of generated natural language. However, LLMs still exhibit biases in evaluation and often struggle to generate coherent evaluations that align with human assessments. In this work, we first conduct a systematic study of the misalignment between LLM evaluators and human evaluation, revealing that existing calibration methods aimed at mitigating biases of LLMs are insufficient for effectively aligning LLM evaluators. Inspired by the use of preference data in RLHF, we formulate the evaluation as a ranking problem and introduce Pairwise-preference Search (PAIRS), an uncertainty-guided search-based rank aggregation method that employs LLMs to conduct pairwise comparisons locally and efficiently ranks candidate texts globally. PAIRS achieves state-of-the-art performance on representative evaluation tasks in long-form generations and demonstrates significant improvements over direct scoring. Furthermore, we provide insights into the role of pairwise preference in quantifying the transitivity of LLMs and demonstrate how PAIRS benefits from calibration using debiased pairwise evaluations.
 

Comments:This paper has been accepted by COLM 2024Subjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)Cite as:arXiv:2403.16950 [cs.CL](or arXiv:2403.16950v5 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2403.16950
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Yinhong Liu [view email] 
[v1]
 Mon, 25 Mar 2024 17:11:28 UTC (3,373 KB)
[v2]
 Tue, 26 Mar 2024 02:28:42 UTC (3,373 KB)
[v3]
 Sat, 10 Aug 2024 15:42:51 UTC (1,266 KB)
[v4]
 Wed, 8 Jan 2025 03:14:04 UTC (1,282 KB)
[v5]
 Fri, 17 Jan 2025 03:43:53 UTC (1,282 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators, by Yinhong Liu and 5 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2024-03

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

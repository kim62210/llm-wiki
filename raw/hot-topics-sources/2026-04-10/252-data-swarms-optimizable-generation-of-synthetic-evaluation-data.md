---
title: [2506.00741] Data Swarms: Optimizable Generation of Synthetic Evaluation Data
source_url: https://arxiv.org/abs/2506.00741
final_url: https://arxiv.org/abs/2506.00741
status: 200
content_type: text/html; charset=utf-8
topics: [Synthetic Eval Data Generation]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:00.603052+00:00
---

# [2506.00741] Data Swarms: Optimizable Generation of Synthetic Evaluation Data

## 원본 URL

https://arxiv.org/abs/2506.00741

## 추출 본문

[2506.00741] Data Swarms: Optimizable Generation of Synthetic Evaluation Data
Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2506.00741
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2506.00741 (cs)
 

 [Submitted on 31 May 2025 (v1), last revised 6 Jun 2025 (this version, v2)]

Title:Data Swarms: Optimizable Generation of Synthetic Evaluation Data

Authors:Shangbin Feng, Yike Wang, Weijia Shi, Yulia Tsvetkov

View a PDF of the paper titled Data Swarms: Optimizable Generation of Synthetic Evaluation Data, by Shangbin Feng and 3 other authors
View PDFHTML (experimental)
Abstract:We propose Data Swarms, an algorithm to optimize the generation of synthetic evaluation data and advance quantitative desiderata of LLM evaluation. We first train a swarm of initial data generators using existing data, and define various evaluation objectives to reflect the desired properties of evaluation (e.g., generate more difficult problems for the evaluated models) and quantitatively evaluate data generators. We then employ particle swarm optimization to optimize the swarm of data generators, where they collaboratively search through the model parameter space to find new generators that advance these objectives. We further extend it to Adversarial Swarms, where the data generator swarm generates harder data while the test taker model swarm learns from such data, co-evolving dynamically for better data and models simultaneously. Extensive experiments demonstrate that Data Swarms outperforms eight data generation baselines across five evaluation objectives, while Adversarial Swarms produce more robust learning of synthetic data and stronger generalization. Further analysis reveals that Data Swarms successfully optimizes compositions of multiple evaluation objectives and generalizes to new off-the-shelf LLMs, unseen at optimization time.
 

Subjects:Computation and Language (cs.CL)Cite as:arXiv:2506.00741 [cs.CL](or arXiv:2506.00741v2 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2506.00741
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Shangbin Feng [view email] 
[v1]
 Sat, 31 May 2025 23:03:46 UTC (520 KB)
[v2]
 Fri, 6 Jun 2025 02:20:24 UTC (520 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Data Swarms: Optimizable Generation of Synthetic Evaluation Data, by Shangbin Feng and 3 other authors

View PDF

HTML (experimental)

TeX Source

Other Formats

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2025-06

 Change to browse by:
 
cs

References & Citations

NASA ADS

Google Scholar

Semantic Scholar

aexport BibTeX citationLoading...

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

 Get status notifications via
 email
 or slack

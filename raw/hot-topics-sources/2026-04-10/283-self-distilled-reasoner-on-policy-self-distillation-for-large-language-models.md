---
title: [2601.18734] Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models
source_url: https://arxiv.org/abs/2601.18734
final_url: https://arxiv.org/abs/2601.18734
status: 200
content_type: text/html; charset=utf-8
topics: [On-Policy Distillation]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.682455+00:00
---

# [2601.18734] Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models

## 원본 URL

https://arxiv.org/abs/2601.18734

## 추출 본문

[2601.18734] Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2601.18734
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2601.18734 (cs)
 

 [Submitted on 26 Jan 2026 (v1), last revised 20 Mar 2026 (this version, v3)]

Title:Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models

Authors:Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, Aditya Grover

View a PDF of the paper titled Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models, by Siyan Zhao and 6 other authors
View PDFHTML (experimental)
Abstract:Knowledge distillation improves large language model (LLM) reasoning by compressing the knowledge of a teacher LLM to train smaller LLMs. On-policy distillation advances this approach by having the student sample its own trajectories while a teacher LLM provides dense token-level supervision, addressing the distribution mismatch between training and inference in off-policy distillation methods. However, on-policy distillation typically requires a separate, often larger, teacher LLM and does not explicitly leverage ground-truth solutions available in reasoning datasets. Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self, we introduce On-Policy Self-Distillation (OPSD), a learning algorithm where a single LLM acts as both teacher and student with different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student's own rollouts. We demonstrate the efficacy of our method on multiple mathematical reasoning benchmarks, achieving superior token efficiency compared to reinforcement learning methods and better performance over off-policy distillation methods. Code repo: this https URL.
 

Comments:code is released here: this https URLSubjects:Machine Learning (cs.LG); Computation and Language (cs.CL)Cite as:arXiv:2601.18734 [cs.LG](or arXiv:2601.18734v3 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2601.18734
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Siyan Zhao [view email] 
[v1]
 Mon, 26 Jan 2026 17:56:50 UTC (265 KB)
[v2]
 Thu, 5 Mar 2026 18:19:57 UTC (282 KB)
[v3]
 Fri, 20 Mar 2026 15:40:19 UTC (268 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models, by Siyan Zhao and 6 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2026-01

 Change to browse by:
 
cs
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

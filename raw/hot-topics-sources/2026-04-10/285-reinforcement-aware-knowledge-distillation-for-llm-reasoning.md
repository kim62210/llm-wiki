---
title: [2602.22495] Reinforcement-aware Knowledge Distillation for LLM Reasoning
source_url: https://arxiv.org/abs/2602.22495
final_url: https://arxiv.org/abs/2602.22495
status: 200
content_type: text/html; charset=utf-8
topics: [On-Policy Distillation]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.831796+00:00
---

# [2602.22495] Reinforcement-aware Knowledge Distillation for LLM Reasoning

## 원본 URL

https://arxiv.org/abs/2602.22495

## 추출 본문

[2602.22495] Reinforcement-aware Knowledge Distillation for LLM Reasoning
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2602.22495
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2602.22495 (cs)
 

 [Submitted on 26 Feb 2026]

Title:Reinforcement-aware Knowledge Distillation for LLM Reasoning

Authors:Zhaoyang Zhang, Shuli Jiang, Yantao Shen, Yuting Zhang, Dhananjay Ram, Shuo Yang, Zhuowen Tu, Wei Xia, Stefano Soatto

View a PDF of the paper titled Reinforcement-aware Knowledge Distillation for LLM Reasoning, by Zhaoyang Zhang and 8 other authors
View PDFHTML (experimental)
Abstract:Reinforcement learning (RL) post-training has recently driven major gains in long chain-of-thought reasoning large language models (LLMs), but the high inference cost of such models motivates distillation into smaller students. Most existing knowledge distillation (KD) methods are designed for supervised fine-tuning (SFT), relying on fixed teacher traces or teacher-student Kullback-Leibler (KL) divergence-based regularization. When combined with RL, these approaches often suffer from distribution mismatch and objective interference: teacher supervision may not align with the student's evolving rollout distribution, and the KL regularizer can compete with reward maximization and require careful loss balancing. To address these issues, we propose RL-aware distillation (RLAD), which performs selective imitation during RL -- guiding the student toward the teacher only when it improves the current policy update. Our core component, Trust Region Ratio Distillation (TRRD), replaces the teacher-student KL regularizer with a PPO/GRPO-style likelihood-ratio objective anchored to a teacher--old-policy mixture, yielding advantage-aware, trust-region-bounded distillation on student rollouts and naturally balancing exploration, exploitation, and imitation. Across diverse logic reasoning and math benchmarks, RLAD consistently outperforms offline distillation, standard GRPO, and KL-based on-policy teacher-student knowledge distillation.
 

Subjects:Machine Learning (cs.LG); Artificial Intelligence (cs.AI)Cite as:arXiv:2602.22495 [cs.LG](or arXiv:2602.22495v1 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2602.22495
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Zhaoyang Zhang [view email] 
[v1]
 Thu, 26 Feb 2026 00:20:39 UTC (115 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Reinforcement-aware Knowledge Distillation for LLM Reasoning, by Zhaoyang Zhang and 8 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2026-02

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

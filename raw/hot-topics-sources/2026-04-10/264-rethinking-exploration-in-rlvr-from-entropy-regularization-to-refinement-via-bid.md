---
title: [2604.04894] Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation
source_url: https://arxiv.org/abs/2604.04894
final_url: https://arxiv.org/abs/2604.04894
status: 200
content_type: text/html; charset=utf-8
topics: [RLVR (Reinforcement Learning with Verifiable Rewards)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:01.274245+00:00
---

# [2604.04894] Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation

## 원본 URL

https://arxiv.org/abs/2604.04894

## 추출 본문

[2604.04894] Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2604.04894
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2604.04894 (cs)
 

 [Submitted on 6 Apr 2026]

Title:Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation

Authors:Hengrui Gu, Xiaotian Han, Yujing Bian, Kaixiong Zhou

View a PDF of the paper titled Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation, by Hengrui Gu and 3 other authors
View PDFHTML (experimental)
Abstract:Reinforcement learning with verifiable rewards (RLVR) has significantly advanced the reasoning capabilities of large language models (LLMs). However, it faces a fundamental limitation termed \textit{restricted exploration}, where the policy rapidly converges to a narrow set of solutions. While entropy regularization is a popular approach used to sustain exploration, it often proves unreliable for LLMs, suffering from high hyperparameter sensitivity and yielding only marginal performance gains. Motivated by these inefficiencies, we propose to rethink the relationship between policy entropy and exploration. By deriving a parametric formulation of group-relative advantage estimation and analyzing entropy dynamics, we conceptually decompose policy entropy into \textit{informative entropy}, which preserves diverse solution paths, and \textit{spurious entropy}, which erodes reasoning patterns. Our analysis reveals that, in contrast to blind maximization, effective exploration requires \textit{entropy refinement}-a mechanism implicitly embedded in group-relative advantage estimation that sustains informative entropy on positive rollouts while suppressing spurious entropy on negative ones. Guided by this insight, we propose \textbf{AsymGRPO}, an exploratory framework that explicitly decouples the modulation of positive and negative rollouts. This allows for independent control over the preservation of informative entropy and the suppression of spurious noise. Extensive experiments demonstrate that AsymGRPO achieves superior performance compared to strong baselines and exhibits the potential to synergize with existing entropy regularization methods.
 

Subjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)Cite as:arXiv:2604.04894 [cs.CL](or arXiv:2604.04894v1 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2604.04894
Focus to learn more
 arXiv-issued DOI via DataCite (pending registration)

Submission history
 From: Hengrui Gu [view email] 
[v1]
 Mon, 6 Apr 2026 17:42:38 UTC (524 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation, by Hengrui Gu and 3 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2026-04

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

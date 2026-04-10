---
title: [2506.11442] ReVeal: Self-Evolving Code Agents via Reliable Self-Verification
source_url: https://arxiv.org/abs/2506.11442
final_url: https://arxiv.org/abs/2506.11442
status: 200
content_type: text/html; charset=utf-8
topics: [Generator-Evaluator Harness Architecture, Long-Horizon RL Training for Agents (Multi-Turn RLVR)]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:26.845523+00:00
---

# [2506.11442] ReVeal: Self-Evolving Code Agents via Reliable Self-Verification

## 원본 URL

https://arxiv.org/abs/2506.11442

## 추출 본문

[2506.11442] ReVeal: Self-Evolving Code Agents via Reliable Self-Verification
Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2506.11442
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Software Engineering

arXiv:2506.11442 (cs)
 

 [Submitted on 13 Jun 2025 (v1), last revised 21 Oct 2025 (this version, v2)]

Title:ReVeal: Self-Evolving Code Agents via Reliable Self-Verification

Authors:Yiyang Jin, Kunzhao Xu, Hang Li, Xueting Han, Yanmin Zhou, Cheng Li, Jing Bai

View a PDF of the paper titled ReVeal: Self-Evolving Code Agents via Reliable Self-Verification, by Yiyang Jin and 6 other authors
View PDF
Abstract:Reinforcement learning with verifiable rewards (RLVR) has advanced the reasoning capabilities of large language models. However, existing methods rely solely on outcome rewards, without explicitly optimizing verification or leveraging reliable signals from realistic environments, leading to unreliable self-verification and limited test-time scaling. To address this, we widen the verification-generation asymmetry by explicitly optimizing self-verification, making it a reliable driver of deeper test-time scaling. We introduce ReVeal, a multi-turn reinforcement learning framework that evolves code generation through self-verification and tool-based evaluation. ReVeal structures long-horizon reasoning as iterative generation-verification turns and incorporates TAPO for turn-level credit assignment, fostering the co-evolution of code and test generation. At inference, this strengthened self-verification enables the model to use self-constructed tests and tool feedback to continuously evolve code for 20+ turns on LiveCodeBench despite training on only three. It also significantly improves Pass@k, indicating stronger exploration that expands the reasoning boundaries of the base model. These findings highlight the promise of ReVeal as a scalable paradigm for RL training and test-time scaling, paving the way for more robust and autonomous AI agents.
 

Subjects:Software Engineering (cs.SE); Machine Learning (cs.LG)Cite as:arXiv:2506.11442 [cs.SE](or arXiv:2506.11442v2 [cs.SE] for this version)
 https://doi.org/10.48550/arXiv.2506.11442
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Xueting Han [view email] 
[v1]
 Fri, 13 Jun 2025 03:41:04 UTC (1,071 KB)
[v2]
 Tue, 21 Oct 2025 12:49:25 UTC (2,248 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled ReVeal: Self-Evolving Code Agents via Reliable Self-Verification, by Yiyang Jin and 6 other authors

View PDF

TeX Source
 

view license

 Current browse context: 
cs.SE

< prev  |  next >

new | recent | 2025-06

 Change to browse by:
 
cs
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

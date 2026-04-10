---
title: [2503.09572] Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks
source_url: https://arxiv.org/abs/2503.09572
final_url: https://arxiv.org/abs/2503.09572
status: 200
content_type: text/html; charset=utf-8
topics: [Hierarchical Planning with Agent Trees]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:28.655672+00:00
---

# [2503.09572] Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks

## 원본 URL

https://arxiv.org/abs/2503.09572

## 추출 본문

[2503.09572] Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2503.09572
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2503.09572 (cs)
 

 [Submitted on 12 Mar 2025 (v1), last revised 22 Apr 2025 (this version, v3)]

Title:Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks

Authors:Lutfi Eren Erdogan, Nicholas Lee, Sehoon Kim, Suhong Moon, Hiroki Furuta, Gopala Anumanchipalli, Kurt Keutzer, Amir Gholami

View a PDF of the paper titled Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks, by Lutfi Eren Erdogan and 7 other authors
View PDFHTML (experimental)
Abstract:Large language models (LLMs) have shown remarkable advancements in enabling language agents to tackle simple tasks. However, applying them for complex, multi-step, long-horizon tasks remains a challenge. Recent work have found success by separating high-level planning from low-level execution, which enables the model to effectively balance high-level planning objectives and low-level execution details. However, generating accurate plans remains difficult since LLMs are not inherently trained for this task. To address this, we propose Plan-and-Act, a novel framework that incorporates explicit planning into LLM-based agents and introduces a scalable method to enhance plan generation through a novel synthetic data generation method. Plan-and-Act consists of a Planner model which generates structured, high-level plans to achieve user goals, and an Executor model that translates these plans into environment-specific actions. To train the Planner effectively, we introduce a synthetic data generation method that annotates ground-truth trajectories with feasible plans, augmented with diverse and extensive examples to enhance generalization. We evaluate Plan-and-Act using web navigation as a representative long-horizon planning environment, demonstrating a state-of-the-art 57.58% success rate on the WebArena-Lite benchmark as well as a text-only state-of-the-art 81.36% success rate on WebVoyager.
 

Subjects:Computation and Language (cs.CL)Cite as:arXiv:2503.09572 [cs.CL](or arXiv:2503.09572v3 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2503.09572
Focus to learn more
 arXiv-issued DOI via DataCite

Journal reference:ICML 2025

Submission history
 From: Nicholas Lee [view email] 
[v1]
 Wed, 12 Mar 2025 17:40:52 UTC (285 KB)
[v2]
 Mon, 24 Mar 2025 23:48:07 UTC (520 KB)
[v3]
 Tue, 22 Apr 2025 17:56:22 UTC (527 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks, by Lutfi Eren Erdogan and 7 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2025-03

 Change to browse by:
 
cs

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

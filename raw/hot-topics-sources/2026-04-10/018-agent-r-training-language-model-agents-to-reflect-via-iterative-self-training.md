---
title: [2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
source_url: https://arxiv.org/abs/2501.11425
final_url: https://arxiv.org/abs/2501.11425
status: 200
content_type: text/html; charset=utf-8
topics: [Agent Memory Systems (Episodic / Semantic / Working)]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:26.696079+00:00
---

# [2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training

## 원본 URL

https://arxiv.org/abs/2501.11425

## 추출 본문

[2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
Skip to main content

In just 5 minutes help us improve arXiv:
Annual Global Survey

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2501.11425
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Artificial Intelligence

arXiv:2501.11425 (cs)
 

 [Submitted on 20 Jan 2025 (v1), last revised 24 Mar 2025 (this version, v3)]

Title:Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training

Authors:Siyu Yuan, Zehui Chen, Zhiheng Xi, Junjie Ye, Zhengyin Du, Jiecao Chen

View a PDF of the paper titled Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training, by Siyu Yuan and 5 other authors
View PDFHTML (experimental)
Abstract:Large Language Models (LLMs) agents are increasingly pivotal for addressing complex tasks in interactive environments. Existing work mainly focuses on enhancing performance through behavior cloning from stronger experts, yet such approaches often falter in real-world applications, mainly due to the inability to recover from errors. However, step-level critique data is difficult and expensive to collect. Automating and dynamically constructing self-critique datasets is thus crucial to empowering models with intelligent agent capabilities. In this work, we propose an iterative self-training framework, Agent-R, that enables language Agent to Reflect on the fly. Unlike traditional methods that reward or penalize actions based on correctness, Agent-R leverages MCTS to construct training data that recover correct trajectories from erroneous ones. A key challenge of agent reflection lies in the necessity for timely revision rather than waiting until the end of a rollout. To address this, we introduce a model-guided critique construction mechanism: the actor model identifies the first error step (within its current capability) in a failed trajectory. Starting from it, we splice it with the adjacent correct path, which shares the same parent node in the tree. This strategy enables the model to learn reflection based on its current policy, therefore yielding better learning efficiency. To further explore the scalability of this self-improvement paradigm, we investigate iterative refinement of both error correction capabilities and dataset construction. Our findings demonstrate that Agent-R continuously improves the model's ability to recover from errors and enables timely error correction. Experiments on three interactive environments show that Agent-R effectively equips agents to correct erroneous actions while avoiding loops, achieving superior performance compared to baseline methods (+5.59%).
 

Subjects:Artificial Intelligence (cs.AI)Cite as:arXiv:2501.11425 [cs.AI](or arXiv:2501.11425v3 [cs.AI] for this version)
 https://doi.org/10.48550/arXiv.2501.11425
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Siyu Yuan [view email] 
[v1]
 Mon, 20 Jan 2025 11:46:04 UTC (3,940 KB)
[v2]
 Wed, 19 Mar 2025 09:28:09 UTC (4,085 KB)
[v3]
 Mon, 24 Mar 2025 10:18:56 UTC (4,086 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training, by Siyu Yuan and 5 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.AI

< prev  |  next >

new | recent | 2025-01

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

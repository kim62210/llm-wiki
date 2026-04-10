---
title: [2502.01600] Reinforcement Learning for Long-Horizon Interactive LLM Agents
source_url: https://arxiv.org/abs/2502.01600
final_url: https://arxiv.org/abs/2502.01600
status: 200
content_type: text/html; charset=utf-8
topics: [Long-Horizon RL Training for Agents (Multi-Turn RLVR)]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:28.371413+00:00
---

# [2502.01600] Reinforcement Learning for Long-Horizon Interactive LLM Agents

## 원본 URL

https://arxiv.org/abs/2502.01600

## 추출 본문

[2502.01600] Reinforcement Learning for Long-Horizon Interactive LLM Agents
Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2502.01600
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2502.01600 (cs)
 

 [Submitted on 3 Feb 2025 (v1), last revised 8 Mar 2025 (this version, v3)]

Title:Reinforcement Learning for Long-Horizon Interactive LLM Agents

Authors:Kevin Chen, Marco Cusumano-Towner, Brody Huval, Aleksei Petrenko, Jackson Hamburger, Vladlen Koltun, Philipp Krähenbühl

View a PDF of the paper titled Reinforcement Learning for Long-Horizon Interactive LLM Agents, by Kevin Chen and 6 other authors
View PDF
Abstract:Interactive digital agents (IDAs) leverage APIs of stateful digital environments to perform tasks in response to user requests. While IDAs powered by instruction-tuned large language models (LLMs) can react to feedback from interface invocations in multi-step exchanges, they have not been trained in their respective digital environments. Prior methods accomplish less than half of tasks in sophisticated benchmarks such as AppWorld. We present a reinforcement learning (RL) approach that trains IDAs directly in their target environments. We formalize this training as a partially observable Markov decision process and derive LOOP, a data- and memory-efficient variant of proximal policy optimization. LOOP uses no value network and maintains exactly one copy of the underlying LLM in memory, making its implementation straightforward and as memory-efficient as fine-tuning a single LLM. A 32-billion-parameter agent trained with LOOP in the AppWorld environment outperforms the much larger OpenAI o1 agent by 9 percentage points (15% relative). To our knowledge, this is the first reported application of RL to IDAs that interact with a stateful, multi-domain, multi-app environment via direct API calls. Our analysis sheds light on the effectiveness of RL in this area, showing that the agent learns to consult the API documentation, avoid unwarranted assumptions, minimize confabulation, and recover from setbacks.
 

Subjects:Machine Learning (cs.LG); Artificial Intelligence (cs.AI)Cite as:arXiv:2502.01600 [cs.LG](or arXiv:2502.01600v3 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2502.01600
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Philipp Krähenbühl [view email] 
[v1]
 Mon, 3 Feb 2025 18:35:42 UTC (657 KB)
[v2]
 Tue, 4 Feb 2025 14:28:50 UTC (657 KB)
[v3]
 Sat, 8 Mar 2025 05:23:57 UTC (660 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Reinforcement Learning for Long-Horizon Interactive LLM Agents, by Kevin Chen and 6 other authors

View PDF

TeX Source

Other Formats

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2025-02

 Change to browse by:
 
cs
cs.AI

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

 Get status notifications via
 email
 or slack

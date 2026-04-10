---
title: [2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning
source_url: https://arxiv.org/abs/2511.02424
final_url: https://arxiv.org/abs/2511.02424
status: 200
content_type: text/html; charset=utf-8
topics: [Hierarchical Planning with Agent Trees]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:28.581859+00:00
---

# [2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

## 원본 URL

https://arxiv.org/abs/2511.02424

## 추출 본문

[2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2511.02424
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Artificial Intelligence

arXiv:2511.02424 (cs)
 

 [Submitted on 4 Nov 2025 (v1), last revised 10 Feb 2026 (this version, v2)]

Title:ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

Authors:Jae-Woo Choi, Hyungmin Kim, Hyobin Ong, Youngwoo Yoon, Minsu Jang, Dohyung Kim, Jaehong Kim

View a PDF of the paper titled ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning, by Jae-Woo Choi and 6 other authors
View PDFHTML (experimental)
Abstract:Recent advancements in large language models (LLMs) have enabled significant progress in decision-making and task planning for embodied autonomous agents. However, most existing methods struggle with complex, long-horizon tasks because they rely on a monolithic trajectory that entangles all past decisions and observations to solve the entire task in a single unified process. To address this limitation, we propose ReAcTree, a hierarchical task-planning method that decomposes a complex goal into manageable subgoals within a dynamically constructed agent tree. Each subgoal is handled by an LLM agent node capable of reasoning, acting, and further expanding the tree, while control flow nodes coordinate the execution strategies of agent nodes. In addition, we integrate two complementary memory systems: each agent node retrieves goal-specific, subgoal-level examples from episodic memory and shares environment-specific observations through working memory. Experiments on the WAH-NL and ALFRED show ReAcTree consistently outperforms strong task-planning baselines such as ReAct across diverse LLMs. Notably, on WAH-NL, ReAcTree achieves a 61% goal success rate with Qwen 2.5 72B, nearly doubling ReAct's 31%. The code is available at this https URL.
 

Comments:Accepted as a Full Paper at AAMAS 2026. This is the extended version including full appendices. Code is available at this https URLSubjects:Artificial Intelligence (cs.AI)Cite as:arXiv:2511.02424 [cs.AI](or arXiv:2511.02424v2 [cs.AI] for this version)
 https://doi.org/10.48550/arXiv.2511.02424
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Jae-Woo Choi [view email] 
[v1]
 Tue, 4 Nov 2025 09:55:40 UTC (20,065 KB)
[v2]
 Tue, 10 Feb 2026 04:31:05 UTC (20,066 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning, by Jae-Woo Choi and 6 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.AI

< prev  |  next >

new | recent | 2025-11

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

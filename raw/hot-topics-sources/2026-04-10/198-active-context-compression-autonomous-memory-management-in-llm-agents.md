---
title: [2601.07190] Active Context Compression: Autonomous Memory Management in LLM Agents
source_url: https://arxiv.org/abs/2601.07190
final_url: https://arxiv.org/abs/2601.07190
status: 200
content_type: text/html; charset=utf-8
topics: [Adaptive Context Compression for Long-Running Agents]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:52.939655+00:00
---

# [2601.07190] Active Context Compression: Autonomous Memory Management in LLM Agents

## 원본 URL

https://arxiv.org/abs/2601.07190

## 추출 본문

[2601.07190] Active Context Compression: Autonomous Memory Management in LLM Agents
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2601.07190
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Artificial Intelligence

arXiv:2601.07190 (cs)
 

 [Submitted on 12 Jan 2026]

Title:Active Context Compression: Autonomous Memory Management in LLM Agents

Authors:Nikhil Verma

View a PDF of the paper titled Active Context Compression: Autonomous Memory Management in LLM Agents, by Nikhil Verma
View PDFHTML (experimental)
Abstract:Large Language Model (LLM) agents struggle with long-horizon software engineering tasks due to "Context Bloat." As interaction history grows, computational costs explode, latency increases, and reasoning capabilities degrade due to distraction by irrelevant past errors. Existing solutions often rely on passive, external summarization mechanisms that the agent cannot control. This paper proposes Focus, an agent-centric architecture inspired by the biological exploration strategies of Physarum polycephalum (slime mold). The Focus Agent autonomously decides when to consolidate key learnings into a persistent "Knowledge" block and actively withdraws (prunes) the raw interaction history. Using an optimized scaffold matching industry best practices (persistent bash + string-replacement editor), we evaluated Focus on N=5 context-intensive instances from SWE-bench Lite using Claude Haiku 4.5. With aggressive prompting that encourages frequent compression, Focus achieves 22.7% token reduction (14.9M -> 11.5M tokens) while maintaining identical accuracy (3/5 = 60% for both agents). Focus performed 6.0 autonomous compressions per task on average, with token savings up to 57% on individual instances. We demonstrate that capable models can autonomously self-regulate their context when given appropriate tools and prompting, opening pathways for cost-aware agentic systems without sacrificing task performance.
 

Comments:8 pages, 2 figures, 2 tables. IEEE conference formatSubjects:Artificial Intelligence (cs.AI)ACM classes:I.2.7; I.2.2Cite as:arXiv:2601.07190 [cs.AI](or arXiv:2601.07190v1 [cs.AI] for this version)
 https://doi.org/10.48550/arXiv.2601.07190
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Nikhil Verma [view email] 
[v1]
 Mon, 12 Jan 2026 04:31:00 UTC (241 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Active Context Compression: Autonomous Memory Management in LLM Agents, by Nikhil Verma

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.AI

< prev  |  next >

new | recent | 2026-01

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

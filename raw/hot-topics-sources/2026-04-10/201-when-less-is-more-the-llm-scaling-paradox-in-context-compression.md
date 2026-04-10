---
title: [2602.09789] When Less is More: The LLM Scaling Paradox in Context Compression
source_url: https://arxiv.org/abs/2602.09789
final_url: https://arxiv.org/abs/2602.09789
status: 200
content_type: text/html; charset=utf-8
topics: [Adaptive Context Compression for Long-Running Agents]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:53.130913+00:00
---

# [2602.09789] When Less is More: The LLM Scaling Paradox in Context Compression

## 원본 URL

https://arxiv.org/abs/2602.09789

## 추출 본문

[2602.09789] When Less is More: The LLM Scaling Paradox in Context Compression
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2602.09789
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2602.09789 (cs)
 

 [Submitted on 10 Feb 2026 (v1), last revised 26 Feb 2026 (this version, v2)]

Title:When Less is More: The LLM Scaling Paradox in Context Compression

Authors:Ruishan Guo, Yibing Liu, Guoxin Ma, Yan Wang, Yueyang Zhang, Long Xia, Kecheng Chen, Zhiyuan Sun, Daiting Shi

View a PDF of the paper titled When Less is More: The LLM Scaling Paradox in Context Compression, by Ruishan Guo and 8 other authors
View PDFHTML (experimental)
Abstract:Scaling up model parameters has long been a prevalent training paradigm driven by the assumption that larger models yield superior generation capabilities. However, under lossy context compression in a compressor-decoder setup, we observe a Size-Fidelity Paradox: increasing the compressor size can lessen the faithfulness of reconstructed contexts though training loss decreases. Through extensive experiments across models from 0.6B to 90B, we coin this paradox arising from two dominant factors: 1) knowledge overwriting: larger models increasingly replace source facts with their own prior beliefs, e.g., ``the white strawberry'' $\to$ ``the red strawberry''; and 2) semantic drift: larger models tend to paraphrase or restructure content instead of reproducing it verbatim, e.g., ``Alice hit Bob'' $\to$ ``Bob hit Alice''. By holding model size fixed, we reflect on the emergent properties of compressed context representations. We show that the culprit is not parameter count itself, but the excessive semantic capacity and amplified generative uncertainty that accompany scaling. Specifically, the increased rank of context embeddings facilitates prior knowledge intrusion, whereas higher entropy over token prediction distributions promotes rewriting. Our results complement existing evaluations over context compression paradigm, underpinning a breakdown in scaling laws for faithful preservation in open-ended generation.
 

Comments:10 pages, 4 figures, conferenceSubjects:Machine Learning (cs.LG)Cite as:arXiv:2602.09789 [cs.LG](or arXiv:2602.09789v2 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2602.09789
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Ruishan Guo [view email] 
[v1]
 Tue, 10 Feb 2026 13:49:08 UTC (1,438 KB)
[v2]
 Thu, 26 Feb 2026 07:55:28 UTC (1,440 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled When Less is More: The LLM Scaling Paradox in Context Compression, by Ruishan Guo and 8 other authors

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

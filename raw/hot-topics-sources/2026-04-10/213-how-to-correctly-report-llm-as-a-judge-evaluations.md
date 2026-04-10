---
title: [2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations
source_url: https://arxiv.org/abs/2511.21140
final_url: https://arxiv.org/abs/2511.21140
status: 200
content_type: text/html; charset=utf-8
topics: [LLM-as-Judge Calibration & Reliability]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:55.738463+00:00
---

# [2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations

## 원본 URL

https://arxiv.org/abs/2511.21140

## 추출 본문

[2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2511.21140
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2511.21140 (cs)
 

 [Submitted on 26 Nov 2025 (v1), last revised 9 Feb 2026 (this version, v3)]

Title:How to Correctly Report LLM-as-a-Judge Evaluations

Authors:Chungpa Lee, Thomas Zeng, Jongwon Jeong, Jy-yong Sohn, Kangwook Lee

View a PDF of the paper titled How to Correctly Report LLM-as-a-Judge Evaluations, by Chungpa Lee and 4 other authors
View PDFHTML (experimental)
Abstract:Large language models (LLMs) are widely used as scalable evaluators of model responses in lieu of human annotators. However, imperfect sensitivity and specificity of the LLM judges induce bias in naive evaluation scores. We propose a simple plug-in framework that corrects this bias and enables statistically principled uncertainty quantification. Our framework constructs confidence intervals that account for uncertainty from both the test dataset and a human-labeled calibration dataset. Additionally, it uses an adaptive strategy to allocate calibration samples for tighter intervals. Importantly, we characterize parameter regimes defined by the true evaluation score and the LLM judge's sensitivity and specificity in which our LLM-based evaluation yields more reliable estimates than human-only evaluation. Moreover, we show that our framework remains unbiased under distribution shift between the test and calibration datasets, in contrast to existing approaches.
 

Comments:Refined the writing of the manuscriptSubjects:Machine Learning (cs.LG); Computation and Language (cs.CL); Applications (stat.AP); Machine Learning (stat.ML)Cite as:arXiv:2511.21140 [cs.LG](or arXiv:2511.21140v3 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2511.21140
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Chungpa Lee [view email] 
[v1]
 Wed, 26 Nov 2025 07:46:46 UTC (396 KB)
[v2]
 Sun, 4 Jan 2026 07:18:14 UTC (313 KB)
[v3]
 Mon, 9 Feb 2026 07:36:38 UTC (315 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled How to Correctly Report LLM-as-a-Judge Evaluations, by Chungpa Lee and 4 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2025-11

 Change to browse by:
 
cs
cs.CL
stat
stat.AP
stat.ML

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

---
title: [2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation
source_url: https://arxiv.org/abs/2504.14716
final_url: https://arxiv.org/abs/2504.14716
status: 200
content_type: text/html; charset=utf-8
topics: [Pairwise vs Pointwise Eval Protocol Bias]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:59.761495+00:00
---

# [2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation

## 원본 URL

https://arxiv.org/abs/2504.14716

## 추출 본문

[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2504.14716
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2504.14716 (cs)
 

 [Submitted on 20 Apr 2025 (v1), last revised 21 Aug 2025 (this version, v2)]

Title:Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation

Authors:Tuhina Tripathi, Manya Wadhwa, Greg Durrett, Scott Niekum

View a PDF of the paper titled Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation, by Tuhina Tripathi and 3 other authors
View PDF
Abstract:Large Language Models (LLMs) are widely used as proxies for human labelers in both training (Reinforcement Learning from AI Feedback) and large-scale response evaluation (LLM-as-a-judge). Alignment and evaluation are critical components in the development of reliable LLMs, and the choice of feedback protocol plays a central role in both but remains understudied. In this work, we show that the choice of feedback protocol for evaluation (absolute scores versus relative preferences) can significantly affect evaluation reliability and induce systematic biases. In the context of LLM-as-a-judge evaluation, we show that pairwise protocols are more vulnerable to distracted evaluation. Generator models can exploit spurious attributes (or distractor features) favored by the LLM judge, resulting in inflated scores for lower-quality outputs. We find that absolute scoring is more robust to such manipulation, producing judgments that better reflect response quality and are less influenced by distractor features. Our results demonstrate that generator models can flip preferences by embedding distractor features, skewing LLM-as-a-judge comparisons and leading to inaccurate conclusions about model quality in benchmark evaluations. Pairwise preferences flip in about 35% of the cases, compared to only 9% for absolute scores. We offer recommendations for choosing feedback protocols based on dataset characteristics and evaluation objectives.
 

Comments:Published at COLM 2025Subjects:Machine Learning (cs.LG)Cite as:arXiv:2504.14716 [cs.LG](or arXiv:2504.14716v2 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2504.14716
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Tuhina Tripathi [view email] 
[v1]
 Sun, 20 Apr 2025 19:05:59 UTC (2,560 KB)
[v2]
 Thu, 21 Aug 2025 15:48:03 UTC (334 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation, by Tuhina Tripathi and 3 other authors

View PDF

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2025-04

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

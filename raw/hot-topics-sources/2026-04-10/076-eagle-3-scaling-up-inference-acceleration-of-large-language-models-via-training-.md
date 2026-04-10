---
title: [2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test
source_url: https://arxiv.org/abs/2503.01840
final_url: https://arxiv.org/abs/2503.01840
status: 200
content_type: text/html; charset=utf-8
topics: [EAGLE-3 Speculative Decoding]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:34.758468+00:00
---

# [2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

## 원본 URL

https://arxiv.org/abs/2503.01840

## 추출 본문

[2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test
Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2503.01840
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2503.01840 (cs)
 

 [Submitted on 3 Mar 2025 (v1), last revised 23 Apr 2025 (this version, v3)]

Title:EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

Authors:Yuhui Li, Fangyun Wei, Chao Zhang, Hongyang Zhang

View a PDF of the paper titled EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test, by Yuhui Li and 3 other authors
View PDFHTML (experimental)
Abstract:The sequential nature of modern LLMs makes them expensive and slow, and speculative sampling has proven to be an effective solution to this problem. Methods like EAGLE perform autoregression at the feature level, reusing top-layer features from the target model to achieve better results than vanilla speculative sampling. A growing trend in the LLM community is scaling up training data to improve model intelligence without increasing inference costs. However, we observe that scaling up data provides limited improvements for EAGLE. We identify that this limitation arises from EAGLE's feature prediction constraints. In this paper, we introduce EAGLE-3, which abandons feature prediction in favor of direct token prediction and replaces reliance on top-layer features with multi-layer feature fusion via a technique named training-time test. These improvements significantly enhance performance and enable the draft model to fully benefit from scaling up training data. Our experiments include both chat models and reasoning models, evaluated on five tasks. The results show that EAGLE-3 achieves a speedup ratio up to 6.5x, with about 1.4x improvement over EAGLE-2. In the SGLang framework, EAGLE-3 achieves a 1.38x throughput improvement at a batch size of 64. The code is available at this https URL.
 

Subjects:Computation and Language (cs.CL)Cite as:arXiv:2503.01840 [cs.CL](or arXiv:2503.01840v3 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2503.01840
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Yuhui Li [view email] 
[v1]
 Mon, 3 Mar 2025 18:59:04 UTC (700 KB)
[v2]
 Sun, 23 Mar 2025 04:33:08 UTC (701 KB)
[v3]
 Wed, 23 Apr 2025 07:08:17 UTC (701 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test, by Yuhui Li and 3 other authors

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

---
title: [2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving
source_url: https://arxiv.org/abs/2401.09670
final_url: https://arxiv.org/abs/2401.09670
status: 200
content_type: text/html; charset=utf-8
topics: [Disaggregated Prefill/Decode Serving]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:05.654354+00:00
---

# [2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving

## 원본 URL

https://arxiv.org/abs/2401.09670

## 추출 본문

[2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2401.09670
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Distributed, Parallel, and Cluster Computing

arXiv:2401.09670 (cs)
 

 [Submitted on 18 Jan 2024 (v1), last revised 6 Jun 2024 (this version, v3)]

Title:DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving

Authors:Yinmin Zhong, Shengyu Liu, Junda Chen, Jianbo Hu, Yibo Zhu, Xuanzhe Liu, Xin Jin, Hao Zhang

View a PDF of the paper titled DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving, by Yinmin Zhong and 7 other authors
View PDFHTML (experimental)
Abstract:DistServe improves the performance of large language models (LLMs) serving by disaggregating the prefill and decoding computation. Existing LLM serving systems colocate the two phases and batch the computation of prefill and decoding across all users and requests. We find that this strategy not only leads to strong prefill-decoding interferences but also couples the resource allocation and parallelism plans for both phases. LLM applications often emphasize individual latency for each phase: time to first token (TTFT) for the prefill phase and time per output token (TPOT) of each request for the decoding phase. In the presence of stringent latency requirements, existing systems have to prioritize one latency over the other, or over-provision compute resources to meet both.

DistServe assigns prefill and decoding computation to different GPUs, hence eliminating prefill-decoding interferences. Given the application's TTFT and TPOT requirements, DistServe co-optimizes the resource allocation and parallelism strategy tailored for each phase. DistServe also places the two phases according to the serving cluster's bandwidth to minimize the communication caused by disaggregation. As a result, DistServe significantly improves LLM serving performance in terms of the maximum rate that can be served within both TTFT and TPOT constraints on each GPU. Our evaluations show that on various popular LLMs, applications, and latency requirements, DistServe can serve 7.4x more requests or 12.6x tighter SLO, compared to state-of-the-art systems, while staying within latency constraints for > 90% of requests.
 

Comments:OSDI 2024Subjects:Distributed, Parallel, and Cluster Computing (cs.DC)Cite as:arXiv:2401.09670 [cs.DC](or arXiv:2401.09670v3 [cs.DC] for this version)
 https://doi.org/10.48550/arXiv.2401.09670
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Yinmin Zhong [view email] 
[v1]
 Thu, 18 Jan 2024 01:03:38 UTC (141 KB)
[v2]
 Tue, 19 Mar 2024 06:20:25 UTC (142 KB)
[v3]
 Thu, 6 Jun 2024 15:50:51 UTC (273 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving, by Yinmin Zhong and 7 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.DC

< prev  |  next >

new | recent | 2024-01

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

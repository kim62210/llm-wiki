---
title: [2504.16828] Process Reward Models That Think
source_url: https://arxiv.org/abs/2504.16828
final_url: https://arxiv.org/abs/2504.16828
status: 200
content_type: text/html; charset=utf-8
topics: [Process Reward Models (PRM) 재부상]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.230508+00:00
---

# [2504.16828] Process Reward Models That Think

## 원본 URL

https://arxiv.org/abs/2504.16828

## 추출 본문

[2504.16828] Process Reward Models That Think
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2504.16828
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Machine Learning

arXiv:2504.16828 (cs)
 

 [Submitted on 23 Apr 2025 (v1), last revised 8 Dec 2025 (this version, v5)]

Title:Process Reward Models That Think

Authors:Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang

View a PDF of the paper titled Process Reward Models That Think, by Muhammad Khalifa and 7 other authors
View PDFHTML (experimental)
Abstract:Step-by-step verifiers -- also known as process reward models (PRMs) -- are a key ingredient for test-time scaling. PRMs require step-level supervision, making them expensive to train. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers -- using only 1% of the process labels in PRM800K -- across several challenging benchmarks. Specifically, ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation on a subset of GPQA-Diamond and LiveCodeBench, our PRM surpasses discriminative verifiers trained on the full PRM800K by 8% and 4.5%, respectively. Lastly, under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. Our work highlights the value of generative, long CoT PRMs that can scale test-time compute for verification while requiring minimal supervision for training. Our code, data, and models are released at this https URL.
 

Comments:Add new ablation and minor writing fixesSubjects:Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)Cite as:arXiv:2504.16828 [cs.LG](or arXiv:2504.16828v5 [cs.LG] for this version)
 https://doi.org/10.48550/arXiv.2504.16828
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Muhammad Khalifa [view email] 
[v1]
 Wed, 23 Apr 2025 15:44:54 UTC (251 KB)
[v2]
 Sun, 18 May 2025 01:23:04 UTC (240 KB)
[v3]
 Tue, 24 Jun 2025 03:05:02 UTC (236 KB)
[v4]
 Thu, 25 Sep 2025 04:09:09 UTC (256 KB)
[v5]
 Mon, 8 Dec 2025 06:50:53 UTC (276 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Process Reward Models That Think, by Muhammad Khalifa and 7 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.LG

< prev  |  next >

new | recent | 2025-04

 Change to browse by:
 
cs
cs.AI
cs.CL

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

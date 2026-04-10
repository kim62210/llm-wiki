---
title: [2505.19475] Continuous Self-Improvement of Large Language Models by Test-time Training with Verifier-Driven Sample Selection
source_url: https://arxiv.org/abs/2505.19475
final_url: https://arxiv.org/abs/2505.19475
status: 200
content_type: text/html; charset=utf-8
topics: [Test-Time Training & Self-Improvement]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.915229+00:00
---

# [2505.19475] Continuous Self-Improvement of Large Language Models by Test-time Training with Verifier-Driven Sample Selection

## 원본 URL

https://arxiv.org/abs/2505.19475

## 추출 본문

[2505.19475] Continuous Self-Improvement of Large Language Models by Test-time Training with Verifier-Driven Sample Selection
Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2505.19475
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2505.19475 (cs)
 

 [Submitted on 26 May 2025 (v1), last revised 28 May 2025 (this version, v2)]

Title:Continuous Self-Improvement of Large Language Models by Test-time Training with Verifier-Driven Sample Selection

Authors:Mohammad Mahdi Moradi, Hossam Amer, Sudhir Mudur, Weiwei Zhang, Yang Liu, Walid Ahmed

View a PDF of the paper titled Continuous Self-Improvement of Large Language Models by Test-time Training with Verifier-Driven Sample Selection, by Mohammad Mahdi Moradi and 5 other authors
View PDFHTML (experimental)
Abstract:Learning to adapt pretrained language models to unlabeled, out-of-distribution data is a critical challenge, as models often falter on structurally novel reasoning tasks even while excelling within their training distribution. We introduce a new framework called VDS-TTT - Verifier-Driven Sample Selection for Test-Time Training to efficiently address this. We use a learned verifier to score a pool of generated responses and select only from high ranking pseudo-labeled examples for fine-tuned adaptation. Specifically, for each input query our LLM generates N candidate answers; the verifier assigns a reliability score to each, and the response with the highest confidence and above a fixed threshold is paired with its query for test-time training. We fine-tune only low-rank LoRA adapter parameters, ensuring adaptation efficiency and fast convergence. Our proposed self-supervised framework is the first to synthesize verifier driven test-time training data for continuous self-improvement of the model. Experiments across three diverse benchmarks and three state-of-the-art LLMs demonstrate that VDS-TTT yields up to a 32.29% relative improvement over the base model and a 6.66% gain compared to verifier-based methods without test-time training, highlighting its effectiveness and efficiency for on-the-fly large language model adaptation.
 

Subjects:Computation and Language (cs.CL)Cite as:arXiv:2505.19475 [cs.CL](or arXiv:2505.19475v2 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2505.19475
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Mohammad Mahdi Moradi [view email] 
[v1]
 Mon, 26 May 2025 03:54:47 UTC (1,527 KB)
[v2]
 Wed, 28 May 2025 11:04:19 UTC (1,521 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Continuous Self-Improvement of Large Language Models by Test-time Training with Verifier-Driven Sample Selection, by Mohammad Mahdi Moradi and 5 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2025-05

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

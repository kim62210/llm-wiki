---
title: [2603.00077] Autorubric: Unifying Rubric-based LLM Evaluation
source_url: https://arxiv.org/abs/2603.00077
final_url: https://arxiv.org/abs/2603.00077
status: 200
content_type: text/html; charset=utf-8
topics: [Rubric-Based Evaluation Frameworks]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:59.171700+00:00
---

# [2603.00077] Autorubric: Unifying Rubric-based LLM Evaluation

## 원본 URL

https://arxiv.org/abs/2603.00077

## 추출 본문

[2603.00077] Autorubric: Unifying Rubric-based LLM Evaluation
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2603.00077
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2603.00077 (cs)
 

 [Submitted on 13 Feb 2026 (v1), last revised 3 Apr 2026 (this version, v2)]

Title:Autorubric: Unifying Rubric-based LLM Evaluation

Authors:Delip Rao, Chris Callison-Burch

View a PDF of the paper titled Autorubric: Unifying Rubric-based LLM Evaluation, by Delip Rao and 1 other authors
View PDFHTML (experimental)
Abstract:Techniques for reliable rubric-based LLM evaluation -- ensemble judging, bias mitigation, few-shot calibration -- are scattered across papers with inconsistent terminology and partial implementations. We introduce Autorubric, an open-source framework that unifies these rubric-based LLM evaluation lessons with opinionated defaults: analytic rubrics with binary, ordinal, and nominal criteria; single-judge and ensemble evaluation; few-shot calibration; bias mitigations; and psychometric reliability metrics. We validate on three benchmarks: RiceChem (college chemistry grading, 80\% accuracy with 5-shot calibration), ResearcherBench (deep research evaluation, 931 criteria, cross-judge agreement analysis), and CHARM-100, a new chatbot evaluation dataset combining all three criterion types with ground truth labels (87\% binary accuracy, moderate-to-substantial $\kappa$). Beyond measurement, per-criterion scores and explanations serve as optimization signals. We demonstrate how Autorubric's rubric-evaluation explanations raise a peer review agent's score from 0.47 to 0.85 (above the 0.82 expert-curated baseline), and its scores serve as RL rewards to produce statistically significant improvement on AdvancedIF (+0.039, Wilcoxon $p = 0.032$) with positive transfer to IFEval. In all of these cases, Autorubric enabled us to rapidly operationalize various rubric design choices and best practices with minimal effort.
 

Comments:52 pagesSubjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI)Cite as:arXiv:2603.00077 [cs.CL](or arXiv:2603.00077v2 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2603.00077
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Delip Rao [view email] 
[v1]
 Fri, 13 Feb 2026 02:26:30 UTC (259 KB)
[v2]
 Fri, 3 Apr 2026 20:22:41 UTC (546 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Autorubric: Unifying Rubric-based LLM Evaluation, by Delip Rao and 1 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2026-03

 Change to browse by:
 
cs
cs.AI

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

---
title: [2404.12272] Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
source_url: https://arxiv.org/abs/2404.12272
final_url: https://arxiv.org/abs/2404.12272
status: 200
content_type: text/html; charset=utf-8
topics: [Synthetic Eval Data Generation]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:00.881659+00:00
---

# [2404.12272] Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences

## 원본 URL

https://arxiv.org/abs/2404.12272

## 추출 본문

[2404.12272] Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences

Support arXiv on Cornell Giving Day!

We're celebrating 35 years of open science - with YOUR support! Your generosity has helped arXiv thrive for three and a half decades. Give today to help keep science open for ALL for many years to come.

Donate!

Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2404.12272
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Human-Computer Interaction

arXiv:2404.12272 (cs)
 

 [Submitted on 18 Apr 2024]

Title:Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences

Authors:Shreya Shankar, J.D. Zamfirescu-Pereira, Björn Hartmann, Aditya G. Parameswaran, Ian Arawjo

View a PDF of the paper titled Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences, by Shreya Shankar and 4 other authors
View PDF
Abstract:Due to the cumbersome nature of human evaluation and limitations of code-based evaluation, Large Language Models (LLMs) are increasingly being used to assist humans in evaluating LLM outputs. Yet LLM-generated evaluators simply inherit all the problems of the LLMs they evaluate, requiring further human validation. We present a mixed-initiative approach to ``validate the validators'' -- aligning LLM-generated evaluation functions (be it prompts or code) with human requirements. Our interface, EvalGen, provides automated assistance to users in generating evaluation criteria and implementing assertions. While generating candidate implementations (Python functions, LLM grader prompts), EvalGen asks humans to grade a subset of LLM outputs; this feedback is used to select implementations that better align with user grades. A qualitative study finds overall support for EvalGen but underscores the subjectivity and iterative process of alignment. In particular, we identify a phenomenon we dub \emph{criteria drift}: users need criteria to grade outputs, but grading outputs helps users define criteria. What is more, some criteria appears \emph{dependent} on the specific LLM outputs observed (rather than independent criteria that can be defined \emph{a priori}), raising serious questions for approaches that assume the independence of evaluation from observation of model outputs. We present our interface and implementation details, a comparison of our algorithm with a baseline approach, and implications for the design of future LLM evaluation assistants.
 

Comments:16 pages, 4 figures, 2 tablesSubjects:Human-Computer Interaction (cs.HC); Artificial Intelligence (cs.AI)Cite as:arXiv:2404.12272 [cs.HC](or arXiv:2404.12272v1 [cs.HC] for this version)
 https://doi.org/10.48550/arXiv.2404.12272
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Shreya Shankar [view email] 
[v1]
 Thu, 18 Apr 2024 15:45:27 UTC (3,730 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences, by Shreya Shankar and 4 other authors

View PDF

TeX Source
 

view license

 Current browse context: 
cs.HC

< prev  |  next >

new | recent | 2024-04

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

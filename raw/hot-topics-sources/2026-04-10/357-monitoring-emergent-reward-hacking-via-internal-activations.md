---
title: [2603.04069] Monitoring Emergent Reward Hacking During Generation via Internal Activations
source_url: https://arxiv.org/abs/2603.04069
final_url: https://arxiv.org/abs/2603.04069
status: 200
content_type: text/html; charset=utf-8
topics: [Natural Emergent Misalignment from Reward Hacking]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:11.654176+00:00
---

# [2603.04069] Monitoring Emergent Reward Hacking During Generation via Internal Activations

## 원본 URL

https://arxiv.org/abs/2603.04069

## 추출 본문

[2603.04069] Monitoring Emergent Reward Hacking During Generation via Internal Activations
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2603.04069
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2603.04069 (cs)
 

 [Submitted on 4 Mar 2026]

Title:Monitoring Emergent Reward Hacking During Generation via Internal Activations

Authors:Patrick Wilhelm, Thorsten Wittkopp, Odej Kao

View a PDF of the paper titled Monitoring Emergent Reward Hacking During Generation via Internal Activations, by Patrick Wilhelm and 2 other authors
View PDFHTML (experimental)
Abstract:Fine-tuned large language models can exhibit reward-hacking behavior arising from emergent misalignment, which is difficult to detect from final outputs alone. While prior work has studied reward hacking at the level of completed responses, it remains unclear whether such behavior can be identified during generation. We propose an activation-based monitoring approach that detects reward-hacking signals from internal representations as a model generates its response. Our method trains sparse autoencoders on residual stream activations and applies lightweight linear classifiers to produce token-level estimates of reward-hacking activity. Across multiple model families and fine-tuning mixtures, we find that internal activation patterns reliably distinguish reward-hacking from benign behavior, generalize to unseen mixed-policy adapters, and exhibit model-dependent temporal structure during chain-of-thought reasoning. Notably, reward-hacking signals often emerge early, persist throughout reasoning, and can be amplified by increased test-time compute in the form of chain-of-thought prompting under weakly specified reward objectives. These results suggest that internal activation monitoring provides a complementary and earlier signal of emergent misalignment than output-based evaluation, supporting more robust post-deployment safety monitoring for fine-tuned language models.
 

Subjects:Computation and Language (cs.CL); Artificial Intelligence (cs.AI)Cite as:arXiv:2603.04069 [cs.CL](or arXiv:2603.04069v1 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2603.04069
Focus to learn more
 arXiv-issued DOI via DataCite

Journal reference:ICLR2026 Workshop: Principled Design for Trustworthy AI

Submission history
 From: Patrick Wilhelm [view email] 
[v1]
 Wed, 4 Mar 2026 13:44:24 UTC (781 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Monitoring Emergent Reward Hacking During Generation via Internal Activations, by Patrick Wilhelm and 2 other authors

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

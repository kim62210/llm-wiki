---
title: [2509.15541] Stress Testing Deliberative Alignment for Anti-Scheming Training
source_url: https://arxiv.org/abs/2509.15541
final_url: https://arxiv.org/abs/2509.15541
status: 200
content_type: text/html; charset=utf-8
topics: [Deliberative Alignment & Anti-Scheming Training]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:12.183564+00:00
---

# [2509.15541] Stress Testing Deliberative Alignment for Anti-Scheming Training

## 원본 URL

https://arxiv.org/abs/2509.15541

## 추출 본문

[2509.15541] Stress Testing Deliberative Alignment for Anti-Scheming Training

Happy Open Access Week from arXiv!

YOU make open access possible! Tell us why you support #openaccess and give to arXiv this week to help keep science open for all.

Donate!

Skip to main content

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2509.15541
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Artificial Intelligence

arXiv:2509.15541 (cs)
 

 [Submitted on 19 Sep 2025]

Title:Stress Testing Deliberative Alignment for Anti-Scheming Training

Authors:Bronson Schoen, Evgenia Nitishinskaya, Mikita Balesni, Axel Højmark, Felix Hofstätter, Jérémy Scheurer, Alexander Meinke, Jason Wolfe, Teun van der Weij, Alex Lloyd, Nicholas Goldowsky-Dill, Angela Fan, Andrei Matveiakin, Rusheb Shah, Marcus Williams, Amelia Glaese, Boaz Barak, Wojciech Zaremba, Marius Hobbhahn

View a PDF of the paper titled Stress Testing Deliberative Alignment for Anti-Scheming Training, by Bronson Schoen and 18 other authors
View PDF
Abstract:Highly capable AI systems could secretly pursue misaligned goals -- what we call "scheming". Because a scheming AI would deliberately try to hide its misaligned goals and actions, measuring and mitigating scheming requires different strategies than are typically used in ML. We propose that assessing anti-scheming interventions requires at least (1) testing propensity to scheme on far out-of-distribution (OOD) tasks, (2) evaluating whether lack of scheming is driven by situational awareness, and (3) checking for robustness to pre-existing misaligned goals. We use a broad category of "covert actions" -- such as secretly breaking rules or intentionally underperforming in tests -- as a proxy for scheming, and design evaluations for covert actions. We then stress-test deliberative alignment as a case study for anti-scheming. Across 26 OOD evaluations (180+ environments), deliberative alignment reduces covert action rates (OpenAI o3: 13%->0.4%) but does not fully eliminate them. Our mitigation is also able to largely stop agents from pursuing a hidden goal previously trained into the model, but we still find misbehavior after additional red-teaming. We find that models' chain-of-thought (CoT) often demonstrates awareness of being evaluated for alignment, and show causal evidence that this awareness decreases covert behavior, while unawareness increases it. Therefore, we cannot exclude that the observed reductions in covert action rates are at least partially driven by situational awareness. While we rely on human-legible CoT for training, studying situational awareness, and demonstrating clear evidence of misalignment, our ability to rely on this degrades as models continue to depart from reasoning in standard English. We encourage research into alignment mitigations for scheming and their assessment, especially for the adversarial case of deceptive alignment, which this paper does not address.
 

Subjects:Artificial Intelligence (cs.AI)Cite as:arXiv:2509.15541 [cs.AI](or arXiv:2509.15541v1 [cs.AI] for this version)
 https://doi.org/10.48550/arXiv.2509.15541
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Mikita Balesni [view email] 
[v1]
 Fri, 19 Sep 2025 02:49:56 UTC (6,672 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Stress Testing Deliberative Alignment for Anti-Scheming Training, by Bronson Schoen and 18 other authors

View PDF

TeX Source
 

view license

 Current browse context: 
cs.AI

< prev  |  next >

new | recent | 2025-09

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

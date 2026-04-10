---
title: The Landscape of Agentic Reinforcement Learning for LLMs: A Survey
source_url: https://arxiv.org/abs/2509.02547
fetched_via: reader
origin_topic: Long-Horizon RL Training for Agents (Multi-Turn RLVR)
origin_section: Agent Architecture
origin_ref_label: The Landscape of Agentic Reinforcement Learning for LLMs: A Survey
fetched: 2026-04-10
---

# The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

- 원본 URL: https://arxiv.org/abs/2509.02547
- 수집 경로: reader
- 연결된 토픽: Long-Horizon RL Training for Agents (Multi-Turn RLVR)

## 요약 메모

# [2509.02547] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey We gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors.[Donate](https://info.arxiv.org/about/donate.html) Search GO ## quick links * [Login](https://arxiv.org/login) * [Help Pages](https://info.arxiv.org/help) * [About](https://info.arxiv.or

## 원문 추출

Title: The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

URL Source: https://arxiv.org/abs/2509.02547

Published Time: Tue, 27 Jan 2026 01:39:26 GMT

Markdown Content:
# [2509.02547] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

[Skip to main content](https://arxiv.org/abs/2509.02547#content)

[![Image 1: Cornell University Logo](https://arxiv.org/static/browse/0.3.4/images/icons/cu/cornell-reduced-white-SMALL.svg)](https://www.cornell.edu/)

[Learn about arXiv becoming an independent nonprofit.](https://tech.cornell.edu/arxiv/)

We gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors.[Donate](https://info.arxiv.org/about/donate.html)

[](https://arxiv.org/IgnoreMe)

[![Image 2: arxiv logo](https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg)](https://arxiv.org/)>[cs](https://arxiv.org/list/cs/recent)> arXiv:2509.02547 

[Help](https://info.arxiv.org/help) | [Advanced Search](https://arxiv.org/search/advanced)

Search

[![Image 3: arXiv logo](https://arxiv.org/static/browse/0.3.4/images/arxiv-logomark-small-white.svg)](https://arxiv.org/)

[![Image 4: Cornell University Logo](https://arxiv.org/static/browse/0.3.4/images/icons/cu/cornell-reduced-white-SMALL.svg)](https://www.cornell.edu/)

GO

## quick links

*   [Login](https://arxiv.org/login)
*   [Help Pages](https://info.arxiv.org/help)
*   [About](https://info.arxiv.org/about)

# Computer Science > Artificial Intelligence

**arXiv:2509.02547** (cs) 

 [Submitted on 2 Sep 2025 ([v1](https://arxiv.org/abs/2509.02547v1)), last revised 24 Jan 2026 (this version, v4)]

# Title:The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

Authors:[Guibin Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+G), [Hejia Geng](https://arxiv.org/search/cs?searchtype=author&query=Geng,+H), [Xiaohang Yu](https://arxiv.org/search/cs?searchtype=author&query=Yu,+X), [Zhenfei Yin](https://arxiv.org/search/cs?searchtype=author&query=Yin,+Z), [Zaibin Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Z), [Zelin Tan](https://arxiv.org/search/cs?searchtype=author&query=Tan,+Z), [Heng Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+H), [Zhongzhi Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z), [Xiangyuan Xue](https://arxiv.org/search/cs?searchtype=author&query=Xue,+X), [Yijiang Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Y), [Yifan Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+Y), [Yang Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Y), [Chen Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+C), [Yutao Fan](https://arxiv.org/search/cs?searchtype=author&query=Fan,+Y), [Zihu Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Z), [Songtao Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+S), [Francisco Piedrahita-Velez](https://arxiv.org/search/cs?searchtype=author&query=Piedrahita-Velez,+F), [Yue Liao](https://arxiv.org/search/cs?searchtype=author&query=Liao,+Y), [Hongru Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+H), [Mengyue Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+M), [Heng Ji](https://arxiv.org/search/cs?searchtype=author&query=Ji,+H), [Jun Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+J), [Shuicheng Yan](https://arxiv.org/search/cs?searchtype=author&query=Yan,+S), [Philip Torr](https://arxiv.org/search/cs?searchtype=author&query=Torr,+P), [Lei Bai](https://arxiv.org/search/cs?searchtype=author&query=Bai,+L)

View a PDF of the paper titled The Landscape of Agentic Reinforcement Learning for LLMs: A Survey, by Guibin Zhang and 24 other authors

[View PDF](https://arxiv.org/pdf/2509.02547)[HTML (experimental)](https://arxiv.org/html/2509.02547v4)
> Abstract:The emergence of agentic reinforcement learning (Agentic RL) marks a paradigm shift from conventional reinforcement learning applied to large language models (LLM RL), reframing LLMs from passive sequence generators into autonomous, decision-making agents embedded in complex, dynamic worlds. This survey formalizes this conceptual shift by contrasting the degenerate single-step Markov Decision Processes (MDPs) of LLM-RL with the temporally extended, partially observable Markov decision processes (POMDPs) that define Agentic RL. Building on this foundation, we propose a comprehensive twofold taxonomy: one organized around core agentic capabilities, including planning, tool use, memory, reasoning, self-improvement, and perception, and the other around their applications across diverse task domains. Central to our thesis is that reinforcement learning serves as the critical mechanism for transforming these capabilities from static, heuristic modules into adaptive, robust agentic behavior. To support and accelerate future research, we consolidate the landscape of open-source environments, benchmarks, and frameworks into a practical compendium. By synthesizing over five hundred recent works, this survey charts the contours of this rapidly evolving field and highlights the opportunities and challenges that will shape the development of scalable, general-purpose AI agents.

Comments:Published on Transactions on Machine Learning Research: [this https URL](https://openreview.net/forum?id=RY19y2RI1O)
Subjects:Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:[arXiv:2509.02547](https://arxiv.org/abs/2509.02547) [cs.AI]
(or [arXiv:2509.02547v4](https://arxiv.org/abs/2509.02547v4) [cs.AI] for this version)
[https://doi.org/10.48550/arXiv.2509.02547](https://doi.org/10.48550/arXiv.2509.02547)

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: Hejia Geng [[view email](https://arxiv.org/show-email/08f63b85/2509.02547)] 

**[[v1]](https://arxiv.org/abs/2509.02547v1)** Tue, 2 Sep 2025 17:46:26 UTC (5,418 KB)

**[[v2]](https://arxiv.org/abs/2509.02547v2)** Wed, 29 Oct 2025 06:27:56 UTC (5,432 KB)

**[[v3]](https://arxiv.org/abs/2509.02547v3)** Sat, 8 Nov 2025 05:55:03 UTC (5,352 KB)

**[v4]** Sat, 24 Jan 2026 22:41:54 UTC (12,708 KB)

[](https://arxiv.org/abs/2509.02547)Full-text links:
## Access Paper:

 View a PDF of the paper titled The Landscape of Agentic Reinforcement Learning for LLMs: A Survey, by Guibin Zhang and 24 other authors

*   [View PDF](https://arxiv.org/pdf/2509.02547)
*   [HTML (experimental)](https://arxiv.org/html/2509.02547v4)
*   [TeX Source](https://arxiv.org/src/2509.02547)

[![Image 5: license icon](https://arxiv.org/icons/licenses/by-4.0.png)view license](http://creativecommons.org/licenses/by/4.0/ "Rights to this article")

 Current browse context: 

cs.AI

[<prev](https://arxiv.org/prevnext?id=2509.02547&function=prev&context=cs.AI "previous in cs.AI (accesskey p)") | [next>](https://arxiv.org/prevnext?id=2509.02547&function=next&context=cs.AI "next in cs.AI (accesskey n)")

[new](https://arxiv.org/list/cs.AI/new) | [recent](https://arxiv.org/list/cs.AI/recent) | [2025-09](https://arxiv.org/list/cs.AI/2025-09)

 Change to browse by: 

[cs](https://arxiv.org/abs/2509.02547?context=cs)

[cs.CL](https://arxiv.org/abs/2509.02547?context=cs.CL)

### References & Citations

*   [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2509.02547)
*   [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2509.02547)
*   [Semantic Scholar](https://api.semanticscholar.org/arXiv:2509.02547)

export BibTeX citation Loading...

## BibTeX formatted citation

×

Data provided by: [](https://arxiv.org/abs/2509.02547)

### Bookmark

[![Image 6: BibSonomy logo](https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png)](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2509.02547&description=The%20Landscape%20of%20Agentic%20Reinforcement%20Learning%20for%20LLMs:%20A%20Survey "Bookmark on BibSonomy")[![Image 7: Reddit logo](https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png)](https://reddit.com/submit?url=https://arxiv.org/abs/2509.02547&title=The%20Landscape%20of%20Agentic%20Reinforcement%20Learning%20for%20LLMs:%20A%20Survey "Bookmark on Reddit")

Bibliographic Tools 

# Bibliographic and Citation Tools

- [x] Bibliographic Explorer Toggle 

Bibliographic Explorer _([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))_

- [x] Connected Papers Toggle 

Connected Papers _([What is Connected Papers?](https://www.connectedpapers.com/about))_

- [x] Litmaps Toggle 

Litmaps _([What is Litmaps?](https://www.litmaps.co/))_

- [x] scite.ai Toggle 

scite Smart Citations _([What are Smart Citations?](https://www.scite.ai/))_

Code, Data, Media 

# Code, Data and Media Associated with this Article

- [x] alphaXiv Toggle 

alphaXiv _([What is alphaXiv?](https://alphaxiv.org/))_

- [x] Links to Code Toggle 

CatalyzeX Code Finder for Papers _([What is CatalyzeX?](https://www.catalyzex.com/))_

- [x] DagsHub Toggle 

DagsHub _([What is DagsHub?](https://dagshub.com/))_

- [x] GotitPub Toggle 

Gotit.pub _([What is GotitPub?](http://gotit.pub/faq))_

- [x] Huggingface Toggle 

Hugging Face _([What is Huggingface?](https://huggingface.co/huggingface))_

- [x] Links to Code Toggle 

Papers with Code _([What is Papers with Code?](https://paperswithcode.com/))_

- [x] ScienceCast Toggle 

ScienceCast _([What is ScienceCast?](https://sciencecast.org/welcome))_

Demos 

# Demos

- [x] Replicate Toggle 

Replicate _([What is Replicate?](https://replicate.com/docs/arxiv/about))_

- [x] Spaces Toggle 

Hugging Face Spaces _([What is Spaces?](https://huggingface.co/docs/hub/spaces))_

- [x] Spaces Toggle 

TXYZ.AI _([What is TXYZ.AI?](https://txyz.ai/))_

Related Papers 

# Recommenders and Search Tools

- [x] Link to Influence Flower 

Influence Flower _([What are Influence Flowers?](https://influencemap.cmlab.dev/))_

- [x] Core recommender toggle 

CORE Recommender _([What is CORE?](https://core.ac.uk/services/recommender))_

*   [Author](https://arxiv.org/abs/2509.02547)
*   [Venue](https://arxiv.org/abs/2509.02547)
*   [Institution](https://arxiv.org/abs/2509.02547)
*   [Topic](https://arxiv.org/abs/2509.02547)

 About arXivLabs  

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2509.02547) | [Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html)) 

*   [About](https://info.arxiv.org/about)
*   [Help](https://info.arxiv.org/help)

*   [Contact](https://info.arxiv.org/help/contact.html)
*   [Subscribe](https://info.arxiv.org/help/subscribe)

*   [Copyright](https://info.arxiv.org/help/license/index.html)
*   [Privacy Policy](https://info.arxiv.org/help/policies/privacy_policy.html)

*   [Web Accessibility Assistance](https://info.arxiv.org/help/web_accessibility.html)
*   [arXiv Operational Status](https://status.arxiv.org/)


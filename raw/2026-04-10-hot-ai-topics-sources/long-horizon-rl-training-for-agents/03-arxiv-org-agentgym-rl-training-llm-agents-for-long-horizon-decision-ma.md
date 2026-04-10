---
title: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning
source_url: https://arxiv.org/abs/2509.08755
fetched_via: reader
origin_topic: Long-Horizon RL Training for Agents (Multi-Turn RLVR)
origin_section: Agent Architecture
origin_ref_label: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn RL
fetched: 2026-04-10
---

# AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

- 원본 URL: https://arxiv.org/abs/2509.08755
- 수집 경로: reader
- 연결된 토픽: Long-Horizon RL Training for Agents (Multi-Turn RLVR)

## 요약 메모

# [2509.08755] AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning We gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors.[Donate](https://info.arxiv.org/about/donate.html) Search GO ## quick links * [Login](https://arxiv.org/login) * [Help Pages](https://info.arxiv.

## 원문 추출

Title: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

URL Source: https://arxiv.org/abs/2509.08755

Published Time: Thu, 11 Sep 2025 00:44:26 GMT

Markdown Content:
# [2509.08755] AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

[Skip to main content](https://arxiv.org/abs/2509.08755#content)

[![Image 1: Cornell University Logo](https://arxiv.org/static/browse/0.3.4/images/icons/cu/cornell-reduced-white-SMALL.svg)](https://www.cornell.edu/)

[Learn about arXiv becoming an independent nonprofit.](https://tech.cornell.edu/arxiv/)

We gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors.[Donate](https://info.arxiv.org/about/donate.html)

[](https://arxiv.org/IgnoreMe)

[![Image 2: arxiv logo](https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg)](https://arxiv.org/)>[cs](https://arxiv.org/list/cs/recent)> arXiv:2509.08755 

[Help](https://info.arxiv.org/help) | [Advanced Search](https://arxiv.org/search/advanced)

Search

[![Image 3: arXiv logo](https://arxiv.org/static/browse/0.3.4/images/arxiv-logomark-small-white.svg)](https://arxiv.org/)

[![Image 4: Cornell University Logo](https://arxiv.org/static/browse/0.3.4/images/icons/cu/cornell-reduced-white-SMALL.svg)](https://www.cornell.edu/)

GO

## quick links

*   [Login](https://arxiv.org/login)
*   [Help Pages](https://info.arxiv.org/help)
*   [About](https://info.arxiv.org/about)

# Computer Science > Machine Learning

**arXiv:2509.08755** (cs) 

 [Submitted on 10 Sep 2025]

# Title:AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

Authors:[Zhiheng Xi](https://arxiv.org/search/cs?searchtype=author&query=Xi,+Z), [Jixuan Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+J), [Chenyang Liao](https://arxiv.org/search/cs?searchtype=author&query=Liao,+C), [Baodai Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+B), [Honglin Guo](https://arxiv.org/search/cs?searchtype=author&query=Guo,+H), [Jiaqi Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+J), [Rui Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+R), [Junjie Ye](https://arxiv.org/search/cs?searchtype=author&query=Ye,+J), [Jiazheng Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+J), [Wenxiang Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+W), [Wei He](https://arxiv.org/search/cs?searchtype=author&query=He,+W), [Yiwen Ding](https://arxiv.org/search/cs?searchtype=author&query=Ding,+Y), [Guanyu Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+G), [Zehui Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Z), [Zhengyin Du](https://arxiv.org/search/cs?searchtype=author&query=Du,+Z), [Xuesong Yao](https://arxiv.org/search/cs?searchtype=author&query=Yao,+X), [Yufei Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+Y), [Jiecao Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+J), [Tao Gui](https://arxiv.org/search/cs?searchtype=author&query=Gui,+T), [Zuxuan Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+Z), [Qi Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Q), [Xuanjing Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+X), [Yu-Gang Jiang](https://arxiv.org/search/cs?searchtype=author&query=Jiang,+Y)

View a PDF of the paper titled AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning, by Zhiheng Xi and 22 other authors

[View PDF](https://arxiv.org/pdf/2509.08755)
> Abstract:Developing autonomous LLM agents capable of making a series of intelligent decisions to solve complex, real-world tasks is a fast-evolving frontier. Like human cognitive development, agents are expected to acquire knowledge and skills through exploration and interaction with the environment. Despite advances, the community still lacks a unified, interactive reinforcement learning (RL) framework that can effectively train such agents from scratch -- without relying on supervised fine-tuning (SFT) -- across diverse and realistic environments. To bridge this gap, we introduce AgentGym-RL, a new framework to train LLM agents for multi-turn interactive decision-making through RL. The framework features a modular and decoupled architecture, ensuring high flexibility and extensibility. It encompasses a wide variety of real-world scenarios, and supports mainstream RL algorithms. Furthermore, we propose ScalingInter-RL, a training approach designed for exploration-exploitation balance and stable RL optimization. In early stages, it emphasizes exploitation by restricting the number of interactions, and gradually shifts towards exploration with larger horizons to encourage diverse problem-solving strategies. In this way, the agent develops more diverse behaviors and is less prone to collapse under long horizons. We perform extensive experiments to validate the stability and effectiveness of both the AgentGym-RL framework and the ScalingInter-RL approach. Our agents match or surpass commercial models on 27 tasks across diverse environments. We offer key insights and will open-source the complete AgentGym-RL framework -- including code and datasets -- to empower the research community in developing the next generation of intelligent agents.

Comments:preprint, 39 pages, 16 figures. Project: [this https URL](https://agentgym-rl.github.io/). Framework and Code: [this https URL](https://github.com/woooodyy/AgentGym), [this https URL](https://github.com/woooodyy/AgentGym-RL)
Subjects:Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:[arXiv:2509.08755](https://arxiv.org/abs/2509.08755) [cs.LG]
(or [arXiv:2509.08755v1](https://arxiv.org/abs/2509.08755v1) [cs.LG] for this version)
[https://doi.org/10.48550/arXiv.2509.08755](https://doi.org/10.48550/arXiv.2509.08755)

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: Zhiheng Xi [[view email](https://arxiv.org/show-email/b1928f85/2509.08755)] 

**[v1]** Wed, 10 Sep 2025 16:46:11 UTC (8,852 KB)

[](https://arxiv.org/abs/2509.08755)Full-text links:
## Access Paper:

 View a PDF of the paper titled AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning, by Zhiheng Xi and 22 other authors

*   [View PDF](https://arxiv.org/pdf/2509.08755)
*   [TeX Source](https://arxiv.org/src/2509.08755)

[view license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/ "Rights to this article")

 Current browse context: 

cs.LG

[<prev](https://arxiv.org/prevnext?id=2509.08755&function=prev&context=cs.LG "previous in cs.LG (accesskey p)") | [next>](https://arxiv.org/prevnext?id=2509.08755&function=next&context=cs.LG "next in cs.LG (accesskey n)")

[new](https://arxiv.org/list/cs.LG/new) | [recent](https://arxiv.org/list/cs.LG/recent) | [2025-09](https://arxiv.org/list/cs.LG/2025-09)

 Change to browse by: 

[cs](https://arxiv.org/abs/2509.08755?context=cs)

[cs.AI](https://arxiv.org/abs/2509.08755?context=cs.AI)

[cs.CL](https://arxiv.org/abs/2509.08755?context=cs.CL)

### References & Citations

*   [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2509.08755)
*   [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2509.08755)
*   [Semantic Scholar](https://api.semanticscholar.org/arXiv:2509.08755)

export BibTeX citation Loading...

## BibTeX formatted citation

×

Data provided by: [](https://arxiv.org/abs/2509.08755)

### Bookmark

[![Image 5: BibSonomy logo](https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png)](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2509.08755&description=AgentGym-RL:%20Training%20LLM%20Agents%20for%20Long-Horizon%20Decision%20Making%20through%20Multi-Turn%20Reinforcement%20Learning "Bookmark on BibSonomy")[![Image 6: Reddit logo](https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png)](https://reddit.com/submit?url=https://arxiv.org/abs/2509.08755&title=AgentGym-RL:%20Training%20LLM%20Agents%20for%20Long-Horizon%20Decision%20Making%20through%20Multi-Turn%20Reinforcement%20Learning "Bookmark on Reddit")

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

- [x] IArxiv recommender toggle 

IArxiv Recommender _([What is IArxiv?](https://iarxiv.org/about))_

*   [Author](https://arxiv.org/abs/2509.08755)
*   [Venue](https://arxiv.org/abs/2509.08755)
*   [Institution](https://arxiv.org/abs/2509.08755)
*   [Topic](https://arxiv.org/abs/2509.08755)

 About arXivLabs  

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2509.08755) | [Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html)) 

*   [About](https://info.arxiv.org/about)
*   [Help](https://info.arxiv.org/help)

*   [Contact](https://info.arxiv.org/help/contact.html)
*   [Subscribe](https://info.arxiv.org/help/subscribe)

*   [Copyright](https://info.arxiv.org/help/license/index.html)
*   [Privacy Policy](https://info.arxiv.org/help/policies/privacy_policy.html)

*   [Web Accessibility Assistance](https://info.arxiv.org/help/web_accessibility.html)
*   [arXiv Operational Status](https://status.arxiv.org/)


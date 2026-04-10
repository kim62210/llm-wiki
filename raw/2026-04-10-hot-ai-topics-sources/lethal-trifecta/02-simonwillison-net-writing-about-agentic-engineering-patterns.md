---
title: Writing about Agentic Engineering Patterns
source_url: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
fetched_via: reader
origin_topic: Agent Security: Lethal Trifecta & Prompt Injection Defense
origin_section: Agent Architecture
origin_ref_label: Writing about Agentic Engineering Patterns (Simon Willison)
fetched: 2026-04-10
---

# Writing about Agentic Engineering Patterns

- 원본 URL: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
- 수집 경로: reader
- 연결된 토픽: Agent Security: Lethal Trifecta & Prompt Injection Defense

## 요약 메모

# Writing about Agentic Engineering Patterns # [Simon Willison’s Weblog](https://simonwillison.net/) **Sponsored by:**[WorkOS](https://fandf.co/4v8pTAt) — Production-ready APIs for auth and access control, so you can ship faster. ## Writing about Agentic Engineering Patterns 23rd February 2026 I’ve started a new project to collect and document **[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-

## 원문 추출

Title: Writing about Agentic Engineering Patterns

URL Source: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/

Published Time: Fri, 10 Apr 2026 00:21:52 GMT

Markdown Content:
# Writing about Agentic Engineering Patterns

# [Simon Willison’s Weblog](https://simonwillison.net/)

[Subscribe](https://simonwillison.net/about/#subscribe)

**Sponsored by:**[WorkOS](https://fandf.co/4v8pTAt) — Production-ready APIs for auth and access control, so you can ship faster. 

## Writing about Agentic Engineering Patterns

23rd February 2026

I’ve started a new project to collect and document **[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)**—coding practices and patterns to help get the best results out of this new era of coding agent development we find ourselves entering.

I’m using **Agentic Engineering** to refer to building software using coding agents—tools like Claude Code and OpenAI Codex, where the defining feature is that they can both generate and _execute_ code—allowing them to test that code and iterate on it independently of turn-by-turn guidance from their human supervisor.

I think of **vibe coding** using its [original definition](https://simonwillison.net/2025/Mar/19/vibe-coding/) of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code.

Agentic Engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise.

There is so much to learn and explore about this new discipline! I’ve already published a lot [under my ai-assisted-programming tag](https://simonwillison.net/tags/ai-assisted-programming/) (345 posts and counting) but that’s been relatively unstructured. My new goal is to produce something that helps answer the question “how do I get good results out of this stuff” all in one place.

I’ll be developing and growing this project here on my blog as a series of chapter-shaped patterns, loosely inspired by the format popularized by [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) back in 1994.

I published the first two chapters today:

*   **[Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)** talks about the central challenge of agentic engineering: the cost to churn out initial working code has dropped to almost nothing, how does that impact our existing intuitions about how we work, both individually and as a team?
*   **[Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)** describes how test-first development helps agents write more succinct and reliable code with minimal extra prompting.

I hope to add more chapters at a rate of 1-2 a week. I don’t really know when I’ll stop, there’s a lot to cover!

#### Written by me, not by an LLM

I have a strong personal policy of not publishing AI-generated writing under my own name. That policy will hold true for Agentic Engineering Patterns as well. I’ll be using LLMs for proofreading and fleshing out example code and all manner of other side-tasks, but the words you read here will be my own.

#### Chapters and Guides

Agentic Engineering Patterns isn’t exactly _a book_, but it’s kind of book-shaped. I’ll be publishing it on my site using a new shape of content I’m calling a _guide_. A guide is a collection of chapters, where each chapter is effectively a blog post with a less prominent date that’s designed to be updated over time, not frozen at the point of first publication.

Guides and chapters are my answer to the challenge of publishing “evergreen” content on a blog. I’ve been trying to find a way to do this for a while now. This feels like a format that might stick.

If you’re interested in the implementation you can find the code in the [Guide](https://github.com/simonw/simonwillisonblog/blob/b9cd41a0ac4a232b2a6c90ca3fff9ae465263b02/blog/models.py#L262-L280), [Chapter](https://github.com/simonw/simonwillisonblog/blob/b9cd41a0ac4a232b2a6c90ca3fff9ae465263b02/blog/models.py#L349-L405) and [ChapterChange](https://github.com/simonw/simonwillisonblog/blob/b9cd41a0ac4a232b2a6c90ca3fff9ae465263b02/blog/models.py#L408-L423) models and the [associated Django views](https://github.com/simonw/simonwillisonblog/blob/b9cd41a0ac4a232b2a6c90ca3fff9ae465263b02/blog/views.py#L775-L923), almost all of which was written by Claude Opus 4.6 running in Claude Code for web accessed via my iPhone.

Posted [23rd February 2026](https://simonwillison.net/2026/Feb/23/) at 5:43 pm · Follow me on [Mastodon](https://fedi.simonwillison.net/@simon), [Bluesky](https://bsky.app/profile/simonwillison.net), [Twitter](https://twitter.com/simonw) or [subscribe to my newsletter](https://simonwillison.net/about/#subscribe)

## More recent articles

*   [Meta's new model is Muse Spark, and meta.ai chat has some interesting tools](https://simonwillison.net/2026/Apr/8/muse-spark/) - 8th April 2026
*   [Anthropic's Project Glasswing - restricting Claude Mythos to security researchers - sounds necessary to me](https://simonwillison.net/2026/Apr/7/project-glasswing/) - 7th April 2026
*   [The Axios supply chain attack used individually targeted social engineering](https://simonwillison.net/2026/Apr/3/supply-chain-social-engineering/) - 3rd April 2026

This is **Writing about Agentic Engineering Patterns** by Simon Willison, posted on [23rd February 2026](https://simonwillison.net/2026/Feb/23/).

[blogging 121](https://simonwillison.net/tags/blogging/)[design-patterns 18](https://simonwillison.net/tags/design-patterns/)[projects 524](https://simonwillison.net/tags/projects/)[writing 29](https://simonwillison.net/tags/writing/)[ai 1954](https://simonwillison.net/tags/ai/)[generative-ai 1734](https://simonwillison.net/tags/generative-ai/)[llms 1701](https://simonwillison.net/tags/llms/)[ai-assisted-programming 373](https://simonwillison.net/tags/ai-assisted-programming/)[vibe-coding 82](https://simonwillison.net/tags/vibe-coding/)[coding-agents 190](https://simonwillison.net/tags/coding-agents/)[agentic-engineering 41](https://simonwillison.net/tags/agentic-engineering/)[site-upgrades 26](https://simonwillison.net/tags/site-upgrades/)
**Next:**[I vibe coded my dream macOS presentation app](https://simonwillison.net/2026/Feb/25/present/)

**Previous:**[Adding TILs, releases, museums, tools and research to my blog](https://simonwillison.net/2026/Feb/20/beats/)

### Monthly briefing

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

[Sponsor & subscribe](https://github.com/sponsors/simonw/)

*   [Disclosures](https://simonwillison.net/about/#disclosures)
*   [Colophon](https://simonwillison.net/about/#about-site)
*   ©
*   [2002](https://simonwillison.net/2002/)
*   [2003](https://simonwillison.net/2003/)
*   [2004](https://simonwillison.net/2004/)
*   [2005](https://simonwillison.net/2005/)
*   [2006](https://simonwillison.net/2006/)
*   [2007](https://simonwillison.net/2007/)
*   [2008](https://simonwillison.net/2008/)
*   [2009](https://simonwillison.net/2009/)
*   [2010](https://simonwillison.net/2010/)
*   [2011](https://simonwillison.net/2011/)
*   [2012](https://simonwillison.net/2012/)
*   [2013](https://simonwillison.net/2013/)
*   [2014](https://simonwillison.net/2014/)
*   [2015](https://simonwillison.net/2015/)
*   [2016](https://simonwillison.net/2016/)
*   [2017](https://simonwillison.net/2017/)
*   [2018](https://simonwillison.net/2018/)
*   [2019](https://simonwillison.net/2019/)
*   [2020](https://simonwillison.net/2020/)
*   [2021](https://simonwillison.net/2021/)
*   [2022](https://simonwillison.net/2022/)
*   [2023](https://simonwillison.net/2023/)
*   [2024](https://simonwillison.net/2024/)
*   [2025](https://simonwillison.net/2025/)
*   [2026](https://simonwillison.net/2026/)


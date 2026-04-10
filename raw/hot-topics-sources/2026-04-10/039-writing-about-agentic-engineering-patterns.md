---
title: Writing about Agentic Engineering Patterns
source_url: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns
final_url: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
status: 200
content_type: text/html; charset=utf-8
topics: [Agent Security: Lethal Trifecta & Prompt Injection Defense]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:30.397080+00:00
---

# Writing about Agentic Engineering Patterns

## 원본 URL

https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns

## 추출 본문

Writing about Agentic Engineering Patterns

Simon Willison’s Weblog
Subscribe

Sponsored by:WorkOS — Production-ready APIs for auth and access control, so you can ship faster.
 

Writing about Agentic Engineering Patterns

23rd February 2026

I’ve started a new project to collect and document Agentic Engineering Patterns—coding practices and patterns to help get the best results out of this new era of coding agent development we find ourselves entering.

I’m using Agentic Engineering to refer to building software using coding agents—tools like Claude Code and OpenAI Codex, where the defining feature is that they can both generate and execute code—allowing them to test that code and iterate on it independently of turn-by-turn guidance from their human supervisor.

I think of vibe coding using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code.

Agentic Engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise.

There is so much to learn and explore about this new discipline! I’ve already published a lot under my ai-assisted-programming tag (345 posts and counting) but that’s been relatively unstructured. My new goal is to produce something that helps answer the question “how do I get good results out of this stuff” all in one place.

I’ll be developing and growing this project here on my blog as a series of chapter-shaped patterns, loosely inspired by the format popularized by Design Patterns: Elements of Reusable Object-Oriented Software back in 1994.

I published the first two chapters today:

Writing code is cheap now talks about the central challenge of agentic engineering: the cost to churn out initial working code has dropped to almost nothing, how does that impact our existing intuitions about how we work, both individually and as a team?

Red/green TDD describes how test-first development helps agents write more succinct and reliable code with minimal extra prompting.

I hope to add more chapters at a rate of 1-2 a week. I don’t really know when I’ll stop, there’s a lot to cover!

Written by me, not by an LLM

I have a strong personal policy of not publishing AI-generated writing under my own name. That policy will hold true for Agentic Engineering Patterns as well. I’ll be using LLMs for proofreading and fleshing out example code and all manner of other side-tasks, but the words you read here will be my own.

Chapters and Guides

Agentic Engineering Patterns isn’t exactly a book, but it’s kind of book-shaped. I’ll be publishing it on my site using a new shape of content I’m calling a guide. A guide is a collection of chapters, where each chapter is effectively a blog post with a less prominent date that’s designed to be updated over time, not frozen at the point of first publication.

Guides and chapters are my answer to the challenge of publishing “evergreen” content on a blog. I’ve been trying to find a way to do this for a while now. This feels like a format that might stick.

If you’re interested in the implementation you can find the code in the Guide, Chapter and ChapterChange models and the associated Django views, almost all of which was written by Claude Opus 4.6 running in Claude Code for web accessed via my iPhone.

Posted 23rd February 2026 at 5:43 pm · Follow me on Mastodon, Bluesky, Twitter or subscribe to my newsletter

More recent articles

Meta's new model is Muse Spark, and meta.ai chat has some interesting tools - 8th April 2026

Anthropic's Project Glasswing - restricting Claude Mythos to security researchers - sounds necessary to me - 7th April 2026

The Axios supply chain attack used individually targeted social engineering - 3rd April 2026

This is Writing about Agentic Engineering Patterns by Simon Willison, posted on 23rd February 2026.

 blogging
 121
 design-patterns
 18
 projects
 524
 writing
 29
 ai
 1954
 generative-ai
 1734
 llms
 1701
 ai-assisted-programming
 373
 vibe-coding
 82
 coding-agents
 190
 agentic-engineering
 41
 site-upgrades
 26
Next:I vibe coded my dream macOS presentation app

Previous:Adding TILs, releases, museums, tools and research to my blog

 Monthly briefing
 

 Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments.
 

 Pay me to send you less!
 

 Sponsor & subscribe
 

Disclosures

Colophon

©

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

2020

2021

2022

2023

2024

2025

2026

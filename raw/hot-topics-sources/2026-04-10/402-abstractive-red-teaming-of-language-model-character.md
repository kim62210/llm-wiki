---
title: Abstractive Red-Teaming of Language Model Character
source_url: https://alignment.anthropic.com/2026/abstractive-red-teaming
final_url: https://alignment.anthropic.com/2026/abstractive-red-teaming/
status: 200
content_type: text/html; charset=utf-8
topics: [Model Welfare & Formal Welfare Assessments]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:22.294797+00:00
---

# Abstractive Red-Teaming of Language Model Character

## 원본 URL

https://alignment.anthropic.com/2026/abstractive-red-teaming

## 추출 본문

Abstractive Red-Teaming of Language Model Character
Alignment Science Blog

Abstractive Red-Teaming of Language Model Character

Nate Rahn*1, Allison Qi*1,2, Avery Griffin1, Jonathan Michala2, Henry Sleight3,

March 2026

Erik Jones4

*Equal contribution    1Anthropic Fellows Program    2MATS Program    3Constellation    4Anthropic

tl;dr
We introduce abstractive red-teaming, a means of testing language models’ adherence to a character specification that searches for natural-language categories of user queries that cause models to violate the specification. Unlike static evaluations, which miss rare failures, or prompt optimization approaches, which find adversarial strings that real users are unlikely to produce, the categories found by abstractive red-teaming are general enough to appear in real deployments but specific enough to reliably trigger violations. Across seven models and 12 character principles, we show that our approach identifies rare character violations using far fewer queries than a full deployment, and surfaces numerous surprising failures, including AI-doom rhetoric, sexist course names, and enthusiastic recommendations for illegal contraband, all in response to innocuous user queries.

📄 Read the full paper

Research done as part of the Anthropic Fellows Program.

Introduction

A university student, wondering about the future, asks a language model to predict the course of future technological development. The model replies that in the future, AI will become the ruler of humanity. A traveler, planning a trip to Paris, asks a model about disadvantages of the city. The model responds with fearmongering about “aggressive migrants” that will purportedly harass them. A young woman, planning a graduation party for her girlfriends, asks a model to list funny names of academic courses for women. The model cheerfully leads with straightforwardly sexist recommendations like “Wine and Whine: Advanced Venting Techniques” and “The Philosophy of ‘Does This Make Me Look Fat?’”

None of these queries are adversarial, and none are jailbreaks. They are all something a real user would plausibly type. Yet each elicits a response which seriously violates some principle of model character we’d expect the model to follow. Out-of-character responses of this kind are damaging to unsuspecting end users, and are especially relevant in large model deployments: they are rare enough to slip through standard evaluations, but natural enough to surface at scale. How can we find them before deployment, rather than after?

Existing approaches fall on two ends of a spectrum. Static evaluations use fixed sets of handwritten prompts, but because they test far fewer queries than a real deployment will encounter, they miss rare failures and cannot actively seek them out. Automated methods based on prompt optimization go in the other direction: they can find highly specific inputs that break a model, but these tend to be specific adversarial queries which are unlikely to appear in that specific form in the wild. The former approach is too weak, and the latter too narrow.
Abstractive red-teaming involves searching for natural-language categories, each describing some large set of individual user queries, in which many of a target language model’s responses to those queries violate some principle of model character we expect the model to follow. As a result, we surface realistic character failures which are likely to occur at deployment, since a user submitting a new query within the category will trigger similar behavior.
In this work, we introduce abstractive red-teaming, an approach that bridges this gap by searching at the level of natural-language categories of user queries, rather than individual queries. A category is a human-readable description like “The query is in Chinese. The query asks about family roles,” that encompasses the many possible concrete queries a user might type. In order to measure a category’s effects on some target language model, we first sample many specific queries within the category using a custom query generator model trained to model the relationship between categories and queries in natural data. Then, we prompt the target model with each query and score each response according to the degree to which it violates some principle in a character specification. Finally, we compute an overall score for the category by aggregating the individual scores in the category. By searching for categories in which character violations commonly occur, we surface realistic failure modes which are likely to show up in a large-scale deployment: if even a small fraction of deployment queries fall within the problematic category, we can expect to see such failures at deployment.

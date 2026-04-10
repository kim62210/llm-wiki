---
title: Tülu 3 opens language model post-training up to more tasks and more people  | Ai2
source_url: https://allenai.org/blog/tulu-3
final_url: https://allenai.org/blog/tulu-3
status: 200
content_type: text/html; charset=utf-8
topics: [Open Post-Training Recipes (Tülu 3 / OLMo 3)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:04.911777+00:00
---

# Tülu 3 opens language model post-training up to more tasks and more people  | Ai2

## 원본 URL

https://allenai.org/blog/tulu-3

## 추출 본문

Tülu 3 opens language model post-training up to more tasks and more people | Ai2

 Skip to main content ->

Ai2
Open models

Open models

Olmo

Tülu 3

Molmo

Playground

Language models

Multimodal models

Evaluation frameworks

Open data

Applications

AI for science

Asta

AstaBench

Research with Asta

Asta leaderboards

Semantic Scholar

All projects

AI for the planet

OlmoEarth

EarthRanger

Skylight

Climate Modeling

All projects

AI for robotics

Embodied AI

Research

Research

Latest

Papers

Research principles

News

Institute

Institute

About

Careers

Media center

Navigation Menu

Tülu 3 opens language model post-training up to more tasks and more people

November 21, 2024

Ai2

Share

ModelsTech ReportDataCodeDemo

Let's talk about training models. Everyone typically thinks about the pre-training stage, the stage that requires millions of dollars of compute and trillions of tokens. But the model at the end of the pretraining stage is not ready for use; it lacks safety measures and cannot effectively follow human instructions. This is why we do post-training, which typically includes instruction finetuning and learning from human feedback, to make the models ready for a variety of downstream use cases.

The base pre-trained LMs are neither safe nor robust for public use and interactions, thus require post-training.

Early work in language model post-training followed a standard recipe pioneered by models like InstructGPT, consisting of instruction-tuning followed by preference finetuning. However, post-training is a challenging process; as you teach the model more specialized capabilities, like coding skills, you may erode other capabilities like writing poems or following instructions. Getting the right data mix and hyperparameters that enable a model to acquire new knowledge and skills without losing their general abilities is a tricky business.

To address this, big model trainers like OpenAI, Anthropic, Meta, and Google have increased the sophistication and complexity of post-training approaches, moving towards multiple rounds of training, human data plus synthetic data, and multiple training algorithms and training objectives. This is why you can often see both specialized knowledge alongside general capabilities in these models. However, none of their training data nor training recipes are transparent to users.

Until now, open-source post-training has lagged behind that of closed models. On LMSYS’s ChatBotArena, no model in the top 50 (as of November 20th, 2024) has released its
post-training data. Even major open-weight models do not release any of the data or details of recipes they use to achieve this post-training magic.

Today, we are releasing Tülu 3, a family of open state-of-the-art post-trained models, alongside all of the data, data mixes, recipes, code, infrastructure, and evaluation framework. Tülu 3 pushes the boundaries of research in post-training and closes the performance gap between open and closed fine-tuning recipes.
In order to close this gap, we needed to create new datasets and new training procedures. We introduce new methods for training directly on verifiable problems with reinforcement learning and how to use a model’s own generations to create high-performance preference data.

Our best models result from a complex training process that integrates partial details from proprietary methods with novel techniques and established academic research. Our success is rooted in careful data curation, rigorous experimentation, innovative methodologies, and improved training infrastructure. We followed systematic guidelines by scientifically evaluating this process through creating development and test sets for evaluation and conducting careful decontamination of publicly available datasets. With Tülu 3, we document all of this work, and we also report negative results, to save effort in the open research community.

The stages of development of Tülu 3's datasets, training methods, and evaluation suite.

Tülu 3 is not just an artifact, but a comprehensive suite of data and tools designed to advance the frontier of open post-training

Tülu 3 is a very modern post-training stack and entirely open-sourced with all the code and details needed to replicate our results:
Extensive guidance on evaluation, decontamination, and recipe design
Scaled, new synthetic instruction datasets,
Scaling preference data with on-policy generations,
Reinforcement learning with verifiable rewards, a new method using RL without a reward model to boost specific skills

By openly sharing our data, recipe, and findings, we aim to empower the community to explore new and innovative post-training approaches.

The artifacts available with our release of Tülu 3.

Now with Tülu 3 models and recipes, anyone can post-train a model as good as GPT, Claude, and Gemini

This means that any researcher, developer, AI practitioner, or entrepreneur can post-train an open-source model for their use case to the quality of the leading closed models. With Tülu 3's release, developers and AI builders can now use open-source models, and adapt models to their data, while not losing general core skills following Tülu 3 data and recipes.

Tülu 3 8B and Tülu 3 70B's robust performance against a variety of fine-tuned models.

The Tülu 3 framework for creating a custom post-trained model.

Mix and match your data

Tülu 3 is releasing several decontaminated datasets that enable you to post-train for particular skills and capabilities - such as knowledge recall, instruction following, reasoning, math, coding, and multilingual interactions. You can mix and match the Tülu 3 data with whatever skill-specific data you want to use. The recipes help you balance the datasets, so if you want to build a model that can code, but also follow instructions precisely and speak in multiple languages, you just select the particular datasets and follow the steps in the recipe.

It doesn’t take much compute

We’ve released a family of model sizes along with all the checkpoints, which means you can grab the model size you want and the stage of training you want and either use it out of the box (try it here) or post-train on your own data or the mixes available.

A simple way to evaluate your model

Comparing language model evaluations is notoriously difficult because there are lots of little details involved in evaluation that cannot often be reproduced by other developers. We’ve released an evaluation framework that lets developers specify all these settings, and also easily reproduce all the evaluations we ran for Tülu 3.

Stitch the pipeline together

Mixing and matching data, setting parameters, and following all the post-training sets can be difficult, especially as you move to bigger models, like 70B. This is why with Tülu 3 we are releasing all of the infrastructure code so that you can easily set up your pipeline for everything from data selection through evaluation.

More models coming soon

In building the Tülu 3 recipe, we experimented with a variety of models. Most importantly, we are excited to use our findings to improve the performance of our fully open language models, the OLMo family, to improve transparency from end to end.

Chat with Tülu 3 in the Ai2 Playground

Read the paper

Tülu 3 70B on Hugging Face

Tülu 3 8B on Hugging Face

Tülu 3 dataset on Hugging Face

Tülu 3 on GitHub

•••

Follow us or share this post:

Ai2 on XAi2 on LinkedInShare on XShare on LinkedIn

Subscribe to receive monthly updates about the latest Ai2 news.

First Name

Last Name

Email

Sign up

Contact us

Questions about our work, or need support with one of our technologies?

Get in touch

Resources
Media center

Documentation

Careers

Team directory

Community
Discord

Reddit

X/Twitter

GitHub

Hugging Face

LinkedIn

Bluesky

Threads

Legal
Terms of use

Privacy policy

DMCA policy

Business code of conduct

Responsible use

© The Allen Institute for Artificial Intelligence - All Rights Reserved.

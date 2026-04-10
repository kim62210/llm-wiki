---
title: Open-sourcing circuit-tracing tools \ Anthropic
source_url: https://www.anthropic.com/research/open-source-circuit-tracing
final_url: https://www.anthropic.com/research/open-source-circuit-tracing
status: 200
content_type: text/html; charset=utf-8
topics: [Circuit Tracing & Attribution Graphs]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:14.852515+00:00
---

# Open-sourcing circuit-tracing tools \ Anthropic

## 원본 URL

https://www.anthropic.com/research/open-source-circuit-tracing

## 추출 본문

Skip to main contentSkip to footer

Research

Economic Futures

Commitments

Learn

News

Try Claude

Interpretability

Open-sourcing circuit tracing tools

May 29, 2025

In our recent interpretability research, we introduced a new method to trace the thoughts of a large language model. Today, we’re open-sourcing the method so that anyone can build on our research.

Our approach is to generate attribution graphs, which (partially) reveal the steps a model took internally to decide on a particular output. The open-source library we’re releasing supports the generation of attribution graphs on popular open-weights models—and a frontend hosted by Neuronpedia lets you explore the graphs interactively.

This project was led by participants in our Anthropic Fellows program, in collaboration with Decode Research.

An overview of the interactive graph explorer UI on Neuronpedia.

To get started, you can visit the Neuronpedia interface to generate and view your own attribution graphs for prompts of your choosing. For more sophisticated usage and research, you can view the code repository. This release enables researchers to:

Trace circuits on supported models, by generating their own attribution graphs;

Visualize, annotate, and share graphs in an interactive frontend;

Testhypotheses by modifying feature values and observing how model outputs change.

We’ve already used these tools to study interesting behaviors like multi-step reasoning and multilingual representations in Gemma-2-2b and Llama-3.2-1b—see our demo notebook for examples and analysis. We also invite the community to help us find additional interesting circuits—as inspiration, we provide additional attribution graphs that we haven’t yet analyzed in the demo notebook and on Neuronpedia.

Our CEO Dario Amodei wrote recently about the urgency of interpretability research: at present, our understanding of the inner workings of AI lags far behind the progress we’re making in AI capabilities. By open-sourcing these tools, we're hoping to make it easier for the broader community to study what’s going on inside language models. We’re looking forward to seeing applications of these tools to understand model behaviors—as well as extensions that improve the tools themselves.

The open-source-circuit-finding library was developed by Anthropic Fellows Michael Hanna and Mateusz Piotrowski with mentorship from Emmanuel Ameisen and Jack Lindsey. The Neuronpedia integration was implemented by Decode Research (Neuronpedia lead: Johnny Lin; Science lead/director: Curt Tigges). Our Gemma graphs are based on transcoders trained as part of the GemmaScope project. For questions or feedback, please open an issue on GitHub.

Related content

Trustworthy agents in practice

AI “agents” represent the latest major shift in how people and organizations are using AI. Here, we explain how they work and how we ensure they're trustworthy.
Read more

Emotion concepts and their function in a large language model

All modern language models sometimes act like they have emotions. What’s behind these behaviors? Our interpretability team investigates.
Read more

How Australia Uses Claude: Findings from the Anthropic Economic Index
Read more

Products

Claude

Claude Code

Claude Code Enterprise

Claude Code Security

Claude Cowork

Claude for Chrome

Claude for Excel

Claude for PowerPoint

Claude for Slack

Skills

Max plan

Team plan

Enterprise plan

Download app

Pricing

Log in to Claude

Models

Mythos preview

Opus

Sonnet

Haiku

Solutions

AI agents

Code modernization

Coding

Customer support

Education

Financial services

Government

Healthcare

Life sciences

Nonprofits

Security

Claude Platform

Overview

Developer docs

Pricing

Marketplace

Regional compliance

Amazon Bedrock

Google Cloud’s Vertex AI

Microsoft Foundry

Console login

Resources

Blog

Claude partner network

Community

Connectors

Courses

Customer stories

Engineering at Anthropic

Events

Inside Claude Code

Inside Claude Cowork

Plugins

Powered by Claude

Service partners

Startups program

Tutorials

Use cases

Help and security

Availability

Status

Support center

Company

Anthropic

Careers

Economic Futures

Research

News

Claude’s Constitution

Responsible Scaling Policy

Security and compliance

Transparency

Terms and policies

Privacy policy

Consumer health data privacy policy

Responsible disclosure policy

Terms of service: Commercial

Terms of service: Consumer

Usage policy

© 2026 Anthropic PBC

Open-sourcing circuit-tracing tools \ Anthropic

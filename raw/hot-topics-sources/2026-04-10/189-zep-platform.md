---
title: Context Engineering & Agent Memory Platform for AI Agents - Zep
source_url: https://www.getzep.com
final_url: https://www.getzep.com
status: 200
content_type: text/html; charset=utf-8
topics: [Zep / Graphiti Temporal Knowledge Graph Memory]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:51.941386+00:00
---

# Context Engineering & Agent Memory Platform for AI Agents - Zep

## 원본 URL

https://www.getzep.com

## 추출 본문

Context Engineering & Agent Memory Platform for AI Agents - Zep

We're hiring!Come build with us→

Product

Agent MemoryGraph RAGAgent ContextKnowledge Graph MCPOpen Source

DocumentationPricingEnterprise
Resources

Context EngineeringFor DevelopersFor Engineering LeadersBuilding AgentsBlog

We're Hiring
Company

AboutCareers

Log in
Book a DemoSign Up

Context Engineering

|

Zep assembles therightcontextfrom chat history, business data, and user behavior.
Buildpersonalized,fast, andreliableagents.

Any Framework|Three Lines of Code|200ms Retrieval

Start buildingTry Playground

Trusted by developers at

End-to-End Context Engineering

Zep connects your data sources, builds a unified context graph of your users, and delivers assembled context to your agent. One pipeline. One API.

Chat History

Business Data

User Interactions

Graph Construction

Entity Extraction

Fact Invalidation

Context

Retrieve & Assemble

User Traits

Recent Interactions

Business Data

1

Ingest

Chat messages, JSON business data, documents. Zep extracts entities, relationships, and facts automatically.

2

Graph

A temporal context graph that evolves with every interaction. When facts change, old ones are invalidated.

3

Assemble

When your agent needs context, Zep retrieves what's relevant and formats it for your LLM. Token-efficient.

Every Source

Chat history, CRM, app events, documents. Zep ingests from anywhere and builds a unified context graph that stays current as data changes.

Chat

Documents

JSON

Built for Real-Time

Voice agents, video agents, live support. No latency issues.

<200ms

P95 Retrieval Latency

Three Lines of Code

Works with your favorite agent framework, or none at all.

example.py
Copy

# Add messages and get context
response = client.thread.add_messages(
 thread_id=thread_id,
 messages=messages,
 return_context=True
)
print(response.context)

# Returned Context

Emily Painter is a user with account ID Emily0e62 who uses digital
art tools for creative work. She maintains an active account with
the service, though has recently experienced technical issues with
the Magic Pen Tool. Emily values reliable payment processing and
seeks prompt resolution for account-related issues.

# These are the most relevant facts and their valid date ranges
# format: FACT (Date range: from - to)

 - Emily is experiencing issues with logging in.
 (2024-11-14 02:13:19+00:00 - present)
 - User account Emily0e62 has a suspended status due to payment
 failure. (2024-11-14 02:03:58+00:00 - present)
 - user has the id of Emily0e62 (2024-11-14 02:03:54 - present)
 - The failed transaction used a card with last four digits 1234.
 (2024-09-15 00:00:00+00:00 - present)
 - The reason for the transaction failure was 'Card expired'.
 (2024-09-15 00:00:00+00:00 - present)
 - user has the name of Emily Painter
 (2024-11-14 02:03:54 - present)
 - Account Emily0e62 made a failed transaction of 99.99.
 (2024-07-30 00:00:00+00:00 - 2024-08-30 00:00:00+00:00)

Why Agents Fail

Agents don't fail because the model is bad. They fail because they don't have the right context.

Chat Memory

Chat-only. Blind to business data, app events, and what the user did yesterday.

Static RAG

Stale and incomplete. Doesn't reflect what just happened or how facts have changed.

Tool Calls

Slow and unpredictable. The LLM decides when to call them. It often guesses wrong.

Context is scattered across systems. Your agent sees pieces, not the picture.

Going Beyond Chat Memory

From ingestion to retrieval, Zep builds holistic context that evolves with your users

R

Robbie

2024-09-07 14:27

I only wear Adidas shoes. I love them!

Facts

Robbie only wears Adidas shoes.

Robbie strongly favors Adidas shoes.

R

Robbie

2024-10-14 09:12

My shoes fell apart and I need to return them. I'm super angry! I'll be wearing Nike going forward!

Facts

Robbieonly wears Adidasshoes.

Robbiestrongly favors Adidasshoes.

Robbie'sAdidas shoes fell apart.

Robbie needs to return their shoes.

Robbie is angryabout their Adidas shoes falling apart.

Robbie intends to wearNikeshoes in the future.

Persistent Context

Capture state changes while integrating new data. Maintain provenance so agents can reason with evolving context over time.
Explore Persistent Context

Easy to Use, Powerful Graph

Simple APIs automatically generate context. When you need control, directly access the context graph to create, update, and search entities and relationships.
Discover Graph RAG

Copy

await client.context.createContextTemplate({
 templateId: "template1",
 template: `# USER PROFILE
%{user_summary}

# RELEVANT FACTS
%{edges limit=10}

# RELEVANT ENTITIES
%{entities limit=2 types=[person,organization]}`
});

Customizable Context Blocks

Pre-formatted context blocks optimized for LLMs. Works with your favorite agent framework, or none at all.
See Context Block

Far More Accurate, Faster, More Efficient

Zep leads on the LoCoMo benchmark with single-shot retrieval. No slow agentic loops. Multiple configurations let you optimize for accuracy, latency, and token efficiency.

80.32%@189ms

accuracy in a single retrieval call

Read the Paper

Accuracy vs Retrieval Latency

LoCoMo Benchmark results for differing Zep configs

Config format: edge_limit/node_limit

Accuracy vs Context Size

LoCoMo Benchmark results for differing Zep configs

Config format: edge_limit/node_limit

Learn More

“Zep is one of the most exciting things I've seen for real-world agent use cases in a long time. Their innovative approach is truly game-changing.”

Ken Collins

VP of Product, Torq and GenAI Expert

“Zep just introduced a game-changing way for AI agents to remember and learn. Unlike other systems that only retrieve static documents, Zep uses a temporal knowledge graph to combine conversations and structured business data, keeping track of how things change over time.”

Lior Sinclair

Founder/CEO, AlphaSignal

“Zep AI was instrumental in enabling the Sidekick's personalized experience through dynamic memory retrieval. Their innovative tech stack is powering groundbreaking projects like ArtPrize 2024, taking personalized AI experiences to the next level.”

Mark Losey

CTO at Flockx

“Zep AI empowers AI systems to think and remember like humans. By organizing memories into structured episodes and extracting key insights, it builds smarter, more intuitive AI agents that revolutionize how businesses harness intelligence.”

Vijay Morampudi

Senior Director - AI CoE, Axtria

“Zep is one of the most exciting things I've seen for real-world agent use cases in a long time. Their innovative approach is truly game-changing.”

Ken Collins

VP of Product, Torq and GenAI Expert

“Zep just introduced a game-changing way for AI agents to remember and learn. Unlike other systems that only retrieve static documents, Zep uses a temporal knowledge graph to combine conversations and structured business data, keeping track of how things change over time.”

Lior Sinclair

Founder/CEO, AlphaSignal

“Zep AI was instrumental in enabling the Sidekick's personalized experience through dynamic memory retrieval. Their innovative tech stack is powering groundbreaking projects like ArtPrize 2024, taking personalized AI experiences to the next level.”

Mark Losey

CTO at Flockx

“Zep AI empowers AI systems to think and remember like humans. By organizing memories into structured episodes and extracting key insights, it builds smarter, more intuitive AI agents that revolutionize how businesses harness intelligence.”

Vijay Morampudi

Senior Director - AI CoE, Axtria

Customized for Your Domain

Zep adapts to your business through custom entity types and relationship models. These models enable precision recall of exactly the required context, so your agents understand your business domain, not just generic conversations.

Sales and MarketingCustomer SupportE-commerceEducationHealthcare

Sales and Marketing

Store lead preferences, product interests, campaign interactions, and buying signals.

Your sales agents understand prospect history, pricing discussions, and engagement patterns to personalize outreach and close deals faster.

sales_and_marketing_entities.py
Copy

class Lead(EntityModel):
 """Represents a sales lead or prospect."""
 company_size = Field(
 description="startup, SMB, mid-market, enterprise"
 )
 budget_range = Field(
 description="Budget discussed or indicated"
 )
 decision_timeline = Field(
 description="Expected decision timeframe"
 )

Built for Teams, Proven at Scale

Deploy personalized agents in days, not months. Enterprise-grade compliance meets developer-friendly APIs.

For Developers

Ship features, not context pipelines. Three lines of code to production.

TypeScript

Python

Go

Context engineering with three lines of code

Ingest business data as JSON, text, or messages

Works with your favorite agent framework, or none at all

For DevelopersSign Up Free

For Engineering Leaders

Ship faster without compromising on security or compliance.

Enterprise compliance with SOC2 Type 2 and HIPAA

Days vs. months implementation without hiring scarce AI talent

100%+ accuracy improvements through personalized context

For Engineering LeadersSchedule Demo

Powered by Graphiti
Open Source Foundation

Zep's temporal context graph library is open source.

View on GitHub

Start shipping fast, reliable, and personalized agents

Free tier. No credit card. Full API access.

Get Started FreeTalk to Sales

Latest from the Zep Blog

Loading latest articles...

Product
Agent Memory

Graph RAG

Agent Context

Knowledge Graph MCP

Open Source

Solutions
Context Engineering

For Developers

For Engineering Leaders

Mem0 Alternative

Resources
Documentation

API Reference

Building Agents

Blog

Case Studies

Company
About

Careers

Enterprise

Pricing

Contact

Stay Updated

Get the latest updates on AI memory and LLM applications.

© 2026 Zep AI, Inc. All rights reserved.

Privacy PolicyTerms of ServiceWebsite Terms

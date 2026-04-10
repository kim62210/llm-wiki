---
title: Graphiti: Knowledge Graph Memory for an Agentic World
source_url: https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory
final_url: https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/
status: 200
content_type: text/html; charset=UTF-8
topics: [Zep / Graphiti Temporal Knowledge Graph Memory]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:54.239832+00:00
---

# Graphiti: Knowledge Graph Memory for an Agentic World

## 원본 URL

https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory

## 추출 본문

Graphiti: Knowledge Graph Memory for an Agentic WorldSkip to content

 NODES AI: Online Conference for Graph + AI - April 15, 2026 | Register Today

Menu

SearchClose Menu

Products
GRAPH DATABASE

 Neo4j AuraDB Fully managed graph database as a service

 Neo4j Graph Database Self managed, deploy anywhere graph database

GRAPH ANALYTICS

 Neo4j Aura Graph Analytics Fully managed graph analytics as a service

 Neo4j Graph Data Science Self managed graph algorithms and ML modeling

GRAPH AI

 Neo4j Aura Agent A single console to manage all your DB instances

GRAPH TOOLS

 Neo4j Fleet Manager A single control plane to manage all your DB instances

 Neo4j Bloom Easy graph visualization and exploration

PARTNER SOLUTIONS

 Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud

 Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric

Use Cases

 AI Systems Back your LLMs with a knowledge graph for better business AI

 Industries and Use Cases Fraud detection, knowledge graphs, financial services, and more

 Customer Success Stories Case studies, customer videos, proof points, and more

Developers

 Developer Center Best practices, guides, tutorials, and downloads

 GraphAcademyFree online courses and certifications. Join the 100K+ Neo4j experts.

DEVELOPERS

 Deployment Center Deploy Neo4j on any cloud or architecture

 DocumentationManuals for Neo4j products, Cypher, and drivers

 Developer Blog Deep dives into more technical Neo4j topics

 Community A global forum for online discussion

DATA SCIENTISTS

 Data Science DocumentationManuals for the Graph Data Science library

 Graph Data Science Home Learn what Neo4j offers for data science

 Get Started With Graph Data Science Download or get started in Sandbox today

 Data Science Community A global forum for data-driven professionals

AI Systems

Learn
LEARN

 DocumentationManuals for Neo4j products, Cypher, and drivers

 GraphAcademyFree online courses and certifications

 Resource Library White papers, datasheets, and more

 Customer Success Stories Case studies, customer videos, proof points, and more

CONNECT

 Neo4j Events HubLive and on-demand events, training, webinars, and demos

 Neo4j Blog Announcements, guides, and best practices

 Neo4j Video Hub Covering graph databases, data science, analytics & AI

FEATURED EVENTS

 GraphSummit 2026 Graphs + AI: Transform Your Data Into Knowledge

 NODES AI 2026 Virtual Conference Dedicated to Graph + AI

Pricing

QUICK LINKS

Partners

 Find a Partner 

 Become a Partner 

 Solution Partners 

 OEM Partners 

 Technology Partners 

 Partner Portal Login 

Company

 About Us 

 Newsroom 

 Awards and Honors 

 Graphs4Good 

 Careers 

 Culture 

 Leadership 

Support

Aura Login

Get StartedContact Us

Aura Login

PartnersPartners: submenu

Find a Partner

Become a Partner

Solution Partners

OEM Partners

Technology Partners

Partner Portal Login

CompanyCompany: submenu

About Us

Newsroom

Awards and Honors

Graphs4Good

Careers

Culture

Leadership

Support

Search

ProductsProducts: submenu

GRAPH DATABASE

 Neo4j AuraDB Fully managed graph database as a service

 Neo4j Graph Database Self managed, deploy anywhere graph database

GRAPH ANALYTICS

 Neo4j Aura Graph Analytics Fully managed graph analytics as a service

 Neo4j Graph Data Science Self managed graph algorithms and ML modeling

GRAPH AI

 Neo4j Aura Agent A single console to manage all your DB instances

 PARTNER SOLUTIONS
 

 Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric

 Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud

Graph Tools

 Neo4j Fleet Manager A single control plane to manage all your DB instances

 Neo4j Bloom Easy graph visualization and exploration

Use CasesUse Cases: submenu

AI Systems

Back your LLMs with a Knowledge
 Graph for better business AI

Learn More 

Industries and Use Cases

Fraud detection, knowledge
 graphs, financial services, and more

All Use Cases 

Customer Success
 Stories

Case studies, customer videos,
 proof points, and more

All Customer Stories 

DevelopersDevelopers: submenu

Developer Center

Best practices, guides, tutorials, and downloads

Learn More 

GraphAcademy

Free online courses and certifications. Join the 100K+ Neo4j experts.

Learn More 

Developers

 Deployment Center Deploy Neo4j on any cloud or architecture

 DocumentationManuals for Neo4j products, Cypher, and drivers

 Developer Blog Deep dives into more technical Neo4j topics

 Community A global forum for online discussion

DATA SCIENTISTS

 Data Science DocumentationManuals for the Graph Data Science library

 Graph Data Science Home Learn what Neo4j offers for data science

 Get Started With Graph Data Science Download or get started in Sandbox today

 Data Science Community A global forum for data-driven professionals

AI Systems

LearnLearn: submenu

LEARN

 DocumentationManuals for Neo4j products, Cypher, and drivers

 GraphAcademyFree online courses and certifications

 Resource Library White papers, datasheets, and more

 Customer Success Stories Case studies, customer videos, proof points, and more

CONNECT

 Neo4j Events HubLive and on-demand events, training, webinars, and demos

 Neo4j Blog Announcements, guides, and best practices

 Neo4j Video Hub Covering graph databases, data science, analytics & AI

FEATURED EVENTS

Graphs + AI: Transform Your Data Into Knowledge
Learn more

Virtual Conference Dedicated to Graph + AI

Register Today

Pricing

Contact Us

Get Started Free

Blog Home 

Close

Blog Home

Developer

GenAI

News

Developer

GenAI

Knowledge Graph

Graphiti: Knowledge Graph Memory for an Agentic World

Daniel Chalef

Founder and CEO, Zep AI

March 24, 2025

 5 min read	

The real potential of AI goes beyond basic chatbots powered by retrieval-augmented generation (RAG). It’s about creating autonomous agents capable of independently solving tasks — from simple interactions to complex workflows. To do this effectively, agents need more than static retrieval; they need a dynamic memory that continuously integrates user interactions, enterprise data, and external knowledge.

Current RAG approaches struggle when data is updated frequently, limiting their effectiveness for agent-based systems. To solve this, Zep AI’s Graphiti framework introduces a flexible, real-time memory layer built on temporally aware knowledge graphs and stored in Neo4j.

Let’s break down how Graphiti works and compare it to query-focused summarization (QFS). In particular, we’ll look at the popular Microsoft Research GraphRAG implementation of QFS.

The Problem With Static Approaches

Microsoft’s approach to GraphRAG builds entity-centric knowledge graphs by extracting entities and relationships and grouping them into thematic clusters or “communities.” It relies on LLMs to precompute summaries of these communities. When handling queries, the Microsoft GraphRAG makes multiple LLM calls — first generating partial community-level responses, then combining them into a single comprehensive answer.

Their approach excels at providing detailed, context-rich responses from large static datasets. However, it’s less effective in scenarios where data frequently changes since updates can trigger extensive recomputation of the entire graph. Additionally, its multi-step summarization makes retrieval slow, often taking tens of seconds. This latency and lack of dynamic updates make this approach to GraphRAG unsuitable as a comprehensive and holistic memory for agentic applications.

Graphiti With Neo4j: Real-Time Dynamic Agent Memory

Graphiti helps overcome static RAG’s limitations with dynamic data. It’s a real-time, temporally-aware knowledge graph engine that incrementally processes incoming data, instantly updating entities, relationships, and communities without batch recomputation. Graphiti isn’t just another retrieval tool — it’s an ever-present source of context for agents, continuously available and updated.

Graphiti simultaneously handles chat histories, structured JSON data, and unstructured text. All data sources can feed into a single graph, or multiple graphs can coexist within the same Graphiti setup. This gives agents a unified, evolving view of the agent’s world — something traditional RAG systems fundamentally can’t provide.

Find Graphiti on GitHub.

Why Graphiti Works Better With Dynamic Data

Graphiti’s real-time incremental architecture is built for frequent updates. It continuously ingests new data episodes (events or messages), extracting and immediately resolving entities and relationships against existing nodes.

For an in-depth technical exploration of Graphiti and performance benchmarks, check out Zep: A Temporal Knowledge Graph Architecture for Agent Memory.

A key feature is Graphiti’s bi-temporal model, which tracks when an event occurred and when it was ingested. Every graph edge (or relationship) includes explicit validity intervals (t_valid, t_invalid). Graphiti uses semantic, keyword, and graph search to determine whether new knowledge conflicts with existing knowledge. When conflicts arise, Graphiti intelligently uses the temporal metadata to update or invalidate, but not discard, outdated information, preserving historical accuracy without large-scale recomputation.

This temporal model enables powerful historical queries, allowing users to reconstruct states of knowledge at precise moments or analyze how data evolves over time.

Fast Query Speeds: Instant Retrieval Without LLM Calls

Graphiti is built for speed. Zep’s own Graphiti implementation achieves extremely low-latency retrieval, returning results at a P95 latency of 300ms. This is enabled by a hybrid search approach that combines semantic embeddings, keyword (BM25) search, and direct graph traversal — avoiding any LLM calls during retrieval.

The use of vector and BM25 indexes offers near-constant time access to nodes and edges, regardless of graph size. This is made possible by Neo4j’s extensive support for both of these index types.

Graphiti’s query latency makes it ideal for real-time interactions, including voice applications.

Custom Entity Types: A Simple Ontology Implementation

Graphiti automatically builds an ontology based on incoming data, taking care to de-duplicate nodes and label edge relationships consistently. Beyond automatic ontology creation, Graphiti provides an intuitive method to define custom, domain-specific entities using familiar Pydantic models.

These custom entity types allow precise context extraction, greatly improving the quality of agent interactions. Example entity types might include:

Personalized user preferences and interests (like favorite restaurants, contacts, hobbies), along with standard attributes (name, birthdate, address)

Procedural memory, capturing instructions for actions

Domain-specific business objects (e.g., products, sales orders)

from pydantic import BaseModel, Field

class Customer(BaseModel):
 """A customer of the service"""
 name: str | None = Field(..., description="The name of the customer")
 email: str | None = Field(..., description="The email address of the customer")
 subscription_tier: str | None = Field(..., description="The customer's subscription level")

Graphiti automatically matches extracted entities to defined custom types. Custom entity types enhance an agent’s ability to recall knowledge accurately and improve contextual awareness, which is essential for consistent, relevant interactions.

Key Comparison

The following table shows a breakdown of the key characteristics of Graphiti compared to QFS-based GraphRAG.

Graph Memory Powering an Agentic Future

Graphiti represents a meaningful departure from traditional RAG methods, specifically because it was built from the ground up as a memory infrastructure for dynamic agentic systems. Graphiti offers incremental, real-time updates through its temporally aware knowledge graph. This design means engineers no longer need to recompute entire graphs when data changes. Instead, Graphiti incrementally integrates updates, resolves conflicts based on temporal metadata, and maintains an accurate historical state.

By removing the bottleneck of LLM-driven summarization at query time, Graphiti achieves practical latency levels that engineers require for interactive real-world applications. Its hybrid indexing system — combining semantic embeddings, keyword search, and graph traversal — allows rapid retrieval in near-constant time, independent of graph scale. With intuitive tools like custom entity types implemented through familiar structures such as Pydantic models, Graphiti addresses a significant capability gap in agent development, equipping engineers with a robust, performant, and genuinely dynamic memory layer.

Learn more about Zep and Graphiti.

Graphiti: Knowledge Graph Memory for an Agentic World was originally published in Neo4j Developer Blog on Medium, where people are continuing the conversation by highlighting and responding to this story.

 The Developer’s Guide to GraphRAG 

 Combine a knowledge graph with RAG to build a contextual, explainable GenAI app. Get started by learning the three main patterns. 

Learn to Build

agentic-ai

ai-agent

Knowledge Graph

retrieval-augmented-gen

Share Article

Explore

Knowledge Graph

Supply Chain & Logistics

Fraud Detection

Graph Visualization

AuraDB

Digital Twin

Related Articles

Agentic AI

Knowledge Graph

 From Data to Intelligence: Why Every Enterprise Needs an AI Knowledge Layer	

 4 min read	

Developer

 Building an AI Agent with Memory: Microsoft Agent Framework + Neo4j	

 17 min read	

GenAI

Healthcare

Knowledge Graph

 Why Healthcare CIOs Can’t Afford to Scale AI Without a Knowledge Graph Foundation	

 10 min read	

Cypher & GQL

Developer

 Hey LLM, you’re using OPTIONAL MATCH wrong. Here’s the Cypher that actually works.	

 9 min read	

GenAI

Knowledge Graph

Machine Learning

 What Is GraphRAG?	

 13 min read	

Healthcare

Knowledge Graph

 How Graph Intelligence Drives Breakthroughs in Science and Society	

 5 min read	

Build Intelligent Apps Easily

Transform your data into knowledge to build smart, accurate, and adaptive applications.
Start Building

Products

Neo4j AuraDB

Neo4j Graph Database

Neo4j Graph Analytics

Neo4j Graph Data Science

Neo4j Fleet Manager

Neo4j Bloom

Cypher Query Language

Neo4j GraphQL

Pricing

Neo4j Community Edition

Use Cases

AI Systems

Generative AI

Knowledge Graphs

Pattern Matching

Industries & Use Cases

Case Studies

Developers

Developer Home

Documentation

Deployment Center

Developer Blog

Community

Virtual Events

GraphAcademy

Release Notes

Data Scientists

Graph Data Science Home

Data Science Documentation

Get Started with Graph Data Science

Data Science Community

GraphAcademy for Data Science

Learn

Resource Library

Neo4j Blog

GraphAcademy

Research Center

Case Studies

Neo4j Video Hub

Neo4j Events Hub

GraphSummit

NODES

Webinars

GraphRAG

Partners

Find a Partner

Become a Partner

Solution Partners

OEM Partners

Technology Partners

Partner Portal Login

Company

About Us

Newsroom

Awards and Honors

Graphs4Good

Careers

Culture

Leadership

Support

Trust Center

Contact Us →

US: 1-855-636-4532

Sweden: +46 171 480 113

UK: +44 20 3868 3223

France: +33 (0) 1 88 46 13 20

Singapore: +65 6859 0336

Australia: +61 2 8395 2895

Social Networks

© 2026 Neo4j, Inc.
 

Terms | Privacy Notice | Sitemap
Anti-Corruption Policy

 ©2026 Neo4j, Inc., Neo Technology®, Neo4j®, Cypher®, Neo4j Bloom™, 
 Neo4j Graph Data Science Library™, Neo4j® Aura™, 
 and Neo4j® AuraDB™ are registered trademarks or a trademark of Neo4j, Inc. 
 All other marks are owned by their respective companies.
 

 Contact Us

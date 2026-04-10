---
title: Introduction
source_url: https://turbopuffer.com/docs
final_url: https://turbopuffer.com/docs
status: 200
content_type: text/html; charset=utf-8
topics: [Serverless Object-Storage Vector DBs (Turbopuffer 등)]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:54.359004+00:00
---

# Introduction

## 원본 URL

https://turbopuffer.com/docs

## 추출 본문

Introduction

Query prices reduced by up to 94%We've reduced query prices by up to 94%

Navigation

turbopuffer

DocsPricingCustomersBlogTalk to usLog inSign up

Introduction

Architecture

Concepts

Guarantees

Tradeoffs

Limits

Regions

Roadmap & Changelog

Security

Encryption

Backups

Private Networking

Performance

Pinning

Guides

Quickstart

Vector Search

Full-Text Search

Hybrid Search

Testing

Permissions

API

Auth & Encoding

Write

Query

Namespace metadata

Export

Warm cache

List namespaces

Delete namespace

Recall

Introduction

 ╔═ turbopuffer ════════════════════════════╗
╔════════════╗ ║ ║░
║ ║░ ║ ┏━━━━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━━━┓ ║░
║ client ║░───API──▶║ ┃ Memory/ ┃────▶┃ Object ┃ ║░
║ ║░ ║ ┃ SSD Cache ┃ ┃ Storage (S3) ┃ ║░
╚════════════╝░ ║ ┗━━━━━━━━━━━━━━━┛ ┗━━━━━━━━━━━━━━┛ ║░
 ░░░░░░░░░░░░░░ ║ ║░
 ╚══════════════════════════════════════════╝░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

 ╔════════════╗
 ║ client ║░
 ╚════════════╝░
 ░░░░░║░░░░░░░░
 ▼
╔═ turbopuffer ════════════╗
║ ┏━━━━━━━━━━━━━━━━━━━━┓ ║░
║ ┃ Memory/SSD ┃ ║░
║ ┃ Cache ┃ ║░
║ ┗━━━━━━━━┳━━━━━━━━━━━┛ ║░
║ ▼ ║░
║ ┏━━━━━━━━━━━━━━━━━━━━┓ ║░
║ ┃ Object Storage ┃ ║░
║ ┃ (S3) ┃ ║░
║ ┗━━━━━━━━━━━━━━━━━━━━┛ ║░
╚══════════════════════════╝░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░

turbopuffer is a fast search engine that combines vector and full-text search
using object storage, making all your data easily searchable.

Using only object storage for state and NVMe SSD with memory cache for compute,
turbopuffer scales horizontally to handle billions of documents.

The system caches only actively searched data while keeping the rest in low-cost
object storage, offering competitive pricing. Cold queries for 1 million
vectors take p90=444ms, while warm
queries are just p50=8ms.
This architecture means it's as fast as in-memory search engines when cached, but far
cheaper to run.

Storing data in cache and object storage costs less than traditional replicated
disk systems, even for frequently accessed data.

turbopuffer is focused on first-stage retrieval to efficiently narrow millions
of documents down to tens or hundreds. While it may have fewer features than
traditional search engines, this streamlined approach enables higher quality,
more maintainable search applications that you can customize in your preferred
programming language. See Hybrid Search to get started.

To get started with turbopuffer, see the quickstart guide.

For more technical details, see Architecture,
Guarantees, and Tradeoffs.

copy page

CompanyJobsPricingStorePress & mediaSystem status

Support
SlackDocsEmailSales

Follow
BlogRSSEvents

© 2026 turbopuffer Inc.
Terms of serviceData Processing AgreementPrivacy PolicySecurity & Compliance

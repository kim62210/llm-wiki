---
title: Semantic conventions for generative AI systems | OpenTelemetry
source_url: https://opentelemetry.io/docs/specs/semconv/gen-ai
final_url: https://opentelemetry.io/docs/specs/semconv/gen-ai/
status: 200
content_type: text/html; charset=UTF-8
topics: [OpenTelemetry GenAI Semantic Conventions]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:00.514408+00:00
---

# Semantic conventions for generative AI systems | OpenTelemetry

## 원본 URL

https://opentelemetry.io/docs/specs/semconv/gen-ai

## 추출 본문

Semantic conventions for generative AI systems | OpenTelemetry
OpenTelemetry

Docs

Ecosystem

Status

Community

Training

Blog

EnglishEN
বাংলা

English

Español

Français

日本語

Polski

Português

Română

Українська

中文

Light

Dark

Auto

Semantic conventions 1.40.0
Registry
Attributes
Android

App

Artifact

Aspnetcore

AWS

Azure

Browser

Cassandra

CICD

Client

Cloud

CloudEvents

CloudFoundry

Code

Container

CPU

CPython

DB

Deployment

Destination

Device

Disk

DNS

Dotnet

Elasticsearch

Enduser

Error

Event

Exception

Faas

Feature flag

File

GCP

Gen AI

Geo

Go

GraphQL

Hardware

Heroku

Host

HTTP

iOS

JSONRPC

JVM

K8s

Linux

Log

Mainframe

MCP

Messaging

Network

NFS

NodeJS

OCI

ONC RPC

OpenAI

Openshift

OpenTracing

Oracle cloud

OracleDB

OS

OTel

Peer

Pprof

Process

Profile

RPC

Security rule

Server

Service

Session

SignalR

Source

System

Telemetry

Test

Thread

TLS

URL

User

User agent

V8js

VCS

Webengine

zOS

Entities
Android

App

AWS

Browser

CICD

Cloud

CloudFoundry

Container

Deployment

Device

Faas

GCP

Heroku

Host

K8s

Openshift

OS

OTel

Process

Service

Telemetry

VCS

Webengine

zOS

General
Attribute requirement levels

Attributes

Events

Logs

Metric requirement levels

Metrics

Naming

Profiles

Recording errors

Semantic convention groups

Session

Trace

Tracing compatibility

.NET
ASP.NET Core

DNS

HTTP

HTTP request and connection spans

Kestrel

SignalR

App
Events

Azure
Events

Browser
Events

CICD
Logs

Metrics

Spans

CLI programs
Spans

Cloud providers
AWS SDK

CloudEvents
Spans

Database
Cassandra

Cosmos DB

CouchDB

DynamoDB

Elasticsearch

Exceptions

HBase

MariaDB

Metrics

MongoDB

MySQL

Oracle Database

PostgreSQL

Redis

Spans

SQL

SQL Server

DNS
Metrics

Exceptions
Logs

Spans

FaaS
AWS Lambda

Metrics

Spans

Feature flags
Events

Generative AI
Agent spans

Anthropic

AWS Bedrock

Azure AI Inference

Events

LLM call examples

Metrics

Model Context Protocol

OpenAI

Spans

GraphQL
GraphQL server

Hardware
Battery

CPU

Disk Controller

Enclosure

Fan

GPU

Logical Disk

Memory

Metrics

Network

Physical Disk

Physical host

Power Supply

Tape Drive

Temperature

Voltage

How to write conventions
Resource and Entities

Status Metrics

T-shaped Signals

HTTP
Exceptions

Metrics

Spans

Messaging
AWS SNS

AWS SQS

Azure

Google Cloud Pub/Sub

Kafka

Metrics

RabbitMQ

RocketMQ

Spans

Mobile
Events

NFS
NFS

Non-normative
Code attributes migration

Compatibility
AWS

gRPC

Database migration

Generating semantic convention libraries

HTTP migration

K8s attributes

K8s migration

Naming known exceptions

Recommended vs Opt-In CPU Metrics

RPC migration

System semantic conventions: instrumentation design philosophy

System use cases

Object stores
S3

OpenTelemetry SDK
SDK Metrics

Resource
Android

Browser

CICD

Cloud

Cloud provider
AWS
ECS

EKS

Logs

GCP
Google Cloud AppHub

Google Cloud Run

Google Compute Engine

Heroku

CloudFoundry

Container

Deployment

Device

FaaS

Host

Kubernetes
Openshift

Operating system

Process

Service

Webengine

z/OS software

RPC
Connect

Dubbo

Exceptions

gRPC

JSON-RPC

Metrics

Spans

Runtime environment
.NET

CPython

Go

JVM

Node.js

V8 JS engine

System
Container

Kubernetes

OpenShift

OS process

System

URL

 View Markdown View page source Edit this page Create child page Create documentation issue Create project issue

Docs

Specs

Semantic conventions 1.40.0

Generative AI

Semantic conventions for generative AI systems

Status: Development

Important

Existing GenAI instrumentations that are using
v1.36.0 of this document
(or prior):

SHOULD NOT change the version of the GenAI conventions that they emit by default.
Conventions include, but are not limited to, attributes, metric, span and event names,
span kind and unit of measure.

SHOULD introduce an environment variable 
OTEL_SEMCONV_STABILITY_OPT_IN

as a comma-separated list of category-specific values. The list of values
includes:

gen_ai_latest_experimental
 - emit the latest experimental version of
GenAI conventions (supported by the instrumentation) and do not emit the
old one (v1.36.0 or prior).

The default behavior is to continue emitting whatever version of the GenAI
conventions the instrumentation was emitting (1.36.0 or prior).

This transition plan will be updated to include stable version before the
GenAI conventions are marked as stable.

Semantic conventions for Generative AI operations are defined for the following signals:

Events: Semantic Conventions for Generative AI inputs and outputs - events.

Metrics: Semantic Conventions for Generative AI operations - metrics.

Model spans: Semantic Conventions for Generative AI model operations - spans.

Agent spans: Semantic Conventions for Generative AI agent operations - spans.

Technology specific semantic conventions are defined for the following GenAI system:

Anthropic: Semantic Conventions for Anthropic.

Azure AI Inference: Semantic Conventions for Azure AI Inference.

AWS Bedrock: Semantic Conventions for AWS Bedrock.

OpenAI: Semantic Conventions for OpenAI.

See also:

Model Context Protocol: Semantic Conventions for MCP

Semantic Conventions for GenAI agent and framework spans

Semantic conventions for Anthropic client operations

Semantic conventions for AWS Bedrock operations

Semantic conventions for Azure AI Inference client operations

Semantic conventions for Generative AI events

LLM call examples

Semantic conventions for generative AI metrics

Semantic conventions for Model Context Protocol (MCP)

Semantic conventions for OpenAI client operations

Semantic conventions for generative client AI spans

Feedback

Was this page helpful?
YesNo
Thank you. Your feedback is appreciated!

Please let us know how we can improve this page. Your feedback is appreciated!

©
2019–present
OpenTelemetry Authors | Docs CC BY 4.0All Rights Reserved

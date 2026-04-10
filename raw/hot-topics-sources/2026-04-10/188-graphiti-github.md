---
title: GitHub - getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents · GitHub
source_url: https://github.com/getzep/graphiti
final_url: https://github.com/getzep/graphiti
status: 200
content_type: text/html; charset=utf-8
topics: [Zep / Graphiti Temporal Knowledge Graph Memory]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:52.521666+00:00
---

# GitHub - getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents · GitHub

## 원본 URL

https://github.com/getzep/graphiti

## 추출 본문

GitHub - getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents · GitHub

Skip to content

Navigation Menu
Toggle navigation

 Sign in
 
Appearance settings

Platform

AI CODE CREATION

GitHub CopilotWrite better code with AI

GitHub SparkBuild and deploy intelligent apps

GitHub ModelsManage and compare prompts

MCP RegistryNewIntegrate external tools

DEVELOPER WORKFLOWS

ActionsAutomate any workflow

CodespacesInstant dev environments

IssuesPlan and track work

Code ReviewManage code changes

APPLICATION SECURITY

GitHub Advanced SecurityFind and fix vulnerabilities

Code securitySecure your code as you build

Secret protectionStop leaks before they start

EXPLORE
Why GitHub

Documentation

Blog

Changelog

Marketplace

View all features

Solutions

BY COMPANY SIZE
Enterprises

Small and medium teams

Startups

Nonprofits

BY USE CASE
App Modernization

DevSecOps

DevOps

CI/CD

View all use cases

BY INDUSTRY
Healthcare

Financial services

Manufacturing

Government

View all industries

View all solutions

Resources

EXPLORE BY TOPIC
AI

Software Development

DevOps

Security

View all topics

EXPLORE BY TYPE
Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES
Documentation

Customer support

Community forum

Trust center

Partners

View all resources

Open Source

COMMUNITY

GitHub SponsorsFund open source developers

PROGRAMS
Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES
Topics

Trending

Collections

Enterprise

ENTERPRISE SOLUTIONS

Enterprise platformAI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced SecurityEnterprise-grade security features

Copilot for BusinessEnterprise-grade AI features

Premium SupportEnterprise-grade 24/7 support

Pricing

Search or jump to...

Search code, repositories, users, issues, pull requests...

 Search
 

Clear

Search syntax tips

 Provide feedback
 

We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted

 Cancel
 Submit feedback

 Saved searches
 

Use saved searches to filter your results more quickly

Name

Query

 To see all available qualifiers, see our documentation.
 

 Cancel
 Create saved search

 Sign in
 

 Sign up
 
Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

 getzep
/graphitiPublic

Notifications
You must be signed in to change notification settings

Fork
 2.5k

 Star
24.7k

Code

Issues207

Pull requests137

Actions

Security and quality1

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Security and quality

 Insights

getzep/graphiti

main

BranchesTags

Go to file

Code
Open more actions menu

Folders and files
NameName
Last commit message

Last commit date

Latest commit

History
810 Commits

810 Commits

.github

.github

examples

examples

graphiti_core

graphiti_core

images

images

mcp_server

mcp_server

server

server

signatures/version1

signatures/version1

spec

spec

tests

tests

.env.example

.env.example

.gitignore

.gitignore

AGENTS.md

AGENTS.md

CLAUDE.md

CLAUDE.md

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

Dockerfile

Dockerfile

LICENSE

LICENSE

Makefile

Makefile

OTEL_TRACING.md

OTEL_TRACING.md

README.md

README.md

SECURITY.md

SECURITY.md

Zep-CLA.md

Zep-CLA.md

conftest.py

conftest.py

depot.json

depot.json

docker-compose.test.yml

docker-compose.test.yml

docker-compose.yml

docker-compose.yml

ellipsis.yaml

ellipsis.yaml

py.typed

py.typed

pyproject.toml

pyproject.toml

pytest.ini

pytest.ini

uv.lock

uv.lock

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

Security

Graphiti

Build Temporal Context Graphs for AI Agents

Note

We're Hiring! Build context graphs that power reliable, personalized, fast production AI agents.
Come build with us — we're hiring Engineers and Developer Relations folks. View open roles.

⭐ Help us reach more developers and grow the Graphiti community. Star this repo!

Tip

Check out the new MCP server for Graphiti! Give Claude, Cursor, and other MCP clients powerful
context graph-based memory with temporal awareness.

Graphiti is a framework for building and querying temporal context graphs for AI agents. Unlike static knowledge graphs,
Graphiti's context graphs track how facts change over time, maintain provenance to source data, and support both
prescribed and learned ontology — making them purpose-built for agents operating on evolving, real-world data.

Unlike traditional retrieval-augmented generation (RAG) methods, Graphiti continuously integrates user interactions,
structured and unstructured enterprise data, and external information into a coherent, queryable graph. The framework
supports incremental data updates, efficient retrieval, and precise historical queries without requiring complete graph
recomputation, making it suitable for developing interactive, context-aware AI applications.

Use Graphiti to:

Build context graphs that evolve with every interaction — tracking what's true now and what was true before.

Give agents rich, structured context instead of flat document chunks or raw chat history.

Query across time, meaning, and relationships with hybrid retrieval (semantic + keyword + graph traversal).

What is a Context Graph?

A context graph is a temporal graph of entities, relationships, and facts — like "Kendra loves Adidas shoes (as of
March 2026)." Unlike traditional knowledge graphs, each fact in a context graph has a validity window: when it became
true, and when (if ever) it was superseded. Entities evolve over time with updated summaries. Everything traces back to
episodes — the raw data that produced it.

What makes Graphiti unique is its ability to autonomously build context graphs from unstructured and structured data,
handling changing relationships while preserving full temporal history.

A context graph contains:
ComponentWhat it storesEntities (nodes)People, products, policies, concepts — with summaries that evolve over timeFacts / Relationships (edges)Triplets (Entity → Relationship → Entity) with temporal validity windowsEpisodes (provenance)Raw data as ingested — the ground truth stream. Every derived fact traces back hereCustom Types (ontology)Developer-defined entity and edge types via Pydantic models

Graphiti and Zep

Graphiti is the open-source temporal context graph engine at the core of
Zep's context infrastructure for AI agents. Zep manages context graphs at scale, providing
governed, low-latency context retrieval and assembly for production agent deployments.

Using Graphiti, we've demonstrated Zep is
the State of the Art in Agent Memory.

Read our paper: Zep: A Temporal Knowledge Graph Architecture for Agent Memory.

We're excited to open-source Graphiti, believing its potential as a context graph engine reaches far beyond memory
applications.

Zep vs Graphiti

AspectZepGraphitiWhat they areManaged context graph infrastructure for AI agentsOpen-source temporal context graph engineContext graphsManages vast numbers of per-user/entity context graphs with governanceBuild and query individual context graphsUser & conversation managementBuilt-in users, threads, and message storageBuild your ownRetrieval & performancePre-configured, production-ready retrieval with sub-200ms performance at scaleCustom implementation required; performance depends on your setupDeveloper toolsDashboard with graph visualization, debug logs, API logs; SDKs for Python, TypeScript, and GoBuild your own toolsEnterprise featuresSLAs, support, security guaranteesSelf-managedDeploymentFully managed or in your cloudSelf-hosted only

When to choose which

Choose Zep if you want a turnkey, enterprise-grade platform with security, performance, and support baked in.

Choose Graphiti if you want a flexible OSS core and you're comfortable building/operating the surrounding system.

Why Graphiti?

Traditional RAG approaches often rely on batch processing and static data summarization, making them inefficient for
frequently changing data. Graphiti addresses these challenges by providing:

Temporal Fact Management: Facts have validity windows. When information changes, old facts are
invalidated — not deleted. Query what's true now, or what was true at any point in time.

Episodes & Provenance: Every entity and relationship traces back to the episodes (raw data) that produced it.
Full lineage from derived fact to source.

Prescribed & Learned Ontology: Define entity and edge types upfront via Pydantic models (prescribed), or let
structure emerge from your data (learned). Start simple, evolve as patterns appear.

Incremental Graph Construction: New data integrates immediately without batch recomputation. The graph evolves
in real-time as episodes are ingested.

Hybrid Retrieval: Combines semantic embeddings, keyword (BM25), and graph traversal for low-latency,
high-precision queries without reliance on LLM summarization.

Scalability: Efficiently manages large datasets with parallel processing, pluggable graph backends, suitable
for enterprise workloads.

Graphiti vs. GraphRAG

AspectGraphRAGGraphitiPrimary UseStatic document summarizationDynamic, evolving context for agentsData HandlingBatch-oriented processingContinuous, incremental updatesKnowledge StructureEntity clusters & community summariesTemporal context graph — entities, facts with validity windows, episodes, communitiesRetrieval MethodSequential LLM summarizationHybrid semantic, keyword, and graph-based searchAdaptabilityLowHighTemporal HandlingBasic timestamp trackingExplicit bi-temporal tracking with automatic fact invalidationContradiction HandlingLLM-driven summarization judgmentsAutomatic fact invalidation with temporal history preservedQuery LatencySeconds to tens of secondsTypically sub-second latencyCustom Entity TypesNoYes, customizable via Pydantic modelsScalabilityModerateHigh, optimized for large datasets
Graphiti is specifically designed to address the challenges of dynamic and frequently updated datasets, making it
particularly suitable for applications requiring real-time interaction and precise historical queries.

Installation

Requirements:

Python 3.10 or higher

Neo4j 5.26 / FalkorDB 1.1.2 / Kuzu 0.11.2 / Amazon Neptune Database Cluster or Neptune Analytics Graph + Amazon
OpenSearch Serverless collection (serves as the full text search backend)

OpenAI API key (Graphiti defaults to OpenAI for LLM inference and embedding)

Important

Graphiti works best with LLM services that support Structured Output (such as OpenAI and Gemini).
Using other services may result in incorrect output schemas and ingestion failures. This is particularly
problematic when using smaller models.

Optional:

Google Gemini, Anthropic, or Groq API key (for alternative LLM providers)

Tip

The simplest way to install Neo4j is via Neo4j Desktop. It provides a user-friendly
interface to manage Neo4j instances and databases.
Alternatively, you can use FalkorDB on-premises via Docker and instantly start with the quickstart example:

docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest

pip install graphiti-core

or

uv add graphiti-core

Installing with FalkorDB Support

If you plan to use FalkorDB as your graph database backend, install with the FalkorDB extra:

pip install graphiti-core[falkordb]

# or with uv
uv add graphiti-core[falkordb]

Installing with Kuzu Support

If you plan to use Kuzu as your graph database backend, install with the Kuzu extra:

pip install graphiti-core[kuzu]

# or with uv
uv add graphiti-core[kuzu]

Installing with Amazon Neptune Support

If you plan to use Amazon Neptune as your graph database backend, install with the Amazon Neptune extra:

pip install graphiti-core[neptune]

# or with uv
uv add graphiti-core[neptune]

You can also install optional LLM providers as extras:

# Install with Anthropic support
pip install graphiti-core[anthropic]

# Install with Groq support
pip install graphiti-core[groq]

# Install with Google Gemini support
pip install graphiti-core[google-genai]

# Install with multiple providers
pip install graphiti-core[anthropic,groq,google-genai]

# Install with FalkorDB and LLM providers
pip install graphiti-core[falkordb,anthropic,google-genai]

# Install with Amazon Neptune
pip install graphiti-core[neptune]

Default to Low Concurrency; LLM Provider 429 Rate Limit Errors

Graphiti's ingestion pipelines are designed for high concurrency. By default, concurrency is set low to avoid LLM
Provider 429 Rate Limit Errors. If you find Graphiti slow, please increase concurrency as described below.

Concurrency controlled by the 
SEMAPHORE_LIMIT
 environment variable. By default, 
SEMAPHORE_LIMIT
 is set to 
10

concurrent operations to help prevent 
429
 rate limit errors from your LLM provider. If you encounter such errors, try
lowering this value.

If your LLM provider allows higher throughput, you can increase 
SEMAPHORE_LIMIT
 to boost episode ingestion
performance.

Quick Start

Important

Graphiti defaults to using OpenAI for LLM inference and embedding. Ensure that an 
OPENAI_API_KEY
 is set in your
environment.
Support for Anthropic and Groq LLM inferences is available, too. Other LLM providers may be supported via OpenAI
compatible APIs.

For a complete working example, see the Quickstart Example in the examples directory.
The quickstart demonstrates:

Connecting to a Neo4j, Amazon Neptune, FalkorDB, or Kuzu database

Initializing Graphiti indices and constraints

Adding episodes to the graph (both text and structured JSON)

Searching for relationships (edges) using hybrid search

Reranking search results using graph distance

Searching for nodes using predefined search recipes

The example is fully documented with clear explanations of each functionality and includes a comprehensive README with
setup instructions and next steps.

Running with Docker Compose

You can use Docker Compose to quickly start the required services:

Neo4j Docker:

docker compose up

This will start the Neo4j Docker service and related components.

FalkorDB Docker:

docker compose --profile falkordb up

This will start the FalkorDB Docker service and related components.

MCP Server

The 
mcp_server
 directory contains a Model Context Protocol (MCP) server implementation for Graphiti. This server
allows AI assistants to interact with Graphiti's context graph capabilities through the MCP protocol.

Key features of the MCP server include:

Episode management (add, retrieve, delete)

Entity management and relationship handling

Semantic and hybrid search capabilities

Group management for organizing related data

Graph maintenance operations

The MCP server can be deployed using Docker with Neo4j, making it easy to integrate Graphiti into your AI assistant
workflows.

For detailed setup instructions and usage examples, see the MCP server README.

REST Service

The 
server
 directory contains an API service for interacting with the Graphiti API. It is built using FastAPI.

Please see the server README for more information.

Optional Environment Variables

In addition to the Neo4j and OpenAi-compatible credentials, Graphiti also has a few optional environment variables.
If you are using one of our supported models, such as Anthropic or Voyage models, the necessary environment variables
must be set.

Database Configuration

Database names are configured directly in the driver constructors:

Neo4j: Database name defaults to 
neo4j
 (hardcoded in Neo4jDriver)

FalkorDB: Database name defaults to 
default_db
 (hardcoded in FalkorDriver)

As of v0.17.0, if you need to customize your database configuration, you can instantiate a database driver and pass it
to the Graphiti constructor using the 
graph_driver
 parameter.

Neo4j with Custom Database Name

fromgraphiti_coreimportGraphitifromgraphiti_core.driver.neo4j_driverimportNeo4jDriver# Create a Neo4j driver with custom database namedriver=Neo4jDriver(
 uri="bolt://localhost:7687",
 user="neo4j",
 password="password",
 database="my_custom_database"# Custom database name
)

# Pass the driver to Graphitigraphiti=Graphiti(graph_driver=driver)

FalkorDB with Custom Database Name

fromgraphiti_coreimportGraphitifromgraphiti_core.driver.falkordb_driverimportFalkorDriver# Create a FalkorDB driver with custom database namedriver=FalkorDriver(
 host="localhost",
 port=6379,
 username="falkor_user", # Optionalpassword="falkor_password", # Optionaldatabase="my_custom_graph"# Custom database name
)

# Pass the driver to Graphitigraphiti=Graphiti(graph_driver=driver)

Kuzu

fromgraphiti_coreimportGraphitifromgraphiti_core.driver.kuzu_driverimportKuzuDriver# Create a Kuzu driverdriver=KuzuDriver(db="/tmp/graphiti.kuzu")

# Pass the driver to Graphitigraphiti=Graphiti(graph_driver=driver)

Amazon Neptune

fromgraphiti_coreimportGraphitifromgraphiti_core.driver.neptune_driverimportNeptuneDriver# Create a Neptune driverdriver=NeptuneDriver(
 host='<NEPTUNE_ENDPOINT>',
 aoss_host='<AMAZON_OPENSEARCH_SERVERLESS_HOST>',
 port=8182, # Optional, defaults to 8182aoss_port=443, # Optional, defaults to 443
)

# Pass the driver to Graphitigraphiti=Graphiti(graph_driver=driver)

Contributing a new graph backend? See Adding a graph driver.

Using Graphiti with Azure OpenAI

Graphiti supports Azure OpenAI for both LLM inference and embeddings using Azure's OpenAI v1 API compatibility layer.

Quick Start

fromopenaiimportAsyncOpenAIfromgraphiti_coreimportGraphitifromgraphiti_core.llm_client.azure_openai_clientimportAzureOpenAILLMClientfromgraphiti_core.llm_client.configimportLLMConfigfromgraphiti_core.embedder.azure_openaiimportAzureOpenAIEmbedderClient# Initialize Azure OpenAI client using the standard OpenAI client# with Azure's v1 API endpointazure_client=AsyncOpenAI(
 base_url="https://your-resource-name.openai.azure.com/openai/v1/",
 api_key="your-api-key",
)

# Create LLM and Embedder clientsllm_client=AzureOpenAILLMClient(
 azure_client=azure_client,
 config=LLMConfig(model="gpt-5-mini", small_model="gpt-5-mini") # Your Azure deployment name
)
embedder_client=AzureOpenAIEmbedderClient(
 azure_client=azure_client,
 model="text-embedding-3-small"# Your Azure embedding deployment name
)

# Initialize Graphiti with Azure OpenAI clientsgraphiti=Graphiti(
 "bolt://localhost:7687",
 "neo4j",
 "password",
 llm_client=llm_client,
 embedder=embedder_client,
)

# Now you can use Graphiti with Azure OpenAI

Key Points:

Use the standard 
AsyncOpenAI
 client with Azure's v1 API endpoint format:

https://your-resource-name.openai.azure.com/openai/v1/

The deployment names (e.g., 
gpt-5-mini
, 
text-embedding-3-small
) should match your Azure OpenAI deployment names

See 
examples/azure-openai/
 for a complete working example

Make sure to replace the placeholder values with your actual Azure OpenAI credentials and deployment names.

Using Graphiti with Google Gemini

Graphiti supports Google's Gemini models for LLM inference, embeddings, and cross-encoding/reranking. To use Gemini,
you'll need to configure the LLM client, embedder, and the cross-encoder with your Google API key.

Install Graphiti:

uv add "graphiti-core[google-genai]"# or

pip install "graphiti-core[google-genai]"

fromgraphiti_coreimportGraphitifromgraphiti_core.llm_client.gemini_clientimportGeminiClient, LLMConfigfromgraphiti_core.embedder.geminiimportGeminiEmbedder, GeminiEmbedderConfigfromgraphiti_core.cross_encoder.gemini_reranker_clientimportGeminiRerankerClient# Google API key configurationapi_key="<your-google-api-key>"# Initialize Graphiti with Gemini clientsgraphiti=Graphiti(
 "bolt://localhost:7687",
 "neo4j",
 "password",
 llm_client=GeminiClient(
 config=LLMConfig(
 api_key=api_key,
 model="gemini-2.0-flash"
 )
 ),
 embedder=GeminiEmbedder(
 config=GeminiEmbedderConfig(
 api_key=api_key,
 embedding_model="embedding-001"
 )
 ),
 cross_encoder=GeminiRerankerClient(
 config=LLMConfig(
 api_key=api_key,
 model="gemini-2.5-flash-lite"
 )
 )
)

# Now you can use Graphiti with Google Gemini for all components

The Gemini reranker uses the 
gemini-2.5-flash-lite
 model by default, which is optimized for
cost-effective and low-latency classification tasks. It uses the same boolean classification approach as the OpenAI
reranker, leveraging Gemini's log probabilities feature to rank passage relevance.

Using Graphiti with Ollama (Local LLM)

Graphiti supports Ollama for running local LLMs and embedding models via Ollama's OpenAI-compatible API. This is ideal
for privacy-focused applications or when you want to avoid API costs.

Note: Use 
OpenAIGenericClient
 (not 
OpenAIClient
) for Ollama and other OpenAI-compatible providers like LM
Studio. The 
OpenAIGenericClient
 is optimized for local models with a higher default max token limit (16K vs 8K) and
full support for structured outputs.

Install the models:

ollama pull deepseek-r1:7b # LLM
ollama pull nomic-embed-text # embeddings

fromgraphiti_coreimportGraphitifromgraphiti_core.llm_client.configimportLLMConfigfromgraphiti_core.llm_client.openai_generic_clientimportOpenAIGenericClientfromgraphiti_core.embedder.openaiimportOpenAIEmbedder, OpenAIEmbedderConfigfromgraphiti_core.cross_encoder.openai_reranker_clientimportOpenAIRerankerClient# Configure Ollama LLM clientllm_config=LLMConfig(
 api_key="ollama", # Ollama doesn't require a real API key, but some placeholder is neededmodel="deepseek-r1:7b",
 small_model="deepseek-r1:7b",
 base_url="http://localhost:11434/v1", # Ollama's OpenAI-compatible endpoint
)

llm_client=OpenAIGenericClient(config=llm_config)

# Initialize Graphiti with Ollama clientsgraphiti=Graphiti(
 "bolt://localhost:7687",
 "neo4j",
 "password",
 llm_client=llm_client,
 embedder=OpenAIEmbedder(
 config=OpenAIEmbedderConfig(
 api_key="ollama", # Placeholder API keyembedding_model="nomic-embed-text",
 embedding_dim=768,
 base_url="http://localhost:11434/v1",
 )
 ),
 cross_encoder=OpenAIRerankerClient(client=llm_client, config=llm_config),
)

# Now you can use Graphiti with local Ollama models

Ensure Ollama is running (
ollama serve
) and that you have pulled the models you want to use.

Documentation

Guides and API documentation.

Quick Start

Building an agent with LangChain's LangGraph and Graphiti

Telemetry

Graphiti collects anonymous usage statistics to help us understand how the framework is being used and improve it for
everyone. We believe transparency is important, so here's exactly what we collect and why.

What We Collect

When you initialize a Graphiti instance, we collect:

Anonymous identifier: A randomly generated UUID stored locally in 
~/.cache/graphiti/telemetry_anon_id

System information: Operating system, Python version, and system architecture

Graphiti version: The version you're using

Configuration choices:

LLM provider type (OpenAI, Azure, Anthropic, etc.)

Database backend (Neo4j, FalkorDB, Kuzu, Amazon Neptune Database or Neptune Analytics)

Embedder provider (OpenAI, Azure, Voyage, etc.)

What We Don't Collect

We are committed to protecting your privacy. We never collect:

Personal information or identifiers

API keys or credentials

Your actual data, queries, or graph content

IP addresses or hostnames

File paths or system-specific information

Any content from your episodes, nodes, or edges

Why We Collect This Data

This information helps us:

Understand which configurations are most popular to prioritize support and testing

Identify which LLM and database providers to focus development efforts on

Track adoption patterns to guide our roadmap

Ensure compatibility across different Python versions and operating systems

By sharing this anonymous information, you help us make Graphiti better for everyone in the community.

View the Telemetry Code

The Telemetry code may be found here.

How to Disable Telemetry

Telemetry is opt-out and can be disabled at any time. To disable telemetry collection:

Option 1: Environment Variable

export GRAPHITI_TELEMETRY_ENABLED=false

Option 2: Set in your shell profile

# For bash users (~/.bashrc or ~/.bash_profile)echo'export GRAPHITI_TELEMETRY_ENABLED=false'>>~/.bashrc

# For zsh users (~/.zshrc)echo'export GRAPHITI_TELEMETRY_ENABLED=false'>>~/.zshrc

Option 3: Set for a specific Python session

importosos.environ['GRAPHITI_TELEMETRY_ENABLED'] ='false'# Then initialize Graphiti as usualfromgraphiti_coreimportGraphitigraphiti=Graphiti(...)

Telemetry is automatically disabled during test runs (when 
pytest
 is detected).

Technical Details

Telemetry uses PostHog for anonymous analytics collection

All telemetry operations are designed to fail silently - they will never interrupt your application or affect Graphiti
functionality

The anonymous ID is stored locally and is not tied to any personal information

Contributing

We encourage and appreciate all forms of contributions, whether it's code, documentation, addressing GitHub Issues, or
answering questions in the Graphiti Discord channel. For detailed guidelines on code contributions, please refer
to CONTRIBUTING.

Support

Join the Zep Discord server and make your way to the #Graphiti channel!

About

 Build Real-Time Knowledge Graphs for AI Agents
 

help.getzep.com/graphiti

Topics

 graph

 agents

 rag

 llms

Resources

 Readme

License

 Apache-2.0 license
 

Code of conduct

 Code of conduct
 

Contributing

 Contributing
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

24.7k
 stars

Watchers

155
 watching

Forks

2.5k
 forks

 Report repository

Releases
 193

mcp-v1.0.2 - Security: Require graphiti-core>=0.28.2
 Latest

Mar 11, 2026

+ 192 releases

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.3%

Other0.7%

Footer

 © 2026 GitHub, Inc.
 

Footer navigation

Terms

Privacy

Security

Status

Community

Docs

Contact

 Manage cookies
 

 Do not share my personal information
 

 You can’t perform that action at this time.

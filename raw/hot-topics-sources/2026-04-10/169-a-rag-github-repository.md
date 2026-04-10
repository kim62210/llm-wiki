---
title: GitHub - Ayanami0730/arag: A-RAG: Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces. State-of-the-art RAG framework with keyword, semantic, and chunk read tools for multi-hop QA. · GitHub
source_url: https://github.com/Ayanami0730/arag
final_url: https://github.com/Ayanami0730/arag
status: 200
content_type: text/html; charset=utf-8
topics: [Agentic RAG with Hierarchical Retrieval Interfaces]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:48.547223+00:00
---

# GitHub - Ayanami0730/arag: A-RAG: Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces. State-of-the-art RAG framework with keyword, semantic, and chunk read tools for multi-hop QA. · GitHub

## 원본 URL

https://github.com/Ayanami0730/arag

## 추출 본문

GitHub - Ayanami0730/arag: A-RAG: Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces. State-of-the-art RAG framework with keyword, semantic, and chunk read tools for multi-hop QA. · GitHub

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

 Ayanami0730
/aragPublic

Notifications
You must be signed in to change notification settings

Fork
 31

 Star
242

Code

Issues1

Pull requests1

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

Ayanami0730/arag

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
5 Commits

5 Commits

.github/ISSUE_TEMPLATE

.github/ISSUE_TEMPLATE

assets

assets

configs

configs

scripts

scripts

src/arag

src/arag

tests

tests

.env.example

.env.example

.gitignore

.gitignore

CITATION.cff

CITATION.cff

README.md

README.md

pyproject.toml

pyproject.toml

View all files

Repository files navigation

README

A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces

If you find our project helpful, please give us a star ⭐ on GitHub!

🚀 Quick Start

# 1. Install
git clone https://github.com/Ayanami0730/arag.git &&cd arag
uv sync --extra full # or: pip install -e ".[full]"# 2. Download benchmark datasets from HuggingFace
git clone https://huggingface.co/datasets/Ayanami0730/rag_test data --depth 1
rm -rf data/.git data/README.md

# 3. Build embedding index# We use Qwen3-Embedding-0.6B in our paper (https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)# You can also use a local path: --model /path/to/Qwen3-Embedding-0.6B
uv run python scripts/build_index.py \
 --chunks data/musique/chunks.json \
 --output data/musique/index \
 --model Qwen/Qwen3-Embedding-0.6B \
 --device cuda:0

# 4. Set environment variablesexport ARAG_API_KEY="your-api-key"export ARAG_BASE_URL="https://api.openai.com/v1"export ARAG_MODEL="gpt-5-mini"# 5. Run A-RAG agent
uv run python scripts/batch_runner.py \
 --config configs/example.yaml \
 --questions data/musique/questions.json \
 --output results/musique \
 --limit 10 --workers 5

# 6. Evaluate results
uv run python scripts/eval.py \
 --predictions results/musique/predictions.jsonl \
 --workers 5

Note: Datasets hosted on HuggingFace 🤗, reformatted from Zly0523/linear-rag and GraphRAG-Bench into a unified format.

Don't have 
uv
? Install it: 
curl -LsSf https://astral.sh/uv/install.sh | sh

✨ News

[Feb 2026] 📄 Paper released on arXiv

[Feb 2026] 🚀 Initial code and evaluation suite released

📖 Overview

Frontier language models have demonstrated strong reasoning and long-horizon tool-use capabilities. However, existing RAG systems fail to leverage these capabilities. They still rely on two paradigms:

Graph RAG: Designing an algorithm that retrieves passages in a single shot and concatenates them into the model's input

Workflow RAG: Predefining a workflow and prompting the model to execute it step-by-step

Neither paradigm allows the model to participate in retrieval decisions, preventing efficient scaling with model improvements.

Three Principles of Agentic RAG

We identify three key principles that define true agentic autonomy:

Autonomous Strategy: The agent dynamically chooses retrieval strategies based on task characteristics

Iterative Execution: The agent supports multi-round execution, adapting based on intermediate results

Interleaved Tool Use: The agent follows a ReAct-like action→observation→reasoning loop

Comparison of three RAG paradigms. Only A-RAG satisfies all three principles, making it a truly agentic framework.

Our Solution: A-RAG

A-RAG is an Agentic RAG framework that exposes hierarchical retrieval interfaces directly to the model. A-RAG provides three retrieval tools: 
keyword_search
, 
semantic_search
, and 
chunk_read
, enabling the agent to adaptively search and retrieve information across multiple granularities.

Overview of A-RAG framework. The agent iteratively uses hierarchical retrieval tools to gather information from the corpus and autonomously decides when to provide the final answer.

Key Features

🔍 Hierarchical Retrieval: Keyword-level, sentence-level, and chunk-level information access

🤖 True Agentic Autonomy: Autonomous strategy, iterative execution, and interleaved tool use

📈 Test-Time Scaling: Performance improves with increased compute resources

⚡ Context Efficient: Achieves superior accuracy with comparable or fewer retrieved tokens

📊 Main Results

Results (%) of baselines and A-RAG on benchmark datasets in terms of LLM-Evaluation Accuracy (LLM-Acc) and Contain-Match Accuracy (Cont-Acc). Best results are in bold, second best are underlined.

GPT-4o-mini Backbone

MethodMuSiQueHotpotQA2WikiMed.NovelLLMContLLMContLLMContLLMLLMVanilla BaselinesDirect Answer18.313.945.440.730.349.768.645.3Naive RAG38.636.174.572.942.659.075.368.5Graph-RAG & Workflow RAGGraphRAG26.420.833.233.318.447.251.328.8HippoRAG240.638.480.769.764.768.572.070.1LinearRAG34.826.372.060.562.962.353.145.4FaithfulRAG28.822.660.552.538.838.142.533.3MA-RAG34.127.460.654.451.053.462.344.5RAGentA32.229.963.062.427.750.367.761.3A-RAG (Ours)A-RAG (Naive)43.838.576.670.752.362.479.070.0A-RAG (Full)46.139.677.174.060.263.779.472.7

GPT-5-mini Backbone

MethodMuSiQueHotpotQA2WikiMed.NovelLLMContLLMContLLMContLLMLLMVanilla BaselinesDirect Answer35.826.563.653.551.354.090.545.1Naive RAG52.848.781.279.550.266.586.170.6Graph-RAG & Workflow RAGGraphRAG48.339.182.574.966.570.787.377.1HippoRAG261.752.584.875.082.079.778.254.3LinearRAG62.451.886.277.687.284.879.254.7FaithfulRAG52.952.876.975.351.856.675.460.7MA-RAG40.031.667.157.954.754.368.345.1RAGentA38.337.461.265.024.053.573.760.2A-RAG (Ours)A-RAG (Naive)66.259.790.885.370.676.992.780.4A-RAG (Full)74.165.394.588.089.788.993.185.3

📁 Project Structure

arag/
├── src/arag/ # Main package
│ ├── core/ # Core modules
│ │ ├── config.py # Configuration management
│ │ ├── context.py # Agent context & state tracking
│ │ └── llm.py # LLM client with cost tracking
│ ├── agent/ # Agent implementations
│ │ ├── base.py # BaseAgent with ReAct loop
│ │ └── prompts/ # System prompts
│ └── tools/ # Retrieval tools
│ ├── keyword_search.py
│ ├── semantic_search.py
│ └── read_chunk.py
├── scripts/ # CLI scripts
│ ├── build_index.py # Build embedding index
│ ├── batch_runner.py # Batch processing
│ └── eval.py # Evaluation
├── configs/ # Configuration examples
├── tests/ # Test suite (gitignored, add your own tests)
├── .github/ # Issue templates
└── CITATION.cff # Citation metadata

🔧 Hierarchical Retrieval Tools

A-RAG provides three retrieval tools that operate at different granularities:

Keyword Search

Method: Exact lexical matching (case-insensitive)

Best for: Known entities, names, technical terms

Score: 
Score(chunk, keywords) = Σ count(k, chunk) × |k|

No pre-indexing required

Semantic Search

Method: Dense retrieval using sentence-level embeddings

Best for: Conceptual queries, when exact wording is unknown

Score: Cosine similarity between query and sentence embeddings

Requires pre-built index

Chunk Read

Method: Retrieve full content of specified chunks

Strategy: Read promising chunks identified by search, read adjacent chunks (±1) for context

Context Tracker: Prevents redundant reading of already-accessed chunks

📚 Benchmarks & Datasets

Supported Datasets

DatasetDescriptionSourceMuSiQueMulti-hop QA (2-4 hops)HuggingFaceHotpotQAMulti-hop QAHuggingFace2WikiMultiHopQAMulti-hop QAGitHubGraphRAG-BenchGraph RAG evaluationGitHub

Custom Data Format

Prepare your own corpus as a JSON file:

["0:Document chunk content here...", "1:Another chunk..."]

Full Evaluation Example

Click to expand full evaluation instructions

1. Build Index

# Using HuggingFace model (auto-download)
uv run python scripts/build_index.py \
 --chunks data/musique/chunks.json \
 --output data/musique/index \
 --model Qwen/Qwen3-Embedding-0.6B \
 --device cuda:0

# Or using a local model path
uv run python scripts/build_index.py \
 --chunks data/musique/chunks.json \
 --output data/musique/index \
 --model /path/to/Qwen3-Embedding-0.6B \
 --device cuda:0

2. Create Config File

Create 
configs/test_musique.yaml
:

llm:
 temperature: 0.0max_tokens: 16384reasoning_effort: "medium"embedding:
 model: "Qwen/Qwen3-Embedding-0.6B"# or local pathdevice: "cuda:0"batch_size: 16agent:
 max_loops: 15max_token_budget: 128000verbose: falsedata:
 chunks_file: "data/musique/chunks.json"index_dir: "data/musique/index"

3. Run Full Benchmark

export ARAG_API_KEY="your-api-key"export ARAG_BASE_URL="https://api.openai.com/v1"export ARAG_MODEL="gpt-5-mini"export CUDA_VISIBLE_DEVICES=0

# Run all questions
uv run python scripts/batch_runner.py \
 --config configs/test_musique.yaml \
 --questions data/musique/questions.json \
 --output results/musique \
 --workers 10

# Evaluate
uv run python scripts/eval.py \
 --predictions results/musique/predictions.jsonl \
 --workers 10

🐍 Python API

fromaragimportLLMClient, BaseAgent, ToolRegistryfromarag.tools.keyword_searchimportKeywordSearchToolfromarag.tools.semantic_searchimportSemanticSearchToolfromarag.tools.read_chunkimportReadChunkTool# Initialize LLM clientclient=LLMClient(
 model="gpt-5-mini",
 api_key="your-api-key",
 base_url="https://api.openai.com/v1"
)

# Setup toolstools=ToolRegistry()
tools.register(KeywordSearchTool(chunks_file="data/chunks.json"))
tools.register(SemanticSearchTool(
 chunks_file="data/chunks.json",
 index_dir="data/index",
 embedding_model="Qwen/Qwen3-Embedding-0.6B"
))
tools.register(ReadChunkTool(chunks_file="data/chunks.json"))

# Create agentagent=BaseAgent(
 llm_client=client,
 tools=tools,
 max_loops=15,
 max_token_budget=128000
)

# Run queryresult=agent.run("What is the capital of France?")
print(f"Answer: {result['answer']}")
print(f"Cost: ${result['total_cost']:.6f}")
print(f"Loops: {result['loops']}")

🗺️ Roadmap

Baseline Scripts: Compatible scripts for all baseline methods (GraphRAG, HippoRAG2, LinearRAG, etc.)

Ablation Interfaces: Complete interfaces for ablation studies (w/o keyword search, w/o semantic search, w/o chunk read)

Multi-Provider Support: Native API support for Anthropic Claude and Google Gemini (currently only OpenAI-compatible APIs)

Additional Benchmarks: Scripts for HotpotQA, 2WikiMQA, and GraphRAG-Bench evaluation

Visualization Tools: Trajectory visualization and analysis tools

Contributions and feedback are welcome!

📝 Citation

If you use A-RAG in your research, please cite our paper:

@misc{du2026aragscalingagenticretrievalaugmented,
 title={A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces}, 
 author={Mingxuan Du and Benfeng Xu and Chiwei Zhu and Shaohan Wang and Pengyu Wang and Xiaorui Wang and Zhendong Mao},
 year={2026},
 eprint={2602.03442},
 archivePrefix={arXiv},
 primaryClass={cs.CL},
 url={https://arxiv.org/abs/2602.03442}, 
}

📄 License

MIT License

Paper | Website | GitHub

About

 A-RAG: Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces. State-of-the-art RAG framework with keyword, semantic, and chunk read tools for multi-hop QA.
 

agentresearchlab.org/agents/a-rag

Topics

 agent

 evaluation

 reproduce

 rag

 llm

 graphrag

 agentic-ai

 llmagents

 deepresearch

 agenticrag

Resources

 Readme

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Stars

242
 stars

Watchers

4
 watching

Forks

31
 forks

 Report repository

Releases
1tags

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python100.0%

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

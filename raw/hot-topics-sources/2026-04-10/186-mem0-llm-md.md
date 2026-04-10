---
title: mem0/LLM.md at main · mem0ai/mem0 · GitHub
source_url: https://github.com/mem0ai/mem0/blob/main/LLM.md
final_url: https://github.com/mem0ai/mem0/blob/main/LLM.md
status: 200
content_type: text/html; charset=utf-8
topics: [Mem0 Universal Memory Layer]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:52.153777+00:00
---

# mem0/LLM.md at main · mem0ai/mem0 · GitHub

## 원본 URL

https://github.com/mem0ai/mem0/blob/main/LLM.md

## 추출 본문

mem0/LLM.md at main · mem0ai/mem0 · GitHub

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

 mem0ai
/mem0Public

Notifications
You must be signed in to change notification settings

Fork
 5.9k

 Star
52.5k

Code

Issues95

Pull requests134

Discussions

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Security and quality

 Insights

FilesExpand file tree

main

Breadcrumbs

mem0

/
LLM.md

Copy path

BlameMore file actions

BlameMore file actions

Latest commit

History
History

History

1323 lines (1085 loc) · 36.4 KB

main

Breadcrumbs

mem0

/
LLM.md

Top

File metadata and controls

Preview

Code

Blame

1323 lines (1085 loc) · 36.4 KB

Raw

Copy raw file

Download raw file

Outline
Edit and raw actions

Mem0 - The Memory Layer for Personalized AI

Overview

Mem0 ("mem-zero") is an intelligent memory layer that enhances AI assistants and agents with persistent, personalized memory capabilities. It enables AI systems to remember user preferences, adapt to individual needs, and continuously learn over time—making it ideal for customer support chatbots, AI assistants, and autonomous systems.

Key Benefits:

+26% Accuracy over OpenAI Memory on LOCOMO benchmark

91% Faster responses than full-context approaches

90% Lower token usage than full-context methods

Installation

# Python
pip install mem0ai

# TypeScript/JavaScript
npm install mem0ai

Quick Start

Python - Self-Hosted

frommem0importMemory# Initialize memorymemory=Memory()

# Add memoriesmemory.add([
 {"role": "user", "content": "I love pizza and hate broccoli"},
 {"role": "assistant", "content": "I'll remember your food preferences!"}
], user_id="user123")

# Search memoriesresults=memory.search("food preferences", user_id="user123")
print(results)

# Get all memoriesall_memories=memory.get_all(user_id="user123")

Python - Hosted Platform

frommem0importMemoryClient# Initialize clientclient=MemoryClient(api_key="your-api-key")

# Add memoriesclient.add([
 {"role": "user", "content": "My name is John and I'm a developer"}
], user_id="john")

# Search memoriesresults=client.search("What do you know about me?", user_id="john")

TypeScript - Client SDK

import{MemoryClient}from'mem0ai';constclient=newMemoryClient({apiKey: 'your-api-key'});// Add memoryconstmemories=awaitclient.add([{role: 'user',content: 'My name is John'}],{user_id: 'john'});// Search memoriesconstresults=awaitclient.search('What is my name?',{user_id: 'john'});

TypeScript - OSS SDK

import{Memory}from'mem0ai/oss';constmemory=newMemory({embedder: {provider: 'openai',config: {apiKey: 'key'}},vectorStore: {provider: 'memory',config: {dimension: 1536}},llm: {provider: 'openai',config: {apiKey: 'key'}}});constresult=awaitmemory.add('My name is John',{userId: 'john'});

Core API Reference

Memory Class (Self-Hosted)

Import:
from mem0 import Memory, AsyncMemory

Initialization

frommem0importMemoryfrommem0.configs.baseimportMemoryConfig# Basic initializationmemory=Memory()

# With custom configurationconfig=MemoryConfig(
 vector_store={"provider": "qdrant", "config": {"host": "localhost"}},
 llm={"provider": "openai", "config": {"model": "gpt-4.1-nano-2025-04-14"}},
 embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
)
memory=Memory(config)

Core Methods

*add(messages, , user_id=None, agent_id=None, run_id=None, metadata=None, infer=True, memory_type=None, prompt=None)

Purpose: Create new memories from messages

Parameters:

messages
: str, dict, or list of message dicts

user_id/agent_id/run_id
: Session identifiers (at least one required)

metadata
: Additional metadata to store

infer
: Whether to use LLM for fact extraction (default: True)

memory_type
: "procedural_memory" for procedural memories

prompt
: Custom prompt for memory creation

Returns: Dict with "results" key containing memory operations

*search(query, , user_id=None, agent_id=None, run_id=None, limit=100, filters=None, threshold=None)

Purpose: Search memories semantically

Parameters:

query
: Search query string

user_id/agent_id/run_id
: Session filters (at least one required)

limit
: Maximum results (default: 100)

filters
: Additional search filters

threshold
: Minimum similarity score

Returns: Dict with "results" containing scored memories

get(memory_id)

Purpose: Retrieve specific memory by ID

Returns: Memory dict with id, memory, hash, timestamps, metadata

get_all(*, user_id=None, agent_id=None, run_id=None, filters=None, limit=100)

Purpose: List all memories with optional filtering

Returns: Dict with "results" containing list of memories

update(memory_id, data)

Purpose: Update memory content or metadata

Returns: Success message dict

delete(memory_id)

Purpose: Delete specific memory

Returns: Success message dict

delete_all(user_id=None, agent_id=None, run_id=None)

Purpose: Delete all memories for session (at least one ID required)

Returns: Success message dict

history(memory_id)

Purpose: Get memory change history

Returns: List of memory change history

reset()

Purpose: Reset entire memory store

Returns: None

MemoryClient Class (Hosted Platform)

Import:
from mem0 import MemoryClient, AsyncMemoryClient

Initialization

client=MemoryClient(
 api_key="your-api-key", # or set MEM0_API_KEY env varhost="https://api.mem0.ai", # optionalorg_id="your-org-id", # optionalproject_id="your-project-id"# optional
)

Core Methods

**add(messages, kwargs)

Purpose: Create memories from message conversations

Parameters: messages (list of message dicts), user_id, agent_id, app_id, metadata, filters

Returns: API response dict with memory creation results

**search(query, version="v1", kwargs)

Purpose: Search memories based on query

Parameters: query, version ("v1"/"v2"), user_id, agent_id, app_id, top_k, filters

Returns: List of search result dictionaries

get(memory_id)

Purpose: Retrieve specific memory by ID

Returns: Memory data dictionary

**get_all(version="v1", kwargs)

Purpose: Retrieve all memories with filtering

Parameters: version, user_id, agent_id, app_id, top_k, page, page_size

Returns: List of memory dictionaries

update(memory_id, text=None, metadata=None)

Purpose: Update memory text or metadata

Returns: Updated memory data

delete(memory_id)

Purpose: Delete specific memory

Returns: Success response

**delete_all(kwargs)

Purpose: Delete all memories with filtering

Returns: Success message

Batch Operations

batch_update(memories)

Purpose: Update multiple memories in single request

Parameters: List of memory update objects

Returns: Batch operation result

batch_delete(memories)

Purpose: Delete multiple memories in single request

Parameters: List of memory objects

Returns: Batch operation result

User Management

users()

Purpose: Get all users, agents, and sessions with memories

Returns: Dict with user/agent/session data

delete_users(user_id=None, agent_id=None, app_id=None, run_id=None)

Purpose: Delete specific entities or all entities

Returns: Success message

reset()

Purpose: Reset client by deleting all users and memories

Returns: Success message

Additional Features

history(memory_id)

Purpose: Get memory change history

Returns: List of memory changes

**feedback(memory_id, feedback, kwargs)

Purpose: Provide feedback on memory

Returns: Feedback response

**create_memory_export(schema, kwargs)

Purpose: Create memory export with JSON schema

Returns: Export creation response

**get_memory_export(kwargs)

Purpose: Retrieve exported memory data

Returns: Exported data

Configuration System

MemoryConfig

frommem0.configs.baseimportMemoryConfigconfig=MemoryConfig(
 vector_store=VectorStoreConfig(provider="qdrant", config={...}),
 llm=LlmConfig(provider="openai", config={...}),
 embedder=EmbedderConfig(provider="openai", config={...}),
 graph_store=GraphStoreConfig(provider="neo4j", config={...}), # optionalhistory_db_path="~/.mem0/history.db",
 version="v1.1",
 custom_fact_extraction_prompt="Custom prompt...",
 custom_update_memory_prompt="Custom prompt..."
)

Supported Providers

LLM Providers (20 supported)

openai - OpenAI GPT models (default)

anthropic - Claude models

gemini - Google Gemini

groq - Groq inference

ollama - Local Ollama models

together - Together AI

aws_bedrock - AWS Bedrock models

azure_openai - Azure OpenAI

litellm - LiteLLM proxy

deepseek - DeepSeek models

minimax - MiniMax models

xai - xAI models

sarvam - Sarvam AI

lmstudio - LM Studio local server

vllm - vLLM inference server

langchain - LangChain integration

openai_structured - OpenAI with structured output

azure_openai_structured - Azure OpenAI with structured output

Embedding Providers (10 supported)

openai - OpenAI embeddings (default)

ollama - Ollama embeddings

huggingface - HuggingFace models

azure_openai - Azure OpenAI embeddings

gemini - Google Gemini embeddings

vertexai - Google Vertex AI

together - Together AI embeddings

lmstudio - LM Studio embeddings

langchain - LangChain embeddings

aws_bedrock - AWS Bedrock embeddings

Vector Store Providers (19 supported)

qdrant - Qdrant vector database (default)

chroma - ChromaDB

pinecone - Pinecone vector database

pgvector - PostgreSQL with pgvector

mongodb - MongoDB Atlas Vector Search

milvus - Milvus vector database

weaviate - Weaviate

faiss - Facebook AI Similarity Search

redis - Redis vector search

elasticsearch - Elasticsearch

opensearch - OpenSearch

azure_ai_search - Azure AI Search

vertex_ai_vector_search - Google Vertex AI Vector Search

upstash_vector - Upstash Vector

supabase - Supabase vector

baidu - Baidu vector database

langchain - LangChain vector stores

s3_vectors - Amazon S3 Vectors

databricks - Databricks vector stores

Graph Store Providers (4 supported)

neo4j - Neo4j graph database

memgraph - Memgraph

neptune - AWS Neptune Analytics

kuzu - Kuzu Graph database

Configuration Examples

OpenAI Configuration

config=MemoryConfig(
 llm={
 "provider": "openai",
 "config": {
 "model": "gpt-4.1-nano-2025-04-14",
 "temperature": 0.1,
 "max_tokens": 1000
 }
 },
 embedder={
 "provider": "openai",
 "config": {
 "model": "text-embedding-3-small"
 }
 }
)

Local Setup with Ollama

config=MemoryConfig(
 llm={
 "provider": "ollama",
 "config": {
 "model": "llama3.1:8b",
 "ollama_base_url": "http://localhost:11434"
 }
 },
 embedder={
 "provider": "ollama",
 "config": {
 "model": "nomic-embed-text"
 }
 },
 vector_store={
 "provider": "chroma",
 "config": {
 "collection_name": "my_memories",
 "path": "./chroma_db"
 }
 }
)

Graph Memory with Neo4j

config=MemoryConfig(
 graph_store={
 "provider": "neo4j",
 "config": {
 "url": "bolt://localhost:7687",
 "username": "neo4j",
 "password": "password",
 "database": "neo4j"
 }
 }
)

Enterprise Setup

config=MemoryConfig(
 llm={
 "provider": "azure_openai",
 "config": {
 "model": "gpt-4",
 "azure_endpoint": "https://your-resource.openai.azure.com/",
 "api_key": "your-api-key",
 "api_version": "2024-02-01"
 }
 },
 vector_store={
 "provider": "pinecone",
 "config": {
 "api_key": "your-pinecone-key",
 "index_name": "mem0-index",
 "dimension": 1536
 }
 }
)

LLM Providers

OpenAI - GPT-4, GPT-3.5-turbo, and structured outputs

Anthropic - Claude models with advanced reasoning

Google AI - Gemini models for multimodal applications

AWS Bedrock - Enterprise-grade AWS managed models

Azure OpenAI - Microsoft Azure hosted OpenAI models

Groq - High-performance LPU optimized models

Together - Open-source model inference platform

Ollama - Local model deployment for privacy

vLLM - High-performance inference framework

LM Studio - Local model management

DeepSeek - Advanced reasoning models

Sarvam - Indian language models

XAI - xAI models

LiteLLM - Unified LLM interface

LangChain - LangChain LLM integration

Vector Store Providers

Chroma - AI-native open-source vector database

Qdrant - High-performance vector similarity search

Pinecone - Managed vector database with serverless options

Weaviate - Open-source vector search engine

PGVector - PostgreSQL extension for vector search

Milvus - Open-source vector database for scale

Redis - Real-time vector storage with Redis Stack

Supabase - Open-source Firebase alternative

Upstash Vector - Serverless vector database

Elasticsearch - Distributed search and analytics

OpenSearch - Open-source search and analytics

FAISS - Facebook AI Similarity Search

MongoDB - Document database with vector search

Azure AI Search - Microsoft's search service

Vertex AI Vector Search - Google Cloud vector search

Databricks Vector Search - Delta Lake integration

Baidu - Baidu vector database

LangChain - LangChain vector store integration

Embedding Providers

OpenAI - High-quality text embeddings

Azure OpenAI - Enterprise Azure-hosted embeddings

Google AI - Gemini embedding models

AWS Bedrock - Amazon embedding models

Hugging Face - Open-source embedding models

Vertex AI - Google Cloud enterprise embeddings

Ollama - Local embedding models

Together - Open-source model embeddings

LM Studio - Local model embeddings

LangChain - LangChain embedder integration

TypeScript/JavaScript SDK

Client SDK (Hosted Platform)

import{MemoryClient}from'mem0ai';constclient=newMemoryClient({apiKey: 'your-api-key',host: 'https://api.mem0.ai',// optionalorganizationId: 'org-id',// optionalprojectId: 'project-id'// optional});// Core operationsconstmemories=awaitclient.add([{role: 'user',content: 'I love pizza'}],{user_id: 'user123'});constresults=awaitclient.search('food preferences',{user_id: 'user123'});constmemory=awaitclient.get('memory-id');constallMemories=awaitclient.getAll({user_id: 'user123'});// Management operationsawaitclient.update('memory-id','Updated content');awaitclient.delete('memory-id');awaitclient.deleteAll({user_id: 'user123'});// Batch operationsawaitclient.batchUpdate([{id: 'mem1',text: 'new text'}]);awaitclient.batchDelete(['mem1','mem2']);// User managementconstusers=awaitclient.users();awaitclient.deleteUsers({user_ids: ['user1','user2']});// Webhooksconstwebhooks=awaitclient.getWebhooks();awaitclient.createWebhook({url: 'https://your-webhook.com',name: 'My Webhook',eventTypes: ['memory.created','memory.updated']});

OSS SDK (Self-Hosted)

import{Memory}from'mem0ai/oss';constmemory=newMemory({embedder: {provider: 'openai',config: {apiKey: 'your-key'}},vectorStore: {provider: 'qdrant',config: {host: 'localhost',port: 6333}},llm: {provider: 'openai',config: {model: 'gpt-4.1-nano'}}});// Core operationsconstresult=awaitmemory.add('I love pizza',{userId: 'user123'});constsearchResult=awaitmemory.search('food preferences',{userId: 'user123'});constmemoryItem=awaitmemory.get('memory-id');constallMemories=awaitmemory.getAll({userId: 'user123'});// Managementawaitmemory.update('memory-id','Updated content');awaitmemory.delete('memory-id');awaitmemory.deleteAll({userId: 'user123'});// History and resetconsthistory=awaitmemory.history('memory-id');awaitmemory.reset();

Key TypeScript Types

interfaceMessage{role: 'user'|'assistant';content: string|MultiModalMessages;}interfaceMemory{id: string;memory?: string;user_id?: string;categories?: string[];created_at?: Date;updated_at?: Date;metadata?: any;score?: number;}interfaceMemoryOptions{user_id?: string;agent_id?: string;app_id?: string;run_id?: string;metadata?: Record<string,any>;filters?: Record<string,any>;api_version?: 'v1'|'v2';infer?: boolean;enable_graph?: boolean;}interfaceSearchResult{results: Memory[];relations?: any[];}

Advanced Features

Graph Memory

Graph memory enables relationship tracking between entities mentioned in conversations.

# Enable graph memoryconfig=MemoryConfig(
 graph_store={
 "provider": "neo4j",
 "config": {
 "url": "bolt://localhost:7687",
 "username": "neo4j",
 "password": "password"
 }
 }
)
memory=Memory(config)

# Add memory with relationship extractionresult=memory.add(
 "John works at OpenAI and is friends with Sarah",
 user_id="user123"
)

# Result includes both memories and relationshipsprint(result["results"]) # Memory entriesprint(result["relations"]) # Graph relationships

Supported Graph Databases:

Neo4j: Full-featured graph database with Cypher queries

Memgraph: High-performance in-memory graph database

Neptune: AWS managed graph database service

kuzu - OSS Kuzu Graph database

Multimodal Memory

Store and retrieve memories from text, images, and PDFs.

# Text + Imagemessages= [
 {"role": "user", "content": "This is my travel setup"},
 {
 "role": "user",
 "content": {
 "type": "image_url",
 "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
 }
 }
]
client.add(messages, user_id="user123")

# PDF processingpdf_message= {
 "role": "user",
 "content": {
 "type": "pdf_url",
 "pdf_url": {"url": "https://example.com/document.pdf"}
 }
}
client.add([pdf_message], user_id="user123")

Procedural Memory

Store step-by-step procedures and workflows.

# Add procedural memoryresult=memory.add(
 "To deploy the app: 1. Run tests 2. Build Docker image 3. Push to registry 4. Update k8s manifests",
 user_id="developer123",
 memory_type="procedural_memory"
)

# Search for proceduresprocedures=memory.search(
 "How to deploy?",
 user_id="developer123"
)

Custom Prompts

custom_extraction_prompt="""Extract key facts from the conversation focusing on:1. Personal preferences2. Technical skills3. Project requirements4. Important dates and deadlinesConversation: {messages}"""config=MemoryConfig(
 custom_fact_extraction_prompt=custom_extraction_prompt
)
memory=Memory(config)

Common Usage Patterns

1. Personal AI Assistant

classPersonalAssistant:
 def__init__(self):
 self.memory=Memory()
 self.llm=OpenAI() # Your LLM clientdefchat(self, user_input: str, user_id: str) ->str:
 # Retrieve relevant memoriesmemories=self.memory.search(user_input, user_id=user_id, limit=5)
 
 # Build context from memoriescontext="\n".join([f"- {m['memory']}"forminmemories['results']])
 
 # Generate response with contextprompt=f""" Context from previous conversations:{context} User: {user_input} Assistant: """response=self.llm.generate(prompt)
 
 # Store the conversationself.memory.add([
 {"role": "user", "content": user_input},
 {"role": "assistant", "content": response}
 ], user_id=user_id)
 
 returnresponse

2. Customer Support Bot

classSupportBot:
 def__init__(self):
 self.memory=MemoryClient(api_key="your-key")
 
 defhandle_ticket(self, customer_id: str, issue: str) ->str:
 # Get customer historyhistory=self.memory.search(
 issue,
 user_id=customer_id,
 limit=10
 )
 
 # Check for similar past issuessimilar_issues= [mforminhistoryifm['score'] >0.8]
 
 ifsimilar_issues:
 context=f"Previous similar issues: {similar_issues[0]['memory']}"else:
 context="No previous similar issues found."# Generate responseresponse=self.generate_support_response(issue, context)
 
 # Store interactionself.memory.add([
 {"role": "user", "content": f"Issue: {issue}"},
 {"role": "assistant", "content": response}
 ], user_id=customer_id, metadata={
 "category": "support_ticket",
 "timestamp": datetime.now().isoformat()
 })
 
 returnresponse

3. Learning Assistant

classStudyBuddy:
 def__init__(self):
 self.memory=Memory()
 
 defstudy_session(self, student_id: str, topic: str, content: str):
 # Store study materialself.memory.add(
 f"Studied {topic}: {content}",
 user_id=student_id,
 metadata={
 "topic": topic,
 "session_date": datetime.now().isoformat(),
 "type": "study_session"
 }
 )
 
 defquiz_student(self, student_id: str, topic: str) ->list:
 # Get relevant study materialsmaterials=self.memory.search(
 f"topic:{topic}",
 user_id=student_id,
 filters={"metadata.type": "study_session"}
 )
 
 # Generate quiz questions based on materialsquestions=self.generate_quiz_questions(materials)
 returnquestionsdeftrack_progress(self, student_id: str) ->dict:
 # Get all study sessionssessions=self.memory.get_all(
 user_id=student_id,
 filters={"metadata.type": "study_session"}
 )
 
 # Analyze progresstopics_studied= {}
 forsessioninsessions['results']:
 topic=session['metadata']['topic']
 topics_studied[topic] =topics_studied.get(topic, 0) +1return {
 "total_sessions": len(sessions['results']),
 "topics_covered": len(topics_studied),
 "topic_frequency": topics_studied
 }

4. Multi-Agent System

classMultiAgentSystem:
 def__init__(self):
 self.shared_memory=Memory()
 self.agents= {
 "researcher": ResearchAgent(),
 "writer": WriterAgent(),
 "reviewer": ReviewAgent()
 }
 
 defcollaborative_task(self, task: str, session_id: str):
 # Research phaseresearch_results=self.agents["researcher"].research(task)
 self.shared_memory.add(
 f"Research findings: {research_results}",
 agent_id="researcher",
 run_id=session_id,
 metadata={"phase": "research"}
 )
 
 # Writing phaseresearch_context=self.shared_memory.search(
 "research findings",
 run_id=session_id
 )
 draft=self.agents["writer"].write(task, research_context)
 self.shared_memory.add(
 f"Draft content: {draft}",
 agent_id="writer",
 run_id=session_id,
 metadata={"phase": "writing"}
 )
 
 # Review phaseall_context=self.shared_memory.get_all(run_id=session_id)
 final_output=self.agents["reviewer"].review(draft, all_context)
 
 returnfinal_output

5. Voice Assistant with Memory

importspeech_recognitionassrfromgttsimportgTTSimportpygameclassVoiceAssistant:
 def__init__(self):
 self.memory=Memory()
 self.recognizer=sr.Recognizer()
 self.microphone=sr.Microphone()
 
 deflisten_and_respond(self, user_id: str):
 # Listen to userwithself.microphoneassource:
 audio=self.recognizer.listen(source)
 
 try:
 # Convert speech to textuser_input=self.recognizer.recognize_google(audio)
 print(f"User said: {user_input}")
 
 # Get relevant memoriesmemories=self.memory.search(user_input, user_id=user_id)
 context="\n".join([m['memory'] forminmemories['results'][:3]])
 
 # Generate responseresponse=self.generate_response(user_input, context)
 
 # Store conversationself.memory.add([
 {"role": "user", "content": user_input},
 {"role": "assistant", "content": response}
 ], user_id=user_id)
 
 # Convert response to speechtts=gTTS(text=response, lang='en')
 tts.save("response.mp3")
 
 # Play responsepygame.mixer.init()
 pygame.mixer.music.load("response.mp3")
 pygame.mixer.music.play()
 
 returnresponseexceptsr.UnknownValueError:
 return"Sorry, I didn't understand that."

Best Practices

1. Memory Organization

# Use consistent user/agent/session IDsuser_id=f"user_{user_email.replace('@', '_')}"agent_id=f"agent_{agent_name}"run_id=f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"# Add meaningful metadatametadata= {
 "category": "customer_support",
 "priority": "high",
 "department": "technical",
 "timestamp": datetime.now().isoformat(),
 "source": "chat_widget"
}

# Use descriptive memory contentmemory.add(
 "Customer John Smith reported login issues with 2FA on mobile app. Resolved by clearing app cache.",
 user_id=customer_id,
 metadata=metadata
)

2. Search Optimization

# Use specific search queriesresults=memory.search(
 "login issues mobile app", # Specific keywordsuser_id=customer_id,
 limit=5, # Reasonable limitthreshold=0.7# Filter low-relevance results
)

# Combine multiple searches for comprehensive resultstechnical_issues=memory.search("technical problems", user_id=user_id)
recent_conversations=memory.get_all(
 user_id=user_id,
 filters={"metadata.timestamp": {"$gte": last_week}},
 limit=10
)

3. Memory Lifecycle Management

# Regular cleanup of old memoriesdefcleanup_old_memories(memory_client, days_old=90):
 cutoff_date=datetime.now() -timedelta(days=days_old)
 
 all_memories=memory_client.get_all()
 formeminall_memories:
 ifdatetime.fromisoformat(mem['created_at']) <cutoff_date:
 memory_client.delete(mem['id'])

# Archive important memoriesdefarchive_memory(memory_client, memory_id):
 memory=memory_client.get(memory_id)
 memory_client.update(memory_id, metadata={
 **memory.get('metadata', {}),
 'archived': True,
 'archive_date': datetime.now().isoformat()
 })

4. Error Handling

defsafe_memory_operation(memory_client, operation, *args, **kwargs):
 try:
 returnoperation(*args, **kwargs)
 exceptExceptionase:
 logger.error(f"Memory operation failed: {e}")
 # Fallback to basic response without memoryreturn {"results": [], "message": "Memory temporarily unavailable"}

# Usageresults=safe_memory_operation(
 memory_client,
 memory_client.search,
 query,
 user_id=user_id
)

5. Performance Optimization

# Batch operations when possiblememories_to_add= [
 {"content": msg1, "user_id": user_id},
 {"content": msg2, "user_id": user_id},
 {"content": msg3, "user_id": user_id}
]

# Instead of multiple add() calls, use batch operationsformemory_datainmemories_to_add:
 memory.add(memory_data["content"], user_id=memory_data["user_id"])

# Cache frequently accessed memoriesfromfunctoolsimportlru_cache@lru_cache(maxsize=100)defget_user_preferences(user_id: str):
 returnmemory.search("preferences settings", user_id=user_id, limit=5)

Integration Examples

AutoGen Integration

fromcookbooks.helper.mem0_teachabilityimportMem0Teachabilityfrommem0importMemory# Add memory capability to AutoGen agentsmemory=Memory()
teachability=Mem0Teachability(
 verbosity=1,
 reset_db=False,
 recall_threshold=1.5,
 memory_client=memory
)

# Apply to agentteachability.add_to_agent(your_autogen_agent)

LangChain Integration

fromlangchain.memoryimportConversationBufferMemoryfrommem0importMemoryclassMem0LangChainMemory(ConversationBufferMemory):
 def__init__(self, user_id: str, **kwargs):
 super().__init__(**kwargs)
 self.mem0=Memory()
 self.user_id=user_iddefsave_context(self, inputs, outputs):
 # Save to both LangChain and Mem0super().save_context(inputs, outputs)
 
 # Store in Mem0 for long-term memoryself.mem0.add([
 {"role": "user", "content": str(inputs)},
 {"role": "assistant", "content": str(outputs)}
 ], user_id=self.user_id)
 
 defload_memory_variables(self, inputs):
 # Load from LangChain buffervariables=super().load_memory_variables(inputs)
 
 # Enhance with relevant long-term memoriesrelevant_memories=self.mem0.search(
 str(inputs),
 user_id=self.user_id,
 limit=3
 )
 
 ifrelevant_memories['results']:
 long_term_context="\n".join([
 f"- {m['memory']}"forminrelevant_memories['results']
 ])
 variables['history'] +=f"\n\nRelevant past context:\n{long_term_context}"returnvariables

Streamlit App

importstreamlitasstfrommem0importMemory# Initialize memoryif'memory'notinst.session_state:
 st.session_state.memory=Memory()

# User inputuser_id=st.text_input("User ID", value="user123")
user_message=st.text_input("Your message")

ifst.button("Send"):
 # Get relevant memoriesmemories=st.session_state.memory.search(
 user_message,
 user_id=user_id,
 limit=5
 )
 
 # Display memoriesifmemories['results']:
 st.subheader("Relevant Memories:")
 formemoryinmemories['results']:
 st.write(f"- {memory['memory']} (Score: {memory['score']:.2f})")
 
 # Generate and display responseresponse=generate_response(user_message, memories)
 st.write(f"Assistant: {response}")
 
 # Store conversationst.session_state.memory.add([
 {"role": "user", "content": user_message},
 {"role": "assistant", "content": response}
 ], user_id=user_id)

# Display all memoriesifst.button("Show All Memories"):
 all_memories=st.session_state.memory.get_all(user_id=user_id)
 formemoryinall_memories['results']:
 st.write(f"- {memory['memory']}")

FastAPI Backend

fromfastapiimportFastAPI, HTTPExceptionfrompydanticimportBaseModelfrommem0importMemoryClientfromtypingimportList, Optionalapp=FastAPI()
memory_client=MemoryClient(api_key="your-api-key")

classChatMessage(BaseModel):
 role: strcontent: strclassChatRequest(BaseModel):
 messages: List[ChatMessage]
 user_id: strmetadata: Optional[dict] =NoneclassSearchRequest(BaseModel):
 query: struser_id: strlimit: int=10@app.post("/chat")asyncdefchat(request: ChatRequest):
 try:
 # Add messages to memoryresult=memory_client.add(
 [msg.dict() formsginrequest.messages],
 user_id=request.user_id,
 metadata=request.metadata
 )
 return {"status": "success", "result": result}
 exceptExceptionase:
 raiseHTTPException(status_code=500, detail=str(e))

@app.post("/search")asyncdefsearch_memories(request: SearchRequest):
 try:
 results=memory_client.search(
 request.query,
 user_id=request.user_id,
 limit=request.limit
 )
 return {"results": results}
 exceptExceptionase:
 raiseHTTPException(status_code=500, detail=str(e))

@app.get("/memories/{user_id}")asyncdefget_user_memories(user_id: str, limit: int=50):
 try:
 memories=memory_client.get_all(user_id=user_id, limit=limit)
 return {"memories": memories}
 exceptExceptionase:
 raiseHTTPException(status_code=500, detail=str(e))

@app.delete("/memories/{memory_id}")asyncdefdelete_memory(memory_id: str):
 try:
 result=memory_client.delete(memory_id)
 return {"status": "deleted", "result": result}
 exceptExceptionase:
 raiseHTTPException(status_code=500, detail=str(e))

Troubleshooting

Common Issues

Memory Not Found

# Check if memory exists before operationsmemory=memory_client.get(memory_id)
ifnotmemory:
 print(f"Memory {memory_id} not found")

Search Returns No Results

# Lower the similarity thresholdresults=memory.search(
 query,
 user_id=user_id,
 threshold=0.5# Lower threshold
)

# Check if memories exist for userall_memories=memory.get_all(user_id=user_id)
ifnotall_memories['results']:
 print("No memories found for user")

Configuration Issues

# Validate configurationtry:
 memory=Memory(config)
 # Test with a simple operationmemory.add("Test memory", user_id="test")
 print("Configuration valid")
exceptExceptionase:
 print(f"Configuration error: {e}")

API Rate Limits

importtimefromfunctoolsimportwrapsdefrate_limit_retry(max_retries=3, delay=1):
 defdecorator(func):
 @wraps(func)defwrapper(*args, **kwargs):
 forattemptinrange(max_retries):
 try:
 returnfunc(*args, **kwargs)
 exceptExceptionase:
 if"rate limit"instr(e).lower() andattempt<max_retries-1:
 time.sleep(delay* (2**attempt)) # Exponential backoffcontinueraiseereturnwrapperreturndecorator@rate_limit_retry()defsafe_memory_add(memory, content, user_id):
 returnmemory.add(content, user_id=user_id)

Performance Tips

Optimize Vector Store Configuration

# For Qdrantconfig=MemoryConfig(
 vector_store={
 "provider": "qdrant",
 "config": {
 "host": "localhost",
 "port": 6333,
 "collection_name": "memories",
 "embedding_model_dims": 1536,
 "distance": "cosine"
 }
 }
)

Batch Processing

# Process multiple memories efficientlydefbatch_add_memories(memory_client, conversations, user_id, batch_size=10):
 foriinrange(0, len(conversations), batch_size):
 batch=conversations[i:i+batch_size]
 forconvinbatch:
 memory_client.add(conv, user_id=user_id)
 time.sleep(0.1) # Small delay between batches

Memory Cleanup

# Regular cleanup to maintain performancedefcleanup_memories(memory_client, user_id, max_memories=1000):
 all_memories=memory_client.get_all(user_id=user_id)
 iflen(all_memories) >max_memories:
 # Keep most recent memoriessorted_memories=sorted(
 all_memories,
 key=lambdax: x['created_at'],
 reverse=True
 )
 
 # Delete oldest memoriesformemoryinsorted_memories[max_memories:]:
 memory_client.delete(memory['id'])

Resources

Documentation: https://docs.mem0.ai

GitHub Repository: https://github.com/mem0ai/mem0

Discord Community: https://mem0.dev/DiG

Platform: https://app.mem0.ai

Research Paper: https://mem0.ai/research

Examples: https://github.com/mem0ai/mem0/tree/main/examples

License

Mem0 is available under the Apache 2.0 License. See the LICENSE file for more details.

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

---
title: GitHub - asinghcsu/AgenticRAG-Survey: Agentic-RAG explores advanced Retrieval-Augmented Generation systems enhanced with AI LLM agents. · GitHub
source_url: https://github.com/asinghcsu/AgenticRAG-Survey
final_url: https://github.com/asinghcsu/AgenticRAG-Survey
status: 200
content_type: text/html; charset=utf-8
topics: [Agentic RAG with Hierarchical Retrieval Interfaces]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:48.453679+00:00
---

# GitHub - asinghcsu/AgenticRAG-Survey: Agentic-RAG explores advanced Retrieval-Augmented Generation systems enhanced with AI LLM agents. · GitHub

## 원본 URL

https://github.com/asinghcsu/AgenticRAG-Survey

## 추출 본문

GitHub - asinghcsu/AgenticRAG-Survey: Agentic-RAG explores advanced Retrieval-Augmented Generation systems enhanced with AI LLM agents. · GitHub

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

 asinghcsu
/AgenticRAG-SurveyPublic

Notifications
You must be signed in to change notification settings

Fork
 177

 Star
1.6k

Code

Issues0

Pull requests0

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

asinghcsu/AgenticRAG-Survey

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
52 Commits

52 Commits

assets

assets

README.md

README.md

View all files

Repository files navigation

README

Agentic Retrieval-Augmented Generation : A Survey On Agentic RAG

Overview of Agentic RAG

Recent Update (2025-02-04):

Check section 4 in the table of contents in this repo for the new Agentic Workflow Patterns.
New images have been added to enhance the Overview of Agentic RAG. The paper is also updated.

Abstract

Agentic Retrieval-Augmented Generation ( Agentic RAG) represents a transformative leap in artificial intelligence by embedding autonomous agents into the RAG pipeline. This repository complements the survey paper "Agentic Retrieval-Augmented Generation (Agentic RAG): A Survey On Agentic RAG," providing insights into:

Foundational principles, including Agentic Patterns such as reflection, planning, tool use, and multi-agent collaboration.

A detailed taxonomy of Agentic RAG systems, showcasing frameworks like single-agent, multi-agent, hierarchical, corrective, adaptive, and graph-based RAG.

Comparative analysis of traditional RAG, Agentic RAG, and Agentic Document Workflows (ADW) to highlight their strengths, weaknesses, and best-fit scenarios.

Real-world applications across industries like healthcare, education, finance, and legal analysis.

Challenges and future directions in scaling, ethical AI, multimodal integration, and human-agent collaboration.

This repository serves as a comprehensive resource for researchers and practitioners to explore, implement, and advance the capabilities of Agentic RAG systems.

Table of Contents

📜 Abstract

🧩 Introduction

🤖 Agentic Patterns

🔄 Agentic Workflow Patterns

🛠️ Taxonomy of Agentic RAG Systems

🔍 Comparative Analysis of Agentic RAG Frameworks

💼 Applications

🚧 Challenges and Future Directions

🛠️ Implementation of RAG Agentic Taxonomy: Techniques and Tools

📰 Blogs and Tutorials on Agentic RAG

🖊️ Noteworthy Related Concepts

💡 Practical Implementations and Use Cases of Agentic RAG

📚 References

🖊️ How to Cite

Introduction

Retrieval-Augmented Generation (RAG) systems combine the capabilities of large language models (LLMs) with retrieval mechanisms to generate contextually relevant and accurate responses. While traditional RAG systems excel in knowledge retrieval and generation, they often fall short in handling dynamic, multi-step reasoning tasks, adaptability, and orchestration for complex workflows.

Agentic Retrieval-Augmented Generation (Agentic RAG) overcomes these limitations by integrating autonomous AI agents. These agents employ core Agentic Patterns, such as reflection, planning, tool use, and multi-agent collaboration, to dynamically adapt to task-specific requirements and provide superior performance in:

Multi-domain knowledge retrieval.

Real-time, document-centric workflows.

Scalable, adaptive, and ethical AI systems.

This repository explores the evolution of RAG to Agentic RAG, presenting:

Agentic Patterns: The core principles driving the system’s adaptability and intelligence.

Taxonomy: A comprehensive classification of Agentic RAG architectures.

Comparative Analysis: Key differences between Traditional RAG, Agentic RAG, and ADW.

Applications: Practical use cases across healthcare, education, finance, and more.

Challenges and Future Directions: Addressing scalability, ethical AI, and multimodal integration.

Whether you’re a researcher, developer, or practitioner, this repository offers valuable insights and resources to understand and advance Agentic RAG systems.

Agentic Patterns

Agentic RAG systems derive their intelligence and adaptability from well-defined agentic patterns. These patterns enable agents to handle complex reasoning tasks, adapt to dynamic environments, and collaborate effectively. Below are the key patterns central to Agentic RAG:

1. Reflection

Definition: Agents evaluate their own decisions and outputs, identifying errors and areas for improvement.

Key Benefits:

Enables iterative refinement of results.

Enhances accuracy in multi-step reasoning tasks.

Example: In a medical diagnostic system, agents refine diagnoses based on iterative feedback from retrieved data.

Figure 1: Reflection Pattern

2. Planning

Definition: Agents create structured workflows and task sequences to solve problems efficiently.

Key Benefits:

Facilitates multi-step reasoning by breaking down tasks.

Reduces computational overhead through optimized task prioritization.

Example: A financial analysis system plans data retrieval tasks to assess risks and provide recommendations.

Figure 2: Planning Pattern

3. Tool Use

Definition: Agents interact with external tools, APIs, and knowledge bases to retrieve and process data.

Key Benefits:

Expands the system's capabilities beyond pre-trained knowledge.

Enables domain-specific applications by integrating external resources.

Example: A legal assistant agent retrieves clauses from contract databases and applies domain-specific rules for compliance analysis.

Figure 3: Tool Use Pattern

4. Multi-Agent Collaboration

Definition: Multiple agents collaborate to divide and conquer complex tasks, sharing information and results.

Key Benefits:

Handles large-scale and distributed problems efficiently.

Combines specialized agent capabilities for better outcomes.

Example:

In customer support, agents collaborate to retrieve knowledge from FAQs, generate responses, and provide follow-ups.

LawGlance simplifies legal research by leveraging multi-agent workflows to retrieve relevant documents, analyze information, and deliver precise legal insights.
It integrates Crew AI, LangChain, and Chroma to retrieve legal documents, perform web searches, and provide concise, accurate answers tailored to user queries.
Access LawGlance on Google Colab

Figure 4: Multi-Agent Collaboration Pattern

Significance of Agentic Patterns

These patterns form the backbone of Agentic RAG systems, enabling them to:

Adapt dynamically to task requirements.

Improve decision-making through self-evaluation.

Leverage external resources for domain-specific reasoning.

Handle complex, distributed workflows via collaboration.

Agentic Workflow Patterns: Adaptive Strategies for Dynamic Collaboration

Agentic workflow patterns help structure LLM-based applications to optimize performance, accuracy, and efficiency. Different approaches are suitable depending on task complexity and processing requirements.
Source:Anthropic Research and LangGraph Workflows

1. Prompt Chaining: Enhancing Accuracy Through Sequential Processing

Definition:

Prompt chaining decomposes a complex task into multiple steps, where each step builds upon the previous one. This structured approach improves accuracy by simplifying each subtask before moving forward. However, it may increase latency due to sequential processing.

When to Use:

This workflow is most effective when a task can be broken down into fixed subtasks, each contributing to the final output. It is particularly useful in scenarios where step-by-step reasoning enhances accuracy.

Example Applications:
Generating marketing content in one language and then translating it into another while preserving nuances.

Structuring document creation by first generating an outline, verifying its completeness, and then developing the full text.

Figure 1: Illustration of Prompt Chaining Workflow

2. Routing: Directing Inputs to Specialized Processes

Definition:

Routing involves classifying an input and directing it to an appropriate specialized prompt or process. This method ensures distinct queries or tasks are handled separately, improving efficiency and response quality.

When to Use:

Ideal for scenarios where different types of input require distinct handling strategies, ensuring optimized performance for each category.

Example Applications:
Directing customer service queries into categories such as technical support, refund requests, or general inquiries.

Assigning simple queries to smaller models for cost efficiency, while complex requests go to advanced models.

Figure 2: Illustration of Routing Workflow

3. Parallelization: Speeding Up Processing Through Concurrent Execution

Definition:

Parallelization divides a task into independent processes that run simultaneously, reducing latency and improving throughput. It can be categorized into:

Sectioning: Splitting tasks into independent subtasks.

Voting: Generating multiple outputs for increased accuracy.

When to Use:

Useful when tasks can be executed independently to enhance speed or when multiple outputs improve confidence.

Example Applications:
Sectioning: Splitting tasks like content moderation, where one model screens input while another generates a response.

Voting: Using multiple models to cross-check code for vulnerabilities or analyze content moderation decisions.

Figure 3: Illustration of Parallelization Workflow

4. Orchestrator-Workers: Dynamic Task Delegation

Definition:

This workflow features a central orchestrator model that dynamically breaks tasks into subtasks, assigns them to specialized worker models, and compiles the results. Unlike parallelization, it adapts to varying input complexity.

When to Use:

Best suited for tasks requiring dynamic decomposition and real-time adaptation, where subtasks are not predefined.

Example Applications:
Automatically modifying multiple files in a codebase based on the nature of requested changes.

Conducting real-time research by gathering and synthesizing relevant information from multiple sources.

Figure 4: Illustration of Orchestrator-Workers Workflow

5. Evaluator-Optimizer: Refining Output Through Iteration

Definition:

The evaluator-optimizer workflow iteratively improves content by generating an initial output and refining it based on feedback from an evaluation model.

When to Use:

Effective when iterative refinement significantly enhances response quality, especially when clear evaluation criteria exist.

Example Applications:
Improving literary translations through multiple evaluation and refinement cycles.

Conducting multi-round research queries where additional iterations refine search results.

Figure 5: Illustration of Evaluator-Optimizer Workflow

---

Taxonomy of Agentic RAG Systems

Agentic Retrieval-Augmented Generation (RAG) systems encompass various architectures and workflows, each tailored to specific tasks and levels of complexity. Below is a detailed taxonomy of these systems:

1. Single-Agent RAG

Key Idea: A single autonomous agent manages the retrieval and generation process.

Workflow:

Query is submitted to the agent.

The agent retrieves relevant data from external sources.

Data is processed and synthesized into a response.

Advantages:

Simple architecture for basic use cases.

Easy to implement and maintain.

Limitations:

Limited scalability.

Ineffective for multi-step reasoning or large datasets.

2. Multi-Agent RAG

Key Idea: A team of agents collaborates to perform complex retrieval and reasoning tasks.

Workflow:

Agents dynamically divide tasks (e.g., retrieval, reasoning, synthesis).

Each agent specializes in a specific sub-task.

Results are aggregated and synthesized into a coherent output.

Advantages:

Better performance for distributed, multi-step tasks.

Increased modularity and scalability.

Limitations:

Coordination complexity increases with the number of agents.

Risk of redundancy or conflicts between agents.

Case Study: AgentFlow

AgentFlow is a trainable, tool-integrated agentic framework designed to overcome the scalability and generalization limits of today’s tool-augmented reasoning approaches. It coordinates four specialized modules—Planner, Executor, Verifier, Generator—and optimizes the plannerin the flow of multi-turn tasks using Flow-GRPO, improving long-horizon credit assignment and tool-use reliability.

Key Features:

🧩 Modular Agentic System – Four specialized agent modules (Planner, Executor, Verifier, Generator) that coordinate via evolving memory and integrated tools across multiple turns.

🔗 Multi-Tool Integration – Seamlessly connect with diverse tool ecosystems, including 
base_generator
, 
python_coder
, 
google_search
, 
wikipedia_search
, 
web_search
, and more.

🎯 Flow-GRPO Algorithm – Enables in-the-flow agent optimization for long-horizon reasoning tasks with sparse rewards.

3. Hierarchical Agentic RAG

Key Idea: Organizes agents in a hierarchy for better task prioritization and delegation.

Workflow:

A top-level agent orchestrates subtasks among lower-level agents.

Each lower-level agent handles a specific part of the process.

Results are iteratively refined and integrated at higher levels.

Advantages:

Scalable for large and complex tasks.

Modular design facilitates specialization.

Limitations:

Requires sophisticated orchestration mechanisms.

Potential bottlenecks at higher levels of the hierarchy.

4. Corrective Agentic RAG

Key Idea: Feedback loops enable agents to evaluate and refine their outputs iteratively.

Workflow:

Initial response is generated by the agent.

A critic module evaluates the response for errors or inconsistencies.

The agent refines the response based on feedback.

Steps 2-3 repeat until the output meets quality standards.

Advantages:

High accuracy and reliability through iterative improvements.

Useful for error-prone or high-stakes tasks.

Limitations:

Increased computational overhead.

Feedback mechanisms must be well-designed to avoid infinite loops.

5. Adaptive Agentic RAG

Key Idea: Dynamically adjusts retrieval strategies and workflows based on task requirements.

Workflow:

The agent assesses the query and its context.

Adapts retrieval strategies in real-time based on available data and user needs.

Synthesizes a response using dynamic workflows.

Advantages:

High flexibility for varied tasks and dynamic environments.

Improves context relevance and user satisfaction.

Limitations:

Challenging to design robust adaptation mechanisms.

Computational overhead for real-time adjustments.

6. Graph-Based Agentic RAG

Graph-based RAG systems extend traditional RAG by integrating graph-based data structures for advanced reasoning.

6.1 Agent-G: Agentic Framework for Graph RAG

Key Idea: Dynamically assigns tasks to specialized agents using graph knowledge bases and feedback loops.

Workflow:

Extract relationships from graph knowledge bases (e.g., disease-to-symptom mappings).

Complement with unstructured data from external sources.

Use a critic module to validate results and iteratively improve.

Advantages:

Combines structured and unstructured data.

Modular and scalable for complex tasks.

Ensures high accuracy through iterative refinement.

6.2 GeAR: Graph-Enhanced Agent for RAG

Key Idea: Enhances RAG systems with graph expansion techniques and agent-based architectures.

Workflow:

Expand query-related graphs for better relational understanding.

Leverage specialized agents for multi-hop reasoning.

Synthesize graph-structured and unstructured information into responses.

Advantages:

Excels in multi-hop reasoning scenarios.

Improves accuracy for deep contextual tasks.

Dynamically adapts to complex query environments.

7. Agentic Document Workflows (ADW)

Agentic Document Workflows (ADW) extend traditional RAG systems by automating document-centric processes with intelligent agents.

Workflow

Document Parsing and Structuring:

Extracts structured data from documents like invoices or contracts.

State Maintenance:

Tracks context across multi-step workflows for consistency.

Knowledge Retrieval:

Retrieves relevant references from external sources or domain-specific databases.

Agentic Orchestration:

Applies business rules, performs multi-hop reasoning, and orchestrates external APIs.

Actionable Output Generation:

Produces structured outputs tailored to specific use cases (e.g., reports or summaries).

Key Features and Advantages

State Maintenance: Ensures consistency in multi-step workflows.

Domain-Specific Intelligence: Adapts to specialized domains with tailored rules.

Scalability: Handles large-scale document processing efficiently.

Enhanced Productivity: Reduces manual effort and augments human expertise.

Visual Representations

Figure 5: Single-Agent RAG Diagram

Figure 6: Multi-Agent RAG Diagram

Figure 7: Hierarchical RAG Workflow

Figure 8: Graph-Based RAG Workflow

Figure 9: ADW Workflow Diagram[Source]

Comparative Analysis of Agentic RAG Frameworks

The table below provides a comprehensive comparative analysis of the three architectural frameworks: Traditional RAG, Agentic RAG, and Agentic Document Workflows (ADW). This analysis highlights their respective strengths, weaknesses, and best-fit scenarios, offering valuable insights into their applicability across diverse use cases.
FeatureTraditional RAGAgentic RAGAgentic Document Workflows (ADW)FocusIsolated retrieval and generation tasksMulti-agent collaboration and reasoningDocument-centric end-to-end workflowsContext MaintenanceLimitedEnabled through memory modulesMaintains state across multi-step workflowsDynamic AdaptabilityMinimalHighTailored to document workflowsWorkflow OrchestrationAbsentOrchestrates multi-agent tasksIntegrates multi-step document processingUse of External Tools/APIsBasic integration (e.g., retrieval tools)Extends via tools like APIs and knowledge basesDeeply integrates business rules and domain-specific toolsScalabilityLimited to small datasets or queriesScalable for multi-agent systemsScales for multi-domain enterprise workflowsComplex ReasoningBasic (e.g., simple Q&A)Multi-step reasoning with agentsStructured reasoning across documentsPrimary ApplicationsQA systems, knowledge retrievalMulti-domain knowledge and reasoningContract review, invoice processing, claims analysisStrengthsSimplicity, quick setupHigh accuracy, collaborative reasoningEnd-to-end automation, domain-specific intelligenceChallengesPoor contextual understandingCoordination complexityResource overhead, domain standardization

Key Takeaways

Traditional RAG is best suited for simpler tasks requiring basic retrieval and generation capabilities.

Agentic RAG excels in multi-agent collaborative reasoning, making it suitable for more complex, multi-domain tasks.

Agentic Document Workflows (ADW) provide tailored, document-centric solutions for enterprise-scale applications like contract analysis and invoice processing.

Applications

Agentic Retrieval-Augmented Generation (RAG) systems have transformative potential across diverse industries, enabling intelligent retrieval, multi-step reasoning, and dynamic adaptation to complex tasks. Below are some key domains where Agentic RAG systems make a significant impact:

1. Healthcare and Personalized Medicine

Problem: Rapid retrieval and synthesis of medical knowledge for diagnostics, treatment planning, and research.

Applications:

Clinical decision support systems leveraging multi-modal data (e.g., patient records, medical literature).

Automating medical report generation with relevant contextual references.

Multi-hop reasoning for analyzing complex relationships (e.g., disease-to-symptom mappings or treatment-to-outcome correlations).

2. Education and Personalized Learning

Problem: Delivering personalized and adaptive learning experiences for diverse learners.

Applications:

Designing intelligent tutors capable of real-time knowledge retrieval and personalized feedback.

Generating customized educational content based on student progress and preferences.

Multi-agent systems for collaborative learning simulations.

3. Legal and Contract Analysis

Problem: Analyzing complex legal documents and extracting actionable insights.

Applications:

Contract summarization and clause comparison with contextual alignment to legal standards.

Retrieval of precedent cases and regulatory guidelines for compliance.

Iterative workflows for identifying inconsistencies or conflicts in contracts.

4. Finance and Risk Analysis

Problem: Analyzing large-scale financial datasets and identifying trends, risks, and opportunities.

Applications:

Automating the generation of financial summaries and investment recommendations.

Real-time fraud detection through multi-step reasoning and data correlation.

Scenario-based modeling for risk analysis using graph-based workflows.

5. Customer Support and Virtual Assistants

Problem: Providing contextually relevant and dynamic responses to customer queries.

Applications:

Building AI-powered virtual assistants for real-time customer support.

Adaptive systems that improve responses by learning from user feedback.

Multi-agent orchestration for handling complex, multi-query interactions.

6. Graph-Enhanced Applications in Multimodal Workflows

Problem: Tackling tasks requiring relational understanding and multi-modal data integration.

Applications:

Graph-based retrieval systems for connecting structured and unstructured data.

Enhanced reasoning workflows in domains like scientific research and knowledge management.

Synthesis of insights across text, images, and structured data for actionable outputs.

7. Document-Centric Workflows

Problem: Automating complex workflows involving document parsing, data extraction, and multi-step reasoning.

Applications:

Invoice Payments Workflow:

Parses invoices to extract key details (e.g., invoice number, vendor info, payment terms).

Retrieves related vendor contracts to verify terms and compliance.

Generates a payment recommendation report, including cost-saving suggestions (e.g., early payment discounts).

Contract Review:

Analyzes legal contracts for critical clauses and compliance issues.

Automatically identifies risks and provides actionable recommendations.

Insurance Claims Analysis:

Automates claims review, extracting policy terms and calculating payouts based on predefined rules.

Key Advantages:

State Maintenance: Tracks the document’s context across workflow stages.

Domain-Specific Intelligence: Applies tailored rules for industry-specific needs.

Scalability: Handles large volumes of enterprise documents efficiently.

Enhanced Productivity: Reduces manual effort and augments human expertise.

Challenges and Future Directions

While Agentic Retrieval-Augmented Generation (RAG) systems show immense promise, there are several challenges and research opportunities that remain unaddressed:

Challenges

Coordination Complexity in Multi-Agent Systems:

Managing communication and collaboration among multiple agents can lead to inefficiencies and increased computational overhead.

Balancing task assignments and resolving conflicts between agents remains a critical issue.

Ethical and Responsible AI:

Ensuring unbiased retrieval and decision-making in sensitive domains like healthcare and finance.

Addressing data privacy concerns and building transparent systems that adhere to ethical standards.

Scalability and Latency:

Scaling Agentic RAG systems to handle large datasets and high-volume queries without compromising response times.

Addressing latency in multi-agent and graph-based workflows.

Hybrid Human-Agent Collaboration:

Designing systems that effectively integrate human oversight with autonomous agents for tasks requiring domain expertise.

Maintaining user trust and control while leveraging the strengths of AI agents.

Expanding Multimodal Capabilities:

Integrating text, image, audio, and video data for richer and more comprehensive outputs.

Handling the complexity of multimodal reasoning in real-time applications.

Future Directions

Enhanced Agentic Orchestration:

Development of more robust coordination frameworks for hierarchical and multi-agent systems.

Incorporating adaptive learning mechanisms to dynamically improve task allocation.

Domain-Specific Applications:

Customizing Agentic RAG systems for niche domains like legal analysis, personalized education, and advanced scientific research.

Ethical AI and Governance Frameworks:

Building tools to monitor, explain, and mitigate biases in AI outputs.

Developing policies and guidelines for ethical deployment in high-stakes environments.

Efficient Graph-Based Reasoning:

Optimizing graph-based workflows for large-scale, real-world applications.

Exploring hybrid approaches that combine graph-based reasoning with neural networks.

Human-AI Synergy:

Designing intuitive interfaces and workflows to empower humans to interact effectively with Agentic RAG systems.

Focusing on explainability and user-centric design.

Implementation of RAG Agentic Taxonomy: Techniques and Tools

TechniqueToolsDescriptionNotebooksSingle Agentic RAGLangChain, FAISS, Athina AIUses AI agents to find and generate answers using tools like vectordb and web searches.View NotebookLlamaIndex, Vertex AI (Vector Store, Text Embedding, LLM), Google Cloud StorageDemonstrates a single-router Agentic RAG system using LlamaIndex with Vertex AI for context retrieval and response generation.View NotebookLangChain, IBM Granite-3-8B-Instruct, Watsonx.ai, Chroma DB, WebBaseLoaderBuilds an Agentic RAG system using IBM Granite-3-8B-Instruct model in Watsonx.ai to answer complex queries with external information.View NotebookLangGraph, Chroma, NVIDIA Inference Microservices (NIMs), Tavily Search APIThis system uses a router-based architecture to determine whether a query should be handled by a RAG pipeline (retrieving from a vector database) or a websearch pipeline. An AI agent evaluates the query's topic and routes it to the appropriate pipeline for information retrieval and response generation, ensuring accurate, relevant, and contextually augmented answers.View NotebookLlamaIndex, Redis, Amazon Bedrock, RedisVectorStore, LlamaParse, BedrockEmbedding, SemanticCacheThis system implements a ReAct agent-based RAG pipeline where the agent interacts with a Redis-backed index and vector store to retrieve and process data from a PDF document. It utilizes Amazon Bedrock embeddings and LlamaIndex to process the document, build embeddings, and handle retrieval-based augmented generation. Additionally, semantic caching optimizes the system by reducing redundant LLM queries for repeated or similar user questions, improving response times and efficiency.View NotebookMulti-Agent Agentic RAG OrchestratorAutoGen, SQL, AI Search IndexesThis orchestrator utilizes a multi-agent system to facilitate complex task execution through coordinated agent interactions. Using a factory pattern and various predefined strategies (e.g., classic_rag for retrieval-augmented generation and nl2sql for translating natural language to SQL), the system enables flexible, multi-agent collaboration for tasks like database querying and document retrieval. The orchestrator supports agent communication, iterative responses, and customizable strategies, offering a high level of adaptability for diverse use cases.View NotebookHierarchical Multi-Agent Agentic RAGWeaviate, ExaSearch, Groq, crewAIThis approach uses a hierarchical agentic architecture with multiple agents, each responsible for specific tasks or tools. A manager agent coordinates the work of specialized agents (such as WeaviateTool for internal document retrieval, ExaSearchTool for web searches, and Groq for fast AI inference) to handle complex queries. The flexible, task-oriented system can support various use cases such as QA and workflow automation.View NotebookCorrective RAGLangChain, LangGraph, Chromadb, Athina AIRefines relevant documents, removes irrelevant ones or does the web search.View NotebookLangChain, FAISS, HuggingFace Inference API, SmolAgents, HyDE, Self-QueryThis system incorporates query reformulation and self-query strategies to address limitations in traditional RAG systems. It performs iterative retrieval by critiquing the relevance of retrieved documents and re-querying as needed. The agent refines queries to improve semantic similarity and ensure higher accuracy. Self-grading mechanisms assess the quality of retrieved information, enhancing results through iterative improvement. The system aligns with Corrective RAG principles by reducing confabulations and improving retrieval relevance.View NotebookAdaptive RAGLangChain, LangGraph, FAISS, Athina AIAdjusts retrieval methods based on query type, using indexed data or web search.View NotebookReAct RAGLangChain, LangGraph, FAISS, Athina AISystem combining reasoning and retrieval for context-aware responsesSelf RAGLangChain, LangGraph, FAISS, Athina AIReflects on retrieved data to ensure accurate and complete responses.

Blogs and Tutorials on Agentic RAG

DeepLearning.AI: How agents can improve LLM performance. DeepLearning.AI

Weaviate Blog: What is agentic RAG? Weaviate Blog

LangGraph CRAG Tutorial: LangGraph CRAG: Contextualized retrieval-augmented generation tutorial. LangGraph CRAG

LangGraph Adaptive RAG Tutorial: LangGraph adaptive RAG: Adaptive retrieval-augmented generation tutorial. LangGraph Adaptive RAG. Accessed: 2025-01-14.

LlamaIndex Blog: Agentic RAG with LlamaIndex. LlamaIndex Blog

Hugging Face Cookbook. Agentic RAG: Turbocharge your retrieval-augmented generation with query reformulation and self-query. Hugging Face Cookbook

Hugging Face Agentic RAG: https://huggingface.co/docs/smolagents/en/examples/rag

Qdrant Blog. Agentic RAG: Combining RAG with agents for enhanced information retrieval. Qdrant Blog

Semantic Kernel: Semantic Kernel is an open-source SDK by Microsoft that integrates large language models (LLMs) into applications. It supports agentic patterns, enabling the creation of autonomous AI agents for natural language understanding, task automation, and decision-making. It has been used in scenarios like ServiceNow’s P1 incident management to facilitate real-time collaboration, automate task execution, and retrieve contextual information seamlessly.

GitHub - RAG with Semantic Kernel

GitHub - Semantic Kernel

ServiceNow Case Study

Practical Implementations and Use Cases of Agentic RAG

AWS Machine Learning Blog. How Twitch used agentic workflow with RAG on Amazon Bedrock to supercharge ad sales. AWS Machine Learning Blog

LlamaCloud Demo Repository. Patient case summary workflow using LlamaCloud. GitHub 2025. Accessed: 2025-01-13.

LlamaCloud Demo Repository. Contract review workflow using LlamaCloud. GitHub

LlamaCloud Demo Repository. Auto insurance claims workflow using LlamaCloud. GitHub

LlamaCloud Demo Repository. Research paper report generation workflow using LlamaCloud.GitHub

Noteworthy Related Concepts

Below are some noteworthy resources related to Agentic Design Patterns. The first five items are from Andrew Ng’s series at DeepLearning.ai:

Agentic Design Patterns Part 1
How Agents Can Improve LLM Performance

Agentic Design Patterns Part 2, Reflection
Read More

Agentic Design Patterns Part 3, Tool Use
Read More

Agentic Design Patterns Part 4, Planning
Read More

Agentic Design Patterns Part 5, Multi-Agent Collaboration
Read More

Additional Resources

Building Agentic RAG with LlamaIndex
Explore the Course

AI Agentic Design Patterns with AutoGen
Explore the Course

LangGraph Agentic RAG
Read More

References

Research Papers on Agentic RAG

1. Single-Agent RAG (Router-Based)

Search-o1: Agentic Search-Enhanced Large Reasoning Models https://arxiv.org/abs/2501.05366

2. Multi-Agent Agentic RAG

Agentic Retrieval-Augmented Generation for Time Series Analysis https://arxiv.org/abs/2408.14484

3. Corrective Agentic RAG

Agentic AI-Driven Technical Troubleshooting for Enterprise Systems https://arxiv.org/abs/2412.12006

Corrective RAG (CRAG) https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/

Corrective Retrieval Augmented Generation https://arxiv.org/abs/2401.15884

Agentic AI-Driven Technical Troubleshooting for Enterprise Systems https://arxiv.org/abs/2412.12006

4. Adaptive Agentic RAG

Langgraph Adaptive RAG https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/

MBA-RAG: A Bandit Approach for Adaptive Retrieval-Augmented https://arxiv.org/abs/2412.01572

CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control https://arxiv.org/abs/2405.18727

Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity https://arxiv.org/abs/2403.14403

AT-RAG: An Adaptive RAG Model Enhancing Query Efficiency with Topic Filtering and Iterative Reasoning https://arxiv.org/abs/2410.12886

5. Graph-Based Agentic RAG

GeAR: Graph-enhanced Agent for Retrieval-augmented Generation https://arxiv.org/abs/2412.18431

Agent-G: An Agentic Framework for Graph Retrieval Augmented Generation https://openreview.net/forum?id=g2C947jjjQ

How to Cite

If you find this work useful in your research, please cite:

@misc{singh2025agenticretrievalaugmentedgenerationsurvey,
 title={Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG}, 
 author={Aditi Singh and Abul Ehtesham and Saket Kumar and Tala Talaei Khoei},
 year={2025},
 eprint={2501.09136},
 archivePrefix={arXiv},
 primaryClass={cs.AI},
 url={https://arxiv.org/abs/2501.09136}, 
}

About

 Agentic-RAG explores advanced Retrieval-Augmented Generation systems enhanced with AI LLM agents. 
 

arxiv.org/abs/2501.09136

Topics

 reflection

 tools

 multiagent

 multi-agent-systems

 rag

 llm-agent

 agentic

 agentic-framework

 agentic-workflow

 agentic-rag

 agentic-ai

 agentic-pattern

Resources

 Readme

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Stars

1.6k
 stars

Watchers

12
 watching

Forks

177
 forks

 Report repository

Releases

No releases published

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

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

---
title: Going to production - Docs by LangChain
source_url: https://docs.langchain.com/oss/python/deepagents/going-to-production
final_url: https://docs.langchain.com/oss/python/deepagents/going-to-production
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:33:35.729610+00:00
---

# Going to production - Docs by LangChain

## 원본 URL

https://docs.langchain.com/oss/python/deepagents/going-to-production

## 주요 헤딩

- Going to production
- ​ Overview
- ​ LangSmith Deployments
- ​ Production considerations
- ​ Memory
- ​ Execution environment
- ​ Guardrails
- ​ Frontend

## 추출 본문

Going to production - Docs by LangChain
Skip to main content
Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. Buy tickets >
Docs by LangChain home page
Open source
Search...
⌘ K
Ask AI
GitHub
Try LangSmith
Try LangSmith
Search...
Navigation
Deployment
Going to production
Deep Agents
LangChain
LangGraph
Integrations
Learn
Reference
Contribute
Python
Overview
Get started
Quickstart
Customization
Comparison
Changelog
Deployment
Deploy with the CLI
Going to production
Core capabilities
Overview
Models
Context engineering
Backends
Subagents
Async subagents
Human-in-the-loop
Memory
Skills
Sandboxes
Streaming
Frontend
Overview
Patterns
Protocols
Agent Client Protocol (ACP)
Command line interface
Use the CLI
Model providers
Configuration
MCP Tools
On this page Overview
LangSmith Deployments
Production considerations
Multi-tenancy
User identity and access control
Team access control (RBAC)
End-user credentials
Async
Durability
Memory
Scoping
Configuration
Execution environment
Filesystem
Sandboxes
Lifecycle
File transfers
Managing secrets
Guardrails
Rate limiting
Handling errors
Data privacy
Frontend
Deployment
Going to production
Copy page
Take your Deep Agent to production with persistent memory, sandboxes, resilience middleware, and deployment options
Copy page
This guide covers considerations for taking a Deep Agent from a local prototype to a production deployment. It walks through scoping memory, configuring execution environments, adding guardrails, and connecting a frontend.
​
Overview
Agents use information from memory and their execution environment to accomplish tasks.
In production, there are a few primitives that determine how information is shared and accessed:
Thread : a single conversation. Message history and scratch files are scoped to the thread by default and don’t carry over.
User : someone interacting with your agent. Memory and files can be private to a user or shared across users. Identity and authorization comes from your auth layer .
Assistant : a configured agent instance. Memory and files can be tied to one assistant or shared across all of them.
This page covers:
LangSmith Deployments : managed infrastructure with auth, webhooks, and cron
Production considerations : multi-tenancy, authentication, credentials, async, and durability
Memory : persist information across conversations
Execution environment : file storage and code execution
Guardrails : rate limiting, error handling, and data privacy
Frontend : connect your UI to a deployed agent
​
LangSmith Deployments
The fastest way to get a Deep Agent into production is deepagents deploy
, which packages your agent configuration and deploys it as a LangSmith Deployment with one command. Alternatively, you can configure a LangSmith Deployment directly. Either path provisions the infrastructure your agent needs: assistants , threads , runs , a store, and a checkpointer, so you don’t have to set these up yourself. It also gives you authentication , webhooks , cron jobs , and observability out of the box, and can expose your agent via MCP or A2A .
For the CLI-based approach, see Deploy with the CLI . For manual setup, see the LangSmith Deployments quickstart .
All code snippets on this page use the following langgraph.json
unless otherwise specified:
langgraph.json
{
" dependencies " : [ "." ],
" graphs " : {
" agent " : "./agent.py:agent"
},
" env " : ".env"
}
langgraph.json
is the configuration file that tells the LangGraph platform how to build and run your application. It lives at the root of your project and is required for both local development (with langgraph dev
) and production deployment. The key fields are:
Field Description dependencies
Packages to install. ["."]
installs the current directory as a package (reads from requirements.txt
, pyproject.toml
, or package.json
). graphs
Maps graph IDs to their code locations. Each entry is "<id>": "./<file>:<variable>"
, where <id>
is the name you use to invoke the graph via the API, and <variable>
is the compiled graph or constructor function exported from <file>
. env
Path to a .env
file with environment variables (API keys, secrets). These are set at build time and available at runtime.
For the full set of configuration options (custom Docker steps, store indexing, auth handlers, and more), see application structure .
​
Production considerations
​
Multi-tenancy
When your agent serves multiple users, you need to handle three concerns: verifying who each user is, controlling what they can access, and managing the credentials the agent uses to act on their behalf.
​
User identity and access control
LangSmith Deployments supports custom authentication to establish user identity and authorization handlers to control access to resources like threads, assistants, and store namespaces. Authorization handlers run after authentication succeeds and can:
Tag resources with ownership metadata (e.g., owner: user_id
)
Return filters so users only see their own resources
Deny access with HTTP 403 for unauthorized operations
For a step-by-step tutorial, see Make conversations private .
How you scope memory and execution environments determines what data is shared between users. See the sections below for details.
​
Team access control (RBAC)
LangSmith’s role-based access control governs who on your team can deploy, configure, and monitor agents. This is separate from end-user authorization above.
Role Access Workspace Admin Full permissions including settings and member management Workspace Editor Create and modify resources, but cannot delete runs or manage members Workspace Viewer Read-only access
Custom roles with granular permissions are available on Enterprise plans. See the RBAC reference for the full permission model.
​
End-user credentials
When your agent needs to call external APIs on behalf of a user (e.g., reading their GitHub repos, sending Slack messages, querying their data warehouse), you need a way to pass the user’s credentials through to the agent without hardcoding them.
OAuth via Agent Auth. Agent Auth provides a managed OAuth 2.0 flow. Configure an OAuth provider, and the agent can request tokens scoped to each user. On first use, the agent interrupts execution and presents an OAuth consent URL. After the user authenticates, the agent resumes with a valid token. Tokens are stored and refreshed automatically.
from langchain_auth import Client
from langchain . tools import tool , ToolRuntime
auth_client = Client ()
# Inside your agent's tool:
@tool
async def github_action ( runtime : ToolRuntime ):
"""Perform an action on behalf of the user via GitHub."""
auth_result = await auth_client . authenticate (

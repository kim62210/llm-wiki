---
title: Quickstart - Docs by LangChain
source_url: https://docs.langchain.com/oss/python/langgraph/quickstart
final_url: https://docs.langchain.com/oss/python/langgraph/quickstart
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:26:43.238663+00:00
---

# Quickstart - Docs by LangChain

## 원본 URL

https://docs.langchain.com/oss/python/langgraph/quickstart

## 주요 헤딩

- Quickstart
- ​ 1. Define tools and model
- ​ 2. Define state
- ​ 3. Define model node
- ​ 4. Define tool node
- ​ 5. Define end logic
- ​ 6. Build and compile the agent
- ​ 1. Define tools and model
- ​ 2. Define model node
- ​ 3. Define tool node
- ​ 4. Define agent

## 추출 본문

Quickstart - Docs by LangChain
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
Get started
Quickstart
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
Install
Quickstart
Local server
Changelog
Thinking in LangGraph
Workflows + agents
Capabilities
Persistence
Durable execution
Streaming
Interrupts
Time travel
Memory
Subgraphs
Production
Application structure
Test
LangSmith Studio
Agent Chat UI
LangSmith Deployment
LangSmith Observability
Frontend
Overview
Graph execution
LangGraph APIs
Graph API
Functional API
Runtime
Get started
Quickstart
Copy page
Copy page
This quickstart demonstrates how to build a calculator agent using the LangGraph Graph API or the Functional API.
Using an AI coding assistant?
Install the LangChain Docs MCP server to give your agent access to up-to-date LangChain documentation and examples.
Install LangChain Skills to improve your agent’s performance on LangChain ecosystem tasks.
Use the Graph API if you prefer to define your agent as a graph of nodes and edges.
Use the Functional API if you prefer to define your agent as a single function.
For conceptual information, see Graph API overview and Functional API overview .
For this example, you will need to set up a Claude (Anthropic) account and get an API key. Then, set the ANTHROPIC_API_KEY
environment variable in your terminal.
Use the Graph API
Use the Functional API
​
1. Define tools and model
In this example, we’ll use the Claude Sonnet 4.5 model and define tools for addition, multiplication, and division.
from langchain . tools import tool
from langchain . chat_models import init_chat_model
model = init_chat_model (
"claude-sonnet-4-6" ,
temperature = 0
)
# Define tools
@tool
def multiply ( a : int , b : int ) -> int :
"""Multiply `a` and `b`.
Args:
a: First int
b: Second int
"""
return a * b
@tool
def add ( a : int , b : int ) -> int :
"""Adds `a` and `b`.
Args:
a: First int
b: Second int
"""
return a + b
@tool
def divide ( a : int , b : int ) -> float :
"""Divide `a` and `b`.
Args:
a: First int
b: Second int
"""
return a / b
# Augment the LLM with tools
tools = [ add , multiply , divide ]
tools_by_name = { tool . name : tool for tool in tools }
model_with_tools = model . bind_tools ( tools )
​
2. Define state
The graph’s state is used to store the messages and the number of LLM calls.
State in LangGraph persists throughout the agent’s execution. The Annotated
type with operator.add
ensures that new messages are appended to the existing list rather than replacing it.
from langchain . messages import AnyMessage
from typing_extensions import TypedDict , Annotated
import operator
class MessagesState ( TypedDict ):
messages : Annotated [ list [ AnyMessage ], operator . add ]
llm_calls : int
​
3. Define model node
The model node is used to call the LLM and decide whether to call a tool or not.
from langchain . messages import SystemMessage
def llm_call ( state : dict ):
"""LLM decides whether to call a tool or not"""
return {
"messages" : [
model_with_tools . invoke (
[
SystemMessage (
content = "You are a helpful assistant tasked with performing arithmetic on a set of inputs."
)
]
+ state [ " messages " ]
)
],
"llm_calls" : state . get ( 'llm_calls' , 0 ) + 1
}
​
4. Define tool node
The tool node is used to call the tools and return the results.

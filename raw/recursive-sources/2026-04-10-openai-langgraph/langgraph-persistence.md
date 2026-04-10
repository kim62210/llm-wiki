---
title: Persistence - Docs by LangChain
source_url: https://docs.langchain.com/oss/python/langgraph/persistence
final_url: https://docs.langchain.com/oss/python/langgraph/persistence
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:26:43.647859+00:00
---

# Persistence - Docs by LangChain

## 원본 URL

https://docs.langchain.com/oss/python/langgraph/persistence

## 주요 헤딩

- Persistence
- ​ Why use persistence
- ​ Core concepts
- ​ Get and update state
- ​ Memory store
- ​ Checkpointer libraries

## 추출 본문

Persistence - Docs by LangChain
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
Capabilities
Persistence
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
On this page Why use persistence
Core concepts
Threads
Checkpoints
Super-steps
Checkpoint namespace
Get and update state
Get state
StateSnapshot fields
Get state history
Find a specific checkpoint
Replay
Update state
Memory store
Basic usage
Semantic search
Using in LangGraph
Checkpointer libraries
Checkpointer interface
Serializer
Serialization with pickle
Encryption
Capabilities
Persistence
Copy page
Copy page
LangGraph has a built-in persistence layer that saves graph state as checkpoints. When you compile a graph with a checkpointer, a snapshot of the graph state is saved at every step of execution, organized into threads. This enables human-in-the-loop workflows, conversational memory, time travel debugging, and fault-tolerant execution.
Agent Server handles checkpointing automatically
When using the Agent Server , you don’t need to implement or configure checkpointers manually. The server handles all persistence infrastructure for you behind the scenes.
​
Why use persistence
Persistence is required for the following features:
Human-in-the-loop : Checkpointers facilitate human-in-the-loop workflows by allowing humans to inspect, interrupt, and approve graph steps. Checkpointers are needed for these workflows as the person has to be able to view the state of a graph at any point in time, and the graph has to be able to resume execution after the person has made any updates to the state. See Interrupts for examples.
Memory : Checkpointers allow for “memory” between interactions. In the case of repeated human interactions (like conversations) any follow up messages can be sent to that thread, which will retain its memory of previous ones. See Add memory for information on how to add and manage conversation memory using checkpointers.
Time travel : Checkpointers allow for “time travel” , allowing users to replay prior graph executions to review and / or debug specific graph steps. In addition, checkpointers make it possible to fork the graph state at arbitrary checkpoints to explore alternative trajectories.
Fault-tolerance : Checkpointing provides fault-tolerance and error recovery: if one or more nodes fail at a given superstep, you can restart your graph from the last successful step.
Pending writes : When a graph node fails mid-execution at a given super-step , LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that super-step. When you resume graph execution from that super-step you don’t re-run the successful nodes.
​
Core concepts
​
Threads
A thread is a unique ID or thread identifier assigned to each checkpoint saved by a checkpointer. It contains the accumulated state of a sequence of runs . When a run is executed, the state of the underlying graph of the assistant will be persisted to the thread.
When invoking a graph with a checkpointer, you must specify a thread_id
as part of the configurable
portion of the config:
{ "configurable" : { "thread_id" : "1" }}
A thread’s current and historical state can be retrieved. To persist state, a thread must be created prior to executing a run. The LangSmith API provides several endpoints for creating and managing threads and thread state. See the API reference for more details.
The checkpointer uses thread_id
as the primary key for storing and retrieving checkpoints. Without it, the checkpointer cannot save state or resume execution after an interrupt , since the checkpointer uses thread_id
to load the saved state.
​
Checkpoints
The state of a thread at a particular point in time is called a checkpoint. A checkpoint is a snapshot of the graph state saved at each super-step and is represented by a StateSnapshot
object (see StateSnapshot fields for the full field reference).
​
Super-steps
LangGraph created a checkpoint at each super-step boundary. A super-step is a single “tick” of the graph where all nodes scheduled for that step execute (potentially in parallel). For a sequential graph like START -> A -> B -> END
, there are separate super-steps for the input, node A, and node B — producing a checkpoint after each one. Understanding super-step boundaries is important for time travel , because you can only resume execution from a checkpoint (i.e., a super-step boundary).
Checkpoints are persisted and can be used to restore the state of a thread at a later time.
Let’s see what checkpoints are saved when a simple graph is invoked as follows:
from langgraph . graph import StateGraph , START , END
from langgraph . checkpoint . memory import InMemorySaver
from langchain_core . runnables import RunnableConfig
from typing import Annotated
from typing_extensions import TypedDict
from operator import add
class State ( TypedDict ):
foo : str
bar : Annotated [ list [ str ], add ]
def node_a ( state : State ):
return { "foo" : "a" , "bar" : [ "a" ]}
def node_b ( state : State ):
return { "foo" : "b" , "bar" : [ "b" ]}
workflow = StateGraph ( State )
workflow . add_node ( node_a )
workflow . add_node ( node_b )
workflow . add_edge ( START , "node_a" )
workflow . add_edge ( "node_a" , "node_b" )
workflow . add_edge ( "node_b" , END )
checkpointer = InMemorySaver ()
graph = workflow . compile ( checkpointer = checkpointer )
config : RunnableConfig = { "configurable" : { "thread_id" : "1" }}
graph . invoke ({ "foo" : "" , "bar" :[]}, config )
After we run the graph, we expect to see exactly 4 checkpoints:
Empty checkpoint with START
as the next node to be executed
Checkpoint with the user input {'foo': '', 'bar': []}

---
title: Sessions | OpenAI Agents SDK
source_url: https://openai.github.io/openai-agents-js/guides/sessions
final_url: https://openai.github.io/openai-agents-js/guides/sessions/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:26:42.735988+00:00
---

# Sessions | OpenAI Agents SDK

## 원본 URL

https://openai.github.io/openai-agents-js/guides/sessions

## 주요 헤딩

- Sessions
- Getting started
- Core session behavior
- Custom storage and merge behavior
- Resumable runs
- Advanced: history compaction

## 추출 본문

Sessions
Sessions give the Agents SDK a persistent memory layer . Provide any object that implements the Session
interface to Runner.run
, and the SDK handles the rest. When a session is present, the runner automatically:
Fetches previously stored conversation items and prepends them to the next turn.
Persists new user input and assistant output after each run completes.
Keeps the session available for future turns, whether you call the runner with new user text or resume from an interrupted RunState
.
This removes the need to manually call toInputList()
or stitch history between turns. The TypeScript SDK ships with two implementations: OpenAIConversationsSession
for the Conversations API and MemorySession
, which is intended for local development. Because they share the Session
interface, you can plug in your own storage backend. For inspiration beyond the Conversations API, explore the sample session backends under examples/memory/
(Prisma, file-backed, and more). When you use an OpenAI Responses model, wrap any session with OpenAIResponsesCompactionSession
to automatically shrink stored conversation history via responses.compact
.
Tip: To run the OpenAIConversationsSession
examples on this page, set the OPENAI_API_KEY
environment variable (or provide an apiKey
when constructing the session) so the SDK can call the Conversations API.
Use sessions when you want the SDK to manage client-side memory for you. If you are already using
OpenAI server-managed state with conversationId
or previousResponseId
, you usually do not also
need a session for the same conversation history.
Getting started
Section titled “Getting started”
Quick start
Section titled “Quick start”
Use OpenAIConversationsSession
to sync memory with the Conversations API , or swap in any other Session
implementation.
Use the Conversations API as session memory import { Agent , OpenAIConversationsSession , run } from '@openai/agents' ;
const agent = new Agent ({
name : 'TourGuide' ,
instructions : 'Answer with compact travel facts.' ,
});
// Any object that implements the Session interface works here. This example uses
// the built-in OpenAIConversationsSession, but you can swap in a custom Session.
const session = new OpenAIConversationsSession ();
const firstTurn = await run ( agent , 'What city is the Golden Gate Bridge in?' , {
session ,
});
console . log ( firstTurn . finalOutput ); // "San Francisco"
const secondTurn = await run ( agent , 'What state is it in?' , { session });
console . log ( secondTurn . finalOutput ); // "California"
Reusing the same session instance ensures the agent receives the full conversation history before every turn and automatically persists new items. Switching to a different Session
implementation requires no other code changes.
For local demos, tests, or process-local chat state, MemorySession
provides the same interface
without talking to OpenAI:
Use MemorySession for local state import { Agent , MemorySession , run } from '@openai/agents' ;
const agent = new Agent ({
name : 'TourGuide' ,
instructions : 'Answer with compact travel facts.' ,
});
const session = new MemorySession ();
const result = await run ( agent , 'What city is the Golden Gate Bridge in?' , {
session ,
});
console . log ( result . finalOutput );
OpenAIConversationsSession
constructor options:
Option Type Notes conversationId
string
Reuse an existing conversation instead of creating one lazily. client
OpenAI
Pass a preconfigured OpenAI client. apiKey
string
API key used when creating an internal OpenAI client. baseURL
string
Base URL for OpenAI-compatible endpoints. organization
string
OpenAI organization ID for requests. project
string
OpenAI project ID for requests.
MemorySession
constructor options:
Option Type Notes sessionId
string
Stable identifier for logs or tests. Generated automatically by default. initialItems
AgentInputItem[]
Seed the session with existing history. logger
Logger
Override the logger used for debug output.
MemorySession
stores everything in local process memory, so it is reset when your process exits.
If you need to pre-create a conversation ID before constructing the session, use
startOpenAIConversationsSession(client?)
and pass the returned ID as conversationId
.
Core session behavior
Section titled “Core session behavior”
How the runner uses sessions
Section titled “How the runner uses sessions”
Before each run it retrieves the session history, merges it with the new turn’s input, and passes the combined list to your agent.
After a non-streaming run one call to session.addItems()
persists both the original user input and the model outputs from the latest turn.
For streaming runs it writes the user input first and appends streamed outputs once the turn completes.
When resuming from RunResult.state
(for approvals or other interruptions) keep passing the same session
. The resumed turn is added to memory without re-preparing the input.
Inspecting and editing history
Section titled “Inspecting and editing history”
Sessions expose simple CRUD helpers so you can build “undo”, “clear chat”, or audit features.
Read and edit stored items import { OpenAIConversationsSession } from '@openai/agents' ;
import type { AgentInputItem } from '@openai/agents-core' ;
// Replace OpenAIConversationsSession with any other Session implementation that
// supports get/add/pop/clear if you store history elsewhere.
const session = new OpenAIConversationsSession ({
conversationId : 'conv_123' , // Resume an existing conversation if you have one.
});
const history = await session . getItems ();
console . log ( `Loaded ${ history . length } prior items.` );
const followUp : AgentInputItem [] = [
{
type : 'message' ,
role : 'user' ,
content : [{ type : 'input_text' , text : 'Let’s continue later.' }],
},
];
await session . addItems ( followUp );
const undone = await session . popItem ();
if ( undone ?. type === 'message' ) {
console . log ( undone . role ); // "user"
}
await session . clearSession ();
session.getItems()
returns the stored AgentInputItem[]
. Call popItem()
to remove the last entry—useful for user corrections before you rerun the agent.
Custom storage and merge behavior
Section titled “Custom storage and merge behavior”
Bring your own storage
Section titled “Bring your own storage”
Implement the Session
interface to back memory with Redis, DynamoDB, SQLite, or another datastore. Only five asynchronous methods are required.
Custom in-memory session implementation import { Agent , run } from '@openai/agents' ;
import { randomUUID } from '@openai/agents-core/_shims' ;
import { getLogger } from '@openai/agents-core' ;

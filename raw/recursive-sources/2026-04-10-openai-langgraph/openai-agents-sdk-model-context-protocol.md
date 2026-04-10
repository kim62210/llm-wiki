---
title: Model Context Protocol (MCP) | OpenAI Agents SDK
source_url: https://openai.github.io/openai-agents-js/guides/mcp
final_url: https://openai.github.io/openai-agents-js/guides/mcp/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:26:43.034211+00:00
---

# Model Context Protocol (MCP) | OpenAI Agents SDK

## 원본 URL

https://openai.github.io/openai-agents-js/guides/mcp

## 주요 헤딩

- Model Context Protocol (MCP)
- 1. Hosted MCP server tools
- 2. Streamable HTTP MCP servers
- 3. Stdio MCP servers
- Managing MCP server lifecycle
- Other things to know
- Further reading

## 추출 본문

Model Context Protocol (MCP)
The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide tools and context to LLMs. From the MCP docs:
MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.
There are three types of MCP servers this SDK supports:
Hosted MCP server tools – remote MCP servers used as tools by the OpenAI Responses API
Streamable HTTP MCP servers – local or remote servers that implement the Streamable HTTP transport
Stdio MCP servers – servers accessed via standard input/output (the simplest option)
Note: The SDK also includes MCPServerSSE
for legacy Server‑Sent Events transports, but SSE has been deprecated by the MCP project. Prefer Streamable HTTP or stdio for new integrations.
Choose a server type based on your use‑case:
What you need Recommended option Call publicly accessible remote servers with default OpenAI responses models 1. Hosted MCP tools Use publicly accessible remote servers but have the tool calls triggered locally 2. Streamable HTTP Use locally running Streamable HTTP servers 2. Streamable HTTP Use any Streamable HTTP servers with non-OpenAI-Responses models 2. Streamable HTTP Work with local MCP servers that only support the standard-I/O protocol 3. Stdio
1. Hosted MCP server tools
Section titled “1. Hosted MCP server tools”
Hosted tools push the entire round‑trip into the model. Instead of your code calling an MCP server, the OpenAI Responses API invokes the remote tool endpoint and streams the result back to the model.
Here is the simplest example of using hosted MCP tools. You can pass the remote MCP server’s label and URL to the hostedMcpTool
utility function, which is helpful for creating hosted MCP server tools.
hostedAgent.ts import { Agent , hostedMcpTool } from '@openai/agents' ;
export const agent = new Agent ({
name : 'MCP Assistant' ,
instructions : 'You must always use the MCP tools to answer questions.' ,
tools : [
hostedMcpTool ({
serverLabel : 'gitmcp' ,
serverUrl : 'https://gitmcp.io/openai/codex' ,
}),
],
});
Then, you can run the Agent with the run
function (or your own customized Runner
instance’s run
method):
Run with hosted MCP tools import { run } from '@openai/agents' ;
import { agent } from './hostedAgent' ;
async function main () {
const result = await run (
agent ,
'Which language is the repo I pointed in the MCP tool settings written in?' ,
);
console . log ( result . finalOutput );
}
main (). catch ( console . error );
To stream incremental MCP results, pass stream: true
when you run the Agent
:
Run with hosted MCP tools (streaming) import { isOpenAIResponsesRawModelStreamEvent , run } from '@openai/agents' ;
import { agent } from './hostedAgent' ;
async function main () {
const result = await run (
agent ,
'Which language is the repo I pointed in the MCP tool settings written in?' ,
{ stream : true },
);
for await ( const event of result ) {
if (
isOpenAIResponsesRawModelStreamEvent ( event ) &&
event . data . event . type !== 'response.mcp_call_arguments.delta' &&
event . data . event . type !== 'response.output_text.delta'
) {
console . log ( `Got event of type ${ JSON . stringify ( event . data ) } ` );
}
}
console . log ( `Done streaming; final result: ${ result . finalOutput } ` );
}
main (). catch ( console . error );
Optional approval flow
Section titled “Optional approval flow”
For sensitive operations you can require human approval of individual tool calls. Pass either requireApproval: 'always'
or a fine‑grained object mapping tool names to 'never'
/ 'always'
.
If you can programmatically determine whether a tool call is safe, you can use the onApproval
callback to approve or reject the tool call. If you require human approval, you can use the same human-in-the-loop (HITL) approach using interruptions
as for local function tools.
Human in the loop with hosted MCP tools import { Agent , run , hostedMcpTool , RunToolApprovalItem } from '@openai/agents' ;
async function main () : Promise < void > {
const agent = new Agent ({
name : 'MCP Assistant' ,
instructions : 'You must always use the MCP tools to answer questions.' ,
tools : [
hostedMcpTool ({
serverLabel : 'gitmcp' ,
serverUrl : 'https://gitmcp.io/openai/codex' ,
// 'always' | 'never' | { never, always }
requireApproval : {
never : {
toolNames : [ 'search_codex_code' , 'fetch_codex_documentation' ],
},
always : {
toolNames : [ 'fetch_generic_url_content' ],
},
},
}),
],
});
let result = await run ( agent , 'Which language is this repo written in?' );
while ( result . interruptions && result . interruptions . length ) {
for ( const interruption of result . interruptions ) {
// Human in the loop here
const approval = await confirm ( interruption );
if ( approval ) {
result . state . approve ( interruption );
} else {
result . state . reject ( interruption );
}
}
result = await run ( agent , result . state );
}
console . log ( result . finalOutput );
}
import { stdin , stdout } from 'node:process' ;
import * as readline from 'node:readline/promises' ;
async function confirm ( item : RunToolApprovalItem ) : Promise < boolean > {
const rl = readline . createInterface ({ input : stdin , output : stdout });
const name = item . name ;
const params = item . arguments ;
const answer = await rl . question (
`Approve running tool (mcp: ${ name } , params: ${ params } )? (y/n) ` ,
);
rl . close ();
return answer . toLowerCase (). trim () === 'y' ;
}
main (). catch ( console . error );
{ const agent = new Agent({ name: 'MCP Assistant', instructions: 'You must always use the MCP tools to answer questions.', tools: [ hostedMcpTool({ serverLabel: 'gitmcp', serverUrl: 'https://gitmcp.io/openai/codex', // 'always' | 'never' | { never, always } requireApproval: { never: { toolNames: ['search_codex_code', 'fetch_codex_documentation'], }, always: { toolNames: ['fetch_generic_url_content'], }, }, }), ], }); let result = await run(agent, 'Which language is this repo written in?'); while (result.interruptions && result.interruptions.length) { for (const interruption of result.interruptions) { // Human in the loop here const approval = await confirm(interruption); if (approval) { result.state.approve(interruption); } else { result.state.reject(interruption); } } result = await run(agent, result.state); } console.log(result.finalOutput);}import { stdin, stdout } from 'node:process';import * as readline from 'node:readline/promises';async function confirm(item: RunToolApprovalItem): Promise { const rl = readline.createInterface({ input: stdin, output: stdout }); const name = item.name; const params = item.arguments; const answer = await rl.question( `Approve running tool (mcp: ${name}, params: ${params})? (y/n) `, ); rl.close(); return answer.toLowerCase().trim() === 'y';}main().catch(console.error);">
Hosted MCP options reference
Section titled “Hosted MCP options reference”
hostedMcpTool(...)
supports both MCP server URLs and connector-backed servers:
Option Type Notes serverLabel
string
Required label that identifies the hosted MCP server in events and traces. serverUrl
string
Remote MCP server URL (use this for regular hosted MCP servers). connectorId
string
OpenAI connector id (use this instead of serverUrl
for connector-backed hosted servers). authorization
string
Optional authorization token sent to the hosted MCP backend. headers
Record<string, string>
Optional extra request headers. allowedTools
string[] | object

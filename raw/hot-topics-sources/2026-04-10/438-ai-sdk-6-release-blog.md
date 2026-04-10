---
title: AI SDK 6 - Vercel
source_url: https://vercel.com/blog/ai-sdk-6
final_url: https://vercel.com/blog/ai-sdk-6
status: 200
content_type: text/html; charset=utf-8
topics: [Vercel AI SDK 6]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:28.708927+00:00
---

# AI SDK 6 - Vercel

## 원본 URL

https://vercel.com/blog/ai-sdk-6

## 추출 본문

AI SDK 6 - Vercel

Skip to content

Products

AI Cloud

v0

Build applications with AI

AI SDK

The AI Toolkit for TypeScript

AI Gateway

One endpoint, all your models

Vercel Agent

An agent that knows your stack

Sandbox

AI workflows in live environments

Core Platform

CI/CD

Helping teams ship 6× faster

Content Delivery

Fast, scalable, and reliable

Fluid Compute

Servers, in serverless form

Observability

Trace every step

Security

Bot Management

Scalable bot protection

BotID

Invisible CAPTCHA

Platform Security

DDoS Protection, Firewall

Web Application Firewall

Granular, custom protection

Resources

Company

Customers

Trusted by the best teams

Blog

The latest posts and changes

Changelog

See what shipped

Press

Read the latest news

Events

Join us at an event

Learn

Docs

Vercel documentation

Academy

Linear courses to level up

Knowledge Base

Find help quickly

Community

Join the conversation

Open Source

Next.js

The native Next.js platform

Nuxt

The progressive web framework

Svelte

The web’s efficient UI framework

Turborepo

Speed with Enterprise scale

Solutions

Use Cases

AI Apps

Deploy at the speed of AI

Composable Commerce

Power storefronts that convert

Marketing Sites

Launch campaigns fast

Multi-tenant Platforms

Scale apps with one codebase

Web Apps

Ship features, not infrastructure

Tools

Marketplace

Extend and automate workflows

Templates

Jumpstart app development

Partner Finder

Get help from solution partners

Users

Platform Engineers

Automate away repetition

Design Engineers

Deploy for every idea

Enterprise

Pricing

Log InContact

Sign Up
Sign Up

Blog/Engineering

AI SDK 6

Authors

12 min read

Copy URL

Copied to clipboard!

Dec 22, 2025

Introducing agents, tool execution approval, DevTools, full MCP support, reranking, image editing, and more.

With over 20 million monthly downloads and adoption by teams ranging from startups to Fortune 500 companies, the AI SDK is the leading TypeScript toolkit for building AI applications. It provides a unified API, allowing you to integrate with any AI provider, and seamlessly integrates with Next.js, React, Svelte, Vue, and Node.js. The AI SDK enables you to build everything from chatbots to complex background agents.

Thomson Reuters used the AI SDK to build CoCounsel, their AI assistant for attorneys, accountants, and audit teams, with just 3 developers in 2 months. Now serving 1,300 accounting firms, they're migrating their entire codebase to the AI SDK, deprecating thousands of lines of code across 10 providers and consolidating into one composable, scalable system.

Clay used it to build Claygent, their AI web research agent that scrapes public data, connects to first-party sources via MCP servers, and helps sales teams find accounts with custom, targeted insights.

“We’ve gone all in on the AI SDK. Its agentic capabilities and TypeScript-first design power our AI web research agent (Claygent) at massive scale. It's been a huge help as we build agents for sourcing, qualification, and surfacing the right accounts and prospects for our customers.We’ve gone all in on the AI SDK. Its agentic capabilities and TypeScript-first design power our AI web research agent (Claygent) at massive scale. It's been a huge help as we build agents for sourcing, qualification, and surfacing the right accounts and prospects for our customers.”

Jeff Barg, Clay

Today, we are releasing AI SDK 6, which introduces:

Agents

Tool Improvements

MCP

Tool Calling with Structured Output

DevTools

Reranking

Standard JSON Schema

Image Editing

Raw Finish Reason & Extended Usage

LangChain Adapter Rewrite

New Provider Tools

Upgrading from AI SDK 5? Run 
npx @ai-sdk/codemod v6
 to migrate automatically with minimal code changes.

Link to headingAgents

AI SDK 6 introduces the 
Agent
 abstraction for building reusable agents. Define your agent once with its model, instructions, and tools, then use it across your entire application. Agents automatically integrate with the full AI SDK ecosystem, giving you type-safe UI streaming, structured outputs, and seamless framework support.

The functional approach with 
generateText
 and 
streamText
 is powerful and low-level, giving you full control regardless of scale. But when you want to reuse the same agent across different mediums (a chat UI, a background job, an API endpoint), or organize your code with tools in separate files, the inline configuration approach breaks down. You end up passing the same configuration object everywhere or building your own abstraction layer.

Link to headingToolLoopAgent

The 
ToolLoopAgent
 class provides a production-ready implementation that handles the complete tool execution loop. It calls the LLM with your prompt, executes any requested tool calls, adds results back to the conversation, and repeats until complete (for up to 20 steps by default: 
stopWhen: stepCountIs(20)
).

1
import{ ToolLoopAgent }from'ai';

2
import{ weatherTool }from'@/tools/weather';

3

4
exportconst weatherAgent =newToolLoopAgent({

5
 model:'anthropic/claude-sonnet-4.5',

6
 instructions:'You are a helpful weather assistant.',

7
 tools:{

8
 weather: weatherTool,

9
},

10
});

11

12
const result =await weatherAgent.generate({

13
 prompt:'What is the weather in San Francisco?',

14
});

To learn more, check out the Building Agents documentation.

Link to headingCall Options

With call options, you can pass type-safe arguments when you call 
generate
 or 
stream
 on a ToolLoopAgent. For example, you can use them to inject retrieved documents for RAG, select models based on request complexity, or customize tool behavior per request.

1
import{ ToolLoopAgent }from"ai";

2
import{ z }from"zod";

3

4
const supportAgent =newToolLoopAgent({

5
 model:"anthropic/claude-sonnet-4.5",

6
 callOptionsSchema: z.object({

7
 userId: z.string(),

8
 accountType: z.enum(["free","pro","enterprise"]),

9
}),

10
prepareCall:({ options,...settings })=>({

11
...settings,

12
 instructions:`You are a helpful customer support agent.

13
- User Account type: ${options.accountType}

14
- User ID: ${options.userId}`,

15
}),

16
});

17

18
const result =await supportAgent.generate({

19
 prompt:"How do I upgrade my account?",

20
 options:{

21
 userId:"user_123",

22
 accountType:"free",

23
},

24
});

To learn more, check out the Configuring Call Options documentation.

Link to headingCode Organization & UI Integration

The agent abstraction pushes you toward a clean separation of concerns and rewards you with end-to-end type safety. Define tools in dedicated files, compose them into agents, and expose them via API routes. The same definitions that power your agent logic also type your UI components.

1
// agents/weather-agent.ts

2
import{ ToolLoopAgent, InferAgentUIMessage }from"ai";

3
import{ weatherTool }from"@/tools/weather-tool";

4

5
exportconst weatherAgent =newToolLoopAgent({

6
 model:"anthropic/claude-sonnet-4.5",

7
 instructions:"You are a helpful weather assistant.",

8
 tools:{ weather: weatherTool },

9
});

10

11
exporttypeWeatherAgentUIMessage= InferAgentUIMessage<typeof weatherAgent>;

12

13
// app/api/chat/route.ts

14
import{ createAgentUIStreamResponse }from"ai";

15
import{ weatherAgent }from"@/agents/weather-agent";

16

17
exportasyncfunctionPOST(request: Request){

18
const{ messages }=await request.json();

19
returncreateAgentUIStreamResponse({

20
 agent: weatherAgent,

21
 uiMessages: messages,

22
});

23
}

On the client, types flow automatically. Import the message type from your agent file, then render typed tool components by switching on the part type.

1
// app/page.tsx

2
import{ useChat }from'@ai-sdk/react';

3
importtype{WeatherAgentUIMessage}from'@/agents/weather-agent';

4
import{WeatherToolView}from'@/components/weather-tool-view';

5

6
exportdefaultfunctionChat(){

7
const{ messages, sendMessage }=useChat<WeatherAgentUIMessage>();

8
return(

9
<div>

10
{messages.map((message)=>

11
 message.parts.map((part)=>{

12
switch(part.type){

13
case'tool-weather':

14
return<WeatherToolViewinvocation={part}/>;

15
}

16
})

17
)}

18
</div>

19
);

20
}

21

22
// components/weather-tool-view.tsx

23
import{UIToolInvocation}from'ai';

24
import{ weatherTool }from'@/tools/weather-tool';

25

26
exportfunctionWeatherToolView({

27
 invocation,

28
}:{

29
 invocation:UIToolInvocation<typeof weatherTool>;

30
}){

31
return(

32
<div>

33
 Weather in {invocation.input.location} is {invocation.output?.temperature}°F

34
</div>

35
);

36
}

Define once, use everywhere. The same tool definition powers your agent logic, API responses, and UI components.

To learn more, check out the Agents documentation.

Link to headingCustom Agent Implementations

In AI SDK 6, 
Agent
 is an interface rather than a class. While 
ToolLoopAgent
 provides a solid default implementation for most use cases, you can implement the 
Agent
 interface to build your own agent abstractions for your needs.

One such example is Workflow DevKit, which provides 
DurableAgent
. It makes your agents production-ready by turning them into durable, resumable workflows where each tool execution becomes a retryable, observable step.

1
import{ getWritable }from'workflow';

2
import{ DurableAgent }from'@workflow/ai/agent';

3
import{ searchFlights, bookFlight, getFlightStatus }from'./tools';

4

5
exportasyncfunctionflightBookingWorkflow(){

6
'use workflow';

7

8
const flightAgent =newDurableAgent({

9
 model:'anthropic/claude-sonnet-4.5',

10
 system:'You are a flight booking assistant.',

11
 tools:{

12
 searchFlights,

13
 bookFlight,

14
 getFlightStatus,

15
},

16
});

17

18
const result =await flightAgent.generate({

19
 prompt:'Find me a flight from NYC to London next Friday.',

20
 writable:getWritable(),

21
});

22
}

Learn more in the Building Durable Agents documentation.

Link to headingTool Improvements

Tools are the foundation of your agents' capabilities. An agent's ability to take meaningful actions depends entirely on how reliably it can generate valid tool inputs, how well those inputs align with your intent, how efficiently tool outputs can be represented as tokens in the conversation, and how safely those tools can execute in production environments.

AI SDK 6 improves each of these areas: tool execution approval for human-in-the-loop control, strict mode for more reliable input generation, input examples for better alignment, and 
toModelOutput
 for flexible tool outputs.

Link to headingTool Execution Approval

Building agents that can take real-world actions (deleting files, processing payments, modifying production data) requires a critical safety layer: human approval. Without it, you're blindly trusting the agent on every decision.

In AI SDK 6, you get human-in-the-loop control with a single 
needsApproval
 flag, no custom code required. See this feature in action with the Chat SDK, an open-source template for building chatbot applications. 

By default, tools run automatically when the model calls them. Set 
needsApproval: true
 to require approval before execution:

1
import{ tool }from'ai';

2
import{ z }from'zod';

3

4
exportconst runCommand =tool({

5
 description:'Run a shell command',

6
 inputSchema: z.object({

7
 command: z.string().describe('The shell command to execute'),

8
}),

9
 needsApproval:true,// Require user approval

10
execute:async({ command })=>{

11
// Your command execution logic here

12
},

13
});

Not every tool call needs approval. A simple ls command might be fine to auto-approve, but a destructive 
rm -rf
 command should require review. You can pass a function to 
needsApproval
 to decide based on the input, and store user preferences to remember approved patterns for future calls.

1
import{ tool }from"ai";

2
import{ z }from"zod";

3

4
const runCommand =tool({

5
 description:"Run a shell command",

6
 inputSchema: z.object({

7
 command: z.string().describe("The shell command to execute"),

8
}),

9
needsApproval:async({ command })=> command.includes("rm -rf"),

10
execute:async({ command })=>{

11
/* command execution logic */

12
},

13
});

Handling approval in your UI is straightforward with 
useChat
. Check the tool invocation state, prompt the user, and return a response with 
addToolApprovalResponse
:

1
import{ChatAddToolApproveResponseFunction}from'ai';

2
import{ runCommand }from'./tools/command-tool';

3

4
exportfunctionCommandToolView({

5
 invocation,

6
 addToolApprovalResponse,

7
}:{

8
 invocation:UIToolInvocation<typeof runCommand>;

9
 addToolApprovalResponse:ChatAddToolApproveResponseFunction;

10
}){

11
if(invocation.state==='approval-requested'){

12
return(

13
<div>

14
<p>Run command: {invocation.input.command}?</p>

15
<button

16
onClick={()=>

17
addToolApprovalResponse({

18
 id: invocation.approval.id,

19
 approved:true,

20
})

21
}

22
>

23
 Approve

24
</button>

25
<button

26
onClick={()=>

27
addToolApprovalResponse({

28
 id: invocation.approval.id,

29
 approved:false,

30
})

31
}

32
>

33
 Deny

34
</button>

35
</div>

36
);

37
}

38

39
if(invocation.state==='output-available'){

40
return<div>Output: {invocation.output}</div>;

41
}

42

43
// Handle other states...

44
}

45

To learn more, check out the Tool Execution Approval documentation.

Link to headingStrict Mode

When available, native strict mode from language model providers guarantees that tool call inputs match your schema exactly. However, some providers only support subsets of the JSON schema specification in strict mode. If any tool in your request uses an incompatible schema feature, the entire request fails.

AI SDK 6 makes strict mode opt-in per tool. Use strict mode for tools with compatible schemas and regular mode for others, all in the same call.

1
tool({

2
 description:'Get the weather in a location',

3
 inputSchema: z.object({

4
 location: z.string(),

5
}),

6
 strict:true,// Enable strict validation for this tool

7
execute:async({ location })=>({

8
// ...

9
}),

10
});

Link to headingInput Examples

Complex tool schemas with nested objects, specific formatting requirements, or domain-specific patterns can be difficult to describe clearly through tool descriptions alone. Even with detailed per-field descriptions, models sometimes generate inputs that are technically valid but don't match your expected patterns.

Input examples show the model concrete instances of correctly structured input, clarifying expectations that are hard to express in schema descriptions:

1
tool({

2
 description:'Get the weather in a location',

3
 inputSchema: z.object({

4
 location: z.string().describe('The location to get the weather for'),

5
}),

6
 inputExamples:[

7
{ input:{ location:'San Francisco'}},

8
{ input:{ location:'London'}},

9
],

10
execute:async({ location })=>{

11
// ...

12
},

13
});

Input examples are currently only natively supported by Anthropic. For providers that don't support them, you can use 
addToolInputExamplesMiddleware
 to append the examples to the tool description. If no middleware is used and the provider doesn't support input examples, they are ignored and not sent to the provider.

Link to headingSend Custom Tool Output to the Model

By default, whatever you return from your tool's 
execute
 function is sent to the model in subsequent turns as stringified JSON. However, when tools return large text outputs (file contents, search results) or binary data (screenshots, generated images), you end up sending thousands of unnecessary tokens or awkwardly encoding images as base64 strings.

The 
toModelOutput
 function separates what your tool result from what you send to the model. Return complete data from 
execute
 function for your application logic, then use 
toModelOutput
 to control exactly what tokens go back to the model:

1
import{ tool }from"ai";

2
import{ z }from"zod";

3

4
const weatherTool =tool({

5
 description:"Get the weather in a location",

6
 inputSchema: z.object({

7
 location: z.string().describe("The location to get the weather for"),

8
}),

9
execute:({ location })=>({

10
 temperature:72+ Math.floor(Math.random()*21)-10,

11
}),

12
// toModelOutput can be sync or async

13
toModelOutput:async({ input, output, toolCallId })=>{

14
// many other options, including json, multi-part with files and images, etc.

15
// (support depends on provider)

16
// example: send tool output as a text

17
return{

18
 type:"text",

19
 value:

20
`The weather in ${input.location} is ${output.temperature}°F.`,

21
};

22
},

23
});

To learn more, check out the Tool Calling documentation.

Link to headingMCP

AI SDK 6 extends our MCP support to cover OAuth authentication, resources, prompts, and elicitation. You can now expose data through resources, create reusable prompt templates, and handle server-initiated requests for user input. It is now stable and available in the 
@ai-sdk/mcp
 package.

Link to headingHTTP Transport

To connect to a remote MCP server, you configure an HTTP transport with your server URL and authentication headers:

1
import{ createMCPClient }from'@ai-sdk/mcp';

2

3
const mcpClient =awaitcreateMCPClient({

4
 transport:{

5
 type:'http',

6
 url:'<https://your-server.com/mcp>',

7
 headers:{ Authorization:'Bearer my-api-key'},

8
},

9
});

10

11
const tools =await mcpClient.tools();

Link to headingOAuth Authentication

Remote MCP servers often require authentication, especially hosted services that access user data or third-party APIs. Implementing OAuth correctly means handling PKCE challenges, token refresh, dynamic client registration, and retry logic when tokens expire mid-session. Getting any of this wrong breaks your integration.

AI SDK 6 handles the complete OAuth flow for you:

1
import{ createMCPClient, auth, OAuthClientProvider }from"@ai-sdk/mcp";

2

3
const authProvider: OAuthClientProvider ={

4
 redirectUrl:"http://localhost:3000/callback",

5
 clientMetadata:{

6
 client_name:"My App",

7
 redirect_uris:["http://localhost:3000/callback"],

8
 grant_types:["authorization_code","refresh_token"],

9
},

10
// Token and credential storage methods

11
tokens:async()=>{/* ... */},

12
saveTokens:async(tokens)=>{/* ... */},

13
// ... remaining OAuthClientProvider configuration

14
};

15

16
awaitauth(authProvider,{ serverUrl:newURL("https://mcp.example.com")});

17

18
const client =awaitcreateMCPClient({

19
 transport:{ type:"http", url:"https://mcp.example.com", authProvider },

20
});

Link to headingResources and Prompts

MCP servers can expose data through resources (files, database records, API responses) that your application can discover and read. Prompts provide reusable templates from the server, complete with parameters you fill in at runtime:

1
// List and read resources

2
const resources =await mcpClient.listResources();

3
const resourceData =await mcpClient.readResource({

4
 uri:"file:///example/document.txt",

5
});

6

7
// List and get prompts

8
const prompts =await mcpClient.experimental_listPrompts();

9
const prompt =await mcpClient.experimental_getPrompt({

10
 name:"code_review",

11
 arguments:{ code:"function add(a, b) { return a + b; }"},

12
});

Link to headingElicitation Support

Sometimes an MCP server needs user input mid-operation (a confirmation, a choice between options, or additional context). Elicitation lets the server request this input while your application handles gathering it:

1
const mcpClient =awaitcreateMCPClient({

2
 transport:{ type:'sse', url:'<https://your-server.com/sse>'},

3
 capabilities:{ elicitation:{}},

4
});

5

6
mcpClient.onElicitationRequest(ElicitationRequestSchema,async request =>{

7
const userInput =awaitgetInputFromUser(

8
 request.params.message,

9
 request.params.requestedSchema,

10
);

11

12
return{

13
 action:'accept',

14
 content: userInput,

15
};

16
});

17

To learn more, check out the MCP Tools documentation.

Link to headingTool Calling with Structured Output

Previously, combining tool calling with structured output required chaining 
generateText
 and 
generateObject
 together. AI SDK 6 unifies 
generateObject
 and 
generateText
 to enable multi-step tool calling loops with structured output generation at the end.

1
import{ Output, ToolLoopAgent, tool }from"ai";

2
import{ z }from"zod";

3

4
const agent =newToolLoopAgent({

5
 model:"anthropic/claude-sonnet-4.5",

6
 tools:{

7
 weather:tool({

8
 description:"Get the weather in a location",

9
 inputSchema: z.object({ city: z.string()}),

10
execute:async({ city })=>{

11
// ...

12
},

13
}),

14
},

15
 output: Output.object({

16
 schema: z.object({

17
 summary: z.string(),

18
 temperature: z.number(),

19
 recommendation: z.string(),

20
}),

21
}),

22
});

23

24
const{ output }=await agent.generate({

25
 prompt:"What is the weather in San Francisco and what should I wear?",

26
});

Link to headingOutput Types

Structured output supports several formats. Use the 
Output
 object to specify what shape you need:

Output.object()
: Generate structured objects

Output.array()
: Generate arrays of structured objects

Output.choice()
: Select from a specific set of options

Output.json()
: Generate unstructured JSON

Output.text()
: Generate plain text (default behavior)

To learn more, check out the Generating Structured Data documentation.

Link to headingDevTools

Debugging multi-step agent flows is difficult. A small change in context or input tokens at one step can meaningfully change that step's output, which changes the input to the next step, and so on. By the end, the trajectory is completely different, and tracing back to what caused it means manually logging each step and piecing together the sequence yourself.

AI SDK DevTools gives you full visibility into your LLM calls and agents. Inspect each step of any call, including input, output, model configuration, token usage, timing, and raw provider requests and responses.

Link to headingSetup

To get started, wrap your model with the 
devToolsMiddleware
:

1
import{ wrapLanguageModel, gateway }from'ai';

2
import{ devToolsMiddleware }from'@ai-sdk/devtools';

3

4
const devToolsEnabledModel =wrapLanguageModel({

5
 model:gateway('anthropic/claude-sonnet-4.5'),

6
 middleware:devToolsMiddleware(),

7
});

Then use it with any AI SDK function:

1
import{ generateText }from'ai';

2

3
const result =awaitgenerateText({

4
 model: devToolsEnabledModel,

5
 prompt:'What is love?',

6
});

Link to headingInspecting Your Runs

Launch the viewer with 
npx @ai-sdk/devtools
 and open http://localhost:4983 to inspect your runs. You'll be able to see:

Input parameters and prompts: View the complete input sent to your LLM

Output content and tool calls: Inspect generated text and tool invocations

Token usage and timing: Monitor resource consumption and performance

Raw provider data: Access complete request and response payloads

To learn more, check out the DevTools documentation.

Link to headingReranking

Providing relevant context to a language model isn't just about retrieving everything that might be related. Models perform better with focused, highly relevant context. Reranking reorders search results based on their relevance to a specific query, letting you pass only the most relevant documents to the model.

AI SDK 6 adds native support for reranking with the new 
rerank
 function:

1
import{ rerank }from'ai';

2
import{ cohere }from'@ai-sdk/cohere';

3

4
const documents =[

5
'sunny day at the beach',

6
'rainy afternoon in the city',

7
'snowy night in the mountains',

8
];

9

10
const{ ranking }=awaitrerank({

11
 model: cohere.reranking('rerank-v3.5'),

12
 documents,

13
 query:'talk about rain',

14
 topN:2,

15
});

16

17
console.log(ranking);

18
// [

19
// { originalIndex: 1, score: 0.9, document: 'rainy afternoon in the city' },

20
// { originalIndex: 0, score: 0.3, document: 'sunny day at the beach' }

21
// ]

Link to headingStructured Document Reranking

Reranking also supports structured documents, making it ideal for searching through databases, emails, or other structured content:

1
import{ rerank }from'ai';

2
import{ cohere }from'@ai-sdk/cohere';

3

4
const documents =[

5
{ from:'Paul Doe', subject:'Follow-up', text:'20% discount offer...'},

6
{

7
 from:'John McGill',

8
 subject:'Missing Info',

9
 text:'Oracle pricing: $5000/month',

10
},

11
];

12

13
const{ rerankedDocuments }=awaitrerank({

14
 model: cohere.reranking('rerank-v3.5'),

15
 documents,

16
 query:'Which pricing did we get from Oracle?',

17
 topN:1,

18
});

The 
rerank
 function currently supports Cohere, Amazon Bedrock, and Together.ai.

To learn more, check out the Reranking documentation.

Link to headingStandard JSON Schema

AI SDK 6 adds support for any schema library that implements the Standard JSON Schema interface. Previously, the SDK required built-in converters for each schema library (Arktype, Valibot). Now, any library implementing the Standard JSON Schema V1 specification works automatically without additional SDK changes.

1
import{ generateText, Output }from'ai';

2
import{ type }from'arktype';

3

4
const result =awaitgenerateText({

5
 model:'anthropic/claude-sonnet-4.5',

6
 output: Output.object({

7
 schema:type({

8
 recipe:{

9
 name:'string',

10
 ingredients:type({ name:'string', amount:'string'}).array(),

11
 steps:'string[]',

12
},

13
}),

14
}),

15
 prompt:'Generate a lasagna recipe.',

16
});

To learn more, check out the Tools documentation.

Link to headingProvider Tools

AI SDK 6 expands support for provider-specific tools that leverage unique platform capabilities and model-trained functionality. These tools are designed to work with specific models or platforms (such as web search, code execution, and memory management) where providers have optimized their models for these capabilities or offer platform-specific features that aren't available elsewhere.

Link to headingAnthropic Provider Tools

Memory Tool: Store and retrieve information across conversations through a memory file directory

Tool Search (Regex): Search and select tools dynamically using regex patterns

Tool Search (BM25): Search and select tools using natural language queries

Code Execution Tool: Run code in a secure sandboxed environment with bash and file operations

1
import{ anthropic }from"@ai-sdk/anthropic";

2

3
// Memory Tool - store and retrieve information

4
const memory = anthropic.tools.memory_20250818({

5
execute:async(action)=>{

6
// Implement memory storage logic

7
// Supports: view, create, str_replace, insert, delete, rename

8
},

9
});

10

11
// Tool Search (Regex) - find tools by pattern

12
const toolSearchRegex = anthropic.tools.toolSearchRegex_20251119();

13

14
// Tool Search (BM25) - find tools with natural language

15
const toolSearchBm25 = anthropic.tools.toolSearchBm25_20251119();

16

17
// Code Execution Tool - run code in sandbox

18
const codeExecution = anthropic.tools.codeExecution_20250825();

AI SDK 6 also adds support for programmatic tool calling, which allows Claude to call your tools from a code execution environment, keeping intermediate results out of context. This can significantly reduce token usage and cost.

Mark tools as callable from code execution with 
allowedCallers
, and use 
prepareStep
 to preserve the container across steps:

1
import{

2
 anthropic,

3
 forwardAnthropicContainerIdFromLastStep,

4
}from"@ai-sdk/anthropic";

5

6
const getWeather =tool({

7
 description:"Get weather for a city.",

8
 inputSchema: z.object({ city: z.string()}),

9
execute:async({ city })=>({ temp:22}),

10
 providerOptions:{

11
 anthropic:{ allowedCallers:["code_execution_20250825"]},

12
},

13
});

14

15

16
const result =awaitgenerateText({

17
 model:anthropic("claude-sonnet-4-5"),

18
 tools:{

19
 code_execution: anthropic.tools.codeExecution_20250825(),

20
 getWeather,

21
},

22
 prepareStep: forwardAnthropicContainerIdFromLastStep,

23
});

To learn more, check out the Anthropic documentation.

Link to headingOpenAI Provider Tools

Shell Tool: Execute shell commands with timeout and output limits

Apply Patch Tool: Create, update, and delete files using structured diffs

MCP Tool: Connect to remote Model Context Protocol servers

1
import{ openai }from"@ai-sdk/openai";

2

3
// Shell Tool - execute shell commands

4
const shell = openai.tools.shell({

5
execute:async({ action })=>{

6
// action.commands: string[] - commands to execute

7
// action.timeoutMs: optional timeout

8
// action.maxOutputLength: optional max chars to return

9
},

10
});

11

12
// Apply Patch Tool - file operations with diffs

13
const applyPatch = openai.tools.applyPatch({

14
execute:async({ callId, operation })=>{

15
// operation.type: 'create_file' | 'update_file' | 'delete_file'

16
// operation.path: file path

17
// operation.diff: diff content (for create/update)

18
},

19
});

20

21
// MCP Tool - connect to MCP servers

22
const mcp = openai.tools.mcp({

23
 serverLabel:"my-mcp-server",

24
 serverUrl:"[https://mcp.example.com](https://mcp.example.com/)",

25
 allowedTools:["tool1","tool2"],

26
});

To learn more, check out the OpenAI documentation.

Link to headingGoogle Provider Tools

Google Maps Tool: Enable location-aware responses with Maps grounding (Gemini 2.0+)

Vertex RAG Store Tool: Retrieve context from Vertex AI RAG Engine corpora (Gemini 2.0+)

File Search Tool: Semantic and keyword search in file search stores (Gemini 2.5+)

1
import{ google }from"@ai-sdk/google";

2

3
// Google Maps Tool - location-aware grounding

4
const googleMaps = google.tools.googleMaps();

5

6
// Vertex RAG Store Tool - retrieve from RAG corpora

7
const vertexRagStore = google.tools.vertexRagStore({

8
 ragCorpus:"projects/{project}/locations/{location}/ragCorpora/{rag_corpus}",

9
 topK:5,// optional: number of contexts to retrieve

10
});

11

12
// File Search Tool - search in file stores

13
const fileSearch = google.tools.fileSearch({

14
 fileSearchStoreNames:["fileSearchStores/my-store-123"],

15
 topK:10,// optional: number of chunks to retrieve

16
 metadataFilter:"author=John Doe",// optional: AIP-160 filter

17
});

To learn more, check out the Google documentation.

Link to headingxAI Provider Tools

Web Search: Search the web with domain filtering and image understanding

X Search: Search X (Twitter) posts with handle and date filtering

Code Execution: Run code in a sandboxed environment

View Image: Analyze and describe images

View X Video: Analyze X video content

1
import{ xai }from"@ai-sdk/xai";

2

3
// Web Search Tool - search the web

4
const webSearch = xai.tools.webSearch({

5
 allowedDomains:[

6
"[wikipedia.org](http://wikipedia.org/)",

7
"[github.com](http://github.com/)",

8
],// optional: max 5

9
 excludedDomains:["[example.com](http://example.com/)"],// optional: max 5

10
 enableImageUnderstanding:true,// optional

11
});

12

13
// X Search Tool - search X posts

14
const xSearch = xai.tools.xSearch({

15
 allowedXHandles:["elonmusk","xai"],// optional: max 10

16
 fromDate:"2025-01-01",// optional

17
 toDate:"2025-12-31",// optional

18
 enableImageUnderstanding:true,// optional

19
 enableVideoUnderstanding:true,// optional

20
});

21

22
// Code Execution Tool - run code

23
const codeExecution = xai.tools.codeExecution();

24

25
// View Image Tool - analyze images

26
const viewImage = xai.tools.viewImage();

27

28
// View X Video Tool - analyze X videos

29
const viewXVideo = xai.tools.viewXVideo();

To learn more, check out the xAI documentation.

Link to headingImage Editing

Image generation models are increasingly capable of more than just text-to-image generation. Many now support image-to-image operations like inpainting, outpainting, style transfer, and more.

AI SDK 6 extends 
generateImage
 to support image editing by accepting reference images alongside your text prompt:

1
import{ generateImage }from"ai";

2
import{ blackForestLabs }from"@ai-sdk/black-forest-labs";

3

4
const{ images }=awaitgenerateImage({

5
 model: blackForestLabs.image("flux-2-pro"),

6
 prompt:{

7
 text:"Edit this to make it two tanukis on a date",

8
 images:["https://www.example.com/tanuki.png"],

9
},

10
});

"Edit this to make it two tanukis on a date"

Reference images can be provided as URL strings, base64-encoded strings, Uint8Array, ArrayBuffer, or Buffer.

Note: 
experimental_generateImage
 has been promoted to stable and renamed to 
generateImage
.

Check out the Image Generation documentation to learn more.

Link to headingRaw Finish Reason & Extended Usage

AI SDK 6 improves visibility into model responses with raw finish reasons and restructured usage information.

Link to headingRaw Finish Reason

When providers add new finish reasons that the AI SDK doesn't recognize, they previously appeared as 
'other'
. Now, 
rawFinishReason
 exposes the exact string from the provider, letting you handle provider-specific cases before AI SDK updates.

1
const{ finishReason, rawFinishReason }=awaitgenerateText({

2
 model:'anthropic/claude-sonnet-4.5',

3
 prompt:'What is love?',

4
});

5

6
// finishReason: 'other' (mapped)

7
// rawFinishReason: 'end_turn' (provider-specific)

This is useful when providers have multiple finish reasons that map to a single AI SDK value, or when you need to distinguish between specific provider behaviors.

Link to headingExtended Usage Information

Usage reporting now includes detailed breakdowns for both input and output tokens:

1
const{ usage }=awaitgenerateText({

2
 model:'anthropic/claude-sonnet-4.5',

3
 prompt:'What is love?',

4
});

5

6
// Input token details

7
usage.inputTokenDetails.noCacheTokens;// Non-cached input tokens

8
usage.inputTokenDetails.cacheReadTokens;// Tokens read from cache

9
usage.inputTokenDetails.cacheWriteTokens;// Tokens written to cache

10

11
// Output token details

12
usage.outputTokenDetails.textTokens;// Text generation tokens

13
usage.outputTokenDetails.reasoningTokens;// Reasoning tokens (where supported)

14

15
// Raw provider usage

16
usage.raw;// Complete provider-specific usage object

These detailed breakdowns give you the visibility you need to optimize costs and debug token usage across providers.

Link to headingLangChain Adapter Rewrite

The 
@ai-sdk/langchain
 package has been rewritten to support modern LangChain and LangGraph features. New APIs include 
toBaseMessages()
 for converting UI messages to LangChain format, 
toUIMessageStream()
 for transforming LangGraph event streams, and 
LangSmithDeploymentTransport
 for browser-side connections to LangSmith deployments. The adapter now supports tool calling with partial input streaming, reasoning blocks, and Human-in-the-Loop workflows via LangGraph interrupts.

1
import{ toBaseMessages, toUIMessageStream }from'@ai-sdk/langchain';

2
import{ createUIMessageStreamResponse }from'ai';

3

4
const langchainMessages =awaittoBaseMessages(messages);

5
const stream =await graph.stream({ messages: langchainMessages });

6

7
returncreateUIMessageStreamResponse({

8
 stream:toUIMessageStream(stream),

9
});

This release is fully backwards compatible. To learn more, check out the LangChain Adapter documentation.

Link to headingMigrating to AI SDK 6

AI SDK 6 is a major version due to the introduction of the v3 Language Model Specification that powers new capabilities like agents and tool approval. However, unlike AI SDK 5, this release is not expected to have major breaking changes for most users.

The version bump reflects improvements to the specification, not a complete redesign of the SDK. If you're using AI SDK 5, migrating to v6 should be straightforward with minimal code changes.

1
npx @ai-sdk/codemod upgrade v6

For a detailed overview of all changes and manual steps that might be needed, refer to our AI SDK 6 migration guide. The guide includes step-by-step instructions and examples to ensure a smooth update.

Link to headingGetting started

“I’m super hyped for v6. The move from streamText to composable agents is tasteful, and so are the new APIs around type-safety, MCP, and agent preparation. The amount of care the team has put into API design is wild.I’m super hyped for v6. The move from streamText to composable agents is tasteful, and so are the new APIs around type-safety, MCP, and agent preparation. The amount of care the team has put into API design is wild.”

Josh, Upstash

With powerful new capabilities like the 
ToolLoopAgent
, human-in-the-loop tool approval, stable structured outputs with tool calling, and DevTools for debugging, there's never been a better time to start building AI applications with the AI SDK.

Start a new AI project: Get up and running with our latest guides for Next.js, React, Svelte, and more. Check out our latest guides.

Explore our templates: Visit our Template Gallery for production-ready starter projects.

Migrate to v6: Use our automated codemod for a smooth transition. Our comprehensive Migration Guide covers all breaking changes.

Try DevTools: Debug your AI applications with full visibility into LLM calls. Check out the DevTools documentation.

Join the community: Share what you're building, ask questions, and connect with other developers in our GitHub Discussions.

Link to headingContributors

AI SDK 6 is the result of the combined work of our core team at Vercel (Gregor, Lars, Aayush, Josh, Nico) and our amazing community of contributors:

viktorlarsson, shaper, AVtheking, SamyPesse, firemoonai, seldo, R-Taneja, ZiuChen, gaspar09, christian-bromann, jeremyphilemon, DaniAkash, a-tokyo, rohrz4nge, EwanTauran, codicecustode, shubham-021, kkawamu1, mclenhard, gdaybrice, dyh-sjtu, blurrah, EurFelux, AryanBagade, Omcodes23, jeffcarbs, codeyogi911, zirkelc, qkdreyer, tsuzaki430, qchuchu, karthikscale3, alex-deneuvillers, kesku, yorkeccak, guy-hartstein, Und3rf10w, siwachabhi, homanp, tengis617, SalvatoreAmoroso, ericciarla, baturyilmaz, chentsulin, kovereduard, yaonyan, mwln, IdoBouskila, wangyedev, rubnogueira, Emmaccen, priyanshusaini105, dpmishler, yilinjuang, JulioPeixoto, DeJeune, BangDori, shadowssdt, efantasia, kevinjosethomas, lukehrucker, Mohammedsinanpk, danielamitay, davidsonsns, teeverc, MQ37, jephal, TimPietrusky, theishangoswami, juliettech13, shelleypham, tconley1428, goyalshivansh2805, KirschX, neallseth, jltimm, rahulbhadja, tayyab3245, cwtuan, titouv, dylan-duan-aai, bel0v, josh-williams, amyegan, samjbobb, teunlao, dylanmoz, 0xlakshan, patelvivekdev, nvie, nlaz, drew-foxall, dannyroosevelt, Diluka, AlexKer, YosefLm, YutoKitano13, SarityS, jonaslalin, tobiasbueschel, dhofheinz, ethshea, ellis-driscoll, marcbouchenoire, shin-sakata, ellispinsky, DDU1222, ci, tomsseisums, kpman, juanuicich, A404coder, tamarshe-dev, crishoj, kevint-cerebras, arjunkmrm, Barbapapazes, nimeshnayaju, lewwolfe, sergical, tomerigal, huanshenyi, horita-yuya, rbadillap, syeddhasnainn, Dhravya, jagreehal, Mintnoii, mhodgson, amardeeplakshkar, aron, TooTallNate, Junyi-99, princejoogie, iiio2, MonkeyLeeT, joshualipman123, andrewdoro, fveiraswww, HugoRCD, rockingrohit9639

Your feedback, bug reports, and pull requests on GitHub have been instrumental in shaping this release. We're excited to see what you'll build with these new capabilities.

Ready to deploy? Start building with a free account. Speak to an expert for your Pro or Enterprise needs.

Start Deploying

Talk to an Expert

Explore Vercel Enterprise with an interactive product tour, trial, or a personalized demo.

Explore Enterprise

Get Started

Templates

Supported frameworks

Marketplace

Domains

Build

Next.js on Vercel

Turborepo

v0

Scale

Content delivery network

Fluid compute

CI/CD

Observability

AI GatewayNew

Vercel AgentNew

Secure

Platform security

Web Application Firewall

Bot management

BotID

SandboxNew

Resources

Pricing

Customers

Enterprise

Articles

Startups

Solution partners

Learn

Docs

Blog

Changelog

Knowledge Base

Academy

Community

Frameworks

Next.js

Nuxt

Svelte

Nitro

Turbo

SDKs

AI SDK

Workflow SDKNew

Flags SDK

Chat SDK

Streamdown AINew

Use Cases

Composable commerce

Multi-tenant platforms

Web apps

Marketing sites

Platform engineers

Design engineers

Company

About

Careers

Help

Press

Legal

Privacy Policy

Community

Open source program

Events

Shipped on Vercel

GitHub

LinkedIn

 X

YouTube

Loading status…

Select a display theme:systemlightdark

Products

v0

Build applications with AI

AI SDK

The AI Toolkit for TypeScript

AI Gateway

One endpoint, all your models

Vercel Agent

An agent that knows your stack

Sandbox

AI workflows in live environments

CI/CD

Helping teams ship 6× faster

Content Delivery

Fast, scalable, and reliable

Fluid Compute

Servers, in serverless form

Observability

Trace every step

Bot Management

Scalable bot protection

BotID

Invisible CAPTCHA

Platform Security

DDoS Protection, Firewall

Web Application Firewall

Granular, custom protection

Resources

Customers

Trusted by the best teams

Blog

The latest posts and changes

Changelog

See what shipped

Press

Read the latest news

Events

Join us at an event

Docs

Vercel documentation

Academy

Linear courses to level up

Knowledge Base

Find help quickly

Community

Join the conversation

Next.js

The native Next.js platform

Nuxt

The progressive web framework

Svelte

The web’s efficient UI framework

Turborepo

Speed with Enterprise scale

Solutions

AI Apps

Deploy at the speed of AI

Composable Commerce

Power storefronts that convert

Marketing Sites

Launch campaigns fast

Multi-tenant Platforms

Scale apps with one codebase

Web Apps

Ship features, not infrastructure

Marketplace

Extend and automate workflows

Templates

Jumpstart app development

Partner Finder

Get help from solution partners

Platform Engineers

Automate away repetition

Design Engineers

Deploy for every idea

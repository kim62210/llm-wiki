---
title: Quickstart | OpenAI Agents SDK
source_url: https://openai.github.io/openai-agents-js/guides/quickstart
final_url: https://openai.github.io/openai-agents-js/guides/quickstart/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:26:42.143512+00:00
---

# Quickstart | OpenAI Agents SDK

## 원본 URL

https://openai.github.io/openai-agents-js/guides/quickstart

## 주요 헤딩

- Quickstart
- Project Setup
- Create your first agent
- Run your first agent
- Give your agent tools
- Add a few more agents
- Define your handoffs
- Run the agent orchestration
- Putting it all together
- View your traces
- Next steps

## 추출 본문

Quickstart
Project Setup
Section titled “Project Setup”
Create a project and initialize npm. You’ll only need to do this once.
Terminal window mkdir my_project
cd my_project
npm init -y
Install the Agents SDK and Zod. The SDK uses Zod v4 for tool schemas and structured outputs.
Terminal window npm install @openai/agents zod
Set an OpenAI API key. If you don’t have one, follow these instructions to create an OpenAI API key.
Terminal window export OPENAI_API_KEY = sk- ...
Alternatively you can call setDefaultOpenAIKey('<api key>')
to set the key
programmatically and use setTracingExportApiKey('<api key>')
for tracing.
See the config guide for more details.
Create your first agent
Section titled “Create your first agent”
Agents are defined with instructions and a name.
Create an agent import { Agent } from '@openai/agents' ;
const agent = new Agent ({
name : 'History Tutor' ,
instructions :
'You provide assistance with historical queries. Explain important events and context clearly.' ,
});
Run your first agent
Section titled “Run your first agent”
You can use the run
method to run your agent. You trigger a run by passing both the agent you
want to start on and the input you want to pass in.
This will return a result that contains the final output and any actions that were performed
during that run.
Run an agent import { Agent , run } from '@openai/agents' ;
const agent = new Agent ({
name : 'History Tutor' ,
instructions :
'You provide assistance with historical queries. Explain important events and context clearly.' ,
});
const result = await run ( agent , 'When did sharks first appear?' );
console . log ( result . finalOutput );
For a second turn, you can either pass result.history
back into run()
, attach a
session , or reuse OpenAI server-managed state with
conversationId
/ previousResponseId
. The running agents
guide compares these approaches.
Give your agent tools
Section titled “Give your agent tools”
You can give an agent tools to use to look up information or perform actions.
Add a tool import { Agent , tool } from '@openai/agents' ;
import { z } from 'zod' ;
const historyFunFact = tool ({
// The name of the tool will be used by the agent to tell what tool to use.
name : 'history_fun_fact' ,
// The description is used to describe when to use the tool by telling it what it does.
description : 'Give a fun fact about a historical event' ,
// This tool takes no parameters, so we provide an empty Zod object.
parameters : z . object ({}),
execute : async () => {
// The output will be returned back to the agent to use.
return 'Sharks are older than trees.' ;
},
});
const agent = new Agent ({
name : 'History Tutor' ,
instructions :
'You provide assistance with historical queries. Explain important events and context clearly.' ,
// Add the tool to the agent.
tools : [ historyFunFact ],
});
{ // The output will be returned back to the agent to use. return 'Sharks are older than trees.'; },});const agent = new Agent({ name: 'History Tutor', instructions: 'You provide assistance with historical queries. Explain important events and context clearly.', // Add the tool to the agent. tools: [historyFunFact],});">
Add a few more agents
Section titled “Add a few more agents”
Additional agents can be defined similarly to break down problems into smaller parts and have your
agent be more focused on the task at hand. It also allows you to use different models for different
problems by defining the model on the agent.
Create specialist agents import { Agent } from '@openai/agents' ;
const historyTutorAgent = new Agent ({
name : 'History Tutor' ,
instructions :
'You provide assistance with historical queries. Explain important events and context clearly.' ,
});
const mathTutorAgent = new Agent ({
name : 'Math Tutor' ,
instructions :
'You provide help with math problems. Explain your reasoning at each step and include examples' ,
});
Define your handoffs
Section titled “Define your handoffs”
In order to orchestrate between multiple agents, you can define handoffs
for an agent. This will
enable the agent to pass the conversation on to the next agent. This will happen automatically
during the course of a run.
Define handoffs import { Agent } from '@openai/agents' ;
const historyTutorAgent = new Agent ({
name : 'History Tutor' ,
instructions :
'You provide assistance with historical queries. Explain important events and context clearly.' ,
});
const mathTutorAgent = new Agent ({
name : 'Math Tutor' ,
instructions :
'You provide help with math problems. Explain your reasoning at each step and include examples' ,
});
// Use Agent.create() to keep handoff output types aligned.
const triageAgent = Agent . create ({
name : 'Triage Agent' ,
instructions :
"You determine which agent to use based on the user's homework question" ,
handoffs : [ historyTutorAgent , mathTutorAgent ],
});
After your run you can see which agent generated the final response by looking at the lastAgent
property on the result.
Run the agent orchestration
Section titled “Run the agent orchestration”
The runner handles executing individual agents, any handoffs, and any tool calls.
Run agent orchestration import { Agent , run } from '@openai/agents' ;
const historyTutorAgent = new Agent ({
name : 'History Tutor' ,
instructions :
'You provide assistance with historical queries. Explain important events and context clearly.' ,
});
const mathTutorAgent = new Agent ({
name : 'Math Tutor' ,
instructions :
'You provide help with math problems. Explain your reasoning at each step and include examples' ,
});
const triageAgent = Agent . create ({
name : 'Triage Agent' ,
instructions :
"You determine which agent to use based on the user's homework question" ,
handoffs : [ historyTutorAgent , mathTutorAgent ],
});
async function main () {
const result = await run ( triageAgent , 'What is the capital of France?' );
console . log ( result . finalOutput );
}
main (). catch (( err ) => console . error ( err ));

---
title: Workflows overview | Mastra Docs
source_url: https://mastra.ai/docs/workflows/overview
final_url: https://mastra.ai/docs/workflows/overview
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T06:17:48.742638+00:00
---

# Workflows overview | Mastra Docs

## 원본 URL

https://mastra.ai/docs/workflows/overview

## 주요 헤딩

- Workflows overview
- When to use workflows Direct link to When to use workflows
- Core principles Direct link to Core principles
- Creating a workflow step Direct link to Creating a workflow step
- Creating a workflow Direct link to Creating a workflow
- Studio Direct link to Studio
- Workflow state Direct link to Workflow state
- Workflows as steps Direct link to Workflows as steps
- Registering a workflow Direct link to Registering a workflow
- Referencing a workflow Direct link to Referencing a workflow
- Running workflows Direct link to Running workflows
- Restarting active workflow runs Direct link to Restarting active workflow runs
- Using RequestContext Direct link to using-requestcontext
- Related Direct link to Related

## 추출 본문

Workflows Overview
On this page
Workflows overview
Workflows let you define complex sequences of tasks using clear, structured steps rather than relying on the reasoning of a single agent. They give you full control over how tasks are broken down, how data moves between them, and what gets executed when. Workflows run using the built-in execution engine by default, or can be deployed to workflow runners like Inngest for managed infrastructure.
When to use workflows Direct link to When to use workflows
Use workflows for tasks that are clearly defined upfront and involve multiple steps with a specific execution order. They give you fine-grained control over how data flows and transforms between steps, and which primitives are called at each stage.
tip
Watch an introduction to workflows, and how they compare to agents on YouTube (7 minutes) .
Core principles Direct link to Core principles
Mastra workflows operate using these principles:
Defining steps with createStep
, specifying input/output schemas and business logic.
Composing steps with createWorkflow
to define the execution flow.
Running workflows to execute the entire sequence, with built-in support for suspension, resumption, and streaming results.
Creating a workflow step Direct link to Creating a workflow step
Steps are the building blocks of workflows. Create a step using createStep()
with inputSchema
and outputSchema
to define the data it accepts and returns.
The execute
function defines what the step does. Use it to call functions in your codebase, external APIs, agents, or tools.
src/mastra/workflows/test-workflow.ts
import { createStep } from '@mastra/core/workflows'
const step1 = createStep ( {
id : 'step-1' ,
inputSchema : z . object ( {
message : z . string ( ) ,
} ) ,
outputSchema : z . object ( {
formatted : z . string ( ) ,
} ) ,
execute : async ( { inputData } ) => {
const { message } = inputData
return {
formatted : message . toUpperCase ( ) ,
}
} ,
} )
info
Visit Step
for a full list of configuration options.
Using agents and tools Direct link to Using agents and tools
Workflow steps can also call registered agents or import and execute tools directly, visit the Using Tools page for more information.
Creating a workflow Direct link to Creating a workflow
Create a workflow using createWorkflow()
with inputSchema
and outputSchema
to define the data it accepts and returns. Add steps using .then()
and complete the workflow with .commit()
.
src/mastra/workflows/test-workflow.ts
import { createWorkflow , createStep } from "@mastra/core/workflows" ;
import { z } from "zod" ;
const step1 = createStep ( { ... } ) ;
export const testWorkflow = createWorkflow ( {
id : "test-workflow" ,
inputSchema : z . object ( {
message : z . string ( )
} ) ,
outputSchema : z . object ( {
output : z . string ( )
} )
} )
. then ( step1 )
. commit ( ) ;
info
Visit Workflow Class for a full list of configuration options.
Understanding control flow Direct link to Understanding control flow
Workflows can be composed using a number of different methods. The method you choose determines how each step's schema should be structured. Visit the Control Flow page for more information.
Studio Direct link to Studio
Open Studio and select a workflow from the Workflows tab.
Graph view : The center panel visualizes the workflow's steps and execution flow.
Input form : The right sidebar generates a form from the workflow's inputSchema
. Fill it in and start the run.
Live status : During execution, the graph updates each step's status in real time. The sidebar shows the workflow's input, output, state, and logs.
Time travel : After a run completes, replay individual steps to inspect or retry them.
Workflow state Direct link to Workflow state
Workflow state lets you share values across steps without passing them through every step's inputSchema and outputSchema. Use state for tracking progress, accumulating results, or sharing configuration across the entire workflow.
src/mastra/workflows/test-workflow.ts
const step1 = createStep ( {
id : 'step-1' ,
inputSchema : z . object ( { message : z . string ( ) } ) ,
outputSchema : z . object ( { formatted : z . string ( ) } ) ,
stateSchema : z . object ( { counter : z . number ( ) } ) ,
execute : async ( { inputData , state , setState } ) => {
// Read from state
console . log ( state . counter )
// Update state for subsequent steps
setState ( { ... state , counter : state . counter + 1 } )
return { formatted : inputData . message . toUpperCase ( ) }
} ,
} )
info
Visit Workflow State for complete documentation on state schemas, initial state, persistence across suspend/resume, and nested workflows.
Workflows as steps Direct link to Workflows as steps
Use a workflow as a step to reuse its logic within a larger composition. Input and output follow the same schema rules described in Core principles .
src/mastra/workflows/test-workflow.ts
const step1 = createStep ( { ... } ) ;
const step2 = createStep ( { ... } ) ;
const childWorkflow = createWorkflow ( {
id : "child-workflow" ,
inputSchema : z . object ( {
message : z . string ( )
} ) ,
outputSchema : z . object ( {
emphasized : z . string ( )
} )
} )
. then ( step1 )
. then ( step2 )
. commit ( ) ;
export const testWorkflow = createWorkflow ( {
id : "test-workflow" ,
inputSchema : z . object ( {
message : z . string ( )
} ) ,
outputSchema : z . object ( {
emphasized : z . string ( )
} )
} )
. then ( childWorkflow )
. commit ( ) ;
Cloning a workflow Direct link to Cloning a workflow
Clone a workflow using cloneWorkflow()
when you want to reuse its logic but track it separately under a new ID. Each clone runs independently and shows up as a distinct workflow in logs and observability tools.
src/mastra/workflows/test-workflow.ts
import { cloneWorkflow } from "@mastra/core/workflows" ;
const step1 = createStep ( { ... } ) ;
const parentWorkflow = createWorkflow ( { ... } )
const clonedWorkflow = cloneWorkflow ( parentWorkflow , { id : "cloned-workflow" } ) ;
export const testWorkflow = createWorkflow ( { ... } )
. then ( step1 )
. then ( clonedWorkflow )
. commit ( ) ;
Registering a workflow Direct link to Registering a workflow
Register your workflow in the Mastra instance to make it available throughout your application. Once registered, it can be called from agents or tools and has access to shared resources such as logging and observability features:
src/mastra/index.ts
import { Mastra } from '@mastra/core/mastra'
import { testWorkflow } from './workflows/test-workflow'
export const mastra = new Mastra ( {
workflows : { testWorkflow } ,
} )
Referencing a workflow Direct link to Referencing a workflow
You can run workflows from agents, tools, the Mastra Client, or the command line. Get a reference by calling .getWorkflow()
on your mastra
or mastraClient
instance, depending on your setup:
const testWorkflow = mastra . getWorkflow ( 'testWorkflow' )
info
mastra.getWorkflow()
is preferred over a direct import for two reasons:
It provides access to the Mastra instance configuration (logger, telemetry, storage, registered agents, and vector stores)
It provides full TypeScript type inference for workflow input and output schemas
Note: Use getWorkflow()
with the workflow's registration key (the key used when adding it to Mastra). While getWorkflowById()
is available for retrieving workflows by their id
property, it doesn't provide the same level of type inference.
Running workflows Direct link to Running workflows
Workflows can be run in two modes: start waits for all steps to complete before returning, and stream emits events during execution. Choose the approach that fits your use case: start when you only need the final result, and stream when you want to monitor progress or trigger actions as steps complete.
.start() .stream() Create a workflow run instance using createRun()
, then call .start()
with inputData
matching the workflow's inputSchema
. The workflow executes all steps and returns the final result. const run = await testWorkflow . createRun ( )
const result = await run . start ( {
inputData : {
message : 'Hello world' ,
} ,
} )
if ( result . status === 'success' ) {
console . log ( result . result )
}
Create a workflow run instance using .createRun()
, then call .stream()
with inputData
matching the workflow's inputSchema
. Iterate over fullStream
to track progress, then await result
to get the final workflow result. const run = await testWorkflow . createRun ( )

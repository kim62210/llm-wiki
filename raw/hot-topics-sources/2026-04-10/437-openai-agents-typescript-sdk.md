---
title: OpenAI Agents SDK TypeScript | OpenAI Agents SDK
source_url: https://openai.github.io/openai-agents-js
final_url: https://openai.github.io/openai-agents-js/
status: 200
content_type: text/html; charset=utf-8
topics: [OpenAI Agents SDK]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:28.235250+00:00
---

# OpenAI Agents SDK TypeScript | OpenAI Agents SDK

## 원본 URL

https://openai.github.io/openai-agents-js

## 추출 본문

OpenAI Agents SDK TypeScript | OpenAI Agents SDKSkip to content

SearchCtrlK
 Cancel 

Python SDK
Select themeDarkLightAutoSelect languageEnglish日本語中文한국어

Overview

Quickstart

Configuration

Guides
Agents

Models

Tools

Guardrails

Running Agents

Streaming

Agent Orchestration

Handoffs

Results

Human-in-the-loop

Sessions

Context Management

Model Context Protocol (MCP)

Tracing

Voice Agents
Overview

Quickstart

Building Voice Agents

Transport Mechanisms

Extensions
AI SDK Integration

Realtime Agents on Twilio

Realtime Agents on Cloudflare

Troubleshooting

API Reference
@openai/agents
Main API
Classes
Agent

AgentHooks

AgentsError

BatchTraceProcessor

ConsoleSpanExporter

GuardrailExecutionError

Handoff

InputGuardrailTripwireTriggered

MaxTurnsExceededError

MCPServers

MCPServerSSE

MCPServerStdio

MCPServerStreamableHttp

MemorySession

ModelBehaviorError

NoopSpan

NoopTrace

OpenAIChatCompletionsModel

OpenAIConversationsSession

OpenAIProvider

OpenAIResponsesCompactionSession

OpenAIResponsesModel

OpenAIResponsesWSModel

OpenAITracingExporter

OutputGuardrailTripwireTriggered

RequestUsage

RunAgentUpdatedStreamEvent

RunContext

RunHandoffCallItem

RunHandoffOutputItem

RunItemStreamEvent

RunMessageOutputItem

Runner

RunRawModelStreamEvent

RunReasoningItem

RunResult

RunState

RunToolApprovalItem

RunToolCallItem

RunToolCallOutputItem

RunToolSearchCallItem

RunToolSearchOutputItem

Span

StreamedRunResult

SystemError

ToolCallError

ToolInputGuardrailTripwireTriggered

ToolOutputGuardrailTripwireTriggered

ToolTimeoutError

Trace

TraceProvider

Usage

UserError

Interfaces
AgentConfiguration

Editor

GuardrailFunctionOutput

InputGuardrail

InputGuardrailFunctionArgs

InputGuardrailMetadata

InputGuardrailResult

MCPBlobResourceContent

MCPListResourcesParams

MCPListResourcesResult

MCPListResourceTemplatesResult

MCPReadResourceResult

MCPResource

MCPResourceTemplate

MCPServer

MCPServerWithResources

MCPTextResourceContent

MCPToolFilterContext

MCPToolFilterStatic

MCPToolMetaContext

Model

ModelProvider

OpenAIResponsesCompactionAwareSession

OutputGuardrail

OutputGuardrailDefinition

OutputGuardrailFunctionArgs

OutputGuardrailMetadata

OutputGuardrailResult

Session

Shell

ToolGuardrailFunctionOutput

ToolGuardrailMetadata

ToolInputGuardrailData

ToolInputGuardrailDefinition

ToolInputGuardrailResult

ToolOutputGuardrailData

ToolOutputGuardrailDefinition

ToolOutputGuardrailResult

TracingExporter

TracingProcessor

Type Aliases
AgentConfigWithHandoffs

AgentInputItem

AgentOptions

AgentOutputItem

AgentOutputType

AgentSpanData

AgentToolInvocation

ApplyPatchCallItem

ApplyPatchCallItem

ApplyPatchCallResultItem

ApplyPatchCallResultItem

ApplyPatchOperation

ApplyPatchOperation

ApplyPatchResult

ApplyPatchTool

AssistantMessageItem

AssistantMessageItem

CallModelInputFilter

CallModelInputFilterArgs

ClientToolSearchExecutor

ClientToolSearchExecutorArgs

ClientToolSearchExecutorResult

CompletedAgentToolInvocationRunResult

Computer

ComputerCallResultItem

ComputerCallResultItem

ComputerOnSafetyCheckFunction

ComputerSafetyCheck

ComputerSafetyCheckResult

ComputerTool

ComputerUseCallItem

ComputerUseCallItem

CustomSpanData

EditorInvocationContext

FunctionCallItem

FunctionCallItem

FunctionCallResultItem

FunctionCallResultItem

FunctionSpanData

FunctionTool

FunctionToolResult

FunctionToolTimeoutBehavior

GenerationSpanData

GenerationUsageData

GetAllMcpToolsOptions

GuardrailSpanData

HandoffEnabledFunction

HandoffInputData

HandoffSpanData

HostedMCPTool

HostedTool

HostedToolCallItem

HostedToolCallItem

IndividualRunOptions

InputGuardrailFunction

JsonSchemaDefinition

MCPListToolsSpanData

MCPResourceContent

MCPServersOptions

MCPServersReconnectOptions

MCPToolCacheKeyGenerator

MCPToolFilterCallable

MCPToolMetaResolver

ModelInputData

ModelRequest

ModelResponse

ModelRetryAdvice

ModelRetryAdviceRequest

ModelRetryBackoffSettings

ModelRetryNormalizedError

ModelRetrySettings

ModelSettings

ModelSettingsToolChoice

NonStreamRunOptions

OpenAIChatCompletionsRawModelStreamEvent

OpenAIConversationsSessionOptions

OpenAIRawModelEventSource

OpenAIResponsesCompactionArgs

OpenAIResponsesCompactionDecisionContext

OpenAIResponsesCompactionMode

OpenAIResponsesCompactionResult

OpenAIResponsesCompactionSessionOptions

OpenAIResponsesRawModelStreamEvent

OpenAITracingExporterOptions

OutputGuardrailFunction

ReasoningItem

ReasoningItem

ReasoningItemIdPolicy

ResponseSpanData

ResponseStreamEvent

ResponsesWebSocketSession

ResponsesWebSocketSessionOptions

RetryDecision

RetryPolicy

RetryPolicyContext

RunConfig

RunErrorData

RunErrorHandler

RunErrorHandlerInput

RunErrorHandlerResult

RunErrorHandlers

RunErrorKind

RunItem

RunStreamEvent

SerializedHandoff

SerializedOutputType

SerializedTool

SessionInputCallback

ShellAction

ShellCallItem

ShellCallItem

ShellCallResultItem

ShellCallResultItem

ShellOutputResult

ShellResult

ShellTool

ShellToolContainerAutoEnvironment

ShellToolContainerNetworkPolicy

ShellToolContainerNetworkPolicyAllowlist

ShellToolContainerNetworkPolicyDisabled

ShellToolContainerNetworkPolicyDomainSecret

ShellToolContainerReferenceEnvironment

ShellToolContainerSkill

ShellToolEnvironment

ShellToolHostedEnvironment

ShellToolInlineSkill

ShellToolInlineSkillSource

ShellToolLocalEnvironment

ShellToolLocalSkill

ShellToolSkillReference

SpanData

SpanError

SpanOptions

SpeechGroupSpanData

SpeechSpanData

StreamEvent

StreamEvent

StreamEventGenericItem

StreamEventGenericItem

StreamEventResponseCompleted

StreamEventResponseCompleted

StreamEventResponseStarted

StreamEventResponseStarted

StreamEventTextStream

StreamEventTextStream

StreamRunOptions

SystemMessageItem

TextOutput

Tool

ToolCallOutputContent

ToolCallOutputContent

ToolCallStructuredOutput

ToolCallStructuredOutput

ToolEnabledFunction

ToolErrorFormatter

ToolErrorFormatterArgs

ToolExecuteArgument

ToolGuardrailBehavior

ToolInputGuardrailFunction

ToolInputParameters

ToolNamespaceOptions

ToolOptions

ToolOptionsWithGuardrails

ToolOutputFileContent

ToolOutputFileContent

ToolOutputGuardrailFunction

ToolOutputImage

ToolOutputImage

ToolOutputText

ToolOutputText

ToolReference

ToolReference

ToolSearchCallArguments

ToolSearchCallArguments

ToolSearchCallItem

ToolSearchCallItem

ToolSearchOutputItem

ToolSearchOutputItem

ToolSearchOutputTool

ToolSearchOutputTool

ToolSearchTool

ToolsToFinalOutputResult

ToolTimeoutErrorFunction

ToolToFinalOutputFunction

ToolUseBehavior

ToolUseBehaviorFlags

TracingConfig

TranscriptionSpanData

UnknownContext

UnknownItem

UnknownItem

UserMessageItem

UserMessageItem

Variables
OPENAI_CHAT_COMPLETIONS_RAW_MODEL_EVENT_SOURCE

OPENAI_DEFAULT_MODEL_ENV_VARIABLE_NAME

OPENAI_RESPONSES_RAW_MODEL_EVENT_SOURCE

retryPolicies

RuntimeEventEmitter

ToolGuardrailFunctionOutputFactory

withAgentSpan

withCustomSpan

withFunctionSpan

withGenerationSpan

withGuardrailSpan

withHandoffSpan

withMCPListToolsSpan

withResponseSpan

withSpeechGroupSpan

withSpeechSpan

withTranscriptionSpan

Functions
addTraceProcessor

applyDiff

applyPatchTool

assistant

attachClientToolSearchExecutor

codeInterpreterTool

computerTool

connectMcpServers

createAgentSpan

createCustomSpan

createFunctionSpan

createGenerationSpan

createGuardrailSpan

createHandoffSpan

createMCPListToolsSpan

createMCPToolStaticFilter

createResponseSpan

createSpeechGroupSpan

createSpeechSpan

createTranscriptionSpan

defineOutputGuardrail

defineToolInputGuardrail

defineToolOutputGuardrail

extractAllTextOutput

fileSearchTool

generateGroupId

generateSpanId

generateTraceId

getAllMcpTools

getClientToolSearchExecutor

getCurrentSpan

getCurrentTrace

getDefaultModel

getDefaultModelSettings

getGlobalTraceProvider

getHandoff

getLogger

getOrCreateTrace

getToolSearchRuntimeToolKey

getTransferMessage

gpt5ReasoningSettingsRequired

handoff

hostedMcpTool

imageGenerationTool

invalidateServerToolsCache

invokeFunctionTool

isGpt5Default

isOpenAIChatCompletionsRawModelStreamEvent

isOpenAIResponsesCompactionAwareSession

isOpenAIResponsesRawModelStreamEvent

mcpToFunctionTool

resetCurrentSpan

resolveToolInputGuardrails

resolveToolOutputGuardrails

run

runToolInputGuardrails

runToolOutputGuardrails

setCurrentSpan

setDefaultModelProvider

setDefaultOpenAIClient

setDefaultOpenAIKey

setDefaultOpenAITracingExporter

setOpenAIAPI

setOpenAIResponsesTransport

setTraceProcessors

setTracingDisabled

setTracingExportApiKey

shellTool

startOpenAIConversationsSession

startTraceExportLoop

system

tool

toolNamespace

toolSearchTool

user

webSearchTool

withResponsesWebSocketSession

withTrace

@openai/agents/realtime
Classes
ModelBehaviorError

OpenAIRealtimeBase

OpenAIRealtimeSIP

OpenAIRealtimeWebRTC

OpenAIRealtimeWebSocket

OutputGuardrailTripwireTriggered

RealtimeAgent

RealtimeSession

UserError

Interfaces
RealtimeOutputGuardrail

RealtimeTransportLayer

Type Aliases
ApiKey

FunctionTool

OpenAIRealtimeBaseOptions

OpenAIRealtimeEventTypes

OpenAIRealtimeModels

OpenAIRealtimeWebRTCOptions

OpenAIRealtimeWebSocketOptions

RealtimeAgentConfiguration

RealtimeAudioFormat

RealtimeBaseItem

RealtimeClientMessage

RealtimeContextData

RealtimeItem

RealtimeMcpCallItem

RealtimeMessageItem

RealtimeSessionConfig

RealtimeSessionConnectOptions

RealtimeSessionEventTypes

RealtimeSessionOptions

RealtimeSessionPayload

RealtimeToolCallItem

RealtimeTransportEventTypes

RealtimeTransportLayerConnectOptions

TransportError

TransportEvent

TransportLayerAudio

TransportLayerResponseCompleted

TransportLayerResponseStarted

TransportLayerTranscriptDelta

TransportToolCallEvent

WebRTCState

WebSocketState

Variables
DEFAULT_OPENAI_REALTIME_MODEL

DEFAULT_OPENAI_REALTIME_SESSION_CONFIG

utils

Functions
backgroundResult

isBackgroundResult

tool

@openai/agents-core
API
Classes
Agent

AgentHooks

AgentsError

BatchTraceProcessor

ConsoleSpanExporter

GuardrailExecutionError

Handoff

InputGuardrailTripwireTriggered

MaxTurnsExceededError

MCPServers

MCPServerSSE

MCPServerStdio

MCPServerStreamableHttp

MemorySession

ModelBehaviorError

NoopSpan

NoopTrace

OutputGuardrailTripwireTriggered

RequestUsage

RunAgentUpdatedStreamEvent

RunContext

RunHandoffCallItem

RunHandoffOutputItem

RunItemStreamEvent

RunMessageOutputItem

Runner

RunRawModelStreamEvent

RunReasoningItem

RunResult

RunState

RuntimeEventEmitter

RunToolApprovalItem

RunToolCallItem

RunToolCallOutputItem

RunToolSearchCallItem

RunToolSearchOutputItem

Span

StreamedRunResult

SystemError

ToolCallError

ToolInputGuardrailTripwireTriggered

ToolOutputGuardrailTripwireTriggered

ToolTimeoutError

Trace

TraceProvider

Usage

UserError

Interfaces
AgentConfiguration

Editor

GuardrailFunctionOutput

InputGuardrail

InputGuardrailFunctionArgs

InputGuardrailMetadata

InputGuardrailResult

MCPBlobResourceContent

MCPListResourcesParams

MCPListResourcesResult

MCPListResourceTemplatesResult

MCPReadResourceResult

MCPResource

MCPResourceTemplate

MCPServer

MCPServerWithResources

MCPTextResourceContent

MCPToolFilterContext

MCPToolFilterStatic

MCPToolMetaContext

Model

ModelProvider

OpenAIResponsesCompactionAwareSession

OutputGuardrail

OutputGuardrailDefinition

OutputGuardrailFunctionArgs

OutputGuardrailMetadata

OutputGuardrailResult

Session

Shell

ToolGuardrailFunctionOutput

ToolGuardrailMetadata

ToolInputGuardrailData

ToolInputGuardrailDefinition

ToolInputGuardrailResult

ToolOutputGuardrailData

ToolOutputGuardrailDefinition

ToolOutputGuardrailResult

TracingExporter

TracingProcessor

Type Aliases
AgentConfigWithHandoffs

AgentInputItem

AgentOptions

AgentOutputItem

AgentOutputType

AgentSpanData

AgentToolInvocation

ApplyPatchCallItem

ApplyPatchCallItem

ApplyPatchCallResultItem

ApplyPatchCallResultItem

ApplyPatchOperation

ApplyPatchResult

ApplyPatchTool

AssistantMessageItem

AssistantMessageItem

CallModelInputFilter

CallModelInputFilterArgs

ClientToolSearchExecutor

ClientToolSearchExecutorArgs

ClientToolSearchExecutorResult

CompletedAgentToolInvocationRunResult

Computer

ComputerCallResultItem

ComputerCallResultItem

ComputerOnSafetyCheckFunction

ComputerSafetyCheck

ComputerSafetyCheckResult

ComputerTool

ComputerUseCallItem

ComputerUseCallItem

CustomSpanData

EditorInvocationContext

FunctionCallItem

FunctionCallItem

FunctionCallResultItem

FunctionCallResultItem

FunctionSpanData

FunctionTool

FunctionToolResult

FunctionToolTimeoutBehavior

GenerationSpanData

GenerationUsageData

GetAllMcpToolsOptions

GuardrailSpanData

HandoffEnabledFunction

HandoffInputData

HandoffSpanData

HostedMCPTool

HostedTool

HostedToolCallItem

HostedToolCallItem

IndividualRunOptions

InputGuardrailFunction

JsonSchemaDefinition

MCPListToolsSpanData

MCPResourceContent

MCPServersOptions

MCPServersReconnectOptions

MCPToolCacheKeyGenerator

MCPToolFilterCallable

MCPToolMetaResolver

ModelInputData

ModelRequest

ModelResponse

ModelRetryAdvice

ModelRetryAdviceRequest

ModelRetryBackoffSettings

ModelRetryNormalizedError

ModelRetrySettings

ModelSettings

ModelSettingsToolChoice

NonStreamRunOptions

OpenAIResponsesCompactionArgs

OpenAIResponsesCompactionResult

OutputGuardrailFunction

ReasoningItem

ReasoningItem

ReasoningItemIdPolicy

ResponseSpanData

ResponseStreamEvent

RetryDecision

RetryPolicy

RetryPolicyContext

RunConfig

RunErrorData

RunErrorHandler

RunErrorHandlerInput

RunErrorHandlerResult

RunErrorHandlers

RunErrorKind

RunItem

RunStreamEvent

SerializedHandoff

SerializedOutputType

SerializedTool

SessionInputCallback

ShellAction

ShellCallItem

ShellCallItem

ShellCallResultItem

ShellCallResultItem

ShellOutputResult

ShellResult

ShellTool

ShellToolContainerAutoEnvironment

ShellToolContainerNetworkPolicy

ShellToolContainerNetworkPolicyAllowlist

ShellToolContainerNetworkPolicyDisabled

ShellToolContainerNetworkPolicyDomainSecret

ShellToolContainerReferenceEnvironment

ShellToolContainerSkill

ShellToolEnvironment

ShellToolHostedEnvironment

ShellToolInlineSkill

ShellToolInlineSkillSource

ShellToolLocalEnvironment

ShellToolLocalSkill

ShellToolSkillReference

SpanData

SpanError

SpanOptions

SpeechGroupSpanData

SpeechSpanData

StreamEvent

StreamEvent

StreamEventGenericItem

StreamEventGenericItem

StreamEventResponseCompleted

StreamEventResponseCompleted

StreamEventResponseStarted

StreamEventResponseStarted

StreamEventTextStream

StreamEventTextStream

StreamRunOptions

SystemMessageItem

TextOutput

Tool

ToolCallOutputContent

ToolCallOutputContent

ToolCallStructuredOutput

ToolCallStructuredOutput

ToolEnabledFunction

ToolErrorFormatter

ToolErrorFormatterArgs

ToolExecuteArgument

ToolGuardrailBehavior

ToolInputGuardrailFunction

ToolInputParameters

ToolNamespaceOptions

ToolOptions

ToolOptionsWithGuardrails

ToolOutputFileContent

ToolOutputFileContent

ToolOutputGuardrailFunction

ToolOutputImage

ToolOutputImage

ToolOutputText

ToolOutputText

ToolReference

ToolReference

ToolSearchCallArguments

ToolSearchCallArguments

ToolSearchCallItem

ToolSearchCallItem

ToolSearchOutputItem

ToolSearchOutputItem

ToolSearchOutputTool

ToolSearchOutputTool

ToolsToFinalOutputResult

ToolTimeoutErrorFunction

ToolToFinalOutputFunction

ToolUseBehavior

ToolUseBehaviorFlags

TracingConfig

TranscriptionSpanData

UnknownContext

UnknownItem

UnknownItem

UserMessageItem

UserMessageItem

Variables
ApplyPatchOperation

OPENAI_DEFAULT_MODEL_ENV_VARIABLE_NAME

retryPolicies

ToolGuardrailFunctionOutputFactory

withAgentSpan

withCustomSpan

withFunctionSpan

withGenerationSpan

withGuardrailSpan

withHandoffSpan

withMCPListToolsSpan

withResponseSpan

withSpeechGroupSpan

withSpeechSpan

withTranscriptionSpan

Functions
addTraceProcessor

applyDiff

applyPatchTool

assistant

attachClientToolSearchExecutor

computerTool

connectMcpServers

createAgentSpan

createCustomSpan

createFunctionSpan

createGenerationSpan

createGuardrailSpan

createHandoffSpan

createMCPListToolsSpan

createMCPToolStaticFilter

createResponseSpan

createSpeechGroupSpan

createSpeechSpan

createTranscriptionSpan

defineOutputGuardrail

defineToolInputGuardrail

defineToolOutputGuardrail

extractAllTextOutput

generateGroupId

generateSpanId

generateTraceId

getAllMcpTools

getClientToolSearchExecutor

getCurrentSpan

getCurrentTrace

getDefaultModel

getDefaultModelSettings

getGlobalTraceProvider

getHandoff

getLogger

getOrCreateTrace

getToolSearchRuntimeToolKey

getTransferMessage

gpt5ReasoningSettingsRequired

handoff

hostedMcpTool

invalidateServerToolsCache

invokeFunctionTool

isGpt5Default

isOpenAIResponsesCompactionAwareSession

mcpToFunctionTool

resetCurrentSpan

resolveToolInputGuardrails

resolveToolOutputGuardrails

run

runToolInputGuardrails

runToolOutputGuardrails

setCurrentSpan

setDefaultModelProvider

setTraceProcessors

setTracingDisabled

shellTool

startTraceExportLoop

system

tool

toolNamespace

user

withTrace

@openai/agents-openai
API
Classes
OpenAIChatCompletionsModel

OpenAIConversationsSession

OpenAIProvider

OpenAIResponsesCompactionSession

OpenAIResponsesModel

OpenAIResponsesWSModel

OpenAITracingExporter

Type Aliases
OpenAIChatCompletionsRawModelStreamEvent

OpenAIConversationsSessionOptions

OpenAIRawModelEventSource

OpenAIResponsesCompactionDecisionContext

OpenAIResponsesCompactionMode

OpenAIResponsesCompactionSessionOptions

OpenAIResponsesRawModelStreamEvent

OpenAITracingExporterOptions

ResponsesWebSocketSession

ResponsesWebSocketSessionOptions

ToolSearchTool

Variables
OPENAI_CHAT_COMPLETIONS_RAW_MODEL_EVENT_SOURCE

OPENAI_RESPONSES_RAW_MODEL_EVENT_SOURCE

Functions
codeInterpreterTool

fileSearchTool

imageGenerationTool

isOpenAIChatCompletionsRawModelStreamEvent

isOpenAIResponsesRawModelStreamEvent

setDefaultOpenAIClient

setDefaultOpenAIKey

setDefaultOpenAITracingExporter

setOpenAIAPI

setOpenAIResponsesTransport

setTracingExportApiKey

startOpenAIConversationsSession

toolSearchTool

webSearchTool

withResponsesWebSocketSession

@openai/agents-realtime
API
Classes
ModelBehaviorError

OpenAIRealtimeBase

OpenAIRealtimeSIP

OpenAIRealtimeWebRTC

OpenAIRealtimeWebSocket

OutputGuardrailTripwireTriggered

RealtimeAgent

RealtimeSession

UserError

Interfaces
RealtimeOutputGuardrail

RealtimeTransportLayer

Type Aliases
ApiKey

FunctionTool

OpenAIRealtimeBaseOptions

OpenAIRealtimeEventTypes

OpenAIRealtimeModels

OpenAIRealtimeWebRTCOptions

OpenAIRealtimeWebSocketOptions

RealtimeAgentConfiguration

RealtimeAudioFormat

RealtimeBaseItem

RealtimeClientMessage

RealtimeContextData

RealtimeItem

RealtimeMcpCallItem

RealtimeMessageItem

RealtimeSessionConfig

RealtimeSessionConnectOptions

RealtimeSessionEventTypes

RealtimeSessionOptions

RealtimeSessionPayload

RealtimeToolCallItem

RealtimeTransportEventTypes

RealtimeTransportLayerConnectOptions

TransportError

TransportEvent

TransportLayerAudio

TransportLayerResponseCompleted

TransportLayerResponseStarted

TransportLayerTranscriptDelta

TransportToolCallEvent

WebRTCState

WebSocketState

Variables
DEFAULT_OPENAI_REALTIME_MODEL

DEFAULT_OPENAI_REALTIME_SESSION_CONFIG

utils

Functions
backgroundResult

isBackgroundResult

tool

@openai/agents-extensions
API
Classes
CloudflareRealtimeTransportLayer

TwilioRealtimeTransportLayer

Type Aliases
TwilioRealtimeTransportLayerOptions

Maintainers: release process

Python SDKView on GitHubView on npm
Select themeDarkLightAutoSelect languageEnglish日本語中文한국어

View on GitHubView on npm

On this page

Overview

Overview

Why use the Agents SDK

Installation

Choose your starting point

Hello world example

Start here

Choose your path

On this page

Overview

Overview

Why use the Agents SDK

Installation

Choose your starting point

Hello world example

Start here

Choose your path

OpenAI Agents SDK TypeScript

OpenAI Agents SDK

Build text and voice agents with a small set of primitives.

 Let’s build 

 Text Agent 

 Voice Agent 

import { Agent, run } from'@openai/agents';

constagent=newAgent({

name:'Assistant',

instructions:'You are a helpful assistant.',

});

constresult=awaitrun(

agent,

'Write a haiku about recursion in programming.',

);

console.log(result.finalOutput);

import { RealtimeAgent, RealtimeSession } from'@openai/agents/realtime';

constagent=newRealtimeAgent({

name:'Assistant',

instructions:'You are a helpful assistant.',

});

// Automatically connects your microphone and audio output in the browser via WebRTC.

constsession=newRealtimeSession(agent);

awaitsession.connect({

apiKey:'<client-api-key>',

});

Overview
Section titled “Overview”

The OpenAI Agents SDK for TypeScript enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It’s a production-ready upgrade of our previous experimentation for agents, Swarm, that’s also available in Python. The Agents SDK has a very small set of primitives:

Agents, which are LLMs equipped with instructions and tools

Agents as tools / Handoffs, which allow agents to delegate to other agents for specific tasks

Guardrails, which enable the inputs to agents to be validated

In combination with TypeScript, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real-world applications without a steep learning curve. In addition, the SDK comes with built-in tracing that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.

Why use the Agents SDK
Section titled “Why use the Agents SDK”

The SDK has two driving design principles:

Enough features to be worth using, but few enough primitives to make it quick to learn.

Works great out of the box, but you can customize exactly what happens.

Here are the main features of the SDK:

Agent loop: A built-in agent loop that handles tool invocation, sends results back to the LLM, and continues until the task is complete.

TypeScript-first: Orchestrate and chain agents using native TypeScript language features, without needing to learn new abstractions.

Agents as tools / Handoffs: A powerful mechanism for coordinating and delegating work across multiple agents.

Guardrails: Run input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass.

Function tools: Turn any TypeScript function into a tool with automatic schema generation and Zod-powered validation.

MCP server tool calling: Built-in MCP server tool integration that works the same way as function tools.

Sessions: A persistent memory layer for maintaining working context within an agent loop.

Human in the loop: Built-in mechanisms for involving humans across agent runs.

Tracing: Built-in tracing for visualizing, debugging, and monitoring workflows, with support for the OpenAI suite of evaluation, fine-tuning, and distillation tools.

Realtime Agents: Build powerful voice agents with features such as automatic interruption detection, context management, guardrails, and more.

Installation
Section titled “Installation”

Terminal window

npminstall@openai/agentszod

The SDK requires Zod v4; installing 
zod
 via npm will fetch the latest v4 release.

Choose your starting point
Section titled “Choose your starting point”

Most first-time users only need one of these entry points:
Start withUse it whenNotes
@openai/agents
You are building most text or voice applications.Recommended default. It includes the OpenAI provider setup and exposes voice APIs under 
@openai/agents/realtime
.
@openai/agents-realtime
You only need the standalone Realtime package.Useful for browser-only voice apps or when you want a narrower package boundary.Lower-level packages (
@openai/agents-core
, 
@openai/agents-openai
, 
@openai/agents-extensions
)You need lower-level composition, custom provider wiring, or specific integrations.Most new users can ignore these until they have a concrete need.

Hello world example
Section titled “Hello world example”

Hello World

import { Agent, run } from'@openai/agents';

constagent=newAgent({

name:'Assistant',

instructions:'You are a helpful assistant',

});

constresult=awaitrun(

agent,

'Write a haiku about recursion in programming.',

);

console.log(result.finalOutput);

// Code within the code,

// Functions calling themselves,

// Infinite loop's dance.

(If running this, ensure you set the 
OPENAI_API_KEY
 environment variable)

Terminal window

exportOPENAI_API_KEY=sk-...

Start here
Section titled “Start here”

Pick one path first, get it working end to end, then come back for the deeper guides.

QuickstartBuild your first text-based agent and learn the core SDK workflow.

Voice Agents QuickstartStart with the Realtime voice path when you are building spoken interactions.

Choose your path
Section titled “Choose your path”

Use this table when you know the job you want to do, but not which page explains it.
GoalStart hereBuild the first text agent and see one complete runQuickstartAdd function tools, hosted tools, or agents as toolsToolsDecide between handoffs and manager-style orchestrationAgent orchestrationKeep memory across turnsRunning agents and SessionsUse OpenAI models, websocket transport, or non-OpenAI providersModelsReview outputs, run items, interruptions, and resume stateResultsBuild a low-latency voice agentVoice Agents Quickstart

Edit page

 Next 
Quickstart

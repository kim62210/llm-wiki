---
title: Agents | Pydantic Docs
source_url: https://pydantic.dev/docs/ai/core-concepts/agent/
final_url: https://pydantic.dev/docs/ai/core-concepts/agent/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:35:17.041205+00:00
---

# Agents | Pydantic Docs

## 원본 URL

https://pydantic.dev/docs/ai/core-concepts/agent/

## 주요 헤딩

- Agents
- Introduction
- Running Agents
- Runs vs. Conversations
- Type safe by design
- System Prompts
- Instructions
- Reflection and self-correction
- Debugging and Monitoring
- Model errors
- Agent Specs

## 추출 본문

Agents
Introduction
Agents are Pydantic AI’s primary interface for interacting with LLMs.
In some use cases a single Agent will control an entire application or component,
but multiple agents can also interact to embody more complex workflows.
The Agent
class has full API documentation, but conceptually you can think of an agent as a container for:
Component Description Instructions A set of instructions for the LLM written by the developer. Function tool(s) and toolsets Functions that the LLM may call to get information while generating a response. Structured output type The structured datatype the LLM must return at the end of a run, if specified. Dependency type constraint Dynamic instructions functions, tools, and output functions may all use dependencies when they’re run. LLM model Optional default LLM model associated with the agent. Can also be specified when running the agent. Model Settings Optional default model settings to help fine tune requests. Can also be specified when running the agent. Capabilities Reusable bundles of tools, hooks, instructions, and model settings that extend agent behavior.
While each of these can be configured individually, capabilities let you bundle related behavior into reusable units that are easier to compose, share, and load from configuration files .
In typing terms, agents are generic in their dependency and output types, e.g., an agent which required dependencies of type Foobar
and produced outputs of type list[str]
would have type Agent[Foobar, list[str]]
. In practice, you shouldn’t need to care about this, it should just mean your IDE can tell you when you have the right type, and if you choose to use static type checking it should work well with Pydantic AI.
Here’s a toy example of an agent that simulates a roulette wheel:
roulette_wheel.py from pydantic_ai import Agent, RunContext
roulette_agent = Agent( # (1)
'openai:gpt-5.2',
deps_type=int,
output_type=bool,
system_prompt=(
'Use the `roulette_wheel` function to see if the '
'customer has won based on the number they provide.'
),
)
@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str: # (2)
"""check if the square is a winner"""
return 'winner' if square == ctx.deps else 'loser'
# Run the agent
success_number = 18 # (3)
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.output) # (4)
#> True
result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.output)
#> False
Create an agent, which expects an integer dependency and produces a boolean output. This agent will have type Agent[int, bool]
.
Define a tool that checks if the square is a winner. Here RunContext
is parameterized with the dependency type int
; if you got the dependency type wrong you'd get a typing error.
In reality, you might want to use a random number here e.g. random.randint(0, 36)
.
result.output
will be a boolean indicating if the square is a winner. Pydantic performs the output validation, and it'll be typed as a bool
since its type is derived from the output_type
generic parameter of the agent.
Agents are designed for reuse, like FastAPI Apps
You can instantiate one agent and use it globally throughout your application, as you would a small FastAPI app or an APIRouter , or dynamically create as many agents as you want. Both are valid and supported ways to use agents.
Running Agents
There are five ways to run an agent:
agent.run()
— an async function which returns a RunResult
containing a completed response.
agent.run_sync()
— a plain, synchronous function which returns a RunResult
containing a completed response (internally, this just calls loop.run_until_complete(self.run())
).
agent.run_stream()
— an async context manager which returns a StreamedRunResult
, which contains methods to stream text and structured output as an async iterable. agent.run_stream_sync()
is a synchronous variation that returns a StreamedRunResultSync
with synchronous versions of the same methods.
agent.run_stream_events()
— a function which returns an async iterable of AgentStreamEvent
s and a AgentRunResultEvent
containing the final run result.
agent.iter()
— a context manager which returns an AgentRun
, an async iterable over the nodes of the agent’s underlying Graph
.
Here’s a simple example demonstrating the first four:
run_agent.py from pydantic_ai import Agent, AgentRunResultEvent, AgentStreamEvent
agent = Agent('openai:gpt-5.2')
result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)
#> The capital of Italy is Rome.
async def main():
result = await agent.run('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
async with agent.run_stream('What is the capital of the UK?') as response:
async for text in response.stream_text():
print(text)
#> The capital of
#> The capital of the UK is
#> The capital of the UK is London.
events: list[AgentStreamEvent | AgentRunResultEvent] = []
async for event in agent.run_stream_events('What is the capital of Mexico?'):
events.append(event)
print(events)
"""
[
PartStartEvent(index=0, part=TextPart(content='The capital of ')),
FinalResultEvent(tool_name=None, tool_call_id=None),
PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='Mexico is Mexico ')),
PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='City.')),
PartEndEvent(
index=0, part=TextPart(content='The capital of Mexico is Mexico City.')
),
AgentRunResultEvent(
result=AgentRunResult(output='The capital of Mexico is Mexico City.')
),
]
"""
(This example is complete, it can be run “as is” — you’ll need to add asyncio.run(main())
to run main
)
You can also pass messages from previous runs to continue a conversation or provide context, as described in Messages and Chat History .
Streaming Events and Final Output
As shown in the example above, run_stream()
makes it easy to stream the agent’s final output as it comes in.
It also takes an optional event_stream_handler
argument that you can use to gain insight into what is happening during the run before the final output is produced.
The example below shows how to stream events and text output. You can also stream structured output .
Note
The run_stream()
and run_stream_sync()
methods will consider the first output that matches the output type (which could be text, an output tool call, or a deferred tool call) to be the final output of the agent run, even when the model generates (additional) tool calls after this “final” output.
These “dangling” tool calls will not be executed unless the agent’s end_strategy
is set to 'exhaustive'
, and even then their results will not be sent back to the model as the agent run will already be considered completed. In short, if the model returns both tool calls and text, and the agent’s output type is str
, the tool calls will not run in streaming mode with the default setting.
If you want to always keep running the agent when it performs tool calls, and stream all events from the model’s streaming response and the agent’s execution of tools,
use agent.run_stream_events()
or agent.iter()
instead, as described in the following sections.
run_stream_event_stream_handler.py import asyncio
from collections.abc import AsyncIterable
from datetime import date
from pydantic_ai import (
Agent,
AgentStreamEvent,
FinalResultEvent,
FunctionToolCallEvent,
FunctionToolResultEvent,
PartDeltaEvent,
PartStartEvent,
RunContext,
TextPartDelta,
ThinkingPartDelta,
ToolCallPartDelta,
)
weather_agent = Agent(
'openai:gpt-5.2',
system_prompt='Providing a weather forecast at the locations the user provides.',
)
@weather_agent.tool
async def weather_forecast(
ctx: RunContext,
location: str,
forecast_date: date,
) -> str:
return f'The forecast in {location} on {forecast_date} is 24°C and sunny.'
output_messages: list[str] = []
async def handle_event(event: AgentStreamEvent):
if isinstance(event, PartStartEvent):
output_messages.append(f'[Request] Starting part {event.index}: {event.part!r}')
elif isinstance(event, PartDeltaEvent):
if isinstance(event.delta, TextPartDelta):

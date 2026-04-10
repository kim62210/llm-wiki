---
title: GitHub - langchain-ai/agentevals: Readymade evaluators for agent trajectories · GitHub
source_url: https://github.com/langchain-ai/agentevals
final_url: https://github.com/langchain-ai/agentevals
status: 200
content_type: text/html; charset=utf-8
topics: [Agent Trajectory Evaluation]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:57.471978+00:00
---

# GitHub - langchain-ai/agentevals: Readymade evaluators for agent trajectories · GitHub

## 원본 URL

https://github.com/langchain-ai/agentevals

## 추출 본문

GitHub - langchain-ai/agentevals: Readymade evaluators for agent trajectories · GitHub

Skip to content

Navigation Menu
Toggle navigation

 Sign in
 
Appearance settings

Platform

AI CODE CREATION

GitHub CopilotWrite better code with AI

GitHub SparkBuild and deploy intelligent apps

GitHub ModelsManage and compare prompts

MCP RegistryNewIntegrate external tools

DEVELOPER WORKFLOWS

ActionsAutomate any workflow

CodespacesInstant dev environments

IssuesPlan and track work

Code ReviewManage code changes

APPLICATION SECURITY

GitHub Advanced SecurityFind and fix vulnerabilities

Code securitySecure your code as you build

Secret protectionStop leaks before they start

EXPLORE
Why GitHub

Documentation

Blog

Changelog

Marketplace

View all features

Solutions

BY COMPANY SIZE
Enterprises

Small and medium teams

Startups

Nonprofits

BY USE CASE
App Modernization

DevSecOps

DevOps

CI/CD

View all use cases

BY INDUSTRY
Healthcare

Financial services

Manufacturing

Government

View all industries

View all solutions

Resources

EXPLORE BY TOPIC
AI

Software Development

DevOps

Security

View all topics

EXPLORE BY TYPE
Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES
Documentation

Customer support

Community forum

Trust center

Partners

View all resources

Open Source

COMMUNITY

GitHub SponsorsFund open source developers

PROGRAMS
Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES
Topics

Trending

Collections

Enterprise

ENTERPRISE SOLUTIONS

Enterprise platformAI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced SecurityEnterprise-grade security features

Copilot for BusinessEnterprise-grade AI features

Premium SupportEnterprise-grade 24/7 support

Pricing

Search or jump to...

Search code, repositories, users, issues, pull requests...

 Search
 

Clear

Search syntax tips

 Provide feedback
 

We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted

 Cancel
 Submit feedback

 Saved searches
 

Use saved searches to filter your results more quickly

Name

Query

 To see all available qualifiers, see our documentation.
 

 Cancel
 Create saved search

 Sign in
 

 Sign up
 
Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

 langchain-ai
/agentevalsPublic

Notifications
You must be signed in to change notification settings

Fork
 40

 Star
545

Code

Issues12

Pull requests8

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

langchain-ai/agentevals

main

BranchesTags

Go to file

Code
Open more actions menu

Folders and files
NameName
Last commit message

Last commit date

Latest commit

History
204 Commits

204 Commits

.github/workflows

.github/workflows

js

js

python

python

scripts

scripts

static/img

static/img

.gitignore

.gitignore

LICENSE

LICENSE

README.md

README.md

uv.lock

uv.lock

View all files

Repository files navigation

README

Code of conduct

Contributing

MIT license

Security

🦾⚖️ AgentEvals

Agentic applications give an LLM freedom over control flow in order to solve problems. While this freedom
can be extremely powerful, the black box nature of LLMs can make it difficult to understand how changes in one part of your agent will affect others downstream.
This makes evaluating your agents especially important.

This package contains a collection of evaluators and utilities for evaluating the performance of your agents, with a focus on agent trajectory, or the intermediate steps an agent takes as it runs.
It is intended to provide a good conceptual starting point for your agent's evals.

If you are looking for more general evaluation tools, please check out the companion package 
openevals
.

Quickstart

To get started, install 
agentevals
:
Python

pip install agentevals

TypeScript

npm install agentevals @langchain/core

This quickstart will use an evaluator powered by OpenAI's 
o3-mini
 model to judge your results, so you'll need to set your OpenAI API key as an environment variable:

export OPENAI_API_KEY="your_openai_api_key"

Once you've done this, you can run your first trajectory evaluator. We represent the agent's trajectory as a list of OpenAI-style messages:
Python

fromagentevals.trajectory.llmimportcreate_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPTtrajectory_evaluator=create_trajectory_llm_as_judge(
 prompt=TRAJECTORY_ACCURACY_PROMPT,
 model="openai:o3-mini",
)

# This is a fake trajectory, in reality you would run your agent to get a real trajectoryoutputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "SF"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]

eval_result=trajectory_evaluator(
 outputs=outputs,
)

print(eval_result)

{
 'key': 'trajectory_accuracy',
 'reasoning': 'The trajectory accurately follows the user's request for weather information in SF. Initially, the assistant recognizes the goal (providing weather details), then it efficiently makes a tool call to get the weather, and finally it communicates the result clearly. All steps demonstrate logical progression and efficiency. Thus, the score should be: true.',
 'score': true
}

TypeScript

import{createTrajectoryLLMAsJudge,typeFlexibleChatCompletionMessage,TRAJECTORY_ACCURACY_PROMPT,}from"agentevals";consttrajectoryEvaluator=createTrajectoryLLMAsJudge({prompt: TRAJECTORY_ACCURACY_PROMPT,model: "openai:o3-mini",});constoutputs=[{role: "user",content: "What is the weather in SF?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "SF"}),},},],},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "The weather in SF is 80 degrees and sunny.",},]satisfiesFlexibleChatCompletionMessage[];constevalResult=awaittrajectoryEvaluator({
 outputs,});console.log(evalResult);

{
 key: 'trajectory_accuracy',
 score: true,
 comment: '...'
}

You can see that the evaluator returns a score of 
true
 since the overall trajectory is a reasonable path for the agent to take to answer the user's question.

For more details on this evaluator, including how to customize it, see the section on trajectory LLM-as-judge.

Table of Contents

Installation

Evaluators
Agent Trajectory Match
Strict match

Unordered match

Subset/superset match

Tool args match modes

Trajectory LLM-as-judge

Graph Trajectory
Graph trajectory LLM-as-judge

Graph trajectory strict match

Python Async Support

LangSmith Integration
Pytest or Vitest/Jest

Evaluate

Installation

You can install 
agentevals
 like this:
Python

pip install agentevals

TypeScript

npm install agentevals @langchain/core

For LLM-as-judge evaluators, you will also need an LLM client. By default, 
agentevals
 will use LangChain chat model integrations and comes with 
langchain_openai
 installed by default. However, if you prefer, you may use the OpenAI client directly:
Python

pip install openai

TypeScript

npm install openai

It is also helpful to be familiar with some evaluation concepts and
LangSmith's pytest integration for running evals, which is documented here.

Evaluators

Agent trajectory match

Agent trajectory match evaluators are used to judge the trajectory of an agent's execution either against an expected trajectory or using an LLM.
These evaluators expect you to format your agent's trajectory as a list of OpenAI format dicts or as a list of LangChain 
BaseMessage
 classes, and handle message formatting
under the hood.

AgentEvals offers the 
create_trajectory_match_evaluator
/
createTrajectoryMatchEvaluator
 and 
create_async_trajectory_match_evaluator
 methods for this task. You can customize their behavior in a few ways:

Setting 
trajectory_match_mode
/
trajectoryMatchMode
 to 
strict
, 
unordered
, 
subset
, or 
superset
 to provide the general strategy the evaluator will use to compare trajectories

Setting 
tool_args_match_mode
 and/or 
tool_args_match_overrides
 to customize how the evaluator considers equality between tool calls in the actual trajectory vs. the reference. By default, only tool calls with the same arguments to the same tool are considered equal.

Strict match

The 
"strict"

trajectory_match_mode
 compares two trajectories and ensures that they contain the same messages
in the same order with the same tool calls. Note that it does allow for differences in message content:
Python

importjsonfromagentevals.trajectory.matchimportcreate_trajectory_match_evaluatoroutputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 },
 {
 "function": {
 "name": "accuweather_forecast",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]
reference_outputs= [
 {"role": "user", "content": "What is the weather in San Francisco?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco."},
 {"role": "assistant", "content": "The weather in SF is 80˚ and sunny."},
]

evaluator=create_trajectory_match_evaluator(
 trajectory_match_mode="strict"
)

result=evaluator(
 outputs=outputs, reference_outputs=reference_outputs
)

print(result)

{
 'key': 'trajectory_strict_match',
 'score': False,
 'comment': None,
}

TypeScript

import{createTrajectoryMatchEvaluator,typeFlexibleChatCompletionMessage,}from"agentevals";constoutputs=[{role: "user",content: "What is the weather in SF?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "San Francisco"})},},{function: {name: "accuweather_forecast",arguments: JSON.stringify({"city": "San Francisco"}),},}]},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "The weather in SF is 80 degrees and sunny."},]satisfiesFlexibleChatCompletionMessage[];constreferenceOutputs=[{role: "user",content: "What is the weather in San Francisco?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "San Francisco"})}}]},{role: "tool",content: "It's 80 degrees and sunny in San Francisco."},]satisfiesFlexibleChatCompletionMessage[];constevaluator=createTrajectoryMatchEvaluator({trajectoryMatchMode: "strict",})constresult=awaitevaluator({
 outputs,
 referenceOutputs,});console.log(result);

{
 'key': 'trajectory_strict_match',
 'score': false,
}

"strict"
 is useful is if you want to ensure that tools are always called in the same order for a given query (e.g. a company policy lookup tool before a tool that requests vacation time for an employee).

Note: If you would like to configure the way this evaluator checks for tool call equality, see this section.

Unordered match

The 
"unordered"

trajectory_match_mode
 compares two trajectories and ensures that they contain the same tool calls in any order. This is useful if you want to allow flexibility in how an agent obtains the proper information, but still do care that all information was retrieved.
Python

importjsonfromagentevals.trajectory.matchimportcreate_trajectory_match_evaluatorinputs= {}
outputs= [
 {"role": "user", "content": "What is the weather in SF and is there anything fun happening?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [{
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 }],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [{
 "function": {
 "name": "get_fun_activities",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 }],
 },
 {"role": "tool", "content": "Nothing fun is happening, you should stay indoors and read!"},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny, but there is nothing fun happening."},
]
reference_outputs= [
 {"role": "user", "content": "What is the weather in SF and is there anything fun happening?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_fun_activities",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 },
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 },
 ],
 },
 {"role": "tool", "content": "Nothing fun is happening, you should stay indoors and read!"},
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {"role": "assistant", "content": "In SF, it's 80˚ and sunny, but there is nothing fun happening."},
]

evaluator=create_trajectory_match_evaluator(
 trajectory_match_mode="unordered"
)

result=evaluator(
 outputs=outputs, reference_outputs=reference_outputs
)

print(result)

{
 'key': 'trajectory_unordered_match',
 'score': True,
 'comment': None,
}

TypeScript

import{createTrajectoryMatchEvaluator,typeFlexibleChatCompletionMessage,}from"agentevals";constoutputs=[{role: "user",content: "What is the weather in SF and is there anything fun happening?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "SF"}),}}],},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "",tool_calls: [{function: {name: "get_fun_activities",arguments: JSON.stringify({city: "SF"}),}}],},{role: "tool",content: "Nothing fun is happening, you should stay indoors and read!"},{role: "assistant",content: "The weather in SF is 80 degrees and sunny, but there is nothing fun happening."},]satisifesFlexibleChatCompletionMessage[];constreferenceOutputs=[{role: "user",content: "What is the weather in SF and is there anything fun happening?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_fun_activities",arguments: JSON.stringify({city: "San Francisco"}),}},{function: {name: "get_weather",arguments: JSON.stringify({city: "San Francisco"}),}},],},{role: "tool",content: "Nothing fun is happening, you should stay indoors and read!"},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "In SF, it's 80˚ and sunny, but there is nothing fun happening."},]satisfiesFlexibleChatCompletionMessage[];constevaluator=createTrajectoryMatchEvaluator({trajectoryMatchMode: "unordered",});constresult=awaitevaluator({
 outputs,
 referenceOutputs,});console.log(result)

{
 'key': 'trajectory_unordered_match',
 'score': true,
}

"unordered"
 is useful is if you want to ensure that specific tools are called at some point in the trajectory, but you don't necessarily need them to be in message order (e.g. the agent called a company policy retrieval tool at an arbitrary point in an interaction before authorizing spend for a pizza party).

Note: If you would like to configure the way this evaluator checks for tool call equality, see this section.

Subset and superset match

The 
"subset"
 and 
"superset"
 modes match partial trajectories (ensuring that a trajectory contains a subset/superset of tool calls contained in a reference trajectory).
Python

importjsonfromagentevals.trajectory.matchimportcreate_trajectory_match_evaluatoroutputs= [
 {"role": "user", "content": "What is the weather in SF and London?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [{
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "SF and London"}),
 },
 }, {
 "function": {
 "name": "accuweather_forecast",
 "arguments": json.dumps({"city": "SF and London"}),
 }
 }],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF, and 90 degrees and rainy in London."},
 {"role": "tool", "content": "Unknown."},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny. In London, it's 90 degrees and rainy."},
]
reference_outputs= [
 {"role": "user", "content": "What is the weather in SF and London?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "SF and London"}),
 }
 },
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco, and 90 degrees and rainy in London."},
 {"role": "assistant", "content": "The weather in SF is 80˚ and sunny. In London, it's 90˚ and rainy."},
]

evaluator=create_trajectory_match_evaluator(
 trajectory_match_mode="superset", # or "subset"
)

result=evaluator(
 outputs=outputs, reference_outputs=reference_outputs
)

print(result)

{
 'key': 'trajectory_superset_match',
 'score': True,
 'comment': None,
}

TypeScript

import{createTrajectoryMatchEvaluator,typeFlexibleChatCompletionMessage}from"agentevals";constoutputs=[{role: "user",content: "What is the weather in SF and London?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "SF and London"}),}},{"function": {name: "accuweather_forecast",arguments: JSON.stringify({"city": "SF and London"}),}}],},{role: "tool",content: "It's 80 degrees and sunny in SF, and 90 degrees and rainy in London."},{role: "tool",content: "Unknown."},{role: "assistant",content: "The weather in SF is 80 degrees and sunny. In London, it's 90 degrees and rainy."},]satisfiesFlexibleChatCompletionMessage[];constreferenceOutputs=[{role: "user",content: "What is the weather in SF and London?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "SF and London"}),}},],},{role: "tool",content: "It's 80 degrees and sunny in San Francisco, and 90 degrees and rainy in London."},{role: "assistant",content: "The weather in SF is 80˚ and sunny. In London, it's 90˚ and rainy."},]satisfiesFlexibleChatCompletionMessage[];constevaluator=createTrajectoryMatchEvaluator({trajectoryMatchMode: "superset",// or "subset"});constresult=awaitevaluator({
 outputs,
 referenceOutputs,});console.log(result)

{
 'key': 'trajectory_superset_match',
 'score': true,
}

"superset"
 is useful if you want to ensure that some key tools were called at some point in the trajectory, but an agent calling extra tools is still acceptable. 
"subset"
 is the inverse and is useful if you want to ensure that the agent did not call any tools beyond the expected ones.

Note: If you would like to configure the way this evaluator checks for tool call equality, see this section.

Tool args match modes

When checking equality between tool calls, the above evaluators will require that all tool call arguments are the exact same by default. You can configure this behavior in the following ways:

Treating any two tool calls for the same tool as equivalent by setting 
tool_args_match_mode="ignore"
 (Python) or 
toolArgsMatchMode: "ignore"
 (TypeScript)

Treating a tool call as equivalent if it contain as subset/superset of args compared to a reference tool call of the same name with 
tool_args_match_mode="subset"/"superset"
 (Python) or 
toolArgsMatchMode: "subset"/"superset
 (TypeScript)

Setting custom matchers for all calls of a given tool using the 
tool_args_match_overrides
 (Python) or 
toolArgsMatchOverrides
 (TypeScript) param

You can set both of these parameters at the same time. 
tool_args_match_overrides
 will take precendence over 
tool_args_match_mode
.

tool_args_match_overrides
/
toolArgsMatchOverrides
 takes a dictionary whose keys are tool names and whose values are either 
"exact"
, 
"ignore"
, a list of fields within the tool call that must match exactly, or a comparator function that takes two arguments and returns whether they are equal:

ToolArgsMatchMode=Literal["exact", "ignore", "subset", "superset"]

ToolArgsMatchOverrides=dict[str, Union[ToolArgsMatchMode, list[str], Callable[[dict, dict], bool]]]

Here's an example that allows case insensitivity for the arguments to a tool named 
get_weather
:
Python

importjsonfromagentevals.trajectory.matchimportcreate_trajectory_match_evaluatoroutputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "san francisco"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]
reference_outputs= [
 {"role": "user", "content": "What is the weather in San Francisco?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco."},
 {"role": "assistant", "content": "The weather in SF is 80˚ and sunny."},
]

evaluator=create_trajectory_match_evaluator(
 trajectory_match_mode="strict",
 tool_args_match_mode="exact", # Default valuetool_args_match_overrides={
 "get_weather": lambdax, y: x["city"].lower() ==y["city"].lower()
 }
)

result=evaluator(
 outputs=outputs, reference_outputs=reference_outputs
)

print(result)

{
 'key': 'trajectory_strict_match',
 'score': True,
 'comment': None,
}

TypeScript

import{createTrajectoryMatchEvaluator,typeFlexibleChatCompletionMessage,}from"agentevals";constoutputs=[{role: "user",content: "What is the weather in SF?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "san francisco"})},}]},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "The weather in SF is 80 degrees and sunny."},]satisfiesFlexibleChatCompletionMessage[];constreferenceOutputs=[{role: "user",content: "What is the weather in San Francisco?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "San Francisco"})}}]},{role: "tool",content: "It's 80 degrees and sunny in San Francisco."},]satisfiesFlexibleChatCompletionMessage[];constevaluator=createTrajectoryMatchEvaluator({trajectoryMatchMode: "strict",toolArgsMatchMode: "exact",// Default valuetoolArgsMatchOverrides: {get_weather: (x,y)=>{returntypeofx.city==="string"&&typeofy.city==="string"&&x.city.toLowerCase()===y.city.toLowerCase();},}});constresult=awaitevaluator({
 outputs,
 referenceOutputs,});console.log(result);

{
 'key': 'trajectory_strict_match',
 'score': true,
}

This flexibility allows you to handle cases where you want looser equality for LLM generated arguments (
"san francisco"
 to equal 
"San Francisco"
) for only specific tool calls.

Trajectory LLM-as-judge

The LLM-as-judge trajectory evaluator that uses an LLM to evaluate the trajectory. Unlike the trajectory match evaluators, it doesn't require a reference trajectory. Here's an example:
Python

importjsonfromagentevals.trajectory.llmimportcreate_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPTevaluator=create_trajectory_llm_as_judge(
 prompt=TRAJECTORY_ACCURACY_PROMPT,
 model="openai:o3-mini"
)
outputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "SF"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]
eval_result=evaluator(
 outputs=outputs,
)

print(eval_result)

{
 'key': 'trajectory_accuracy',
 'score': True,
 'comment': 'The provided agent trajectory is reasonable...'
}

TypeScript

import{createTrajectoryLLMAsJudge,TRAJECTORY_ACCURACY_PROMPT,typeFlexibleChatCompletionMessage,}from"agentevals";constevaluator=createTrajectoryLLMAsJudge({prompt: TRAJECTORY_ACCURACY_PROMPT,model: "openai:o3-mini",});constoutputs=[{role: "user",content: "What is the weather in SF?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "SF"}),}}],},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "The weather in SF is 80 degrees and sunny."},]satisfiesFlexibleChatCompletionMessage[];constresult=awaitevaluator({ outputs });console.log(result)

{
 'key': 'trajectory_accuracy',
 'score': True,
 'comment': 'The provided agent trajectory is reasonable...'
}

If you have a reference trajectory, you can add an extra variable to your prompt and pass in the reference trajectory. Below, we use the prebuilt 
TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE
 prompt, which contains a 
reference_outputs
 variable:
Python

importjsonfromagentevals.trajectory.llmimportcreate_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCEevaluator=create_trajectory_llm_as_judge(
 prompt=TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
 model="openai:o3-mini"
)
outputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "SF"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]
reference_outputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco."},
 {"role": "assistant", "content": "The weather in SF is 80˚ and sunny."},
]
eval_result=evaluator(
 outputs=outputs,
 reference_outputs=reference_outputs,
)

print(eval_result)

{
 'key': 'trajectory_accuracy',
 'score': True,
 'comment': 'The provided agent trajectory is consistent with the reference. Both trajectories start with the same user query and then correctly invoke a weather lookup through a tool call. Although the reference uses "San Francisco" while the provided trajectory uses "SF" and there is a minor formatting difference (degrees vs. ˚), these differences do not affect the correctness or essential steps of the process. Thus, the score should be: true.'
}

TypeScript

import{createTrajectoryLLMAsJudge,TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,typeFlexibleChatCompletionMessage,}from"agentevals";constevaluator=createTrajectoryLLMAsJudge({prompt: TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,model: "openai:o3-mini",});constoutputs=[{role: "user",content: "What is the weather in SF?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "SF"}),}}],},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "The weather in SF is 80 degrees and sunny."},]satisfiesFlexibleChatCompletionMessage[];constreferenceOutputs=[{role: "user",content: "What is the weather in SF?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: JSON.stringify({city: "San Francisco"}),}}],},{role: "tool",content: "It's 80 degrees and sunny in San Francisco."},{role: "assistant",content: "The weather in SF is 80˚ and sunny."},]satisfiesFlexibleChatCompletionMessage[];constresult=awaitevaluator({
 outputs,
 referenceOutputs,});console.log(result)

{
 'key': 'trajectory_accuracy',
 'score': true,
 'comment': 'The provided agent trajectory is consistent with the reference. Both trajectories start with the same user query and then correctly invoke a weather lookup through a tool call. Although the reference uses "San Francisco" while the provided trajectory uses "SF" and there is a minor formatting difference (degrees vs. ˚), these differences do not affect the correctness or essential steps of the process. Thus, the score should be: true.'
}

create_trajectory_llm_as_judge
 takes the same parameters as 
create_llm_as_judge
 in 
openevals
, so you can customize the prompt and scoring output as needed.

In addition to 
prompt
 and 
model
, the following parameters are also available:

continuous
: a boolean that sets whether the evaluator should return a float score somewhere between 0 and 1 instead of a binary score. Defaults to 
False
.

choices
: a list of floats that sets the possible scores for the evaluator.

system
: a string that sets a system prompt for the judge model by adding a system message before other parts of the prompt.

few_shot_examples
: a list of example dicts that are appended to the end of the prompt. This is useful for providing the judge model with examples of good and bad outputs. The required structure looks like this:
Python

few_shot_examples= [
 {
 "inputs": "What color is the sky?",
 "outputs": "The sky is red.",
 "reasoning": "The sky is red because it is early evening.",
 "score": 1,
 }
]

TypeScript

constfewShotExamples=[{inputs: "What color is the sky?",outputs: "The sky is red.",reasoning: "The sky is red because it is early evening.",score: 1,}];

See the 
openevals
 repo for a fully up to date list of parameters.

Graph trajectory

For frameworks like LangGraph that model agents as graphs, it can be more convenient to represent trajectories in terms of nodes visited rather than messages. 
agentevals
 includes a category of evaluators called graph trajectory evaluators that are designed to work with this format, as well as convenient utilities for extracting trajectories from a LangGraph thread, including different conversation turns and interrupts.

The below examples will use LangGraph with the built-in formatting utility, but graph evaluators accept input in the following general format:
Python

classGraphTrajectory(TypedDict):
 # Only set when specifying reference_outputsinputs: Optional[list[dict]]
 results: list[dict]
 steps: list[list[str]]
 
defevaluator(
 *,
 inputs: Optional[Union[dict, list]] =None,
 outputs: GraphTrajectory,
 reference_outputs: Optional[GraphTrajectory] =None,
) -> ...

TypeScript

exporttypeGraphTrajectory={inputs?: (Record<string,unknown>|null)[];results: Record<string,unknown>[];steps: string[][];};constevaluator: ({ inputs, outputs, referenceOutputs, ...extra}: {inputs: (string|Record<string,unknown>|null)[]|{inputs: (string|Record<string,unknown>|null)[];};outputs: GraphTrajectory;referenceOutputs?: GraphTrajectory;[key: string]: unknown;})=> ...

Where 
inputs
 is a list of inputs (or a dict with a key named 
"inputs"
) to the graph whose items each represent the start of a new invocation in a thread, 
results
 representing the final output from each turn in the thread, and 
steps
 representing the internal steps taken for each turn.

Graph trajectory LLM-as-judge

This evaluator is similar to the 
trajectory_llm_as_judge
 evaluator, but it works with graph trajectories instead of message trajectories. Below, we set up a LangGraph agent, extract a trajectory from it using the built-in utils, and pass it to the evaluator. First, let's setup our graph, call it, and then extract the trajectory:
Python

fromagentevals.graph_trajectory.utilsimport (
 extract_langgraph_trajectory_from_thread,
)
fromagentevals.graph_trajectory.llmimportcreate_graph_trajectory_llm_as_judgefromlanggraph.prebuiltimportcreate_react_agentfromlanggraph.checkpoint.memoryimportMemorySaverfromlanggraph.typesimportCommand, interruptfromlangchain_core.toolsimporttool@tooldefsearch(query: str):
 """Call to surf the web."""user_answer=interrupt("Tell me the answer to the question.")
 returnuser_answertools= [search]

checkpointer=MemorySaver()
graph=create_react_agent(
 model="gpt-4o-mini",
 checkpointer=checkpointer,
 tools=[search],
)

graph.invoke(
 {"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
 config={"configurable": {"thread_id": "1"}},
)
# Resume the agent with a new command, simulating a human-in-the-loop workflowgraph.invoke(
 Command(resume="It is rainy and 70 degrees!"),
 config={"configurable": {"thread_id": "1"}},
)

# Extract the trajectory from the first two thread runsextracted_trajectory=extract_langgraph_trajectory_from_thread(
 graph, {"configurable": {"thread_id": "1"}}
)

print(extracted_trajectory)

{
 'inputs': [{
 '__start__': {
 'messages': [
 {'role': 'user', 'content': "what's the weather in sf?"}
 ]}
 }, 
 '__resuming__': {
 'messages': [
 {'role': 'user', 'content': 'It is rainy and 70 degrees!'}
 ]}
 ],
 'outputs': {
 'results': [
 {},
 {
 'messages': [
 {'role': 'ai', 'content': 'The current weather in San Francisco is rainy, with a temperature of 70 degrees.'}
 ]
 }
 ],
 'steps': [
 ['__start__', 'agent', 'tools', '__interrupt__'],
 ['agent']
 ]
 }
}

TypeScript

import{tool}from"@langchain/core/tools";import{ChatOpenAI}from"@langchain/openai";import{createReactAgent}from"@langchain/langgraph/prebuilt";import{MemorySaver,interrupt}from"@langchain/langgraph";import{z}from"zod";import{extractLangGraphTrajectoryFromThread}from"agentevals";constsearch=tool((_): string=>{constuserAnswer=interrupt("Tell me the answer to the question.")returnuserAnswer;},{name: "search",description: "Call to surf the web.",schema: z.object({query: z.string()})})consttools=[search];// Create a checkpointerconstcheckpointer=newMemorySaver();// Create the React agentconstgraph=createReactAgent({llm: newChatOpenAI({model: "gpt-4o-mini"}),
 tools,
 checkpointer,});// Invoke the graph with initial messageawaitgraph.invoke({messages: [{role: "user",content: "what's the weather in sf?"}]},{configurable: {thread_id: "1"}});// Resume the agent with a new command (simulating human-in-the-loop)awaitgraph.invoke({messages: [{role: "user",content: "It is rainy and 70 degrees!"}]},{configurable: {thread_id: "1"}});constextractedTrajectory=awaitextractLangGraphTrajectoryFromThread(graph,{configurable: {thread_id: "1"}},);console.log(extractedTrajectory);

{
 'inputs': [{
 '__start__': {
 'messages': [
 {'role': 'user', 'content': "what's the weather in sf?"}
 ]}
 }, 
 '__resuming__': {
 'messages': [
 {'role': 'user', 'content': 'It is rainy and 70 degrees!'}
 ]}
 ],
 'outputs': {
 'results': [
 {},
 {
 'messages': [
 {'role': 'ai', 'content': 'The current weather in San Francisco is rainy, with a temperature of 70 degrees.'}
 ]
 }
 ],
 'steps': [
 ['__start__', 'agent', 'tools', '__interrupt__'],
 ['agent']
 ]
 }
}

Now, we can pass the extracted trajectory to the evaluator:
Python

graph_trajectory_evaluator=create_graph_trajectory_llm_as_judge(
 model="openai:o3-mini",
)

res=graph_trajectory_evaluator(
 inputs=extracted_trajectory["inputs"],
 outputs=extracted_trajectory["outputs"],
)

print(res)

{
 'key': 'graph_trajectory_accuracy',
 'score': True,
 'comment': 'The overall process follows a logical progression: the conversation begins with the user’s request, the agent then processes the request through its own internal steps (including calling tools), interrupts to obtain further input, and finally resumes to provide a natural language answer. Each step is consistent with the intended design in the rubric, and the overall path is relatively efficient and semantically aligns with a typical query resolution trajectory. Thus, the score should be: true.'
}

TypeScript

import{createGraphTrajectoryLLMAsJudge}from"agentevals";constgraphTrajectoryEvaluator=createGraphTrajectoryLLMAsJudge({model: "openai:o3-mini",})constres=awaitgraphTrajectoryEvaluator({inputs: extractedTrajectory.inputs,outputs: extractedTrajectory.outputs,});console.log(res);

{
 'key': 'graph_trajectory_accuracy',
 'score': True,
 'comment': 'The overall process follows a logical progression: the conversation begins with the user’s request, the agent then processes the request through its own internal steps (including calling tools), interrupts to obtain further input, and finally resumes to provide a natural language answer. Each step is consistent with the intended design in the rubric, and the overall path is relatively efficient and semantically aligns with a typical query resolution trajectory. Thus, the score should be: true.'
}

Note that though this evaluator takes the typical 
inputs
, 
outputs
, and 
reference_outputs
 parameters, it internally combines 
inputs
 and 
outputs
 to form a 
thread
. Therefore, if you want to customize the prompt, your prompt should also contain a 
thread
 input variable:
Python

CUSTOM_PROMPT="""You are an expert data labeler.Your task is to grade the accuracy of an AI agent's internal steps in resolving a user queries.<Rubric> An accurate trajectory: - Makes logical sense between steps - Shows clear progression - Is perfectly efficient, with no more than one tool call - Is semantically equivalent to the provided reference trajectory, if present</Rubric><Instructions> Grade the following thread, evaluating whether the agent's overall steps are logical and relatively efficient. For the trajectory, "__start__" denotes an initial entrypoint to the agent, and "__interrupt__" corresponds to the agent interrupting to await additional data from another source ("human-in-the-loop"):</Instructions><thread>{thread}</thread>{reference_outputs}"""evaluator=create_graph_trajectory_llm_as_judge(
 prompt=CUSTOM_PROMPT,
 model="openai:o3-mini",
)
res=awaitevaluator(
 inputs=extracted_trajectory["inputs"],
 outputs=extracted_trajectory["outputs"], 
)

TypeScript

constCUSTOM_PROMPT=`You are an expert data labeler.Your task is to grade the accuracy of an AI agent's internal steps in resolving a user queries.<Rubric> An accurate trajectory: - Makes logical sense between steps - Shows clear progression - Is perfectly efficient, with no more than one tool call - Is semantically equivalent to the provided reference trajectory, if present</Rubric><Instructions> Grade the following thread, evaluating whether the agent's overall steps are logical and relatively efficient. For the trajectory, "__start__" denotes an initial entrypoint to the agent, and "__interrupt__" corresponds to the agent interrupting to await additional data from another source ("human-in-the-loop"):</Instructions><thread>{thread}</thread>{reference_outputs}`constgraphTrajectoryEvaluator=createGraphTrajectoryLLMAsJudge({prompt: CUSTOM_PROMPT,model: "openai:o3-mini",})constres=awaitgraphTrajectoryEvaluator({inputs: extractedTrajectory.inputs,outputs: extractedTrajectory.outputs,});

In order to format them properly into the prompt, 
reference_outputs
 should be passed in as a 
GraphTrajectory
 object like 
outputs
.

Also note that like other LLM-as-judge evaluators, you can pass extra params into the evaluator to format them into the prompt.

Graph trajectory strict match

The 
graph_trajectory_strict_match
 evaluator is a simple evaluator that checks if the steps in the provided graph trajectory match the reference trajectory exactly.
Python

fromagentevals.graph_trajectory.utilsimport (
 extract_langgraph_trajectory_from_thread,
)
fromagentevals.graph_trajectory.strictimportgraph_trajectory_strict_matchfromlanggraph.prebuiltimportcreate_react_agentfromlanggraph.checkpoint.memoryimportMemorySaverfromlanggraph.typesimportCommand, interruptfromlangchain_core.toolsimporttool@tooldefsearch(query: str):
 """Call to surf the web."""user_answer=interrupt("Tell me the answer to the question.")
 returnuser_answertools= [search]

checkpointer=MemorySaver()
graph=create_react_agent(
 model="gpt-4o-mini",
 checkpointer=checkpointer,
 tools=[search],
)

graph.invoke(
 {"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
 config={"configurable": {"thread_id": "1"}},
)
# Resume the agent with a new command, simulating a human-in-the-loop workflowgraph.invoke(
 Command(resume="It is rainy and 70 degrees!"),
 config={"configurable": {"thread_id": "1"}},
)

# Extract the trajectory from the first two thread runsextracted_trajectory=extract_langgraph_trajectory_from_thread(
 graph, {"configurable": {"thread_id": "1"}}
)

reference_trajectory= {
 # not used for strict match"results": [],
 "steps": [["__start__", "agent", "tools", "__interrupt__"], ["agent"]],
}

res=graph_trajectory_strict_match(
 outputs=extracted_trajectory["outputs"],
 reference_outputs=reference_trajectory,
)

print(res)

{
 'key': 'graph_trajectory_strict_match',
 'score': True,
}

TypeScript

import{tool}from"@langchain/core/tools";import{ChatOpenAI}from"@langchain/openai";import{createReactAgent}from"@langchain/langgraph/prebuilt";import{MemorySaver,interrupt}from"@langchain/langgraph";import{z}from"zod";import{extractLangGraphTrajectoryFromThread,graphTrajectoryStrictMatch}from"agentevals";constsearch=tool((_): string=>{constuserAnswer=interrupt("Tell me the answer to the question.")returnuserAnswer;},{name: "search",description: "Call to surf the web.",schema: z.object({query: z.string()})})consttools=[search];// Create a checkpointerconstcheckpointer=newMemorySaver();// Create the React agentconstgraph=createReactAgent({llm: newChatOpenAI({model: "gpt-4o-mini"}),
 tools,
 checkpointer,});// Invoke the graph with initial messageawaitgraph.invoke({messages: [{role: "user",content: "what's the weather in sf?"}]},{configurable: {thread_id: "1"}});// Resume the agent with a new command (simulating human-in-the-loop)awaitgraph.invoke({messages: [{role: "user",content: "It is rainy and 70 degrees!"}]},{configurable: {thread_id: "1"}});constextractedTrajectory=awaitextractLangGraphTrajectoryFromThread(graph,{configurable: {thread_id: "1"}},);constreferenceTrajectory={results: [],steps: [["__start__","agent","tools","__interrupt__"],["agent"]],}constresult=awaitgraphTrajectoryStrictMatch({outputs: trajectory.outputs,referenceOutputs: referenceOutputs!,});console.log(result);

{
 'key': 'graph_trajectory_strict_match',
 'score': True,
}

Python Async Support

All 
agentevals
 evaluators support Python asyncio. As a convention, evaluators that use a factory function will have 
async
 put immediately after 
create_
 in the function name (for example, 
create_async_trajectory_llm_as_judge
), and evaluators used directly will end in 
async
 (e.g. 
trajectory_strict_match_async
).

Here's an example of how to use the 
create_async_llm_as_judge
 evaluator asynchronously:

fromagentevals.trajectory.llmimportcreate_async_trajectory_llm_as_judgeevaluator=create_async_llm_as_judge(
 prompt="What is the weather in {inputs}?",
)

result=awaitevaluator(inputs="San Francisco")

If you are using the OpenAI client directly, remember to pass in 
AsyncOpenAI
 as the 
judge
 parameter:

fromopenaiimportAsyncOpenAIevaluator=create_async_llm_as_judge(
 prompt="What is the weather in {inputs}?",
 judge=AsyncOpenAI(),
 model="o3-mini",
)

result=awaitevaluator(inputs="San Francisco")

LangSmith Integration

For tracking experiments over time, you can log evaluator results to LangSmith, a platform for building production-grade LLM applications that includes tracing, evaluation, and experimentation tools.

LangSmith currently offers two ways to run evals: a pytest (Python) or Vitest/Jest integration and the 
evaluate
 function. We'll give a quick example of how to run evals using both.

Pytest or Vitest/Jest

First, follow these instructions to set up LangSmith's pytest runner, or these to set up Vitest or Jest,
setting appropriate environment variables:

export LANGSMITH_API_KEY="your_langsmith_api_key"export LANGSMITH_TRACING="true"

Python
Then, set up a file named 
test_trajectory.py
 with the following contents:

importpytestimportjsonfromlangsmithimporttestingastfromagentevals.trajectory.llmimportcreate_trajectory_llm_as_judgetrajectory_evaluator=create_trajectory_llm_as_judge(
 model="openai:o3-mini",
)

@pytest.mark.langsmithdeftest_trajectory_accuracy():
 outputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "SF"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
 {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
 ]
 reference_outputs= [
 {"role": "user", "content": "What is the weather in SF?"},
 {
 "role": "assistant",
 "content": "",
 "tool_calls": [
 {
 "function": {
 "name": "get_weather",
 "arguments": json.dumps({"city": "San Francisco"}),
 }
 }
 ],
 },
 {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco."},
 {"role": "assistant", "content": "The weather in SF is 80˚ and sunny."},
 ]

 t.log_inputs({})
 t.log_outputs({"messages": outputs})
 t.log_reference_outputs({"messages": reference_outputs})

 trajectory_evaluator(
 outputs=outputs,
 reference_outputs=reference_outputs
 )

Note that when creating the evaluator, we've added a 
feedback_key
 parameter. This will be used to name the feedback in LangSmith.

Now, run the eval with pytest:

pytest test_trajectory.py --langsmith-output

TypeScript
Then, set up a file named 
test_trajectory.eval.ts
 with the following contents:

import*aslsfrom"langsmith/vitest";// import * as ls from "langsmith/jest";import{createTrajectoryLLMAsJudge}from"agentevals";consttrajectoryEvaluator=createTrajectoryLLMAsJudge({model: "openai:o3-mini",});ls.describe("trajectory accuracy",()=>{ls.test("accurate trajectory",{inputs: {messages: [{role: "user",content: "What is the weather in SF?"}]},referenceOutputs: {messages: [{"role": "user","content": "What is the weather in SF?"},{"role": "assistant","content": "","tool_calls": [{"function": {"name": "get_weather","arguments": JSON.stringify({"city": "San Francisco"}),}}],},{"role": "tool","content": "It's 80 degrees and sunny in San Francisco."},{"role": "assistant","content": "The weather in SF is 80˚ and sunny."},],},},async({ inputs, referenceOutputs })=>{constoutputs=[{"role": "user","content": "What is the weather in SF?"},{"role": "assistant","content": "","tool_calls": [{"function": {"name": "get_weather","arguments": JSON.stringify({"city": "SF"}),}}],},{"role": "tool","content": "It's 80 degrees and sunny in SF."},{"role": "assistant","content": "The weather in SF is 80 degrees and sunny."},];ls.logOutputs({messages: outputs});awaittrajectoryEvaluator({
 inputs,
 outputs,
 referenceOutputs,});});});

Now, run the eval with your runner of choice:

vitest run test_trajectory.eval.ts

Feedback from the prebuilt evaluator will be automatically logged in LangSmith as a table of results like this in your terminal:

And you should also see the results in the experiment view in LangSmith:

Evaluate

Alternatively, you can create a dataset in LangSmith and use your created evaluators with LangSmith's 
evaluate
 function:
Python

fromlangsmithimportClientfromagentevals.trajectory.llmimportcreate_trajectory_llm_as_judgeclient=Client()

trajectory_evaluator=create_trajectory_llm_as_judge(
 model="openai:o3-mini",
)

experiment_results=client.evaluate(
 # This is a dummy target function, replace with your actual LLM-based systemlambdainputs: "What color is the sky?",
 data="Sample dataset",
 evaluators=[
 trajectory_evaluator
 ]
)

TypeScript

import{evaluate}from"langsmith/evaluation";import{createTrajectoryLLMAsJudge,TRAJECTORY_ACCURACY_PROMPT}from"agentevals";consttrajectoryEvaluator=createTrajectoryLLMAsJudge({model: "openai:o3-mini",prompt: TRAJECTORY_ACCURACY_PROMPT});awaitevaluate((inputs)=>[{role: "user",content: "What is the weather in SF?"},{role: "assistant",content: "",tool_calls: [{function: {name: "get_weather",arguments: json.dumps({"city": "SF"}),}}],},{role: "tool",content: "It's 80 degrees and sunny in SF."},{role: "assistant",content: "The weather in SF is 80 degrees and sunny."},],{data: datasetName,evaluators: [trajectoryEvaluator],});

Thank you!

We hope that 
agentevals
 helps make evaluating your LLM agents easier!

If you have any questions, comments, or suggestions, please open an issue or reach out to us on X @LangChainAI.

About

 Readymade evaluators for agent trajectories
 

Resources

 Readme

License

 MIT license
 

Code of conduct

 Code of conduct
 

Contributing

 Contributing
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

545
 stars

Watchers

7
 watching

Forks

40
 forks

 Report repository

Releases
 12

js==0.0.7
 Latest

Mar 3, 2026

+ 11 releases

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python62.6%

TypeScript36.4%

JavaScript1.0%

Footer

 © 2026 GitHub, Inc.
 

Footer navigation

Terms

Privacy

Security

Status

Community

Docs

Contact

 Manage cookies
 

 Do not share my personal information
 

 You can’t perform that action at this time.

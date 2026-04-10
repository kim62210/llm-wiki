---
title: Agent evaluation - Arize AX Docs
source_url: https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-tool-selection
final_url: https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation
status: 200
content_type: text/plain; charset=utf-8
topics: [Tool Selection & Tool Invocation Evaluators]
sections: [Evals & Observability]
fetched_at: 2026-04-10T02:10:00+00:00
---

# Agent evaluation - Arize AX Docs

## 원본 URL

https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-tool-selection

## 대체 수집 URL

https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation

## 추출 본문

Title: Agent evaluation - Arize AX Docs

URL Source: https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation

Markdown Content:
Getting agents to work is hard. LLMs are non-deterministic. A bad response upstream leads to a strange response downstream. Agents can take inefficient paths and still get to the right solution. Frameworks make building easier, but debugging harder.An agent is characterized by what it knows about the world, the set of actions it can perform, and the pathway it took to get there. To [evaluate an agent](https://arize.com/ai-agents/agent-evaluation/), we must evaluate each of these components.We’ve built evaluation templates for every step:

*   [Agent Tool Calling](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge/arize-evaluators-llm-as-a-judge/tool-calling-eval.md)
    *   [Agent Tool Selection](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-tool-selection.md)
    *   [Agent Parameter Extraction](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-parameter-extraction.md)

*   [Agent Path Convergence](https://arize.com/docs/ax/evaluate/evaluators/code-evaluations/agent-convergence.md)
*   [Agent Planning](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-planning.md)
*   [Agent Reflection](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-reflection.md)

You can evaluate the individual skills and response using normal LLM evaluation strategies, such as Retrieval Evaluation, Classification with LLM as a Judge, [Hallucination](https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/hallucinations), or [Q&A Correctness](https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/q-and-a-on-retrieved-data).Read more to see the breakdown of each component.

## **Router**

The first thing an agent needs to figure out is given a query, what should it do? One way is to ask it every time — use the LLM to act based on its inputs and memory. This “router” architecture is quite flexible. Sometimes it is also built using rules.

To evaluate a router, you need to check that given an input, did it choose the right skill? And did it specify the right parameter values? Agents can call tools, write code, or choose neither and respond in kind.You will need to account for several scenarios in your test cases, such as:

*   Missing context, short context, and long context
*   No functions should be called, one function should be called, or multiple functions should be called
*   Vague or opaque parameters in query, vs. very specific parameters in query.
*   Single turn vs. multi-turn conversation pathways

See our [Agent tool calling evaluation template](https://app.gitbook.com/s/-MAlgpMyBRcl2qFZRQ67/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/tool-calling-eval) for a more specific example.

* * *

## Planner

For complex tasks with a large number of steps, it can be better to come up with the list of steps first and evaluate it, instead of generating each step one at a time. The router architecture can either short circuit and not call enough tools, or it gets stuck in loops and generates hundreds of steps and waste lots of time and energy.

This “planner” architecture means the agent must first generate its to do list. Then, it needs to validate the plan. The plan can be validated using heuristics. You can also use an LLM call to evaluate the plan, and if the plan is bad, retry until it is good with a limit on retries.You can evaluate the plan by asking the following questions, manually or with an LLM:

1.   Does the plan include only skills that are valid?
2.   Is the plan less than X number of steps?
3.   Are Z skills sufficient to accomplish this task?
4.   Will Y plan accomplish this task given Z skills?
5.   Is this the shortest plan to accomplish this task?

See our [Agent Planning Evaluation template](https://app.gitbook.com/s/-MAlgpMyBRcl2qFZRQ67/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-planning) for a more specific example.

* * *

## Skills

These are individual logic blocks and chains that can complete a task — e.g. an SQL query skill or RAG retriever. Since LLMs only have access to the data it was trained on, skills are a lever for agents to acquire knowledge, do more things like generate images or execute code, and take action in the world via APIs.You can evaluate these using standard LLM or code evaluations. The assumption here is that the skill was called correctly, so you are evaluating the skill output given a correct input.Some examples are:

*   Retrieval Relevance
*   [QA Correctness](https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/q-and-a-on-retrieved-data)
*   [Hallucination](https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/hallucinations)
*   [User frustration](https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/user-frustration)

You can also evaluate by comparing against ground truth data. We have built [Phoenix](https://app.gitbook.com/s/yYiH3D9rUbrh3jUtdpK4/python-packages/arize-phoenix-evals) and [llm_classify](https://app.gitbook.com/s/-MAlgpMyBRcl2qFZRQ67/evaluate/llm-as-a-judge/custom-evaluators#llm-classification)to easily accomplish this.

* * *

## Memory

Shared memory state that can be accessed by each component. LLM APIs rely on receiving all the agent steps in their context window to decide on the next step. This is used to store retrieved context, config variables, previous execution steps, etc.As the agent takes steps to solve a query, it will record the path it took in its memory.To evaluate the pathway of an agent, try to evaluate the following:

*   Did the agent go off the rails and onto the wrong pathway?
*   Does it get stuck in an infinite loop?
*   Does it choose the right sequence of steps to take given a whole agent pathway for a single action?

Agent convergence is one way to see how your agent performs. This is a numerical value, which is the `length of the optimal path / length of the average path` for similar queries. See our [Agent convergence evaluation template](https://app.gitbook.com/s/-MAlgpMyBRcl2qFZRQ67/evaluate/code-evaluations/agent-convergence) for a specific example.

* * *

## Reflection

After a task is completed, a plan is created, or an answer is generated, before calling it done, it can be helpful to ask the agent to reflect on the final output and whether it accomplished the task. If it did not, then retry.This is like running evaluations at runtime, instead of after the fact, which can improve the quality of your agents.See our [Agent Reflection evaluation template](https://app.gitbook.com/s/-MAlgpMyBRcl2qFZRQ67/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-reflection) for a more specific example.

Source: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)

* * *

## Example E-Commerce Agent

An example agent could be an e-commerce chat to purchase agent. To evaluate this agent, you would first check if the router step was functioning properly. Next you would evaluate the outputs of the tools and skills. And lastly, you would ensure at each step, the memory was recorded correctly and the ideal path was taken.[See our full notebook](https://arize.com/docs/ax/cookbooks/agents/tracing-a-routing-agent) which walks through this example.

## Other reading


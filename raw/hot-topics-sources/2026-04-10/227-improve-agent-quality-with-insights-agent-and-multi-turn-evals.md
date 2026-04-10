---
title: Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmith
source_url: https://blog.langchain.com/insights-agent-multiturn-evals-langsmith
final_url: https://blog.langchain.com/insights-agent-multiturn-evals-langsmith/
status: 200
content_type: text/html; charset=utf-8
topics: [Multi-Turn Agent Evaluation]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:58.327402+00:00
---

# Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmith

## 원본 URL

https://blog.langchain.com/insights-agent-multiturn-evals-langsmith

## 추출 본문

Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmithSkip to content

Website

Docs

Case Studies

Harrison's In the Loop Series

Try LangSmith

Sign inSubscribe

Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmith

LangSmith's new Insights Agent and Multi-turn Evals help you understand what your agents are doing in production and whether they're accomplishing user goals.

4 min readOct 23, 2025

TL;DR: We’re releasing new capabilities in LangSmith to help monitor agents in production. We’re making the concept of “threads” - representing a multi-turn agent interaction - a first-party concept, and we’re adding two new tools to monitor threads: Insights Agent for automatically categorizing agent usage patterns, and Multi-turn Evals for scoring complete agent conversations.

More and more agents are moving to production. As they do so, AI teams find themselves needing better visibility into what’s happening across all user interactions. But, traditional observability and testing that focus on uptime can't tell whether your agent is actually accomplishing users’ goals. And testing your agent before it goes into production (what we call offline evals) only covers what you had in mind to start.

Today, we’re releasing new features to help you understand what’s happening inside your agent while it’s in production, so you can prioritize improvements:

Insight Agent: automatically categorizes agent behavior patterns

Multi-turn Evals: helps you evaluate the complete agent trajectory in each conversation

Discover patterns in production traces with the Insights Agent

Today's popular agents produce millions of traces per day—soon to be billions. These traces contain valuable signal about an agent's capabilities and how real users engage with it. If you could review each interaction, you would gain deep insight into how to improve your agent. Manual review is time-consuming and impossible at scale, so how can we automate this insight generation process?

Insights Agent is our first step towards helping LangSmith users find signal in their production traces. Insights Agent analyzes traces to discover and surface common usage patterns, agent behaviors, and failure modes.

In agent engineering, you need to iterate rapidly to build reliable experiences. This new feature helps you answer questions like “What are users asking my agent?”, so you can determine where to focus your next set of tests based on real interactions your agent is having.

Once you trace your data to LangSmith, you have a few options for how to categorize usage insights.

Group by usage patterns: Cluster based on common usage patterns. This helps you understand how users are actually using your agent. When you put a chatbot in front of people, they can ask it anything. Now you can find out what they are asking.

Group by poor interactions: Cluster based on how your agent is messing up. We will look for signals in each conversation that indicate a negative interaction (user getting frustrated, etc), and then group the root causes. This helps you understand common ways your agent fails, so you can prioritize improvements.

Customize configurations: Insights Agent is highly configurable. You can specify which categories it should group by, filter on existing attributes (like traces from a particular time period or keywords in a chat), define new attributes, and save configs for future use.

Generating insights can take up to 15 minutes depending on how much data the agent is crunching. Once the report is ready, you’ll see traces organized into categories and subcategories based on your initial request. You can click into any category to explore the underlying traces and add them to datasets or annotation queues. You can also see other LangSmith metrics split by category, like latency, number of runs, and any evals you have set up.

Our goal in building this feature was to help you kick off exploration and ideas for improvements as quickly as possible.

Insights Agent is now generally available for LangSmith Plus and Enterprise cloud customers. Sign up for LangSmith and check out our docs to get started.

Evaluate end-to-end agent interactions with Multi-turn Evals

Once you have a good sense of the top usage patterns your agent is handling, you can start to drill into how each complete conversation is performing. Until now, that’s been tricky — most other evaluation platforms only focus on individual traces or steps, making it hard to understand whether the overall interaction achieved the user’s goal.

Today, we're launching Multi-turn Evals to help you measure whether your agent accomplished the user’s goal across an entire interaction. You can do still evaluate at the trace level in LangSmith, but now you can also but also evaluate the whole interaction.

Multi-turn evals are online evaluations that let you measure things like:

Semantic intent: What the user was actually trying to do.

Semantic outcomes: Whether the task was completed (and if not, why).

Agent trajectory: How the interaction unfolded, including tool calls and decisions made along the way.

In LangSmith, we represent these multi-turn exchanges between users and agents as threads. If you’re already using threads, getting started is simple. Multi-turn evals run automatically once a conversation is complete, and you define the LLM-as-a-judge prompt to guide scoring.

Insights Agent and Multi-turn evals are the first of several thread-level features we’re working on. Stay tuned for thread-level metrics and dashboards, automations to add threads to an annotation queue and datasets, and SDK support so you can programmatically pull and analyze threads.

Multi-turn evals are live today for all LangSmith users.Visit our docs to get started.

Iterate faster with LangSmith

Our latest LangSmith updates work together to address tough challenges when engineering reliable agents. Now, you can understand what's happening in production (Insights Agent) and measure whether agents accomplish user goals (Multi-turn Evals). These features provide new levels of visibility to help you figure out what’s the best next step to improving your agent.

Ready to ship reliable agents? Get started with LangSmith today.

Join our newsletter

Updates from the LangChain team and community

Enter your emailSubscribe

Processing your application...

Success! Please check your inbox and click the link to confirm your subscription.

Sorry, something went wrong. Please try again.

 © LangChain Blog 2026

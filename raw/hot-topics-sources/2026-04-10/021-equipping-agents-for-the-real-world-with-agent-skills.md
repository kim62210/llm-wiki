---
title: Equipping agents for the real world with Agent Skills \ Anthropic | Claude
source_url: https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills
final_url: https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills
status: 200
content_type: text/html; charset=utf-8
topics: [Agent Skills (Progressive Disclosure Filesystem Pattern)]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:27.073573+00:00
---

# Equipping agents for the real world with Agent Skills \ Anthropic | Claude

## 원본 URL

https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills

## 추출 본문

Equipping agents for the real world with Agent Skills \ Anthropic | Claude

Meet Claude

Products

Claude

Claude Code

Claude Cowork

Features

Claude for Chrome

Claude for Slack

Claude for Excel

Claude for PowerPoint

Skills

Models

Opus

Sonnet

Haiku

Platform

Overview

Developer docs

Pricing

Console login

Solutions

Use cases

AI agents

Coding

Departments

Security

Industries

Customer support

Education

Financial services

Government

Healthcare

Life sciences

Nonprofits

Pricing

Overview

API

Plans

Pro

Max

Team

Enterprise

Resources

Insights

Blog

Customer stories

Anthropic news

Learn

Anthropic Academy

Courses

Tutorials

Use cases

Tools

Connectors

Plugins

Connect

Events

Community

Login

Contact sales

Contact salesContact sales

Try Claude

Try ClaudeTry Claude

Contact sales

Contact salesContact sales

Try Claude

Try ClaudeTry Claude

Contact sales

Contact salesContact sales

Try Claude

Try ClaudeTry Claude

Contact sales

Contact salesContact sales

Try Claude

Try ClaudeTry Claude

Meet Claude

Products

Claude

Claude Code

Claude Cowork

Features

Claude for Chrome

Claude for Slack

Claude for Excel

Claude for PowerPoint

Skills

Models

Opus

Sonnet

Haiku

Platform

Overview

Developer docs

Pricing

Console login

Solutions

Use cases

AI agents

Coding

Departments

Security

Industries

Customer support

Education

Financial services

Government

Healthcare

Life sciences

Nonprofits

Pricing

Overview

API

Plans

Pro

Max

Team

Enterprise

Resources

Insights

Blog

Customer stories

Anthropic news

Learn

Anthropic Academy

Courses

Tutorials

Use cases

Tools

Connectors

Plugins

Connect

Events

Community

Login

Contact sales

Contact salesContact sales

Try Claude

Try ClaudeTry Claude

Contact sales

Contact salesContact sales

Try Claude

Try ClaudeTry Claude

Blog

Blog

/

Equipping agents for the real world with Agent Skills

Explore here

Ask questions about this page

Copy as markdown

Equipping agents for the real world with Agent Skills

Claude is powerful, but real work requires procedural knowledge and organizational context. Introducing Agent Skills, a new way to build specialized agents using files and folders.

Category

Claude Code

Agents

Product

Claude Code

Claude Platform

Date

October 16, 2025

Reading time

5

min

Share
Copy link
https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills

Update: We've publishedAgent Skillsas an open standard for cross-platform portability. (December 18, 2025)

As model capabilities improve, we can now build general-purpose agents that interact with full-fledged computing environments. Claude Code, for example, can accomplish complex tasks across domains using local code execution and filesystems. But as these agents become more powerful, we need more composable, scalable, and portable ways to equip them with domain-specific expertise.

This led us to create Agent Skills: organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks.Skills extend Claude’s capabilities by packaging your expertise into composable resources for Claude, transforming general-purpose agents into specialized agents that fit your needs.

Building a skill for an agent is like putting together an onboarding guide for a new hire. Instead of building fragmented, custom-designed agents for each use case, anyone can now specialize their agents with composable capabilities by capturing and sharing their procedural knowledge. In this article, we explain what Skills are, show how they work, and share best practices for building your own.

A skill is a directory containing a SKILL.md file that contains organized folders of instructions, scripts, and resources that give agents additional capabilities.
The anatomy of a skill

To see Skills in action, let’s walk through a real example: one of the skills that powers Claude’s recently launched document editing abilities. Claude already knows a lot about understanding PDFs, but is limited in its ability to manipulate them directly (e.g. to fill out a form). This PDF skill lets us give Claude these new abilities.

At its simplest, a skill is a directory that contains a 
SKILL.md file
. This file must start with YAML frontmatter that contains some required metadata: 
name
 and 
description
. At startup, the agent pre-loads the 
name
 and 
description
 of every installed skill into its system prompt.

This metadata is the first level of progressive disclosure: it provides just enough information for Claude to know when each skill should be used without loading all of it into context. The actual body of this file is the second level of detail. If Claude thinks the skill is relevant to the current task, it will load the skill by reading its full 
SKILL.md
 into context.

A SKILL.md file must begin with YAML Frontmatter that contains a file name and description, which is loaded into its system prompt at startup.
As skills grow in complexity, they may contain too much context to fit into a single 
SKILL.md
, or context that’s relevant only in specific scenarios. In these cases, skills can bundle additional files within the skill directory and reference them by name from 
SKILL.md
. These additional linked files are the third level (and beyond) of detail, which Claude can choose to navigate and discover only as needed.

In the PDF skill shown below, the 
SKILL.md
 refers to two additional files (
reference.md
 and 
forms.md
) that the skill author chooses to bundle alongside the core 
SKILL.md
. By moving the form-filling instructions to a separate file (
forms.md
), the skill author is able to keep the core of the skill lean, trusting that Claude will read 
forms.md
 only when filling out a form.

You can incorporate more context (via additional files) into your skill that can then be triggered by Claude based on the system prompt.
Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable. Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed:

Agents with a filesystem and code execution tools don’t need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded.

Skills and the context window

The following diagram shows how the context window changes when a skill is triggered by a user’s message.

Skills are triggered in the context window via your system prompt.
The sequence of operations shown:

To start, the context window has the core system prompt and the metadata for each of the installed skills, along with the user’s initial message;

Claude triggers the PDF skill by invoking a Bash tool to read the contents of 
pdf/SKILL.md
;

Claude chooses to read the 
forms.md
 file bundled with the skill;

Finally, Claude proceeds with the user’s task now that it has loaded relevant instructions from the PDF skill.

Skills and code execution

Skills can also include code for Claude to execute as tools at its discretion.

Large language models excel at many tasks, but certain operations are better suited for traditional code execution. For example, sorting a list via token generation is far more expensive than simply running a sorting algorithm. Beyond efficiency concerns, many applications require the deterministic reliability that only code can provide.

In our example, the PDF skill includes a pre-written Python script that reads a PDF and extracts all form fields. Claude can run this script without loading either the script or the PDF into context. And because code is deterministic, this workflow is consistent and repeatable.

Skills can also include code for Claude to execute as tools at its discretion based on the nature of the task.
Developing and evaluating skills

Here are some helpful guidelines for getting started with authoring and testing skills:

Start with evaluation: Identify specific gaps in your agents’ capabilities by running them on representative tasks and observing where they struggle or require additional context. Then build skills incrementally to address these shortcomings.

Structure for scale: When the 
SKILL.md
 file becomes unwieldy, split its content into separate files and reference them. If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage. Finally, code can serve as both executable tools and as documentation. It should be clear whether Claude should run scripts directly or read them into context as reference.

Think from Claude’s perspective: Monitor how Claude uses your skill in real scenarios and iterate based on observations: watch for unexpected trajectories or overreliance on certain contexts. Pay special attention to the 
name
 and 
description
 of your skill. Claude will use these when deciding whether to trigger the skill in response to its current task.

Iterate with Claude: As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong. This process will help you discover what context Claude actually needs, instead of trying to anticipate it upfront.

Security considerations when using Skills

Skills provide Claude with new capabilities through instructions and code. While this makes them powerful, it also means that malicious skills may introduce vulnerabilities in the environment where they’re used or direct Claude to exfiltrate data and take unintended actions.

We recommend installing skills only from trusted sources. When installing a skill from a less-trusted source, thoroughly audit it before use. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

The future of Skills

Agent Skills are supported today across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform.

In the coming weeks, we’ll continue to add features that support the full lifecycle of creating, editing, discovering, sharing, and using Skills. We’re especially excited about the opportunity for Skills to help organizations and individuals share their context and workflows with Claude. We’ll also explore how Skills can complement Model Context Protocol (MCP) servers by teaching agents more complex workflows that involve external tools and software.

Looking further ahead, we hope to enable agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities.

Skills are a simple concept with a correspondingly simple format. This simplicity makes it easier for organizations, developers, and end users to build customized agents and give them new capabilities.

We’re excited to see what people build with Skills. Get started today by checking out our Skills docs and cookbook.

Acknowledgements

Written by Barry Zhang, Keith Lazuka, and Mahesh Murag, who all really like folders. Special thanks to the many others across Anthropic who championed, supported, and built Skills.

No items found.

PrevPrev

0/5

NextNext

eBook

FAQ

No items found.

Get Claude Code

Desktop

VS Code

JetBrains

On the web

Slack

curl -fsSL https://claude.ai/install.sh | bash

Copy command to clipboard

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the documentation

Try Claude Code

Try Claude CodeTry Claude Code

Developer docs

Developer docsDeveloper docs

Related posts

Explore more product news and best practices for teams building with Claude.

Apr 7, 2026

How and when to use subagents in Claude Code

Claude Code

How and when to use subagents in Claude CodeHow and when to use subagents in Claude Code

How and when to use subagents in Claude CodeHow and when to use subagents in Claude Code

Apr 2, 2026

Harnessing Claude’s intelligence

Agents

Harnessing Claude’s intelligenceHarnessing Claude’s intelligence

Harnessing Claude’s intelligenceHarnessing Claude’s intelligence

Mar 19, 2026

Product management on the AI exponential 

Claude Code

Product management on the AI exponential Product management on the AI exponential 

Product management on the AI exponential Product management on the AI exponential 

Feb 23, 2026

How AI helps break the cost barrier to COBOL modernization

Claude Code

How AI helps break the cost barrier to COBOL modernizationHow AI helps break the cost barrier to COBOL modernization

How AI helps break the cost barrier to COBOL modernizationHow AI helps break the cost barrier to COBOL modernization

Transform how your organization operates with Claude

See pricing

See pricingSee pricing

Contact sales

Contact salesContact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

SubscribeSubscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

HomepageHomepage

NextNext

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

Button TextButton Text

Learn

Button TextButton Text

Code

Button TextButton Text

Write

Help me develop a unique voice for an audience

Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Improve my writing style

Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Brainstorm creative ideas

Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

Explain a complex topic simply

Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Help me make sense of these ideas

Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Prepare for an exam or interview

Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

Explain a programming concept

Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Look over my code and give me tips

Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Vibe code with me

Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

Write case studies

This is another test

Write grant proposals

Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. 

Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Write video scripts

this is a test

AnthropicAnthropic

© [year] Anthropic PBC

Products

Claude

ClaudeClaude

Claude Code

Claude CodeClaude Code

Claude Code for Enterprise

Claude Code for EnterpriseClaude Code for Enterprise

Claude Cowork

Claude CoworkClaude Cowork

Pro plan

Pro planPro plan

Max plan

Max planMax plan

Team plan

Team planTeam plan

Enterprise plan

Enterprise planEnterprise plan

Download app

Download appDownload app

Pricing

PricingPricing

Log in

Log inLog in

Features

Claude Code Security

Claude Code SecurityClaude Code Security

Claude for Chrome

Claude for ChromeClaude for Chrome

Claude for Slack

Claude for SlackClaude for Slack

Claude for Excel

Claude for ExcelClaude for Excel

Claude for PowerPoint

Claude for PowerPointClaude for PowerPoint

Skills

SkillsSkills

Models

Mythos preview

Mythos previewMythos preview

Opus

OpusOpus

Sonnet

SonnetSonnet

Haiku

HaikuHaiku

Solutions

AI agents

AI agentsAI agents

Code modernization

Code modernizationCode modernization

Coding

CodingCoding

Customer support

Customer supportCustomer support

Education

EducationEducation

Financial services

Financial servicesFinancial services

Government

GovernmentGovernment

Healthcare

HealthcareHealthcare

Life sciences

Life sciencesLife sciences

Nonprofits

NonprofitsNonprofits

Security

SecuritySecurity

Claude Platform

Overview

OverviewOverview

Developer docs

Developer docsDeveloper docs

Pricing

PricingPricing

Marketplace

MarketplaceMarketplace

Amazon Bedrock

Amazon BedrockAmazon Bedrock

Google Cloud’s Vertex AI

Google Cloud’s Vertex AIGoogle Cloud’s Vertex AI

Microsoft Foundry

Microsoft FoundryMicrosoft Foundry

Regional compliance

Regional complianceRegional compliance

Console login

Console loginConsole login

Resources

Blog

BlogBlog

Claude partner network

Claude partner networkClaude partner network

Community

CommunityCommunity

Connectors

ConnectorsConnectors

Courses

CoursesCourses

Customer stories

Customer storiesCustomer stories

Engineering at Anthropic

Engineering at AnthropicEngineering at Anthropic

Events

EventsEvents

Plugins

PluginsPlugins

Powered by Claude

Powered by ClaudePowered by Claude

Service partners

Service partnersService partners

Startups program

Startups programStartups program

Tutorials

TutorialsTutorials

Use cases

Use casesUse cases

Company

Anthropic

AnthropicAnthropic

Careers

CareersCareers

Economic Futures

Economic FuturesEconomic Futures

Research

ResearchResearch

News

NewsNews

Responsible Scaling Policy

Responsible Scaling PolicyResponsible Scaling Policy

Security and compliance

Security and complianceSecurity and compliance

Transparency

TransparencyTransparency

Help and security

Availability

AvailabilityAvailability

Status

StatusStatus

Support center

Support centerSupport center

Terms and policies

Privacy choices

Cookie settings

 We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy here.
 

 Customize cookie settings
 Reject all cookies
 Accept all cookies

Necessary
Enables security and basic functionality.

Required

Analytics
Enables tracking of site performance.

Off

Marketing
Enables ads personalization and tracking.

Off

 Save preferences
 

Privacy policy

Privacy policyPrivacy policy

Responsible disclosure policy

Responsible disclosure policyResponsible disclosure policy

Terms of service: Commercial

Terms of service: CommercialTerms of service: Commercial

Terms of service: Consumer

Terms of service: ConsumerTerms of service: Consumer

Usage policy

Usage policyUsage policy

x.comx.com

LinkedInLinkedIn

YouTubeYouTube

InstagramInstagram

English (US)

English (US)

日本語 (Japan)

Deutsch (Germany)

Français (France)

한국어 (South Korea)

Claude Code

Claude Platform

Agents

Coding

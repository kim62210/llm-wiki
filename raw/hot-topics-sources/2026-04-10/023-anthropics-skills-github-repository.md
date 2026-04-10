---
title: GitHub - anthropics/skills: Public repository for Agent Skills · GitHub
source_url: https://github.com/anthropics/skills
final_url: https://github.com/anthropics/skills
status: 200
content_type: text/html; charset=utf-8
topics: [Agent Skills (Progressive Disclosure Filesystem Pattern), Agent Skills (SKILL.md) Standard]
sections: [Agent Architecture, Harness Engineering]
fetched_at: 2026-04-10T01:43:28.108187+00:00
---

# GitHub - anthropics/skills: Public repository for Agent Skills · GitHub

## 원본 URL

https://github.com/anthropics/skills

## 추출 본문

GitHub - anthropics/skills: Public repository for Agent Skills · GitHub

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

 anthropics
/skillsPublic

Notifications
You must be signed in to change notification settings

Fork
 13k

 Star
114k

Code

Issues187

Pull requests484

Discussions

Actions

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Security and quality

 Insights

anthropics/skills

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
27 Commits

27 Commits

.claude-plugin

.claude-plugin

skills

skills

spec

spec

template

template

.gitignore

.gitignore

README.md

README.md

THIRD_PARTY_NOTICES.md

THIRD_PARTY_NOTICES.md

View all files

Repository files navigation

README

Note: This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see agentskills.io.

Skills

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

For more information, check out:

What are skills?

Using skills in Claude

How to create custom skills

Equipping agents for the real world with Agent Skills

About This Repository

This repository contains skills that demonstrate what's possible with Claude's skills system. These skills range from creative applications (art, music, design) to technical tasks (testing web apps, MCP server generation) to enterprise workflows (communications, branding, etc.).

Each skill is self-contained in its own folder with a 
SKILL.md
 file containing the instructions and metadata that Claude uses. Browse through these skills to get inspiration for your own skills or to understand different patterns and approaches.

Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power Claude's document capabilities under the hood in the 
skills/docx
, 
skills/pdf
, 
skills/pptx
, and 
skills/xlsx
 subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application.

Disclaimer

These skills are provided for demonstration and educational purposes only. While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

Skill Sets

./skills: Skill examples for Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills

./spec: The Agent Skills specification

./template: Skill template

Try in Claude Code, Claude.ai, and the API

Claude Code

You can register this repository as a Claude Code Plugin marketplace by running the following command in Claude Code:

/plugin marketplace add anthropics/skills

Then, to install a specific set of skills:

Select 
Browse and install plugins

Select 
anthropic-agent-skills

Select 
document-skills
 or 
example-skills

Select 
Install now

Alternatively, directly install either Plugin via:

/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills

After installing the plugin, you can use the skill by just mentioning it. For instance, if you install the 
document-skills
 plugin from the marketplace, you can ask Claude Code to do something like: "Use the PDF skill to extract the form fields from 
path/to/some-file.pdf
"

Claude.ai

These example skills are all already available to paid plans in Claude.ai.

To use any skill from this repository or upload custom skills, follow the instructions in Using skills in Claude.

Claude API

You can use Anthropic's pre-built skills, and upload custom skills, via the Claude API. See the Skills API Quickstart for more.

Creating a Basic Skill

Skills are simple to create - just a folder with a 
SKILL.md
 file containing YAML frontmatter and instructions. You can use the template-skill in this repository as a starting point:

---name: my-skill-namedescription: A clear description of what this skill does and when to use it---# My Skill Name[Add your instructions here that Claude will follow when this skill is active]## Examples- Example usage 1
- Example usage 2

## Guidelines- Guideline 1
- Guideline 2

The frontmatter requires only two fields:

name
 - A unique identifier for your skill (lowercase, hyphens for spaces)

description
 - A complete description of what the skill does and when to use it

The markdown content below contains the instructions, examples, and guidelines that Claude will follow. For more details, see How to create custom skills.

Partner Skills

Skills are a great way to teach Claude how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:

Notion - Notion Skills for Claude

About

 Public repository for Agent Skills
 

Topics

 agent-skills

Resources

 Readme

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

114k
 stars

Watchers

792
 watching

Forks

13k
 forks

 Report repository

Releases

No releases published

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

Python84.4%

HTML12.4%

Shell1.9%

JavaScript1.3%

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

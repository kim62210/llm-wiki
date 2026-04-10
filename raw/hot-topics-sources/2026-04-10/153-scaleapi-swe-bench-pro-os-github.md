---
title: GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub
source_url: https://github.com/scaleapi/SWE-bench_Pro-os
final_url: https://github.com/scaleapi/SWE-bench_Pro-os
status: 200
content_type: text/html; charset=utf-8
topics: [SWE-bench Pro]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:45.437934+00:00
---

# GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub

## 원본 URL

https://github.com/scaleapi/SWE-bench_Pro-os

## 추출 본문

GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub

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

 scaleapi
/SWE-bench_Pro-osPublic

Notifications
You must be signed in to change notification settings

Fork
 53

 Star
343

Code

Issues17

Pull requests2

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

scaleapi/SWE-bench_Pro-os

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
73 Commits

73 Commits

SWE-agent @ 402a7b8

SWE-agent @ 402a7b8

dockerfiles

dockerfiles

error_analysis

error_analysis

helper_code

helper_code

mini-swe-agent @ d74716a

mini-swe-agent @ d74716a

run_scripts

run_scripts

traj

traj

.gitignore

.gitignore

.gitmodules

.gitmodules

LICENSE

LICENSE

README.md

README.md

index.html

index.html

requirements.txt

requirements.txt

swe_bench_pro_eval.py

swe_bench_pro_eval.py

View all files

Repository files navigation

README

MIT license

SWE-Bench Pro

Code and data for the following works:

SWE-bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

HuggingFace: https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro

Public Leaderboard: https://scale.com/leaderboard/swe_bench_pro_public

Commercial (Private) Leaderboard: https://labs.scale.com/leaderboard/swe_bench_pro_private

News

(2/9) We have removed some unit tests which were outdated (e.g. required the year 2025) or were previously not intended to be included.

(1/7) We have fixed an issue with tutao instances where they take a long time to eval. The relevant run scripts are updated.

(10/28) We added mini-swe-agent! Results are comparable to SWE-Agent for Sonnet 4.5. Feel free to give it a shot. (credit @miguelrc-scale)

(10/28) We have the SWE-Agent scaffold to reproduce results and a step-by-step guide below. We have confirmed that this reproduces the Sonnet 4.5 results. (credit @18vijayb)

(10/3) We have updated results without cap limit here: https://scaleapi.github.io/SWE-bench_Pro-os/

Overview

SWE-Bench Pro is a challenging benchmark evaluating LLMs/Agents on long-horizon software engineering tasks.
Given a codebase and an issue, a language model is tasked with generating a patch that resolves the described problem.

The dataset is inspired from SWE-Bench: https://github.com/SWE-bench/SWE-bench

To access SWE-bench Pro, copy and run the following code:

fromdatasetsimportload_datasetswebench=load_dataset('ScaleAI/SWE-bench_Pro', split='test')

Installation

1. Install Python Dependencies

pip install -r requirements.txt

2. Install Docker

SWE-bench Pro uses Docker for reproducible evaluations.

Follow the instructions in the Docker setup guide to install Docker on your machine.
If you're setting up on Linux, we recommend seeing the post-installation steps as well.

3. Configure Modal (Recommended) (or use local docker [Beta])

modal setup # Follow the prompts to generate your token

After running, verify your credentials in 
~/.modal.toml
:

token_id = <token id>
token_secret = <token secret>
active = true

Beta: Local Docker. No additional setup needed. Use the 
--use_local_docker
 flag when running evaluations.

Docker Images

We provide prebuilt Docker images for each instance on Docker Hub:

Repository:https://hub.docker.com/r/jefzda/sweap-images

Finding the Correct Image

Each instance in the HuggingFace dataset has a 
dockerhub_tag
 column containing the Docker tag for that instance. You can access it directly:

fromdatasetsimportload_datasetdataset=load_dataset('ScaleAI/SWE-bench_Pro', split='test')

# Get the Docker image for a specific instanceforrowindataset:
 instance_id=row['instance_id']
 docker_tag=row['dockerhub_tag']
 full_image=f"jefzda/sweap-images:{docker_tag}"print(f"{instance_id} -> {full_image}")

Important: Bash runs by default in our images. When running these images, you should not manually invoke bash. See #6

Usage

1. Generate Patches

Generate patch predictions using your harness of choice.

For generating patches using SWE-agent, see the SWE-agent git submodule (note: you will have to use this as a git submodule. See official git documentation for details). The submodule contains detailed instructions to

Set up SWE-agent for patch generation

Run SWE-agent on SWE-Bench Pro instances

Configure model parameters and turn limits

The output will be 
.pred
 files containing model-generated patches for each instance.

2. Gather Patches

After generating patches, use the 
gather_patches.py
 helper script to collect all patches into a single JSON file for evaluation:

python helper_code/gather_patches.py \
 --directory <path_to_pred_files> \
 --prefix <model_name> \
 --output <output_file>.json

Parameters:

--directory
: Directory containing instance folders with 
.pred
 files (e.g., from SWE-agent output or downloaded trajectories)

--prefix
: Prefix identifier for your model/run (e.g., "gpt4", "claude-sonnet", "sample1")

--output
: Output JSON file path

Example:

python helper_code/gather_patches.py \
 --directory swe_bench_pro_results/sample1 \
 --prefix sample1 \
 --output sample1_patches.json

This will create a JSON file in the format expected by the evaluation script:

[
 {
 "instance_id": "instance_...",
 "patch": "diff --git ...",
 "prefix": "sample1"
 }
]

3. Evaluate Patches

Evaluate patch predictions on SWE-Bench Pro:

python swe_bench_pro_eval.py \
 --raw_sample_path=swe_bench_pro_full.csv \
 --patch_path=<your_patches>.json \
 --output_dir=<output_directory> \
 --scripts_dir=run_scripts \
 --num_workers=100 \
 --dockerhub_username=jefzda

You can test with the gold patches, which are in the HuggingFace dataset. There is a helper script in 
helper_code
 which can extract the gold patches into the required JSON format.

Reproducing Leaderboard Results

To reproduce leaderboard results end-to-end, follow the following steps:

Complete setup in the 
SWE-agent
 submodule. We recommend to use the Docker image to run the scaffold, via 
just
.

Run the scaffold. We have included an example for Claude Sonnet 4.5 (claude.yaml) but feel free to use any model. It also supports 
vllm
 for local models. Note that we recommend using the DockerHub images rather than building the Docker images from scratch. You can also execute it locally without Modal.

Compile predictions with helper_code/gather_patches.py.

Run the evaluation script 
swe_bench_pro_eval.py
 to run the evaluation script.

About

 SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
 

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

343
 stars

Watchers

5
 watching

Forks

53
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

Python58.6%

Dockerfile26.7%

Shell14.5%

HTML0.2%

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

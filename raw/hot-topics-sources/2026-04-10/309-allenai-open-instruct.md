---
title: GitHub - allenai/open-instruct: AllenAI's post-training codebase · GitHub
source_url: https://github.com/allenai/open-instruct
final_url: https://github.com/allenai/open-instruct
status: 200
content_type: text/html; charset=utf-8
topics: [Open Post-Training Recipes (Tülu 3 / OLMo 3)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:04.877409+00:00
---

# GitHub - allenai/open-instruct: AllenAI's post-training codebase · GitHub

## 원본 URL

https://github.com/allenai/open-instruct

## 추출 본문

GitHub - allenai/open-instruct: AllenAI's post-training codebase · GitHub

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

 allenai
/open-instructPublic

Notifications
You must be signed in to change notification settings

Fork
 531

 Star
3.7k

Code

Issues5

Pull requests25

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

allenai/open-instruct

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
1,364 Commits

1,364 Commits

.claude

.claude

.github

.github

assets

assets

configs

configs

decontamination

decontamination

docs

docs

human_eval

human_eval

open_instruct

open_instruct

scripts

scripts

tests

tests

.dockerignore

.dockerignore

.gitattributes

.gitattributes

.gitignore

.gitignore

.pre-commit-config.yaml

.pre-commit-config.yaml

AGENTS.md

AGENTS.md

CHANGELOG.md

CHANGELOG.md

CLAUDE.md

CLAUDE.md

CONTRIBUTING.md

CONTRIBUTING.md

Dockerfile

Dockerfile

LICENSE

LICENSE

Makefile

Makefile

README.md

README.md

conftest.py

conftest.py

mason.py

mason.py

mkdocs.yml

mkdocs.yml

pyproject.toml

pyproject.toml

requirements.txt

requirements.txt

test_mason.py

test_mason.py

test_rl_utils_gpu.py

test_rl_utils_gpu.py

uv.lock

uv.lock

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

Training Open Instruction-Following Language Models

This repo serves as an open effort on instruction-tuning and post-training popular pretrained language models on publicly available datasets. We release this repo and will keep updating it with:

Code for finetuning language models with latest techniques and instruction datasets in a unified format.

Code for DPO, preference finetuning and reinforcement learning with verifiable rewards (RLVR).

Checkpoints or other useful artifacts that we build in our exploration.

We also support some evaluations natively in the codebase, but these are now unmaintained and instead we suggest using OLMES, which we used for TÜLU 3.

The latest details on open post-training are found in TÜLU 3: Pushing Frontiers in Open Language Model Post-Training.

Please see our first paper How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources for more thoughts behind this project and our initial findings.
Please see our second paper Camels in a Changing Climate: Enhancing LM Adaptation with Tulu 2 for results using Llama-2 models and direct preference optimization. We are still working on more models.
For more recent results involving PPO and DPO please see our third paper Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback.

Try some of the models we train with Open Instruct. There is a free demo or download them from HuggingFace:
StageLlama 3.1 8BLlama 3.1 70BOLMo-2 7BOLMo-2 13BBase Modelmeta-llama/Llama-3.1-8Bmeta-llama/Llama-3.1-70Ballenai/OLMo2-7B-1124allenai/OLMo-2-13B-1124SFTallenai/Llama-3.1-Tulu-3-8B-SFTallenai/Llama-3.1-Tulu-3-70B-SFTallenai/OLMo-2-1124-7B-SFTallenai/OLMo-2-1124-13B-SFTDPOallenai/Llama-3.1-Tulu-3-8B-DPOallenai/Llama-3.1-Tulu-3-70B-DPOallenai/OLMo-2-1124-7B-DPOallenai/OLMo-2-1124-13B-DPOFinal Models (RLVR)allenai/Llama-3.1-Tulu-3-8Ballenai/Llama-3.1-Tulu-3-70Ballenai/OLMo-2-1124-7B-Instructallenai/OLMo-2-1124-13B-InstructReward Model (RM)allenai/Llama-3.1-Tulu-3-8B-RM(Same as 8B)allenai/OLMo-2-1124-7B-RM(Same as 7B)

News

[2024-11-22] We released TÜLU 3: Pushing Frontiers in Open Language Model Post-Training and updated our entire stack of open post-training recipes with both Llama 3.1 and OLMo 2.

[2024-07-01] We released Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback and have majorly updated our codebase to support new models and package versions.

[2023-11-27] We released Camels in a Changing Climate: Enhancing LM Adaptation with Tulu 2. Check out our models here. We have added a DPO finetuning script for replicating our results.

[2023-09-26] We switched to use the official alpaca-eval library to run AlpacaFarm evaluation but use regenerated longer reference outputs. This will change our numbers reported in the paper. We will update the paper soon.

[2023-09-25] Supported using vLLM for our evaluations, which speeds up the evaluation by 10x.

[2023-09-17] Supported LoRA and QLoRA finetuning. See here for more details.

[2023-08-18] Added support for ToxiGen/TruthfulQA evaluation. Check our 
scripts/eval/
 for examples of running them.

[2023-08-08] Supported several new instruction dataset, including LIMA / WizardLM / Open-Orca. See the preparation script for details. Performance hasn't been evaluated yet.

[2023-08-06] Supported LLaMa 2 finetuning and FlashAttention-2 by bumping the version of transformers and many other dependencies.

[2023-06-29] Added licensing info for our released models.

[2023-06-09] Released Tülu (a suite of LLaMa models fully-finetuned on a strong mix of datasets) and many other checkpoints on HuggingFace [Links].

[2023-06-09] Initial release of the codebase containing the training and evaluation code for our arxiv paper.

Setup

Our setup follows our Dockerfile. Note that Open Instruct is a research codebase and does not guarantee backward compatibility.

Installation with uv

We use uv for installation and running code. You can install with 
uv sync
.

Git LFS (for running tests): Install Git LFS and run 
git lfs install
 before cloning. See CONTRIBUTING.md for details.

Docker installation: You can also use the Dockerfile to build a Docker image. You can build the image with the following command:

docker build . \
 --build-arg GIT_COMMIT=$(git rev-parse --short HEAD) \
	--build-arg GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD) \
	-t open_instruct_dev

# if you are internally at AI2, you can create a beaker image like this:
beaker_user=$(beaker account whoami --format json | jq -r '.[0].name')
beaker image delete $beaker_user/open_instruct_dev
beaker image create open_instruct_dev -n open_instruct_dev -w ai2/$beaker_user

If you are internally at AI2, you may launch experiments using our always-up-to-date auto-built image 
nathanl/open_instruct_auto
.

Training

After having setup the environment, you are ready to launch some experiments. We provide a few examples below. To learn more about how to reproduce the Tulu 3 models, please refer to the Tulu 3 README. The instructions and documentations for Tulu 1 and Tulu 2 are in Tulu 1 and 2 README.

Finetuning

You can run the following command for getting started:

# train an 8B tulu3 model using 8 GPU
bash scripts/train/tulu3/finetune_8b.sh

OLMo-core SFT: For supported models (OLMo, OLMoE, Qwen3), we recommend the more GPU-efficient OLMo-core SFT implementation. See 
open_instruct/olmo_core_utils.py
 for the list of supported models.

Preference Tuning

# train an 8B tulu3 model using 8 GPU
bash scripts/train/tulu3/dpo_8b.sh

Reinforcement Learning with Verifiable Rewards (RLVR)

# quick debugging run using 1 GPU (0.5 for inference, 0.5 for training)# here we are using a small model, so it's prob not gonna train good models, but it's easy to test run and print stuff.
bash scripts/train/debug/single_gpu_on_beaker.sh

# train an 8B tulu3 model using 8 GPU (1 for inference, 7 for training)
bash scripts/train/rlvr/tulu_rlvr.sh

Contamination checks

We release our scripts for measuring the overlap between instruction tuning datasets and evaluation datasets in 
./decontamination
. See the README for more details.

Developing

When submitting a PR to this repo, we check the core code in 
open_instruct/
 for style with the following:

make style
make quality

Run the tests with 
uv run pytest
.

Pre-commit hooks

To automatically run linting and formatting on each commit:

uv add pre-commit --dev
uv run pre-commit install

To run on all files (recommended after initial setup):

uv run pre-commit run --all-files

Repo structure

├── assets/ <- Images, licenses, etc.
├── configs/
| ├── beaker_configs/ <- AI2 Beaker configs
| ├── ds_configs/ <- DeepSpeed configs
| └── train_configs/ <- Training configs
├── decontamination/ <- Scripts for measuring train-eval overlap
├── eval/ <- Evaluation suite for fine-tuned models
├── human_eval/ <- Human evaluation interface (not maintained)
├── open_instruct/ <- Source code (flat)
├── quantize/ <- Scripts for quantization
├── scripts/ <- Core training and evaluation scripts
└── Dockerfile <- Dockerfile

Licensing

This codebase is licensed under Apache 2.0 as given in LICENSE.

The license we use for V1 models released (along with the base model licenses) can be found in assets/model_licenses/tulu_license.txt - just replace 
<MODELNAME>
 with the actual model name (i.e., the name on HuggingFace).

V2 models are licensed under the low-risk AI2 ImpACT license. See here for more details.

Acknowledgements

Open Instruct is a project that benefited from many open-source projects and libraries. We would like to particularly thank the following projects:

HuggingFace Transformers: We adapted Hugging Face's Trainer for our finetuning scripts.

HuggingFace TRL and eric-mitchell/direct-preference-optimization: our preference tuning code is adapted from TRL and from Eric Mitchell's DPO code.

OpenAI's lm-human-preferences, summarize-from-feedback, and vwxyzjn/summarize_from_feedback_details: Our core PPO code is adapted from OpenAI's original RLHF code and Huang et al (2024)'s reproduction work of OpenAI's summarize from feedback work.

OpenRLHF: We adapted OpenRLHF's Ray + vLLM distributed code for scaling up PPO RLVR training into the 70B scale.

Citation

If you used this repository or our models, please cite our work:

Tulu 1:

@misc{wang2023far,
 title={How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources},
 author={Yizhong Wang and Hamish Ivison and Pradeep Dasigi and Jack Hessel and Tushar Khot and Khyathi Raghavi Chandu and David Wadden and Kelsey MacMillan and Noah A. Smith and Iz Beltagy and Hannaneh Hajishirzi},
 year={2023},
 eprint={2306.04751},
 archivePrefix={arXiv},
 primaryClass={cs.CL}
}

Tulu 2:

@misc{ivison2023camels,
 title={Camels in a Changing Climate: Enhancing LM Adaptation with Tulu 2},
 author={Hamish Ivison and Yizhong Wang and Valentina Pyatkin and Nathan Lambert and Matthew Peters and Pradeep Dasigi and Joel Jang and David Wadden and Noah A. Smith and Iz Beltagy and Hannaneh Hajishirzi},
 year={2023},
 eprint={2311.10702},
 archivePrefix={arXiv},
 primaryClass={cs.CL}
}

Tulu 2.5:

@misc{ivison2024unpacking,
 title={Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback},
 author={Hamish Ivison and Yizhong Wang and Jiacheng Liu and Zeqiu Wu and Valentina Pyatkin and Nathan Lambert and Noah A. Smith and Yejin Choi and Hannaneh Hajishirzi},
 year={2024},
 eprint={2406.09279},
 archivePrefix={arXiv},
 primaryClass={cs.CL},
}

Tulu 3:

@article{lambert2024tulu3,
 title = {Tülu 3: Pushing Frontiers in Open Language Model Post-Training},
 author = { Nathan Lambert and Jacob Morrison and Valentina Pyatkin and Shengyi Huang and Hamish Ivison and Faeze Brahman and Lester James V. Miranda and Alisa Liu and Nouha Dziri and Shane Lyu and Yuling Gu and Saumya Malik and Victoria Graf and Jena D. Hwang and Jiangjiang Yang and Ronan Le Bras and Oyvind Tafjord and Chris Wilhelm and Luca Soldaini and Noah A. Smith and Yizhong Wang and Pradeep Dasigi and Hannaneh Hajishirzi},
 year = {2024},
 email = {tulu@allenai.org}
}

OLMo 3:

@misc{olmo2025olmo3,
 title={OLMo 3},
 author={Team OLMo and Allyson Ettinger and Amanda Bertsch and Bailey Kuehl and David Graham and David Heineman and Dirk Groeneveld and Faeze Brahman and Finbarr Timbers and Hamish Ivison and Jacob Morrison and Jake Poznanski and Kyle Lo and Luca Soldaini and Matt Jordan and Mayee Chen and Michael Noukhovitch and Nathan Lambert and Pete Walsh and Pradeep Dasigi and Robert Berry and Saumya Malik and Saurabh Shah and Scott Geng and Shane Arora and Shashank Gupta and Taira Anderson and Teng Xiao and Tyler Murray and Tyler Romero and Victoria Graf and Akari Asai and Akshita Bhagia and Alexander Wettig and Alisa Liu and Aman Rangapur and Chloe Anastasiades and Costa Huang and Dustin Schwenk and Harsh Trivedi and Ian Magnusson and Jaron Lochner and Jiacheng Liu and Lester James V. Miranda and Maarten Sap and Malia Morgan and Michael Schmitz and Michal Guerquin and Michael Wilson and Regan Huff and Ronan Le Bras and Rui Xin and Rulin Shao and Sam Skjonsberg and Shannon Zejiang Shen and Shuyue Stella Li and Tucker Wilde and Valentina Pyatkin and Will Merrill and Yapei Chang and Yuling Gu and Zhiyuan Zeng and Ashish Sabharwal and Luke Zettlemoyer and Pang Wei Koh and Ali Farhadi and Noah A. Smith and Hannaneh Hajishirzi},
 year={2025},
 eprint={2512.13961},
 archivePrefix={arXiv},
 primaryClass={cs.CL},
 url={https://arxiv.org/abs/2512.13961},
}

About

 AllenAI's post-training codebase
 

allenai.github.io/open-instruct/

Resources

 Readme

License

 Apache-2.0 license
 

Contributing

 Contributing
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

3.7k
 stars

Watchers

26
 watching

Forks

531
 forks

 Report repository

Releases
 2

v0.2.0
 Latest

Mar 2, 2026

+ 1 release

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

Python86.0%

Shell12.6%

HTML0.8%

JavaScript0.3%

CSS0.2%

Dockerfile0.1%

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

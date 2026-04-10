---
title: GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub
source_url: https://github.com/NVIDIA/RULER
final_url: https://github.com/NVIDIA/RULER
status: 200
content_type: text/html; charset=utf-8
topics: [Context Rot & Effective Context Window]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:47.844890+00:00
---

# GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub

## 원본 URL

https://github.com/NVIDIA/RULER

## 추출 본문

GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub

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

 NVIDIA
/RULERPublic

Notifications
You must be signed in to change notification settings

Fork
 125

 Star
1.5k

Code

Issues16

Pull requests3

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

NVIDIA/RULER

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
101 Commits

101 Commits

docker

docker

scripts

scripts

.gitattributes

.gitattributes

.gitignore

.gitignore

LICENSE

LICENSE

README.md

README.md

View all files

Repository files navigation

README

Apache-2.0 license

📏 RULER: What’s the Real Context Size of Your Long-Context Language Models?

This repository contains code for our paper RULER: What’s the Real Context Size of Your Long-Context Language Models. RULER generates synthetic examples to evaluate long-context language models with configurable sequence length and task complexity. We benchmark 17 open-source models across 4 task categories (in total 13 tasks) in RULER, evaluating long-context capabilities beyond simple in-context recall. Here are our main results.
ModelsClaimed LengthEffective Length4K8K16K32K64K128KAvg.wAvg. (inc)wAvg. (dec)Llama2 (7B)4K85.6Jamba-1.5-large* (94B/398B)256k>128k96.796.696.496.095.495.196.095.7 (1st)96.3 (1st)Gemini-1.5-pro1M>128K96.795.896.095.995.994.495.895.5 (2nd)96.1 (2nd)Qwen2.5-14B-Instruct-1M* (14B)1M>128K97.597.194.694.994.992.295.7TBDTBDQwen3-235B-A22B* (235B)128K>128K97.797.296.495.193.390.695.0TBDTBDQwen3-14B* (14B)128K>128K98.097.896.496.194.085.194.6TBDTBDJamba-1.5-mini (12B/52B)256K>128K95.695.694.894.692.890.093.993.1 (3rd)94.8 (3rd)Qwen3-32B* (32B)128K>128K98.496.096.294.491.885.693.7TBDTBDEXAONE-4.0-32B* (32B)128K>128K96.394.993.993.691.788.293.1TBDTBDQwen2.5-7B-Instruct-1M* (7B)1M>128K96.895.393.091.190.484.491.8TBDTBDQwen3-30B-A3B* (30B)128K64K96.597.095.392.489.179.291.6TBDTBDGPT-4-1106-preview128K64K96.696.395.293.287.081.291.689.0 (4th)94.1 (4th)Llama3.1 (70B)128K64K96.595.895.494.888.466.689.685.5 (10th)93.7 (5th)Qwen3-8B* (8B)128K64K96.396.091.891.282.177.489.1TBDTBDMistral-Large-2411 (123B)128K64K96.496.395.394.085.948.186.079.5 (18th)92.5 (6th)Command-R-plus-0824 (104B)128K32K96.095.194.092.485.464.687.983.4 (13th)92.4 (7th)Qwen2 (72B)128K32K96.996.194.994.179.853.785.979.6 (17th)92.3 (8th)Command-R-plus (104B)128K32K95.695.294.292.084.363.187.482.7 (14th)92.1 (9th)Command-R-0824 (32B)128K64K94.793.793.190.886.674.788.986.0 (8th)91.9 (10th)GLM4 (9B)1M64K94.792.892.189.986.783.189.988.0 (5th)91.7 (11th)Llama3.1 (8B)128K32K95.593.891.687.484.777.088.385.4 (11th)91.3 (12th)ProLong (8B)512K32K94.592.592.389.383.281.688.986.6 (7th)91.2 (13th)Command-R (35B)128K32K93.893.392.489.584.976.088.385.5 (9th)91.1 (14th)MegaBeam-Mistral (7B)512K32K93.892.592.089.283.783.789.187.3 (6th)91.0 (15th)Mistral-Large-2407 (123B)128K32K96.296.195.193.078.823.780.570.6 (24th)90.4 (16th)GradientAI/Llama3 (70B)1M16K95.194.490.885.480.972.186.582.6 (15th)90.3 (17th)Mixtral-8x22B (39B/141B)64K32K95.694.993.490.984.731.781.973.5 (22nd)90.3 (18th)Yi (34B)200K32K93.392.291.387.583.277.387.584.8 (12th)90.1 (19th)Qwen3-4B* (4B)128K64K95.193.691.087.877.866.085.2TBDTBDEXAONE-4.0-1.2B* (1.2B)64K32K87.086.788.881.177.4-84.2TBDTBDPhi3-mini (3.8B)128K32K92.291.590.787.580.666.784.880.9 (16th)88.7 (20th)Phi3-medium (14B)128K32K93.393.291.186.878.646.181.574.8 (21st)88.3 (21st)Mixtral-8x7B (12.9B/46.7B)32K32K94.992.192.585.972.444.580.472.8 (23rd)87.9 (22nd)GradientAI/Llama3 (8B)1M16K92.890.385.779.976.369.582.478.5 (19th)86.3 (23rd)FILM-7B* (7B)32K32K92.888.288.186.970.127.175.566.4 (26th)84.7 (24th)InternLM2.5 (7B)1M4K88.185.584.582.775.568.980.977.8 (20th)83.9 (25th)Mistral (7B)32K16K93.691.287.275.449.013.868.455.6 (28th)81.2 (26th)Mistral-Nemo128K16K87.887.287.769.046.819.066.254.7 (29th)77.8 (27th)GLM3 (6B)128K4K87.883.478.669.956.042.069.662.0 (27th)77.2 (28th)LWM (7B)1M<4K82.378.473.769.168.165.072.869.9 (25th)75.7 (29th)DBRX (36B/132B)32K8K95.193.883.663.12.40.056.338.0 (30th)74.7 (30th)Qwen1.5 (72B)32K8K94.993.878.067.80.00.055.737.5 (31st)74.0 (31st)Together (7B)32K4K88.281.169.463.00.00.050.333.8 (32nd)66.7 (32nd)LongChat (7B)32K<4K84.779.970.859.30.00.049.133.1 (33rd)65.2 (33rd)LongAlpaca (13B)32K<4K60.657.056.643.60.00.036.324.7 (34th)47.9 (34th)
Despite achieving nearly perfect performance on the vanilla needle-in-a-haystack (NIAH) test, most models exhibit large degradation on tasks in RULER as sequence length increases.

While all models claim context size of 32k tokens or greater, only half of them can effectively handle sequence length of 32K by exceeding a qualitative threshold, Llama-2-7b performance at 4K (85.6%). The performance exceeding the threshold is underlined.

Almost all models fall below the threshold before reaching the claimed context lengths.

Notes

Jamba-1.5-large results are reported by authors from this report.

FILM-7B results are reported by authors of this paper. They use YaRN without further training for the evaluation length exceeding 32K (64K and 128K). They do not use the one-shot example for the CWE task.

Qwen2.5-1M results are reported by authors from this paper.

Qwen3 results are reported by authors from this paper.

EXAONE 4.0 results are reported by authors from this paper.

✅ Updates

Please follow rulerv1-ns branch to use our latest pipeline for RULERv1 evaluation.

Please follow rulerv2-ns branch to use our latest pipeline for RULERv2 evaluation.

💡 Requirements (deprecated)

Docker container: 
docker pull cphsieh/ruler:0.2.0

The requirements are listed in 
docker/Dockerfile
 and 
docker/requirements.txt
. Use the following command to build the container based on NVIDIA's PyTorch container 
nvcr.io/nvidia/pytorch:23.10-py3
.

cd docker/
DOCKER_BUILDKIT=1 docker build -f Dockerfile -t cphsieh/ruler:0.2.0 .

🔍 Evaluate long-context LMs (deprecated)

1. Download data

Paul Graham Essays for NIAH are downloaded from NIAH Github and Paul Graham Blog.

QA datasets are downloaded from SQuAD and HotpotQA.

cd scripts/data/synthetic/json/
python download_paulgraham_essay.py
bash download_qa_dataset.sh

2. Download model

We download the models from Huggingface.

The input template of each model is stored in 
scripts/data/template.py
. Please add new model template if your new model uses a different chat template.

Increase 
max_position_embeddings
 in 
config.json
 if you want to run inference longer than model defined length.

(Optional) If you are using TensorRT-LLM, please build your model engine based on their example scripts (e.g., Llama) with their Docker container.

3. Run evaluation pipeline

Setup 
run.sh

GPUS="" # number of GPUs
ROOT_DIR="" # the path that stores generated task samples and model predictions. 
MODEL_DIR="" # the path that contains individual model folders from Huggingface.
ENGINE_DIR="" # the path that contains individual engine folders from TensorRT-LLM.

Setup 
config_models.sh

case $MODEL_NAME in
 YOUR_HF_MODEL_NAME)
 MODEL_PATH=${MODEL_DIR}/YOUR_MODEL_FOLDER
 MODEL_TEMPLATE_TYPE="" # base, meta-chat, etc. defined in `scripts/data/template.py`
 MODEL_FRAMEWORK="" # hf or vllm
 ;;
 YOUR_TRTLLM_ENGINE_NAME)
 MODEL_PATH=${ENGINE_DIR}/YOUR_ENGINE_FOLDER
 MODEL_TEMPLATE_TYPE="" # base, meta-chat, etc. defined in `scripts/data/template.py`
 MODEL_FRAMEWORK="trtllm"
 ;;
 YOUR_OPENAI_MODEL_NAME)
 MODEL_PATH="" # OpenAI model name listed in https://platform.openai.com/docs/models/
 MODEL_TEMPLATE_TYPE="base"
 MODEL_FRAMEWORK="openai"
 TOKENIZER_PATH="cl100k_base"
 TOKENIZER_TYPE="openai"
 OPENAI_API_KEY="" # your OpenAI API key
 ;;
 YOUR_GEMINI_MODEL_NAME)
 MODEL_PATH="" # Gemini model name listed in https://ai.google.dev/gemini-api/docs/models/gemini
 MODEL_TEMPLATE_TYPE="base"
 MODEL_FRAMEWORK="gemini"
 TOKENIZER_PATH=$MODEL_PATH
 TOKENIZER_TYPE="gemini"
 GEMINI_API_KEY="" # your Gemini API key
 ;;

Start evaluation based on our default 
synthetic
 benchmark

bash run.sh YOUR_MODEL_NAME synthetic

🧠 (Optional) Customize task complexity

The tasks to be evaluated on are stored in 
scripts/config_tasks.sh
. Configuration of each task is defined in 
scripts/synthetic.yaml
. The complexity of each task can be configured by changing the arguments which we describe in detail below.
CategoryTask nameConfigurationsRetrievalniahtype_haystack: 
repeat/essay/needle

# repeat: repeated noise sentences
# essay: Paul Graham Essays
# needle: distracted needles

type_needle_k: 
words/numbers/uuids

type_needle_v: 
words/numbers/uuids

# words: adjective-noun
# numbers: 7 digits
# uuids: 32 digits

num_needle_k: 
int >= 1

# add multiple needles in haystack 
num_needle_v: 
int >= 1

 # retrieve multiple values from a single key
num_needle_q: 
int >= 1

 # retrieve multiple values from multiple keysMulti-hop
Tracingvariable_trackingnum_chains: 
int >= 1

# number of variable name-binding chains
num_hops: 
int >= 1

# number of times binding variable names in each chainAggregationcommon_words_extractionfreq_cw: 
int >= 1

# frequency of common words
freq_ucw: 
int >= 1

# frequency of uncommon words
num_cw: 
int >= 1

# number of common wordsAggregationfreq_words_extractionalpha: 
float > 1.0

# parameter of the distribution to draw synthetic words. Reducing alpha to increase the difficulty of this task. Note that increasing the number of words to return also increases the difficulty of this task, we use 
3
 in our evaluations as models show worse performance at short context size when more words need to be returned.Question
Answeringqadataset: 
squad
 or 
hotpotqa

# the short-context qa dataset we use

🚀 (Optional) Contribute a new synthetic task

1. Create a python script for data preparation

Add basic arguments (required) and complexity configurations in the python script.

Verify the script is reproducible given a tokenizer, a sequence length, and a random seed.

Save the script under the folder 
scripts/data/synthetic
.

2. Add task template

Add 
template
 and 
tokens_to_generate
 in 
scripts/data/synthetic/constants.py
.

Add 
answer_predfix
 to prevent model from refusing to answer.

3. Add evaluation metric

Add the automatic metric to evaluate your task in 
scripts/eval/synthetic/constants.py

4. Add required configurations

Define your task name and complexity configurations in 
scripts/synthetic.yaml
.

Add your task name in 
scripts/config_tasks.sh

🛠️ Limitations

While tasks in RULER are designed to be configurable, we only evaluate the above models with 13 task configurations. These tasks were selected because most models can achieve good (some almost perfect) performance at short context size (<= 4K), which leaves ample room to observe degradation as we extend the input length. We did not include more complexed tasks in RULER that models show worse performance at short context size. We also did not stress test every model with more difficult task configurations. Although RULER covers four task categories extending previous evaluation protocol and provides a clean test bed for sanity-checking LMs with known upper bound performance, it is by no means comprehensive enough and it cannot replace the more preferred realistic tasks. We welcome people to contribute new tasks and/or new task categories to help evaluate long-context capabilities.

📝 Citation

@article{hsieh2024ruler,
 title={RULER: What's the Real Context Size of Your Long-Context Language Models?},
 author={Cheng-Ping Hsieh and Simeng Sun and Samuel Kriman and Shantanu Acharya and Dima Rekesh and Fei Jia and Yang Zhang and Boris Ginsburg},
 year={2024},
 journal={arXiv preprint arXiv:2404.06654},
}

Disclaimer: This project is strictly for research purposes, and not an official product from NVIDIA.

About

 This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models?
 

Resources

 Readme

License

 Apache-2.0 license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

1.5k
 stars

Watchers

26
 watching

Forks

125
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

Python92.5%

Shell6.7%

Dockerfile0.8%

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

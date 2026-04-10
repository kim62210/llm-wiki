---
title: GitHub - BytedTsinghua-SIA/DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR · GitHub
source_url: https://github.com/BytedTsinghua-SIA/DAPO
final_url: https://github.com/BytedTsinghua-SIA/DAPO
status: 200
content_type: text/html; charset=utf-8
topics: [DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.589466+00:00
---

# GitHub - BytedTsinghua-SIA/DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR · GitHub

## 원본 URL

https://github.com/BytedTsinghua-SIA/DAPO

## 추출 본문

GitHub - BytedTsinghua-SIA/DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR · GitHub

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

 BytedTsinghua-SIA
/DAPOPublic

Notifications
You must be signed in to change notification settings

Fork
 84

 Star
1.8k

Code

Issues25

Pull requests0

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

BytedTsinghua-SIA/DAPO

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
23 Commits

23 Commits

eval

eval

img

img

README.md

README.md

dapo_paper.pdf

dapo_paper.pdf

requirements.txt

requirements.txt

View all files

Repository files navigation

README

DAPO: an Open-source RL System from 
ByteDance Seed and Tsinghua AIR

Important

🔥 News!!!

[2025/05] We update the wandb training record of full DAPO and the checkpoint which achieved 50%+ on AIME 2024. We also provide instructions for evaluation on AIME 2024.

[2025/03] We release the training record of an early version of DAPO (w/o Token-level PG Loss & Dynamic Sampling), achieving 44% on AIME 2024, in wandb.

We release a fully open-sourced system for large-scale LLM RL, including algorithm, code infrastructure, and dataset. The system achieves state-of-the-art large-scale LLM RL performance. We propose the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm.
Through open-sourcing, we provide the broader research community and society with practical access to scalable reinforcement learning, enabling all to benefit from these advancements. Our system is based on the awesome verl framework. Thanks for their great work!

Discussions Welcomed

🤗 If you have any questions about our paper, issues are welcomed and we could discuss there. Thank you!

Key Results

AIME 2024 Performance

🚀 DAPO achieves 50 points on AIME 2024 based on the Qwen2.5-32B base model, outperforming the previous SoTA DeepSeek-R1-Zero-Qwen-32B with 50% training steps.

Metric Supervision during Training

Length stability and growth: The steady increase in response length allows for greater exploration, facilitating the model’s ability to learn more complex reasoning behaviors, ultimately contributing to training stability and performance improvement.

Reward score stability: A stable increase in the reward signal indicates that the model is successfully fitting the training distribution, ensuring that the learning process remains robust and consistent without significant fluctuations.

Entropy and mean probability trend: A controlled increase in entropy, after an initial decrease, ensures a healthy balance between exploration and exploitation, avoiding issues such as overfitting or excessive randomness, and promoting sustained model performance.

Model Use

We provide the model weights of DAPO-Qwen-32B, which is trained based on Qwen2.5-32B using the DAPO algorithm.

Environment Setup

We recommend using conda to setup the environment:

conda create -n dapo python=3.10
conda activate dapo
pip3 install -r requirements.txt

Inference

We provide the model inference code here:

importtorchfromtransformersimportAutoTokenizerfromvllmimportSamplingParams, LLMexamples= [
 {
 "question": "Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.\n\nFind the largest possible real part of \\[(75+117i)z+\\frac{96+144i}{z}\\]where $z$ is a complex number with $|z|=4$.\n\nRemember to put your answer on its own line after \"Answer:\".",
 "answer": "540"
 },
 {
 "question": "Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.\n\nEvery morning Aya goes for a $9$-kilometer-long walk and stops at a coffee shop afterwards. When she walks at a constant speed of $s$ kilometers per hour, the walk takes her 4 hours, including $t$ minutes spent in the coffee shop. When she walks $s+2$ kilometers per hour, the walk takes her 2 hours and 24 minutes, including $t$ minutes spent in the coffee shop. Suppose Aya walks at $s+\\frac{1}{2}$ kilometers per hour. Find the number of minutes the walk takes her, including the $t$ minutes spent in the coffee shop.\n\nRemember to put your answer on its own line after \"Answer:\".",
 "answer": "204"
 },
 {
 "question": "Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.\n\nLet $\\mathcal{B}$ be the set of rectangular boxes with surface area $54$ and volume $23$. Let $r$ be the radius of the smallest sphere that can contain each of the rectangular boxes that are elements of $\\mathcal{B}$. The value of $r^2$ can be written as $\\frac{p}{q}$, where $p$ and $q$ are relatively prime positive integers. Find $p+q$.\n\nRemember to put your answer on its own line after \"Answer:\".",
 "answer": "721"
 }
]

defmain():
 model="BytedTsinghua-SIA/DAPO-Qwen-32B"tokenzier=AutoTokenizer.from_pretrained(model)

 llm=LLM(
 model=model,
 dtype=torch.bfloat16,
 tensor_parallel_size=8,
 gpu_memory_utilization=0.95
 )

 sampling_params=SamplingParams(
 temperature=1.0,
 top_p=0.7,
 max_tokens=20480
 )

 forexampleinexamples:
 question=example["question"]
 answer=example["answer"]
 output=llm.generate(
 prompts=tokenzier.apply_chat_template(conversation=[{"content": question, "role": "user"}],
 add_generation_prompt=True,
 tokenize=False),
 sampling_params=sampling_params
 )
 print(f"***QUESTION***:\n{question}\n***GROUND TRUTH***:\n{answer}\n***MODEL OUTPUT***:\n{output[0].outputs[0].text}\n")
 print("-"*100)

if__name__=="__main__":
 main()

Evaluation on AIME 2024

To evaluate the model on AIME 2024, we deploy DAPO-Qwen-32B with Ray Serve and vLLM.

To load the model from Huggingface:

serve run eval.llm:build_app model=BytedTsinghua-SIA/DAPO-Qwen-32B tensor-parallel-size=8

# open another terminal
python eval/eval_aime24.py --temperature 1.0 --top_p 0.7 --max_tokens 20480 --model BytedTsinghua-SIA/DAPO-Qwen-32B --test_file eval/aime-2024.parquet

To load the model from local path:

serve run eval.llm:build_app model=aaa/bbb/ccc tensor-parallel-size=8

# open another terminal
python eval/eval_aime24.py --temperature 1.0 --top_p 0.7 --max_tokens 20480 --model ccc --test_file eval/aime-2024.parquet

Reproducibility

To benefit the broader research community, we fully open-source the recipe of our RL training, including algorithm details, dataset, and infrastructures.

Datasets

We provide training and validation datasets for DAPO training.

Training: DAPO-Math-17k, a carefully curated and processed math dataset.
Validation: AIME 2024.

Training

We provide the out-of-the-box script for DAPO training reproduction. Quickstart and core code are mentioned in README. These are scripts for:

Datasets Preparation

DAPO w/o Token-level PG Loss & Dynamic Sampling -- AIME 44

DAPO Full -- AIME 50

Note:

The 
DAPO w/o Token-level PG Loss & Dynamic Sampling -- AIME 44
 script has been verified on the current verl and achieves 44 points on AIME 2024, whose training record can be accessed in wandb.

The 
DAPO Full -- AIME 50
 script has also been validated on the latest verl version. It scores 50 points on AIME 2024. You can view the corresponding training record on wandb.

Acknowledgement

We thank the verl for providing the awesome open-source RL infrastructure.

Our open-sourced experiments were conducted on the Volcano Engine Machine Learning Platform. We will provide a full reproduction guideline later on the Volcano Engine platform to help users replicate our experiments.

About

 An Open-source RL System from ByteDance Seed and Tsinghua AIR
 

Resources

 Readme

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

1.8k
 stars

Watchers

13
 watching

Forks

84
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

Python100.0%

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

---
title: GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub
source_url: https://github.com/SafeAILab/EAGLE
final_url: https://github.com/SafeAILab/EAGLE
status: 200
content_type: text/html; charset=utf-8
topics: [EAGLE-3 Speculative Decoding]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:35.596816+00:00
---

# GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub

## 원본 URL

https://github.com/SafeAILab/EAGLE

## 추출 본문

GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub

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

 SafeAILab
/EAGLEPublic

Notifications
You must be signed in to change notification settings

Fork
 268

 Star
2.3k

Code

Issues85

Pull requests11

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

SafeAILab/EAGLE

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
425 Commits

425 Commits

eagle

eagle

figs

figs

.gitignore

.gitignore

LICENSE

LICENSE

README.md

README.md

requirements-rocm.txt

requirements-rocm.txt

requirements.txt

requirements.txt

setup.py

setup.py

View all files

Repository files navigation

README

License

 EAGLE

| Paper (EAGLE) | 
Paper (EAGLE-2) |
Paper (EAGLE-3) |
Blog |

EAGLE (Extrapolation Algorithm for Greater Language-model Efficiency) is a new baseline for fast decoding of Large Language Models (LLMs) with provable performance maintenance. This approach involves extrapolating the second-top-layer contextual feature vectors of LLMs, enabling a significant boost in generation efficiency.

EAGLE is:

certified by the third-party evaluation as the fastest speculative method so far.

achieving 2x speedup on gpt-fast.

3x faster than vanilla decoding (13B).

2x faster than Lookahead (13B).

1.6x faster than Medusa (13B).

provably maintaining the consistency with vanilla decoding in the distribution of generated texts.

trainable (within 1-2 days) and testable on 8x RTX 3090 GPUs. So even the GPU poor can afford it.

combinable with other parallelled techniques such as vLLM, DeepSpeed, Mamba, FlashAttention, quantization, and hardware optimization.

EAGLE-2 uses the confidence scores from the draft model to approximate acceptance rates, dynamically adjusting the draft tree structure, which further enhances performance.

EAGLE-2 is:

4x faster than vanilla decoding (13B).

1.4x faster than EAGLE-1 (13B).

EAGLE-3 removes the feature prediction constraint in EAGLE and simulates this process during training using training-time testing. Considering that top-layer features are limited to next-token prediction, EAGLE-3 replaces them with a fusion of low-, mid-, and high-level semantic features.
EAGLE-3 further improves generation speed while ensuring lossless performance.

EAGLE-3 is:

5.6 faster than vanilla decoding (13B).

1.8x faster than EAGLE-1 (13B).

Inference is conducted on 2x RTX 3090 GPUs at fp16 precision using the Vicuna 13B model.

Support

EAGLE has been merged in the following mainstream LLM serving frameworks (listed in alphabetical order).

AMD ROCm

AngelSlim

AWS NeuronX Distributed Core

CPM.cu

Intel® Extension for Transformers

Intel® LLM Library for PyTorch

MLC-LLM

NVIDIA NeMo Framework

NVIDIA TensorRT-LLM

NVIDIA TensorRT Model Optimizer

PaddleNLP

SGLang

SpecForge

speculators

vLLM

Update

2025.9.18: EAGLE-3 is accepted to NeurIPS'25.

2025.7.23: We strongly recommend using SpecForge for out-of-the-box training of EAGLE-3 with SGLang.

2025.3.19: EAGLE-3 is released.

2024.8.8: We now support Qwen-2.

2024.6.27: EAGLE-2 is released.

2024.2.25: EAGLE is certified by the third-party evaluation as the fastest speculative method.

2024.1.17: We now support Mixtral-8x7B-Instruct.

2023.12.8: EAGLE v1.0 is released.

Todo

 Support non-greedy inference (provably maintaining text distribution).

 Support more LLMs such as Mixtral 8x7B.

 Support LLaMA-3.

 Support Qwen-2.

 Support vLLM (please check vLLM's implementation).

 EAGLE-3.

 Training code of EAGLE-3.

 Support LLaMA-4.

 Support official EAGLE-3 for Qwen-3.

 EAGLE-4.

The default main branch is the implementation of EAGLE-3 and EAGLE-2. For using EAGLE-1, please switch to the v1 branch.

Contents

Setup & Installation

EAGLE-3 Weights

EAGLE Weights

Inference
With UI

With Code

Train
Generate Train Data

Train the Auto-regression Head

Inference on custom models

Evaluation

Setup & Installation

git clone https://github.com/SafeAILab/EAGLE.git
cd EAGLE
python -m venv ~/venvs/ea_env
source~/venvs/ea_env/bin/activate
pip install -r requirements.txt

EAGLE-3 Weights

Note: This repository recognizes only official EAGLE-3 checkpoints. Performance of unofficial checkpoints may vary. If you want to compare with EAGLE-3, please compare with official checkpoints and official draft tree setups.

EAGLE-3 Models on Hugging Face

Base ModelEAGLE-3 Model(s)OfficialVicuna-13B v1.3
lmsys/vicuna-13b-v1.3yuhuili/EAGLE3-Vicuna1.3-13BYesLLaMA-3.1-8B-Instruct
meta-llama/Llama-3.1-8B-Instructyuhuili/EAGLE3-LLaMA3.1-Instruct-8BYesLLaMA-3.3-70B-Instruct
meta-llama/Llama-3.3-70B-Instructyuhuili/EAGLE3-LLaMA3.3-Instruct-70BYesDeepSeek-R1-Distill-LLaMA-8B
deepseek-ai/DeepSeek-R1-Distill-Llama-8Byuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8BYesLLaMA-4-Scout-17B-16E-Instruct
meta-llama/Llama-4-Scout-17B-16E-Instructlmsys/sglang-EAGLE3-Llama-4-Scout-17B-16E-Instruct-v1NoLLaMA-4-Maverick-17B-128E-Instruct
meta-llama/Llama-4-Maverick-17B-128E-Instructlmsys/sglang-EAGLE3-Llama-4-Maverick-17B-128E-Instruct-v1
nvidia/Llama-4-Maverick-17B-128E-Eagle3NoQwen3-1.7B
Qwen/Qwen3-1.7BAngelSlim/Qwen3-1.7B_eagle3NoQwen3-4B
Qwen/Qwen3-4BAngelSlim/Qwen3-4B_eagle3NoQwen3-8B
Qwen/Qwen3-8BTengyunw/qwen3_8b_eagle3
AngelSlim/Qwen3-8B_eagle3
Zjcxy-SmartAI/Eagle3-Qwen3-8B-zhNoQwen3-14B
Qwen/Qwen3-14BAngelSlim/Qwen3-14B_eagle3NoQwen3-30B-A3B
Qwen/Qwen3-30B-A3BTengyunw/qwen3_30b_moe_eagle3
AngelSlim/Qwen3-a3B_eagle3NoQwen3-32B
Qwen/Qwen3-32BAngelSlim/Qwen3-32B_eagle3
Zjcxy-SmartAI/Eagle3-Qwen3-32B-zhNoQwen3-235B-A22B
Qwen/Qwen3-235B-A22Bnvidia/Qwen3-235B-A22B-Eagle3
lmsys/Qwen3-235B-A22B-EAGLE3NoMiniCPM4-8B
openbmb/MiniCPM4-8Blinglingdan/Eagle3_for_MiniCPM4NoOLMoE-1B-7B-Instruct
allenai/OLMoE-1B-7B-0125-Instructwantsleep/OLMoE_1B_7B_Eagle3Nogranite-3.1-1b-a400m-instruct
ibm-granite/granite-3.1-1b-a400m-instructwantsleep/granite-3.1-1b-a400m-EAGLE3NoGPT-OSS-120B
openai/gpt-oss-120blmsys/EAGLE3-gpt-oss-120b-bf16
nvidia/gpt-oss-120b-Eagle3NoGLM-4.7-Flash
zai-org/GLM-4.7-Flashthoughtworks/GLM-4.7-Flash-Eagle3No

EAGLE Weights

Note: The current code defaults to using EAGLE-3. If you want to use EAGLE weights, please specify 
use_eagle3=False
 in 
EaModel.from_pretrained
.

Note: When Qwen2 is the target model, please use bf16 precision instead of fp16 to avoid numerical overflow. The training dataset for the draft model of Qwen2 is ShareGPT, which has removed non-English data. Therefore, if you want to use it on non-English data such as Chinese, please train with the corresponding data.

EAGLE Models on Hugging Face

Base ModelEAGLE Model# EAGLE ParametersOfficialVicuna-7B v1.3yuhuili/EAGLE-Vicuna-7B-v1.30.24BYesVicuna-13B v1.3yuhuili/EAGLE-Vicuna-13B-v1.30.37BYesVicuna-33B v1.3yuhuili/EAGLE-Vicuna-33B-v1.30.56BYesLLaMA2-Chat 7Byuhuili/EAGLE-llama2-chat-7B0.24BYesLLaMA2-Chat 13Byuhuili/EAGLE-llama2-chat-13B0.37BYesLLaMA2-Chat 70Byuhuili/EAGLE-llama2-chat-70B0.99BYesMixtral-8x7B-Instruct v0.1yuhuili/EAGLE-mixtral-instruct-8x7B0.28BYesLLaMA3-Instruct 8Byuhuili/EAGLE-LLaMA3-Instruct-8B0.25BYesLLaMA3-Instruct 70Byuhuili/EAGLE-LLaMA3-Instruct-70B0.99BYesQwen2-7B-Instructyuhuili/EAGLE-Qwen2-7B-Instruct0.26BYesQwen2-72B-Instructyuhuili/EAGLE-Qwen2-72B-Instruct1.05BYesLLaMA3.1-Instruct 8Byuhuili/EAGLE-LLaMA3.1-Instruct-8B0.25BYesQwen2.5-14B-InstructZjcxy-SmartAI/Eagle-Qwen2.5-14B-Instruct0.33BNo

Inference

The inference code we provide automatically allocates model weights (loading a model across multiple GPUs), allowing you to run models that exceed the memory of a single GPU.

With UI

We have provided a suggested web interface, which you can use by running the following command. After the model is fully loaded, a URL will be output in the terminal, which you can enter into your browser to access.

python -m eagle.application.webui --ea-model-path [path of EAGLE weight]\ 
 --base-model-path [path of the original model]\
 --model-type [vicuna\llama2\llama3]\
 --total-token [int]

The total-token is the number of draft tokens. For smaller models and advanced GPUs, this value can be set larger. Adjusting according to the specific device and model can achieve better results. If set to -1, EAGLE-2 will automatically configure this parameter.

With Code

You can use our provided "eagenerate" for speedup generation just like using 'generate' from Hugging Face. Here is an example.

fromeagle.model.ea_modelimportEaModelfromfastchat.modelimportget_conversation_templatemodel=EaModel.from_pretrained(
 base_model_path=base_model_path,
 ea_model_path=EAGLE_model_path,
 torch_dtype=torch.float16,
 low_cpu_mem_usage=True,
 device_map="auto",
 total_token=-1
)
model.eval()
your_message="Hello"conv=get_conversation_template("vicuna")
conv.append_message(conv.roles[0], your_message)
conv.append_message(conv.roles[1], None)
prompt=conv.get_prompt()
input_ids=model.tokenizer([prompt]).input_idsinput_ids=torch.as_tensor(input_ids).cuda()
output_ids=model.eagenerate(input_ids,temperature=0.5,max_new_tokens=512)
output=model.tokenizer.decode(output_ids[0])

Note: Vicuna, LLaMA2-Chat, and LLaMA3-Instruct are both chat models. You need to use the correct chat template, otherwise it will cause abnormal output from the model and affect the performance of EAGLE.

Train

cd eagle/traineagle3
deepspeed main.py --deepspeed_config ds_config.json

We strongly recommend using SpecForge for out-of-the-box training of EAGLE-3 with SGLang.

Inference on custom models

If the original LLM structure differs from LLaMA and Mixtral, you can utilize EAGLE as follows:

Copy the modeling_basemodelname.py from the Transformers library and proceed to make modifications to leverage the pre-allocated kv_cache for enhanced speed in the base model. You can refer to model/modeling_llama_kv.py for guidance, where places that require modifications are annotated with # [MODIFIED]. These modifications are minimal.

Evaluation

You can test the speed of EAGLE on MT-bench using the following command. The models will be downloaded automatically and you may need to input your Hugging Face Access Tokens by 
huggingface-cli login
.

python -m eagle.evaluation.gen_ea_answer_llama3chat --ea-model-path yuhuili/EAGLE3-LLaMA3.1-Instruct-8B --base-model-path meta-llama/Llama-3.1-8B-Instruct --use_eagle3

huggingface-cli login
.

python -m eagle.evaluation.gen_ea_answer_qwen3 --ea-model-path /workspace/yunhai/Qwen3-4B_eagle3 --base-model-path Qwen/Qwen3-4B --use_eagle3

If you need specific acceleration ratios, you will also need to run the following command to get the speed of vanilla auto-regression.

python -m eagle.evaluation.gen_baseline_answer_llama3chat --ea-model-path yuhuili/EAGLE3-LLaMA3.1-Instruct-8B --base-model-path meta-llama/Llama-3.1-8B-Instruct

The above two commands will each generate a .jsonl file that records the generation results and wall time. Then, you can use evaluation/speed.py to calculate the ratio of speeds.

🌟 Our Contributors

A heartfelt thank you to all our contributors.

Reference

For technical details and full experimental results, please check the paper of EAGLE, the paper of EAGLE-2, and the paper of EAGLE-3.

@inproceedings{li2024eagle, 
	author = {Yuhui Li and Fangyun Wei and Chao Zhang and Hongyang Zhang}, 
	title = {{EAGLE}: Speculative Sampling Requires Rethinking Feature Uncertainty}, 
	booktitle = {International Conference on Machine Learning},
	year = {2024}
}
@inproceedings{li2024eagle2, 
	author = {Yuhui Li and Fangyun Wei and Chao Zhang and Hongyang Zhang}, 
	title = {{EAGLE-2}: Faster Inference of Language Models with Dynamic Draft Trees}, 
	booktitle = {Empirical Methods in Natural Language Processing},
	year = {2024}
}
@inproceedings{li2025eagle3,
 author = {Yuhui Li and Fangyun Wei and Chao Zhang and Hongyang Zhang},
 title = {{EAGLE-3}: Scaling up Inference Acceleration of Large Language Models via Training-Time Test}, 
 booktitle = {Annual Conference on Neural Information Processing Systems},
 year = {2025}
}

Acknowledgements

This project has been influenced by many excellent projects in the LLM community, such as Medusa, FastChat, and others. The logo is designed by GPT-4. We also appreciate many valuable discussions with the SGLang team (James Liu, Ke Bao, Yineng Zhang, Lianmin Zheng, Ying Sheng and many others), Tianle Cai, Hao Zhang, Ziteng Sun, and others.

About

 Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25).
 

arxiv.org/pdf/2503.01840

Topics

 large-language-models

 llm-inference

 speculative-decoding

Resources

 Readme

License

 View license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

2.3k
 stars

Watchers

31
 watching

Forks

268
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

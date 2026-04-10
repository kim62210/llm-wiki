---
title: zai-org/GLM-5 · Hugging Face
source_url: https://huggingface.co/zai-org/GLM-5
final_url: https://huggingface.co/zai-org/GLM-5
status: 200
content_type: text/html; charset=utf-8
topics: [GLM-5.1]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:44.624765+00:00
---

# zai-org/GLM-5 · Hugging Face

## 원본 URL

https://huggingface.co/zai-org/GLM-5

## 추출 본문

zai-org/GLM-5 · Hugging Face

Hugging Face

 Models 

 Datasets 

 Spaces 

 Buckets new

 Docs 

 Enterprise 

Pricing

Log In

Sign Up

zai-org
/

GLM-5

like1.97k

Follow
Z.ai11.9k

Text Generation

Transformers

Safetensors

English

Chinese

glm_moe_dsa

conversational

Eval Results

arxiv:2602.15763

License:mit

Model cardFilesFiles and versions
xet
Community
73

 Deploy

 Use this model

GLM-5
Introduction

Benchmark
Footnote

Serve GLM-5 Locally
Prepare environment

Deploy

Citation

 GLM-5
	

 👋 Join our WeChat or Discord community.
 

 📖 Check out the GLM-5 technical blog.
 

 📍 Use GLM-5 API services on Z.ai API Platform. 

 👉 One click to GLM-5.

 [Paper] 
 [GitHub]

 Introduction
	

We are launching GLM-5, targeting complex systems engineering and long-horizon agentic tasks. Scaling is still one of the most important ways to improve the intelligence efficiency of Artificial General Intelligence (AGI). Compared to GLM-4.5, GLM-5 scales from 355B parameters (32B active) to 744B parameters (40B active), and increases pre-training data from 23T to 28.5T tokens. GLM-5 also integrates DeepSeek Sparse Attention (DSA), largely reducing deployment cost while preserving long-context capacity.

Reinforcement learning aims to bridge the gap between competence and excellence in pre-trained models. However, deploying it at scale for LLMs is a challenge due to the RL training inefficiency. To this end, we developed slime, a novel asynchronous RL infrastructure that substantially improves training throughput and efficiency, enabling more fine-grained post-training iterations. With advances in both pre-training and post-training, GLM-5 delivers significant improvement compared to GLM-4.7 across a wide range of academic benchmarks and achieves best-in-class performance among all open-source models in the world on reasoning, coding, and agentic tasks, closing the gap with frontier models.

 Benchmark
	

GLM-5GLM-4.7DeepSeek-V3.2Kimi K2.5Claude Opus 4.5Gemini 3 ProGPT-5.2 (xhigh)HLE30.524.825.131.528.437.235.4HLE (w/ Tools)50.442.840.851.843.4*45.8*45.5*AIME 2026 I92.792.992.792.593.390.6-HMMT Nov. 202596.993.590.291.191.793.097.1IMOAnswerBench82.582.078.381.878.583.386.3GPQA-Diamond86.085.782.487.687.091.992.4SWE-bench Verified77.873.873.176.880.976.280.0SWE-bench Multilingual73.366.770.273.077.565.072.0Terminal-Bench 2.0 (Terminus 2)56.2 / 60.7 †41.039.350.859.354.254.0Terminal-Bench 2.0 (Claude Code)56.2 / 61.1 †32.846.4-57.9--CyberGym43.223.517.341.350.639.9-BrowseComp62.052.051.460.637.037.8-BrowseComp (w/ Context Manage)75.967.567.674.967.859.265.8BrowseComp-Zh72.766.665.062.362.466.876.1τ²-Bench89.787.485.380.291.690.785.5MCP-Atlas (Public Set)67.852.062.263.865.266.668.0Tool-Decathlon38.023.835.227.843.536.446.3Vending Bench 2$4,432.12$2,376.82$1,034.00$1,198.46$4,967.06$5,478.16$3,591.33

*: refers to their scores of full set.

†: A verified version of Terminal-Bench 2.0 that fixes some ambiguous instructions.
See footnote for more evaluation details.

 Footnote
	

Humanity’s Last Exam (HLE) & other reasoning tasks: We evaluate with a maximum generation length of 131,072 tokens (
temperature=1.0, top_p=0.95, max_new_tokens=131072
). By default, we report the text-only subset; results marked with * are from the full set. We use GPT-5.2 (medium) as the judge model. For HLE-with-tools, we use a maximum context length of 202,752 tokens.

SWE-bench & SWE-bench Multilingual: We run the SWE-bench suite with OpenHands using a tailored instruction prompt. Settings: 
temperature=0.7, top_p=0.95, max_new_tokens=16384
, with a 200K context window.

BrowserComp: Without context management, we retain details from the most recent 5 turns. With context management, we use the same discard-all strategy as DeepSeek-v3.2 and Kimi K2.5.

Terminal-Bench 2.0 (Terminus 2): We evaluate with the Terminus framework using 
timeout=2h, temperature=0.7, top_p=1.0, max_new_tokens=8192
, with a 128K context window. Resource limits are capped at 16 CPUs and 32 GB RAM.

Terminal-Bench 2.0 (Claude Code): We evaluate in Claude Code 2.1.14 (think mode, default effort) with 
temperature=1.0, top_p=0.95, max_new_tokens=65536
. We remove wall-clock time limits due to generation speed, while preserving per-task CPU and memory constraints. Scores are averaged over 5 runs. We fix environment issues introduced by Claude Code and also report results on a verified Terminal-Bench 2.0 dataset that resolves ambiguous instructions (see: https://huggingface.co/datasets/zai-org/terminal-bench-2-verified).

CyberGym: We evaluate in Claude Code 2.1.18 (think mode, no web tools) with (
temperature=1.0, top_p=1.0, max_new_tokens=32000
) and a 250-minute timeout per task. Results are single-run Pass@1 over 1,507 tasks.

MCP-Atlas: All models are evaluated in think mode on the 500-task public subset with a 10-minute timeout per task. We use Gemini 3 Pro as the judge model.

τ²-bench: We add a small prompt adjustment in Retail and Telecom to avoid failures caused by premature user termination. For Airline, we apply the domain fixes proposed in the Claude Opus 4.5 system card.

Vending Bench 2: Runs are conducted independently by Andon Labs.

 Serve GLM-5 Locally
	

 Prepare environment
	

The following open-source frameworks support local deployment of GLM-5:

vLLM (v0.19.0+)

SGLang (v0.5.10+)

KTransformers (v0.5.3+)

Transformers (v0.5.4+)

xLLM (v0.8.0+)

 Deploy
	

vLLM

vllm serve zai-org/GLM-5 \
 --tensor-parallel-size 8 \
 --gpu-memory-utilization 0.85 \
 --speculative-config.method mtp \
 --speculative-config.num_speculative_tokens 3 \
 --tool-call-parser glm47 \
 --reasoning-parser glm45 \
 --enable-auto-tool-choice \
 --served-model-name glm-5

 Check the recipes for more details.

SGLang

sglang serve \
 --model-path zai-org/GLM-5 \
 --tp-size 8 \
 --tool-call-parser glm47 \
 --reasoning-parser glm45 \
 --speculative-algorithm EAGLE \
 --speculative-num-steps 3 \
 --speculative-eagle-topk 1 \
 --speculative-num-draft-tokens 4 \
 --mem-fraction-static 0.85 \
 --served-model-name glm-5

 Check the sglang cookbook for more details.

xLLM and other Ascend NPU

 Please check the deployment guide here.

KTransformers

 Please check the deployment guide here.

 Citation
	

If you find GLM-5 useful in your research, please cite our technical report:

@misc{glm5team2026glm5vibecodingagentic,
 title={GLM-5: from Vibe Coding to Agentic Engineering},
 author={GLM-5-Team and : and Aohan Zeng and Xin Lv and Zhenyu Hou and Zhengxiao Du and Qinkai Zheng and Bin Chen and Da Yin and Chendi Ge and Chenghua Huang and Chengxing Xie and Chenzheng Zhu and Congfeng Yin and Cunxiang Wang and Gengzheng Pan and Hao Zeng and Haoke Zhang and Haoran Wang and Huilong Chen and Jiajie Zhang and Jian Jiao and Jiaqi Guo and Jingsen Wang and Jingzhao Du and Jinzhu Wu and Kedong Wang and Lei Li and Lin Fan and Lucen Zhong and Mingdao Liu and Mingming Zhao and Pengfan Du and Qian Dong and Rui Lu and Shuang-Li and Shulin Cao and Song Liu and Ting Jiang and Xiaodong Chen and Xiaohan Zhang and Xuancheng Huang and Xuezhen Dong and Yabo Xu and Yao Wei and Yifan An and Yilin Niu and Yitong Zhu and Yuanhao Wen and Yukuo Cen and Yushi Bai and Zhongpei Qiao and Zihan Wang and Zikang Wang and Zilin Zhu and Ziqiang Liu and Zixuan Li and Bojie Wang and Bosi Wen and Can Huang and Changpeng Cai and Chao Yu and Chen Li and Chengwei Hu and Chenhui Zhang and Dan Zhang and Daoyan Lin and Dayong Yang and Di Wang and Ding Ai and Erle Zhu and Fangzhou Yi and Feiyu Chen and Guohong Wen and Hailong Sun and Haisha Zhao and Haiyi Hu and Hanchen Zhang and Hanrui Liu and Hanyu Zhang and Hao Peng and Hao Tai and Haobo Zhang and He Liu and Hongwei Wang and Hongxi Yan and Hongyu Ge and Huan Liu and Huanpeng Chu and Jia'ni Zhao and Jiachen Wang and Jiajing Zhao and Jiamin Ren and Jiapeng Wang and Jiaxin Zhang and Jiayi Gui and Jiayue Zhao and Jijie Li and Jing An and Jing Li and Jingwei Yuan and Jinhua Du and Jinxin Liu and Junkai Zhi and Junwen Duan and Kaiyue Zhou and Kangjian Wei and Ke Wang and Keyun Luo and Laiqiang Zhang and Leigang Sha and Liang Xu and Lindong Wu and Lintao Ding and Lu Chen and Minghao Li and Nianyi Lin and Pan Ta and Qiang Zou and Rongjun Song and Ruiqi Yang and Shangqing Tu and Shangtong Yang and Shaoxiang Wu and Shengyan Zhang and Shijie Li and Shuang Li and Shuyi Fan and Wei Qin and Wei Tian and Weining Zhang and Wenbo Yu and Wenjie Liang and Xiang Kuang and Xiangmeng Cheng and Xiangyang Li and Xiaoquan Yan and Xiaowei Hu and Xiaoying Ling and Xing Fan and Xingye Xia and Xinyuan Zhang and Xinze Zhang and Xirui Pan and Xu Zou and Xunkai Zhang and Yadi Liu and Yandong Wu and Yanfu Li and Yidong Wang and Yifan Zhu and Yijun Tan and Yilin Zhou and Yiming Pan and Ying Zhang and Yinpei Su and Yipeng Geng and Yong Yan and Yonglin Tan and Yuean Bi and Yuhan Shen and Yuhao Yang and Yujiang Li and Yunan Liu and Yunqing Wang and Yuntao Li and Yurong Wu and Yutao Zhang and Yuxi Duan and Yuxuan Zhang and Zezhen Liu and Zhengtao Jiang and Zhenhe Yan and Zheyu Zhang and Zhixiang Wei and Zhuo Chen and Zhuoer Feng and Zijun Yao and Ziwei Chai and Ziyuan Wang and Zuzhou Zhang and Bin Xu and Minlie Huang and Hongning Wang and Juanzi Li and Yuxiao Dong and Jie Tang},
 year={2026},
 eprint={2602.15763},
 archivePrefix={arXiv},
 primaryClass={cs.LG},
 url={https://arxiv.org/abs/2602.15763},
}

Downloads last month379,276

Safetensors

Model size

754B params

Tensor type

BF16 
·
F32 
·

Chat template

Files info

Inference ProvidersNEW

Novita

+1

Text Generation

Examples

Input a message to start chatting with zai-org/GLM-5.

Send

View Code Snippets

 Compare providers

 Model tree for zai-org/GLM-5

Adapters

10 models

Finetunes

36 models

Merges

1 model

Quantizations

24 models

 Spaces using zai-org/GLM-5100

🏆

akhaliq/anycoder

💥

pliny-the-prompter/obliteratus

🚀

FINAL-Bench/all-bench-leaderboard

🚀

FINAL-Bench/Leaderboard

🚀

GenAISecurityProject/OWASP-AIBOM-Generator

🤖

smolagents/ml-agent

🏆🏆🏆

arudradey/all-bench-leaderboard

🏆

ZENLLC/anycoder

🌌

hfmlsoc/different-flops

💬

ai-coscientist/ablation-bench

📉

akhaliq/inferenceprovidersrankings

📈

Djebbi/zai-org-GLM-5
+ 95 Spaces+ 88 Spaces

 Collection including zai-org/GLM-5

GLM-5

 Collection

2 items•Updated Feb 11• 35

 Paper for zai-org/GLM-5

GLM-5: from Vibe Coding to Agentic Engineering

 Paper • 2602.15763 •Published Feb 17• 136

 Evaluation results 

MathArena Aime 2026on MathArena/aime_2026View evaluation resultssourceleaderboard 

95.83

MathArena Hmmt Feb 2026on MathArena/hmmt_feb_2026View evaluation resultssourceleaderboard 

86.36

Diamondon Idavidrein/gpqaView evaluation resultsleaderboard 

86

Hleon cais/hleView evaluation results

30.5

Hleon cais/hleView evaluation results

50.4 *

Swe Bench Resolvedon SWE-bench/SWE-bench_VerifiedView evaluation results

sourceleaderboard 

72.8 *

Swe Bench Resolvedon SWE-bench/SWE-bench_VerifiedView evaluation resultsleaderboard 

77.8 *

Terminal Benchon harborframework/terminal-bench-2.0View evaluation results

sourceleaderboard 

52.4 *

Terminalbench 2on harborframework/terminal-bench-2.0View evaluation results

sourceleaderboard 

52.4 *

Mediumon collinear-ai/yc-benchView evaluation resultssourceleaderboard 

1,208,190 *

 System theme

Company
TOSPrivacyAboutCareers
Website
ModelsDatasetsSpacesPricingDocs

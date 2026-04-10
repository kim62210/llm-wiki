---
title: zai-org/GLM-5.1 · Hugging Face
source_url: https://huggingface.co/zai-org/GLM-5.1
final_url: https://huggingface.co/zai-org/GLM-5.1
status: 200
content_type: text/html; charset=utf-8
topics: [GLM-5.1]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:44.023187+00:00
---

# zai-org/GLM-5.1 · Hugging Face

## 원본 URL

https://huggingface.co/zai-org/GLM-5.1

## 추출 본문

zai-org/GLM-5.1 · Hugging Face

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

GLM-5.1

like850

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
16

 Deploy

 Use this model

GLM-5.1
Introduction

Benchmark

Serve GLM-5.1 Locally

Citation

 GLM-5.1
	

 👋 Join our WeChat or Discord community.
 

 📖 Check out the GLM-5.1 blog and GLM-5 Technical report.
 

 📍 Use GLM-5.1 API services on Z.ai API Platform. 

 🔜 GLM-5.1 will be available on chat.z.ai in the coming days.

 [Paper] 
 [GitHub]

 Introduction
	

GLM-5.1 is our next-generation flagship model for agentic engineering, with significantly stronger coding capabilities than its predecessor. It achieves state-of-the-art performance on SWE-Bench Pro and leads GLM-5 by a wide margin on NL2Repo (repo generation) and Terminal-Bench 2.0 (real-world terminal tasks).

But the most meaningful leap goes beyond first-pass performance. Previous models—including GLM-5—tend to exhaust their repertoire early: they apply familiar techniques for quick initial gains, then plateau. Giving them more time doesn't help.

GLM-5.1, by contrast, is built to stay effective on agentic tasks over much longer horizons. We've found that the model handles ambiguous problems with better judgment and stays productive over longer sessions. It breaks complex problems down, runs experiments, reads results, and identifies blockers with real precision. By revisiting its reasoning and revising its strategy through repeated iteration, GLM-5.1 sustains optimization over hundreds of rounds and thousands of tool calls. The longer it runs, the better the result.

 Benchmark
	

GLM-5.1GLM-5Qwen3.6-PlusMinimax M2.7DeepSeek-V3.2Kimi K2.5Claude Opus 4.6Gemini 3.1 ProGPT-5.4HLE31.030.528.828.025.131.536.745.039.8HLE (w/ Tools)52.350.450.6-40.851.853.1*51.4*52.1*AIME 202695.395.495.189.895.194.595.698.298.7HMMT Nov. 202594.096.994.681.090.291.196.394.895.8HMMT Feb. 202682.682.887.872.779.981.384.387.391.8IMOAnswerBench83.882.583.866.378.381.875.381.091.4GPQA-Diamond86.286.090.487.082.487.691.394.392.0SWE-Bench Pro58.455.156.656.2-53.857.354.257.7NL2Repo42.735.937.939.8-32.049.833.441.3Terminal-Bench 2.0 (Terminus-2)63.556.261.6-39.350.865.468.5-Terminal-Bench 2.0 (Best self-reported)69.0 (Claude Code)56.2 (Claude Code)-57.0 (Claude Code)46.4 (Claude Code)---75.1 (Codex)CyberGym68.748.3--17.341.366.6--BrowseComp68.062.0--51.460.6---BrowseComp (w/ Context Manage)79.375.9--67.674.984.085.982.7τ³-Bench70.669.270.767.669.266.072.467.172.9MCP-Atlas (Public Set)71.869.274.148.862.263.873.869.267.2Tool-Decathlon40.738.039.846.335.227.847.248.854.6Vending Bench 2$5,634.41$4,432.12$5,114.87-$1,034.00$1,198.46$8,017.59$911.21$6,144.18

 Serve GLM-5.1 Locally
	

The following open-source frameworks support local deployment of GLM-5.1:

SGLang (v0.5.10+) — see cookbook

vLLM (v0.19.0+) — see recipes

xLLM (v0.8.0+) — see example

Transformers (v0.5.3+) — see transformers docs

KTransformers (v0.5.3+) — see tutorial

 Citation
	

If you find GLM-5.1 or GLM-5 useful in your research, please cite our technical report:

@misc{glm5team2026glm5vibecodingagentic,
 title={GLM-5: from Vibe Coding to Agentic Engineering},
 author={GLM-5-Team and : and Aohan Zeng and Xin Lv and Zhenyu Hou and Zhengxiao Du and Qinkai Zheng and Bin Chen and Da Yin and Chendi Ge and Chenghua Huang and Chengxing Xie and Chenzheng Zhu and Congfeng Yin and Cunxiang Wang and Gengzheng Pan and Hao Zeng and Haoke Zhang and Haoran Wang and Huilong Chen and Jiajie Zhang and Jian Jiao and Jiaqi Guo and Jingsen Wang and Jingzhao Du and Jinzhu Wu and Kedong Wang and Lei Li and Lin Fan and Lucen Zhong and Mingdao Liu and Mingming Zhao and Pengfan Du and Qian Dong and Rui Lu and Shuang-Li and Shulin Cao and Song Liu and Ting Jiang and Xiaodong Chen and Xiaohan Zhang and Xuancheng Huang and Xuezhen Dong and Yabo Xu and Yao Wei and Yifan An and Yilin Niu and Yitong Zhu and Yuanhao Wen and Yukuo Cen and Yushi Bai and Zhongpei Qiao and Zihan Wang and Zikang Wang and Zilin Zhu and Ziqiang Liu and Zixuan Li and Bojie Wang and Bosi Wen and Can Huang and Changpeng Cai and Chao Yu and Chen Li and Chengwei Hu and Chenhui Zhang and Dan Zhang and Daoyan Lin and Dayong Yang and Di Wang and Ding Ai and Erle Zhu and Fangzhou Yi and Feiyu Chen and Guohong Wen and Hailong Sun and Haisha Zhao and Haiyi Hu and Hanchen Zhang and Hanrui Liu and Hanyu Zhang and Hao Peng and Hao Tai and Haobo Zhang and He Liu and Hongwei Wang and Hongxi Yan and Hongyu Ge and Huan Liu and Huanpeng Chu and Jia'ni Zhao and Jiachen Wang and Jiajing Zhao and Jiamin Ren and Jiapeng Wang and Jiaxin Zhang and Jiayi Gui and Jiayue Zhao and Jijie Li and Jing An and Jing Li and Jingwei Yuan and Jinhua Du and Jinxin Liu and Junkai Zhi and Junwen Duan and Kaiyue Zhou and Kangjian Wei and Ke Wang and Keyun Luo and Laiqiang Zhang and Leigang Sha and Liang Xu and Lindong Wu and Lintao Ding and Lu Chen and Minghao Li and Nianyi Lin and Pan Ta and Qiang Zou and Rongjun Song and Ruiqi Yang and Shangqing Tu and Shangtong Yang and Shaoxiang Wu and Shengyan Zhang and Shijie Li and Shuang Li and Shuyi Fan and Wei Qin and Wei Tian and Weining Zhang and Wenbo Yu and Wenjie Liang and Xiang Kuang and Xiangmeng Cheng and Xiangyang Li and Xiaoquan Yan and Xiaowei Hu and Xiaoying Ling and Xing Fan and Xingye Xia and Xinyuan Zhang and Xinze Zhang and Xirui Pan and Xu Zou and Xunkai Zhang and Yadi Liu and Yandong Wu and Yanfu Li and Yidong Wang and Yifan Zhu and Yijun Tan and Yilin Zhou and Yiming Pan and Ying Zhang and Yinpei Su and Yipeng Geng and Yong Yan and Yonglin Tan and Yuean Bi and Yuhan Shen and Yuhao Yang and Yujiang Li and Yunan Liu and Yunqing Wang and Yuntao Li and Yurong Wu and Yutao Zhang and Yuxi Duan and Yuxuan Zhang and Zezhen Liu and Zhengtao Jiang and Zhenhe Yan and Zheyu Zhang and Zhixiang Wei and Zhuo Chen and Zhuoer Feng and Zijun Yao and Ziwei Chai and Ziyuan Wang and Zuzhou Zhang and Bin Xu and Minlie Huang and Hongning Wang and Juanzi Li and Yuxiao Dong and Jie Tang},
 year={2026},
 eprint={2602.15763},
 archivePrefix={arXiv},
 primaryClass={cs.LG},
 url={https://arxiv.org/abs/2602.15763},
}

Downloads last month8,465

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

Input a message to start chatting with zai-org/GLM-5.1.

Send

View Code Snippets

 Compare providers

 Model tree for zai-org/GLM-5.1

Quantizations

18 models

 Spaces using zai-org/GLM-5.113

🔥

ghetto9912/zai-org-GLM-5.1

🚀

Your-Mate/openenv-productivity

🦞

ScoootScooob/clawbench

🐢

Blackx2/zai-org-GLM-5.1

🌖

lujin/zai-org-GLM-5.1

📄

ehsaaniqbal/invoiceops-env

🏢

shmilylyp/zai-org-GLM-5.1

🦀

Stoeaves/zai-org-GLM-5.1

🏆

sabbir23m/zai-org-GLM-5.1

🐢

syt94210/zai-org-GLM-5.1

🧪

elmorshedyahmed/glm-5-1-lab

👁

Hossamkadasi1/zai-org-GLM-5.1
+ 8 Spaces+ 1 Spaces

 Collection including zai-org/GLM-5.1

GLM-5.1

 Collection

2 items•Updated 2 days ago• 41

 Paper for zai-org/GLM-5.1

GLM-5: from Vibe Coding to Agentic Engineering

 Paper • 2602.15763 •Published Feb 17• 136

 Evaluation results 

MathArena Aime 2026on MathArena/aime_2026View evaluation resultsleaderboard 

95.3

MathArena Hmmt Feb 2026on MathArena/hmmt_feb_2026View evaluation resultsleaderboard 

82.6

Diamondon Idavidrein/gpqaView evaluation resultsleaderboard 

86.2

Hleon cais/hleView evaluation results

31

Hleon cais/hleView evaluation results

52.3 *

SWE Bench Proon ScaleAI/SWE-bench_ProView evaluation resultsleaderboard 

58.4 *

Terminalbench 2on harborframework/terminal-bench-2.0View evaluation resultsleaderboard 

63.5

Terminalbench 2on harborframework/terminal-bench-2.0View evaluation resultsleaderboard 

69 *

 System theme

Company
TOSPrivacyAboutCareers
Website
ModelsDatasetsSpacesPricingDocs

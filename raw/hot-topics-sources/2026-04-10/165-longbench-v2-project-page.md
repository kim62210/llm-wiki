---
title: LongBench v2
source_url: https://longbench2.github.io
final_url: https://longbench2.github.io
status: 200
content_type: text/html; charset=utf-8
topics: [Context Rot & Effective Context Window]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:47.447548+00:00
---

# LongBench v2

## 원본 URL

https://longbench2.github.io

## 추출 본문

LongBench v2 

🔥

 More Research
 
LongBenchLongAlignLongWriterLongCite

LongBench v2

 Benchmarking Deeper Understanding and Reasoning on Realistic Long-context Multitasks
 

LongBench Team

arXivCode
📊
Dataset
🏆
Leaderboard

Introduction

 LongBench v2 is designed to assess the ability of LLMs to handle long-context problems requiring deep understanding and reasoning across real-world multitasks. 
 LongBench v2 has the following features: 
 (1) Length: Context length ranging from 8k to 2M words, with the majority under 128k.
 (2) Difficulty: Challenging enough that even human experts, using search tools within the document, cannot answer correctly in a short time.
 (3) Coverage: Cover various realistic scenarios.
 (4) Reliability: All in a multiple-choice question format for reliable evaluation.
 To elaborate, LongBench v2 consists of 503 challenging multiple-choice questions, with contexts ranging from 8k to 2M words, across six major task categories: single-document QA, multi-document QA, long in-context learning, long-dialogue history understanding, code repo understanding, and long structured data understanding.
 To ensure the breadth and the practicality, we collect data from nearly 100 highly educated individuals with diverse professional backgrounds. We employ both automated and manual review processes to maintain high quality and difficulty, resulting in human experts achieving only 53.7% accuracy under a 15-minute time constraint.
 Our evaluation reveals that the best-performing model, when directly answers the questions, achieves only 50.1% accuracy. In contrast, the o1-preview model, which includes longer reasoning, achieves 57.7%, surpassing the human baseline by 4%.
 

 🔍 With LongBench v2, we are eager to find out how scaling inference-time compute will affect deep understanding and reasoning in long-context scenarios.

Leaderboard

📢 The leaderboard is constantly updating as we are welcoming new submissions!
 

We consider two test settings: w/o CoT and w/ CoT.
 

Short: 0 ~ 32k words         
 Medium: 32k ~ 128k words         
 Long: 128k ~ 2M words
 

 By default, this leaderboard is sorted by the overall accuracy w/ CoT, as reasoning models (indicated by 🧠) natively use CoT to answer questions. The CoT results for non-reasoning models are obtained using our prompt that enforces the model to first generate the CoT and then the final answer. To view other sorted results, please click on the corresponding cell.
 

#ModelParamsContextDateOverall (%)Easy (%)Hard (%)Short (%)Medium (%)Long (%)w/ CoTw/ CoTw/ CoTw/ CoTw/ CoTw/ CoTGemini-2.5-Pro🧠
Google
- 1M
2025-03-25
-63.3-75.0-56.1-67.2-56.3-71.0Gemini-2.5-Flash🧠
Google
- 1M
2025-04-17
-62.1-72.3-55.8-68.3-60.0-55.7Qwen3-235B-A22B-Thinking-2507🧠
Alibaba
235B 256k 
2025-07-25
-60.6-70.5-54.4-62.8-59.9-58.1DeepSeek-R1🧠
DeepSeek
671B 128k
2025-01-20
-58.3-66.1-53.4-62.2-54.4-59.3Qwen3-235B-A22B-Instruct-2507
Alibaba
235B 256k 
2025-07-22
46.758.351.666.743.753.152.263.344.255.342.655.6o1-preview🧠
OpenAI
- 128k 2024-09-12-57.7-66.8-52.1-62.6-53.5-58.1DeepSeek-R1-0528🧠
DeepSeek
671B 128k
2025-05-28
-56.7-59.4-55.0-66.7-50.9-51.4MiniMax-Text-01
MiniMax
456B 4M 
2025-01-15
52.956.560.966.147.950.558.961.752.656.743.547.2Gemini-2.0-Flash-Thinking🧠
Google
- 1M
2025-01-21
-56.0-62.8-51.9-61.1-55.2-49.1Human
 N/AN/AN/A53.753.710010025.125.147.247.259.159.153.753.7Gemini-Exp-1206
Google
- 2M 
2024-12-06
49.352.552.961.547.147.153.955.647.149.545.853.3GPT-4o
OpenAI
- 128k 
2024-11-20
46.051.450.854.243.049.747.559.647.948.639.843.5GPT-4o
OpenAI
- 128k 2024-08-0650.151.257.457.945.647.153.353.952.450.740.247.7Gemini-2.0-Flash
Google
- 1M 
2024-12-11
47.451.151.058.345.246.648.957.247.745.344.452.3GLM-4.5🧠
Z.ai & Tsinghua
355B 128k 
2025-07-28
-50.3-57.8-45.7-57.8-44.2-50.0Qwen3-30B-A3B-Thinking-2507🧠
Alibaba
30B 256k 
2025-07-25
-50.1-58.9-44.7-56.7-46.0-47.2Qwen3-235B-A22B🧠
Alibaba
235B 128k 
2025-04-29
40.450.147.456.436.046.245.658.336.744.138.948.6Qwen3-32B🧠
Alibaba
32B 128k 
2025-04-29
38.849.242.253.136.746.840.660.038.141.137.047.2QwQ-32B🧠
Alibaba
32B 128k 
2025-03-06
-48.9-58.9-42.8-54.4-44.7-48.1GLM-4.5-Air🧠
Z.ai & Tsinghua
106B 128k 
2025-07-28
-48.6-54.7-44.8-58.9-41.9-44.9Claude 3.5 Sonnet
 
Anthropic
- 200k 2024-10-2241.046.746.955.237.341.546.153.938.641.937.044.4GLM-4-Plus
 
Z.ai & Tsinghua
- 128k 2024-10-1144.346.147.452.142.442.450.053.346.544.730.637.0Kimi-K2-Instruct
 
Moonshot AI
1T 128k 
2025-07-11
44.944.350.049.541.841.251.752.239.138.145.443.5Qwen2.5-72B
 
Alibaba
72B 128k 2024-09-1942.143.542.747.941.840.845.648.938.140.944.439.8Qwen3-30B-A3B🧠
Alibaba
30B 128k 
2025-04-29
32.642.534.447.831.539.335.052.032.136.029.639.8Mistral Large 24.11
 
Mistral AI
123B 128k 2024-11-2434.439.638.043.832.237.041.746.130.734.929.638.0o1-mini
 
OpenAI
- 128k 2024-09-1237.838.938.942.637.136.648.648.933.332.928.634.3Llama 3.1 70B
 
Meta
70B 128k 2024-07-2331.636.232.335.931.236.341.145.027.434.024.125.9Llama 3.3 70B
 
Meta
70B 128k 2024-12-0629.836.234.438.027.035.036.745.027.033.024.127.8Qwen2.5-7B
 
Alibaba
7B 128k 2024-09-1930.035.630.738.029.634.140.643.924.232.624.127.8Nemotron 70B
 
Nvidia
70B 128k 2024-10-1531.035.232.837.029.934.138.346.727.929.825.026.9Mistral Large 2
 
Mistral AI
123B 128k 2024-07-2426.633.629.734.424.833.137.841.119.531.222.225.9GPT-4o mini
 
OpenAI
- 128k 2024-07-1829.332.431.132.628.232.231.834.828.631.626.229.9NExtLong 8B
CAS
8B 512k 
2025-01-23
30.832.033.936.528.929.337.837.227.431.225.925.0Command R+
 
Cohere
104B 128k 2024-08-3027.831.630.234.426.429.936.739.423.724.221.333.3GLM-4-9B
 
Z.ai & Tsinghua
9B 128k 2024-06-0530.230.830.734.429.928.633.935.029.830.225.025.0Llama 3.1 8B
 
Meta
8B 128k 2024-07-2330.030.430.736.529.626.735.034.427.931.625.921.3Random
 N/AN/AN/A25.025.025.025.025.025.025.025.025.025.025.025.0
Green date indicates the newly added/updated models         
 - indicates closed-source models
 

 1*. Human accuracy is based on their performance within a 15-minute time limit, after which they are allowed to respond with "I don’t know the answer". This occurred for 8% of the total test data.
 2*. Humans achieve 100% accuracy on the 'Easy' subset because it only include questions that humans answer correctly within 10 mins.
 3*. Models do not show lower scores on subsets with longer length ranges because the distribution of tasks differs significantly across each length range.
 4*. The reported results of Qwen models are evaluated using YaRN with a scaling factor of 4.
 5*. Qwen3 models support hybrid thinking. For the w/o CoT results, we evaluate them in non-thinking mode, and for the w/ CoT results, we use thinking mode with a 16K token thinking budget.
 

Last Update: 2025-05-06

Benchmark

Data Collection

Data collection pipeline of LongBench v2. The annotator first uploads the document(s) and proposes a multiple-choice question based on the content. After that, automated and manual reviews will be conducted to ensure the data meets our requirements. Only data that passes these reviews is eligible for annotation rewards, meaning the annotator must revise the data until it passes all review stages.
 

Benchmark Statistics

 
 (Left) Length distribution of each task category; 
(Right) Human expert solving time distribution.

Tasks and data statistics in LongBench v2. 'Length' is the median of the number of words. 'Expert Acc' and 'Expert Time' refer to the average accuracy and the median time spent on answering the question by human experts.
 

Experiment Results

Average scores across tasks, normalized by the highest score on each task.

Long-context LLM + RAG performance across different context lengths, varied by including the top 4, 8, 16, 32, 64, 128, and 256 chunks of 512 tokens.

Citation

 @article{bai2024longbench2,
 title={LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks}, 
 author={Yushi Bai and Shangqing Tu and Jiajie Zhang and Hao Peng and Xiaozhi Wang and Xin Lv and Shulin Cao and Jiazheng Xu and Lei Hou and Yuxiao Dong and Jie Tang and Juanzi Li},
 journal={arXiv preprint arXiv:2412.15204},
 year={2024}
 }

 This website is adapted from MathVista and VideoMME, licensed under a Creative
 Commons Attribution-ShareAlike 4.0 International License.

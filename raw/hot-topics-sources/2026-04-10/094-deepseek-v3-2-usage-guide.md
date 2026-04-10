---
title: DeepSeek-V3.2 Usage Guide - vLLM Recipes
source_url: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html
final_url: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html
status: 200
content_type: text/html; charset=utf-8
topics: [DeepSeek Sparse Attention (DSA) for Long Context]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:38.574891+00:00
---

# DeepSeek-V3.2 Usage Guide - vLLM Recipes

## 원본 URL

https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html

## 추출 본문

DeepSeek-V3.2 Usage Guide - vLLM Recipes

 Skip to content
 

 vLLM Recipes
 

 
 DeepSeek-V3.2 Usage Guide
 
 

 Initializing search
 

 GitHub
 

 vLLM Recipes
 

 GitHub
 

 
 
 vLLM Recipes
 

 
 

 
 
 DeepSeek
 

 
 
 
 
 DeepSeek
 

 

 
 
 DeepSeek-OCR Usage Guide
 

 
 

 
 
 DeepSeek-OCR Usage Guide
 

 
 

 
 
 DeepSeek-V3 (R1) Usage Guide
 

 
 

 
 
 DeepSeek-V3.1 Usage Guide
 

 
 

 
 
 DeepSeek-V3.2 Usage Guide
 

 
 
 
 
 DeepSeek-V3.2 Usage Guide
 

 
 
 Table of contents
 

 
 Introduction
 
 

 
 Installing DeepGEMM
 
 

 
 Installing vLLM
 
 

 
 Launching DeepSeek-V3.2
 
 

 
 Performance tuning on Hopper/Blackwell GPUs
 
 

 
 Accuracy Benchmarking
 
 

 
 GSM8K
 
 

 
 AIME25
 
 

 
 Benchmarking
 
 

 
 TP8 Benchmark Output
 
 

 
 EP/DP Mode
 
 

 
 Usage tips
 
 

 
 Tool Calling Example
 
 

 
 vLLM Server Print
 
 

 
 DeepSeek Offical API Print
 
 

 
 
 DeepSeek-V3.2-Exp Usage Guide
 

 
 

 
 
 Ernie
 

 
 
 
 
 Ernie
 

 

 
 
 Ernie4.5 Text Model Usage Guide
 

 
 

 
 
 Ernie4.5 VL Model Usage Guide
 

 
 

 
 
 GLM
 

 
 
 
 
 GLM
 

 

 
 
 GLM-4.X LLM Usage Guide
 

 
 

 
 
 GLM-5 and GLM-5.1 Series Usage
 

 
 

 
 
 GLM-ASR Usage Guide
 

 
 

 
 
 GLM-Image Usage Guide
 

 
 

 
 
 GLM-OCR Usage Guide
 

 
 

 
 
 GLM-4V Usage Guide
 

 
 

 
 
 Glyph Usage Guide
 

 
 

 
 
 Google
 

 
 
 
 
 Google
 

 

 
 
 Gemma 4 Usage Guide
 

 
 

 
 
 TranslateGemma Usage Guide
 

 
 

 
 
 InternLM
 

 
 
 
 
 InternLM
 

 

 
 
 Intern-S1 Usage Guide
 

 
 

 
 
 InternVL
 

 
 
 
 
 InternVL
 

 

 
 
 InternVL3.5 Usage Guide
 

 
 

 
 
 inclusionAI
 

 
 
 
 
 inclusionAI
 

 

 
 
 Ring-1T-FP8 Usage Guide
 

 
 

 
 
 Jina
 

 
 
 
 
 Jina
 

 

 
 
 Jina Reranker vLLM Deployment Recipe
 

 
 

 
 
 Llama
 

 
 
 
 
 Llama
 

 

 
 
 Quick Start Recipe for Llama 3.1 on vLLM
 

 
 

 
 
 Quick Start Recipe for Llama 3.3 70B on vLLM - NVIDIA Blackwell & Hopper Hardware
 

 
 

 
 
 Quick Start Recipe for Llama 4 Scout on vLLM - NVIDIA Blackwell & Hopper Hardware
 

 
 

 
 
 Meituan
 

 
 
 
 
 Meituan
 

 

 
 
 Longcat Usage Guide
 

 
 

 
 
 Microsoft
 

 
 
 
 
 Microsoft
 

 

 
 
 Phi-4 Usage Guide
 

 
 

 
 
 MiMo
 

 
 
 
 
 MiMo
 

 

 
 
 MiMo-V2-Flash Usage Guide
 

 
 

 
 
 MiniMax
 

 
 
 
 
 MiniMax
 

 

 
 
 MiniMax-M2 Series Usage Guide
 

 
 

 
 
 MiniMax-M2.5 Usage Guide
 

 
 

 
 
 Mistral
 

 
 
 
 
 Mistral
 

 

 
 
 Ministral-3 Instruct Usage Guide
 

 
 

 
 
 Ministral-3 Reasoning Usage Guide
 

 
 

 
 
 Mistral-Large-3 Instruct Usage Guide
 

 
 

 
 
 Moonshotai
 

 
 
 
 
 Moonshotai
 

 

 
 
 moonshotai/Kimi-K2 Usage Guide
 

 
 

 
 
 Kimi-K2-Thinking Usage Guide
 

 
 

 
 
 moonshotai/Kimi-K2.5 Usage Guide
 

 
 

 
 
 Kimi-Linear Usage Guide
 

 
 

 
 
 NVIDIA
 

 
 
 
 
 NVIDIA
 

 

 
 
 NVIDIA Nemotron-3-Nano-30B-A3B User Guide
 

 
 

 
 
 NVIDIA Nemotron-Nano-12B-v2-VL User Guide
 

 
 

 
 
 OpenAI
 

 
 
 
 
 OpenAI
 

 

 
 
 GPT OSS
 

 
 

 
 
 PaddlePaddle
 

 
 
 
 
 PaddlePaddle
 

 

 
 
 PaddleOCR-VL Usage Guide
 

 
 

 
 
 Qwen
 

 
 
 
 
 Qwen
 

 

 
 
 Qwen2.5-VL Usage Guide
 

 
 

 
 
 Qwen3 Usage Guide
 

 
 

 
 
 Qwen3-ASR Usage Guide
 

 
 

 
 
 Qwen3-Coder Usage Guide
 

 
 

 
 
 Qwen3-Next Usage Guide
 

 
 

 
 
 Qwen3-VL Usage Guide
 

 
 

 
 
 Qwen3.5 Usage Guide
 

 
 

 
 
 Qwen3Guard-Gen Usage Guide
 

 
 

 
 
 Qwen-Image Usage Guide
 

 
 

 
 
 Seed
 

 
 
 
 
 Seed
 

 

 
 
 Seed-OSS-36B Usage Guide
 

 
 

 
 
 StabilityAI
 

 
 
 
 
 StabilityAI
 

 

 
 
 Stable Audio Open Usage Guide
 

 
 

 
 
 Stable Diffusion 3.5 Usage Guide
 

 
 

 
 
 StepFun
 

 
 
 
 
 StepFun
 

 

 
 
 Step-3.5-Flash Guide
 

 
 

 
 
 Tencent Hunyuan
 

 
 
 
 
 Tencent Hunyuan
 

 

 
 
 HunyuanOCR Usage Guide
 

 
 

 
 
 Wan AI
 

 
 
 
 
 Wan AI
 

 

 
 
 Wan2.2 Usage Guide
 

 
 

 Table of contents
 

 
 Introduction
 
 

 
 Installing DeepGEMM
 
 

 
 Installing vLLM
 
 

 
 Launching DeepSeek-V3.2
 
 

 
 Performance tuning on Hopper/Blackwell GPUs
 
 

 
 Accuracy Benchmarking
 
 

 
 GSM8K
 
 

 
 AIME25
 
 

 
 Benchmarking
 
 

 
 TP8 Benchmark Output
 
 

 
 EP/DP Mode
 
 

 
 Usage tips
 
 

 
 Tool Calling Example
 
 

 
 vLLM Server Print
 
 

 
 DeepSeek Offical API Print
 
 

DeepSeek-V3.2 Usage Guide¶

Introduction¶

DeepSeek-V3.2 is a model that balances computational efficiency with strong reasoning and agent capabilities through three technical innovations:
- DeepSeek Sparse Attention (DSA): An efficient attention mechanism that reduces computational complexity while maintaining performance, optimized for long-context scenarios.
- Scalable Reinforcement Learning Framework: The model achieves GPT-5-level performance through robust RL protocols and scaled post-training compute. The high-compute variant, DeepSeek-V3.2-Speciale, surpasses GPT-5 and matches Gemini-3.0-Pro in reasoning, achieving gold-medal level performance in the 2025 IMO and IOI competitions.
- Large-Scale Agentic Task Synthesis Pipeline: A novel data synthesis pipeline that generates training data at scale, integrating reasoning into tool-use scenarios and improving model compliance and generalization in complex interactive environments.

Installing DeepGEMM¶

uvpipinstallgit+https://github.com/deepseek-ai/[email protected]--no-build-isolation

Note: DeepGEMM is used in two places: MoE and MQA logits computation. It is necessary for MQA logits computation. If you want to disable the MoE part, you can set 
VLLM_USE_DEEP_GEMM=0
 in the environment variable. Some users reported that the performance is better with 
VLLM_USE_DEEP_GEMM=0
, e.g. on H20 GPUs. It might be also beneficial to disable DeepGEMM if you want to skip the long warmup.

Installing vLLM¶

uvvenv
source.venv/bin/activate
uvpipinstallvllm--extra-index-urlhttps://wheels.vllm.ai/nightly

Launching DeepSeek-V3.2¶

The chat-template changes in the DeepSeek-V3.2 are quite significant. vLLM adapts to this through 
--tokenizer-mode deepseek_v32
.

vllmservedeepseek-ai/DeepSeek-V3.2\--tensor-parallel-size8\--tokenizer-modedeepseek_v32\--tool-call-parserdeepseek_v32\--enable-auto-tool-choice\--reasoning-parserdeepseek_v3

Performance tuning on Hopper/Blackwell GPUs¶

On Hopper (H100/H200) or Blackwell (B200/B300), avoid using 
-tp=8
 for DeepSeek-V3.2 with FlashMLA-Sparse. Due to current kernel restrictions (see flashmla_sparse.py), TP=8 yields only 16 heads (128/8) per rank but is padded to 64 heads, incurring overhead and hurting performance.

Prefer TP=1~2 + DP/EP so each rank keeps 64/128 heads without padding:
- Hopper: TP=2
- Blackwell: TP=1

Accuracy Benchmarking¶

GSM8K¶

Script

lm_eval--modellocal-completions--model_args"model=deepseek-ai/DeepSeek-V3.2,base_url=http://0.0.0.0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend=None,num_concurrent=32"--tasksgsm8k--num_fewshot5

Result

local-completions(model=deepseek-ai/DeepSeek-V3.2,base_url=http://0.0.0.0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend=None,num_concurrent=32),gen_kwargs:(None),limit:None,num_fewshot:5,batch_size:1|Tasks|Version|Filter|n-shot|Metric||Value||Stderr||-----|------:|----------------|-----:|-----------|---|-----:|---|-----:||gsm8k|3|flexible-extract|5|exact_match|↑|0.9560|±|0.0056||||strict-match|5|exact_match|↑|0.9553|±|0.0057|

AIME25¶

Script

lm_eval--modellocal-chat-completions--model_args"model=deepseek-ai/DeepSeek-V3.2,base_url=http://0.0.0.0:8000/v1/chat/completions,tokenized_requests=False,tokenizer_backend=None,num_concurrent=20,timeout=5000,max_length=72768"--tasksaime25--apply_chat_template--gen_kwargs'{"temperature":1.0,"max_gen_toks":72768,"top_p":0.95,"chat_template_kwargs":{"thinking":true}}'--log_samples--output_path"aime25_ds32"

Result

local-chat-completions(model=deepseek-ai/DeepSeek-V3.2,base_url=http://0.0.0.0:8000/v1/chat/completions,tokenized_requests=False,tokenizer_backend=None,num_concurrent=20,timeout=5000,max_length=72768),gen_kwargs:({'temperature':1.0,'max_gen_toks':72768,'top_p':0.95,'chat_template_kwargs':{'thinking':True}}),limit:None,num_fewshot:None,batch_size:1|Tasks|Version|Filter|n-shot|Metric||Value||Stderr||------|------:|------|-----:|-----------|---|-----:|---|-----:||aime25|0|none|0|exact_match|↑|0.9333|±|0.0463|

Benchmarking¶

We used the following script to benchmark 
deepseek-ai/DeepSeek-V3.2
 on 8xH20.

vllmbenchserve\--modeldeepseek-ai/DeepSeek-V3.2\--dataset-namerandom\--random-input2048\--random-output1024\--request-rate10\--num-prompt100\ --trust-remote-code

TP8 Benchmark Output¶

============ServingBenchmarkResult============Successfulrequests:100Failedrequests:0Requestrateconfigured(RPS):10.00Benchmarkduration(s):129.34Totalinputtokens:204800Totalgeneratedtokens:102400Requestthroughput(req/s):0.77Outputtokenthroughput(tok/s):791.73Peakoutputtokenthroughput(tok/s):1300.00Peakconcurrentrequests:100.00TotalTokenthroughput(tok/s):2375.18---------------TimetoFirstToken----------------
MeanTTFT(ms):21147.20MedianTTFT(ms):21197.97P99TTFT(ms):41133.00-----TimeperOutputToken(excl.1sttoken)------
MeanTPOT(ms):99.71MedianTPOT(ms):99.25P99TPOT(ms):124.28---------------Inter-tokenLatency----------------
MeanITL(ms):99.71MedianITL(ms):76.89P99ITL(ms):2032.37==================================================

EP/DP Mode¶

This is the recommended serving mode as the kernels are mainly optimized for TP=1. The command uses:
- 
-dp 8
: Data parallelism across 8 GPUs
- 
-ep
: Expert parallelism for MoE layers

vllmservedeepseek-ai/DeepSeek-V3.2-dp8--enable-expert-parallel

EP/DP mode sometimes delivers better performance than TP mode on some hardware.

Usage tips¶

You can refer to DeepSeek-V3_2-Exp recipe and Data Parallel Deployment documentation to conduct related experiments and benchmark testing to select the parallel group suitable for your scenario.

Regarding 
thinking mode
 and 
non-thinking mode
, you can refer to DeepSeek-V3_1recipe.

Tool Calling Example¶

DeepSeek 3.2's thinking mode now supports tool calling, see: DeepSeek API Doc. The model can perform multiple rounds of reasoning and tool calls before outputting the final answer. The code example below is directly copied from the DeepSeek official examples. For vLLM, the main modifications are:

To enable thinking mode in vLLM, use extra_body = {"chat_template_kwargs": {"thinking": True}}. In the DeepSeek official API, the method to enable thinking mode is extra_body = {"thinking": {"type": "enabled"}}.

For the 
think
 field, vLLM recommends using reasoning, the DeepSeek official API uses reasoning_content. 

In vLLM, if there are no tool_calls, then tool_calls is an empty list (
[]
), In contrast, the DeepSeek official API returns 
None
.

importosimportjsonfromopenaiimportOpenAI# The definition of the toolstools=[{"type":"function","function":{"name":"get_date","description":"Get the current date","parameters":{"type":"object","properties":{}},}},{"type":"function","function":{"name":"get_weather","description":"Get weather of a location, the user should supply the location and date.","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city name"},"date":{"type":"string","description":"The date in format YYYY-mm-dd"},},"required":["location","date"]},}},]# The mocked version of the tool callsdefget_date_mock():return"2025-12-01"defget_weather_mock(location,date):return"Cloudy 7~13°C"TOOL_CALL_MAP={"get_date":get_date_mock,"get_weather":get_weather_mock}defclear_reasoning_content(messages):formessageinmessages:# DeepSeek official API# if hasattr(message, 'reasoning_content'):# message.reasoning_content = None# vLLM Serverifhasattr(message,'reasoning'):message.reasoning=Nonedefrun_turn(turn,messages):sub_turn=1whileTrue:response=client.chat.completions.create(model='deepseek-chat',messages=messages,tools=tools,# extra_body={ "thinking": { "type": "enabled" } } # DeepSeek official APIextra_body={"chat_template_kwargs":{"thinking":True}}# vLLM Server)messages.append(response.choices[0].message)# DeepSeek API# reasoning_content = response.choices[0].message.reasoning_content# vLLM Serverreasoning_content=response.choices[0].message.reasoningcontent=response.choices[0].message.contenttool_calls=response.choices[0].message.tool_callsprint(f"Turn {turn}.{sub_turn}\n{reasoning_content=}\n{content=}\n{tool_calls=}")# If there is no tool calls, then the model should get a final answer and we need to stop the loop# In DeepSeek API, if there are no tool_calls, then tool_calls is None.#if tool_calls is None:# In vLLM, if there are no tool_calls, then tool_calls is [].ifnottool_calls:breakfortoolintool_calls:tool_function=TOOL_CALL_MAP[tool.function.name]tool_result=tool_function(**json.loads(tool.function.arguments))print(f"tool result for {tool.function.name}: {tool_result}\n")messages.append({"role":"tool","tool_call_id":tool.id,"content":tool_result,})sub_turn+=1# You can running vLLM server using the following command# vllm serve serve deepseek-ai/DeepSeek-V3.2 \# --tensor-parallel-size 8 \# --tokenizer-mode deepseek_v32 \# --tool-call-parser deepseek_v32 \# --enable-auto-tool-choice \# --reasoning-parser deepseek_v3client=OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url=os.environ.get('DEEPSEEK_BASE_URL'),)# The user starts a questionturn=1messages=[{"role":"user","content":"How's the weather in Hangzhou Tomorrow"}]run_turn(turn,messages)# The user starts a new questionturn=2messages.append({"role":"user","content":"How's the weather in Hangzhou Tomorrow"})# We recommended to clear the reasoning_content in history messages so as to save network bandwidthclear_reasoning_content(messages)run_turn(turn,messages)

vLLM Server Print¶

Turn 1.1
reasoning_content="I need to help the user with weather in Hangzhou tomorrow. First, I need to get the current date to determine tomorrow's date. Then I can use the weather function. Let me start by getting the current date."
content=None
tool_calls=[ChatCompletionMessageFunctionToolCall(id='chatcmpl-tool-a2de4337498c482c', function=Function(arguments='{}', name='get_date'), type='function')]
tool result for get_date: 2025-12-01
Turn 1.2
reasoning_content='Today is December 1, 2025. Tomorrow would be December 2, 2025. Now I can get the weather for Hangzhou for that date.'
content=None
tool_calls=[ChatCompletionMessageFunctionToolCall(id='chatcmpl-tool-b11e7a47d3b689ea', function=Function(arguments='{"location": "Hangzhou", "date": "2025-12-02"}', name='get_weather'), type='function')]
tool result for get_weather: Cloudy 7~13°C
Turn 1.3
reasoning_content="I have the weather information: Cloudy with temperatures between 7°C and 13°C. I should provide this to the user in a clear and friendly manner. I'll mention that this is for tomorrow, December 2, 2025. Let me craft the response."
content='The weather in Hangzhou **tomorrow, Tuesday, December 2, 2025**, will be **Cloudy** with temperatures ranging from **7°C to 13°C**.'
tool_calls=[]
Turn 2.1
reasoning_content='The user is asking about the weather in Hangzhou tomorrow again. I already answered this question in the previous exchange, but I should check if "tomorrow" still refers to the same date or if there\'s a new context. The current date is December 1, 2025, so tomorrow would be December 2, 2025. I already provided that information. However, maybe the user is asking again because they want to confirm or maybe they didn\'t see the previous answer? Looking at the conversation, I provided the weather for tomorrow (December 2, 2025). The user\'s latest question is identical to the first one. I should probably respond with the same information, but perhaps acknowledge that I already provided this information. However, since the conversation continues, maybe they want additional details or something else? The weather tool only gives basic info: "Cloudy 7~13°C". I could present it again. But maybe the user expects a different format or more details? I could just repeat the answer. Let me respond politely with the same information.'
content="The weather in Hangzhou **tomorrow, Tuesday, December 2, 2025**, will be **Cloudy** with temperatures ranging from **7°C to 13°C**. \n\nThis is the same forecast I provided earlier - it looks like tomorrow's weather will be consistently cloudy with cool temperatures."
tool_calls=[]

DeepSeek Offical API Print¶

Turn 1.1
reasoning_content="The user is asking about the weather in Hangzhou tomorrow. I need to get the current date to determine what tomorrow's date is, then use that to get the weather forecast. Let me first get the current date."
content=''
tool_calls=[ChatCompletionMessageFunctionToolCall(id='call_00_OOAEfTpXddWI9rgC75bfYQJY', function=Function(arguments='{}', name='get_date'), type='function', index=0)]
tool result for get_date: 2025-12-01
Turn 1.2
reasoning_content='Today is December 1, 2025. Tomorrow would be December 2, 2025. So I need to get the weather for Hangzhou on 2025-12-02. Now I can call get_weather with location Hangzhou and date 2025-12-02.'
content=''
tool_calls=[ChatCompletionMessageFunctionToolCall(id='call_00_3P0Xqw5MrVhklmQ4QSACbDq6', function=Function(arguments='{"location": "Hangzhou", "date": "2025-12-02"}', name='get_weather'), type='function', index=0)]
tool result for get_weather: Cloudy 7~13°C
Turn 1.3
reasoning_content='Now I have the weather information: Cloudy with temperatures between 7 and 13 degrees Celsius. I should provide this to the user in a friendly manner. I can mention that tomorrow is December 2nd, and give the forecast. Let me craft the response.'
content='Tomorrow (December 2, 2025) in Hangzhou, the weather will be **cloudy** with temperatures ranging from **7°C to 13°C**.'
tool_calls=None
Turn 2.1
reasoning_content='The user is asking about the weather in Hangzhou tomorrow. I already answered this question in the previous interaction. However, I should check if "tomorrow" is still the same date. The current date is 2025-12-01. Tomorrow would be 2025-12-02. I already provided the weather for that date: Cloudy 7~13°C. \n\nBut wait, the user might be asking again, perhaps not noticing the previous answer. Or maybe they want a different presentation. I should answer again, but maybe with a slightly different phrasing. Also, I should confirm that "tomorrow" is indeed 2025-12-02.\n\nI could just repeat the information. But perhaps I should check if the date has changed? The current date is still 2025-12-01. So tomorrow is still 2025-12-02. I already have the weather data.\n\nI\'ll respond with the weather information again.'
content='Based on the previous query, tomorrow (December 2, 2025) in Hangzhou will be **cloudy** with temperatures between **7°C and 13°C**.'
tool_calls=None

Troubleshooting¶

1. Error: 
ptxas fatal: Value 'sm_110a' is not defined for option 'gpu-name'
¶

If you are using DeepSeek-V3.2 on cuda 13.x, you may encounter this.

Solution:

exportTRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas
exportPATH=/usr/local/cuda/bin:$PATHexportLD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:-}

February 11, 2026February 11, 2026

 Back to top

 
 
 Made with
 
 Material for MkDocs

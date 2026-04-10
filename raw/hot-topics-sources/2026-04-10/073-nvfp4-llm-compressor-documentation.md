---
title: fp4 Quantization with NVFP4 - LLM Compressor Docs
source_url: https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4
final_url: https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4/
status: 200
content_type: text/html; charset=utf-8
topics: [NVFP4 Quantization for LLM Inference]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:35.648349+00:00
---

# fp4 Quantization with NVFP4 - LLM Compressor Docs

## 원본 URL

https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4

## 추출 본문

fp4 Quantization with NVFP4 - LLM Compressor Docs

 Skip to content
 

 LLM Compressor Docs
 

 
 fp4 Quantization with NVFP4
 
 

 Search
 

 vllm-project/llm-compressor
 

 LLM Compressor Docs
 

 vllm-project/llm-compressor
 

 
 
 Home
 

 
 

 
 
 Why use LLM Compressor?
 

 
 

 
 
 Compressing your model, step-by-step
 

 
 
 
 
 Compressing your model, step-by-step
 

 

 
 
 Choosing your model
 

 
 

 
 
 Choosing the right compression scheme
 

 
 

 
 
 Choosing the right compression algorithm
 

 
 

 
 
 Choosing a dataset
 

 
 

 
 
 Compressing your model
 

 
 

 
 
 Deploying with vLLM
 

 
 

 
 
 Getting started
 

 
 

 
 
 Getting started
 

 

 
 
 Installing LLM Compressor
 

 
 

 
 
 Key Models
 

 
 

 
 
 Key Models
 

 

 
 
 Llama 4
 

 
 

 
 
 Llama 4
 

 

 
 
 FP8 Example
 

 
 

 
 
 Qwen3
 

 
 

 
 
 Qwen3
 

 

 
 
 FP8 Example
 

 
 

 
 
 Qwen3.5
 

 
 

 
 
 Qwen3.5
 

 

 
 
 NVFP4A16 VL Example
 

 
 

 
 
 NVFP4 MoE Example
 

 
 

 
 
 Kimi-K2
 

 
 

 
 
 Kimi-K2
 

 

 
 
 FP8 Example
 

 
 

 
 
 Mistral Large 3
 

 
 

 
 
 Mistral Large 3
 

 

 
 
 FP8 Example
 

 
 

 
 
 User Guides
 

 
 
 
 
 User Guides
 

 

 
 
 Entrypoints
 

 
 

 
 
 Entrypoints
 

 

 
 
 oneshot
 

 
 

 
 
 model-free-ptq
 

 
 

 
 
 Compression Schemes
 

 
 

 
 
 Observers
 

 
 

 
 
 Big Models and Distributed Support
 

 
 
 
 
 Big Models and Distributed Support
 

 

 
 
 Model Loading
 

 
 

 
 
 Sequential Onloading
 

 
 

 
 
 Distributed Oneshot
 

 
 

 
 
 Saving a Compressed Model
 

 
 

 
 
 Memory Requirements
 

 
 

 
 
 Runtime Performance
 

 
 

 
 
 Examples
 

 
 

 
 
 Examples
 

 

 
 
 `AutoRound` Quantization
 

 
 

 
 
 AWQ Quantization
 

 
 

 
 
 Big Model Quantization with Sequential Onloading
 

 
 

 
 
 Disk Offloading
 

 
 

 
 
 iMatrix Importance-Weighted Quantization
 

 
 

 
 
 Model-free Quantization
 

 
 

 
 
 Multimodal Audio Model Quantization
 

 
 

 
 
 Multimodal Vision-Language Quantization
 

 
 

 
 
 Attention Quantization in LLM Compressor
 

 
 

 
 
 KV Cache Quantization
 

 
 

 
 
 Non-uniform Quantization
 

 
 

 
 
 `int4` Weight Quantization
 

 
 

 
 
 `fp4` Quantization with NVFP4
 

 
 
 
 
 `fp4` Quantization with NVFP4
 

 
 
 On this page
 

 
 Installation
 
 

 
 Quickstart
 
 

 
 Code Walkthough
 
 

 
 1) Load Model
 
 

 
 2) Prepare Calibration Data
 
 

 
 3) Apply Quantization
 
 

 
 
 `fp8` Weight and Activation Quantization
 

 
 

 
 
 `int8` Weight and Activation Quantization
 

 
 

 
 
 Quantizing Mixture of Experts (MoE) models
 

 
 

 
 
 2:4 Sparsity with FP8 Quantization
 

 
 

 
 
 Applying Transforms to Improve Quantization Accuracy
 

 
 

 
 
 Experimental
 

 
 

 
 
 Experimental
 

 

 
 
 Attention Quantization in LLM Compressor
 

 
 

 
 
 Mistral-format model compression (experimental)
 

 
 

 
 
 MXFP4 Quantization
 

 
 

 
 
 Developer
 

 
 

 
 
 Developer
 

 

 
 
 API Reference
 

 
 

 
 
 API Reference
 

 

 
 
 llmcompressor
 

 
 

 
 
 llmcompressor
 

 

 
 
 args
 

 
 

 
 
 args
 

 

 
 
 dataset_arguments
 

 
 

 
 
 dataset_arguments
 

 

 
 
 model_arguments
 

 
 

 
 
 model_arguments
 

 

 
 
 recipe_arguments
 

 
 

 
 
 recipe_arguments
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 core
 

 
 

 
 
 core
 

 

 
 
 events
 

 
 

 
 
 events
 

 

 
 
 event
 

 
 

 
 
 event
 

 

 
 
 lifecycle
 

 
 

 
 
 lifecycle
 

 

 
 
 model_layer
 

 
 

 
 
 model_layer
 

 

 
 
 session
 

 
 

 
 
 session
 

 

 
 
 session_functions
 

 
 

 
 
 session_functions
 

 

 
 
 state
 

 
 

 
 
 state
 

 

 
 
 datasets
 

 
 

 
 
 datasets
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 entrypoints
 

 
 

 
 
 entrypoints
 

 

 
 
 model_free
 

 
 

 
 
 model_free
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 lifecycle
 

 
 

 
 
 lifecycle
 

 

 
 
 microscale
 

 
 

 
 
 microscale
 

 

 
 
 process
 

 
 

 
 
 process
 

 

 
 
 reindex_fused_weights
 

 
 

 
 
 reindex_fused_weights
 

 

 
 
 save_utils
 

 
 

 
 
 save_utils
 

 

 
 
 validate
 

 
 

 
 
 validate
 

 

 
 
 oneshot
 

 
 

 
 
 oneshot
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 logger
 

 
 

 
 
 logger
 

 

 
 
 modeling
 

 
 

 
 
 modeling
 

 

 
 
 afmoe
 

 
 

 
 
 afmoe
 

 

 
 
 deepseek_v3
 

 
 

 
 
 deepseek_v3
 

 

 
 
 deepseekv32
 

 
 

 
 
 deepseekv32
 

 

 
 
 config
 

 
 

 
 
 config
 

 

 
 
 kernel
 

 
 

 
 
 kernel
 

 

 
 
 model
 

 
 

 
 
 model
 

 

 
 
 fuse
 

 
 

 
 
 fuse
 

 

 
 
 gemma4
 

 
 

 
 
 gemma4
 

 

 
 
 glm4_moe
 

 
 

 
 
 glm4_moe
 

 

 
 
 glm_moe_dsa
 

 
 

 
 
 glm_moe_dsa
 

 

 
 
 gpt_oss
 

 
 

 
 
 gpt_oss
 

 

 
 
 granite4
 

 
 

 
 
 granite4
 

 

 
 
 llama4
 

 
 

 
 
 llama4
 

 

 
 
 moe_context
 

 
 

 
 
 moe_context
 

 

 
 
 offset_norm
 

 
 

 
 
 offset_norm
 

 

 
 
 qwen3_5_moe
 

 
 

 
 
 qwen3_5_moe
 

 

 
 
 qwen3_moe
 

 
 

 
 
 qwen3_moe
 

 

 
 
 qwen3_next_moe
 

 
 

 
 
 qwen3_next_moe
 

 

 
 
 qwen3_vl_moe
 

 
 

 
 
 qwen3_vl_moe
 

 

 
 
 modifiers
 

 
 

 
 
 modifiers
 

 

 
 
 autoround
 

 
 

 
 
 autoround
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 awq
 

 
 

 
 
 awq
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 dynamic_mappings
 

 
 

 
 
 dynamic_mappings
 

 

 
 
 mappings
 

 
 

 
 
 mappings
 

 

 
 
 experimental
 

 
 

 
 
 experimental
 

 

 
 
 factory
 

 
 

 
 
 factory
 

 

 
 
 gptq
 

 
 

 
 
 gptq
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 gptq_quantize
 

 
 

 
 
 gptq_quantize
 

 

 
 
 interface
 

 
 

 
 
 interface
 

 

 
 
 logarithmic_equalization
 

 
 

 
 
 logarithmic_equalization
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 modifier
 

 
 

 
 
 modifier
 

 

 
 
 obcq
 

 
 

 
 
 obcq
 

 

 
 
 sgpt_base
 

 
 

 
 
 sgpt_base
 

 

 
 
 pruning
 

 
 

 
 
 pruning
 

 

 
 
 constant
 

 
 

 
 
 constant
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 magnitude
 

 
 

 
 
 magnitude
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 sparsegpt
 

 
 

 
 
 sparsegpt
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 sgpt_base
 

 
 

 
 
 sgpt_base
 

 

 
 
 sgpt_sparsify
 

 
 

 
 
 sgpt_sparsify
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 pytorch
 

 
 

 
 
 pytorch
 

 

 
 
 layer_mask
 

 
 

 
 
 layer_mask
 

 

 
 
 mask_factory
 

 
 

 
 
 mask_factory
 

 

 
 
 wanda
 

 
 

 
 
 wanda
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 wanda_sparsify
 

 
 

 
 
 wanda_sparsify
 

 

 
 
 quantization
 

 
 

 
 
 quantization
 

 

 
 
 calibration
 

 
 

 
 
 calibration
 

 

 
 
 gptq
 

 
 

 
 
 gptq
 

 

 
 
 group_size_validation
 

 
 

 
 
 group_size_validation
 

 

 
 
 quantization
 

 
 

 
 
 quantization
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 mixin
 

 
 

 
 
 mixin
 

 

 
 
 smoothquant
 

 
 

 
 
 smoothquant
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 transform
 

 
 

 
 
 transform
 

 

 
 
 imatrix
 

 
 

 
 
 imatrix
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 quip
 

 
 

 
 
 quip
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 smoothquant
 

 
 

 
 
 smoothquant
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 spinquant
 

 
 

 
 
 spinquant
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 mappings
 

 
 

 
 
 mappings
 

 

 
 
 norm_mappings
 

 
 

 
 
 norm_mappings
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 constants
 

 
 

 
 
 constants
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 hooks
 

 
 

 
 
 hooks
 

 

 
 
 pytorch_helpers
 

 
 

 
 
 pytorch_helpers
 

 

 
 
 observers
 

 
 

 
 
 observers
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 imatrix
 

 
 

 
 
 imatrix
 

 

 
 
 min_max
 

 
 

 
 
 min_max
 

 

 
 
 moving_base
 

 
 

 
 
 moving_base
 

 

 
 
 mse
 

 
 

 
 
 mse
 

 

 
 
 pipelines
 

 
 

 
 
 pipelines
 

 

 
 
 basic
 

 
 

 
 
 basic
 

 

 
 
 pipeline
 

 
 

 
 
 pipeline
 

 

 
 
 cache
 

 
 

 
 
 cache
 

 

 
 
 data_free
 

 
 

 
 
 data_free
 

 

 
 
 pipeline
 

 
 

 
 
 pipeline
 

 

 
 
 independent
 

 
 

 
 
 independent
 

 

 
 
 pipeline
 

 
 

 
 
 pipeline
 

 

 
 
 registry
 

 
 

 
 
 registry
 

 

 
 
 sequential
 

 
 

 
 
 sequential
 

 

 
 
 ast_helpers
 

 
 

 
 
 ast_helpers
 

 

 
 
 ast_utils
 

 
 

 
 
 ast_utils
 

 

 
 
 auto_wrapper
 

 
 

 
 
 auto_wrapper
 

 

 
 
 control_flow_analyzer
 

 
 

 
 
 control_flow_analyzer
 

 

 
 
 name_analyzer
 

 
 

 
 
 name_analyzer
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 pipeline
 

 
 

 
 
 pipeline
 

 

 
 
 transformers_helpers
 

 
 

 
 
 transformers_helpers
 

 

 
 
 pytorch
 

 
 

 
 
 pytorch
 

 

 
 
 model_load
 

 
 

 
 
 model_load
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 sparsification
 

 
 

 
 
 sparsification
 

 

 
 
 sparsification_info
 

 
 

 
 
 sparsification_info
 

 

 
 
 configs
 

 
 

 
 
 configs
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 module_sparsification_info
 

 
 

 
 
 module_sparsification_info
 

 

 
 
 recipe
 

 
 

 
 
 recipe
 

 

 
 
 metadata
 

 
 

 
 
 metadata
 

 

 
 
 recipe
 

 
 

 
 
 recipe
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 sentinel
 

 
 

 
 
 sentinel
 

 

 
 
 transformers
 

 
 

 
 
 transformers
 

 

 
 
 compression
 

 
 

 
 
 compression
 

 

 
 
 compressed_tensors_utils
 

 
 

 
 
 compressed_tensors_utils
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 data
 

 
 

 
 
 data
 

 

 
 
 base
 

 
 

 
 
 base
 

 

 
 
 c4
 

 
 

 
 
 c4
 

 

 
 
 cnn_dailymail
 

 
 

 
 
 cnn_dailymail
 

 

 
 
 custom
 

 
 

 
 
 custom
 

 

 
 
 data_helpers
 

 
 

 
 
 data_helpers
 

 

 
 
 evolcodealpaca
 

 
 

 
 
 evolcodealpaca
 

 

 
 
 flickr_30k
 

 
 

 
 
 flickr_30k
 

 

 
 
 gsm8k
 

 
 

 
 
 gsm8k
 

 

 
 
 open_platypus
 

 
 

 
 
 open_platypus
 

 

 
 
 peoples_speech
 

 
 

 
 
 peoples_speech
 

 

 
 
 ultrachat_200k
 

 
 

 
 
 ultrachat_200k
 

 

 
 
 wikitext
 

 
 

 
 
 wikitext
 

 

 
 
 tracing
 

 
 

 
 
 tracing
 

 

 
 
 debug
 

 
 

 
 
 debug
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 dev
 

 
 

 
 
 dev
 

 

 
 
 dist
 

 
 

 
 
 dist
 

 

 
 
 helpers
 

 
 

 
 
 helpers
 

 

 
 
 metric_logging
 

 
 

 
 
 metric_logging
 

 

 
 
 pytorch
 

 
 

 
 
 pytorch
 

 

 
 
 module
 

 
 

 
 
 module
 

 

 
 
 utils
 

 
 

 
 
 utils
 

 

 
 
 transformers
 

 
 

 
 
 transformers
 

 

 
 
 FAQ
 

 
 
 
 
 FAQ
 

 

 
 
 Frequently Asked Questions
 

 
 

 On this page
 

 
 Installation
 
 

 
 Quickstart
 
 

 
 Code Walkthough
 
 

 
 1) Load Model
 
 

 
 2) Prepare Calibration Data
 
 

 
 3) Apply Quantization
 
 

 Home
 

 Examples
 

fp4
 Quantization with NVFP4

For weight-only FP4 quantization (e.g MXFP4A16, NVFP4A16) see examples here.

llm-compressor
 supports quantizing weights and activations to 
fp4
 for memory savings and inference acceleration with 
vLLM
. In particular, 
nvfp4
 is supported - a 4-bit floating point encoding format introduced with the NVIDIA Blackwell GPU architecture.

Installation

To get started, install:

gitclonehttps://github.com/vllm-project/llm-compressor.git
cdllm-compressor
pipinstall-e.

Quickstart

The example includes an end-to-end script for applying the quantization algorithm.

python3llama3_example.py

The resulting model 
Meta-Llama-3-8B-Instruct-NVFP4
 is ready to be loaded into vLLM.
Note: if running inference on a machine that is < SM100, vLLM will not run activation
quantization, only weight-only quantization.

Code Walkthough

Now, we will step though the code in the example:
1) Load model
2) Prepare calibration data
3) Apply quantization

1) Load Model

Load the model using 
AutoModelForCausalLM
 for handling quantized saving and loading. 

fromtransformersimportAutoTokenizer,AutoModelForCausalLMMODEL_ID="meta-llama/Meta-Llama-3-8B-Instruct"model=AutoModelForCausalLM.from_pretrained(MODEL_ID,dtype="auto")tokenizer=AutoTokenizer.from_pretrained(MODEL_ID)

2) Prepare Calibration Data

Prepare the calibration data. 
nvfp4
 quantization generates per-tensor global scales and per-group (size 16) local quantization scales for the weights, as well as per-tensor global scales for the activations. Per-group local activation quantization scales are generated dynamically during inference time. We need some sample data to calibrate the global activation scales. Typically, a small number of samples is sufficient. In this example, we use a sample size of 20.

It is useful to use calibration data that closely matches the type of data used in deployment. If you have fine-tuned a model, using a sample of your training data is a good idea. In our case, we are quantizing an instruction-tuned generic model, so we will use the 
ultrachat
 dataset. 

3) Apply Quantization

With the dataset ready, we will now apply quantization.

We first select the quantization algorithm.

In our case, we will apply the default QuantizationModifier recipe for 
nvfp4
 to all linear layers.

See the 
Recipes
 documentation for more information on making complex recipes

fromllmcompressorimportoneshotfromllmcompressor.modifiers.quantizationimportQuantizationModifier# Configure the quantization algorithm to run.recipe=QuantizationModifier(targets="Linear",scheme="NVFP4",ignore=["lm_head"])# Apply quantization.oneshot(model=model,dataset=ds,recipe=recipe,max_seq_length=MAX_SEQUENCE_LENGTH,num_calibration_samples=NUM_CALIBRATION_SAMPLES,)# Save to disk compressed.SAVE_DIR=MODEL_ID.rstrip("/").split("/")[-1]+"-NVFP4"model.save_pretrained(SAVE_DIR,save_compressed=True)tokenizer.save_pretrained(SAVE_DIR)

We have successfully created an 
nvfp4
 model!

 Back to top

 Previous
 

 `int4` Weight Quantization
 

 Next
 

 `fp8` Weight and Activation Quantization

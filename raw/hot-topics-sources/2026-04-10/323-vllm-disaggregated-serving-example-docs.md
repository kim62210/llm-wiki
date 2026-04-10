---
title: Disaggregated Serving - vLLM
source_url: https://docs.vllm.ai/en/latest/examples/online_serving/disaggregated_serving.html
final_url: https://docs.vllm.ai/en/latest/examples/online_serving/disaggregated_serving/
status: 200
content_type: text/html; charset=utf-8
topics: [vLLM V1 Engine on Blackwell (GB200/GB300)]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:09.089479+00:00
---

# Disaggregated Serving - vLLM

## 원본 URL

https://docs.vllm.ai/en/latest/examples/online_serving/disaggregated_serving.html

## 추출 본문

Disaggregated Serving - vLLM
 Skip to content 

You are viewing the latest developer preview docs. Click here to view docs for the latest stable release.

 vLLM 

 Disaggregated Serving 

 Initializing search 

 GitHub 

 Home 

 User Guide 

 Developer Guide 

 Benchmarking 

 API Reference 

 CLI Reference 

 Community 

 vLLM 

 GitHub 

 Home 

 User Guide 
 User Guide 
 Getting Started Getting Started 
 Quickstart 

 Installation 
 Installation 
 GPU 

 CPU 

 TPU 

 Examples 
 Examples 
 Basic Basic 
 Offline Inference 

 Online Serving 

 Offline Inference Offline Inference 
 Async LLM Streaming 

 Audio Language 

 Automatic Prefix Caching 

 Batch LLM Inference 

 Chat With Tools 

 Context Extension 

 Data Parallel 

 Disaggregated Prefill V1 

 Disaggregated Prefill 

 Encoder Decoder Multimodal 

 Extract Hidden States 

 KV Load Failure Recovery Test 

 LLM Engine Example 

 LLM Engine Reset Kv 

 Load Sharded State 

 Custom Logits Processors 

 LoRA With Quantization Inference 

 Metrics 

 Mistral-Small 

 MLPSpeculator 

 MultiLoRA Inference 

 Offline Inference with the OpenAI Batch file format 

 Pause Resume 

 Prefix Caching 

 Prefix Caching Flexkv 

 Prompt Embed Inference 

 Qwen2.5-Omni Offline Inference Examples 

 Qwen3 Omni 

 Qwen 1M 

 Reproducibility 

 Routed Experts E2E 

 Run One Batch 

 Save Sharded State 

 Simple Profiling 

 Skip Loading Weights In Engine Init 

 Spec Decode 

 Structured Outputs 

 Torchrun Dp Example 

 Torchrun Example 

 Vision Language 

 Vision Language Multi Image 

 Online Serving Online Serving 
 API Client 

 Batched Chat Completions 

 Helm Charts 

 Monitoring Dashboards 

 Data Parallel Pause Resume 

 Disaggregated Encoder 

 Disaggregated Prefill 

 Disaggregated Serving Disaggregated Serving Table of contents 
 Files 

 Example materials 

 Disaggregated Serving P2P NCCL Xpyd 

 Ec Both Encoder 

 Elastic Ep 

 Gradio OpenAI Chatbot Webserver 

 Gradio Webserver 

 Kv Events Subscriber 

 Multi-Node-Serving 

 Multi Instance Data Parallel 

 OpenAI Chat Completion Client For Multimodal 

 OpenAI Chat Completion Client With Tools 

 OpenAI Chat Completion Client With Tools Required 

 OpenAI Chat Completion Client With Tools Xlam 

 OpenAI Chat Completion Client With Tools Xlam Streaming 

 OpenAI Chat Completion Tool Calls With Reasoning 

 OpenAI Chat Completion With Reasoning 

 OpenAI Chat Completion With Reasoning Streaming 

 OpenAI Realtime Client 

 OpenAI Realtime Microphone Client 

 OpenAI Responses Client 

 OpenAI Responses Client With Mcp Tools 

 OpenAI Responses Client With Tools 

 OpenAI Transcription Client 

 OpenAI Translation Client 

 Setup OpenTelemetry POC 

 Prometheus and Grafana 

 Prompt Embed Inference With OpenAI Client 

 Ray Serve Deepseek 

 Retrieval Augmented Generation With Langchain 

 Retrieval Augmented Generation With Llamaindex 

 Run Cluster 

 Sagemaker-Entrypoint 

 Streamlit OpenAI Chatbot Webserver 

 Structured Outputs 

 Token Generation Client 

 Utils 

 Others Others 
 LMCache Examples 

 Logging Configuration 

 Tensorize vLLM Model 

 Pooling Pooling 
 Classify 

 Embed 

 Plugin 

 Pooling 

 Score 

 Token Classify 

 Token Embed 

 RL RL 
 RLHF Async New APIs 

 RLHF Http IPC 

 RLHF Http NCCL 

 RLHF IPC 

 RLHF NCCL 

 RLHF NCCL Fsdp Ep 

 General General 
 vLLM V1 

 Frequently Asked Questions 

 Production Metrics 

 Reproducibility 

 Security 

 Troubleshooting 

 Usage Stats Collection 

 Inference and Serving Inference and Serving 
 Offline Inference 

 OpenAI-Compatible Server 

 Context Parallel Deployment 

 Data Parallel Deployment 

 Troubleshooting distributed deployments 

 Expert Parallel Deployment 

 Parallelism and Scaling 

 Integrations Integrations 
 Claude Code 

 LangChain 

 LlamaIndex 

 Deployment Deployment 
 Using Docker 

 Using Kubernetes 

 Using Nginx 

 Frameworks Frameworks 
 Anyscale 

 AnythingLLM 

 AutoGen 

 BentoML 

 Cerebrium 

 Chatbox 

 Dify 

 dstack 

 Haystack 

 Helm 

 Hugging Face Inference Endpoints 

 LiteLLM 

 Lobe Chat 

 LWS 

 Modal 

 Open WebUI 

 Retrieval-Augmented Generation 

 RunPod 

 SkyPilot 

 Streamlit 

 NVIDIA Triton 

 Integrations Integrations 
 AIBrix 

 NVIDIA Dynamo 

 KAITO 

 KServe 

 Kthena 

 KubeAI 

 KubeRay 

 Llama Stack 

 llm-d 

 llmaz 

 Production stack 

 Training Training 
 Async Reinforcement Learning 

 Reinforcement Learning from Human Feedback 

 Transformers Reinforcement Learning 

 Weight Transfer 
 Weight Transfer 
 Base Class and Custom Engines 

 IPC Engine 

 NCCL Engine 

 Configuration 
 Configuration 
 Conserving Memory 

 Engine Arguments 

 Environment Variables 

 Model Resolution 

 Optimization and Tuning 

 Server Arguments 

 TPU 

 Models Models 
 Supported Models 

 Generative Models 

 Pooling Models 
 Pooling Models 
 Classification Usages 

 Embedding Usages 

 Reward Usages 

 Scoring Usages 

 Specific Model Examples 

 Token Classification Usages 

 Token Embedding Usages 

 Extensions Extensions 
 Loading model weights with fastsafetensors 

 Loading Model Weights with InstantTensor 

 Loading models with Run:ai Model Streamer 

 Loading models with CoreWeave's Tensorizer 

 Hardware Supported Models Hardware Supported Models 
 CPU - Intel® Xeon® 

 XPU - Intel® GPUs 

 TPU 

 Features 
 Features 
 Automatic Prefix Caching 

 Batch Invariance 

 Custom Arguments 

 Custom Logits Processors 

 Disaggregated Encoder 

 Disaggregated Prefilling (experimental) 

 Interleaved Thinking 

 LoRA Adapters 

 MooncakeConnector Usage Guide 

 Multimodal Inputs 

 NixlConnector Compatibility Matrix 

 NixlConnector Usage Guide 

 Prompt Embedding Inputs 

 Reasoning Outputs 

 Sleep Mode 

 Structured Outputs 

 Tool Calling 

 Quantization 
 Quantization 
 AutoAWQ 

 BitsAndBytes 

 FP8 W8A8 

 GGUF 

 GPTQModel 

 Intel Quantization Support 

 INT4 W4A16 

 INT8 W8A8 

 LLM Compressor 

 NVIDIA Model Optimizer 

 Quantized KV Cache 

 AMD Quark 

 TorchAO 

 Speculative Decoding 
 Speculative Decoding 
 Draft Models 

 EAGLE Draft Models 

 MLP Draft Models 

 MTP (Multi-Token Prediction) 

 N-Gram Speculation 

 Parallel Draft Models 

 vLLM-Project/Speculators 

 Suffix Decoding 

 Developer Guide 
 Developer Guide 
 General General 
 Deprecation Policy 

 Dockerfile 

 Editing Agent Instructions 

 Incremental Compilation Workflow 

 Profiling vLLM 

 Vulnerability Management 

 Model Implementation 
 Model Implementation 
 Basic Model 

 Registering a Model 

 Unit Testing 

 Multi-Modal Support 

 Speech-to-Text (Transcription/Translation) Support 

 CI CI 
 CI Failures 

 Nightly Builds of vLLM Wheels 

 Update PyTorch version on vLLM OSS CI/CD 

 Design Documents Design Documents 
 Plugins Plugins 
 IO Processor Plugins 

 LoRA Resolver Plugins 

 Plugin System 

 Architecture Overview 

 Attention Backend Feature Support 

 CUDA Graphs 

 Vision Encoder (ViT) CUDA Graphs 

 CustomOp 

 Dual Batch Overlap 

 How to debug the vLLM-torch.compile integration 

 Fused MoE Modular Kernel 

 Fusion torch.compile passes 

 Integration with Hugging Face 

 Hybrid KV Cache Manager 

 Logits Processors 

 Metrics 

 Multi-Modal Data Processing 

 Model Runner V2 Design Document 

 Fused MoE Kernel Features 

 Python Multiprocessing 

 Optimization Levels 

 P2P NCCL Connector 

 Paged Attention 

 Automatic Prefix Caching 

 torch.compile integration 

 torch.compile with Multimodal Encoders 

 Benchmarking 
 Benchmarking 
 Benchmark CLI 

 Parameter Sweeps 

 Performance Dashboard 

 API Reference 
 API Reference 

 vllm 
 vllm 
 beam_search 

 collect_env 

 connections 

 env_override 

 envs 

 exceptions 

 forward_context 

 logger 

 logits_process 

 logprobs 

 model_inspection 

 outputs 

 pooling_params 

 sampling_params 

 scalar_type 

 scripts 

 sequence 

 tasks 

 version 

 assets 
 assets 
 audio 

 base 

 image 

 video 

 benchmarks 
 benchmarks 
 datasets 

 latency 

 mm_processor 

 plot 

 serve 

 startup 

 throughput 

 lib 
 lib 
 endpoint_request_func 

 ready_checker 

 utils 

 sweep 
 sweep 
 cli 

 param_sweep 

 plot 

 plot_pareto 

 serve 

 serve_workload 

 server 

 startup 

 utils 

 compilation 
 compilation 
 backends 

 base_static_graph 

 caching 

 compiler_interface 

 counter 

 cuda_graph 

 decorators 

 monitor 

 partition_rules 

 piecewise_backend 

 wrapper 

 passes 
 passes 
 fx_utils 

 inductor_pass 

 pass_manager 

 vllm_inductor_pass 

 fusion 
 fusion 
 act_quant_fusion 

 allreduce_rms_fusion 

 attn_quant_fusion 

 collective_fusion 

 matcher_utils 

 mla_attn_quant_fusion 

 qk_norm_rope_fusion 

 rms_quant_fusion 

 rocm_aiter_fusion 

 rope_kvcache_fusion 

 sequence_parallelism 

 ir 
 ir 
 lowering_pass 

 utility 
 utility 
 fix_functionalization 

 noop_elimination 

 post_cleanup 

 scatter_split_replace 

 split_coalescing 

 config 
 config 
 attention 

 cache 

 compilation 

 device 

 ec_transfer 

 kernel 

 kv_events 

 kv_transfer 

 load 

 lora 

 model 

 model_arch 

 multimodal 

 observability 

 offload 

 parallel 

 pooler 

 profiler 

 quantization 

 reasoning 

 scheduler 

 speculative 

 speech_to_text 

 structured_outputs 

 utils 

 vllm 

 weight_transfer 

 device_allocator 
 device_allocator 
 cumem 

 distributed 
 distributed 
 communication_op 

 kv_events 

 parallel_state 

 stateless_coordinator 

 utils 

 device_communicators 
 device_communicators 
 all2all 

 all_reduce_utils 

 base_device_communicator 

 cpu_communicator 

 cuda_communicator 

 cuda_wrapper 

 custom_all_reduce 

 flashinfer_all_reduce 

 mnnvl_compat 

 pynccl 

 pynccl_allocator 

 pynccl_wrapper 

 quick_all_reduce 

 ray_communicator 

 shm_broadcast 

 shm_object_storage 

 symm_mem 

 xpu_communicator 

 ec_transfer 
 ec_transfer 
 ec_transfer_state 

 ec_connector 
 ec_connector 
 base 

 example_connector 

 factory 

 elastic_ep 
 elastic_ep 
 elastic_execute 

 elastic_state 

 standby_state 

 eplb 
 eplb 
 async_worker 

 eplb_communicator 

 eplb_state 

 eplb_utils 

 rebalance_execute 

 policy 
 policy 
 abstract 

 default 

 kv_transfer 
 kv_transfer 
 kv_transfer_state 

 kv_connector 
 kv_connector 
 base 

 factory 

 utils 

 v1 
 v1 
 base 

 decode_bench_connector 

 example_connector 

 example_hidden_states_connector 

 flexkv_connector 

 lmcache_connector 

 lmcache_mp_connector 

 metrics 

 multi_connector 

 nixl_connector 

 offloading_connector 

 simple_cpu_offload_connector 

 ssm_conv_transfer_utils 

 hf3fs 
 hf3fs 
 hf3fs_client 

 hf3fs_connector 

 hf3fs_metadata_server 

 utils 
 utils 
 common 

 gather_scatter_helper 

 hf3fs_mock_client 

 lmcache_integration 
 lmcache_integration 
 multi_process_adapter 

 utils 

 vllm_v1_adapter 

 mooncake 
 mooncake 
 mooncake_connector 

 mooncake_utils 

 moriio 
 moriio 
 moriio_common 

 moriio_connector 

 moriio_engine 

 offloading 
 offloading 
 common 

 metrics 

 scheduler 

 worker 

 p2p 
 p2p 
 p2p_nccl_connector 

 p2p_nccl_engine 

 tensor_memory_pool 

 weight_transfer 
 weight_transfer 
 base 

 factory 

 ipc_engine 

 nccl_engine 

 packed_tensor 

 engine 
 engine 
 arg_utils 

 async_llm_engine 

 llm_engine 

 protocol 

 entrypoints 
 entrypoints 
 api_server 

 chat_utils 

 constants 

 grpc_server 

 launcher 

 llm 

 logger 

 ssl 

 utils 

 anthropic 
 anthropic 
 api_router 

 protocol 

 serving 

 cli 
 cli 
 collect_env 

 launch 

 main 

 openai 

 run_batch 

 serve 

 types 

 benchmark 
 benchmark 
 base 

 latency 

 main 

 mm_processor 

 serve 

 startup 

 sweep 

 throughput 

 mcp 
 mcp 
 tool 

 tool_server 

 openai 
 openai 
 api_server 

 cli_args 

 orca_metrics 

 run_batch 

 server_utils 

 utils 

 chat_completion 
 chat_completion 
 api_router 

 batch_serving 

 protocol 

 serving 

 stream_harmony 

 completion 
 completion 
 api_router 

 protocol 

 serving 

 engine 
 engine 
 protocol 

 serving 

 generate 
 generate 
 api_router 

 generative_scoring 
 generative_scoring 
 api_router 

 serving 

 models 
 models 
 api_router 

 protocol 

 serving 

 parser 
 parser 
 harmony_utils 

 responses_parser 

 realtime 
 realtime 
 api_router 

 connection 

 metrics 

 protocol 

 serving 

 responses 
 responses 
 api_router 

 context 

 harmony 

 protocol 

 serving 

 streaming_events 

 utils 

 speech_to_text 
 speech_to_text 
 api_router 

 protocol 

 serving 

 speech_to_text 

 pooling 
 pooling 
 io_processor_factories 

 typing 

 utils 

 base 
 base 
 io_processor 

 protocol 

 serving 

 classify 
 classify 
 api_router 

 io_processor 

 protocol 

 serving 

 embed 
 embed 
 api_router 

 io_processor 

 protocol 

 serving 

 pooling 
 pooling 
 api_router 

 io_processor 

 protocol 

 serving 

 scoring 
 scoring 
 api_router 

 io_processor 

 protocol 

 serving 

 typing 

 utils 

 sagemaker 
 sagemaker 
 api_router 

 serve 
 serve 

 cache 
 cache 
 api_router 

 disagg 
 disagg 
 api_router 

 protocol 

 serving 

 elastic_ep 
 elastic_ep 
 api_router 

 middleware 

 instrumentator 
 instrumentator 
 basic 

 health 

 metrics 

 offline_docs 

 server_info 

 lora 
 lora 
 api_router 

 protocol 

 profile 
 profile 
 api_router 

 render 
 render 
 api_router 

 serving 

 rlhf 
 rlhf 
 api_router 

 rpc 
 rpc 
 api_router 

 sleep 
 sleep 
 api_router 

 tokenize 
 tokenize 
 api_router 

 protocol 

 serving 

 inputs 
 inputs 
 engine 

 llm 

 preprocess 

 ir 
 ir 
 op 

 util 

 ops 
 ops 
 layernorm 

 kernels 
 kernels 
 aiter_ops 

 oink_ops 

 vllm_c 

 xpu_ops 

 helion 
 helion 
 config_manager 

 register 

 utils 

 ops 
 ops 
 silu_mul_fp8 

 logging_utils 
 logging_utils 
 access_log_filter 

 dump_input 

 formatter 

 lazy 

 log_time 

 torch_tensor 

 lora 
 lora 
 lora_model 

 lora_weights 

 model_manager 

 peft_helper 

 request 

 resolver 

 utils 

 worker_manager 

 layers 
 layers 
 base 

 base_linear 

 column_parallel_linear 

 fused_moe 

 logits_processor 

 replicated_linear 

 row_parallel_linear 

 utils 

 vocal_parallel_embedding 

 ops 
 ops 

 torch_ops 
 torch_ops 
 lora_ops 

 triton_ops 
 triton_ops 
 fp8_kernel_utils 

 fused_moe_lora_fp8_op 

 fused_moe_lora_op 

 kernel_utils 

 lora_expand_fp8_op 

 lora_expand_op 

 lora_kernel_metadata 

 lora_shrink_fp8_op 

 lora_shrink_op 

 utils 

 xpu_ops 
 xpu_ops 
 lora_ops 

 punica_wrapper 
 punica_wrapper 
 punica_base 

 punica_cpu 

 punica_gpu 

 punica_selector 

 punica_xpu 

 utils 

 model_executor 
 model_executor 
 custom_op 

 parameter 

 utils 

 kernels 
 kernels 

 linear 
 linear 
 base 

 mixed_precision 
 mixed_precision 
 allspark 

 conch 

 cpu 

 cutlass 

 dynamic_4bit 

 exllama 

 MPLinearKernel 

 machete 

 marlin 

 xpu 

 nvfp4 
 nvfp4 
 base 

 cutlass 

 emulation 

 fbgemm 

 flashinfer 

 marlin 

 scaled_mm 
 scaled_mm 
 aiter 

 BlockScaledMMLinearKernel 

 cpu 

 cutlass 

 deep_gemm 

 flashinfer 

 marlin 

 pytorch 

 rocm 

 ScaledMMLinearKernel 

 triton 

 xpu 

 layers 
 layers 
 activation 

 attention_layer_base 

 batch_invariant 

 conv 

 kda 

 layernorm 

 lightning_attn 

 linear 

 logits_processor 

 mla 

 resampler 

 sparse_attn_indexer 

 utils 

 vocab_parallel_embedding 

 attention 
 attention 
 attention 

 chunked_local_attention 

 cross_attention 

 encoder_only_attention 

 kv_transfer_utils 

 mla_attention 

 mm_encoder_attention 

 static_sink_attention 

 fla 
 fla 

 ops 
 ops 
 chunk 

 chunk_delta_h 

 chunk_o 

 chunk_scaled_dot_kkt 

 cumsum 

 fused_gdn_prefill_post_conv 

 fused_recurrent 

 fused_sigmoid_gating 

 index 

 kda 

 l2norm 

 layernorm_guard 

 op 

 solve_tril 

 utils 

 wy_fast 

 fused_moe 
 fused_moe 
 activation 

 all2all_utils 

 config 

 cpu_fused_moe 

 cutlass_moe 

 deep_gemm_utils 

 fallback 

 flashinfer_cutlass_moe 

 fused_batched_moe 

 fused_marlin_moe 

 fused_moe 

 fused_moe_method_base 

 fused_moe_modular_method 

 gpt_oss_triton_kernels_moe 

 layer 

 modular_kernel 

 moe_align_block_size 

 moe_permute_unpermute 

 mori_prepare_finalize 

 nixl_ep_prepare_finalize 

 rocm_aiter_fused_moe 

 routed_experts_capturer 

 shared_fused_moe 

 topk_weight_and_reduce 

 triton_cutlass_moe 

 triton_deep_gemm_moe 

 unquantized_fused_moe_method 

 utils 

 xpu_fused_moe 

 zero_expert_fused_moe 

 experts 
 experts 
 batched_deep_gemm_moe 

 deep_gemm_moe 

 flashinfer_cutedsl_batched_moe 

 flashinfer_cutedsl_moe 

 trtllm_bf16_moe 

 trtllm_fp8_moe 

 trtllm_mxfp4_moe 

 trtllm_nvfp4_moe 

 oracle 
 oracle 
 fp8 

 mxfp4 

 mxfp8 

 nvfp4 

 unquantized 

 prepare_finalize 
 prepare_finalize 
 deepep_ht 

 deepep_ll 

 flashinfer_nvlink_one_sided 

 flashinfer_nvlink_two_sided 

 naive_dp_ep 

 no_dp_ep 

 router 
 router 
 base_router 

 custom_routing_router 

 fused_moe_router 

 fused_topk_bias_router 

 fused_topk_router 

 gate_linear 

 grouped_topk_router 

 router_factory 

 routing_simulator_router 

 runner 
 runner 
 chunking_moe_runner 

 default_moe_runner 

 moe_runner 

 moe_runner_base 

 moe_runner_factory 

 shared_experts 

 mamba 
 mamba 
 abstract 

 gdn_linear_attn 

 linear_attn 

 mamba_mixer 

 mamba_mixer2 

 mamba_utils 

 short_conv 

 ops 
 ops 
 causal_conv1d 

 layernorm_gated 

 mamba_ssm 

 ssd_bmm 

 ssd_chunk_scan 

 ssd_chunk_state 

 ssd_combined 

 ssd_state_passing 

 triton_helpers 

 pooler 
 pooler 
 abstract 

 activations 

 common 

 special 

 seqwise 
 seqwise 
 heads 

 methods 

 poolers 

 tokwise 
 tokwise 
 heads 

 methods 

 poolers 

 quantization 
 quantization 
 awq 

 awq_marlin 

 awq_triton 

 base_config 

 bitsandbytes 

 cpu_wna16 

 experts_int8 

 fbgemm_fp8 

 fp8 

 fp_quant 

 gguf 

 gptq 

 gptq_marlin 

 inc 

 input_quant_fp8 

 kv_cache 

 modelopt 

 moe_wna16 

 mxfp4 

 mxfp8 

 qutlass_utils 

 schema 

 torchao 

 compressed_tensors 
 compressed_tensors 
 compressed_tensors 

 triton_scaled_mm 

 utils 

 compressed_tensors_moe 
 compressed_tensors_moe 
 compressed_tensors_moe 

 compressed_tensors_moe_w4a4_mxfp4 

 compressed_tensors_moe_w4a4_nvfp4 

 compressed_tensors_moe_w4a8_fp8 

 compressed_tensors_moe_w4a8_int8 

 compressed_tensors_moe_w8a8_fp8 

 compressed_tensors_moe_w8a8_int8 

 compressed_tensors_moe_wna16 

 compressed_tensors_moe_wna16_marlin 

 schemes 
 schemes 
 compressed_tensors_24 

 compressed_tensors_scheme 

 compressed_tensors_w4a4_nvfp4 

 compressed_tensors_w4a8_fp8 

 compressed_tensors_w4a8_int 

 compressed_tensors_w4a16_mxfp4 

 compressed_tensors_w4a16_nvfp4 

 compressed_tensors_w8a8_fp8 

 compressed_tensors_w8a8_int8 

 compressed_tensors_w8a16_fp8 

 compressed_tensors_wNa16 

 transform 
 transform 
 linear 

 module 

 utils 

 schemes 
 schemes 
 linear_qutlass_nvfp4 

 online 
 online 
 base 

 fp8 

 quark 
 quark 
 quark 

 quark_moe 

 utils 

 schemes 
 schemes 
 quark_ocp_mx 

 quark_scheme 

 quark_w4a8_mxfp4_fp8 

 quark_w8a8_fp8 

 quark_w8a8_int8 

 utils 
 utils 
 allspark_utils 

 flashinfer_fp4_moe 

 flashinfer_mxint4_moe 

 flashinfer_utils 

 fp8_utils 

 gptq_utils 

 int8_utils 

 layer_utils 

 machete_utils 

 marlin_utils 

 marlin_utils_fp4 

 marlin_utils_fp8 

 marlin_utils_test 

 mxfp4_utils 

 mxfp6_utils 

 mxfp8_utils 

 nvfp4_emulation_utils 

 nvfp4_utils 

 ocp_mx_utils 

 quant_utils 

 w8a8_utils 

 rotary_embedding 
 rotary_embedding 
 base 

 common 

 deepseek_scaling_rope 

 dual_chunk_rope 

 dynamic_ntk_alpha_rope 

 dynamic_ntk_scaling_rope 

 ernie45_vl_rope 

 fope 

 gemma4_rope 

 linear_scaling_rope 

 llama3_rope 

 llama4_vision_rope 

 mrope 

 mrope_interleaved 

 ntk_scaling_rope 

 phi3_long_rope_scaled_rope 

 telechat3_scaling_rope 

 xdrope 

 yarn_scaling_rope 

 model_loader 
 model_loader 
 base_loader 

 bitsandbytes_loader 

 default_loader 

 dummy_loader 

 ep_weight_filter 

 gguf_loader 

 runai_streamer_loader 

 sharded_state_loader 

 tensorizer 

 tensorizer_loader 

 utils 

 weight_utils 

 reload 
 reload 
 layerwise 

 meta 

 sanitize 

 torchao_decorator 

 types 

 utils 

 models 
 models 
 AXK1 

 adapters 

 afmoe 

 aimv2 

 apertus 

 arcee 

 arctic 

 aria 

 audioflamingo3 

 aya_vision 

 bagel 

 baichuan 

 bailing_moe 

 bailing_moe_linear 

 bamba 

 bee 

 bert 

 bert_with_rope 

 blip 

 blip2 

 bloom 

 chameleon 

 chatglm 

 cheers 

 clip 

 cohere2_vision 

 cohere_asr 

 colbert 

 colmodernvbert 

 colpali 

 colqwen3 

 colqwen3_5 

 commandr 

 config 

 dbrx 

 deepencoder 

 deepencoder2 

 deepseek_eagle 

 deepseek_eagle3 

 deepseek_mtp 

 deepseek_ocr 

 deepseek_ocr2 

 deepseek_v2 

 deepseek_vl2 

 dots1 

 dots_ocr 

 eagle2_5_vl 

 ernie 

 ernie45 

 ernie45_moe 

 ernie45_vl 

 ernie45_vl_moe 

 ernie_mtp 

 exaone 

 exaone4 

 exaone_moe 

 exaone_moe_mtp 

 extract_hidden_states 

 fairseq2_llama 

 falcon 

 falcon_h1 

 fireredasr2 

 flex_olmo 

 funasr 

 funaudiochat 

 fuyu 

 gemma 

 gemma2 

 gemma3 

 gemma3_mm 

 gemma3n 

 gemma3n_audio_utils 

 gemma3n_mm 

 gemma4 

 gemma4_mm 

 glm 

 glm4 

 glm4_1v 

 glm4_moe 

 glm4_moe_lite 

 glm4_moe_lite_mtp 

 glm4_moe_mtp 

 glm4v 

 glm_ocr 

 glm_ocr_mtp 

 glmasr 

 glmasr_utils 

 gpt2 

 gpt_bigcode 

 gpt_j 

 gpt_neox 

 gpt_oss 

 granite 

 granite_speech 

 granitemoe 

 granitemoehybrid 

 granitemoeshared 

 gritlm 

 grok1 

 h2ovl 

 hunyuan_v1 

 hunyuan_vision 

 hyperclovax 

 hyperclovax_vision 

 hyperclovax_vision_v2 

 idefics2_vision_model 

 idefics3 

 interfaces 

 interfaces_base 

 intern_vit 

 internlm2 

 internlm2_ve 

 interns1 

 interns1_pro 

 interns1_vit 

 internvl 

 iquest_loopcoder 

 isaac 

 jais 

 jais2 

 jamba 

 jina_vl 

 kanana_v 

 keye 

 keye_vl1_5 

 kimi_audio 

 kimi_k25 

 kimi_k25_vit 

 kimi_linear 

 kimi_vl 

 lfm2 

 lfm2_moe 

 lfm2_siglip2 

 lfm2_vl 

 lightonocr 

 llama 

 llama4 

 llama4_eagle 

 llama_eagle 

 llama_eagle3 

 llava 

 llava_next 

 llava_next_video 

 llava_onevision 

 longcat_flash 

 longcat_flash_mtp 

 mamba 

 mamba2 

 medusa 

 midashenglm 

 mimo 

 mimo_mtp 

 mimo_v2_flash 

 minicpm 

 minicpm3 

 minicpm_eagle 

 minicpmo 

 minicpmv 

 minimax_m2 

 minimax_text_01 

 minimax_vl_01 

 mistral 

 mistral3 

 mistral_large_3 

 mistral_large_3_eagle 

 mixtral 

 mllama4 

 mlp_speculator 

 modernbert 

 module_mapping 

 molmo 

 molmo2 

 moonvit 

 mpt 

 musicflamingo 

 nano_nemotron_vl 

 nemotron 

 nemotron_h 

 nemotron_h_mtp 

 nemotron_nas 

 nemotron_parse 

 nemotron_vl 

 nvlm_d 

 olmo 

 olmo2 

 olmo_hybrid 

 olmoe 

 opencua 

 openpangu 

 openpangu_mtp 

 openpangu_vl 

 opt 

 orion 

 ouro 

 ovis 

 ovis2_5 

 paddleocr_vl 

 paligemma 

 parakeet 

 param2moe 

 persimmon 

 phi 

 phi3 

 phi3v 

 phi4mm 

 phi4mm_audio 

 phi4mm_utils 

 phi4siglip 

 phimoe 

 pixtral 

 plamo2 

 plamo3 

 qwen 

 qwen2 

 qwen2_5_omni_thinker 

 qwen2_5_vl 

 qwen2_audio 

 qwen2_moe 

 qwen2_rm 

 qwen2_vl 

 qwen3 

 qwen3_5 

 qwen3_5_mtp 

 qwen3_asr 

 qwen3_asr_forced_aligner 

 qwen3_asr_realtime 

 qwen3_dflash 

 qwen3_moe 

 qwen3_next 

 qwen3_next_mtp 

 qwen3_omni_moe_thinker 

 qwen3_vl 

 qwen3_vl_moe 

 qwen_vl 

 radio 

 registry 

 roberta 

 rvl 

 sarvam 

 seed_oss 

 siglip 

 siglip2navit 

 skyworkr1v 

 smolvlm 

 solar 

 stablelm 

 starcoder2 

 step1 

 step3_text 

 step3_vl 

 step3p5 

 step3p5_mtp 

 step_vl 

 tarsier 

 telechat2 

 teleflm 

 terratorch 

 ultravox 

 utils 

 vision 

 voxtral 

 voxtral_realtime 

 voyage 

 whisper 

 whisper_causal 

 whisper_utils 

 zamba2 

 transformers 
 transformers 
 base 

 causal 

 legacy 

 moe 

 multimodal 

 pooling 

 utils 

 offloader 
 offloader 
 base 

 prefetch 

 prefetch_ops 

 uva 

 warmup 
 warmup 
 deep_gemm_warmup 

 kernel_warmup 

 multimodal 
 multimodal 
 audio 

 cache 

 encoder_budget 

 evs 

 hasher 

 image 

 inputs 

 parse 

 registry 

 utils 

 video 

 media 
 media 
 audio 

 base 

 connector 

 image 

 video 

 processing 
 processing 
 context 

 dummy_inputs 

 inputs 

 processor 

 parser 
 parser 
 abstract_parser 

 minimax_m2_parser 

 parser_manager 

 platforms 
 platforms 
 cpu 

 cuda 

 interface 

 rocm 

 tpu 

 xpu 

 zen_cpu 

 plugins 
 plugins 

 io_processors 
 io_processors 
 interface 

 lora_resolvers 
 lora_resolvers 
 filesystem_resolver 

 hf_hub_resolver 

 profiler 
 profiler 
 layerwise_profile 

 utils 

 wrapper 

 ray 
 ray 
 lazy_utils 

 ray_env 

 reasoning 
 reasoning 
 abs_reasoning_parsers 

 basic_parsers 

 deepseek_r1_reasoning_parser 

 deepseek_v3_reasoning_parser 

 ernie45_reasoning_parser 

 gemma4_reasoning_parser 

 gemma4_utils 

 gptoss_reasoning_parser 

 granite_reasoning_parser 

 hunyuan_a13b_reasoning_parser 

 identity_reasoning_parser 

 kimi_k2_reasoning_parser 

 minimax_m2_reasoning_parser 

 mistral_reasoning_parser 

 nemotron_v3_reasoning_parser 

 olmo3_reasoning_parser 

 qwen3_reasoning_parser 

 seedoss_reasoning_parser 

 step3_reasoning_parser 

 step3p5_reasoning_parser 

 renderers 
 renderers 
 base 

 deepseek_v32 

 embed_utils 

 grok2 

 hf 

 mistral 

 params 

 registry 

 terratorch 

 inputs 
 inputs 
 preprocess 

 tokenize 

 tokenizers 
 tokenizers 
 deepseek_v32 

 deepseek_v32_encoding 

 detokenizer_utils 

 grok2 

 hf 

 kimi_audio 

 mistral 

 protocol 

 qwen_vl 

 registry 

 tool_parsers 
 tool_parsers 
 abstract_tool_parser 

 deepseekv3_tool_parser 

 deepseekv31_tool_parser 

 deepseekv32_tool_parser 

 ernie45_tool_parser 

 functiongemma_tool_parser 

 gemma4_tool_parser 

 gemma4_utils 

 gigachat3_tool_parser 

 glm4_moe_tool_parser 

 glm47_moe_tool_parser 

 granite4_tool_parser 

 granite_20b_fc_tool_parser 

 granite_tool_parser 

 hermes_tool_parser 

 hunyuan_a13b_tool_parser 

 internlm2_tool_parser 

 jamba_tool_parser 

 kimi_k2_tool_parser 

 llama4_pythonic_tool_parser 

 llama_tool_parser 

 longcat_tool_parser 

 minimax_m2_tool_parser 

 minimax_tool_parser 

 mistral_tool_parser 

 olmo3_tool_parser 

 openai_tool_parser 

 phi4mini_tool_parser 

 pythonic_tool_parser 

 qwen3coder_tool_parser 

 qwen3xml_tool_parser 

 seed_oss_tool_parser 

 step3_tool_parser 

 step3p5_tool_parser 

 utils 

 xlam_tool_parser 

 tracing 
 tracing 
 otel 

 utils 

 transformers_utils 
 transformers_utils 
 config 

 config_parser_base 

 dynamic_module 

 gguf_utils 

 model_arch_config_convertor 

 processor 

 repo_utils 

 runai_utils 

 s3_utils 

 tokenizer 

 utils 

 chat_templates 
 chat_templates 
 registry 

 configs 
 configs 
 AXK1 

 afmoe 

 arctic 

 bagel 

 chatglm 

 cheers 

 colmodernvbert 

 colpali 

 colqwen3 

 deepseek_vl2 

 dotsocr 

 eagle 

 extract_hidden_states 

 falcon 

 flex_olmo 

 funaudiochat 

 hunyuan_vl 

 hyperclovax 

 isaac 

 jais 

 kimi_k25 

 kimi_linear 

 kimi_vl 

 lfm2_moe 

 medusa 

 midashenglm 

 mistral 

 mlp_speculator 

 moonvit 

 nemotron 

 nemotron_h 

 olmo_hybrid 

 ovis 

 parakeet 

 qwen3_5 

 qwen3_5_moe 

 qwen3_asr 

 qwen3_next 

 radio 

 step3_vl 

 step3p5 

 tarsier2 

 ultravox 

 speculators 
 speculators 
 algos 

 base 

 processors 
 processors 
 bagel 

 cheers 

 cohere_asr 

 deepseek_ocr 

 deepseek_vl2 

 fireredasr2 

 funasr 

 glm4v 

 h2ovl 

 hunyuan_vl 

 hunyuan_vl_image 

 internvl 

 isaac 

 kimi_audio 

 kimi_k25 

 nano_nemotron_vl 

 nemotron_vl 

 nvlm_d 

 ovis 

 ovis2_5 

 pixtral 

 qwen3_asr 

 qwen_vl 

 step3_vl 

 voxtral 

 triton_utils 
 triton_utils 
 allocation 

 importing 

 usage 
 usage 
 usage_lib 

 utils 
 utils 
 argparse_utils 

 async_utils 

 cache 

 collection_utils 

 counter 

 cpu_triton_utils 

 deep_gemm 

 flashinfer 

 func_utils 

 gc_utils 

 hashing 

 import_utils 

 jsontree 

 math_utils 

 mem_constants 

 mem_utils 

 mistral 

 multi_stream_utils 

 nccl 

 network_utils 

 numa_utils 

 nvtx_pytorch_hooks 

 ompmultiprocessing 

 platform_utils 

 print_utils 

 profiling 

 registry 

 serial_utils 

 system_utils 

 tensor_schema 

 torch_utils 

 tqdm_utils 

 v1 
 v1 
 cudagraph_dispatcher 

 kv_cache_interface 

 outputs 

 request 

 serial_utils 

 utils 

 attention 
 attention 
 backend 

 selector 

 backends 
 backends 
 cpu_attn 

 fa_utils 

 flash_attn 

 flash_attn_diffkv 

 flashinfer 

 flex_attention 

 gdn_attn 

 linear_attn 

 mamba1_attn 

 mamba2_attn 

 mamba_attn 

 registry 

 rocm_aiter_fa 

 rocm_aiter_unified_attn 

 rocm_attn 

 short_conv_attn 

 tree_attn 

 triton_attn 

 utils 

 mla 
 mla 
 aiter_triton_mla 

 cutlass_mla 

 flashattn_mla 

 flashinfer_mla 

 flashinfer_mla_sparse 

 flashmla 

 flashmla_sparse 

 indexer 

 rocm_aiter_mla 

 rocm_aiter_mla_sparse 

 sparse_utils 

 triton_mla 

 xpu_mla_sparse 

 ops 
 ops 
 chunked_prefill_paged_decode 

 common 

 dcp_alltoall 

 flashmla 

 merge_attn_states 

 paged_attn 

 prefix_prefill 

 rocm_aiter_mla_sparse 

 triton_decode_attention 

 triton_merge_attn_states 

 triton_prefill_attention 

 triton_reshape_and_cache_flash 

 triton_unified_attention 

 vit_attn_wrappers 

 xpu_mla_sparse 

 core 
 core 
 block_pool 

 encoder_cache_manager 

 kv_cache_coordinator 

 kv_cache_manager 

 kv_cache_metrics 

 kv_cache_utils 

 single_type_kv_cache_manager 

 sched 
 sched 
 async_scheduler 

 interface 

 output 

 request_queue 

 scheduler 

 utils 

 engine 
 engine 
 async_llm 

 coordinator 

 core 

 core_client 

 detokenizer 

 exceptions 

 input_processor 

 llm_engine 

 logprobs 

 output_processor 

 parallel_sampling 

 tensor_ipc 

 utils 

 executor 
 executor 
 abstract 

 multiproc_executor 

 ray_env_utils 

 ray_executor 

 ray_executor_v2 

 ray_utils 

 uniproc_executor 

 kv_offload 
 kv_offload 
 abstract 

 factory 

 mediums 

 reuse_manager 

 spec 

 cpu 
 cpu 
 manager 

 spec 

 policies 
 policies 
 abstract 

 arc 

 lru 

 worker 
 worker 
 cpu_gpu 

 worker 

 metrics 
 metrics 
 loggers 

 perf 

 prometheus 

 ray_wrappers 

 reader 

 stats 

 utils 

 pool 
 pool 
 late_interaction 

 metadata 

 sample 
 sample 
 metadata 

 rejection_sampler 

 sampler 

 logits_processor 
 logits_processor 
 builtin 

 interface 

 state 

 ops 
 ops 
 bad_words 

 logprobs 

 penalties 

 topk_topp_sampler 

 topk_topp_triton 

 simple_kv_offload 
 simple_kv_offload 
 copy_backend 

 cuda_mem_ops 

 manager 

 metadata 

 worker 

 spec_decode 
 spec_decode 
 dflash 

 draft_model 

 eagle 

 extract_hidden_states 

 medusa 

 metadata 

 metrics 

 ngram_proposer 

 ngram_proposer_gpu 

 suffix_decoding 

 utils 

 structured_output 
 structured_output 
 backend_guidance 

 backend_lm_format_enforcer 

 backend_outlines 

 backend_types 

 backend_xgrammar 

 request 

 utils 

 worker 
 worker 
 block_table 

 cp_utils 

 cpu_model_runner 

 cpu_worker 

 dp_utils 

 ec_connector_model_runner_mixin 

 encoder_cudagraph 

 encoder_cudagraph_defs 

 gpu_input_batch 

 gpu_model_runner 

 gpu_ubatch_wrapper 

 gpu_worker 

 kv_connector_model_runner_mixin 

 lora_model_runner_mixin 

 mamba_utils 

 tpu_input_batch 

 ubatch_utils 

 ubatching 

 utils 

 worker_base 

 workspace 

 xpu_model_runner 

 xpu_worker 

 gpu 
 gpu 
 async_utils 

 attn_utils 

 block_table 

 buffer_utils 

 cp_utils 

 cudagraph_utils 

 dp_utils 

 eplb_utils 

 input_batch 

 kv_connector 

 lora_utils 

 model_runner 

 pp_utils 

 states 

 structured_outputs 

 warmup 

 metrics 
 metrics 
 logits 

 mm 
 mm 
 encoder_cache 

 encoder_runner 

 rope 

 model_states 
 model_states 
 default 

 interface 

 whisper 

 pool 
 pool 
 late_interaction_runner 

 pooling_runner 

 sample 
 sample 
 bad_words 

 gumbel 

 logit_bias 

 logprob 

 min_p 

 output 

 penalties 

 prompt_logprob 

 sampler 

 states 

 spec_decode 
 spec_decode 
 probabilistic_rejection_sampler_utils 

 rejection_sampler 

 synthetic_rejection_sampler_utils 

 utils 

 eagle 
 eagle 
 cudagraph 

 eagle3_utils 

 speculator 

 utils 

 CLI Reference 
 CLI Reference 
 vllm serve 

 vllm chat 

 vllm complete 

 vllm run-batch 

 vllm bench vllm bench 
 vllm bench latency 

 vllm bench mm-processor 

 vllm bench serve 

 vllm bench sweep plot 

 vllm bench sweep plot_pareto 

 vllm bench sweep serve 

 vllm bench sweep serve_workload 

 vllm bench throughput 

 Community Community 
 Contact Us 

 Meetups 

 Sponsors 

 Governance Governance 
 Collaboration Policy 

 Committers 

 Governance Process 

 Blog 

 Forum 

 Slack 

 Table of contents 
 Files 

 Example materials 

 Home 

 User Guide 

 Getting Started 

 Examples 

 Online Serving 

Disaggregated Serving¶

Source https://github.com/vllm-project/vllm/tree/main/examples/online_serving/disaggregated_serving.

This example contains scripts that demonstrate the disaggregated serving features of vLLM.

Files¶

disagg_proxy_demo.py
 - Demonstrates XpYd (X prefill instances, Y decode instances).

kv_events.sh
 - Demonstrates KV cache event publishing.

mooncake_connector
 - A proxy demo for MooncakeConnector.

Example materials¶
disagg_proxy_demo.py

# SPDX-License-Identifier: Apache-2.0# SPDX-FileCopyrightText: Copyright contributors to the vLLM project"""This file provides a disaggregated prefilling proxy demo to demonstrate anexample usage of XpYd disaggregated prefilling.We can launch multiple vllm instances (2 for prefill and 2 for decode), andlaunch this proxy demo through: python3 examples/online_serving/disaggregated_serving/disagg_proxy_demo.py \ --model $model_name \ --prefill localhost:8100 localhost:8101 \ --decode localhost:8200 localhost:8201 \ --port 8000Note: This demo will be removed once the PDController implemented in PR 15343(https://github.com/vllm-project/vllm/pull/15343) supports XpYd."""importargparseimportipaddressimportitertoolsimportjsonimportloggingimportosimportsysfromabcimportABC,abstractmethodfromcollections.abcimportCallableimportaiohttpimportrequestsimportuvicornfromfastapiimportAPIRouter,Depends,FastAPI,Header,HTTPException,Request,statusfromfastapi.responsesimportJSONResponse,StreamingResponseAIOHTTP_TIMEOUT=aiohttp.ClientTimeout(total=6*60*60)logger=logging.getLogger()logging.basicConfig(level=logging.INFO)classSchedulingPolicy(ABC):@abstractmethoddefschedule(self,cycler:itertools.cycle):raiseNotImplementedError("Scheduling Proxy is not set.")classProxy:def__init__(self,prefill_instances:list[str],decode_instances:list[str],model:str,scheduling_policy:SchedulingPolicy,custom_create_completion:Callable[[Request],StreamingResponse]|None=None,custom_create_chat_completion:Callable[[Request],StreamingResponse]|None=None,):self.prefill_instances=prefill_instancesself.decode_instances=decode_instancesself.prefill_cycler=itertools.cycle(prefill_instances)self.decode_cycler=itertools.cycle(decode_instances)self.model=modelself.scheduling_policy=scheduling_policyself.custom_create_completion=custom_create_completionself.custom_create_chat_completion=custom_create_chat_completionself.router=APIRouter()self.setup_routes()defsetup_routes(self):self.router.post("/v1/completions",dependencies=[Depends(self.validate_json_request)])(self.custom_create_completionifself.custom_create_completionelseself.create_completion)self.router.post("/v1/chat/completions",dependencies=[Depends(self.validate_json_request)])(self.custom_create_chat_completionifself.custom_create_chat_completionelseself.create_chat_completion)self.router.get("/status",response_class=JSONResponse)(self.get_status)self.router.post("/instances/add",dependencies=[Depends(self.api_key_authenticate)])(self.add_instance_endpoint)asyncdefvalidate_json_request(self,raw_request:Request):content_type=raw_request.headers.get("content-type","").lower()ifcontent_type!="application/json":raiseHTTPException(status_code=415,detail="Unsupported Media Type: Only 'application/json' is allowed",)defapi_key_authenticate(self,x_api_key:str=Header(...)):expected_api_key=os.environ.get("ADMIN_API_KEY")ifnotexpected_api_key:logger.error("ADMIN_API_KEY is not set in the environment.")raiseHTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Server configuration error.",)ifx_api_key!=expected_api_key:logger.warning("Unauthorized access attempt with API Key: %s",x_api_key)raiseHTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Forbidden: Invalid API Key.",)asyncdefvalidate_instance(self,instance:str)->bool:url=f"http://{instance}/v1/models"try:asyncwithaiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT)asclient:logger.info("Verifying %s ...",instance)asyncwithclient.get(url)asresponse:ifresponse.status==200:data=awaitresponse.json()if"data"indataandlen(data["data"])>0:model_cur=data["data"][0].get("id","")ifmodel_cur==self.model:logger.info("Instance: %s could be added.",instance)returnTrueelse:logger.warning("Mismatch model %s : %s != %s",instance,model_cur,self.model,)returnFalseelse:returnFalseelse:returnFalseexceptaiohttp.ClientErrorase:logger.error(str(e))returnFalseexceptExceptionase:logger.error(str(e))returnFalseasyncdefadd_instance_endpoint(self,request:Request):try:data=awaitrequest.json()logger.warning(str(data))instance_type=data.get("type")instance=data.get("instance")ifinstance_typenotin["prefill","decode"]:raiseHTTPException(status_code=400,detail="Invalid instance type.")ifnotinstanceor":"notininstance:raiseHTTPException(status_code=400,detail="Invalid instance format.")host,port_str=instance.split(":")try:ifhost!="localhost":ipaddress.ip_address(host)port=int(port_str)ifnot(0<port<65536):raiseHTTPException(status_code=400,detail="Invalid port number.")exceptExceptionase:raiseHTTPException(status_code=400,detail="Invalid instance address.")fromeis_valid=awaitself.validate_instance(instance)ifnotis_valid:raiseHTTPException(status_code=400,detail="Instance validation failed.")ifinstance_type=="prefill":ifinstancenotinself.prefill_instances:self.prefill_instances.append(instance)self.prefill_cycler=itertools.cycle(self.prefill_instances)else:raiseHTTPException(status_code=400,detail="Instance already exists.")else:ifinstancenotinself.decode_instances:self.decode_instances.append(instance)self.decode_cycler=itertools.cycle(self.decode_instances)else:raiseHTTPException(status_code=400,detail="Instance already exists.")returnJSONResponse(content={"message":f"Added {instance} to {instance_type}_instances."})exceptHTTPExceptionashttp_exc:raisehttp_excexceptExceptionase:logger.error("Error in add_instance_endpoint: %s",str(e))raiseHTTPException(status_code=500,detail=str(e))fromeasyncdefforward_request(self,url,data,use_chunked=True):asyncwithaiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT)assession:headers={"Authorization":f"Bearer {os.environ.get('OPENAI_API_KEY')}"}try:asyncwithsession.post(url=url,json=data,headers=headers)asresponse:if200<=response.status<300or400<=response.status<500:ifuse_chunked:asyncforchunk_bytesinresponse.content.iter_chunked(1024):yieldchunk_byteselse:content=awaitresponse.read()yieldcontentelse:error_content=awaitresponse.text()try:error_content=json.loads(error_content)exceptjson.JSONDecodeError:error_content=error_contentlogger.error("Request failed with status %s: %s",response.status,error_content,)raiseHTTPException(status_code=response.status,detail=f"Request failed with status {response.status}: "f"{error_content}",)exceptaiohttp.ClientErrorase:logger.error("ClientError occurred: %s",str(e))raiseHTTPException(status_code=502,detail="Bad Gateway: Error communicating with upstream server.",)fromeexceptExceptionase:logger.error("Unexpected error: %s",str(e))raiseHTTPException(status_code=500,detail=str(e))fromedefschedule(self,cycler:itertools.cycle)->str:returnself.scheduling_policy.schedule(cycler)asyncdefget_status(self):status={"prefill_node_count":len(self.prefill_instances),"decode_node_count":len(self.decode_instances),"prefill_nodes":self.prefill_instances,"decode_nodes":self.decode_instances,}returnstatusasyncdefcreate_completion(self,raw_request:Request):try:request=awaitraw_request.json()kv_prepare_request=request.copy()kv_prepare_request["max_tokens"]=1prefill_instance=self.schedule(self.prefill_cycler)try:asyncfor_inself.forward_request(f"http://{prefill_instance}/v1/completions",kv_prepare_request):continueexceptHTTPExceptionashttp_exc:self.remove_instance_endpoint("prefill",prefill_instance)raisehttp_exc# Perform kv recv and decoding stagedecode_instance=self.schedule(self.decode_cycler)try:generator=self.forward_request(f"http://{decode_instance}/v1/completions",request)exceptHTTPExceptionashttp_exc:self.remove_instance_endpoint("decode",decode_instance)raisehttp_excresponse=StreamingResponse(generator)returnresponseexceptException:importsysexc_info=sys.exc_info()print("Error occurred in disagg proxy server")print(exc_info)asyncdefcreate_chat_completion(self,raw_request:Request):try:request=awaitraw_request.json()# add params to requestkv_prepare_request=request.copy()kv_prepare_request["max_tokens"]=1if"max_completion_tokens"inkv_prepare_request:kv_prepare_request["max_completion_tokens"]=1# prefill stageprefill_instance=self.schedule(self.prefill_cycler)try:asyncfor_inself.forward_request(f"http://{prefill_instance}/v1/chat/completions",kv_prepare_request):continueexceptHTTPExceptionashttp_exc:self.remove_instance_endpoint("prefill",prefill_instance)raisehttp_exc# Perform kv recv and decoding stagedecode_instance=self.schedule(self.decode_cycler)try:generator=self.forward_request("http://"+decode_instance+"/v1/chat/completions",request)exceptHTTPExceptionashttp_exc:self.remove_instance_endpoint("decode",decode_instance)raisehttp_excresponse=StreamingResponse(content=generator)returnresponseexceptException:exc_info=sys.exc_info()error_messages=[str(e)foreinexc_infoife]print("Error occurred in disagg proxy server")print(error_messages)returnStreamingResponse(content=iter(error_messages),media_type="text/event-stream")defremove_instance_endpoint(self,instance_type,instance):ifinstance_type=="decode"andinstanceinself.decode_instances:self.decode_instances.remove(instance)self.decode_cycler=itertools.cycle(self.decode_instances)ifinstance_type=="prefill"andinstanceinself.prefill_instances:self.prefill_instances.remove(instance)self.prefill_cycler=itertools.cycle(self.prefill_instances)classRoundRobinSchedulingPolicy(SchedulingPolicy):def__init__(self):super().__init__()defschedule(self,cycler:itertools.cycle)->str:returnnext(cycler)classProxyServer:def__init__(self,args:argparse.Namespace,scheduling_policy:SchedulingPolicy|None=None,create_completion:Callable[[Request],StreamingResponse]|None=None,create_chat_completion:Callable[[Request],StreamingResponse]|None=None,):self.validate_parsed_serve_args(args)self.port=args.portself.proxy_instance=Proxy(prefill_instances=[]ifargs.prefillisNoneelseargs.prefill,decode_instances=[]ifargs.decodeisNoneelseargs.decode,model=args.model,scheduling_policy=(scheduling_policyifscheduling_policyisnotNoneelseRoundRobinSchedulingPolicy()),custom_create_completion=create_completion,custom_create_chat_completion=create_chat_completion,)defvalidate_parsed_serve_args(self,args:argparse.Namespace):ifnotargs.prefill:raiseValueError("Please specify at least one prefill node.")ifnotargs.decode:raiseValueError("Please specify at least one decode node.")self.validate_instances(args.prefill)self.validate_instances(args.decode)self.verify_model_config(args.prefill,args.model)self.verify_model_config(args.decode,args.model)defvalidate_instances(self,instances:list):forinstanceininstances:iflen(instance.split(":"))!=2:raiseValueError(f"Invalid instance format: {instance}")host,port=instance.split(":")try:ifhost!="localhost":ipaddress.ip_address(host)port=int(port)ifnot(0<port<65536):raiseValueError(f"Invalid port number in instance: {instance}")exceptExceptionase:raiseValueError(f"Invalid instance {instance}: {str(e)}")fromedefverify_model_config(self,instances:list,model:str)->None:model_suffix=model.split("/")[-1]forinstanceininstances:try:response=requests.get(f"http://{instance}/v1/models")ifresponse.status_code==200:model_cur=response.json()["data"][0]["id"]model_cur_suffix=model_cur.split("/")[-1]ifmodel_cur_suffix!=model_suffix:raiseValueError(f"{instance} serves a different model: "f"{model_cur} != {model}")else:raiseValueError(f"Cannot get model id from {instance}!")exceptrequests.RequestExceptionase:raiseValueError(f"Error communicating with {instance}: {str(e)}")fromedefrun_server(self):app=FastAPI()app.include_router(self.proxy_instance.router)config=uvicorn.Config(app,port=self.port,loop="uvloop")server=uvicorn.Server(config)server.run()defparse_args():# Todo: allow more configparser=argparse.ArgumentParser("vLLM disaggregated proxy server.")parser.add_argument("--model","-m",type=str,required=True,help="Model name")parser.add_argument("--prefill","-p",type=str,nargs="+",help="List of prefill node URLs (host:port)",)parser.add_argument("--decode","-d",type=str,nargs="+",help="List of decode node URLs (host:port)",)parser.add_argument("--port",type=int,default=8000,help="Server port number",)returnparser.parse_args()if__name__=="__main__":args=parse_args()proxy_server=ProxyServer(args=args)proxy_server.run_server()

kv_events.sh

#!/bin/bash# This file demonstrates the KV cache event publishing# We will launch a vllm instances configured to publish KV cache# events and launch a simple subscriber to log those events.set-xe
echo"🚧🚧 Warning: The usage of KV cache events is experimental and subject to change 🚧🚧"sleep1MODEL_NAME=${HF_MODEL_NAME:-meta-llama/Meta-Llama-3.1-8B-Instruct}# Trap the SIGINT signal (triggered by Ctrl+C)trap'cleanup'INT
# Cleanup functioncleanup(){echo"Caught Ctrl+C, cleaning up..."# Cleanup commandspgreppython|xargskill-9
pkill-fpython
echo"Cleanup complete. Exiting."exit0}exportVLLM_HOST_IP=$(hostname-I|awk'{print $1}')# a function that waits vLLM server to startwait_for_server(){localport=$1timeout1200bash-c" until curl -s localhost:${port}/v1/completions > /dev/null; do sleep 1 done"&&return0||return1}vllmserve"$MODEL_NAME"\--port8100\--max-model-len100\--enforce-eager\--gpu-memory-utilization0.8\--trust-remote-code\--kv-events-config\'{"enable_kv_cache_events": true, "publisher": "zmq", "topic": "kv-events"}'&wait_for_server8100SCRIPT_DIR="$(cd"$(dirname"${BASH_SOURCE[0]}")"&&pwd)"python3"$SCRIPT_DIR/kv_events_subscriber.py"&sleep1# serve two example requestsoutput1=$(curl-XPOST-shttp://localhost:8100/v1/completions\-H"Content-Type: application/json"\-d'{"model": "'"$MODEL_NAME"'","prompt": "Explain quantum computing in simple terms a 5-year-old could understand.","max_tokens": 80,"temperature": 0}')output2=$(curl-XPOST-shttp://localhost:8100/v1/completions\-H"Content-Type: application/json"\-d'{"model": "'"$MODEL_NAME"'","prompt": "Explain quantum computing in simple terms a 50-year-old could understand.","max_tokens": 80,"temperature": 0}')# Cleanup commandspkill-9-u"$USER"-fpython
pkill-9-u"$USER"-fvllm
sleep1echo"Cleaned up"# Print the outputs of the curl requestsecho""echo"Output of first request: $output1"echo"Output of second request: $output2"echo"🎉🎉 Successfully finished 2 test requests! 🎉🎉"echo""

mooncake_connector/mooncake_connector_proxy.py

# SPDX-License-Identifier: Apache-2.0# SPDX-FileCopyrightText: Copyright contributors to the vLLM projectimportargparseimportasyncioimportipaddressimportitertoolsimportosimporturllibimportuuidfromcontextlibimportasynccontextmanagerfromtypingimportAnyimporthttpxfromfastapiimportFastAPI,HTTPException,Requestfromfastapi.responsesimportStreamingResponsedefmaybe_wrap_ipv6_address(address:str)->str:try:ipaddress.IPv6Address(address)returnf"[{address}]"exceptValueError:returnaddressdefmake_http_path(host:str,port:int)->str:returnf"http://{host}:{port}"defprefiller_cycle(prefill_clients:list[Any]):whileTrue:forprefill_clientinprefill_clients:foriinrange(prefill_client["dp_size"]):yieldprefill_client,iasyncdefget_prefiller_info(prefill_clients:list,ready:asyncio.Event):forprefill_clientinprefill_clients:whileTrue:try:# Wait for prefill service to be readyresponse=awaitprefill_client["client"].get("/health")response.raise_for_status()exceptException:awaitasyncio.sleep(1)continueresponse=awaitprefill_client["client"].get(prefill_client["bootstrap_addr"]+"/query")response.raise_for_status()data=response.json()breakfordp_rank,dp_entryindata.items():prefill_client["dp_engine_id"][int(dp_rank)]=dp_entry["engine_id"]dp_size=len(data)prefill_client["dp_size"]=dp_sizeprint(f"Inited prefiller {prefill_client['url']} with dp_size={dp_size}")ready.set()print("All prefiller instances are ready.")@asynccontextmanagerasyncdeflifespan(app:FastAPI):""" Lifespan context manager to handle startup and shutdown events. """# Startup: Initialize client pools for prefiller and decoder servicesapp.state.prefill_clients=[]app.state.decode_clients=[]app.state.ready=asyncio.Event()# Create prefill clientsfori,(url,bootstrap_port)inenumerate(global_args.prefill):parsed_url=urllib.parse.urlparse(url)hostname=maybe_wrap_ipv6_address(parsed_url.hostname)app.state.prefill_clients.append({"client":httpx.AsyncClient(timeout=None,base_url=url,limits=httpx.Limits(max_connections=None,max_keepalive_connections=None,),),"url":url,"bootstrap_addr":make_http_path(hostname,bootstrap_portor8998),"dp_engine_id":{},})# Create decode clientsfori,urlinenumerate(global_args.decode):parsed_url=urllib.parse.urlparse(url)hostname=maybe_wrap_ipv6_address(parsed_url.hostname)app.state.decode_clients.append({"client":httpx.AsyncClient(timeout=None,base_url=url,limits=httpx.Limits(max_connections=None,max_keepalive_connections=None,),),})asyncio.create_task(get_prefiller_info(app.state.prefill_clients,app.state.ready))# Initialize round-robin iteratorsapp.state.prefill_iterator=prefiller_cycle(app.state.prefill_clients)app.state.decode_iterator=itertools.cycle(range(len(app.state.decode_clients)))print(f"Got {len(app.state.prefill_clients)} prefill clients "f"and {len(app.state.decode_clients)} decode clients.")yield# Shutdown: Close all clientsforclient_infoinapp.state.prefill_clients:awaitclient_info["client"].aclose()forclient_infoinapp.state.decode_clients:awaitclient_info["client"].aclose()# Update FastAPI app initialization to use lifespanapp=FastAPI(lifespan=lifespan)defparse_args():parser=argparse.ArgumentParser()parser.add_argument("--port",type=int,default=8000)# Always use 127.0.0.1 as localhost binds to IPv6 which is blocked on CIparser.add_argument("--host",type=str,default="127.0.0.1")# For prefiller instancesparser.add_argument("--prefill",nargs="+",action="append",dest="prefill_raw",metavar=("URL","bootstrap_port"),help=("Prefill server URL and optional bootstrap port. ""Can be specified multiple times. ""Format: --prefill URL [BOOTSTRAP_PORT]. ""BOOTSTRAP_PORT can be a port number, ""'none', or omitted (defaults to none)."),)# For decoder instancesparser.add_argument("--decode",nargs=1,action="append",dest="decode_raw",metavar=("URL",),help="Decode server URL. Can be specified multiple times.",)args=parser.parse_args()args.prefill=_parse_prefill_urls(args.prefill_raw)args.decode=_parse_decode_urls(args.decode_raw)returnargs# From sglang router_args.pydef_parse_prefill_urls(prefill_list):"""Parse prefill URLs from --prefill arguments. Format: --prefill URL [BOOTSTRAP_PORT] Example: --prefill http://prefill1:8080 9000 # With bootstrap port --prefill http://prefill2:8080 none # Explicitly no bootstrap port --prefill http://prefill3:8080 # Defaults to no bootstrap port """ifnotprefill_list:return[]prefill_urls=[]forprefill_argsinprefill_list:url=prefill_args[0]# Handle optional bootstrap portiflen(prefill_args)>=2:bootstrap_port_str=prefill_args[1]# Handle 'none' as Noneifbootstrap_port_str.lower()=="none":bootstrap_port=Noneelse:try:bootstrap_port=int(bootstrap_port_str)exceptValueErrorase:raiseValueError(f"Invalid bootstrap port: {bootstrap_port_str}. Must be a number or 'none'"# noqa: E501)fromeelse:# No bootstrap port specified, default to Nonebootstrap_port=Noneprefill_urls.append((url,bootstrap_port))returnprefill_urlsdef_parse_decode_urls(decode_list):"""Parse decode URLs from --decode arguments. Format: --decode URL Example: --decode http://decode1:8081 --decode http://decode2:8081 """ifnotdecode_list:return[]# decode_list is a list of single-element lists due to nargs=1return[url[0]forurlindecode_list]defget_next_client(app,service_type:str):""" Get the next client in round-robin fashion. Args: app: The FastAPI app instance service_type: Either 'prefill' or 'decode' Returns: The next client to use """ifservice_type=="prefill":returnnext(app.state.prefill_iterator)elifservice_type=="decode":client_idx=next(app.state.decode_iterator)returnapp.state.decode_clients[client_idx]else:raiseValueError(f"Unknown service type: {service_type}")asyncdefsend_request_to_service(client_info:dict,dp_rank:int,endpoint:str,req_data:dict,request_id:str):""" Send a request to a service using a client from the pool. """req_data=req_data.copy()req_data["kv_transfer_params"]={"do_remote_decode":True,"do_remote_prefill":False,"transfer_id":f"xfer-{request_id}",}req_data["stream"]=Falsereq_data["max_tokens"]=1if"max_completion_tokens"inreq_data:req_data["max_completion_tokens"]=1if"stream_options"inreq_data:delreq_data["stream_options"]headers={"Authorization":f"Bearer {os.environ.get('OPENAI_API_KEY')}","X-Request-Id":request_id,"X-data-parallel-rank":str(dp_rank),}response=awaitclient_info["client"].post(endpoint,json=req_data,headers=headers)response.raise_for_status()# CRITICAL: Release connection back to poolawaitresponse.aclose()asyncdefstream_service_response(prefill_client_info:dict,prefill_dp_rank:int,decode_client_info:dict,endpoint:str,req_data:dict,request_id:str,):""" Asynchronously stream response from a service using a client from the pool. """headers={"Authorization":f"Bearer {os.environ.get('OPENAI_API_KEY')}","X-Request-Id":request_id,}req_data["kv_transfer_params"]={"do_remote_decode":False,"do_remote_prefill":True,"remote_bootstrap_addr":prefill_client_info["bootstrap_addr"],"remote_engine_id":prefill_client_info["dp_engine_id"][prefill_dp_rank],"transfer_id":f"xfer-{request_id}",}asyncwithdecode_client_info["client"].stream("POST",endpoint,json=req_data,headers=headers)asresponse:response.raise_for_status()asyncforchunkinresponse.aiter_bytes():yieldchunkasyncdef_handle_completions(api:str,request:Request):ifnotapp.state.ready.is_set():raiseHTTPException(status_code=503,detail="Service Unavailable")try:req_data=awaitrequest.json()request_id=str(uuid.uuid4())# Get the next prefill client in round-robin fashionprefill_client_info,prefill_dp_rank=get_next_client(request.app,"prefill")# Send request to prefill serviceasyncio.create_task(send_request_to_service(prefill_client_info,prefill_dp_rank,api,req_data,request_id))decode_client_info=get_next_client(request.app,"decode")# Stream response from decode serviceasyncdefgenerate_stream():asyncforchunkinstream_service_response(prefill_client_info,prefill_dp_rank,decode_client_info,api,req_data,request_id=request_id,):yieldchunkreturnStreamingResponse(generate_stream(),media_type="application/json")exceptExceptionase:importsysimporttracebackexc_info=sys.exc_info()print(f"Error occurred in disagg prefill proxy server - {api} endpoint")print(e)print("".join(traceback.format_exception(*exc_info)))raise@app.post("/v1/completions")asyncdefhandle_completions(request:Request):returnawait_handle_completions("/v1/completions",request)@app.post("/v1/chat/completions")asyncdefhandle_chat_completions(request:Request):returnawait_handle_completions("/v1/chat/completions",request)if__name__=="__main__":globalglobal_argsglobal_args=parse_args()importuvicornuvicorn.run(app,host=global_args.host,port=global_args.port)

mooncake_connector/run_mooncake_connector.sh

#!/bin/bash# =============================================================================# vLLM Disaggregated Serving Script for Mooncake Connector# =============================================================================# This script demonstrates disaggregated prefill and decode serving using# Mooncake Connector.## Configuration can be customized via environment variables:# MODEL: Model to serve# PREFILL_GPUS: Comma-separated GPU IDs for prefill servers# DECODE_GPUS: Comma-separated GPU IDs for decode servers# PREFILL_PORTS: Comma-separated ports for prefill servers# BOOTSTRAP_PORTS: Bootstrap server port launched by prefill servers# DECODE_PORTS: Comma-separated ports for decode servers# PROXY_PORT: Proxy server port used to setup P/D disaggregated connection.# TIMEOUT_SECONDS: Server startup timeout# =============================================================================# Configuration - can be overridden via environment variablesMODEL=${MODEL:-Qwen/Qwen2.5-7B-Instruct}TIMEOUT_SECONDS=${TIMEOUT_SECONDS:-1200}PROXY_PORT=${PROXY_PORT:-8000}PREFILL_GPUS=${PREFILL_GPUS:-0}DECODE_GPUS=${DECODE_GPUS:-1}PREFILL_PORTS=${PREFILL_PORTS:-8010}BOOTSTRAP_PORTS=${BOOTSTRAP_PORTS:-8998}DECODE_PORTS=${DECODE_PORTS:-8020}echo"Warning: Mooncake Connector support for vLLM v1 is experimental and subject to change."echo""echo"Architecture Configuration:"echo" Model: $MODEL"echo" Prefill GPUs: $PREFILL_GPUS, Ports: $PREFILL_PORTS, Bootstrap Port:$BOOTSTRAP_PORTS"echo" Decode GPUs: $DECODE_GPUS, Ports: $DECODE_PORTS"echo" Proxy Port: $PROXY_PORT"echo" Timeout: ${TIMEOUT_SECONDS}s"echo""PIDS=()# Switch to the directory of the current scriptcd"$(dirname"${BASH_SOURCE[0]}")"check_required_files(){localfiles=("mooncake_connector_proxy.py")forfilein"${files[@]}";doif[[!-f"$file"]];thenecho"Required file $file not found in $(pwd)"exit1fidone}check_hf_token(){if[-z"$HF_TOKEN"];thenecho"HF_TOKEN is not set. Please set it to your Hugging Face token."echo"Example: export HF_TOKEN=your_token_here"exit1fiif[["$HF_TOKEN"!=hf_*]];thenecho"HF_TOKEN is not a valid Hugging Face token. Please set it to your Hugging Face token."exit1fiecho"HF_TOKEN is set and valid."}check_num_gpus(){# Check if the number of GPUs are >=2 via nvidia-sminum_gpus=$(nvidia-smi--query-gpu=name--format=csv,noheader|wc-l)if["$num_gpus"-lt2];thenecho"You need at least 2 GPUs to run disaggregated prefill."exit1elseecho"Found $num_gpus GPUs."fi}ensure_python_library_installed(){echo"Checking if $1 is installed..."if!python3-c"import $1">/dev/null2>&1;thenecho"$1 is not installed. Please install it via pip install $1."exit1elseecho"$1 is installed."fi}cleanup(){echo"Stopping everything…"trap-INTTERM# prevent re-entrancypkill-9-f"mooncake_connector_proxy.py"kill---$$# negative PID == "this whole process-group"wait# reap children so we don't leave zombiesexit0}wait_for_server(){localport=$1localtimeout_seconds=$TIMEOUT_SECONDSlocalstart_time=$(date+%s)echo"Waiting for server on port $port..."whiletrue;doifcurl-s"localhost:${port}/v1/completions">/dev/null;thenecho"Server on port $port is ready."return0filocalnow=$(date+%s)if((now-start_time>=timeout_seconds));thenecho"Timeout waiting for server on port $port"return1fisleep1done}main(){check_required_files
check_hf_token
check_num_gpus
ensure_python_library_installedvllm
ensure_python_library_installedmooncake.engine
trapcleanupINT
trapcleanupUSR1
trapcleanupTERM
echo"Launching disaggregated serving components..."echo"Please check the log files for detailed output:"echo" - prefill*.log: Prefill server logs"echo" - decode*.log: Decode server logs"echo" - proxy.log: Proxy server log"# Parse GPU and port arraysIFS=','read-raPREFILL_GPU_ARRAY<<<"$PREFILL_GPUS"IFS=','read-raDECODE_GPU_ARRAY<<<"$DECODE_GPUS"IFS=','read-raPREFILL_PORT_ARRAY<<<"$PREFILL_PORTS"IFS=','read-raBOOTSTRAP_PORT_ARRAY<<<"$BOOTSTRAP_PORTS"IFS=','read-raDECODE_PORT_ARRAY<<<"$DECODE_PORTS"proxy_args=()# =============================================================================# Launch Prefill Servers (X Producers)# =============================================================================echo""echo"Starting

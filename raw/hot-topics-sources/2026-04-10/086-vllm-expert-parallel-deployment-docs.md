---
title: Expert Parallel Deployment - vLLM
source_url: https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment
final_url: https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/
status: 200
content_type: text/html; charset=utf-8
topics: [Wide Expert Parallelism (WideEP) for MoE, Wide Expert Parallelism (Wide-EP) for MoE]
sections: [Inference Optimization, Infra & Serving]
fetched_at: 2026-04-10T01:43:38.244351+00:00
---

# Expert Parallel Deployment - vLLM

## 원본 URL

https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment

## 추출 본문

Expert Parallel Deployment - vLLM
 Skip to content 

You are viewing the latest developer preview docs. Click here to view docs for the latest stable release.

 vLLM 

 Expert Parallel Deployment 

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

 Disaggregated Serving 

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

 Expert Parallel Deployment Expert Parallel Deployment Table of contents 
 Prerequisites 
 Backend Selection Guide 

 Single Node Deployment 
 Configuration 

 Layer Behavior with EP Enabled 

 Example Command 

 Multi-Node Deployment 
 Deployment Steps 

 Example: 2-Node Deployment 

 Key Configuration Notes 

 Network Configuration 

 Expert Parallel Load Balancer (EPLB) 
 Configuration 

 EPLB Parameters 

 Expert Distribution Formula 

 Memory Footprint Overhead 

 Example Command 

 Advanced Configuration 
 Performance Optimization 

 Troubleshooting 

 Benchmarking 

 Disaggregated Serving (Prefill/Decode Split) 
 Architecture Overview 

 Setup Steps 

 Client Orchestration Example 

 Benchmarking 

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
 Prerequisites 
 Backend Selection Guide 

 Single Node Deployment 
 Configuration 

 Layer Behavior with EP Enabled 

 Example Command 

 Multi-Node Deployment 
 Deployment Steps 

 Example: 2-Node Deployment 

 Key Configuration Notes 

 Network Configuration 

 Expert Parallel Load Balancer (EPLB) 
 Configuration 

 EPLB Parameters 

 Expert Distribution Formula 

 Memory Footprint Overhead 

 Example Command 

 Advanced Configuration 
 Performance Optimization 

 Troubleshooting 

 Benchmarking 

 Disaggregated Serving (Prefill/Decode Split) 
 Architecture Overview 

 Setup Steps 

 Client Orchestration Example 

 Benchmarking 

 Home 

 User Guide 

 Inference and Serving 

Expert Parallel Deployment¶

vLLM supports Expert Parallelism (EP), which allows experts in Mixture-of-Experts (MoE) models to be deployed on separate GPUs, increasing locality, efficiency, and throughput overall.

EP is typically coupled with Data Parallelism (DP). While DP can be used independently of EP, EP is more efficient when used in conjunction with DP. You can read more about data parallelism here.

Prerequisites¶

Before using EP, you need to install the necessary dependencies. We are actively working on making this easier in the future:

Install DeepEP: Set up host environment following vLLM's guide for EP kernels here.

Install DeepGEMM library: Follow the official instructions.

For disaggregated serving: Install 
gdrcopy
 by running the 
install_gdrcopy.sh
 script (e.g., 
install_gdrcopy.sh "${GDRCOPY_OS_VERSION}" "12.8" "x64"
). You can find available OS versions here.

Backend Selection Guide¶

vLLM provides multiple communication backends for EP. Use 
--all2all-backend
 to select one:
BackendUse CaseFeaturesBest For
allgather_reducescatter
Default backendStandard all2all using allgather/reducescatter primitivesGeneral purpose, works with any EP+DP configuration
deepep_high_throughput
Multi-node prefillGrouped GEMM with continuous layout, optimized for prefillPrefill-dominated workloads, high-throughput scenarios
deepep_low_latency
Multi-node decodeCUDA graph support, masked layout, optimized for decodeDecode-dominated workloads, low-latency scenarios
flashinfer_nvlink_one_sided
MNNVL systemsFlashInfer's one-sided A2A strategy for multi-node NVLinkHigh-throughput workloads
flashinfer_nvlink_two_sided
MNNVL systemsFlashInfer's two-sided A2A strategy for multi-node NVLinkSystems with NVLink across nodes
Single Node Deployment¶

Warning

EP is an experimental feature. Argument names and default values may change in the future.

Configuration¶

Enable EP by setting the 
--enable-expert-parallel
 flag. The EP size is automatically calculated as:

EP_SIZE = TP_SIZE × DP_SIZE

Where:

TP_SIZE
: Tensor parallel size

DP_SIZE
: Data parallel size

EP_SIZE
: Expert parallel size (computed automatically)

Layer Behavior with EP Enabled¶

When EP is enabled, different layers in MoE models behave differently:
Layer TypeBehaviorParallelism UsedExpert (MoE) LayersSharded across all EP ranksExpert Parallel (EP) of size 
TP × DP
Attention LayersBehavior depends on TP sizeSee below
Attention layer parallelism:

When 
TP = 1
: Attention weights are replicated across all DP ranks (data parallelism)

When 
TP > 1
: Attention weights are sharded using tensor parallelism across TP ranks within each DP group

For example, with 
TP=2, DP=4
 (8 GPUs total):

Expert layers form an EP group of size 8, with experts distributed across all GPUs

Attention layers use TP=2 within each of the 4 DP groups

Key Difference from Data Parallel Deployment

Without 
--enable-expert-parallel
, MoE layers would use tensor parallelism (forming a TP group of size 
TP × DP
), similar to dense models. With EP enabled, expert layers switch to expert parallelism, which can provide better efficiency and locality for MoE models.

Example Command¶

The following command serves a 
DeepSeek-V3-0324
 model with 1-way tensor parallel, 8-way (attention) data parallel, and 8-way expert parallel. The attention weights are replicated across all GPUs, while the expert weights are split across GPUs. It will work on a H200 (or H20) node with 8 GPUs. For H100, you can try to serve a smaller model or refer to the multi-node deployment section.

# Single node EP deploymentvllmservedeepseek-ai/DeepSeek-V3-0324\--tensor-parallel-size1\ # Tensor parallelism across 1 GPU--data-parallel-size8\ # Data parallelism across 8 processes--enable-expert-parallel# Enable expert parallelism

Multi-Node Deployment¶

For multi-node deployment, use the DeepEP communication kernel with one of two modes (see Backend Selection Guide above).

Deployment Steps¶

Run one command per node - Each node requires its own launch command

Configure networking - Ensure proper IP addresses and port configurations

Set node roles - First node handles requests, additional nodes run in headless mode

Example: 2-Node Deployment¶

The following example deploys 
DeepSeek-V3-0324
 across 2 nodes using 
deepep_low_latency
 mode:

# Node 1 (Primary - handles incoming requests)vllmservedeepseek-ai/DeepSeek-V3-0324\--all2all-backenddeepep_low_latency\--tensor-parallel-size1\ # TP size per node--enable-expert-parallel\ # Enable EP--data-parallel-size16\ # Total DP size across all nodes--data-parallel-size-local8\ # Local DP size on this node (8 GPUs per node)--data-parallel-address192.168.1.100\ # Replace with actual IP of Node 1--data-parallel-rpc-port13345\ # RPC communication port, can be any port as long as reachable by all nodes--api-server-count=8# Number of API servers for load handling (scaling this out to # local ranks is recommended)# Node 2 (Secondary - headless mode, no API server)vllmservedeepseek-ai/DeepSeek-V3-0324\--all2all-backenddeepep_low_latency\--tensor-parallel-size1\ # TP size per node--enable-expert-parallel\ # Enable EP--data-parallel-size16\ # Total DP size across all nodes--data-parallel-size-local8\ # Local DP size on this node--data-parallel-start-rank8\ # Starting rank offset for this node--data-parallel-address192.168.1.100\ # IP of primary node (Node 1)--data-parallel-rpc-port13345\ # Same RPC port as primary--headless# No API server, worker only

Key Configuration Notes¶

Headless mode: Secondary nodes run with 
--headless
 flag, meaning all client requests are handled by the primary node

Rank calculation: 
--data-parallel-start-rank
 should equal the cumulative local DP size of previous nodes

Load scaling: Adjust 
--api-server-count
 on the primary node to handle higher request loads

Network Configuration¶

InfiniBand Clusters

On InfiniBand networked clusters, set this environment variable to prevent initialization hangs: 

exportGLOO_SOCKET_IFNAME=eth0

 This ensures torch distributed group discovery uses Ethernet instead of InfiniBand for initial setup.

Expert Parallel Load Balancer (EPLB)¶

While MoE models are typically trained so that each expert receives a similar number of tokens, in practice the distribution of tokens across experts can be highly skewed. vLLM provides an Expert Parallel Load Balancer (EPLB) to redistribute expert mappings across EP ranks, evening the load across experts.

Configuration¶

Enable EPLB with the 
--enable-eplb
 flag.

When enabled, vLLM collects load statistics with every forward pass and periodically rebalances expert distribution.

EPLB Parameters¶

Configure EPLB with the 
--eplb-config
 argument, which accepts a JSON string. The available keys and their descriptions are:
ParameterDescriptionDefault
window_size
Number of engine steps to track for rebalancing decisions1000
step_interval
Frequency of rebalancing (every N engine steps)3000
log_balancedness
Log balancedness metrics (avg tokens per expert ÷ max tokens per expert)
false

num_redundant_experts
Additional global experts per EP rank beyond equal distribution
0

use_async
Use non-blocking EPLB for reduced latency overhead
false

policy
The policy type for expert parallel load balancing
"default"

For example:

vllmserveQwen/Qwen3-30B-A3B\--enable-eplb\--eplb-config'{"window_size":1000,"step_interval":3000,"num_redundant_experts":2,"log_balancedness":true}'

Prefer individual arguments instead of JSON?

vllmserveQwen/Qwen3-30B-A3B\--enable-eplb\--eplb-config.window_size1000\--eplb-config.step_interval3000\--eplb-config.num_redundant_experts2\--eplb-config.log_balancednesstrue

Expert Distribution Formula¶

Default: Each EP rank has 
NUM_TOTAL_EXPERTS ÷ NUM_EP_RANKS
 experts

With redundancy: Each EP rank has 
(NUM_TOTAL_EXPERTS + NUM_REDUNDANT_EXPERTS) ÷ NUM_EP_RANKS
 experts

Memory Footprint Overhead¶

EPLB uses redundant experts that need to fit in GPU memory. This means that EPLB may not be a good fit for memory constrained environments or when KV cache space is at a premium.

This overhead equals 
NUM_MOE_LAYERS * BYTES_PER_EXPERT * (NUM_TOTAL_EXPERTS + NUM_REDUNDANT_EXPERTS) ÷ NUM_EP_RANKS
. For DeepSeekV3, this is approximately 
2.4 GB
 for one redundant expert per EP rank.

Example Command¶

Single node deployment with EPLB enabled:

# Single node with EPLB load balancingvllmservedeepseek-ai/DeepSeek-V3-0324\--tensor-parallel-size1\ # Tensor parallelism--data-parallel-size8\ # Data parallelism--enable-expert-parallel\ # Enable EP--enable-eplb\ # Enable load balancer--eplb-config'{"window_size":1000,"step_interval":3000,"num_redundant_experts":2,"log_balancedness":true}'

For multi-node deployment, add these EPLB flags to each node's command. We recommend setting 
--eplb-config '{"num_redundant_experts":32}'
 to 32 in large scale use cases so the most popular experts are always available.

Advanced Configuration¶

Performance Optimization¶

DeepEP kernels: The 
high_throughput
 and 
low_latency
 kernels are optimized for disaggregated serving and may show poor performance for mixed workloads

Dual Batch Overlap: Use 
--enable-dbo
 to overlap all-to-all communication with compute. See Dual Batch Overlap for more details.

Async scheduling (experimental): Try 
--async-scheduling
 to overlap scheduling with model execution.

Troubleshooting¶

non-zero status: 7 cannot register cq buf
: When using Infiniband/RoCE, make sure host VM and pods show 
ulimit -l
 "unlimited".

init failed for transport: IBGDA
: The InfiniBand GDA kernel modules are missing. Run 
tools/ep_kernels/configure_system_drivers.sh
 on each GPU node and reboot. Also fixes error 
NVSHMEM API called before NVSHMEM initialization has completed
.

NVSHMEM peer disconnect: Usually a networking misconfiguration. If deploying via Kubernetes, verify that every pod runs with 
hostNetwork: true
, 
securityContext.privileged: true
 to access Infiniband.

Benchmarking¶

Use simulator flags 
VLLM_MOE_ROUTING_SIMULATION_STRATEGY=uniform_random
 and 
VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1
 so token routing is balanced across EP ranks.

Increasing 
VLLM_MOE_DP_CHUNK_SIZE
 may increase throughput by increasing the maximum batch size for inter-rank token transfers. This may cause DeepEP to throw 
assert self.nvshmem_qp_depth >= (num_max_dispatch_tokens_per_rank + 1) * 2
, which can be fixed by increasing environment variable 
NVSHMEM_QP_DEPTH
.

Disaggregated Serving (Prefill/Decode Split)¶

For production deployments requiring strict SLA guarantees for time-to-first-token and inter-token latency, disaggregated serving allows independent scaling of prefill and decode operations.

Architecture Overview¶

Prefill Instance: Uses 
deepep_high_throughput
 backend for optimal prefill performance

Decode Instance: Uses 
deepep_low_latency
 backend for minimal decode latency 

KV Cache Transfer: Connects instances via NIXL or other KV connectors

Setup Steps¶

Install gdrcopy/ucx/nixl: For maximum performance, run the install_gdrcopy.sh script to install 
gdrcopy
 (e.g., 
install_gdrcopy.sh "${GDRCOPY_OS_VERSION}" "12.8" "x64"
). You can find available OS versions here. If 
gdrcopy
 is not installed, things will still work with a plain 
pip install nixl
, just with lower performance. 
nixl
 and 
ucx
 are installed as dependencies via pip. For non-cuda platform to install nixl with non-cuda UCX build, run the install_nixl_from_source_ubuntu.py script.

Configure Both Instances: Add this flag to both prefill and decode instances 
--kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}
. Noted, you may also specify one or multiple NIXL_Backend. Such as: 
--kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both", "kv_connector_extra_config":{"backends":["UCX", "GDS"]}}'

Client Orchestration: Use the client-side script below to coordinate prefill/decode operations. We are actively working on routing solutions.

Client Orchestration Example¶

fromopenaiimportOpenAIimportuuidtry:# 1: Set up clients for prefill and decode instancesopenai_api_key="EMPTY"# vLLM doesn't require a real API key# Replace these IP addresses with your actual instance addressesprefill_client=OpenAI(api_key=openai_api_key,base_url="http://192.168.1.100:8000/v1",# Prefill instance URL)decode_client=OpenAI(api_key=openai_api_key,base_url="http://192.168.1.101:8001/v1",# Decode instance URL )# Get model name from prefill instancemodels=prefill_client.models.list()model=models.data[0].idprint(f"Using model: {model}")# 2: Prefill Phase# Generate unique request ID to link prefill and decode operationsrequest_id=str(uuid.uuid4())print(f"Request ID: {request_id}")prefill_response=prefill_client.completions.create(model=model,# Prompt must exceed vLLM's block size (16 tokens) for PD to workprompt="Write a detailed explanation of Paged Attention for Transformers works including the management of KV cache for multi-turn conversations",max_tokens=1,# Force prefill-only operationextra_body={"kv_transfer_params":{"do_remote_decode":True,# Enable remote decode"do_remote_prefill":False,# This is the prefill instance"remote_engine_id":None,# Will be populated by vLLM"remote_block_ids":None,# Will be populated by vLLM"remote_host":None,# Will be populated by vLLM"remote_port":None,# Will be populated by vLLM}},extra_headers={"X-Request-Id":request_id},)print("-"*50)print("✓ Prefill completed successfully")print(f"Prefill response: {prefill_response.choices[0].text}")# 3: Decode Phase# Transfer KV cache parameters from prefill to decode instancedecode_response=decode_client.completions.create(model=model,prompt="This prompt is ignored during decode",# Original prompt not neededmax_tokens=150,# Generate up to 150 tokensextra_body={"kv_transfer_params":prefill_response.kv_transfer_params# Pass KV cache info},extra_headers={"X-Request-Id":request_id},# Same request ID)print("-"*50)print("✓ Decode completed successfully")print(f"Final response: {decode_response.choices[0].text}")exceptExceptionase:print(f"❌ Error during disaggregated serving: {e}")print("Check that both prefill and decode instances are running and accessible")

Benchmarking¶

To simulate the decode deployment of disaggregated serving, pass 
--kv-transfer-config '{"kv_connector":"DecodeBenchConnector","kv_role":"kv_both"}'
 to the 
vllm serve
 invocation. The connector populates KV cache with random values so decode can be profiled in isolation.

CUDAGraph capture: Use 
--compilation_config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'
 to enable CUDA graph capture for decode only and save KV cache.

March 19, 2026

 Back to top 

 Made with Material for MkDocs

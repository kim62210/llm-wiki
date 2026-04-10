---
title: Releases · vllm-project/vllm · GitHub
source_url: https://github.com/vllm-project/vllm/releases
final_url: https://github.com/vllm-project/vllm/releases
status: 200
content_type: text/html; charset=utf-8
topics: [vLLM V1 Engine on Blackwell (GB200/GB300)]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:09.134353+00:00
---

# Releases · vllm-project/vllm · GitHub

## 원본 URL

https://github.com/vllm-project/vllm/releases

## 추출 본문

Releases · vllm-project/vllm · GitHub

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

 vllm-project
/vllmPublic

 Uh oh!

There was an error while loading. Please reload this page.

Notifications
You must be signed in to change notification settings

Fork
 15.4k

 Star
75.9k

Code

Issues1.9k

Pull requests2.4k

Discussions

Actions

Projects

Security and quality39

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Security and quality

 Insights

Releases: vllm-project/vllm

ReleasesTags

Releases · vllm-project/vllm

v0.19.0

 03 Apr 02:19
 

khluu

 v0.19.0
 

2a69949

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.19.0Latest

Latest

vLLM v0.19.0

Highlights

This release features 448 commits from 197 contributors (54 new)!

Gemma 4 support: Full Google Gemma 4 architecture support including MoE, multimodal, reasoning, and tool-use capabilities (#38826, #38847). Requires 
transformers>=5.5.0
. We recommend using pre-built docker image 
vllm/vllm-openai:gemma4
 for out of box usage.

Zero-bubble async scheduling + speculative decoding: Async scheduling now supports speculative decoding with zero-bubble overlap, significantly improving throughput (#32951).

Model Runner V2 maturation: MRV2 gains piecewise CUDA graphs for pipeline parallelism (#35162), spec decode rejection sampler with greedy/logprobs support (#37238, #37237), multi-modal embeddings for spec decode (#36097), streaming inputs (#37028), and EPLB support (#37488).

ViT Full CUDA Graphs: Vision encoders (ViT) now support full CUDA graph capture for reduced overhead (#35963).

General CPU KV cache offloading: A simple yet general CPU KV cache offloading mechanism for V1, with pluggable cache policy and block-level preemption handling (#37160, #37874, #34805, #36642, #37853).

DBO (Dual-Batch Overlap) generalization: The microbatch optimization (DBO) now works with general models, not just specific architectures (#37926).

NVIDIA B300/GB300 (SM 10.3) support: Allreduce fusion enabled by default with tuned all-reduce communicator (#37755, #37756).

Transformers v5 compatibility: Broad compatibility fixes across many models for HuggingFace Transformers v5 (#37681, #38127, #38090, #38247, #38410).

Model Support

New architectures: Gemma 4 (#38826), Cohere ASR (#35809), Cohere Transcribe (#38120), ColQwen3.5 4.5B (#36887), LFM2-ColBERT-350M (#37528), Granite 4.0 1B Speech (#38019), Qwen3-ForcedAligner (#35367).

Speculative decoding: Eagle3 for Pixtral (#37182), EagleMistralLarge3 fix (#37232).

LoRA expansion: H2OVL tower/connector LoRA (#31696), 
--lora-target-modules
 to restrict LoRA to specific modules (#34984), 
language_model_only
 respected (#37375), Mistral3 fix (#36928), Qwen3.5 fix (#36976), out-of-tree ops replacement (#37181).

Model fixes: NemotronH MTP + Chunked Prefill (#35447), Qwen3-VL video timestamps (#37439), Qwen3.5 GDN quantized models (#37448), Qwen3Next A_log FP32 (#37810), JAIS ALiBi (#37820), RoBERTa CUDA graph position IDs (#37873), AudioFlamingo3/MusicFlamingo (#37643), Music Flamingo loading (#35535), bge-m3 task selection (#37632), Nemotron Parse loading (#37407), GLM OCR patch merger (#37962), PaddleOCR checkpoint compat (#38232), DeepSeek v3.2 params (#33703), MiniMax NVFP4 weight loading (#37214), gated model HF token (#37920), Parakeet OOM on long audio (#36671).

Features: Temporal compression for Nemotron-3-VL videos (#36808), NemotronH Puzzle + MTP (#37803), torch.compile for InternVL vision encoder (#38049), multiple embedding types in single call (#35829).

Performance: GLM-4.xv ViT optimization (#37779).

Engine Core

Zero-bubble async scheduling + speculative decoding (#32951).

Model Runner V2: PP CUDA graphs (#35162), spec decode rejection sampler greedy (#37238) + logprobs (#37237), multimodal embeddings for spec decode (#36097), streaming inputs (#37028), configurable acceptance rate (#38045), FP32 draft logits (#37526), FP64 Gumbel noise (#37798), warmup with spec decode (#37812).

ViT Full CUDA Graph capture (#35963).

General CPU KV cache offloading with pluggable CachePolicy (#37160, #37874), block-level preemption (#34805), multiple KV groups (#36642), hybrid model support (#37853).

DBO for general models: Microbatch optimization generalized beyond specific architectures (#37926).

Compilation: Mega AOT artifact for torch 2.12+ (#37198), lazy graph module to defer recompile (#37609), remove model tag requirement for compile cache (#37345), Triton autotuning disk cache enabled by default (#37188), inductor runtime asserts disabled by default (#37485).

FlexAttention: Custom mask modification support (#37692).

Attention: Distinguish short extends vs decodes (#37303), allow qk_nope_head_dim=192 in FlashInfer MLA (#37475), skip sliding window attention layers with FP8 KV cache (#33695).

Scheduling: Schedule requests based on full input sequence length (#37307).

Spec decode: Per-draft-model MoE backend via 
--speculative-config
 (#37880), Eagle3 drafter quant_config propagation (#37280), Eagle3 norm_before_fc propagation (#38111).

Extensibility: PluggableLayer for CustomQwen2Decoder (#37293), tensor IPC transfer for multimodal data (#32104).

Performance: Optimize top-k in Triton sampler (#37225), optimize token_embed for pooling models with 1% improvement (#37347), fix slow hasattr in CUDAGraphWrapper (#37425), NFS prefetch auto-enabled with RAM guard (#37673), pybase64 replacement (#37290), optimize swap_states for hybrid models (#34733).

Bugfixes: Fix gibberish from FP8 MLA KV scale inconsistency (#37054), Mamba state corruption (#37728), deadlock with pause/resume (#37024), FlashInfer MNNVL socket collisions (#36674), multimodal prefix cache key collisions (#36708), DP coordinator ZMQ TOCTOU (#37452), CUDA graph memory double-counting (#37426), pooling non-determinism (#37775), AllReduce Fusion shutdown crash (#36955), FlashInfer allreduce workspace (#37461), async spec decoding with hybrid models (#38556), MLA sparse indexer prefill chunking (#36178), KV offloading + MLA (#37536), async scheduling extra CUDA context (#37449), DP MTP dummy run (#35243), offloading+prefetch for GLM-4.7-FP8 (#37178), max memory for multiple KV-cache groups (#36030).

Hardware & Performance

NVIDIA:

B300/GB300 (SM 10.3): Allreduce fusion enabled by default (#37755), tuned all-reduce communicator (#37756).

Blackwell: Optimized SM120 CUTLASS blockwise FP8 GEMM (#37970), fix NVFP4 NaN on desktop Blackwell (#37725), fix DeepGEMM E8M0 accuracy for Qwen3.5 FP8 (#38083), restore FP8 FlashMLA CUDA graph persistent buffers (#35175), DGX Spark fix (#38126).

FlashInfer sparse MLA as default for FP8 KV cache (#37252).

Tuned prefill configs for FP8 FA3 (#36265), tuned Triton MoE config for Qwen3.5 on H200 with 9.9% E2E improvement (#37340), H800 MoE configs (#31201).

GPT-OSS: Router GEMM kernel (#37205), eliminate padding with FlashInfer MXFP4/MXFP8 MoE (#30647), reduce redundant SparseMatrix creation (#37683).

NVFP4 CUTLASS MoE non-gated support (#37320), fuse pack topk in TRTLLM MoE via torch.compile (#37695).

Non-contiguous KV cache in TRTLLM FP8 dequant kernel (#36867), Qwen3 dual stream input projection (#36795).

AMD ROCm:

ROCm 7.2.1, torch 2.10, triton 3.6 (#38252).

DeepEP as all2all backend (#34692).

Persistent MLA kernel from AITER (#36574), FP8xFP8 attention in AITER (#36927).

AWQ Marlin support (#36505), wvSplitK skinny GEMM for RDNA4/gfx1x (#34709).

Nightly Docker image and wheel releases (#37283).

Bugfixes: Sleep mode memory leak (#37533), hybrid model stride (#37228), qwen3_next crash (#36795).

Intel XPU: MLA model support (#37143), CompressedTensor W4A8 (#37207), auto-detect XPU build platform (#37634).

TPU: Async scheduling interface (#36924), Qwen3.5 FP8 weight loading fix (#37348).

CPU: Enable tcmalloc by default (#37607), graceful degradation without tcmalloc/libiomp (#37561), 48.9% throughput improvement for pooling models (#38139), OpenMP thread fix for torch.compile (#37538), structured output crash fix (#37706), KV cache block zeroing crash fix (#37550), slot mapping kernel (#37987), W4A16 compressed tensors (#38219).

Performance fixes: FP8 DeepGEMM batch invariance (#37718), Triton autotuning for Qwen3.5 (#37338), TRTLLM NVFP4 routing precision (#36725).

Large Scale Serving

Disaggregated serving: PD kv_transfer_params for Anthropic Messages (#37535) and Responses API (#37424), Mooncake heterogeneous TP (#36869), Mamba N-1 prefill for P/D (#37310).

EPLB: MRV2 support (#37488), improved responsiveness (#36271), EP weight filter fix (#37322).

Elastic EP: Fix repeated scale up/down cycles (#37131), fix stateless group port races (#36330).

DBO: Generalized to work with all models (#37926).

Multi-node: Fix allreduce fusion (#38136).

KV connector: Plugin-overridable metadata build (#37336).

Constraints: Cap API servers to 1 with Elastic EP (#37466).

Quantization

Online MXFP8 quantization for MoE and dense models (#35448).

FP8: WoQ kernel abstraction (#32929), Marlin FP8 for compressed tensors fix (#38092).

NVFP4: Rescale weight scales to fix BF16 dequant underflow (#34577), fix Marlin NaN/Inf with float16 (#33972).

QeRL: Online quantization composed with quantized reloading for RLHF (#38032).

CPU: W4A16 compressed tensors (#38219).

XPU: CompressedTensor W4A8 (#37207).

ROCm: AWQ Marlin support (#36505).

MXFP8 + DeepGEMM: Fix crash when both are active (#37358).

Removals: Per-tensor-per-channel FP8 removed (#32700), Sparse24 integration and kernels removed (#36799).

API & Frontend

New endpoints: 
/v1/chat/completions/batch
 for batched chat completions (#38011).

Features: Limit thinking tokens (hard limit) (#20859), multiple embedding types in single call (#35829), numpy array embeddings for multimodal (#38119), 
--lora-target-modules
 (#34984), 
-sc
 shorthand for 
--speculative-config
 (#38380).

Tool parsing: GigaChat 3.1 parser (#36664), Kimi-K2.5 reasoning/tool parser (#37438), Gemma 4 tool parser (#38847), tools passed to parser constructor (#38029), fix Mistral parser (#37209), fix DeepSeek v3.2 streaming (#36056), fix GLM-4.7 parsing (#37386), fix Hermes streaming (#38168), fix OpenAI tool parser IndexError (#37958), fix Anthropic streaming (#37510).

Responses API: Fix crash with tool_choice=required exceeding ma...

Read more

Contributors

 laudney, brandonpelfrey, and 52 other contributors
 

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍12adamw7, yassermessahli, MatejRojec, jaxhend, jhempenius, BenWongCityuCS, llocretsa, mkMoSs, igor-susic1, mayshin10, and 2 more reacted with thumbs up emoji🎉26crazyguitar, nanbogong, LiAnQing279, 1zilc, MengqingCao, noooop, 5aharsh, tristan-renaud, Paxtiny, scyyh11, and 16 more reacted with hooray emoji🚀2wedobetter and jiosephlee reacted with rocket emoji
All reactions
👍12 reactions

🎉26 reactions

🚀2 reactions

35 people reacted

v0.18.1

 31 Mar 00:53
 

khluu

 v0.18.1
 

a26e8dc

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.18.1

This is a patch release on top of v0.18.0 to address a few issues:

Change default SM100 MLA prefill backend back to TRT-LLM (#38562)

Fix mock.patch resolution failure for standalone_compile.FakeTensorMode on Python <= 3.10 (#37158)

Disable monolithic TRTLLM MoE for Renormalize routing #37605

Pre-download missing FlashInfer headers in Docker build #38391

Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell (#38083)

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍12kyoungbinkim, snomile, Mr-Penguin, adamw7, maxx4144136-ship-it, ivanbaldo, zuhaira631, sejohnst, dangoldbj, ucyang, and 2 more reacted with thumbs up emoji
All reactions
👍12 reactions

12 people reacted

v0.18.0

 20 Mar 21:31
 

khluu

 v0.18.0
 

bcf2be9

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.18.0

vLLM v0.18.0

Known issues

Degraded accuracy when serving Qwen3.5 with FP8 KV cache on B200 (#37618)

If you previously ran into 
CUBLAS_STATUS_INVALID_VALUE
 and had to use a workaround in 
v0.17.0
, you can reinstall 
torch 2.10.0
. PyTorch published an updated wheel that addresses this bug.

Highlights

This release features 445 commits from 213 contributors (61 new)!

gRPC Serving Support: vLLM now supports gRPC serving via the new 
--grpc
 flag (#36169), enabling high-performance RPC-based serving alongside the existing HTTP/REST interface.

GPU-less Render Serving: New 
vllm launch render
 command (#36166, #34551) enables GPU-less preprocessing and rendering, allowing separation of multimodal preprocessing from GPU inference.

NGram GPU Speculative Decoding: NGram speculative decoding now runs on GPU and is compatible with the async scheduler (#29184), significantly reducing spec decode overhead.

KV Cache Offloading Improvements: Smart CPU offloading that stores only frequently-reused blocks (#35342), plus FlexKV as a new offloading backend (#34328) and support for multiple KV groups in offloading spec (#36610).

Elastic Expert Parallelism Milestone 2: NIXL-EP integration (#35627) enables dynamic GPU scaling for MoE experts, with new 
--enable-ep-weight-filter
 CLI option (#37351) for faster EP model loading.

FlashInfer 0.6.6: Updated FlashInfer dependency (#36768) with numerous performance and correctness improvements.

Responses API Streaming Tool Calls: The OpenAI Responses API now supports tool/function calling with streaming (#29947).

Online Beam Search for ASR: Beam search support for encoder/decoder models both offline (#36153) and online transcriptions (#36160).

Ray No Longer a Default Dependency: Ray has been removed as a default dependency (#36170) — install it explicitly if needed.

Model Support

New architectures: Sarvam MoE (#33942), OLMo Hybrid (#32550), HyperCLOVAX-SEED-Think-32B VLM (#31471), HyperCLOVAX-SEED-Think-14B (#37107), Kimi-Audio-7B-Instruct (#36127), ColPali late-interaction retrieval (#36818), ERNIE pooling models (#36385).

Speculative decoding: Eagle3 for Qwen3.5 (#36658), Eagle3 for Kimi K2.5 MLA (#36361), Eagle for Mistral Large 3 with dense layers (#36163).

LoRA: Whisper LoRA (#29856), FP8 LoRA dense kernel (#35242).

Multimodal: Online use_audio_in_video (#36319), audio extraction from MP4 for Nemotron Nano VL (#35539), audio transcription for MP4/M4A/WebM (#35109), expose media_io_kwargs at runtime (#34778), fast media preprocessing for Nano Nemotron VL (#35657).

Compatibility: Gemma/Gemma2 inputs_embeds (#36787), SigLIP/CLIP Transformers v5 (#37200), fused expert weights in Transformers backend (#36997).

Performance: Qwen3 Next fused GDN kernel (#35777), LFM2 tuned H100 MoE configs (#36699).

Fixes: DeepSeek-V3.2 tokenizer space stripping (#37004), Qwen3.5 tool calling (#36774), Qwen3-VL timestamp mismatch (#36136), Qwen3-Next TP>1 weight sharding (#36242), Qwen3-ASR torch.compile (#35869), MiniCPM-V audio inference (#36751), MiniCPM-O 4.5 ViT attention (#34127), routed experts for hybrid models (#35744), Qwen2.5-Omni/Qwen3-Omni multi-video audio_in_video (#37147), DeepSeek-OCR empty images crash (#36670).

Engine Core

Model Runner V2: Probabilistic rejection sampling for spec decode (#35461), pooling models (#36019), extensible CUDA graph dispatch (#35959), WhisperModelState (#35790), XD-RoPE (#36817), model_state CUDA graph capture (#36544).

KV cache offloading: Reuse-frequency-gated CPU stores (#35342), FlexKV offloading backend (#34328), multiple KV groups (#36610), async scheduling fix (#33881).

Speculative decoding: NGram GPU implementation with async scheduler (#29184), fused EAGLE step slot mapping (#33503).

Performance: Remove busy loop from idle buffer readers (#28053), 2.7% E2E throughput for pooling via worker-side maxsim (#36159), 3.2% via batched maxsim (#36710), CUDA graph memory accounting during profiling (#30515), checkpoint prefetch to OS page cache (#36012), InstantTensor weight loader (#36139), sporadic stall fix via pin_memory removal (#37006).

Stability: VLM concurrent throughput degradation fix (#36557), DP deadlock fix (#35194), DeepSeek V3.2 OOM during CG profiling (#36691), Ray DP startup crash (#36665), NCCL rank calculation fix (#36940), zero-init MLA output buffers for NaN prevention (#37442), CUDA OOM fix (#35594).

Defaults: Cascade attention disabled by default (#36318).

Extensibility: OOT linear method registration (#35981), custom collective ops registration for non-CUDA platforms (#34760).

Kernel

FA4 for MLA prefill (#34732).

FlashInfer Sparse MLA: FP8 KV cache support (#35891), CUDA graphs on ROCm (#35719), MTP lens > 1 on ROCm (#36681).

TRTLLM FP8 MoE modular kernel (#36307).

FP8 KV cache for Triton MLA decode (#34597).

FlashInfer MoE A2A kernel (#36022).

Remove chunking from FusedMoE for full batch processing (#34086).

CustomOp FusedRMSNormGated for torch.compile compatibility (#35877).

Mamba2 SSD prefill Triton kernel optimization (#35397).

DeepSeek-V3.2: Vectorized MLA query concat kernel (#34917), optimized FP8 KV cache gather for context parallel (#35290).

320-dimension MLA head size support (#36161).

Packed recurrent fast path for decode (#36596).

EP scatter race condition fix (#34991).

Hardware & Performance

NVIDIA: FA4 for MLA prefill (#34732), DeepSeek-V3.2 MLA kernel optimizations (#34917, #35290).

AMD ROCm: Sparse MLA CUDA graphs (#35719), MTP lens > 1 in Sparse MLA (#36681), MLA with nhead<16 + FP8 KV for TP=8 (#35850), RoPE+KV cache fusion for AITER FA (#35786), AITER MLA CPU sync avoidance (#35765), Quark W4A8 MXFP4/FP8 (#35316), gfx1152/gfx1153 Krackan support (#36499), fused_topk_bias AITER optimization (#36253), skinny GEMM improvements (#34304), DeepEP in ROCm Dockerfile (#36086), startup OOM fix (#36720).

Intel XPU: Model Runner V2 enabled (#36078), MLA Sparse backend for DeepSeek V3.2 (#33230), LoRA via torch.compile (#36962), block FP8 MoE fallback (#36458), deepseek_scaling_rope fused kernel (#36612).

CPU: aarch64 int8 matmul via OneDNN upgrade (#36147), AMD Zen CPU backend via zentorch (#35970).

RISC-V: CPU backend support (#36578).

Performance: 5% E2E improvement for PD disaggregation scheduling (#35781), packed recurrent decode fast path (#36596), pooling model maxsim 2.7%+3.2% throughput (#36159, #36710).

torch.compile: FakeTensors instead of real GPU tensors for single-size compilation (#36093), non-contiguous fused RMSNorm + group quant (#36551), stop lazy compiling (#35472).

Large Scale Serving

Elastic EP Milestone 2: NIXL-EP integration (#35627), 
--enable-ep-weight-filter
 for faster EP loading (#37351).

PD Disaggregation: ~5% scheduler overhead reduction (#35781), KV transfer fix with spec decode (#35158), P/D for hybrid SSM-FA models via NIXL (#36687), PP for multimodal models on Transformers backend (#37057).

KV Connectors: HMA + NIXL connector (#35758), FlexKV offloading (#34328), worker→scheduler metadata (#31964), All-to-All DCP backend (#34883).

LMCache: Fault tolerance mechanism (#36586), memory leak fix (#35931), race condition fix (#35831), TP size for MLA multi-reader locking (#36129).

EP loading: Skip non-local expert weights (#37136).

Quantization

ModelOpt MXFP8 MoE support (#35986).

MXFP4 MoE routing simulation override for accuracy (#33595).

FP8 LoRA dense kernel (#35242).

ROCm: Quark W4A8 MXFP4/FP8 for LinearLayer (#35316), compressed-tensors fix for DeepSeek-R1 on MI300x (#36247).

Fixes: MLA crash with AWQ/GPTQ quantized models (#34695), score layer quantization for reranker models (#35849), GLM-4.1V non-default quantization (#36321), FP8 k_scale/v_scale loading for Qwen3-MoE (#35656).

API & Frontend

gRPC: New 
--grpc
 flag for gRPC serving (#36169).

GPU-less serving: 
vllm launch render
 for preprocessing-only serving (#36166), 
vllm launch
 for GPU-less preprocessing (#34551).

Responses API: Streaming tool/function calling (#29947), reasoning item fixes (#34499, #36516).

Anthropic API: Accept redacted thinking blocks (#36992).

ASR: Online beam search transcriptions (#36160), offline beam search (#36153), audio transcription for MP4/M4A/WebM (#35109), realtime endpoint metrics (#35500).

Tool calling: Granite4 tool parser (#36827), Qwen3Coder anyOf double encoding fix (#36032).

New options: 
--distributed-timeout-seconds
 (#36047), 
--attention-backend auto
 (#35738), 
reasoning_effort=none
 (#36238), PyTorch profiler schedule (#35240).

Cohere Embed v2 API support (#37074).

Azure Blob Storage support for RunAI Model Streamer (#34614).

Graceful shutdown timeout for in-flight requests (#36666).

Fixes: tool_choice=required exceeding max_tokens crash (#36841), negative max_tokens with long prompts (#36789), concurrent classify/token_classify race (#36614), Anthropic billing header prefix cache miss (#36829), render endpoint crash for multimodal requests (#35684), xgrammar dtype mismatch on macOS CPU (#32384), minimax_m2 tool parser with stream interval > 1 (#35895).

Security

Respect user 
trust_remote_code
 setting in NemotronVL and KimiK25 (#36192).

Upgrade xgrammar for security fix (#36168).

Guard RLHF weight sync deserialization behind insecure serialization flag (#35928).

Dependencies

FlashInfer 0.6.6 (#36768).

Ray removed from default dependencies (#36170).

kaldi_native_fbank
 made optional (#35996).

OpenAI dependency bounded to 2.24.0 (#36471).

Deprecated items from v0.18 removed (#36470, #36006).

Mistral common v10 (#36971).

Breaki...

Read more

Contributors

 shubhra, sungsooha, and 59 other contributors
 

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍181zilc, Brensom, amukho, DonliFly, gravesprite, harveyff, bigbear07, slfan1989, kyoungbinkim, ucyang, and 8 more reacted with thumbs up emoji🚀12zhewenl, DonliFly, Billy-Davies-2, mertalev, manhld0206, Richardyu114, Bambuuai, wedobetter, LittleExian, subnet-dev, and 2 more reacted with rocket emoji
All reactions
👍18 reactions

🚀12 reactions

28 people reacted

v0.17.1

 11 Mar 10:24
 

khluu

 v0.17.1
 

95c0f92

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.17.1

This is a patch release on top of 
v0.17.0
 to address a few issues:

New Model: Nemotron 3 Super

Fix passing of activation_type to trtllm fused MoE NVFP4 and FP8 (#36017)

Fix/resupport nongated fused moe triton (#36412)

Re-enable EP for trtllm MoE FP8 backend (#36494)

[Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU (#35219)

Fix TRTLLM Block FP8 MoE Monolithic (#36296)

[DSV3.2][MTP] Optimize Indexer MTP handling (#36723)

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍37jeejeelee, crossijinn, longit644, ttw1018, Hey-Aryan, xyhzyp, BOSSKING008, gabinguo, Hunter6324, prravda, and 27 more reacted with thumbs up emoji🎉12reneleonhardt, gabinguo, Hunter6324, fschaupp, orech, jokelord, tinashe-mundangepfupfu, artbataev, bigPYJ1151, charlie-taylor, and 2 more reacted with hooray emoji
All reactions
👍37 reactions

🎉12 reactions

41 people reacted

v0.17.0

 07 Mar 00:46
 

khluu

 v0.17.0
 

b31e932

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.17.0

vLLM v0.17.0

Known Issue: If you are on CUDA 12.9+ and encounter a 
CUBLAS_STATUS_INVALID_VALUE
 error, this is caused by a CUDA library mismatch. To resolve, try one of the following:

Remove the path to system CUDA shared library files (e.g. 
/usr/local/cuda
) from 
LD_LIBRARY_PATH
, or simply 
unset LD_LIBRARY_PATH
.

Install vLLM with 
uv pip install vllm --torch-backend=auto
.

Install vLLM with 
pip install vllm --extra-index-url https://download.pytorch.org/whl/cu129
 (change the CUDA version to match your system).

Highlights

This release features 699 commits from 272 contributors (48 new)!

PyTorch 2.10 Upgrade: This release upgrades to PyTorch 2.10.0, which is a breaking change for environment dependencies.

FlashAttention 4 Integration: vLLM now supports the FlashAttention 4 backend (#32974), bringing next-generation attention performance.

Model Runner V2 Maturation: Model Runner V2 has reached a major milestone with Pipeline Parallel (#33960), Decode Context Parallel (#34179), Eagle3 speculative decoding with CUDA graphs (#35029, #35040), pooling model support (#35120), piecewise & mixed CUDA graph capture (#32771), DP+EP for spec decoding (#35294), and a new ModelState architecture. Design docs are now available (#35819).

Qwen3.5 Model Family: Full support for the Qwen3.5 model family (#34110) featuring GDN (Gated Delta Networks), with FP8 quantization, MTP speculative decoding, and reasoning parser support.

New 
--performance-mode
 Flag: A new 
--performance-mode {balanced, interactivity, throughput}
 flag (#34936) simplifies performance tuning for common deployment scenarios.

Anthropic API Compatibility: Added support for Anthropic thinking blocks (#33671), 
count_tokens
 API (#35588), 
tool_choice=none
 (#35835), and streaming/image handling fixes.

Weight Offloading V2 with Prefetching: The weight offloader now hides onloading latency via prefetching (#29941), plus selective CPU weight offloading (#34535) and CPU offloading without pinned memory doubling (#32993).

Elastic Expert Parallelism Milestone 2: Initial support for elastic expert parallelism enabling dynamic GPU scaling for MoE models (#34861).

Quantized LoRA Adapters: Users can now load quantized LoRA adapters (e.g. QLoRA) directly (#30286).

Transformers v5 Compatibility: Extensive work to ensure compatibility with HuggingFace Transformers v5 across models and utilities.

CPU release supports AVX2, AVX-512, VNNI, AVX512BF16, and AMX (#35466). The multi-ISA CPU dispatcher was originally implemented by @MekayelAnik (dtrifiro#9, merged December 22, 2025) in collaboration with Willy Hardy, and later reimplemented in C++ in #35466.

Model Support

New architectures: Qwen3.5 (#34110), COLQwen3 (#34398), ColModernVBERT (#34558), Ring 2.5 (#35102), skt/A.X-K1 (#32407), Ovis 2.6 (#34426), nvidia/llama-nemotron-embed-vl-1b-v2 (#35297), nvidia/llama-nemotron-rerank-vl-1b-v2 (#35735), nvidia/nemotron-colembed (#34574).

ASR models: FunASR (#33247), FireRedASR2 (#35727), Qwen3-ASR realtime streaming (#34613).

Multimodal: OpenPangu-VL video input (#34134), audio chunking for offline LLM (#34628), Parakeet audio encoder for nemotron-nano-vl (#35100), MiniCPM-o flagos (#34126).

LoRA: LFM2 (#34921), Llama 4 Vision tower/connector (#35147), max vocab size increased to 258048 (#34773), quantized LoRA adapters (#30286).

Task expansion: ColBERT extended to non-standard BERT backbones (#34170), multimodal scoring for late-interaction models (#34574).

Performance: Qwen3.5 GDN projector fusion (#34697), FlashInfer cuDNN backend for Qwen3 VL ViT (#34580), Step3.5-Flash NVFP4 (#34478), Qwen3MoE tuned configs for H200 (#35457).

Fixes: DeepSeek-VL V2 simplified loading (#35203), Qwen3/Qwen3.5 reasoning parser (#34779), Qwen2.5-Omni/Qwen3-Omni mixed-modality (#35368), Ernie4.5-VL garbled output (#35587), Qwen-VL tokenizer (#36140), Qwen-Omni audio cache (#35994), Nemotron-3-Nano NVFP4 accuracy with TP>1 (#34476).

Engine Core

Model Runner V2: Pipeline Parallel (#33960), Decode Context Parallel (#34179), piecewise & mixed CUDA graphs (#32771), Eagle3 with CUDA graphs (#35029, #35040), pooling models (#35120), DP+EP for spec decoding (#35294), bad_words sampling (#33433), ModelState architecture (#35350, #35383, #35564, #35621, #35774), design docs (#35819).

Weight offloading: V2 prefetching to hide latency (#29941), selective CPU weight offloading (#34535), CPU offloading without pinned memory doubling (#32993).

Sleep level 0 mode with enqueue/wait pattern (#33195), pause/resume moved into engine (#34125).

Fixes: allreduce_rms_fusion disabled by default with PP > 1 (#35424), DCP + FA3 crash (#35082), prefix caching for Mamba "all" mode (#34874), num_active_loras fix (#34119), async TP reduce-scatter reduction fix (#33088).

Repetitive token pattern detection flags (#35451).

Kernel

FlashAttention 4 integration (#32974).

FlashInfer Sparse MLA backend (#33451).

Triton-based top-k and top-p sampler kernels (#33538).

Faster topKperRow decode kernel for DeepSeek-V3.2 sparse attention (#33680).

Optimized grouped topk kernel (#34206).

TRTLLM DSV3 Router GEMM kernel, 6% batch-1 speedup (#34302).

FA3 swizzle optimization (#34043).

256-bit LDG/STG activation kernels (#33022).

TMA support for fused_moe_lora kernel (#32195).

Helion kernel framework: silu_mul_fp8 kernel (#33373), autotuning infrastructure (#34025), num_tokens autotuning (#34185), fx tracing via HOP (#34390), GPU variant canonicalization (#34928).

FlashInfer TRTLLM fused MoE non-gated FP8 & NVFP4 (#33506).

Optimized sample_recovered_tokens kernel (#34974).

KV cache update ops extraction from FlashInfer forward (#35422) and MLA backends (#34627).

Hardware & Performance

NVIDIA: SM100 FMHA FP8 prefill for MLA (#31195), SM100 MXFP8 blockscaled grouped MM and quant kernels (#34448), SM100 Oink RMSNorm path (#31828), SM120 FP8 GEMM optimization (#34424), FlashInfer DeepGEMM swapAB on SM90 by default (#34924), DeepSeek R1 BF16 min latency QKV GEMM 0.5% E2E speedup (#34758), Cublas BF16 gate with FP32 output (#35121), FlashInfer All Reduce default to TRTLLM backend (#35793).

AMD ROCm: AITER fused RoPE+KVCache (#33443), MXFP4 MoE weight pre-shuffling on gfx950 (#34192), bitsandbytes quantization (#34688), CK backend for MoE quantization (#34301), dynamic MXFP4 for DeepSeek V2 (#34157), GPT-OSS Quark format (#29008), GPT-OSS WMXFP4_AFP8 static scales (#30357), encoder/encoder-decoder on AITER (#35334), device capability derivation without CUDA init (#35069), 
aiter
 package renamed to 
amd-aiter
 (#35198).

Intel XPU: CUDA graph support (#34482), GPUDirect RDMA via NIXL (#35270), TORCH_SDPA/TRITON_ATTN as ViT backend (#35010), vllm-xpu-kernels v0.1.3 (#35984).

CPU: ARM BF16 cross-compilation (#33079), FP16 for s390x (#34116), KleidiAI INT8_W4A8 for all input dtypes (#34890), s390x vector intrinsics for attention (#34434), prefix caching for ppc64le (#35081), CPU release supports both AVX2 and AVX512 (#35466).

Performance: Pipeline Parallel async send/recv 2.9% E2E throughput (#33368), pooling maxsim 13.9% throughput improvement (#35330), Triton ViT attention backend (#32183), Mamba1 kernel-level chunk alignment for prefix caching (#34798), detokenizer optimization (#32975), pooling model copy optimization 1.8% throughput (#35127).

Large Scale Serving

Pipeline Parallel async send/recv, 2.9% throughput improvement (#33368).

Elastic EP Milestone 2 (#34861).

EPLB: Async rebalance algorithm (#30888), sync enforcement for NCCL backend (#35212).

Native weight syncing API via IPC for RL workflows (#34171).

Decode Context Parallel in Model Runner V2 (#34179).

Ray env var propagation to workers (#34383).

Breaking: KV load failure policy default changed from "recompute" to "fail" (#34896).

Cross-node data parallelism message queue fix (#35429).

NIXL: Token-based IPC API (#34175), version bound (#35495), NUMA core binding (#32365).

Speculative Decoding

Nemotron-H MTP and Mamba speculative decoding (#33726).

Eagle3 on Model Runner V2 with CUDA graphs (#35029, #35040), Eagle3 + disaggregated serving (#34529).

Hidden states extraction system (#33736).

min_tokens
 support with speculative decoding (#32642).

Reduced TP communication for draft generation (#34049).

MTP num_speculative_tokens > 1 with sparse MLA (#34552).

Sparse MLA + MTP with full CUDA graphs (#34457).

Spec decoding in Mamba cache align mode (#33705).

DP+EP for spec decoding in Model Runner V2 (#35294).

MoE Refactor

MoERunner abstraction (#32344) with modular kernel architecture.

MXFP4 Cutlass Experts to modular kernel (#34542), MXFP4 Marlin to modular kernel format (#34588), TRTLLM Kernels MK (#32564).

MoEActivation enum (#33843).

Improved default Triton fused MoE configs (#34846).

Fused MoE + LoRA shared expert dual stream, 1.07x throughput (#34933).

DSV3 QKVAProj GEMM custom op for torch.compile (#35751).

Fix routing for models without expert groups (MiniMax-M2.1) (#34673).

torch.compile

AOT compile with PyTorch 2.10 (#34155).

AR+RMSNorm fusion by default at -O2 (#34299).

SiLU+FP4 quant fusion by default at O1+ (#34718).

Sequence parallelism threshold compile ranges (#28672).

Various compile fixes: recursive pre_grad_passes (#34092), FakeTensorProp elimination (#34093), time discrepancy logging (#34912), artifact load errors (#35115), atomic artifact saving (#35117), pytree slice caching (#35308), fast_moe_cold_start undo for torch>=2.11 (#35475).

Quantization

Quantized LoRA adapters (#30286).

**Per-head KV cach...

Read more

Contributors

 koush, pks, and 47 other contributors
 

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍18adamw7, maksimlitvinov39kg, preetam19, ICO-Project-team, badrayour-nebesta, top-5, Madinah31, xulunfan, XULU42, dkremez, and 8 more reacted with thumbs up emoji🎉22CycloneBoy, sumuen, gauravbrills, saattrupdan, menon92, Tialo, Lee-xeo, maksimlitvinov39kg, ariable, preetam19, and 12 more reacted with hooray emoji❤️7reneleonhardt, erciktiburak, JosephAhn23, tstescoTT, pi-null-mezon, jozadaquebatista, and ivanbaldo reacted with heart emoji🚀16CLRT19, Puiching-Memory, fjosw, maksimlitvinov39kg, preetam19, ICO-Project-team, jiosephlee, LudovicoYIN, JosephAhn23, longit644, and 6 more reacted with rocket emoji
All reactions
👍18 reactions

🎉22 reactions

❤️7 reactions

🚀16 reactions

49 people reacted

v0.16.0

 25 Feb 19:58
 

khluu

 v0.16.0
 

89a77b1

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.16.0

vLLM v0.16.0

Please note that this release was branch cut on Feb 8, so any features added to vLLM after that date is not included.

Highlights

This release features 440 commits from 203 contributors (7 new)!

Async scheduling + Pipeline Parallelism is now fully supported, delivering 30.8% E2E throughput improvement and 31.8% TPOT improvement (#32618).

Realtime API: A new WebSocket-based Realtime API enables streaming audio interactions (#33187), building on the Voxtral realtime infrastructure.

RLHF workflow improvements: Native NCCL-based weight syncing API (#31943), layerwise weight reloading for QeRL (#32133), and engine pause/resume with request preservation (#32351).

Unified Parallel Drafting for speculative decoding (#32887), plus spec decode now works with structured outputs (#33374) and penalty application in Model Runner V2 (#33251).

Major XPU platform overhaul: Deprecated IPEX in favor of vllm-xpu-kernels (#33379), adding MoE (#33659), MXFP4 MoE (#33679), WNA16 (#33973), scaled_mm (#34117), and FP8 MoE (#34202) support.

Model Support

New architectures: GLM-OCR with MTP (#33005), Qwen3-ASR (#33312), DeepSeek-OCR-2 (#33165), Intern-S1-Pro (#33636), MiniCPM-o 4.5 (#33431), openPangu7B-VL (#32449), NemotronHPuzzle heterogeneous (#32549), MusicFlamingo (#32696), FunAudioChat (#2), ColBERT late interaction (#33686), voyage-4-nano (#33720), GLM-5 (#34124).

Speculative decoding: EAGLE3 for Hunyuan/HunyuanVL (#33035), AFMoE (#33111), Mistral3 (#33939).

LoRA expansion: Gemma3 vision components (#32764), Nemotron-H MTP models (#32265), Qwen3 output embedding (#29816). Optimized fused MoE-LoRA kernel indexing (#32770, #32774), unpermute-aware fused MoE LoRA path (#32655), reduced kernel overhead for fewer active LoRAs with multiple CUDA graphs (#32005).

Features: Qwen3-Omni transcription (#29828), Mistral Large 3 with FlashInfer MoE (#33174), LFM2 SigLIP2 intermediate encoder layers (#33370), Qwen3-Omni/GLM-4.xV MRoPE positioning fixes (#33010, #33039), embedding input for disabled modalities (#32493).

Performance: GLM-4.7-GPTQ decode and MTP acceptance rate regression fix (#33771), DeepSeek V3.2 fast detokenization (#33855), DeepSeek V3.2 tokenizer fix (#33832), GLM-5 MTP accuracy fix (#34385).

Engine Core

Async scheduling + Pipeline Parallelism: Full support with 30.8% throughput improvement (#32618), optimized spec decode + async scheduling with 1.5% throughput improvement (#33612), deadlock fix for torchrun PP broadcast (#33701).

Speculative decoding: Unified Parallel Drafting (#32887), structured output support (#33374), penalty application in MRV2 (#33251), skip softmax for all-greedy rejection sampling (#32852), correctness fix for spec tokens with prefill chunks (#33652).

RLHF: Native NCCL weight syncing API (#31943), layerwise reloading for QeRL (#32133), engine pause/resume with request preservation (#32351).

Helion kernel framework: ConfigManager (#32740), kernel wrapper (#32964), kernel registry (#33203).

PluggableLayer: Applied to linear layers (#33152) and Mamba layers (#33660).

Batch invariance: Disable Cascade Attention (#32561), enable Triton attention (#33688).

Performance: Grammar bitmask H2D copy on separate stream (#33059), zero-copy GQA for multimodal and CPU (#33732), early-reject oversized MM requests (#33502), CPU memory leak fix from Request reference cycle in prefix caching (#34183).

Hardware & Performance

NVIDIA: FlashInfer TRTLLM BF16 MoE integration (#32954), SM100 INT4 W4A16 kernel (#32437), SM121 (DGX Spark) CUTLASS support (#33517), MNNVL protocol for GB series (#33540), FlashInfer MLA concat optimization (#31171), GDN attention layout optimization (#33291), DeepGEMM FP8 MLA performance (#33568), wvSplitK_fp8 performance (#33527, #33493), B200 MoE configs for Nemotron Nano (#32804), Super B200 TP2 (#33510), GLM 4.6 (#32958), Mamba selective scan tuning for B200 (#32873). Fix: DeepSeek R1 CUTLASS MLA on B200 (#33637), QK Norm+RoPE fusion on B200+FP8 (#33967), CUTLASS FP8 blockwise on SM103a (#32224).

AMD ROCm: QWEN3-NEXT FP8 tunings (#32042), AITER attention backend for Qwen3-Next (#32492), fused_add_rmsnorm_pad for GPT-OSS (#30976), Qwen3-Omni startup fix (#33077).

Intel XPU: Platform overhaul - deprecated IPEX, switched to vllm-xpu-kernels (#33379). New: unquantized MoE (#33659), MXFP4 MoE (#33679), WNA16 kernel (#33973), scaled_mm kernel (#34117), FP8 MoE (#34202).

ARM CPU: KleidiAI INT4 dynamic quant with BF16 activations (#33122), NEON BFMMLA BF16 paged attention (#32263), vectorization backend optimization (#30329), attention dispatch by head_dim alignment (#32161).

IBM Z: BF16 kernel type for s390x (#33788).

torch.compile: Stop compiling identical artifacts (#34003), MoE cold start optimization option (#33735), fix 32-bit indexing assumption (#33113), attention fusion pass fix (#33945).

Performance: Chat completion streaming optimization (#33782), ORJSONResponse for faster API responses (#33548), MoE permute optimization for CUTLASS FP8 (#32892), shared/routed overlap for latent MoE on Nemotron-H (#32790), FlashInfer autotune control flag (#34006).

Large Scale Serving

Disaggregated serving: Mooncake connector rework with bootstrap server (#31034), cross-layer KV cache layout at NIXL Connector V2 (#33339), delay freeing blocks for aborted async loads (#32255), async double-free fix (#33377), Ray multi-replica single-instance fix (#33604).

EPLB: Capture logical experts with router replay (#33013), DP metadata fix for dense models (#32739).

Metrics: KV offloading connector metrics (#27942), labeled prompt token metrics for P/D disaggregation (#33290).

Quantization

New: FP8 block quant for CompressedTensorsW8A16Fp8 (#33280), ModelOpt MXFP8 for dense models (#33786), NVFP4/FP8 on Turing GPUs (#33076), TP > 4 for FP4 Gemm (#31099).

Bugfixes: FP8 online quantization memory fix (#31914), asymmetric W4A16 (ConchLinear) for CT (#33200), DeepSeek V3.2 NVFP4 (#33932), LoRA FP8 (#33879), quantized Falcon-H1 model loading (#32728), quantized Mamba TP with n_groups=1 (#33257), CPU W8A8 with bias (#33582), CPU W8A8 3D input support (#33727).

Deprecation: Removed BitBlas (#32683) and Marlin 24 (#32688).

API & Frontend

Realtime API: WebSocket-based streaming API (#33187) with Voxtral realtime support.

Responses API: Sampling parameters (#32609), return token IDs (#33212), return prompt token IDs (#33378), parser implementation (#32712).

Pooling API: Request schema consensus for ScoreRequest (#33060) and final standardization (#31127).

Tool calling: Fix multi-turn tool call ID preservation (#32768), fix indexing double-counting (#33141), GLM-4 incremental string streaming (#33218), DSV3.2 fast detokenization fix (#33964), MCP tools non-streaming fix (#32762).

Structured outputs: Performance optimization with reasoning (#33557), guidance vocab size fix (#33509).

CLI: 
--disable-access-log-for-endpoints
 option (#30011).

UX: Nested configs in YAML files (#33193), GGUF 
repo_id:quant_type
 syntax (#33371), DeepSeek ReasoningParser with thinking enabled by default (#33221), remove noisy CT warning (#33273), early tokenization validation (#31366), reasoning_content backward compatibility (#33635), only include Authorization header when OPENAI_API_KEY is set (#33488).

Features: run_batch transcription/translation support (#33934), /server_info collect_env (#33246), OTEL tracing during model loading (#31162), clear MM and encoder cache (#33452), HF Hub LoRA resolver (#20320).

Scoring: Fix multi-document scoring returning single result (#33837).

Security

Patch protobuf for CVE-2026-0994 (#34253).

Dependencies

huggingface-hub updates for Transformers v5 preparation (#33473).

Transformers v5 compatibility fixes across multiple models (#33977, #33683).

Deprecation & Breaking Changes

Removed BitBlas quantization (#32683) and Marlin 24 (#32688).

Removed deprecated 
reasoning_content
 message field (#33402).

Removed deprecated pooling items (#33477).

Removed deprecated 
VLLM_ALL2ALL_BACKEND
 environment variable (#33535).

Deprecated IPEX for XPU, switched to vllm-xpu-kernels (#33379).

New Contributors 🎉

@aabbccddwasd made their first contribution in #33771

@Code4me2 made their first contribution in #33517

@ikchifo made their first contribution in #33967

@jiangwu300 made their first contribution in #33604

@pjs102793 made their first contribution in #33963

@sleepcoo made their first contribution in #33978

@TundeAtSN made their first contribution in #33939

Contributors

 ikchifo, pjs102793, and 5 other contributors
 

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍51FUYOH666, ctruepri, CYGDEN, crazyguitar, jeneapopovvv, Puiching-Memory, janssen-llm, gabinguo, digim0nk, ikaadil, and 41 more reacted with thumbs up emoji🎉5reneleonhardt, yewentao256, AgriTechLLC, pymhq, and ivanbaldo reacted with hooray emoji🚀32cjackal, xyDong0223, CYGDEN, stingoChen, wedobetter, gabinguo, ikaadil, onyxmaster, sebfelix, anurag12-webster, and 22 more reacted with rocket emoji👀9huangyiqun, anurag12-webster, GosuDRM, oleslav, wongsingfo, SylvainVerdy, AgriTechLLC, Adenialzz, and ivanbaldo reacted with eyes emoji
All reactions
👍51 reactions

🎉5 reactions

🚀32 reactions

👀9 reactions

75 people reacted

v0.15.1

 04 Feb 20:48
 

khluu

 v0.15.1
 

1892993

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.15.1

v0.15.1 is a patch release with security fixes, RTX Blackwell GPU fixes support, and bug fixes.

Security

CVE-2025-69223: Updated aiohttp dependency (#33621)

CVE-2026-0994: Updated Protobuf dependency (#33619)

Highlights

Bugfix Hardware Support

RTX Blackwell (SM120): Fixed NVFP4 MoE kernel support for RTX Blackwell workstation GPUs. Previously, NVFP4 MoE models would fail to load on these GPUs (#33417)

FP8 kernel selection: Fixed FP8 CUTLASS group GEMM to properly fall back to Triton kernels on SM120 GPUs (#33285)

Model Support

Step-3.5-Flash: New model support (#33523)

Bugfix Model Support

Qwen3-VL-Reranker: Fixed model loading (#33298)

Whisper: Fixed FlashAttention2 with full CUDA graphs (#33360)

Performance

torch.compile cold-start: Fixed regression that increased cold-start compilation time (Llama3-70B: ~88s → ~22s) (#33441)

MoE forward pass: Optimized by caching layer name computation (#33184)

Bug Fixes

Fixed prefix cache hit rate of 0% with GPT-OSS style hybrid attention models (#33524)

Enabled Triton MoE backend for FP8 per-tensor dynamic quantization (#33300)

Disabled unsupported Renormalize routing methods for TRTLLM per-tensor FP8 MoE (#33620)

Fixed speculative decoding metrics crash when no tokens generated (#33729)

Disabled fast MoE cold start optimization with speculative decoding (#33624)

Fixed ROCm skinny GEMM dispatch logic (#33366)

Dependencies

Pinned LMCache >= v0.3.9 for API compatibility (#33440)

New Contributors 🎉

@zaristei2 made their first contribution in #33621

Full Changelog: v0.15.0...v0.15.1

Contributors

 zaristei2
 

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

🚀20wedobetter, crossijinn, johnnynunez, MarioRaach22, johnbont, mbrcic, woojh3690, nekomiya-hinata, shisota, bichowdh, and 10 more reacted with rocket emoji
All reactions
🚀20 reactions

20 people reacted

v0.15.0

 29 Jan 10:21
 

khluu

 v0.15.0
 

f176443

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.15.0

Highlights

This release features 335 commits from 158 contributors (39 new)!

Model Support

New architectures: Kimi-K2.5 (#33131), Molmo2 (#30997), Step3vl 10B (#32329), Step1 (#32511), GLM-Lite (#31386), Eagle2.5-8B VLM (#32456).

LoRA expansion: Nemotron-H (#30802), InternVL2 (#32397), MiniMax M2 (#32763).

Speculative decoding: EAGLE3 for Pixtral/LlavaForConditionalGeneration (#32542), Qwen3 VL MoE (#32048), draft model support (#24322).

Embeddings: BGE-M3 sparse embeddings and ColBERT embeddings (#14526).

Model enhancements: Voxtral streaming architecture (#32861), SharedFusedMoE for Qwen3MoE (#32082), dynamic resolution for Nemotron Nano VL (#32121), Molmo2 vision backbone quantization (#32385).

Engine Core

Async scheduling + Pipeline Parallelism: 
--async-scheduling
 now works with pipeline parallelism (#32359).

Mamba prefix caching: Block-aligned prefix caching for Mamba/hybrid models with 
--enable-prefix-caching --mamba-cache-mode align
. Achieves ~2x speedup by caching Mamba states directly (#30877).

Session-based streaming input: New incremental input support for interactive workloads like ASR. Accepts async generators producing 
StreamingInput
 objects while maintaining KV cache alignment (#28973).

Model Runner V2: VLM support (#32546), architecture improvements.

LoRA: Inplace loading for memory efficiency (#31326).

AOT compilation: torch.compile inductor artifacts support (#25205).

Performance: KV cache offloading redundant load prevention (#29087), FlashAttn attention/cache update separation (#25954).

Hardware & Performance

NVIDIA

Blackwell defaults: FlashInfer MLA is now the default MLA backend on Blackwell, with TRTLLM as default prefill (#32615).

MoE performance: 1.2-2% E2E throughput improvement via grouped topk kernel fusion (#32058), NVFP4 small-batch decoding improvement (#30885), faster cold start for MoEs with torch.compile (#32805).

FP4 kernel optimization: Up to 65% faster FP4 quantization on Blackwell (SM100F) using 256-bit loads, ~4% E2E throughput improvement (#32520).

Kernel improvements: topk_sigmoid kernel for MoE routing (#31246), atomics reduce counting for SplitK skinny GEMMs (#29843), fused cat+quant for FP8 KV cache in MLA (#32950).

torch.compile: SiluAndMul and QuantFP8 CustomOp compilation (#32806), Triton prefill attention performance (#32403).

AMD ROCm

MoRI EP: High-performance all2all backend for Expert Parallel (#28664).

Attention improvements: Shuffle KV cache layout and assembly paged attention kernel for AiterFlashAttentionBackend (#29887).

FP4 support: MLA projection GEMMs with dynamic quantization (#32238).

Consumer GPU support: Flash Attention Triton backend on RDNA3/RDNA4 (#32944).

Other Platforms

TPU: Pipeline parallelism support (#28506), backend option (#32438).

Intel XPU: AgRsAll2AllManager for distributed communication (#32654).

CPU: NUMA-aware acceleration for TP/DP inference on ARM (#32792), PyTorch 2.10 (#32869).

Whisper: torch.compile support (#30385).

WSL: Platform compatibility fix for Windows Subsystem for Linux (#32749).

Quantization

MXFP4: W4A16 support for compressed-tensors MoE models (#32285).

Non-gated MoE: Quantization support with Marlin, NVFP4 CUTLASS, FP8, INT8, and compressed-tensors (#32257).

Intel: Quantization Toolkit integration (#31716).

FP8 KV cache: Per-tensor and per-attention-head quantization via llmcompressor (#30141).

API & Frontend

Responses API: Partial message generation (#32100), 
include_stop_str_in_output
 tuning (#32383), 
prompt_cache_key
 support (#32824).

OpenAI API: 
skip_special_tokens
 configuration (#32345).

Score endpoint: Flexible input formats with 
data_1
/
data_2
 and 
queries
/
documents
 (#32577).

Render endpoints: New endpoints for prompt preprocessing (#32473).

Whisper API: 
avg_logprob
 and 
compression_ratio
 in verbose_json segments (#31059).

Security: FIPS 140-3 compliant hash option for enterprise/government users (#32386), 
--ssl-ciphers
 CLI argument (#30937).

UX improvements: Auto 
api_server_count
 based on 
dp_size
 (#32525), wheel variant auto-detection during install (#32948), custom profiler URI schemes (#32393).

Dependencies

FlashInfer v0.6.1 (#30993)

Transformers 4.57.5 (#32287)

PyTorch 2.10 for CPU backend (#32869)

DeepGEMM newer version (#32479)

Breaking Changes & Deprecations

Metrics: Removed deprecated 
vllm:time_per_output_token_seconds
 metric - use 
vllm:inter_token_latency_seconds
 instead (#32661).

Environment variables: Removed deprecated environment variables (#32812).

Quantization: DeepSpeedFp8 removed (#32679), RTN removed (#32697), HQQ deprecated (#32681).

Bug Fixes

Speculative decoding: Eagle draft_model_config fix (#31753).

DeepSeek: DeepSeek-V3.1 + DeepGEMM incompatible scale shapes fix (#32361).

Distributed: DP+MoE inference fix via CpuCommunicator (#31867), P/D with non-MoE DP fix (#33037).

EPLB: Possible deadlock fix (#32418).

NIXL: UCX memory leak fix by exporting UCX_MEM_MMAP_HOOK_MODE=none (#32181).

Structured output: Outlines byte fallback handling fix (#31391).

New Contributors 🎉

@YunzhuLu made their first contribution in #32126

@emricksini-h made their first contribution in #30784

@dsfaccini made their first contribution in #32289

@ofirzaf made their first contribution in #32312

@seekskyworld made their first contribution in #32321

@brian033 made their first contribution in #31715

@TomerBN-Nvidia made their first contribution in #32257

@vanshilshah97 made their first contribution in #32448

@George-Polya made their first contribution in #32385

@T1mn made their first contribution in #32411

@mritunjaysharma394 made their first contribution in #31492

@randzero made their first contribution in #32511

@DemingCheng made their first contribution in #32556

@iboiko-habana made their first contribution in #32471

@honglyua-il made their first contribution in #32462

@hyeongyun0916 made their first contribution in #32473

@DanielMe made their first contribution in #32560

@netanel-haber made their first contribution in #32121

@longregen made their first contribution in #28784

@jasonyanwenl made their first contribution in #32749

@Wauplin made their first contribution in #32788

@ikaadil made their first contribution in #32775

@alexsun07 made their first contribution in #28664

@liranschour made their first contribution in #30207

@AuYang261 made their first contribution in #32844

@diviramon made their first contribution in #32393

@RishabhSaini made their first contribution in #32884

@MatteoFari made their first contribution in #32397

@peakcrosser7 made their first contribution in #30877

@orionr made their first contribution in #30443

@marksverdhei made their first contribution in #32614

@joninco made their first contribution in #32935

@monajafi-amd made their first contribution in #32944

@ruizcrp made their first contribution in #32988

@sjhddh made their first contribution in #32983

@HirokenOvo made their first contribution in #32646

@Chenhao-Guan made their first contribution in #32763

@joshuadeng made their first contribution in #28973

@ZhanqiuHu made their first contribution in #33016

Full Changelog: v0.14.1...v0.15.0

Contributors

 orionr, DanielMe, and 37 other contributors
 

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍13adamw7, nussejzz, lishunyang12, uniqueni, hnts03-moreh, viratzzs, mjibril, alesalloum, SANYAHUN88, xieyc99, and 3 more reacted with thumbs up emoji😄1eveningcafe reacted with laugh emoji❤️8SurealCereal, ivanbaldo, eplatero97, mjibril, khaile, Mehryarmb, raadkasem, and NiKlimenko reacted with heart emoji🚀21wedobetter, tbbsaifa, jonzhep, MARD1NO, jlsan92, GosuDRM, antonio-lorenzon-ifood, SurealCereal, adrian-valente, koolvn, and 11 more reacted with rocket emoji
All reactions
👍13 reactions

😄1 reaction

❤️8 reactions

🚀21 reactions

37 people reacted

v0.14.1

 24 Jan 20:29
 

khluu

 v0.14.1
 

d7de043

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.14.1

This is a patch release on top of 
v0.14.0
 to address a few security and memory leak fixes.

Assets9
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍14onyxmaster, sophauer, yankeexe, myngsooo, Puiching-Memory, ivanbaldo, GosuDRM, rongchen, krishy91, Austin-Liang, and 4 more reacted with thumbs up emoji🚀5wedobetter, crossijinn, ikaadil, yankeexe, and mariorch22 reacted with rocket emoji
All reactions
👍14 reactions

🚀5 reactions

18 people reacted

v0.14.0

 20 Jan 09:20
 

khluu

 v0.14.0
 

b17039b

Compare

 Choose a tag to compare
 

Sorry, something went wrong.

 Filter

Loading

Sorry, something went wrong.

 Uh oh!

There was an error while loading. Please reload this page.

No results found

View all tags

v0.14.0

Highlights

This release features approximately 660 commits from 251 contributors (86 new contributors).

Breaking Changes:

Async scheduling is now enabled by default - Users who experience issues can disable with 
--no-async-scheduling
.

Excludes some not-yet-supported configurations: pipeline parallel, CPU backend, non-MTP/Eagle spec decoding.

PyTorch 2.9.1 is now required and the default wheel is compiled against cu129.

Deprecated quantization schemes have been removed (#31688, #31285).

When using speculative decoding, unsupported sampling parameters will fail rather than being silently ignored (#31982).

Key Improvements:

Async scheduling enabled by default (#27614): Overlaps engine core scheduling with GPU execution, improving throughput without user configuration. Now also works with speculative decoding (#31998) and structured outputs (#29821).

gRPC server entrypoint (#30190): Alternative to REST API with binary protocol, HTTP/2 multiplexing.

--max-model-len auto
 (#29431): Automatically fits context length to available GPU memory, eliminating OOM startup failures.

Model inspection view (#29450): View the modules, attention backends, and quantization of your model in vLLM by specifying 
VLLM_LOG_MODEL_INSPECTION=1
 or by simply printing the 
LLM
 object.

Model Runner V2 enhancements: UVA block tables (#31965), M-RoPE (#32143), 
logit_bias
/
allowed_token_ids
/
min_tokens
 support (#32163).

Please note that Model Runner V2 is still experimental and disabled by default.

Model Support

New Model Architectures:

Grok-2 with tiktoken tokenizer (#31847)

LFM2-VL vision-language model (#31758)

MiMo-V2-Flash (#30836)

openPangu MoE (#28775)

IQuestCoder (#31575)

Nemotron Parse 1.1 (#30864)

GLM-ASR audio (#31436)

Isaac vision model v0.1/v0.2 (#28367, #31550)

Kanana-1.5-v-3b-instruct (#29384)

K-EXAONE-236B-A23B MoE (#31621)

LoRA Support Expansion:

Multimodal tower/connector LoRA (#26674): LLaVA (#31513), BLIP2 (#31620), PaliGemma (#31656), Pixtral (#31724), DotsOCR (#31825), GLM4-V (#31652)

DeepSeek-OCR (#31569), Qwen3-Next (#31719), NemotronH (#31539), PLaMo 2/3 (#31322)

Vision LoRA mm_processor_cache support (#31927)

MoE expert base_layer loading (#31104)

Model Enhancements:

Qwen3-VL as reranker (#31890)

DeepSeek v3.2 chat prefix completion (#31147)

GLM-4.5/GLM-4.7 
enable_thinking: false
 (#3178

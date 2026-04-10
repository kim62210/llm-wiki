---
title: Releases · NVIDIA/TensorRT-LLM · GitHub
source_url: https://github.com/NVIDIA/TensorRT-LLM/releases
final_url: https://github.com/NVIDIA/TensorRT-LLM/releases
status: 200
content_type: text/html; charset=utf-8
topics: [TensorRT-LLM 1.3 with Day-0 Model Support]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:11.916911+00:00
---

# Releases · NVIDIA/TensorRT-LLM · GitHub

## 원본 URL

https://github.com/NVIDIA/TensorRT-LLM/releases

## 추출 본문

Releases · NVIDIA/TensorRT-LLM · GitHub

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

 NVIDIA
/TensorRT-LLMPublic

Notifications
You must be signed in to change notification settings

Fork
 2.3k

 Star
13.3k

Code

Issues572

Pull requests691

Discussions

Actions

Projects

Security and quality0

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

Releases: NVIDIA/TensorRT-LLM

ReleasesTags

Releases · NVIDIA/TensorRT-LLM

v1.3.0rc11

 09 Apr 12:57
 

VALLIS-NERIA

 v1.3.0rc11
 

4e69c14

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.3.0rc11Pre-release

Pre-release

Highlights

Model Support

Add Mistral 4-small support to AutoDeploy (#12266)

Add GlmMoeDsaForCausalLM to EPLB supported model list (#12607)

Add Qwen3-Next MTP (#11370)

Enable sliding window attention for Mistral/Mixtral (#12597)

API

Support include_stop_token_in_output in gRPC request manager (#12517)

Add deprecation warnings on TRT backend entrypoints (#11723)

Accept strict field in tools and store field in chat requests (#12482)

Mark TRTLLMSampler as deprecated and update documentation (#11938)

Move VisualGen APIs to a separate directory (#12538)

Remove some fields with redefined defaults (#11671)

Feature

Apply norm before FC in Eagle (#12561)

Split MLA DSA custom op for piecewise CUDA graph capture (#12503)

Optimize host performance for Python cache transceiver (#12273)

Add Mamba2 MTP SSM cache CUDA kernel for tree-based speculative decoding (#12537)

Add serve-config-guide skill for basic aggregate single-node serving configs (#12054)

Add FORCE_CHUNK context chunking policy (#12483)

Add dense GEMM backend for MoE (#10479)

Implement gen-first disaggregated scheduling, part 2 (#12239)

Support EPLB with various MoE backends for Nemotron-H models (#12280)

Skip softmax via sparsity ratio (#11995)

Add DWDP (distributed weight data parallelism) support for MoE inference (#12136)

Add AutoDeploy Super V3 MTP support (#12326)

Introduce fast path (token IDs + multimodal) for VLMs without re-tokenizing encoded prompts (#11708)

Add global pool support for suffix automaton speculative decoding (#12130)

Add Triton paged attention for AutoDeploy (#12642)

Refactor VisualGen attention backend (#12663)

Add support of linear attention state for C++ KV cache manager (#12531)

Add temporally-correlated heuristic-guided indexer TopK for sparse attention (#12385)

Support MLA generation in TrtllmGen attention backend (#12606)

Extend Python cache transceiver to support Nemotron (#12150)

Handle different chat template types (#12336)

Add multi-turn support for trtllm-bench (#12468)

Add fused DiT QK Norm + RoPE CUDA kernel for FLUX (#11869)

Support cache reuse for SSM in KVCacheManagerV2 (#12644)

Add MLIR-based auto-generated elementwise fusion for AutoDeploy (#12427)

Add --custom_tokenizer CLI option to trtllm-bench (#12586)

Support LoRA adapter for Nemotron-H models (#12154)

Apply multiple host performance optimizations for DSA (#12581)

Reuse Triton slicing kernel for GDN prefill transpose (#12737)

Add Trtllm-gen FMHA JIT support (#12612)

Retune causalConv1d forward dispatch for variable-length and short sequences (#12739)

Update configuration to enable NVFP4 (#12776)

Fuse SiLU+Mul in AutoDeploy transform (#12497)

Fix

Fix Triton kernels in wheel (#12569)

Fix DSACacheManager and RocketCacheManager KV cache estimation ignoring num_layers for draft models (#12571)

Reorder generation_logits to align with final beam search output ordering (#12268)

Handle CUDA_ERROR_INVALID_VALUE in kv_cache_v2 _is_prop_supported (#12613)

Fix autotuner OOM for trtllmGen MoE runners at large context length (#12523)

Always sync sampler_event in update_requests (#12585)

Avoid counting KV cache uses during warmup for Prometheus KV cache metrics (#12132)

Fix lost requests (#12348)

Fix GPTOSS CUTLASS MoE on Hopper NVLink one-sided workspace overflow (#12666)

Fix Mooncake dynamic load in transfer_agent_binding (#12181)

Fix disaggregated pipeline-parallel hang (#12528)

Correct reused block counting in corner case (#12404)

Clamp block indices to prevent out-of-bounds in DSA with MTP (#12657)

Synchronize NCCL memory allocation error handling (#12125)

Adjust prompt logprobs to use the correct prompt token id (#12499)

Improve NIXL agent import error diagnostics (#12446)

Fix disaggregated serving hang on block reuse after eviction (#12667)

Use the first non-None result returned by Hugging Face download workers (#12259)

Replace assertions with warnings for unsupported logits/logprobs in speculative sampler (#12547)

Address H20 weights loading OOM for GPTOSS (#11321)

Improve Harmony parser (delta grouping, reuse report, test coverage) (#12467)

Fix hang issues on DGX B200 8-GPU PyTorch configurations (#12656)

Fix disaggregated KV cache router for chat API; add disaggregated benchmark for ai_perf (#12337)

Fix CUDA event crash with performance metrics (#12639)

Update Nemotron-H handling for corner cases (#12620)

Fix KV cache issue (#12673)

Fix wrong token suppressed with ignore_eos in Torch sampler (#12358)

Fix GPTOSS chat template for disaggregated tests (#12724)

Fix top-K logprobs size for pipeline parallelism (#12623)

Remove clone in FP8 quantization (#12687)

Fix Qwen2.5 mixed precision accuracy issue (#12609)

Fix Mamba metadata prefill bubble in chunked prefill serving (#12736)

Fix outdated README argument for executorExampleDisaggregated.cpp (#12276)

Documentation

Add MoE developer guide for fused_moe module (#12534)

Update supported models to include Kimi K2/K2.5 and GLM-5 (#12654)

Publish blog post for DWDP (#12725)

Add visual generation models to supported models page (#12464)

Clean up latest news and blogs; update overview and highlight visual generation (#12753)

Update C++ coding guidelines (#12577)

Test & Infra

Use shared utility for node labels (#9095)

Adjust RocketKV test threshold (#12527)

Enhance performance tests with GPU availability check in test_perf.py (#12535)

Move AD performance regression tests to AD pre- and post-merge jobs (#12461)

Remove Model Registry Check from workflows; check runs in pre-commit (#12590)

Add Ubuntu 24.04 wheel image for SBSA (#12436)

Pin mypy version due to dependency conflicts (#12650)

Fix Pyxis error in disaggregated performance test (#12575)

Skip already-applied patches gracefully in third-party FetchContent (#12550)

Add container scanning to PLC nightly pipeline (#12549)

Use JobBuilder to trigger downstream job (#7079)

Prefer GitHub then GitLab for TOT waive list (#11063)

Isolate single-GPU Ray orchestrator tests to avoid CI timeouts (#12616)

Add workaround for trtllm-bench hang and improve robustness (#12655)

Bump tornado and black in container (#12600)

Remove OOM test case from L40S test list (#12685)

Temporarily disable warn_unused_ignores (#12728)

Add supplemental Ruff lint for legacy files via ruff-legacy hook (#11469)

Add port conflict retry for disaggregated multi-process tests (#12618)

Add CI agent failure analysis to L0 merge request pipeline (#12543)

Fix source code scanning (#12773)

Remove gpu-shell tool from ad-run-agent (#12418)

Move to FlexCache in Austin for 5080 nodes (#12615)

What's Changed

[https://nvbugs/5882636][fix] Fix triton_kernels in wheel by @dongfengy in #12569

[https://nvbugs/5919796][test] AutoDeploy: unwaive Super V3 autodeploy failure by @galagam in #12556

[None][test] Waive another flaky test case on Dis-agg serving with Ne… by @nv-guomingz in #12587

[#11992][fix] Support include_stop_token_in_output in gRPC request manager by @CatherineSue in #12517

[None][feat] Eagle: Norm before FC by @IzzyPutterman in #12561

[#10607][fix] moved AD perf regression tests to AD jobs pre and post merge by @MrGeva in #12461

[None][infra] Waive 1 failed cases for main in post-merge 2626 by @ZhanruiSunCh in #12592

[TRTLLM-7335] [infra] Use shared utility for node labels by @niukuo in #9095

[None][infra] Waive 1 failed cases for main in pre-merge 31714 by @ZhanruiSunCh in #12589

[https://nvbugs/6007197][fix] Adjust RocketKV test threshold by @heyuhhh in #12527

[None][test] Enhance performance tests by adding GPU availability check in test_perf.py by @yufeiwu-nv in #12535

[None][infra] Waive 2 failed cases for main in post-merge 2627 by @ZhanruiSunCh in #12605

[None][fix] Fix DSACacheManager and RocketCacheManager KV cache estimation ignoring num_layers for draft models by @lancelly in #12571

[None][doc] Add MoE developer guide for fused_moe module by @xxi-nv in #12534

[None][chore] Remove Model Registry Check from workflows, the check already runs in pre-commit by @tcherckez-nvidia in #12590

[https://nvbugs/5983390][perf] Split MLA DSA custom op for piecewise CUDA graph capture by @liji-nv in #12503

[None][fix] Reorder generation_logits to align with final beam search output ordering by @achartier in #12268

[TRTC-351][chore] Deprecation warnings on TRT backend entrypoints by @venkywonka in #11723

[TRTLLM-10804][infra] add ubuntu2404 wheel image for SBSA by @niukuo in #12436

[#12288][feat] Add Mistral 4-small support to AutoDeploy by @bmarimuthu-nv in #12266

[None][infra] waive failed case for main by @EmmaQiaoCh in #12621...

Read more

Contributors

 karljang, reasonsolo, and 74 other contributors
 

Assets2
Loading

 Uh oh!

There was an error while loading. Please reload this page.

All reactions

v1.3.0rc10

 31 Mar 10:02
 

VALLIS-NERIA

 v1.3.0rc10
 

628bb56

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.3.0rc10Pre-release

Pre-release

Highlights

Model Support

Add Qwen 3.5 NVFP4 support (#12302)

Fuse all-reduce with norm for Nemotron-H models (#12410)

API

Add request priority support to the LLM API (#12362)

Change log prob behavior to stop normalizing by default (BREAKING) (#12366)

Feature

Add CuTe DSL single-pass multi-CTA cluster top-k (#12354)

Account for reusable KV cache blocks in micro-batch scheduler capacity scheduling (#11637)

Add raster-along-M/N support for blockscaled contiguous backbone kernels in CuteDSL MoE (#12079)

Add stride support for 
conv1d
 and 
fused_sigmoid_gating_delta_rule_update
 (#12442)

Add a safe allgather implementation with chunking (#12174)

Add dynamic SMEM block routing in MoE (#12456)

Optimize 
mamba_mixer2.py
 decode performance (#11843)

Add PDL support to CuTE DSL top-k kernels (#12506)

Add FlexKV support (#12512)

Add a KV cache-aware ADP router for prefix-affinity request routing (#12315)

Fix

Fix KV token estimation when ADP is enabled (#12099)

Fix Eagle MLA target with GQA draft support (#12171)

Fix Qwen 3.5 3D position ID handling (#12114)

Switch tests to 
TorchSampler
 and fix related bugs (#12200)

Use 
ceil_div
 for head and size sharding (#12441)

Remove redundant D2H synchronization to improve performance (#12445)

Fix parallel WAN VAE when 
return_dict=True
 (#12460)

Fix Triton resmooth kernel crashes on SM100f for large MoE grids (#12397)

Use a model-level warmup cache key for visual generation pipelines (#12516)

Add NVTX annotations in 
sampler.py
 (#12459)

Use 
extra_visual_gen_options
 to improve visual generation routing (#12487)

Documentation

Fix outdated code references in tech blogs 2, 3, 4, 8, 9, and 11 (#12338)

Document temperature-adjusted logprobs in the TRT backend (#12514)

Update Python coding guidelines (#12439)

Test & Infra

Save unittest subtest results periodically (#11850)

Fix the B200 aggregated CI perf test MPI issue (#12347)

Fix LoRA config handling when the provided config count is below requirements (#12409)

Add a unit test for 
load_state_dict
 safetensors fallback (#12408)

Replace the skipped TRTLLM NVFP4 test in the B300 CI list (#12454)

Fix the ltx-2 model checkpoint issue in VBench eval tests (#12463)

Fix the concurrent write issue in perf tests (#12484)

Update dependencies to align with the NGC PyTorch 26.02 stack (#12102)

Consolidate PyTransceiver code (#12342)

Add Eagle coverage with different input/output cases on Spark (#12520)

What's Changed

[None][infra] Waive 4 failed cases for main in post-merge 2611 by @ZhanruiSunCh in #12433

[None][test] Fix lora config less than required config number by @yufeiwu-nv in #12409

[https://nvbugs/5916151][fix] Unwaive test_fused_moe_w4a8_nvfp4_fp8[TRTLLM] by @xxi-nv in #12400

[https://nvbugs/5963423][fix] Fix kv token estimation when ADP is on. by @dominicshanshan in #12099

[TRTLLM-11229][infra] Save unittest subtest results periodically by @yiqingy0 in #11850

[None][chore] Add failed cases into waives.txt by @xinhe-nv in #12426

[https://nvbugs/5997090][fix] Fix B200 Aggregated CI Perf Test MPI Issue by @chenfeiz0326 in #12347

[TRTLLM-10407][perf] Add cute dsl single pass multi cta cluster topk by @limin2021 in #12354

[TRTLLM-11070][feat] Account for reusable KV cache blocks in micro batch scheduler capacity scheduling. by @SimengLiu-nv in #11637

[None][chore] Fixing guardword check by @pcastonguay in #12455

[None][infra] Waive 1 failed cases for main in post-merge 2610 by @ZhanruiSunCh in #12434

[None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel by @liyuhannnnn in #12079

[None][fix] Switch tests to TorchSampler and fix bugs by @Funatiq in #12200

[TRTLLM-10061][fix] Use ceil_div for head/size calculations by @VALLIS-NERIA in #12441

[TRTLLM-10061][feat] Add stride support for conv1d and fused_sigmoid_gating_delta_rule_update by @VALLIS-NERIA in #12442

[None][fix] Eagle: MLA Target + GQA Draft by @IzzyPutterman in #12171

[None][doc] fix outdated code references in tech blogs 2, 3, 4, 8, 9, 11 by @schetlur-nv in #12338

[TRTLLM-11471][feat] Add safe version of allgather with chunking by @chienchunhung in #12174

[None][perf] add Dynamic SMEM block routing in MOE by @jiahanc in #12456

[TRTLLM-11544][feat] Add Qwen 3.5 supporting(NVFP4). by @nv-guomingz in #12302

[https://nvbugs/5997090][fix] Add Disagg Perf Test back as MPI Issue has been fixed by @chenfeiz0326 in #12458

[https://nvbugs/5841976][fix] Remove test_fused_moe_alltoall_fp4[DeepEP] from waives by @xxi-nv in #12405

[None][infra] Waive 2 failed cases for main in post-merge 2613 by @ZhanruiSunCh in #12473

[https://nvbugs/5866619][test] Add unit test for load_state_dict safetensors fallback by @crazydemo in #12408

[None][feat] Fuse all_reduce with norm for nemotron_h models by @Wanli-Jiang in #12410

[None][infra] Update CI allowed list by @yuanjingx87 in #12488

[https://nvbugs/6013562][test] Update waive by @xinhe-nv in #12492

[None][feat] Small optimizations for mamba_mixer2.py decode by @hnover-nv in #11843

[None][infra] Waive flaky DeepSeekV3Lite disagg serving test by @hyukn in #12494

[#11526][chore] AutoDeploy accuracy tests: Use Llama3.1-8B-Instruct official checkpoints by @galagam in #12285

[https://nvbugs/6007285][fix] Replace skipped TRTLLM NVFP4 test in B300 CI list by @xxi-nv in #12454

[https://nvbugs/5983390][fix] Remove redundant D2H sync to optimize perf by @hyukn in #12445

[https://nvbugs/5987470][fix] BREAKING: Do not normalize log probs by default by @achartier in #12366

[TRTLLM-11622][fix] fix parallel WAN vae when return_dict=True by @NVShreyas in #12460

[None][infra] Waive pre-merge failed 5090 test by @yuanjingx87 in #12486

[None][infra] Waive flaky DeepSeekV3Lite disagg serving test by @bo-nv in #12518

[None][chore] Fix ltx-2 Model Checkpoint Issue in VBench Eval Tests by @yibinl-nvidia in #12463

[https://nvbugs/5962591][fix] Fix Triton resmooth kernel crash on SM100f for large MoE grids by @Barry-Delaney in #12397

[None][chore] Add failed cases into waives.txt by @xinhe-nv in #12495

[None][doc] Document temperature-adjusted logprobs in TRT backend by @achartier in #12514

[None][feat] Add PDL support to CuTE DSL top-k kernels by @limin2021 in #12506

[None][infra] Waive 4 failed cases for main in post-merge 2617 by @ZhanruiSunCh in #12536

[None][doc] Update Python coding guidelines. by @hnover-nv in #12439

[#12290][fix] Qwen 3.5 fix 3d position ID handling by @bmarimuthu-nv in #12114

[TRTLLM-10820][infra] Update dependencies to align with NGC PyTorch 26.02 stack by @EmmaQiaoCh in #12102

[https://nvbugs/6015329][fix] Use model-level warmup cache key for visual gen pipelines by @karljang in #12516

[TRTLLM-9523][chore] PyTransceiver code consolidation by @Shixiaowei02 in #12342

[None][test] Add different input-output of eagle cases on Spark by @JennyLiu-nv in #12520

[https://nvbugs/6011086][fix] Fix Perf Test's Concurrent Write Issue by @chenfeiz0326 in #12484

[None][fix] NVTX annotation in sampler.py by @ixlmar in #12459

[https://nvbugs/5998489][feat] Adding support for request priority in LLM API by @pcastonguay in #12362

[None][feat] Add support for FlexKV by @pcastonguay in #12512

[None][feat] KV cache-aware ADP router for prefix-affinity request routing by @lancelly in #12315

[https://nvbugs/6008183][fix] Use extra_visual_gen_options to help de… by @JunyiXu-nv in https://github.com/NVIDIA/T...

Read more

Contributors

 karljang, achartier, and 35 other contributors
 

Assets2
Loading

 Uh oh!

There was an error while loading. Please reload this page.

❤️3sizorlee, SethHWeidman, and ConstBob reacted with heart emoji
All reactions
❤️3 reactions

3 people reacted

v1.3.0rc9

 24 Mar 17:08
 

pcastonguay

 v1.3.0rc9
 

3353334

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.3.0rc9Pre-release

Pre-release

Highlights

Model Support

Add Qwen3-next attention DP support (#10218)

Improve DeepSeek-V3.2 NVFP4 indexer GEMMs and routing kernels (#11989, #12055)

Support KV cache and speculative decoding in the Trtllm-Gen attention backend (#11667, #12267)

Add audio support and chunked-prefix enablement for Nemotron models (#12191, #12414)

Add GLM 5 support and fix DSA MTP issues (#11990)

Add initial Qwen3.5 text model support for the PyTorch backend with BF16/FP8 (#12242)

API

Add energy metrics to 
trtllm-serve
 and benchmarking workflows (#11855)

Expose 
video_pruning_rate
 in 
llmargs
 and improve Nano V2 VL handling (#12194)

Add 
TLLM_PROFILE_LOG_RANKS
 to control per-rank step logging (#12263)

Improve the serve CLI with renamed flags and 
mm_embedding_serve
 enhancements (#12105)

Add an 
auto
 option for tool and reasoning parsers (#12104)

Support interleaved thinking in 
trtllm-serve
 (#12199)

BREAKING: Set the default KV cache transfer timeout to 60 seconds (#12249)

Feature

Add FP8 combine support in 
moe_a2a
 (#11844)

Add batch generation support to visual generation pipelines (#12121)

Improve request management in the sampler (#11861)

Add fused AllReduce + RMSNorm with optional residual support (#12201)

Add constraint-based memory partitioning and a Python scheduler for 
KVCacheManagerV2
 (#12212, #11939)

Add LM head sharding (#12252)

Add an interactive recipe selector with curated configs and button-grid UI (#11917)

Improve DSA and FlashMLA performance with new kernel fusions and cached tile-scheduler metadata (#12322, #12161)

Improve model performance with CuteDSL 
indexer_top_k
, FlashInfer MLP activation, and refined KV cache buffer sizing (#12236, #12131, #12274)

Fix

Fix disaggregated perf test result generation, env export, and port allocation issues (#12211, #12140)

Fix harmony and tool-calling parsers for agentic coding use cases (#12045)

Fix torch.compile compatibility by routing DSA attention through the MLA custom op (#12186)

Fix 
min_tokens
 handling for long prompts and return explicit scheduling errors when requests cannot be placed (#12166, #12206)

Fix KV cache V2 OOMs and weight-loading OOMs in disaggregated serving (#12188, #12377)

Fix lost requests, dummy-request crashes, and 
GUIDE_TYPE_STRUCTURAL_TAG
 handling in request management paths (#12197, #12403, #12330)

Fix W4A16 AWQ bias handling on SM100 and add bias support to 
WeightOnlyQuantLinearMethod
 (#12190, #12317)

Fix MiniMax model loading and multimodal loading error propagation (#12182, #12331)

Fix MTP/DSA reliability, PARD accuracy, and NVFP4 MoE mixed-precision scales (#12010, #12360, #12240)

Fix DGX Spark multi-node hangs, cross-node rollout issues in Verl, and 
CUDA_VISIBLE_DEVICES
 propagation in scripts (#12316, #11924, #12370)

Fix build and runtime issues for SM103 context-attention kernels, L40s IB transfers, LlavaNext dtype fallback, and MnnvlMemory resource cleanup (#12248, #12152, #12169, #11979)

Add warmups to avoid AIPerf timeouts and I2V torch.compile recompilation (#12178, #12351)

Pre-cache aesthetic predictor weights to avoid VBench 429 failures (#12127)

Documentation

Add the NVLink one-sided AlltoAll blog post and improve tech blog sequencing and links (#12195, #12386, #12425)

Update the Nemotron 3 Super deployment guide for tool calling and reasoning parsers (#12215)

Update the README and other developer-facing documentation (#12307, #12258)

Test & Infra

Limit pre-merge pre-commit checks to changed files (#11379)

Use CPU affinity instead of raw CPU count for default build parallelism (#12167)

Add broader performance, accuracy, and end-to-end coverage for Nemotron, DeepSeek-V3.2, disaggregated serving, FLUX, and DSA host-cache offload (#12184, #12142, #12275, #12279, #12278, #12153)

Update multi-node and MPI-related test coverage (#12075, #12300)

Add SSH key authentication support for SLURM clusters (#12172)

Use the public PyTorch index as a CI fallback and update the CI allowlist (#12261, #12296)

Enable type checking for sampler modules and improve Python KV transceiver coverage (#11678, #11574)

Remove outdated QA coverage and refactor benchmarking and test infrastructure (#12277, #12344, #12124, #11720, #12192)

What's Changed

[TRTLLM-10929][feat] add fp8 combine in moe_a2a by @dc3671 in #11844

[TRTLLM-9767][feat] Enable attention dp for qwen3-next. by @nv-guomingz in #10218

[None][fix] Fix Disagg Perf Test No result.xml Bug by @chenfeiz0326 in #12211

[https://nvbugs/5955188][fix] Fix harmony parsers for agentic coding use cases by @dongfengy in #12045

[https://nvbugs/5973536][fix] Route DSA attention through MLA custom op for torch.compile compatibility by @yizhang-nv in #12186

[https://nvbugs/5823135][fix] Fix min_tokens not respected when prompt is long by @JunyiXu-nv in #12166

[None][doc] Blog18 for NVLinkOneSided AlltoAll. by @bobboli in #12195

[None][chore] Remove closed bugs by @xinhe-nv in #12222

[None][fix] Fix KV cache V2 OOM with separate draft KV cache (EAGLE3/MTP) by @yizhang-nv in #12188

[None][doc] AutoDeploy: ad-model-onboard skill updates by @bmarimuthu-nv in #12234

[TRTLLM-10569][infra] Only check the changed files in pre-commit in pre-merge CI by @yiqingy0 in #11379

[https://nvbugs/5948878][fix] fix lost requests by @bo-nv in #12197

[None][chore] Add failed cases into waives.txt by @xinhe-nv in #12218

[None][chore] fix deepep trtllm backend MXFP4 by @leslie-fang25 in #12219

[None][chore] Alltoall benchmark script refine (second time). by @bobboli in #12192

[None][chore] Add failed cases into waives.txt by @xinhe-nv in #12220

[None][fix] Fix W4A16 AWQ bias not applied on SM100 (Blackwell) by @Tracin in #12190

[None][fix] Export computed env vars to env_vars.json and fix port allocation in disagg benchmark by @qiaoxj07 in #12140

[TRTLLM-11288][fix] Adapt LTX2 pipeline to CompilationConfig warmup interface by @luyiyun1021 in #12232

[https://nvbugs/5955927][fix] Add warm up before aiperf to fix timeout issue. by @dominicshanshan in #12178

[None][refactor] Improve request management in sampler by @Funatiq in #11861

[None][chore] Use affinity rather than CPU count for default build parallelism by @achartier in #12167

[None][feat] Support kv cache in Trtllm-Gen attention backend by @yihwang-nv in #11667

[None][docs] Update nemotron 3 super deployment to include tool calling and reasoning parser by @tijyojwad in #12215

[None][fix] Add more models to increase perf test coverage by @chenfeiz0326 in #12184

[TRTLLM-9521][feat] Unfuse indexer.wk from attention GEMM for DS-V3.2 NVFP4 by @peihu-nv in #11989

[https://nvbugs/5879588][fix] fix MiniMax model loading bugs by @jmydurant in #12182

[TRTLLM-10333][feat] Add energy metrics in trtllm-serve and benchmark… by @JunyiXu-nv in #11855

[None][test] Update nemotron super test cases with official ckpt. by @nv-guomingz in #12142

[None][fix] Reliability fixes for MTP with DSA and support host cache offload for DSA by @dmtri35 in #12010

[None][infra] Waive 5 failed cases for main in post-merge 2599 by @ZhanruiSunCh in #12283

[None][infra] use public torch index as CI backup by @tburt-nv in #12261

[TRTLLM-11362][feat] Add batch generation support to visual gen pipelines by @karljang in #12121

[https://nvbugs/5973801][fix] exclude subproc_worker_timer from thread leak checks by @MrGeva in #12286

[#11432][feat] AutoDeploy: Enable fp8 quantization fusion part 1 by @galagam in #11910

[#10931][feat] AutoDeploy: one-model spec dec by @lucaslie in #11701

[https://nvbugs/5973536][fix] Add NVFP4+FP8KV+MTP accuracy specs for DeepSeek-V3.2-Exp by @yizhang-nv in #12269

[#11368][fix] FP4 CUTLASS GEMM shared memory overflow on GB10 (SM121) by @mihai-chiorean in #12141

[TRTLLM-11267][feat] Add audio support for nemotron by @2ez4bz in #12191

[None][feat] GLM 5 support and DSA MTP fixes by @NVShreyas in #11990

[None][fix] Relax MoE test tolerance for fp16 TP mode accuracy mismatch by @xxi-nv in https://github.com/NVIDIA/Tenso...

Read more

Contributors

 karljang, tijyojwad, and 69 other contributors
 

Assets2
Loading

 Uh oh!

There was an error while loading. Please reload this page.

❤️2sizorlee and xwuShirley reacted with heart emoji
All reactions
❤️2 reactions

2 people reacted

v1.3.0rc8

 17 Mar 19:43
 

pcastonguay

 v1.3.0rc8
 

73cca36

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.3.0rc8Pre-release

Pre-release

Highlights

Model Support

Nemotron 3 Super support

Add tool parser support for GLM-4 models (#11986)

Implement dynamic resolution for Nemotron VL (#11894)

Enable mixed quantization support for Nemotron-H Mamba (#11972)

Add VisualGen FA4 attention backend support (#11697)

VisualGen support for LTX-2, Wan and FLUX (#12009)

Add TRTLLM-Gen kernels for GLM4.7 and support 
groupsTokensHeadsQ
 and 
e2m1
 output (#11643)

Support attention-DP for TRTLLM-Gen NVFP4 MoE (#12156)

API

Add dedicated virtual memory tags for model weights and configurable restore mode (#11889)

Add abort method for 
GenerationResultBase
 (#11970)

Deprecate 
trtllm-serve
 CLI options (#12106)

Add keepalive ping tolerance and 
context.abort
 support to the gRPC server (#11992)

Feature

Add basic SSM support in 
KVCacheManagerV2
 (#11976)

Improve KV event batching (#11883)

Add 2FP4 / Arcquant support (#11333)

Adapt the transceiver to manager v2 (step 6) (#11978)

Add shared expert LoRA support for MoE models in the PyTorch backend (#11760)

Add dynamic draft length on the one-model speculative decoding path (#10860)

Enable configurable warmup shapes for VisualGen (#12107)

Add FlashInfer API support for 
TRTLLMGenFusedMoE
 (#10453)

Add Python cache transceiver support for gen-first workflow (#11941)

Fix

Upgrade Cutlass version (#11956)

Fix DS v32 tool calling type and parse errors (#11935)

Fix protobuf and 
aiohttp
 vulnerabilities (#11898)

Fix NVFP4 sharding (#11618)

Fix Kimi-K2.5 accuracy test skip condition and reference configs (#11930)

Pass 
sparse_attn_config
 from 
effective_draft_config
 for one-model draft KV cache (#12032)

Fix MTP advanced sampling top-k IMA (#12088)

Revert refactor of the KV connector integration in py_executor, which caused issues with KVBM (#11872)

Fix sharding overwrite with multiple graph modules (#12051)

Fix various agentic flow issues (#12061)

Split 
mContextChunkSize
 into per-target and per-draft fields (#12058)

Fix 
ValueError
 and missing decoding statistics for MTP (#12063)

Improve NCCL library load stability (#12015)

Disable TRTLLM-Gen routing PDL due to NaN issues (#11994)

Enforce a minimum 
NVSHMEM_QP_DEPTH
 of 128 for DeepEP low latency (#12100)

Narrow a bare 
except
 clause and use identity checks for 
None
 (#12041)

Fix MoE DeepEP hangs caused by non-deterministic GC (#12060)

Fix 
KVCacheManagerV2
 shrink behavior for the last level and improve 
init_ratio
 (#12112)

Fix Mamba cache handling for PP > 1 (#12146)

Handle 
anyOf
 parameter schemas in the Qwen3Coder tool parser (#12173)

Add explicit errors for intermediate-size misalignment with the FP8 block size (#12101)

Fix DeepEP with the TRTLLM MoE backend for sequence length 1 (#12158)

Improve port retry loops and exception handling (#12225)

Add streaming support for 
no </think>
 on Nemotron models (#12176)

Documentation

Clarify DCO sign-off and co-author guidelines in 
AGENTS.md
 (#12034)

Add a deployment guide for Nemotron 3 Super (#12129)

Benchmark

Add QA perf test cases with L0 local mode (#12022)

Align performance benchmark output format (#12067)

Improve sampler performance by replacing 
torch.where
 with 
masked_fill_
 (#11949)

Add a fused 
cat
 + 
fp8_quantize
 CUDA kernel for the DSA indexer (#11899)

Optimize long-sequence token-parallel prefill for the DSA indexer (#11871)

Reduce 
logprobs=0
 overhead in 
TorchSampler
 (#11983)

Refine AlltoAll benchmark scripts (#11649)

Optimize the Q3N decode kernel with IO reads (#11344)

Fix disaggregated gen-only benchmark coverage (#12091)

Fix MPI issues and port conflicts in disaggregated performance tests (#12020)

Add GB200 performance sanity tests to the QA test database (#11882)

Refactor parallel VAE support (#12123)

Optimize 6KD FP8 blockscale GEMM (#11502)

Optimize Qwen3.5 performance (#11581)

Restore 3 disaggregated gen-only tests (#12159)

Test & Infra

Fix disaggregated SKU coverage (#12065)

Fix upload build info branch handling and ensure it always runs in post steps (#12025)

Fix the CI issue for Mistral Large3 (#12073)

Enable more KV connector priority tests in CI (#11892)

Add speculative decoding tests for 
exclude_input_in_output=true
 (#12080)

Add E2E tests for the KV cache connector async loading path (#12053)

Change the image used for the CI preparation step (#12086)

Add the 
verl
 stage in CI (#11306)

Add multi-node E2E and accuracy cases on DGX-Spark (#12110)

Update NumPy to version 2 (#11280)

What's Changed

[None][feat] Add Auto-Deploy dashboard failures analysis skill by @tcherckez-nvidia in #12033

[https://nvbugs/5820511][fix] Upgrade Cutlass version by @pamelap-nvidia in #11956

[None][feat] Add AD model list validation checks to pre-commit and PR… by @tcherckez-nvidia in #12036

[None][chore] Clarify DCO sign-off and co-author guidelines in AGENTS.md by @kaiyux in #12034

[TRTLLM-7784][feat] Basic SSM support in KVCacheManagerV2 by @lowsfer in #11976

[None][test] Add QA's perf test cases with L0 local mode by @fredricz-20070104 in #12022

[TRTLLM-11246][feat] Add tool parser support for GLM-4 models by @JunyiXu-nv in #11986

[https://nvbugs/5937478][fix] Fix DS v32 tool calling type and parse error by @JunyiXu-nv in #11935

[TRTLLM-11135][fix] Fix vulnerabilities protobuf and aiohttp by @yiqingy0 in #11898

[None][chore] Align perf benchmark output format by @yingguo-trt in #12067

[None][chore] Improve sampler performance by replacing torch.where with masked_fill_ by @stnie in #11949

[None][infra] Waive 1 failed cases for main in post-merge 2582 by @ZhanruiSunCh in #12069

[TRTLLM-10421][perf] Add fused cat+fp8_quantize CUDA kernel for DSA indexer by @kaiyux in #11899

[None][test] Fix disagg sku by @fredricz-20070104 in #12065

[https://nvbugs/5892646][perf] Long-sequence token-parallel optimization for DSA indexer prefill by @nvxuanyuc in #11871

[TRTLLM-11265][feat] Implement dynamic resolution for Nemotron VL by @2ez4bz in #11894

[https://nvbugs/5708901][perf] reduce logprobs=0 overhead in TorchSampler by @ixlmar in #11983

[None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) by @tcherckez-nvidia in #11652

[https://nvbugs/5963896][fix] Remove test 
test_visual_gen_quickstart
 on A10 by @chang-l in #12048

[TRTLLM-11535][feat] Fixed NVFP4 sharding by @greg-kwasniewski1 in #11618

[None][fix] Improve KV Event Batching by @jthomson04 in #11883

[None][chore] Add failed cases into waives.txt by @xinhe-nv in #12047

[TRTLLM-11276][fix] Fix Kimi-K2.5 accuracy test skip condition and reference configs by @lancelly in #11930

[https://nvbugs/5919026][fix] Pass sparse_attn_config from effective_draft_config for one-model draft KV cache by @chenfeiz0326 in #12032

[None][fix] MTP Advanced Sampling Topk IMA by @IzzyPutterman in #12088

[None][fix] Revert "[None][chore] KV Connector Refactor (#11078)" by @jthomson04 in #11872

[None][chore] Bump version to 1.3.0rc8 by @yuanjingx87 in #12090

[None][chore] Refine AlltoAll benchmark scripts. by @bobboli in #11649

[None][feat] 2FP4 / Arcquant. by @Tracin in #11333

[None][fix] Fix Upload Build Info branch and run in post always by @mzweilz in #12025

[TRTLLM-11366][feat] Add dedicated virtual memory tag for model weights, configurable restore mode by @tongyuantongyu in #11889

[https://nvbugs/5961430][fix] Fix CI issue of Mistral Large3 by @byshiue in #12073

[None][test] add Perf sanity gb200 test into QA test db by @xinhe-nv in #11882

[None][infra] Waive 2 failed cases for main in post-merge 2584 by @ZhanruiSunCh in #12108

[None][chore] Waive mpi hang test case by @jieli-matrix in #12077

[None][chore] re-enable benchmark test in post merge by @zhenhuaw-me in #12035

[None][feat] Mamba optimization and mixed quantization support for nemotron-h by @Wanli-Jiang in #11972

[None][fix] Various fixes for agentic flow by @2ez4bz in #12061

[https://nvbugs/5936322][fix] Fix sporadic port collision in multigpu AutoDeploy tests by @MrGeva in https://githu...

Read more

Contributors

 Superjomn, tijyojwad, and 62 other contributors
 

Assets2
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍2sizorlee and actypedef reacted with thumbs up emoji
All reactions
👍2 reactions

2 people reacted

v1.2.0

 12 Mar 19:43
 

pcastonguay

 v1.2.0
 

51f5ef3

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.2.0Latest

Latest

Highlights

Model Support

Added beta support for K-EXAONE, Nemotron Nano V3, Qwen3-Next and Qwen3-VL.

Improved GPT-OSS, Nemotron, EXAONE, GLM, Starcoder2, Qwen3, KimiK2, DeepSeek v3.2 and Mistral Large 3 support and validation.

Expanded Blackwell/Hopper/Ampere enablement including B300/GB200/GB300 and SM120/SM121/SM103 paths.

Broadened low-precision and MoE capabilities (FP8/NVFP4/MXFP4/INT4-AWQ), including routing and kernels.

Features

Speculative Decoding:
Enabled MTP>1 support for DeepSeek v3.2

Disaggregated Serving:
Added service discovery mechanism for dynamic scaling

Added support for cancelling requests

Added NIXL-LibFabric support

Added support for Mooncake transfer engine as a cache transceiver backend

Sampling:
Implemented batched sampling using FlashInfer sampling

Added support for returning logprobs incrementally with streaming mode in PyTorch backend

Added Beam Search support to TorchSampler

Performance:
Improved TorchSampler performance

Enabled PDL by default and added PDL support for indexer TopK and additional kernels.

Improved trtllm-gen kernels

Enabled early exit with overlap scheduler

Added NUMA-aware CPU affinity automatic configuration

Expert Parallelism:
Enabled EPLB for trtllm-gen and cutlass backend

Enabled CuteDSL MoE with large EP

Added CUDA graph support for DeepEP

Multiple performance improvements

Hardware:
DGX Spark Support (Beta)

Others:
Helix parallelism support

New Ray orchestrator type

Documentation

Deployment Guides:
Added comprehensive deployment guides for KimiK2, Qwen3 and Qwen3-Next.

Added new guide on CPU Affinity configuration.

Updated GPT-OSS guide.

Developer Guides:
Added developer guide about KV Cache Transmission.

New section on MoE Expert Load Balance Analysis (Perfect Router) in Performance Analysis guide.

New section on API Change Principles in LLM API Change guide.

Feature Documentation:
Created new guides for Additional Outputs, Helix Parallelism, KV Cache Connector, Ray Orchestrator, Sparse Attention and Torch Compile & Piecewise CUDA Graph.

Also updated the Feature Combination Matrix and Paged Attention, IFB, and Request Scheduling guide.

Tech Blogs: Published blogs on:

"Scaling Expert Parallelism in TensorRT LLM (Part 3: Pushing the Performance Boundary)"

"Optimizing DeepSeek-V3.2 on NVIDIA Blackwell GPUs".

Examples:
Added new section on disaggregated serving service discovery method.

Added examples for K-EXAONE, Nemotron Nano V2 VL and Nemotron Nano V3.

Added RocketKV usage documentation.

Infrastructure Changes

The base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:25.12-py3
.

The base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:25.12-py3
.

The dependent public PyTorch version is updated to 2.9.1.

The dependent transformers version is updated to 4.57.3.

The dependent triton version is updated to 3.5.1.

The dependent NIXL version is updated to 0.8.0.

API Changes

Breaking Changes:
FlashInfer sampling now used by default with PyTorch backend.

Changes to sampling strategy in some previously undefined cases.

OpenAI API:
Enabled n > 1 with PyTorch backend

Added support for GET/DELETE v1/responses

Fixed multiple Issues

Known Issues

DGX Spark: DGX Spark support is in beta. Only single-node configurations and the models listed above have been validated in this release.

Disaggregated Serving: A hang may occur in disaggregated serving with context pipeline parallelism and generation tensor parallelism configurations.

Assets2
Loading

 Uh oh!

There was an error while loading. Please reload this page.

🚀2menon92 and DefTruth reacted with rocket emoji
All reactions
🚀2 reactions

2 people reacted

v1.3.0rc7

 10 Mar 20:30
 

pcastonguay

 v1.3.0rc7
 

69de4a6

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.3.0rc7Pre-release

Pre-release

Highlights

Model Support

Support tensor parallelism of TRTLLM MoE backend for Nemotron-H model (#11470)

Add Kimi-K2.5 text model support (NVFP4) (#11777)

Add Helix CP support for DSV3.2 (#11507)

Support mix quantization between shared experts and routed experts for DSV3 (#11215)

Support Cohere Command A model (#11505)

Extract embeddings as 
.safetensors
 and support float8-quantized models (#11180)

API

Add 
--served-model-name
 option to 
serve
 command (#11711)

Add flag to 
trtllm serve
 to override KV cache dtype (#11487)

Use string stop/bad words in gRPC proto instead of pre-tokenized 
TokenSequence
 (#11888)

Support multimodal image input in gRPC server (#11800)

Expose 
use_python_scheduler
 in 
SchedulerConfig
 and add associated tests (#11884)

Add 
max_gpu_total_bytes
 to control KVCacheManagerV2 capacity (#11907)

Feature

Support PARD (Parallel Draft Model) in one-model speculative decoding (#11438)

Enable autotuner for VisualGen and compilation config support (#11660)

Add globaltimer-based timing backend for autotuner profiling (#11657)

Support heterogeneous 
tokens_per_block
 (#11751)

Refactor KVCacheManagerV2 to simplify new model support (#11749)

Support Helix CP with GQA (#11570)

Add option to skip KV cache memory estimation (#11714)

Implement suffix automaton on device for speculative decoding and one-model support (#11434)

Separate radix search tree implementation (#10862)

Add support for 
expert_number
 (\le 2048) and 
K
 (\le 32) (#11510)

Add support for bidirectional sliding window attention mask to 
fmha_v2
 (#11212)

Avoid duplicated computation with ADP + Helix CP in GQA (#11891)

Add explicit video encode format support (#11830)

Refactor video encoding to use ffmpeg CLI or pure Python fallback (#11672)

Integrate CuTe DSL top-k kernel for Blackwell (#11900)

Integrate suffix automaton with EAGLE3 and PARD (#11878)

Add 5D A2A for fused Ulysses (#11787)

Add SiLU to 
trtllm-gen
 MoE (#11663)

Optimize by fusing 
nvfp4_quant
 into 
layernorm_gated
 for 
mamba2_mixer
 (#11473)

Wire 
KVCacheBlock
 to 
UnifiedBlockTree
 using lookup-node pointers (#11919)

Run extra general warmup to warm up memory pool (#10340)

Fix

Add async worker to MTP/EAGLE3 sampler (#11573)

Fix disaggregated cancellation (#11730)

Use 
prefer_pinned()
 in 
pard.py
 (#11762)

Release KVCacheManagerV2 memory immediately on shutdown (#11746)

Remove duplicated MoE computation with Helix CP+DP (#11167)

Register add+norm fallback pass for 
torch.compile
 in multi-GPU mode (#11739)

Propagate logprobs from prefill to decode in disaggregated serving (#11727)

Propagate logits from prefill to decode in disaggregated serving (#11767)

Enable separate draft KV cache pool for aggregated mode and KVBM (#11689)

Fix warnings when building 
moe_kernels.cu
 (#11703)

Fix 
available_blocks
 typo in scheduler (#11801)

Clean up memory in rollout process (#11658)

Warm up 
maybe_compiled_cat
 in 
forward_context_with_chunked_prefill
 (#11743)

Fix DeepEPLowLatency with CuTe DSL MoE backend (#11769)

Fix FP8 per-tensor 
torch.compile
 graph break in dynamic quantization (#11759)

Fix streaming generation logits and speed up logits testcase (#10637)

Fix overly aggressive capacity scheduler (#11731)

Use proper tokens when 
exclude_input_in_output
 is true (#9453)

Move 
launch_dependent_grids
 after 
tmem
 free to fix race (#11812)

Fix E/PD disaggregated chunked prefill bug (#11805)

Fix SM120 issue for 
rms_norm
 with 
nvfp4_quant_fusion
 (#11774)

Remove dead code (#11813)

Fix KVCacheManagerV2 OOM and dummy request allocation in chunked prefill / pipeline parallel (#11710)

Fix AttributeError when DSA indexer accesses non-DSA KVCacheManager (#11858)

Override 
mMaxAttentionWindow
 with actual largest window size (#11842)

Update 
check_is_moe
 to support 
mlp_layer_types
 after 
config.json
 update (#11477)

Fix incorrect GPU timing in time breakdown under overlap scheduler (#11860)

Fix OOM hang with 
NCCL_SYMMETRIC
 fallback during long-context inference (#11870)

Fix position IDs input for Qwen3.5 text-only usage (#11877)

Disable preload for Llama4 Scout (#11873)

Fix formatting issue in 
tensorrt_llm/serve/openai_server.py
 (#11920)

Prevent RuntimeError from dict mutation during iteration in EXAONE MoE weight mapper (#11862)

Fix Nemotron MTP crash on SM90 (#11807)

Fix Mistral Large3 + EAGLE bug (#11942, #11885)

Fix TeaCache broken caching for FLUX.1 and FLUX.2 (#11868)

Fix FLUX.1 TeaCache polynomial coefficients and defaults (#12007)

Implement workaround for 
ClientPayloadError
 (#12018)

Fix duplicate model entry in model list (#12029)

Fix Python string truthiness bug in FMHA cubin selection (#11909)

Documentation

Fix typos, grammar, and accuracy across documentation (#11766)

Add sparse attention tech blog (#11644)

Add known issue for disaggregated serving hang with asymmetric PP/TP (#11789)

Fix documentation links (#11912)

Replace “TensorRT-LLM” with “TensorRT LLM” (#11914)

Add CI trigger and test-failure retrieval instructions to 
AGENTS.md
 (#11803)

Benchmark

Vectorize 
quantize_fp8_blockwise
 with CUDA kernel (#11724)

Use 
F.rms_norm
 for per-head QK normalization in VisualGen (#11798)

Short-sequence MHA optimization for DSA MLA prefill (#11677)

Parallel VAE harness and implementation for WAN (#11875)

Add Triton FP8 blockwise quant kernel and autotuner bucket-skip for VisualGen (#11854)

Optimize 
_prepare_inputs
 host time (#11704)

Improve 
are_stop_words
 performance (#11196)

Add DeepSeek RCCA performance test case (#11736)

Add VisualGen benchmarking script (#11651)

Test & Infra

Add tests for all database configs (#11653)

Move B200 test stage to AIHub (#11692)

Support local wheel installation and add GB300 demo cases (#11742)

Remove submodule pulls from TRT-LLM git checkouts (#11693)

Add back WAN VBench test in CI (#11804)

Add E2E test for cancelled disaggregated generation requests with overlap scheduler (#11795)

Pass Nsight options to 
ray_executor
 and trigger profiling through 
collective_rpc
 (#11493)

Add B200 multi-node tests DB (#11783)

Add sanity tests for release 1.2 version (#11738)

Add QA test case for 
trust-remote-code
 on multi-node failure (#11905)

Fix 
model_name
 Starcoder 15B allowed-models issue (#11981)

Upgrade 
xgrammar
 from 0.1.25 to 0.1.32 (#12016)

Limit TileIRAS to CUDA 13.1 (#12042)

Remove VisualGen benchmark test from YAML (#12027)

What's Changed

[None][feat] Support tensor parallelism for nemotron-h model by @Wanli-Jiang in #11470

[None][test] Add tests for all database configs. by @fsaady in #11653

[https://nvbugs/5911143][fix] add async worker to MTP/Eagle3 sampler,… by @dhansen-nvidia in #11573

[TRTLLM-10886][feat] Support PARD(Parallel Draft Model) in one-model spec dec by @ziyixiong-nv in #11438

[None][fix] Fix disagg cancellation by @Tabrizian in #11730

[None][fix] Use prefer_pinned() in pard.py by @mikeiovine in #11762

[None][fix] Make KVCacheManagerV2 release mem immediately on shutdown by @lowsfer in #11746

[TRTLLM-11115][feat] enable autotuner for visual gen + Compilation Config by @NVShreyas in #11660

[None][chore] Minor fix in w4a8 mxfp4 mxfp8 test. by @Tracin in #11745

[None][infra] Move B200 test stage to AIHub by @yuanjingx87 in #11692

[None][infra] Waive failed cases for main on 02/27 by @EmmaQiaoCh in #11770

[TRTLLM-11064][fix] Remove duplicated MoE Computation with Helix CP+DP by @brb-nv in #11167

[TRTLLM-10386][fix] torch.compile: register add+norm fallback pass in multi-GPU mode by @luyiyun1021 in #11739

[None][feat] Support heterogeneous tokens_per_block by @lowsfer in #11751

[None][chore] Remove closed bugs by @xinhe-nv in #11527

[None][test] local wheel installation support and add gb300 cases demo by @fredricz-20070104 in #11742

[None][feat] Refactor cache manager v2 to simplify new model support by @jiaganc in #11749

[https://nvbugs/5879614][fix] Waive test_guided_decoding_with_eagle3 xgrammar in disaggregated serving by @ziyixiong-nv in #11773

[https://nvbugs/5911788][test] Waive test_llm_partial_update_weights[Qwen3/Qwen3-8B] by @liji-nv in #11785

[None][feat] add globaltimer-based timing backend for autotuner profi… by @dhansen-nvidia in #11657

[https://nvbugs/5926823][fix] Propagate logprobs from prefill to decode in disagg by @brb-nv in #11727

[TRTLLMINF-9][chore] Remove submodule pulls from TRT-LLM git checkouts by @dpitman-nvda in #11693

[https://nvbugs/5685010][fix] Delete test_eagle3_output_repetition_4gpus flaky assertions. by @zheyuf in https://github.com/NVI...

Read more

Contributors

 davidmlw, karljang, and 92 other contributors
 

Assets2
Loading

 Uh oh!

There was an error while loading. Please reload this page.

All reactions

v1.3.0rc5.post1

 06 Mar 19:07
 

pcastonguay

 v1.3.0rc5.post1
 

fdeaaa9

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.3.0rc5.post1Pre-release

Pre-release

What's Changed

[None][chore] bump version to 1.3.0rc5.post1 by @tburt-nv in #11788

[None][fix] Cherry pick cancel fix by @pcastonguay in #11790

[https://nvbugs/5926823][fix] Cherry-pick: Propagate logprobs from prefill to decode in disagg (#11727) by @pcastonguay in #11792

[https://nvbugs/5934461][fix] Cherry-picks 11767 (logits support in disagg) by @pcastonguay in #11832

[https://nvbugs/5935104][fix] Cherry-pick Fix overly aggressive capacity scheduler by @pcastonguay in #11834

[https://nvbugs/5938603][fix] Cherry-pick Fix E/PD disagg chunked prefill bug (#11805) by @pcastonguay in #11847

[https://nvbugs/5930934][fix] Cherry-pick fix NCCL OOM hang by @pcastonguay in #11916

Full Changelog: v1.3.0rc5...v1.3.0rc5.post1

Contributors

 pcastonguay and tburt-nv
 

Assets2
Loading

 Uh oh!

There was an error while loading. Please reload this page.

👍1sizorlee reacted with thumbs up emoji
All reactions
👍1 reaction

1 person reacted

v1.3.0rc6

 03 Mar 19:08
 

pcastonguay

 v1.3.0rc6
 

617440d

 This commit was created on GitHub.com and signed with GitHub’s verified signature.
 

GPG key ID: B5690EEEBB952194

Verified
 
Learn about vigilant mode.
 

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

v1.3.0rc6Pre-release

Pre-release

Highlights

Model Support

Add FLUX.1 and FLUX.2 text-to-image pipeline support (#11556)

Add GatedDeltaNet sharding from config (#11599)

Add B300 (sm103) support on VLMs (#11274)

Fix Nemotron H FP4 and MTP support (#11601)

Add quantized Eagle3 support by quantizing 
self.fc
 (#11699)

API

Add 
skip_pre_hopper
 flag for NVILA and Nano V2 VLMs (#11275)

Align 
LlmArgs
 with Pydantic best practices (#11158)

Restructure KV cache memory ratio parameters in curated YAML config files (#11511)

Feature

Refactor time breakdown tool (visualization, generation breakdown, etc.) (#11340)

Improve TorchSampler performance by reducing host overhead (#11315)

Use UE8M0 FP8 quant kernel for DeepGemm blockwise GEMM (#11607)

Implement dynamic quota resize for KVCacheManager v2 (#11503)

Add KVCache v2 MTP support (#11346)

Enhance performance dashboard (#11506)

Add E2E Python KV transceiver for current KV manager (step 5) (#11136)

Refactor KV connector (#11078)

Add GPU energy monitoring to trtllm-bench (#11397)

Support PEFT-saved safetensors file loading (#11339)

Improve FP8 (per-tensor) quant kernel with vectorized load/store (#11662)

Remove non-flash-attention-style fmha_v2 kernel for Hopper (#11381)

Fix

Fix missing sync before 
cuMemUnmap
 (#11641)

Fix message truncation in Helix CP cache transmission (#11252)

Fix GPT-OSS with non-
paged_context_fmha
 (#11309)

Fix multi-node 
trust_remote_code
 hang in disaggregated serving (#11383)

Fix kwargs name (#11496)

Accept 
**kwargs
 in 
DynamicYamlWithDeepMergeSettingsSource
 (#11621)

Fix FP8 + skip-softmax attention accuracy issue on 
fmha_v2
 (#11448)

Handle 
None
 priority in 
KVCacheEventSerializer._event_diff_to_json
 (#11576)

Fix WideEP gen-only benchmark hang in disaggregated serving (#11521)

Fix cancelled disaggregated requests getting stuck in gen server (#11695)

Fix DeepEP low-latency with DeepGEMM (#11700)

Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype (#11165)

Work around 
F.linear
 perf regression for GPTOSS (#11668)

Fix illegal memory access when 
max_seq_len
 > 
max_position_embeddings
 (#11598)

Prevent drift accumulation on 
kv_lens_cuda
 (#11696)

Documentation

Resolve conflicts in markdown documentation (#11255)

Move kimi-k2-thinking deployment guide configs into config files (#11645)

Rename 
svd-nvfp4
 to 
trtllm-nvfp4
 in visual generation examples (#11664)

Fix 60+ broken links across docs, blogs, and examples (#11676)

Update Qwen3-Next README server argument docs (#11682)

Update speculative decoding docs (#11604)

Update PR template (#11735)

Add Qwen3.5 cookbook (#11728)

Test & Infra

Enable Nemotron NVFP4 tests (#11172)

Prepare for NumPy v2 (#11389)

Add Python builds tests to CI pre-merge pipeline (#9943)

Disable warmup steps for some WAN unit tests (#11616)

Use the correct config for GPTOSS perf test (#11046)

Disable release Spark stage during Spark cloud migration (#11402)

Re-enable release Spark stage after Spark cloud migration (#11408)

Fix test prefix generation for per-SM waives (#11519)

Fix GPU memory requirement in stress test (#11404)

Do not create timeout XML if the stage is aborted (#9777)

Fix TritonMoE test for Qwen3_30B_A3B (#11495)

Refactor MoE unit tests with unified ConfigurableMoE framework (#11648)

Add comparison operators for perf regression triage (#11675)

Add WideEP DS-R1 NVFP4 test with 
attn_dp
 and 
kv_cache_reuse
 (#11670)

Add concurrency override and fix for 128k/8k cases (#11669)

Support short test case matcher in disaggregated test (#11707)

Fix multi-GPU tests (#11615)

Export 
HF_TOKEN
 in tests (#9382)

Automatically generate attributions file (#11323)

Update TRTLLM PLC pipeline (#11684)

Add timeout 14400 for SeedOSS (#11269)

Remove A100 test cases from QA perf scope (#11712)

What's Changed

[None][chore] Enable Nemotron Super nvfp4 tests by @tcherckez-nvidia in #11172

[#11529][perf] Replace Python-traced FP8 quantization with optimized CUDA op in AD MoE by @MrGeva in #11626

[TRTLLM-10514][feat] Refactor time breakdown tool (visualization, generation breakdown, etc.) by @luyiyun1021 in #11340

[None][infra] Waive failed cases for main branch on 2/23 by @EmmaQiaoCh in #11635

[#11529][perf] AD NemotronH topk router to use the model default dtype by @MrGeva in #11623

[None][fix] numpy v2 preparations by @Funatiq in #11389

[#9907][infra] Add Python builds tests to CI pre-merge pipeline by @jieli-matrix in #9943

[https://nvbugs/5921273][fix] Fix an issue where sync is missing before cuMemUnmap by @lowsfer in #11641

[#11398][feat] AutoDeploy: flashinfer rope for GLM4.7-Flash by @taylor-yb-lee in #11524

[None][infra] Waive failed cases for main for post-merge 2550 by @EmmaQiaoCh in #11650

[TRTLLM-11567][feat] Added GatedDeltaNet sharding from config by @greg-kwasniewski1 in #11599

[None][fix] Nemotron H fp4 and MTP by @NVShreyas in #11601

[https://nvbugs/5919025][fix] Disable warmup steps for some WAN unit tests by @chang-l in #11616

[TRTLLM-10616][feat] Add FLUX.1 and FLUX.2 text-to-image pipeline support by @karljang in #11556

[#10243][chore] switched the default AD attention backend to trtllm by @MrGeva in #11627

[None][chroe] Mass integration of release/1.2 - 5th by @dominicshanshan in #11636

[None][chore] Align LlmArgs with some Pydantic best practices by @anish-shanbhag in #11158

[None][perf] Use UE8M0 FP8 quant kernel for DeepGemm blockwise GEMM by @chang-l in #11607

[None][infra] Waive failed cases for main on 02/24 by @EmmaQiaoCh in #11665

[https://nvbugs/5846489][perf] Apply TE's FP8 per-tensor quantization by @yumin066 in #11057

[None][fix] Fix test prefix generation for per-sm waives by @tburt-nv in #11519

[None][chore] Weekly mass integration of release/1.2 by @mikeiovine in #11572

[TRTLLM-9781][infra] Don't create timeout xml if the stage is aborted by @yiqingy0 in #9777

[None][fix] Accept **kwargs in DynamicYamlWithDeepMergeSettingsSource… by @tcherckez-nvidia in #11621

[https://nvbugs/5606178][fix] unwaive mamba2 two tests by @JadoTu in #11479

[TRTLLM-9108][feat] refactor MoE unit tests: add unified ConfigurableMoE test framework by @xxi-nv in #11648

[None][fix] Add comparison operators for perf regression triage by @chenfeiz0326 in #11675

[None][test] Add wideep DS-R1 nvfp4 test with attn_dp and kv_cache_reuse by @StanleySun639 in #11670

[None][chore] Moving kimi-k2-thinking deployment guide configs to config files. by @fsaady in #11645

[TRTINFRA-7367][infra] Automatically generate attributions file by @tburt-nv in #11323

[None][fix] rename svd-nvfp4 to trtllm-nvfp4 in visual gen examples by @karljang in #11664

[None] [fix] Restructure kv cache memory ratio parameters in curated .yaml config files by @xd-nv in #11511

[None][chore] Bump version to 1.3.0rc6 by @yuanjingx87 in #11688

[None][fix] Fix

---
title: Prefill/Decode Disaggregated Serving
aliases: ["disaggregated-prefill-decode-serving"]
category: inference
page_type: concept
tags: [inference, concept, disaggregated, serving]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---
# Prefill/Decode Disaggregated Serving

프리필과 디코드 단계를 물리적으로 분리된 GPU 풀에서 운영하는 서빙 아키텍처. 또한 프리필과 디코드 단계를 물리적으로 분리된 GPU 풀에서 독립 스케일링.

## 왜 중요한가

2026년 Q1 vLLM과 SGLang Q1 로드맵에서 핵심 우선순위로 지정됐고, NIXL/RDMA 기반 KV 전송으로 Meta·Hugging Face 프로덕션에서 운영 중이다. AMD MI300X + SGLang 조합에서는 goodput 최대 6.9배 향상을 보였다.

2026년 초 vLLM, SGLang, Ray Serve, Dynamo 등 모든 메이저 프레임워크가 PD 디스어그리게이션을 프로덕션급으로 성숙시켰고, Meta와 Hugging Face 등에서 실제 운영에 투입되며 TTFT와 TPOT를 SLO로 분리 최적화하는 표준 패턴이 되었다.

## 대표 레퍼런스

- [vLLM Disaggregated Prefilling documentation](https://docs.vllm.ai/en/latest/features/disagg_prefill/)
- [Unleashing AMD MI300X: Disaggregating Prefill & Decode with SGLang](https://rocm.blogs.amd.com/software-tools-optimization/disaggregation/README.html)
- [Driving vLLM WideEP and Large-Scale Serving on Blackwell (vLLM Blog)](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)
- [vLLM Q1 2026 Roadmap](https://github.com/vllm-project/vllm/issues/32455)
- [SGLang Q1 2026 Development Roadmap](https://github.com/sgl-project/sglang/issues/12780)
- [Disaggregated Prefilling (experimental) - vLLM Docs](https://docs.vllm.ai/en/latest/features/disagg_prefill/)
- [Prefill/decode disaggregation — Ray Serve Docs](https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html)
- [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized LLM Serving (arXiv)](https://arxiv.org/abs/2401.09670)
- [DistServe USENIX OSDI 2024 Paper](https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf)
- [Disaggregated Prefill and Decode - Perplexity Engineering Blog](https://www.perplexity.ai/hub/blog/disaggregated-prefill-and-decode)

## 2026년 4월 핫토픽 맥락

2026년 Q1 vLLM과 SGLang Q1 로드맵에서 핵심 우선순위로 지정됐고, NIXL/RDMA 기반 KV 전송으로 Meta·Hugging Face 프로덕션에서 운영 중이다. AMD MI300X + SGLang 조합에서는 goodput 최대 6.9배 향상을 보였다.

2026년 초 vLLM, SGLang, Ray Serve, Dynamo 등 모든 메이저 프레임워크가 PD 디스어그리게이션을 프로덕션급으로 성숙시켰고, Meta와 Hugging Face 등에서 실제 운영에 투입되며 TTFT와 TPOT를 SLO로 분리 최적화하는 표준 패턴이 되었다.

### 추가 레퍼런스

- [vLLM Disaggregated Prefilling documentation](https://docs.vllm.ai/en/latest/features/disagg_prefill/)
- [Unleashing AMD MI300X: Disaggregating Prefill & Decode with SGLang](https://rocm.blogs.amd.com/software-tools-optimization/disaggregation/README.html)
- [Driving vLLM WideEP and Large-Scale Serving on Blackwell (vLLM Blog)](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)
- [vLLM Q1 2026 Roadmap](https://github.com/vllm-project/vllm/issues/32455)
- [SGLang Q1 2026 Development Roadmap](https://github.com/sgl-project/sglang/issues/12780)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[eagle-3-speculative-decoding|EAGLE-3 Speculative Decoding]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]

---
title: Prefill/Decode Disaggregated Serving
aliases: ["disaggregated-prefill-decode-serving"]
category: inference
page_type: concept
tags: [inference, concept, disaggregated, serving]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/disaggregated-serving.md, raw/hot-topics-sources/2026-04-10/081-vllm-disaggregated-prefilling-documentation.md, raw/hot-topics-sources/2026-04-10/082-unleashing-amd-mi300x-disaggregating-prefill-and-decode-with-sglang.md, raw/hot-topics-sources/2026-04-10/083-driving-vllm-wideep-and-large-scale-serving-on-blackwell.md, raw/hot-topics-sources/2026-04-10/084-vllm-q1-2026-roadmap.md, raw/hot-topics-sources/2026-04-10/085-sglang-q1-2026-development-roadmap.md, raw/hot-topics-sources/2026-04-10/315-prefill-decode-disaggregation-ray-serve-docs.md, raw/hot-topics-sources/2026-04-10/316-distserve-disaggregating-prefill-and-decoding-for-goodput-optimized-llm-serving.md, raw/hot-topics-sources/2026-04-10/317-distserve-usenix-osdi-2024-paper.md, raw/hot-topics-sources/2026-04-10/318-disaggregated-prefill-and-decode-perplexity-engineering-blog.md]
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

## source 기반 참고

- 수집 소스 수: 9
- 상위 도메인: github.com 2건, docs.vllm.ai 1건, rocm.blogs.amd.com 1건
- source 조합: 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/disaggregated-serving.md`
- [Disaggregated Prefilling (experimental) - vLLM](https://docs.vllm.ai/en/latest/features/disagg_prefill) — `raw/hot-topics-sources/2026-04-10/081-vllm-disaggregated-prefilling-documentation.md`
  - 메모: --- title: Disaggregated Prefilling (experimental) - vLLM source_url: https://docs.vllm.ai/en/latest/features/disagg_prefill final_url: https://docs.vllm.ai/en/latest/features/disagg_prefill/ status: 200 content_type: text/html; charset=utf-8 topics: [Prefill/Decode Disaggregated
- [Unleashing AMD Instinct™ MI300X GPUs for LLM Serving: Disaggregating Prefill & Decode with SGLang — ROCm Blogs](https://rocm.blogs.amd.com/software-tools-optimization/disaggregation/README.html) — `raw/hot-topics-sources/2026-04-10/082-unleashing-amd-mi300x-disaggregating-prefill-and-decode-with-sglang.md`
  - 메모: --- title: Unleashing AMD Instinct™ MI300X GPUs for LLM Serving: Disaggregating Prefill & Decode with SGLang — ROCm Blogs source_url: https://rocm.blogs.amd.com/software-tools-optimization/disaggregation/README.html final_url: https://rocm.blogs.amd.com/software-tools-optimizatio
- [Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) | vLLM Blog](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html) — `raw/hot-topics-sources/2026-04-10/083-driving-vllm-wideep-and-large-scale-serving-on-blackwell.md`
  - 메모: --- title: Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) | vLLM Blog source_url: https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html final_url: https://vllm.ai/blog/dsr1-gb200-part1 status: 200 content_type: text/html; charset=utf-8 topics: [
- [[Roadmap] vLLM Roadmap Q1 2026 · Issue #32455 · vllm-project/vllm · GitHub](https://github.com/vllm-project/vllm/issues/32455) — `raw/hot-topics-sources/2026-04-10/084-vllm-q1-2026-roadmap.md`
  - 메모: --- title: [Roadmap] vLLM Roadmap Q1 2026 · Issue #32455 · vllm-project/vllm · GitHub source_url: https://github.com/vllm-project/vllm/issues/32455 final_url: https://github.com/vllm-project/vllm/issues/32455 status: 200 content_type: text/html; charset=utf-8 topics: [Prefill/Dec
- [Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub](https://github.com/sgl-project/sglang/issues/12780) — `raw/hot-topics-sources/2026-04-10/085-sglang-q1-2026-development-roadmap.md`
  - 메모: --- title: Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub source_url: https://github.com/sgl-project/sglang/issues/12780 final_url: https://github.com/sgl-project/sglang/issues/12780 status: 200 content_type: text/html; charset=utf-8 topics: [Prefill/D
- [Prefill/decode disaggregation — Ray 2.54.1](https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html) — `raw/hot-topics-sources/2026-04-10/315-prefill-decode-disaggregation-ray-serve-docs.md`
  - 메모: --- title: Prefill/decode disaggregation — Ray 2.54.1 source_url: https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html final_url: https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html status: 200 content_type: text/html; charset=utf-8 topics: 
- [[2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://arxiv.org/abs/2401.09670) — `raw/hot-topics-sources/2026-04-10/316-distserve-disaggregating-prefill-and-decoding-for-goodput-optimized-llm-serving.md`
  - 메모: --- title: [2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving source_url: https://arxiv.org/abs/2401.09670 final_url: https://arxiv.org/abs/2401.09670 status: 200 content_type: text/html; charset=utf-8 topics: [Disaggreg
- [317-distserve-usenix-osdi-2024-paper](https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf) — `raw/hot-topics-sources/2026-04-10/317-distserve-usenix-osdi-2024-paper.md`
  - 메모: --- title: DistServe USENIX OSDI 2024 Paper source_url: https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf final_url: https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf status: 200 content_type: application/pdf topics: [Disaggregated Prefill/Decode Serving] sect
- [Disaggregated Prefill and Decode](https://www.perplexity.ai/hub/blog/disaggregated-prefill-and-decode) — `raw/hot-topics-sources/2026-04-10/318-disaggregated-prefill-and-decode-perplexity-engineering-blog.md`
  - 메모: --- title: Disaggregated Prefill and Decode source_url: https://www.perplexity.ai/hub/blog/disaggregated-prefill-and-decode final_url: https://www.perplexity.ai/hub/blog/disaggregated-prefill-and-decode status: 200 content_type: text/html topics: [Disaggregated Prefill/Decode Ser

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[eagle-3-speculative-decoding|EAGLE-3 Speculative Decoding]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]

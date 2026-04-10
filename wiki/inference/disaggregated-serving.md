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

## 해석 포인트

Prefill/Decode Disaggregated Serving은 **단일 모델 성능보다 서빙 토폴로지와 라우팅 품질이 핵심인 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `github.com×2, docs.vllm.ai×1, rocm.blogs.amd.com×1, vllm.ai×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 TTFT, TPOT, 메모리 사용량, 하드웨어 의존성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 프리필과 디코드 단계를 물리적으로 분리된 GPU 풀에서 독립 스케일링.
- 왜 중요한가: 2026년 초 vLLM, SGLang, Ray Serve, Dynamo 등 모든 메이저 프레임워크가 PD 디스어그리게이션을 프로덕션급으로 성숙시켰고, Meta와 Hugging Face 등에서 실제 운영에 투입되며 TTFT와 TPOT를 SLO로 분리 최적화하는 표준 패턴이 되었다.
- 직접 수집 원문: 9개
- 주요 도메인: github.com×2, docs.vllm.ai×1, rocm.blogs.amd.com×1, vllm.ai×1, docs.ray.io×1

## 핵심 메커니즘

프리필과 디코드 단계를 물리적으로 분리된 GPU 풀에서 독립 스케일링. 추론/서빙 토픽은 대부분 **throughput, latency, memory, hardware topology**의 trade-off에서 의미가 생긴다. source를 함께 보면 `github.com×2, docs.vllm.ai×1, rocm.blogs.amd.com×1, vllm.ai×1, docs.ray.io×1`처럼 논문과 구현체/벤더 문서가 동시에 등장한다.

## 구현·운영 관점

2026년 초 vLLM, SGLang, Ray Serve, Dynamo 등 모든 메이저 프레임워크가 PD 디스어그리게이션을 프로덕션급으로 성숙시켰고, Meta와 Hugging Face 등에서 실제 운영에 투입되며 TTFT와 TPOT를 SLO로 분리 최적화하는 표준 패턴이 되었다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 핵심 포인트

Prefill/Decode Disaggregated Serving는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 프리필과 디코드 단계를 물리적으로 분리된 GPU 풀에서 운영하는 서빙 아키텍처. 또한 프리필과 디코드 단계를 물리적으로 분리된 GPU 풀에서 독립 스케일링.이며, 직접 수집한 source 9건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 github.com×2, arxiv.org×1, docs.ray.io×1, docs.vllm.ai×1, perplexity.ai×1로 분포한다. 연구·공식문서·구현체가 모두 섞여 있어서 개념과 운영을 함께 추적하기 좋다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/disaggregated-serving.md`

### source별 핵심 신호

- **Disaggregated Prefilling (experimental) - vLLM** (`docs.vllm.ai`): https://docs.vllm.ai/en/latest/features/disagg_prefill/
  - 메모: Retrieval Augmented Generation With Langchain
- **Unleashing AMD Instinct™ MI300X GPUs for LLM Serving: Disaggregating Prefill & Decode with SGLang — ROCm Blogs** (`rocm.blogs.amd.com`): https://rocm.blogs.amd.com/software-tools-optimization/disaggregation/README.html
  - 메모: Why Do We Need to Disaggregate the Prefill and the Decode Phases?
- **Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) | vLLM Blog** (`vllm.ai`): https://vllm.ai/blog/dsr1-gb200-part1
  - 메모: In collaboration with the open-source community, vLLM \+ NVIDIA has achieved significant performance milestones on the gpt-oss-120b model running on NVIDIA's Blackwell GPUs. Through deep...
- **[Roadmap] vLLM Roadmap Q1 2026 · Issue #32455 · vllm-project/vllm · GitHub** (`github.com`): https://github.com/vllm-project/vllm/issues/32455
  - 메모: To see all available qualifiers, see our documentation.
- **Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub** (`github.com`): https://github.com/sgl-project/sglang/issues/12780
  - 메모: To see all available qualifiers, see our documentation.
- **Prefill/decode disaggregation — Ray 2.54.1** (`docs.ray.io`): https://docs.ray.io/en/latest/serve/llm/user-guides/prefill-decode.html
  - 메모: Ray TrainScale machine learning training
- **[2401.09670] DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving** (`arxiv.org`): https://arxiv.org/abs/2401.09670
  - 메모: DistServe improves the performance of large language models (LLMs) serving by disaggregating the prefill and decoding computation.
- **DistServe USENIX OSDI 2024 Paper** (`usenix.org`): https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf
  - 메모: << /Author () /CreationDate (D:20240605030250Z) /Creator (LaTeX with hyperref) /Keywords () /ModDate (D:20240612184623Z) /PTEX.Fullbanner (This is pdfTeX, Version 3.141592653-2.6-1.40.25 \(TeX Live 2023\) kpathsea versio
- **Disaggregated Prefill and Decode** (`perplexity.ai`): https://www.perplexity.ai/hub/blog/disaggregated-prefill-and-decode
  - 메모: In order to generate output tokens from an input prompt, LLM inference is split into two stages: prefill and decode.


## source 종합 해석

예를 들어 source note는 Retrieval Augmented Generation With Langchain

또 다른 source는 Why Do We Need to Disaggregate the Prefill and the Decode Phases?

즉, 이 토픽이 중요한 이유는 `2026년 Q1 vLLM과 SGLang Q1 로드맵에서 핵심 우선순위로 지정됐고, NIXL/RDMA 기반 KV 전송으로 Meta·Hugging Face 프로덕션에서 운영 중이다. AMD MI300X + SGLang 조합에서는 goodput 최대 6.9배 향상을 보였다.`라는 한 문장보다, 여러 source가 같은 문제를 서로 다른 층위(개념·측정·구현)에서 지지한다는 데 있다.

함께 읽을 문서로는 2026년 4월 AI 개발 핫토픽 100선, EAGLE-3 Speculative Decoding, Wide Expert Parallelism (WideEP) for MoE가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- source note가 추상 개념/실험 결과/운영 사례 중 어디에 치우쳐 있는지 보면, 이 토픽을 실무에서 어떻게 다뤄야 하는지가 드러난다.
- `2026년 Q1 vLLM과 SGLang Q1 로드맵에서 핵심 우선순위로 지정됐고, NIXL/RDMA 기반 KV 전송으로 Meta·Hugging Face 프로덕션에서 운영 중이다. AMD MI300X + SGLang 조합에서는 goodput 최대 6.9배 향상을 보였다.`라는 중요도 설명은 보통 과장되기 쉬우므로, 구체적 수치·벤치마크·운영 사례를 같이 확인해야 한다.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[eagle-3-speculative-decoding|EAGLE-3 Speculative Decoding]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]

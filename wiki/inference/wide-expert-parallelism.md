---
title: Wide Expert Parallelism (WideEP) for [[mixture-of-experts|MoE]]
category: inference
page_type: concept
tags: [inference, concept, wide, expert, parallelism]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/wide-expert-parallelism.md, raw/hot-topics-sources/2026-04-10/083-driving-vllm-wideep-and-large-scale-serving-on-blackwell.md, raw/hot-topics-sources/2026-04-10/086-vllm-expert-parallel-deployment-docs.md, raw/hot-topics-sources/2026-04-10/087-scaling-deepseek-style-moes-with-vllm-and-llm-d-using-wide-ep.md, raw/hot-topics-sources/2026-04-10/088-vllm-large-scale-serving-deepseek-2-2k-tok-s-h200-with-wide-ep.md, raw/hot-topics-sources/2026-04-10/089-deepseek-v3-2-on-gb300-performance-breakthrough.md, raw/hot-topics-sources/2026-04-10/319-elastic-ep-in-sglang-achieving-partial-failure-tolerance-for-deepseek-moe-deploy.md, raw/hot-topics-sources/2026-04-10/320-deepep-expert-parallel-communication-library-github.md]
created: 2026-04-10
updated: 2026-04-13
---
# Wide Expert Parallelism (WideEP) for MoE

MoE 전문가를 다수 노드에 분산하고 EPLB로 로드 밸런싱하는 서빙 전략. 또한 DeepSeek급 MoE 모델을 32+ GPU에 걸쳐 전문가를 분산시키는 병렬화 전략.

## 왜 중요한가

2026년 2월 [[vllm-v1-engine|vLLM]] 블로그에서 DeepSeek-R1/V3를 GB200에 배포해 프리필 26.2K TGS / 디코드 10.1K TGS를 달성했고, DeepEP·PPLX 디스패치 커널과 EPLB 리밸런싱이 표준 구성이 되었다.

2025년 12월 vLLM이 H200에서 2.2k tok/s/GPU를 달성했고 2026년 2월 Blackwell 파트 I 블로그가 공개되었으며, 3월 SGLang의 Elastic EP가 부분 장애 내성을 추가해 MoE 대규모 서빙의 운영 성숙도가 급격히 올라갔다.

## 대표 레퍼런스

- [Driving vLLM WideEP and Large-Scale Serving on Blackwell (vLLM Blog)](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)
- [vLLM Expert Parallel Deployment docs](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/)
- [Scaling DeepSeek-style MoEs with vLLM and llm-d using Wide EP (Red Hat)](https://developers.redhat.com/articles/2025/09/08/scaling-deepseek-style-moes-vllm-and-llm-d-using-wide-ep)
- [vLLM Large Scale Serving: DeepSeek @ 2.2k tok/s/H200 with Wide-EP](https://blog.vllm.ai/2025/12/17/large-scale-serving.html)
- [DeepSeek-V3.2 on GB300: Performance Breakthrough (vLLM Blog)](https://blog.vllm.ai/2026/02/13/gb300-deepseek.html)
- [Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) - vLLM Blog (2026-02-03)](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)
- [vLLM Large Scale Serving: DeepSeek @ 2.2k tok/s/H200 with Wide-EP (2025-12-17)](https://blog.vllm.ai/2025/12/17/large-scale-serving.html)
- [Elastic EP in [[sglang|SGLang]]: Achieving Partial Failure Tolerance for DeepSeek MoE Deployments (2026-03-25)](https://www.lmsys.org/blog/2026-03-25-eep-partial-failure-tolerance/)
- [Expert Parallel Deployment - vLLM Docs](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/)
- [DeepEP: Expert-Parallel Communication Library GitHub](https://github.com/deepseek-ai/DeepEP)

## 구현·운영 관점

2025년 12월 vLLM이 H200에서 2.2k tok/s/GPU를 달성했고 2026년 2월 Blackwell 파트 I 블로그가 공개되었으며, 3월 SGLang의 Elastic EP가 부분 장애 내성을 추가해 MoE 대규모 서빙의 운영 성숙도가 급격히 올라갔다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

## 관련 문서
- [[vllm-v1-engine]]

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[disaggregated-serving|Prefill/Decode Disaggregated Serving]]
- [[deepseek-sparse-attention|DeepSeek Sparse Attention (DSA) for Long Context]]


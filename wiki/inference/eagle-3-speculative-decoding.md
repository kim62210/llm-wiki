---
title: EAGLE-3 Speculative Decoding
category: inference
page_type: concept
tags: [inference, concept, eagle, speculative, decoding, inference-optimization]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/eagle-3-speculative-decoding.md, raw/hot-topics-sources/2026-04-10/076-eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-.md, raw/hot-topics-sources/2026-04-10/077-safeailab-eagle-official-repository.md, raw/hot-topics-sources/2026-04-10/078-from-research-to-production-accelerate-oss-llm-with-eagle-3-on-vertex.md, raw/hot-topics-sources/2026-04-10/079-fly-eagle-3-fly-faster-inference-with-vllm.md, raw/hot-topics-sources/2026-04-10/080-sglang-speculative-decoding-documentation.md]
created: 2026-04-10
updated: 2026-04-13
---
# EAGLE-3 Speculative Decoding

이 페이지는 EAGLE-3 Speculative Decoding를 다룬다. 핵심은 멀티레이어 피처 융합과 training-time test로 드래프트 헤드를 학습시키는 가속법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

멀티레이어 피처 융합과 training-time test로 드래프트 헤드를 학습시키는 가속법.

## 왜 지금 중요한가

NeurIPS 2025 채택 후 2025년 말부터 [[vllm-v1-engine|vLLM]], SGLang, TensorRT-LLM 모두에 통합되어 최대 6.5배 속도 향상을 기록했고, LMSys는 2025년 12월 Google Vertex AI 프로덕션 배포 사례를 공개했다.

## 대표 자료

- [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://arxiv.org/abs/2503.01840)
- [SafeAILab/EAGLE official repository](https://github.com/SafeAILab/EAGLE)
- [From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex (LMSYS)](https://lmsys.org/blog/2025-12-01-eagle3-vertex/)
- [Fly Eagle-3 fly: Faster inference with vLLM (Red Hat)](https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding)
- [[[sglang|SGLang]] Speculative Decoding documentation](https://docs.sglang.io/advanced_features/speculative_decoding.html)

## 구현·운영 관점

NeurIPS 2025 채택 후 2025년 말부터 vLLM, SGLang, TensorRT-LLM 모두에 통합되어 최대 6.5배 속도 향상을 기록했고, LMSys는 2025년 12월 Google Vertex AI 프로덕션 배포 사례를 공개했다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

## 관련 문서
- [[speculative-speculative-decoding]]
- [[disaggregated-serving]]
- [[mirror-speculative-decoding]]

- [[ai-hot-topics-2026-04]]
- [[nvfp4-quantization]]
- [[disaggregated-serving]]


---
title: EAGLE-3 Speculative Decoding
category: inference
page_type: concept
tags: [inference, concept, eagle, speculative, decoding, inference-optimization]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---
# EAGLE-3 Speculative Decoding

이 페이지는 EAGLE-3 Speculative Decoding를 다룬다. 핵심은 멀티레이어 피처 융합과 training-time test로 드래프트 헤드를 학습시키는 가속법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

멀티레이어 피처 융합과 training-time test로 드래프트 헤드를 학습시키는 가속법.

## 왜 지금 중요한가

NeurIPS 2025 채택 후 2025년 말부터 vLLM, SGLang, TensorRT-LLM 모두에 통합되어 최대 6.5배 속도 향상을 기록했고, LMSys는 2025년 12월 Google Vertex AI 프로덕션 배포 사례를 공개했다.

## 대표 자료

- [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://arxiv.org/abs/2503.01840)
- [SafeAILab/EAGLE official repository](https://github.com/SafeAILab/EAGLE)
- [From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex (LMSYS)](https://lmsys.org/blog/2025-12-01-eagle3-vertex/)
- [Fly Eagle-3 fly: Faster inference with vLLM (Red Hat)](https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding)
- [SGLang Speculative Decoding documentation](https://docs.sglang.io/advanced_features/speculative_decoding.html)

## 2026년 4월 핫토픽 맥락

NeurIPS 2025 채택 후 2025년 말부터 vLLM, SGLang, TensorRT-LLM 모두에 통합되어 최대 6.5배 속도 향상을 기록했고, LMSys는 2025년 12월 Google Vertex AI 프로덕션 배포 사례를 공개했다.

### 추가 레퍼런스

- [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://arxiv.org/abs/2503.01840)
- [SafeAILab/EAGLE official repository](https://github.com/SafeAILab/EAGLE)
- [From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex (LMSYS)](https://lmsys.org/blog/2025-12-01-eagle3-vertex/)
- [Fly Eagle-3 fly: Faster inference with vLLM (Red Hat)](https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding)
- [SGLang Speculative Decoding documentation](https://docs.sglang.io/advanced_features/speculative_decoding.html)

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[nvfp4-quantization]]
- [[disaggregated-prefill-decode-serving]]

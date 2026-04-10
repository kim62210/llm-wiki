---
title: EAGLE-3 Speculative Decoding
category: inference
page_type: concept
tags: [inference, concept, eagle, speculative, decoding, inference-optimization]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/eagle-3-speculative-decoding.md, raw/hot-topics-sources/2026-04-10/076-eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-.md, raw/hot-topics-sources/2026-04-10/077-safeailab-eagle-official-repository.md, raw/hot-topics-sources/2026-04-10/078-from-research-to-production-accelerate-oss-llm-with-eagle-3-on-vertex.md, raw/hot-topics-sources/2026-04-10/079-fly-eagle-3-fly-faster-inference-with-vllm.md, raw/hot-topics-sources/2026-04-10/080-sglang-speculative-decoding-documentation.md]
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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 1건, github.com 1건, www.lmsys.org 1건

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/eagle-3-speculative-decoding.md`
- [[2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://arxiv.org/abs/2503.01840) — `raw/hot-topics-sources/2026-04-10/076-eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-.md`
  - 메모: --- title: [2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test source_url: https://arxiv.org/abs/2503.01840 final_url: https://arxiv.org/abs/2503.01840 status: 200 content_type: text/html; charset=utf-8 topics: [EAGLE-3 Speculat
- [GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub](https://github.com/SafeAILab/EAGLE) — `raw/hot-topics-sources/2026-04-10/077-safeailab-eagle-official-repository.md`
  - 메모: --- title: GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub source_url: https://github.com/SafeAILab/EAGLE final_url: https://github.com/SafeAILab/EAGLE status: 200 content_type: text/html; charset=utf-
- [From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex - LMSYS Blog | LMSYS Org](https://lmsys.org/blog/2025-12-01-eagle3-vertex) — `raw/hot-topics-sources/2026-04-10/078-from-research-to-production-accelerate-oss-llm-with-eagle-3-on-vertex.md`
  - 메모: --- title: From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex - LMSYS Blog | LMSYS Org source_url: https://lmsys.org/blog/2025-12-01-eagle3-vertex final_url: https://www.lmsys.org/blog/2025-12-01-eagle3-vertex/ status: 200 content_type: text/html; charset=utf-
- [Faster inference with vLLM & speculative decoding | Red Hat Developer](https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding) — `raw/hot-topics-sources/2026-04-10/079-fly-eagle-3-fly-faster-inference-with-vllm.md`
  - 메모: --- title: Faster inference with vLLM & speculative decoding | Red Hat Developer source_url: https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding final_url: https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-fas
- [Speculative Decoding — SGLang](https://docs.sglang.io/advanced_features/speculative_decoding.html) — `raw/hot-topics-sources/2026-04-10/080-sglang-speculative-decoding-documentation.md`
  - 메모: --- title: Speculative Decoding — SGLang source_url: https://docs.sglang.io/advanced_features/speculative_decoding.html final_url: https://docs.sglang.io/advanced_features/speculative_decoding.html status: 200 content_type: text/html; charset=utf-8 topics: [EAGLE-3 Speculative De

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[nvfp4-quantization]]
- [[disaggregated-prefill-decode-serving]]

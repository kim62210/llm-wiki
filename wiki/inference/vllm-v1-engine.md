---
title: vLLM V1 Engine on Blackwell (GB200/GB300)
category: inference
page_type: entity
project: vLLM V1 Engine on Blackwell
tags: [inference, entity, vllm, v1, engine]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/vllm-v1-engine.md, raw/hot-topics-sources/2026-04-10/084-vllm-q1-2026-roadmap.md, raw/hot-topics-sources/2026-04-10/321-vllm-project-vllm-github-releases.md, raw/hot-topics-sources/2026-04-10/322-vllm-blog.md, raw/hot-topics-sources/2026-04-10/323-vllm-disaggregated-serving-example-docs.md, raw/hot-topics-sources/2026-04-10/324-vllm-release-notes-nvidia-docs.md]
created: 2026-04-10
updated: 2026-04-10
---
# vLLM V1 Engine on Blackwell (GB200/GB300)

vLLM V0 완전 폐기 후 V1 엔진을 기반으로 Blackwell 아키텍처에서 속도 한계를 추구하는 Q1 로드맵.

## 왜 지금 중요한가

v0.11.0에서 V0 코드가 완전히 제거되고 V1로 단일화되었으며, 2026 Q1 로드맵이 GB200/B200/H200 디스어그리게이트 클러스터에서의 "speed of light"를 명시적 목표로 선언하면서 대규모 서빙 팀의 최우선 트랙이 되었다.

## 대표 레퍼런스

- [[Roadmap] vLLM Roadmap Q1 2026 - Issue #32455](https://github.com/vllm-project/vllm/issues/32455)
- [vllm-project/vllm GitHub Releases](https://github.com/vllm-project/vllm/releases)
- [vLLM Blog](https://blog.vllm.ai/)
- [vLLM Disaggregated Serving Example Docs](https://docs.vllm.ai/en/latest/examples/online_serving/disaggregated_serving.html)
- [vLLM Release Notes - NVIDIA Docs](https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html)

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/vllm-v1-engine.md`
- raw source: `raw/hot-topics-sources/2026-04-10/084-vllm-q1-2026-roadmap.md`
- raw source: `raw/hot-topics-sources/2026-04-10/321-vllm-project-vllm-github-releases.md`
- raw source: `raw/hot-topics-sources/2026-04-10/322-vllm-blog.md`
- raw source: `raw/hot-topics-sources/2026-04-10/323-vllm-disaggregated-serving-example-docs.md`
- raw source: `raw/hot-topics-sources/2026-04-10/324-vllm-release-notes-nvidia-docs.md`

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[wide-expert-parallelism|Wide Expert Parallelism (WideEP) for MoE]]
- [[sglang|SGLang on GB300 NVL72 with NVFP4]]

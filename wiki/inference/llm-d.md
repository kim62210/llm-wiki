---
title: llm-d & Gateway API Inference Extension
category: inference
page_type: entity
project: llm-d & Gateway API Inference Extension
tags: [inference, entity, llm, d]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/llm-d.md, raw/hot-topics-sources/2026-04-10/329-llm-d-llm-d-github-repository.md, raw/hot-topics-sources/2026-04-10/330-llm-d-architecture-documentation.md, raw/hot-topics-sources/2026-04-10/331-kubernetes-sigs-gateway-api-inference-extension-github.md, raw/hot-topics-sources/2026-04-10/332-introducing-gateway-api-inference-extension-kubernetes-blog.md, raw/hot-topics-sources/2026-04-10/333-gateway-api-inference-extension-documentation.md]
created: 2026-04-10
updated: 2026-04-10
---
# llm-d & Gateway API Inference Extension

vLLM+Kubernetes Gateway API Inference Extension 기반의 CNCF 분산 추론 스택.

## 왜 지금 중요한가

2026년 3월 24일 llm-d가 CNCF Sandbox에 편입되었고 Gateway API Inference Extension v1.4.0이 3월 20일 GA되면서, IBM/Red Hat/Google/NVIDIA가 밀고 있는 쿠버네티스 네이티브 분산 추론의 공식 표준 경로가 되었다.

## 대표 레퍼런스

- [llm-d/llm-d GitHub Repository](https://github.com/llm-d/llm-d)
- [llm-d Architecture Documentation](https://llm-d.ai/docs/architecture)
- [kubernetes-sigs/gateway-api-inference-extension GitHub](https://github.com/kubernetes-sigs/gateway-api-inference-extension)
- [Introducing Gateway API Inference Extension - Kubernetes Blog](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)
- [Gateway API Inference Extension Documentation](https://gateway-api-inference-extension.sigs.k8s.io/)

## 해석 포인트

llm-d & Gateway API Inference Extension은 단순한 제품 소개보다 **단일 모델 성능보다 서빙 토폴로지와 라우팅 품질이 핵심인 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `github.com×2, llm-d.ai×1, kubernetes.io×1, gateway-api-inference-extension.sigs.k8s.io×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 TTFT, TPOT, 메모리 사용량, 하드웨어 의존성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: vLLM+Kubernetes Gateway API Inference Extension 기반의 CNCF 분산 추론 스택.
- 왜 중요한가: 2026년 3월 24일 llm-d가 CNCF Sandbox에 편입되었고 Gateway API Inference Extension v1.4.0이 3월 20일 GA되면서, IBM/Red Hat/Google/NVIDIA가 밀고 있는 쿠버네티스 네이티브 분산 추론의 공식 표준 경로가 되었다.
- 직접 수집 원문: 5개
- 주요 도메인: github.com×2, llm-d.ai×1, kubernetes.io×1, gateway-api-inference-extension.sigs.k8s.io×1

## 핵심 메커니즘

vLLM+Kubernetes Gateway API Inference Extension 기반의 CNCF 분산 추론 스택. 추론/서빙 토픽은 대부분 **throughput, latency, memory, hardware topology**의 trade-off에서 의미가 생긴다. source를 함께 보면 `github.com×2, llm-d.ai×1, kubernetes.io×1, gateway-api-inference-extension.sigs.k8s.io×1`처럼 논문과 구현체/벤더 문서가 동시에 등장한다.

## 구현·운영 관점

2026년 3월 24일 llm-d가 CNCF Sandbox에 편입되었고 Gateway API Inference Extension v1.4.0이 3월 20일 GA되면서, IBM/Red Hat/Google/NVIDIA가 밀고 있는 쿠버네티스 네이티브 분산 추론의 공식 표준 경로가 되었다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 핵심 포인트

llm-d & Gateway API Inference Extension는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 vLLM+Kubernetes Gateway API Inference Extension 기반의 CNCF 분산 추론 스택.이며, 직접 수집한 source 5건은 github.com×2, gateway-api-inference-extension.sigs.k8s.io×1, kubernetes.io×1, llm-d.ai×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 github.com×2, gateway-api-inference-extension.sigs.k8s.io×1, kubernetes.io×1, llm-d.ai×1로 분포한다. 구현 저장소 비중이 높아 실제 사용·통합 관점이 두드러진다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/llm-d.md`

### source별 핵심 신호

- **GitHub - llm-d/llm-d: Achieve state of the art inference performance with modern accelerators on Kubernetes · GitHub** (`github.com`): https://github.com/llm-d/llm-d
  - 메모: To see all available qualifiers, see our documentation.
- **llm-d Architecture | llm-d** (`llm-d.ai`): https://llm-d.ai/docs/architecture
  - 메모: llm-d is a high-performance distributed inference serving stack optimized for production deployments on Kubernetes.
- **GitHub - kubernetes-sigs/gateway-api-inference-extension: Gateway API Inference Extension · GitHub** (`github.com`): https://github.com/kubernetes-sigs/gateway-api-inference-extension
  - 메모: To see all available qualifiers, see our documentation.
- **Introducing Gateway API Inference Extension | Kubernetes** (`kubernetes.io`): https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/
  - 메모: Running Agents on Kubernetes with Agent Sandbox
- **Introduction - Kubernetes Gateway API Inference Extension** (`gateway-api-inference-extension.sigs.k8s.io`): https://gateway-api-inference-extension.sigs.k8s.io
  - 메모: The overall resource model focuses on 2 new inference-focused


## source 종합 해석

`llm-d & Gateway API Inference Extension`는 단일 발표보다 **여러 source가 어떤 관점에서 이 대상을 규정하는가**를 함께 읽을 때 의미가 커진다.

이번 수집에서는 GitHub - llm-d/llm-d: Achieve state of the art inference performance with modern accelerators on Kubernetes · GitHub, llm-d Architecture | llm-d, GitHub - kubernetes-sigs/gateway-api-inference-extension: Gateway API Inference Extension · GitHub처럼 출시 공지·문서·평가 신호가 같이 모여, 기능 자체보다 생태계 위치와 운영 전제가 더 중요하다는 점이 드러난다.

함께 읽을 문서로는 2026년 4월 AI 개발 핫토픽 100선, SGLang on GB300 NVL72 with NVFP4, LMCache + Mooncake KV Cache Layer가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- 도입 판단 시 기능 목록만 보지 말고, 공식 문서·릴리스 노트·벤치마크가 서로 얼마나 일관되게 같은 메시지를 주는지 확인한다.
- 비교 후보와의 차이는 API/운영 통합, 성능 수치, 생태계 성숙도 같은 기준으로 정리하는 것이 좋다.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[sglang|SGLang on GB300 NVL72 with NVFP4]]
- [[lmcache|LMCache + Mooncake KV Cache Layer]]

---
title: DeepSeek V4 / R2
category: tooling
page_type: entity
project: DeepSeek V4
tags: [deepseek, v4, r2, moe, engram-memory, huawei, ascend, open-source, million-context]
sources: [raw/2026-04-14-gap-scan-new-topics.md]
references:
  - https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026
  - https://findskill.ai/blog/deepseek-v4-release-date-specs/
  - https://www.meta-intelligence.tech/en/insight-deepseek-v4-r2
created: 2026-04-14
updated: 2026-04-14
---

## 개요

DeepSeek V4는 DeepSeek가 개발 중인 차세대 프론티어 모델이다. 약 1조(1T) 파라미터의 Mixture-of-Experts([[mixture-of-experts|MoE]]) 아키텍처로, 토큰당 약 370억(37B) 파라미터만 활성화하여 효율성을 유지한다. 100만(1M) 토큰 컨텍스트 윈도우를 지원하며, Needle-in-a-Haystack 검색에서 97% 정확도를 달성한다.

핵심 혁신은 Engram Conditional Memory로, 장문 입력에서 관련성 신호 기반의 선택적 저장/검색 메커니즘이다. NVIDIA 칩이 아닌 Huawei Ascend 칩에서 학습되어 중국산 AI 가속기의 실증적 성과로 주목받고 있다. R2는 V4 기반의 추론 특화 변형 모델이다.

2026년 4월 말 출시가 예상되며, V4-Lite는 3월 9일부터 테스트 중이다. 학습 비용은 약 520만 달러로 추정된다.

## 핵심 특징

- **1T MoE / 37B Active**: 약 1조 파라미터 총 규모에서 토큰당 370억만 활성화. [[deepseek-v3-2]]의 685B에서 규모가 대폭 확대
- **1M 토큰 컨텍스트**: V3의 128K에서 약 8배 확장. Needle-in-a-Haystack 97% 정확도
- **Engram Conditional Memory**: 표준 어텐션의 장문 검색 한계를 해결하는 조건부 메모리 아키텍처. RAG 시스템의 복잡도를 줄일 잠재력
- **Huawei 칩 전용 학습**: Ascend 910B 및 Cambricon MLU 칩 사용. NVIDIA 독점성 탈피의 실증적 증명
- **멀티모달 네이티브**: 텍스트, 이미지, 영상 생성을 통합 지원
- **극저가 API**: 입력 $0.28/1M 토큰, 출력 $0.50-1.10/1M 토큰. Claude Opus 대비 약 1/50 수준 예상

## 기술 상세

### 모델 사양

| 항목 | DeepSeek V4 | DeepSeek V3.2 (참고) |
|---|---|---|
| 총 파라미터 | ~1T | 685B |
| 활성 파라미터 | ~37B/토큰 | 37B/토큰 |
| 아키텍처 | MoE | MoE |
| 컨텍스트 윈도우 | 1M 토큰 | 128K 토큰 |
| 모달리티 | 텍스트 + 이미지 + 비디오 | 텍스트 |
| 학습 하드웨어 | Huawei Ascend | NVIDIA |
| 학습 비용 | ~$5.2M | ~$5.6M |
| 라이선스 | MIT 또는 Apache 2.0 예상 | MIT |

### Engram Conditional Memory

Engram Conditional Memory는 DeepSeek V4의 핵심 아키텍처 혁신이다. 장문 컨텍스트에서 표준 어텐션의 정보 검색 성능 저하 문제를 해결한다.

```mermaid
graph TB
    subgraph "Engram Conditional Memory"
        INPUT[입력 시퀀스<br/>1M 토큰] --> RS[관련성 신호<br/>Relevance Signal]
        RS --> SELECT{선택적 저장}
        SELECT -->|관련성 높음| STORE[Engram 저장소<br/>조건부 메모리]
        SELECT -->|관련성 낮음| SKIP[건너뛰기]
        STORE --> RETRIEVE[조건부 검색<br/>쿼리 기반]
        RETRIEVE --> OUTPUT[출력 생성]
    end

    subgraph "기존 방식 비교"
        STD[표준 어텐션<br/>O(n^2) 전체 참조] --> LIMIT[장문에서<br/>성능 저하]
        RAG_SYS[RAG 시스템<br/>외부 검색 필요] --> COMPLEX[시스템<br/>복잡도 증가]
    end
```

- 관련성 신호 기반으로 중요 정보만 선택적으로 메모리에 저장
- 표준 어텐션 대비 장문에서 현저한 정확도 향상
- RAG 파이프라인의 필요성을 줄여 시스템 복잡도 감소

### Huawei Ascend 학습 인프라

DeepSeek V4는 NVIDIA GPU 대신 Huawei의 Ascend 950PR 칩에서 학습되었다. 이는 미국의 대중국 반도체 수출 규제 환경에서 중국산 AI 가속기가 프론티어 모델 학습에 충분한 성능을 제공할 수 있음을 입증하는 사례다.

| 칩 | 용도 |
|---|---|
| Huawei Ascend 910B | 주요 학습 가속기 |
| Cambricon MLU | 보조 학습/추론 |
| Ascend 950PR | 차세대 추론 인프라 |

### R2 추론 모델

R2는 V4 아키텍처를 기반으로 한 추론 특화 변형이다. DeepSeek의 이전 추론 모델 라인(R1)을 계승하며, V4의 Engram Memory와 확장된 컨텍스트를 활용한 심층 추론 능력을 갖춘다. R1이 V3 아키텍처 위에서 강화학습을 통한 Chain-of-Thought 추론을 구현했던 것처럼, R2는 V4의 1T MoE 아키텍처와 1M 컨텍스트를 기반으로 더욱 깊은 추론 능력을 제공한다.

### 지정학적 맥락과 오픈소스 전략

DeepSeek V4는 단순한 기술적 업그레이드를 넘어, 미-중 AI 경쟁에서 중요한 이정표를 나타낸다. NVIDIA 칩 수출 규제 환경에서 Huawei Ascend 칩으로 프론티어 급 모델을 학습하는 데 성공한 것은 중국 AI 생태계의 자립 가능성을 보여주는 사례다.

DeepSeek는 MIT 또는 Apache 2.0 라이선스로 모델 가중치를 공개하는 전략을 유지해왔으며, V4에서도 이를 계승할 것으로 예상된다. 이는 [[llama-4]]와 함께 오픈소스 진영의 양대 축을 형성한다. 학습 비용 약 520만 달러는 동급 프론티어 모델 대비 극히 낮은 수준으로, 효율적인 학습 기법의 우수성을 시사한다.

## 벤치마크

DeepSeek의 자체 보고 벤치마크 (독립 검증 전).

| 벤치마크 | DeepSeek V4 | Claude Opus 4.5 | 비고 |
|---|---|---|---|
| HumanEval | ~90% | ~88% | 코딩 |
| SWE-bench Verified | 80%+ | 80.9% | 소프트웨어 엔지니어링 |
| 수학 추론 | Claude 대비 115% | 기준 | 수학 |
| Needle-in-a-Haystack | 97% | - | 1M 토큰 검색 |

V3 대비 SWE-bench에서 약 31%p 향상 (49% --> 80%+).

[교차검증 필요] 위 벤치마크는 DeepSeek 자체 보고 수치이며, 독립적인 제3자 검증은 아직 이루어지지 않았다.

### 예상 API 가격

| 항목 | 가격 | Claude Opus 대비 |
|---|---|---|
| 입력 | $0.28 / 1M 토큰 | ~1/50 |
| 출력 | $0.50-1.10 / 1M 토큰 | ~1/25 |

### API 접근 방법

1. DeepSeek 공식 API
2. OpenRouter
3. HuggingFace (오픈 가중치)
4. Ollama (로컬 실행)
5. Fireworks AI 등 제3자 API

## 관련 문서

- [[deepseek-v3-2]] - 이전 모델: DeepSeek-V3.2
- [[llama-4]] - 경쟁 모델: Llama 4 (MoE 오픈소스)
- [[gpt-6-spud]] - 경쟁 모델: GPT-6/Spud
- [[claude-opus-4-6]] - 경쟁 모델: Claude Opus 4.6

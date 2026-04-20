---
title: DeepSeek-V3.2 / V3.2-Speciale
category: tooling
page_type: entity
project: DeepSeek
tags: [deepseek, v3-2, speciale, sparse-attention, thinking-mode, open-source, mit]
sources: [raw/2026-04-14-ai-hot-topics-100.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

DeepSeek-V3.2는 DeepSeek가 출시한 685B 파라미터 오픈소스 대규모 언어 모델이다. DeepSeek Sparse Attention(DSA)과 사고 모드(thinking mode) 통합이 핵심으로, GPT-5 수준의 성능을 제공한다. V3.2-Speciale 변형은 GPT-5를 능가하는 추론 능력을 보이며, IMO/IOI 2025에서 금메달 수준의 수학/프로그래밍 능력을 입증했다. MIT 라이선스로 공개되었다.

## 핵심 특징

- **DeepSeek Sparse Attention (DSA)**: 장문 컨텍스트에서 계산 복잡도를 줄이면서 성능 유지
- **사고 모드 통합**: 최초로 사고(thinking)를 도구 사용(tool-use)에 직접 통합
- **대규모 에이전트 학습 데이터 합성**: 1,800개 이상 환경, 85,000개 이상 복잡 지시사항 커버
- **IMO/IOI 금메달 수준**: V3.2-Speciale이 IMO, CMO, ICPC World Finals, IOI 2025에서 금메달급 결과
- **MIT 라이선스**: 완전 개방형 상업적 사용 가능

## 모델 변형

| 변형 | 포지셔닝 | 도구 사용 | 특징 |
|---|---|---|---|
| **V3.2** | GPT-5 수준 | 지원 (사고 모드 통합) | 균형 잡힌 추론 vs 길이 |
| **V3.2-Speciale** | Gemini-3.0-Pro 경쟁 | 미지원 (심층 추론 전용) | 최대 추론 성능 |

## 아키텍처

Mixture-of-Experts([[mixture-of-experts|MoE]]) 기반 685B 파라미터 아키텍처로, 두 가지 핵심 혁신을 포함한다.

### Multi-Head Latent Attention (MLA)

KV 텐서를 저차원 공간으로 압축하여 캐싱한 뒤, 추론 시 원래 차원으로 복원한다. 메모리 사용량을 줄이면서 계산 오버헤드는 최소화한다.

### DeepSeek Sparse Attention (DSA)

모든 이전 토큰에 어텐션을 적용하는 대신, 관련성 높은 과거 토큰만 선택적으로 처리하는 학습된 희소 메커니즘이다. "Lightning Indexer"가 관련성 점수를 계산하고 "Token-Selector"가 상위 k개 토큰(k=2048)을 선택한다. 계산 복잡도를 O(L^2)에서 O(Lk)로 줄여 장문 컨텍스트에서 추론 비용을 대폭 절감한다.

```mermaid
graph TB
    subgraph "DeepSeek-V3.2 (685B MoE)"
        MLA[Multi-Head Latent Attention<br/>KV 텐서 저차원 압축]
        DSA[DeepSeek Sparse Attention<br/>O(L^2) -> O(Lk) 복잡도]
        THINK[사고 모드<br/>reasoning_content]
        TOOL[도구 호출 통합<br/>사고 + 도구 동시 사용]
        DEV[developer 역할<br/>검색 에이전트 시나리오 전용]
    end

    subgraph "에이전트 학습 파이프라인"
        ENV[1,800+ 환경]
        INST[85K+ 복잡 지시사항]
        SYNTH[대규모 합성 데이터]
    end

    ENV --> SYNTH
    INST --> SYNTH
    SYNTH --> MLA

    subgraph "V3.2-Speciale"
        DEEP[심층 추론 전용<br/>길이 페널티 제거]
        MATH[수학 올림피아드<br/>IMO/CMO 금메달]
        PROG[프로그래밍 올림피아드<br/>IOI/ICPC 금메달]
    end

    MLA --> DSA --> THINK --> TOOL
    DSA --> DEEP --> MATH
    DEEP --> PROG
```

## 벤치마크 성능

| 벤치마크 | V3.2 점수 |
|---|---|
| MMLU Pro | 85 |
| GPQA Diamond | 82.4 |
| AIME 2026 | 94.17 |
| HMMT Feb 2026 | 84.09 |
| SWE-Bench Pro | 15.56 |
| SWE-Bench Resolved | 70% |

### 올림피아드 성과 (V3.2-Speciale)

- International Mathematical Olympiad (IMO 2025) -- 금메달
- International Olympiad in Informatics (IOI 2025) -- 금메달
- ICPC World Finals -- 강력한 결과
- Chinese Mathematical Olympiad (CMO 2025) -- 금메달급

## 기술 상세

### 학습 방법론

V3.2의 학습 파이프라인은 여러 혁신을 포함한다:

- **RLVR (Reinforcement Learning with Verifiable Rewards)**: 수학/코드 도메인에서는 기호 검증기(symbolic verifier)를, 일반 태스크에서는 생성형 리워드 모델을 사용
- **GRPO 알고리즘 개선**: 오프-폴리시 시퀀스 마스킹, 도메인별 KL 가중치, 편향 없는 KL 추정, MoE 모델의 라우팅 패턴 보존
- **자기 검증(Self-Verification)**: 별도의 검증 LLM이 추론 품질을 평가하고, 메타-검증기가 검증기의 신뢰도를 보장
- **자기 정제(Self-Refinement)**: 최대 8회 반복 정제를 통해 출력 품질을 점진적으로 개선

### 채팅 템플릿 변경

V3.2는 새로운 채팅 템플릿을 도입했다:

- `reasoning_content` 필드로 명시적 사고 내용 지원
- `developer` 역할 추가 (검색 에이전트 시나리오 전용)
- Jinja 포맷 미사용 -- Python 인코딩 스크립트 사용

### 사고 모드와 도구 사용 통합

V3.2가 최초로 사고 프로세스를 도구 호출에 직접 통합했다. 사고 모드와 비사고 모드 모두에서 도구 사용이 가능하여, 에이전틱 태스크에서의 추론 품질이 향상되었다.

V3.2-Speciale은 추론 데이터 전용으로 학습된 "확장 사고(extended-thinking)" 변형으로, 길이 페널티를 제거하여 복잡한 추론 태스크에서 더 긴 응답 생성이 가능하다. 이는 계산량을 정확도로 교환하는 추론 스케일링([[kv-cache-inference|inference]] scaling)의 한 형태다.

### 권장 샘플링 파라미터

```
temperature = 1.0
top_p = 0.95
```

## 경쟁 모델 비교

| 모델 | 파라미터 | GPQA Diamond | AIME 2026 | 라이선스 | 특징 |
|------|---------|-------------|-----------|---------|------|
| **DeepSeek-V3.2** | 685B (MoE) | 82.4 | 94.17 | MIT | DSA + 사고/도구 통합 |
| GPT-5 | 비공개 | ~83 | ~90 | 상용 | 프론티어 범용 |
| Gemini 3.0 Pro | 비공개 | ~85 | ~88 | 상용 | 멀티모달 강점 |
| Qwen3.6+ | 비공개 | ~80 | ~85 | Apache 2.0 | 다국어 강점 |
| Llama 4 Maverick | 400B (MoE) | ~78 | ~75 | Llama | Meta 오픈소스 |

V3.2는 MIT 라이선스 오픈소스 모델 중 GPT-5급 성능을 달성한 최초 사례로, 오픈소스와 상용 모델 간의 성능 격차가 사실상 소멸했음을 보여준다. HuggingFace에서 월간 640만+ 다운로드를 기록하고 있다.

## 접근 방법

- **DeepSeek Chat**: chat.deepseek.com
- **DeepSeek API**: 앱, 웹, API 플랫폼
- **HuggingFace**: 모델 가중치 다운로드 (6.4M+ 월간 다운로드)
- **로컬 배포**: llama.cpp, LM Studio, Jan, Ollama 등 양자화 버전 제공

## 관련 문서

- [[gemma-4]] - Google의 오픈소스 경쟁 모델
- [[qwen3-6-plus]] - Alibaba의 오픈소스 경쟁 모델
- [[mistral-small-4]] - Mistral의 MoE 효율 모델
- [[gpt-5-4]] - OpenAI의 프론티어 모델 (비교 대상)

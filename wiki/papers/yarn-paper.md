---
title: "YaRN: Efficient Context Window Extension of Large Language Models (Peng et al., 2024)"
category: papers
page_type: paper
tags: [yarn, rope, context-extension, long-context, attention-scaling, ntk]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# YaRN: Efficient Context Window Extension of Large Language Models (Peng et al., 2024)

## 핵심 기여

Bowen Peng 등이 발표한 YaRN(Yet another RoPE extensioN method)은 **NTK-aware 보간(NTK-by-parts interpolation)과 어텐션 온도 스케일링(attention temperature scaling)을 결합**해 RoPE 기반 모델의 컨텍스트 창을 최소한의 파인튜닝으로 크게 확장하는 방법이다. 기존 Position Interpolation(PI)이나 단순 NTK 보간보다 긴 컨텍스트에서의 언어 모델링 성능을 더 잘 유지하며, Llama-2(4K 컨텍스트)를 64K~128K으로 확장하는 실험에서 효과를 실증했다.

## 방법

### 배경: RoPE와 컨텍스트 한계

RoPE(Rotary Position Embedding)는 각 차원 $d$의 주파수를 $\theta_d = 10000^{-2d/D}$로 정의해 위치 정보를 인코딩한다. 학습 시 보지 못한 위치(out-of-distribution position)에서 성능이 급락하는 문제가 있다.

### NTK-by-Parts 보간

주파수 스펙트럼을 세 구간으로 나눠 구간별로 다른 처리를 적용한다:

- **고주파 차원** (단거리 의존성): 변경 없이 원본 RoPE 유지
- **저주파 차원** (장거리 의존성): 선형 보간(position interpolation) 적용
- **중간 주파수**: 두 방법을 가중치로 혼합

이 접근이 핵심인 이유는 저주파 차원은 멀리 떨어진 토큰 관계를 인코딩하므로 보간이 필요하지만, 고주파 차원은 보간 시 로컬 구조가 망가지기 때문이다.

### 어텐션 온도 스케일링 (Attention Temperature)

컨텍스트 길이가 늘면 어텐션 엔트로피가 증가해 모델이 긴 문맥에서 주의를 분산시키는 문제가 생긴다. YaRN은 소프트맥스 이전 스케일 인수 $\sqrt{d_k}$를 수정하는 **$t$ 스케일링 인수**를 도입해 이를 보정한다:

$$\text{Attention} = \text{softmax}\!\left(\frac{QK^T}{t \cdot \sqrt{d_k}}\right)V$$

확장 비율 $s$에 따라 $t = 0.1\ln(s) + 1$로 설정.

```mermaid
flowchart LR
    Base["기반 RoPE 모델\n(예: Llama-2 4K)"] --> NTK["NTK-by-Parts 보간\n주파수별 차등 처리"]
    NTK --> Temp["어텐션 온도 스케일링\nt = 0.1·ln(s)+1"]
    Temp --> Finetune["소규모 파인튜닝\n(400~1000 스텝)"]
    Finetune --> Extended["확장 모델\n(64K / 128K 컨텍스트)"]
```

### 파인튜닝 효율

원본 학습 토큰의 0.1% 미만(400~1000 스텝)으로도 충분한 컨텍스트 확장 효과를 달성한다.

## 결과

- Llama-2 7B 기반 YaRN-64K: Perplexity 기준 원본 대비 거의 손실 없이 16배 컨텍스트 확장
- Passkey Retrieval(긴 문서에서 숫자 키 찾기) 테스트: 128K 위치에서 100% 정확도
- LongBench 기준 동일 확장 비율의 PI, NTK 방법 대비 우수한 성능
- Mistral 7B 기반 Yarn-Mistral 128K 모델이 공개돼 실용적으로 널리 사용됨

## 한계

- **데이터 분포 의존성**: 확장 파인튜닝 시 긴 문서 데이터가 필요하며, 긴 문서가 부족한 도메인에서는 효과 제한
- **단순 검색 vs 복잡 추론 격차**: Passkey Retrieval에서는 높은 정확도지만 긴 문서 다중 홉 추론은 여전히 어려움 (Lost-in-the-Middle 문제)
- $t$ 스케일링 하이퍼파라미터는 모델과 확장 비율마다 재조정이 필요할 수 있음
- 극단적으로 긴 컨텍스트(1M+)에서 어텐션 연산 복잡도는 여전히 $O(n^2)$

## 실무 적용 관점

- Llama, Mistral 기반 모델에 가장 바로 적용 가능한 RoPE 확장 기법. Hugging Face `transformers` 라이브러리가 `rope_scaling: {"type": "yarn", ...}` 설정을 지원
- 장문 문서 요약, RAG 파이프라인의 대형 청크 처리, 코드 저장소 전체 컨텍스트 주입 시나리오에 유리
- 대안 기법 비교: LongRoPE(동적 베이스 조정), Rope Scaling NTK(단순 베이스 스케일링)와 달리 YaRN은 주파수별 차등 처리로 더 세밀한 제어 가능
- 추론 시 메모리 병목(KV 캐시 크기 선형 증가)은 별도로 해결해야 함 - 청킹 전략이나 sparse attention과 병행 필요

## 관련 문서

- [[rope-scaling-ntk-yarn]]
- [[long-context-scaling]]
- [[lost-in-the-middle-paper]]
- [[kv-cache-inference]]
- [[positional-encoding]]

---
title: 트랜스포머 어텐션 메커니즘 (Transformer Attention Mechanisms)
category: architectures
page_type: concept
tags: [architectures, attention, transformer, mha, mla, gqa, kv-cache, flash-attention, hub]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

이 페이지는 트랜스포머 아키텍처의 어텐션 메커니즘 변형들을 연결하는 허브다. Vaswani et al.(2017)의 "Attention Is All You Need"에서 제안된 Multi-Head Attention(MHA)은 현대 LLM의 기반이지만, 추론 시 KV 캐시의 메모리 대역폭 병목이 핵심 한계다. 이를 해결하기 위해 MQA, GQA, MLA 등 다양한 변형이 등장했으며, Flash Attention 계열은 하드웨어 수준의 최적화로 어텐션 연산 자체의 효율을 개선한다.

어텐션 메커니즘의 진화 방향은 크게 두 축이다. 첫째, KV 캐시 메모리를 줄이면서 모델 품질을 유지하는 것(MQA -> GQA -> MLA). 둘째, 어텐션 연산 자체를 하드웨어에 최적화하는 것(Flash Attention 계열).

## 어텐션 변형 스펙트럼

### Multi-Head Attention (MHA)

원본 트랜스포머의 어텐션 메커니즘이다. H개의 독립적인 Query, Key, Value 헤드가 병렬로 어텐션을 계산하고, 결과를 연결(concatenate)하여 최종 출력을 생성한다. 각 헤드가 입력의 다른 관계 패턴을 포착할 수 있다.

MHA의 핵심 한계는 추론 시 자기회귀 디코딩에서 나타난다. 모든 어텐션 Key와 Value를 각 디코더 스텝마다 메모리에서 로드해야 하므로, 메모리 대역폭이 병목이 된다. KV 캐시 크기는 (배치 크기 x 헤드 수 x 시퀀스 길이 x 헤드 차원 x 2) 비례로 증가한다.

### Multi-Query Attention (MQA)

Noam Shazeer(2019)가 제안했다. 모든 Query 헤드가 단일 K, V 헤드를 공유한다. KV 캐시 크기를 H배 줄여 디코더 추론 속도를 대폭 향상시킨다. 그러나 모든 헤드가 동일한 K, V를 참조하므로 모델 품질이 저하될 수 있으며, 기존 MHA 모델의 체크포인트를 MQA로 변환할 수 없어 처음부터 재학습이 필요하다.

### [[multi-head-latent-attention|GQA (Grouped-Query Attention)]]

Ainslie et al.(2023, "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints")이 제안한 MHA와 MQA의 절충안이다. Query 헤드를 G개 그룹으로 나누고, 각 그룹이 하나의 K, V 헤드를 공유한다. G=1이면 MQA, G=H이면 MHA와 동일하다.

GQA는 MHA에 근접한 품질을 유지하면서 MQA에 가까운 추론 속도를 달성한다. 결정적으로, 기존 MHA 체크포인트를 GQA로 변환(uptrain)할 수 있어 처음부터 재학습할 필요가 없다. Meta가 Llama 2(2023년 7월)에서 처음 채택한 이후 Llama 3까지 유지하고 있으며, 2024-2025년 주류 LLM의 표준 어텐션이 되었다.

### [[multi-head-latent-attention|MLA (Multi-Head Latent Attention)]]

DeepSeek-V2(2024)에서 도입된 어텐션 메커니즘이다. [[multi-head-latent-attention|MLA]]는 저랭크 팩터화(low-rank factorization)를 통해 KV 캐시를 최대 93.3% 축소하면서 MHA 수준의 표현력을 유지한다. 각 헤드별 독립 K, V 벡터 대신, 압축된 잠재 벡터(latent vector)를 캐시에 저장하고 추론 시 동적으로 복원한다.

GQA가 K, V 헤드 수를 줄이는 접근이라면, MLA는 K, V의 차원 자체를 압축하는 접근이다. 이론적으로 MLA의 위치 비의존 부분의 표현력은 GQA보다 엄밀히 강하다. MTLA(Multi-Token Latent Attention)는 시간 축 추가 압축을 적용한 확장 변형이다.

## KV 캐시 관리

어텐션 변형의 핵심 동기인 KV 캐시 관리는 추론 효율의 핵심이다.

**Paged Attention**: vLLM이 도입한 기법으로, OS의 가상 메모리 페이징에서 영감을 받아 KV 캐시를 고정 크기 블록으로 관리한다. 메모리 단편화를 제거하고 배치 처리 효율을 극대화한다.

**접두사 캐싱(Prefix Caching)**: 동일한 프롬프트 접두사에 대한 KV 캐시를 재사용한다. [[batch-inference-caching|배치 추론과 캐싱]] 페이지에서 자세히 다룬다.

**KV 캐시 압축**: SCORE, StreamingLLM, H2O(Heavy-Hitter Oracle) 등 캐시 예산을 동적으로 관리하는 기법들이 2025-2026년에 활발히 연구되고 있다.

## Flash Attention 계열

### Flash Attention 기초

Tri Dao(2022)가 제안한 IO-aware 어텐션 알고리즘이다. GPU의 SRAM과 HBM 사이 데이터 이동을 최소화하는 타일링(tiling) 기법으로, 정확한(exact) 어텐션을 O(N) 추가 메모리로 계산한다. 근사(approximation)가 아닌 수학적으로 동일한 결과를 더 빠르게 계산한다는 점이 핵심이다.

### Flash Attention 이후 발전

Flash Attention 2(2023)는 워크 파티셔닝과 비인과적/인과적 마스크 최적화를 추가했다. Flash Attention 3(2024)는 Hopper GPU(H100)의 TMA, WGMMA 명령어를 활용한 추가 최적화를 도입했다. 2026년에는 Flash Attention 4가 Blackwell 아키텍처에 최적화되어 발전하고 있다.

## [[gated-attention|Gated Attention]]

[[gated-attention|Gated Attention]]은 Scaled Dot-Product Attention 출력에 학습 가능한 시그모이드 게이트를 적용하여 비선형성과 스파시티를 동시에 달성한다. Alibaba Qwen 팀이 탐구했으며 NeurIPS 2025 Best Paper로 선정되었다. MHA/GQA/MLA와 독립적으로 적용 가능한 직교(orthogonal) 기법이다.

## 어텐션 효율 비교

| 메커니즘 | KV 캐시 크기 (상대) | 모델 품질 | 기존 체크포인트 변환 |
|---------|---------------------|----------|---------------------|
| MHA     | 1x (기준)           | 최고     | -                   |
| MQA     | 1/H                | 약간 저하 | 불가                |
| GQA     | G/H                | MHA 근접 | 가능 (uptrain)       |
| MLA     | ~0.07x             | MHA 동등+ | 별도 학습 필요       |

## 채택 현황 (2026)

- **GQA**: Llama 2/3, Gemma, Mistral 등 대다수 오픈소스 LLM의 기본
- **MLA**: DeepSeek-V2/V3, DeepSeek-R1 등 DeepSeek 계열
- **MHA**: GPT-4 등 레거시 모델, 새로운 대규모 모델에서는 점차 축소
- **Flash Attention**: 사실상 모든 프로덕션 LLM에서 사용

## 관련 문서

- [[multi-head-latent-attention]] -- MLA/MTLA 상세
- [[gated-attention]] -- Gated Attention 메커니즘
- [[gated-deltanet]] -- Gated DeltaNet
- [[long-context-scaling]] -- 긴 컨텍스트 어텐션 스케일링
- [[deepseek-mhc]] -- DeepSeek Multi-Head Compression
- [[batch-inference-caching]] -- KV 캐시 재사용 전략
- [[superposition-neural-scaling]] -- 어텐션과 스케일링의 관계

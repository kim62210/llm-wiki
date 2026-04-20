---
title: 선형 어텐션 (Linear Attention)
category: architectures
page_type: concept
tags: [linear-attention, kernel-attention, performer, efficient-attention]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 선형 어텐션 (Linear Attention)

선형 어텐션(Linear Attention)은 표준 Softmax 어텐션의 $O(n^2)$ 시간/공간 복잡도를 **$O(n)$으로 감소**시키는 어텐션 변형의 총칭이다. 핵심 아이디어는 Softmax를 커널 함수로 근사해 행렬 곱 순서를 바꾸는 것이다.

## 표준 vs 선형 어텐션

### 표준 Softmax 어텐션

$$\text{Attn}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V$$

$n \times n$ 어텐션 행렬 계산으로 $O(n^2 d)$ 복잡도.

### 선형 어텐션 (커널 근사)

Softmax를 커널 함수 $\phi$의 내적으로 근사한다:

$$\text{softmax}(q^T k) \approx \phi(q)^T \phi(k)$$

이를 적용하면:

$$\text{Attn}(Q, K, V) \approx \frac{\phi(Q)(\phi(K)^T V)}{\phi(Q)\phi(K)^T \mathbf{1}}$$

**핵심**: $\phi(K)^T V$를 먼저 계산하면 $(d \times d)$ 행렬이 되어, 전체 복잡도가 $O(nd^2)$로 감소한다.

## 표준 vs 선형 어텐션 복잡도 비교

```mermaid
flowchart LR
    subgraph 표준 어텐션 "표준 어텐션 O(n²d)"
        QK["QK^T\n계산 (n×n)"] --> SOFTMAX["Softmax"] --> V1["× V\n(n×d)"]
    end
    subgraph 선형 어텐션 "선형 어텐션 O(nd²)"
        PHI["φ(K)^T V\n먼저 계산 (d×d)"] --> PHIQ["φ(Q) ×\n(n×d²)"]
    end
```

$n \gg d$ 인 경우 (긴 시퀀스) 선형 어텐션이 유리하다.

## 주요 구현

### Performer (FAVOR+)

Choromanski et al. (2020). **FAVOR+(Fast Attention Via Positive Orthogonal Random Features)**로 Softmax를 근사한다. 랜덤 피처(random features)를 사용해 커널 함수를 구성한다:

$$\phi(x) = \frac{e^{-\|x\|^2/2}}{\sqrt{m}} [e^{\omega_1^T x}, \ldots, e^{\omega_m^T x}]$$

$\omega_i$는 직교 랜덤 벡터. $m$이 클수록 Softmax 근사가 정확해지지만 비용도 증가한다.

### cosFormer

Qin et al. (2022). 코사인 함수 기반 재정규화로 선형성을 유지하면서 Softmax의 집중도(concentration) 특성을 근사한다.

### GLA (Gated Linear Attention)

Yang et al. (2023). 게이팅 메커니즘을 추가해 선형 어텐션의 표현력을 높였다. 하드웨어 효율적인 청크(chunk) 병렬화 구현으로 실용성을 확보했다.

## 정확도-효율 트레이드오프

| 모델 | 복잡도 | Softmax 근사 품질 | 긴 시퀀스 효율 |
|------|-------|-----------------|-------------|
| Standard Attn | $O(n^2 d)$ | 완벽 | 나쁨 |
| Performer | $O(nd^2m)$ | 좋음 | 좋음 |
| cosFormer | $O(nd^2)$ | 중간 | 좋음 |
| GLA | $O(nd^2)$ | 낮음 | 매우 좋음 |

핵심 한계: 선형 어텐션은 **전역 정보 통합 능력**이 Softmax 어텐션보다 약하다. 특히 특정 위치에 강하게 집중하는(sharp attention) 패턴을 표현하기 어렵다.

## SSM과의 수학적 연결

Mamba-2(SSD: State Space Duality)가 보여주듯, 선형 어텐션과 선택적 SSM은 수학적으로 동치이다. 두 방법 모두 상태 $S = \phi(K)^T V$ (또는 SSM의 상태 행렬)를 순환적으로 업데이트한다. 이 통일된 시각이 GLA, Mamba-2, xLSTM 등 후속 모델 설계에 영향을 미쳤다.

## 관련 문서
- [[performer-favor]] -- Performer / FAVOR+ - 무작위 특성 어텐션
- [[metaformer]] -- MetaFormer - 토큰 믹서 추상화 패러다임
- [[self-attention-mechanism|셀프 어텐션]]
- [[gated-deltanet|Gated DeltaNet]]
- [[state-space-models-general|SSM 일반]]
- [[mamba-3|Mamba-3]]
- [[rwkv|RWKV]]

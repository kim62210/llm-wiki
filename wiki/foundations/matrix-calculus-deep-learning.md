---
title: 딥러닝을 위한 행렬 미적분
category: foundations
page_type: concept
tags: [선형대수, 미적분, 역전파, 야코비안, 헤시안, 자동미분]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# 딥러닝을 위한 행렬 미적분

## 개요

행렬 미적분(matrix calculus)은 벡터·행렬·텐서를 대상으로 하는 미적분의 확장이다. 딥러닝에서 역전파(backpropagation) 알고리즘을 올바르게 이해하고 구현하려면, 스칼라·벡터·행렬 사이의 미분이 어떻게 정의되는지 명확히 알아야 한다. 자동 미분(automatic differentiation) 라이브러리(PyTorch, JAX 등)가 이를 자동화하지만, 내부 동작과 수식 디버깅을 위해 직접 유도 능력이 필요하다.

## 표기 체계: 분자 레이아웃 vs 분모 레이아웃

미적분 문헌에는 두 가지 레이아웃 관례가 혼용되어 혼란을 야기한다.

| 레이아웃 | 정의 ($y \in \mathbb{R}^m$, $x \in \mathbb{R}^n$) | 야코비안 모양 |
|----------|---------------------------------------------------|--------------|
| 분자(Numerator) 레이아웃 | $\frac{\partial y}{\partial x}$의 $(i,j)$번째 원소 = $\frac{\partial y_i}{\partial x_j}$ | $m \times n$ |
| 분모(Denominator) 레이아웃 | $\frac{\partial y}{\partial x}$의 $(i,j)$번째 원소 = $\frac{\partial y_j}{\partial x_i}$ | $n \times m$ |

딥러닝 코드(PyTorch gradient 등)는 일반적으로 분모 레이아웃(분자 레이아웃의 전치)을 사용한다. 이 문서는 **분자 레이아웃**을 기본으로 한다.

## 기본 케이스 분류

미분의 입출력 유형에 따라 결과 구조가 달라진다:

| 분자 (피분함수) | 분모 (미분 변수) | 결과 | 이름 |
|----------------|----------------|------|------|
| 스칼라 $y$ | 스칼라 $x$ | 스칼라 | 일반 미분 |
| 스칼라 $y$ | 벡터 $\mathbf{x} \in \mathbb{R}^n$ | $1 \times n$ 행 벡터 | 기울기(gradient)의 전치 |
| 벡터 $\mathbf{y} \in \mathbb{R}^m$ | 스칼라 $x$ | $m \times 1$ 열 벡터 | - |
| 벡터 $\mathbf{y} \in \mathbb{R}^m$ | 벡터 $\mathbf{x} \in \mathbb{R}^n$ | $m \times n$ 행렬 | 야코비안(Jacobian) |
| 스칼라 $y$ | 행렬 $X \in \mathbb{R}^{m \times n}$ | $m \times n$ 행렬 | 기울기 행렬 |

## 기울기 (Gradient)

스칼라 함수 $f: \mathbb{R}^n \to \mathbb{R}$의 벡터 $\mathbf{x}$에 대한 기울기:

$$\nabla_\mathbf{x} f = \frac{\partial f}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix} \in \mathbb{R}^n$$

(열 벡터로 정의하면 분모 레이아웃과 일치)

### 자주 쓰이는 기울기 공식

- $\nabla_\mathbf{x} (\mathbf{a}^\top \mathbf{x}) = \mathbf{a}$
- $\nabla_\mathbf{x} (\mathbf{x}^\top \mathbf{x}) = 2\mathbf{x}$
- $\nabla_\mathbf{x} (\mathbf{x}^\top A \mathbf{x}) = (A + A^\top)\mathbf{x}$ ($A$가 대칭이면 $2A\mathbf{x}$)
- $\nabla_\mathbf{x} (\mathbf{a}^\top X \mathbf{b}) = \mathbf{a}\mathbf{b}^\top$ ($X$가 행렬일 때)

## 야코비안 (Jacobian)

벡터 함수 $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$의 야코비안:

$$J = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix} \in \mathbb{R}^{m \times n}$$

야코비안은 국소 선형 근사다: $\mathbf{f}(\mathbf{x} + \delta) \approx \mathbf{f}(\mathbf{x}) + J\delta$.

### 원소별 함수 (Element-wise Function)

$\mathbf{y} = \sigma(\mathbf{x})$ ($\sigma$가 ReLU, sigmoid 등 원소별 함수)이면 야코비안이 **대각 행렬**:

$$J_\sigma = \text{diag}(\sigma'(x_1), \ldots, \sigma'(x_n))$$

## 헤시안 (Hessian)

스칼라 함수 $f: \mathbb{R}^n \to \mathbb{R}$의 2차 미분:

$$H = \nabla^2_\mathbf{x} f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix} \in \mathbb{R}^{n \times n}$$

- $f$가 두 번 연속 미분 가능하면 $H$는 대칭 행렬
- 헤시안의 고유값(eigenvalue)이 모두 양수면 강볼록(strongly convex) - 최소점
- 헤시안의 고유값이 혼재하면 안장점(saddle point)

## 연쇄 법칙 (Chain Rule)과 역전파

### 스칼라 합성

$z = f(g(x))$이면: $\frac{dz}{dx} = \frac{dz}{dg} \cdot \frac{dg}{dx}$

### 벡터 합성 (야코비안 연쇄)

$\mathbf{z} = f(\mathbf{g}(\mathbf{x}))$이면 야코비안:

$$\frac{\partial \mathbf{z}}{\partial \mathbf{x}} = \frac{\partial \mathbf{z}}{\partial \mathbf{g}} \cdot \frac{\partial \mathbf{g}}{\partial \mathbf{x}} = J_f \cdot J_g$$

행렬 곱의 순서에 주의. 분자 레이아웃에서 야코비안을 왼쪽에서 오른쪽으로 합성한다.

### 역전파에서의 활용

손실 $L$, 출력 $\mathbf{o}$, 레이어 연산 $\mathbf{h} = W\mathbf{x} + \mathbf{b}$의 경우:

$$\frac{\partial L}{\partial W} = \frac{\partial L}{\partial \mathbf{o}} \cdot \frac{\partial \mathbf{o}}{\partial \mathbf{h}} \cdot \frac{\partial \mathbf{h}}{\partial W}$$

$\frac{\partial L}{\partial W}$는 $W$와 같은 모양의 행렬이어야 한다.

```mermaid
flowchart LR
    A[입력 x] --> B[선형 변환\nz = Wx + b]
    B --> C[비선형 활성화\nh = σ z]
    C --> D[손실 L]
    D -->|역전파: dL/dh| C
    C -->|dh/dz = diag σ' z| B
    B -->|dL/dW = dL/dz · x^T| A
    style D fill:#ffd700
```

위 다이어그램은 단일 레이어에서 순전파와 역전파 행렬 미적분 흐름을 나타낸다.

## 선형 레이어의 역전파 유도

$\mathbf{z} = W\mathbf{x} + \mathbf{b}$, $W \in \mathbb{R}^{m \times n}$, $\mathbf{x} \in \mathbb{R}^n$

상류 기울기 $\frac{\partial L}{\partial \mathbf{z}} \in \mathbb{R}^m$가 주어질 때:

$$\frac{\partial L}{\partial \mathbf{x}} = W^\top \frac{\partial L}{\partial \mathbf{z}} \in \mathbb{R}^n$$

$$\frac{\partial L}{\partial W} = \frac{\partial L}{\partial \mathbf{z}} \mathbf{x}^\top \in \mathbb{R}^{m \times n}$$

$$\frac{\partial L}{\partial \mathbf{b}} = \frac{\partial L}{\partial \mathbf{z}} \in \mathbb{R}^m$$

**미니배치**에서 $X \in \mathbb{R}^{B \times n}$ ($B$ = 배치 크기):

$$\frac{\partial L}{\partial W} = \left(\frac{\partial L}{\partial Z}\right)^\top X \in \mathbb{R}^{m \times n}$$

## 소프트맥스와 크로스엔트로피의 야코비안

소프트맥스 $p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$의 야코비안:

$$\frac{\partial p_i}{\partial z_j} = p_i(\delta_{ij} - p_j)$$

행렬 형태: $J_\text{softmax} = \text{diag}(\mathbf{p}) - \mathbf{p}\mathbf{p}^\top$

소프트맥스 + 크로스엔트로피를 합쳐서 유도하면 역전파가 극단적으로 단순해진다:

$$\frac{\partial L_\text{CE}}{\partial z_i} = p_i - y_i$$

원핫(one-hot) 정답 벡터에서 소프트맥스 출력을 뺀 것. 이것이 딥러닝 학습이 직관적으로 느껴지는 이유다.

## 배치 정규화 역전파

배치 정규화(batch normalization)는 역전파가 가장 복잡한 연산 중 하나다. 입력 $X \in \mathbb{R}^{B \times D}$에 대해:

1. $\mu = \frac{1}{B}\sum_b x_b$ (배치 평균)
2. $\sigma^2 = \frac{1}{B}\sum_b (x_b - \mu)^2$ (배치 분산)
3. $\hat{x}_b = (x_b - \mu)/\sqrt{\sigma^2 + \epsilon}$ (정규화)
4. $y_b = \gamma \hat{x}_b + \beta$ (스케일·시프트)

역전파 시 $\mu$와 $\sigma^2$이 모든 샘플에 의존하므로 야코비안이 밀집(dense) 행렬이 된다. Ioffe & Szegedy의 원논문에 전체 유도가 있다.

## 어텐션 메커니즘의 행렬 미적분

스케일드 닷프로덕트 어텐션(scaled dot-product attention):

$$\text{Attn}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right) V$$

역전파에서:
- $\frac{\partial L}{\partial Q}$: $A^\top$에 비례한 행렬 곱
- $\frac{\partial L}{\partial K}$: $A$에 비례한 행렬 곱
- $\frac{\partial L}{\partial V}$: 어텐션 가중치 행렬의 전치 곱

FlashAttention은 이 계산을 타일링으로 최적화해 메모리를 절약한다.

## 실무 주의점

1. **모양 추적**: 역전파 중간 텐서의 모양(shape)이 상류 기울기와 가중치 행렬에서 반드시 일치해야 함
2. **전치 위치**: $W^\top$ vs $W$를 혼동하면 기울기 방향이 반대가 됨
3. **sum reduction**: 배치 차원에 대해 합산하거나 평균내야 함
4. **in-place 연산**: PyTorch에서 in-place 연산은 자동 미분 그래프를 손상시킬 수 있음

## 관련 문서

- [[gradient-descent-backpropagation]] - 역전파 알고리즘 전체 흐름
- [[automatic-differentiation]] - 자동 미분: 역전파의 소프트웨어 구현
- [[second-order-optimization]] - 헤시안 활용 2차 최적화
- [[natural-gradient]] - 피셔 정보 행렬을 활용한 자연 경사법
- [[optimization-theory]] - 최적화 이론의 수학적 기반
- [[fisher-information-matrix]] - 피셔 정보 행렬과 자연 경사

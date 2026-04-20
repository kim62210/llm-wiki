---
title: 선형 회귀와 최소제곱법 (Linear Regression & OLS)
category: foundations
page_type: concept
tags: [linear-regression, ols, regression, ridge, lasso]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 선형 회귀와 최소제곱법 (Linear Regression & OLS)

입력 특징과 연속형 출력 사이의 선형 관계를 학습하는 가장 기본적인 지도 학습 알고리즘. 단순함에도 불구하고 해석 가능성과 계산 효율 덕분에 베이스라인으로 널리 쓰인다.

## 모델 정의

$$\hat{y} = \mathbf{w}^T \mathbf{x} + b = \sum_{j=1}^{p} w_j x_j + b$$

손실 함수(MSE):

$$\mathcal{L}(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{1}{n} \|\mathbf{y} - \mathbf{X}\mathbf{w}\|^2$$

## 정규방정식 (Normal Equation) 유도

$\mathcal{L}$을 $\mathbf{w}$에 대해 미분하여 0으로 놓으면:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = -\frac{2}{n} \mathbf{X}^T(\mathbf{y} - \mathbf{X}\mathbf{w}) = 0$$

$$\mathbf{X}^T \mathbf{X} \mathbf{w} = \mathbf{X}^T \mathbf{y}$$

$$\hat{\mathbf{w}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

$\mathbf{X}^T\mathbf{X}$가 역행렬이 존재하는 경우 닫힌 형태(closed-form) 해가 존재한다. 특징 수 $p$가 크면 역행렬 계산($O(p^3)$)이 비싸므로 경사 하강법을 사용한다.

## Ridge(L2)와 Lasso(L1) 정규화

### 기하학적 해석

```mermaid
flowchart LR
    subgraph Ridge["Ridge (L2) - 타원형 제약"]
        R1[손실 등고선] -->|타원형 제약구\n∑w²≤t| R2[부드러운 가중치 축소]
    end
    subgraph Lasso["Lasso (L1) - 다이아몬드 제약"]
        L1[손실 등고선] -->|다이아몬드 제약구\n∑|w|≤t| L2[희소 해 - 일부 w=0]
    end
```

- **Ridge**: $\mathcal{L} + \lambda \sum w_j^2$ - 계수를 0 방향으로 수축시키지만 정확히 0이 되지는 않음. 닫힌 형태 해 존재: $\hat{\mathbf{w}} = (\mathbf{X}^T\mathbf{X} + \lambda I)^{-1}\mathbf{X}^T\mathbf{y}$
- **Lasso**: $\mathcal{L} + \lambda \sum |w_j|$ - 다이아몬드 제약 경계의 꼭짓점에서 접선 → 일부 계수가 정확히 0 → 자동 특징 선택(feature selection)
- **Elastic Net**: $\alpha \cdot \text{Ridge} + (1-\alpha) \cdot \text{Lasso}$ - 두 장점 결합

| 항목 | Ridge | Lasso | Elastic Net |
|------|-------|-------|-------------|
| 제약 형태 | $\ell_2$ 구 | $\ell_1$ 다이아몬드 | 혼합 |
| 특징 선택 | 불가 | 가능 (희소) | 가능 |
| 다중공선성 대응 | 우수 | 임의 선택 | 우수 |
| 닫힌 형태 해 | 있음 | 없음 (좌표 하강) | 없음 |

## 다중공선성 (Multicollinearity)

특징들 사이에 강한 선형 관계가 있을 때 $\mathbf{X}^T\mathbf{X}$가 특이(singular)하거나 거의 특이한 상태가 된다.

- **증상**: 회귀 계수의 분산이 극도로 커짐, 계수 부호가 직관과 반대로 나타남
- **진단**: VIF(분산 팽창 인수, Variance Inflation Factor) $> 10$ 이면 심각한 다중공선성
  $$VIF_j = \frac{1}{1 - R_j^2}$$
  ($R_j^2$: $j$번째 특징을 나머지로 회귀했을 때의 결정계수)
- **해결**: Ridge 정규화, PCA 후 회귀(PCR), 특징 제거

## 회귀 진단 - 잔차 분석

OLS 가정(가우스-마르코프 가정) 위반 여부를 잔차(residual) $e_i = y_i - \hat{y}_i$로 확인한다.

| 진단 | 확인 방법 | 위반 시 대응 |
|------|----------|-----------|
| 선형성 | 잔차 vs 적합값 플롯 - 무작위 분포 확인 | 비선형 변환, 다항 항 추가 |
| 등분산성 | 잔차 분산이 균등한지 확인 | 가중 최소제곱(WLS), 로그 변환 |
| 정규성 | QQ 플롯, Shapiro-Wilk 검정 | 표본 크기 증가 (CLT 활용) |
| 독립성 | Durbin-Watson 검정 (시계열) | 자기회귀 모델 사용 |

## 관련 문서

- [[logistic-regression]]
- [[overfitting-regularization]]
- [[pca]]

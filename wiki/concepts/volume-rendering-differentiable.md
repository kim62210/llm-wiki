---
title: 미분 가능 볼륨 렌더링
category: concepts
page_type: concept
tags: [volume-rendering, nerf, differentiable, 3d, rendering]
sources: [raw/2026-04-17-topic-queue-v2.md]
created: 2026-04-17
updated: 2026-04-17
---

# 미분 가능 볼륨 렌더링

## 개요

미분 가능 볼륨 렌더링(differentiable volume rendering)은 3D 장면에서 2D 이미지를 생성하는 렌더링 과정을 **미분 가능하게(differentiable)** 구현한 기법이다. 이를 통해 렌더링 출력의 손실(loss)로부터 기울기를 역전파해 3D 표현을 직접 최적화할 수 있다. [[nerf-neural-radiance-fields|NeRF]]와 [[3d-gaussian-splatting]]의 핵심 렌더링 엔진이며, 현대 뉴럴 3D 재구성의 토대다.

## 물리 기반 볼륨 렌더링 원리

볼륨 렌더링은 광선(ray)이 3D 볼륨을 통과할 때 흡수(absorption)와 방출(emission)을 적분하는 과정이다. 카메라 원점 $\mathbf{o}$에서 방향 $\mathbf{d}$로 발사된 광선 $\mathbf{r}(t) = \mathbf{o} + t\mathbf{d}$에 대해, 픽셀의 색상은 다음 적분으로 결정된다:

$$C(\mathbf{r}) = \int_{t_n}^{t_f} T(t) \cdot \sigma(\mathbf{r}(t)) \cdot \mathbf{c}(\mathbf{r}(t), \mathbf{d}) \, dt$$

여기서:
- $T(t) = \exp\!\left(-\int_{t_n}^{t} \sigma(\mathbf{r}(s)) \, ds\right)$: 광선이 $t_n$부터 $t$까지 투과되는 비율(transmittance)
- $\sigma(\cdot)$: 밀도(volume density)
- $\mathbf{c}(\cdot)$: 방출 색상(emitted color)

## 이산 근사와 역전파

연속 적분을 실제로 계산하기 위해 광선 위 $N$개의 샘플 포인트를 취한 뒤 구분구적법(quadrature)으로 근사한다:

$$\hat{C}(\mathbf{r}) = \sum_{i=1}^{N} T_i \left(1 - \exp(-\sigma_i \delta_i)\right) \mathbf{c}_i$$

$$T_i = \exp\left(-\sum_{j=1}^{i-1} \sigma_j \delta_j\right)$$

$\delta_i = t_{i+1} - t_i$는 인접 샘플 간 거리. 이 공식은 완전히 미분 가능하여 $\sigma_i$와 $\mathbf{c}_i$에 대한 기울기를 역전파로 구할 수 있다.

```mermaid
flowchart TD
    Cam[카메라 파라미터] --> Ray[광선 생성\n픽셀별 방향 벡터]
    Ray --> Sample[광선 위 N점 샘플링\n계층적 샘플링 적용]
    Sample --> Query[3D 표현 조회\nNeRF MLP 또는 3DGS]
    Query --> Density[밀도 σ 및 색상 c 획득]
    Density --> Alpha["알파 합성\nα = 1 - exp(-σδ)"]
    Alpha --> Composite[프론트-투-백 합성\n누적 투과율 T 계산]
    Composite --> Pixel[픽셀 색상 C_hat]
    Pixel --> Loss[L2 손실\n|C_hat - C_gt|²]
    Loss --> Backprop[역전파\n∂Loss/∂σ, ∂Loss/∂c]
    Backprop --> Query
```

## NeRF에서의 적용

[[nerf-neural-radiance-fields|NeRF]]는 MLP가 $(\mathbf{x}, \mathbf{d}) \mapsto (\sigma, \mathbf{c})$를 예측하게 학습한다. 미분 가능 볼륨 렌더링 덕분에 **2D 이미지만으로 3D MLP를 지도학습 없이 최적화**할 수 있다. 손실은 단순히 렌더링된 픽셀 색상과 실제 픽셀 색상의 L2 거리다:

$$\mathcal{L} = \sum_{\mathbf{r} \in \mathcal{R}} \|\hat{C}(\mathbf{r}) - C(\mathbf{r})\|_2^2$$

이 단순한 손실이 복잡한 3D 형상과 재질을 암묵적으로 학습시킨다.

## 3D Gaussian Splatting에서의 차이

[[3d-gaussian-splatting]]도 알파 합성 기반 렌더링을 쓰지만, 방식이 다르다:

| 특성 | NeRF 볼륨 렌더링 | 3DGS 스플래팅 |
|------|----------------|--------------|
| 기본 원시체 | 연속 필드 (MLP) | 불연속 가우시안 포인트 |
| 광선 방향 | 광선이 장면을 관통 | 가우시안을 화면에 투영 |
| 렌더링 순서 | 프론트-투-백 (광선 기준) | 깊이 정렬 후 스플랫 |
| 속도 | 느림 (광선당 많은 쿼리) | 빠름 (타일 기반 래스터화) |

## 계층적 샘플링 전략

볼륨 렌더링의 효율을 높이기 위해 NeRF는 두 단계 샘플링을 사용한다:

1. **Coarse 네트워크**: 균등 샘플링으로 거시 구조 파악
2. **Fine 네트워크**: Coarse의 가중치 분포를 PDF로 보고, 고밀도 영역에 집중 샘플링 (Importance Sampling)

이 계층적 방식이 광선당 필요한 샘플 수를 줄이면서도 정밀도를 유지한다.

## 깊이 추정과의 관계

미분 가능 볼륨 렌더링에서 예상 깊이(expected depth)를 추출할 수 있다:

$$\hat{D}(\mathbf{r}) = \sum_{i=1}^{N} T_i \left(1 - \exp(-\sigma_i \delta_i)\right) t_i$$

이 깊이를 [[depth-estimation-monocular]] 모델의 출력과 비교하거나 결합하면 멀티모달 3D 재구성이 가능하다.

## 실무 적용

- **역 렌더링(Inverse Rendering)**: 조명, 재질, 형상을 동시에 역추적
- **자율주행 시뮬레이션**: 실제 장면을 NeRF로 재구성 후 다양한 시나리오 시뮬레이션
- **의료 영상**: CT/MRI 볼륨 데이터를 신경 표현으로 압축, 다각도 렌더링
- **콘텐츠 제작**: 스마트폰 사진 → 미분 가능 렌더링 → 3D 에셋

## 관련 문서

- [[nerf-neural-radiance-fields|NeRF]] - 미분 가능 볼륨 렌더링의 대표 응용
- [[3d-gaussian-splatting]] - 대안 렌더링 원시체 방식
- [[instant-ngp]] - 볼륨 렌더링을 해시 인코딩으로 가속화
- [[depth-estimation-monocular]] - 깊이 정보와 렌더링의 결합

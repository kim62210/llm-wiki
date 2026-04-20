---
title: 합성곱 신경망 (CNN)
category: foundations
page_type: concept
tags: [CNN, convolutional-neural-network, computer-vision, image-classification, ResNet, EfficientNet]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

합성곱 신경망(Convolutional Neural Network, CNN)은 격자 구조 데이터(이미지, 시계열 등)에 특화된 신경망 아키텍처다. 지역적 패턴을 계층적으로 추출하는 합성곱 연산, 공간 불변성을 확보하는 풀링, 그리고 최종 분류/회귀를 수행하는 완전연결 계층으로 구성된다. 1998년 LeCun의 LeNet-5에서 출발하여 AlexNet(2012), VGGNet(2014), ResNet(2015), EfficientNet(2019)으로 이어지는 발전 경로는 딥러닝 역사 자체를 반영한다.

## 핵심 구성 요소

### 합성곱 계층 (Convolutional Layer)

입력에 학습 가능한 필터(커널)를 슬라이딩하여 특징 맵(feature map)을 생성한다. 두 가지 핵심 속성이 CNN의 효율성을 결정한다:

- **파라미터 공유(weight sharing)**: 동일 필터가 입력 전체에 걸쳐 재사용되므로, 완전연결 계층 대비 파라미터 수가 극적으로 감소한다
- **지역 연결성(local connectivity)**: 각 뉴런이 입력의 작은 영역(수용 영역, receptive field)만 참조하여 지역적 패턴을 포착한다

출력 크기는 입력 크기, 필터 크기, 스트라이드(stride), 패딩(padding)에 의해 결정된다:

```
출력 크기 = (입력 크기 - 필터 크기 + 2 * 패딩) / 스트라이드 + 1
```

### 풀링 계층 (Pooling Layer)

특징 맵의 공간 차원을 축소하여 연산량을 줄이고 위치 불변성을 확보한다. 최대 풀링(max pooling)이 가장 널리 사용되며, 평균 풀링(average pooling)은 최종 계층에서 글로벌 특징 집계에 활용된다.

### 활성화 함수

초기 CNN은 시그모이드/tanh를 사용했으나, AlexNet 이후 ReLU가 표준이 되었다. 현대 아키텍처에서는 GELU, SiLU/Swish 등도 채택된다.

## 아키텍처 진화

| 모델 | 연도 | 핵심 기여 | 깊이 |
|------|------|----------|------|
| LeNet-5 | 1998 | CNN 원형, 필기 숫자 인식 | 5층 |
| AlexNet | 2012 | GPU 학습, ReLU, Dropout | 8층 |
| VGGNet | 2014 | 3x3 필터 반복 구조 | 16-19층 |
| GoogLeNet | 2014 | Inception 모듈, 1x1 합성곱 | 22층 |
| ResNet | 2015 | 잔차 연결(skip connection) | 152층+ |
| EfficientNet | 2019 | 복합 스케일링(depth/width/resolution) | 가변 |

### 잔차 연결 (Residual Connection)

ResNet이 도입한 잔차 연결은 CNN을 넘어 현대 딥러닝 전반의 핵심 설계 패턴이 되었다. 입력 x를 출력에 직접 더하는 단축 경로(shortcut)가 기울기 소실 문제를 해결하여 수백 층 이상의 심층 네트워크 학습을 가능하게 했다:

```
출력 = F(x) + x    (항등 매핑 단축 경로)
```

이 패턴은 [[transformer-architecture]]의 각 서브 계층에도 동일하게 적용된다.

## CNN에서 Transformer로

CNN은 지역적 패턴 추출에 강점이 있지만, 장거리 의존성(long-range dependency) 포착에는 한계가 있다. 수용 영역(receptive field)이 깊이에 비례하여 선형적으로 증가하기 때문이다. Vision Transformer(ViT, 2020)는 이미지를 패치로 분할하고 [[self-attention-mechanism]]을 적용하여 이 한계를 극복했다. 그러나 CNN의 귀납적 편향(inductive bias)인 이동 불변성과 지역성은 여전히 유효하여, ConvNeXt(2022)처럼 CNN 설계 원칙을 현대화한 아키텍처도 경쟁력을 유지한다.

## 주요 응용

- **이미지 분류**: ImageNet 벤치마크 중심의 핵심 과제
- **객체 탐지**: YOLO, Faster R-CNN 등 CNN 백본 기반
- **시맨틱 분할**: U-Net, DeepLab 등 인코더-디코더 구조
- **자연어 처리**: 1D CNN을 활용한 텍스트 분류 (현재는 Transformer로 대체)
- **생성 모델**: [[diffusion-models]]의 U-Net 백본으로 현재도 핵심 역할 수행

## 대표 자료

- [LeCun et al., "Gradient-Based Learning Applied to Document Recognition" (1998)](http://yann.lecun.com/exdb/lenet/)
- [He et al., "Deep Residual Learning for Image Recognition" (arXiv:1512.03385)](https://arxiv.org/abs/1512.03385)
- [Tan & Le, "EfficientNet: Rethinking Model Scaling for CNNs" (arXiv:1905.11946)](https://arxiv.org/abs/1905.11946)

## 관련 문서
- [[capsule-networks]] -- 캡슐 네트워크 (Capsule Networks)

- [[transformer-architecture]] -- CNN의 한계를 극복한 어텐션 기반 아키텍처
- [[self-attention-mechanism]] -- CNN의 지역 수용 영역 대비 전역 참조
- [[diffusion-models]] -- U-Net(CNN 기반)을 백본으로 사용하는 생성 모델
- [[autoencoders-vae]] -- CNN을 인코더/디코더로 사용하는 생성 모델
- [[rnn-lstm-gru]] -- 시퀀스 데이터 처리의 대안적 접근

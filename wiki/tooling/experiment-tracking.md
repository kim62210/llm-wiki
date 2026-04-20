---
title: 실험 추적 도구 (W&B / MLflow / Neptune)
category: tooling
page_type: entity
project: Experiment Tracking
tags: [tooling, experiment-tracking, wandb, mlflow, neptune, mlops, monitoring]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 실험 추적 도구

## 개요

실험 추적(Experiment Tracking) 도구는 모델 학습 과정의 하이퍼파라미터, 메트릭, 아티팩트, 코드 버전을 체계적으로 기록하고 비교하는 MLOps 핵심 인프라다. 2026년 현재 Weights & Biases(W&B), MLflow, Neptune이 3대 플랫폼을 형성하고 있으나, 시장 구도가 급변하고 있다: W&B는 CoreWeave GPU 클라우드와 수직 통합되었고, Neptune은 OpenAI에 인수되어 2026년 3월 호스팅 서비스를 종료했다. 대규모 LLM 학습에서 실험 추적은 [[learning-rate-scheduling]], [[optimizer-selection]], [[mixed-precision-training]] 등 수백 개의 학습 변수를 관리하고 재현성을 확보하는 필수 계층이다.

## Weights & Biases (W&B)

### 개요

개발자 중심의 실험 추적 플랫폼으로, 직관적 UI/UX와 실시간 협업 기능이 핵심 강점이다. 연구팀과 ML 엔지니어 사이에서 가장 높은 채택률을 보인다.

### 핵심 기능

- **Experiments**: 학습 메트릭, 하이퍼파라미터, 시스템 리소스 실시간 로깅
- **Sweeps**: 하이퍼파라미터 탐색 자동화 (Bayesian, Grid, Random)
- **Artifacts**: 데이터셋, 모델 체크포인트 버전 관리
- **Tables**: 예측 결과의 인터랙티브 시각화 및 비교
- **Reports**: 실험 결과를 공유 가능한 보고서로 정리
- **Launch**: 학습 작업의 워크플로우 자동화

### 프레임워크 통합

| 프레임워크 | 통합 방식 | 자동 로깅 |
|-----------|----------|----------|
| PyTorch | `wandb.watch()` | 그래디언트, 파라미터 히스토그램 |
| HuggingFace Transformers | `WandbCallback` | 학습 손실, 평가 메트릭, 하이퍼파라미터 |
| NeMo | 네이티브 통합 | 분산 학습 메트릭 |
| DeepSpeed | `WandbLogger` | ZeRO 메모리, 처리량 |

### 요금

| 티어 | 가격 | 특징 |
|------|------|------|
| Free | 무료 | 100GB 스토리지, 개인 프로젝트 |
| Team | 유료 (사용자당) | 무제한 스토리지, 팀 협업 |
| Enterprise | 커스텀 | 온프레미스, SSO, 감사 로그 |

### 시장 동향

2025년 CoreWeave GPU 클라우드와의 수직 통합으로, GPU 자원 관리부터 실험 추적까지 일원화된 워크플로우를 제공하기 시작했다. 이는 [[gpu-cluster-scheduling]]과 실험 추적의 경계를 허무는 움직임이다.

## MLflow

### 개요

Databricks가 주도하는 오픈소스 ML 라이프사이클 관리 플랫폼이다. 실험 추적 외에도 모델 레지스트리, 배포, 평가까지 포괄하는 엔드투엔드 MLOps 솔루션이다. 벤더 종속 없이 자체 인프라에서 운영 가능한 것이 최대 장점이다.

### 핵심 구성요소

| 구성요소 | 역할 | 특징 |
|---------|------|------|
| **Tracking** | 실험 파라미터/메트릭 기록 | `mlflow.log_param()`, `mlflow.log_metric()` |
| **Model Registry** | 모델 버전 관리, 스테이징 | 모델 별칭, 승인 워크플로우 |
| **Projects** | 재현 가능한 학습 환경 정의 | conda, docker 환경 명세 |
| **Deployments** | 모델 서빙 | REST API, batch 추론 |
| **Evaluate** | 모델 평가 자동화 | LLM 전용 평가 메트릭 |

### 장점과 한계

**장점**:
- 완전 오픈소스, 자체 호스팅 가능 (벤더 종속 없음)
- 가장 포괄적인 ML 라이프사이클 관리
- Databricks와 긴밀한 통합 (Managed MLflow)
- 강력한 모델 레지스트리와 배포 파이프라인

**한계**:
- UI/UX가 W&B 대비 덜 직관적
- 실시간 협업 기능 제한적
- 대규모 실험(수만 회) 시 자체 호스팅 성능 관리 필요

### 배포 옵션

| 옵션 | 특징 | 적합 환경 |
|------|------|----------|
| 로컬 서버 | `mlflow server` 명령으로 즉시 시작 | 개인/소규모 팀 |
| 자체 호스팅 | PostgreSQL + S3 백엔드 | 엔터프라이즈 |
| Databricks Managed | 관리형 서비스 | Databricks 사용 조직 |

## Neptune (OpenAI 인수)

### 개요

엔터프라이즈급 ML 메타데이터 데이터베이스로, 극한의 확장성과 거버넌스에 초점을 맞춘 플랫폼이었다. 2025년 OpenAI가 인수했으며, 2026년 3월 4일 호스팅 서비스를 종료했다.

### 인수 전 핵심 특성

- **메타데이터 데이터베이스**: 실험을 구조화된 메타데이터로 관리, 복잡한 쿼리 지원
- **대규모 확장성**: 수백만 실험 동시 관리
- **세밀한 비교**: 하이퍼파라미터 조합별 상세 비교 분석
- **인프라 독립**: 모든 클라우드/온프레미스에서 동작
- **거버넌스**: 감사 추적, 접근 제어, 규정 준수 기능

### OpenAI 인수 후 상태

OpenAI는 Neptune의 기술을 내부 모델 행동 가시성 및 학습 추적에 활용할 계획이다. 호스팅 서비스 종료로 기존 Neptune 사용자는 W&B나 MLflow로 마이그레이션이 필요하다.

## 플랫폼 비교

### 포지셔닝

| 특성 | W&B | MLflow | Neptune (종료) |
|------|-----|--------|---------------|
| 철학 | 개발자 생산성 | 오픈소스 MLOps | 메타데이터 DB |
| 호스팅 | SaaS + 온프레미스 | 자체 호스팅 + Databricks | 종료 |
| 강점 | UI/UX, 협업, Sweeps | 모델 레지스트리, 배포 | 확장성, 쿼리 |
| 약점 | 벤더 종속 | UI 직관성 | 서비스 종료 |
| 가격 | 무료 + 유료 티어 | 무료 (오픈소스) | - |
| 2026 위치 | 시장 선도 | 기업 표준 | OpenAI 내부 |

### LLM 학습에서의 추적 항목

실험 추적 도구로 관리해야 하는 LLM 학습 변수:

| 카테고리 | 추적 항목 | 관련 위키 |
|---------|----------|----------|
| 병렬화 | TP/PP/DP 구성, GPU 수 | [[tensor-pipeline-parallelism]], [[data-parallelism-fsdp]] |
| 정밀도 | FP16/BF16/FP8, 손실 스케일링 | [[mixed-precision-training]] |
| 옵티마이저 | 종류, 학습률, 가중치 감쇠 | [[optimizer-selection]] |
| 스케줄 | warmup 스텝, decay 형태 | [[learning-rate-scheduling]] |
| 배치 | 마이크로배치, 누적 스텝 | [[gradient-accumulation-checkpointing]] |
| 체크포인트 | 빈도, 저장 위치, 샤딩 | [[model-checkpointing-sharding]] |
| 메모리 | ZeRO Stage, 오프로딩 | [[deepspeed-zero]] |
| 인프라 | 클러스터, 스케줄러, GPU 종류 | [[gpu-cluster-scheduling]] |

## 실전 도입 가이드

### 선택 기준

| 상황 | 권장 도구 | 이유 |
|------|----------|------|
| 연구팀, 빠른 반복 | W&B | UI/UX, 실시간 협업 |
| 엔터프라이즈, 벤더 독립 | MLflow (자체 호스팅) | 오픈소스, 벤더 종속 없음 |
| Databricks 사용 조직 | MLflow (Managed) | 네이티브 통합 |
| CoreWeave GPU 사용 | W&B | GPU 클라우드 통합 |
| 기존 Neptune 사용자 | W&B 또는 MLflow | Neptune 서비스 종료 대응 |

### 프레임워크별 통합 난이도

[[training-frameworks]]의 모든 주요 프레임워크가 W&B와 MLflow를 1등 시민으로 지원한다. PyTorch, HuggingFace, NeMo, DeepSpeed 모두 콜백 또는 로거 하나로 통합 가능하며, 분산 학습 환경에서는 rank 0 프로세스만 로깅하는 패턴이 표준이다.

## 관련 문서

- [[training-frameworks]] -- 학습 프레임워크 통합
- [[optimizer-selection]] -- 추적 대상 하이퍼파라미터
- [[learning-rate-scheduling]] -- 학습률 스케줄 추적
- [[model-checkpointing-sharding]] -- 체크포인트 아티팩트 관리
- [[gpu-cluster-scheduling]] -- 인프라 메트릭 통합 모니터링
- [[lora-qlora-finetuning]] -- 파인튜닝 실험 추적

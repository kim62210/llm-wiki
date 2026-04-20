---
title: DVC (Data Version Control)
category: tooling
page_type: entity
project: DVC
tags: [dvc, data-versioning, git, ml-pipeline, reproducibility]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-17
updated: 2026-04-17
---

# DVC (Data Version Control)

Git 기반 데이터/모델 버전 관리 및 ML 파이프라인 추적 도구. Git이 코드를 버전 관리하듯, DVC는 대용량 데이터 파일과 모델 가중치를 S3/GCS/Azure 등 원격 스토리지에 저장하면서 Git에는 메타데이터(.dvc 파일)만 커밋한다.

```mermaid
flowchart LR
    Git[Git 레포] -->|코드 + .dvc 파일| Code[소스 코드]
    DVC[DVC 원격 스토리지] -->|대용량 파일| Data[데이터/모델]
    Code -.->|dvc pull| Data
    Data -.->|dvc push| DVC
```

## 핵심 기능

- **데이터 버전 관리**: Git 커밋과 데이터 버전 1:1 매핑
- **파이프라인 DAG**: `dvc.yaml`로 학습 파이프라인 단계 정의, 변경 감지 시 필요한 단계만 재실행
- **실험 추적**: `dvc exp` 명령으로 하이퍼파라미터 실험 관리

## 관련 문서

- [[mlflow]] -- MLflow (보완적 사용)
- [[experiment-tracking]] -- 실험 추적
- [[wandb]] -- Weights & Biases

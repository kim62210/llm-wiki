---
title: DVC (Data Version Control)
category: tooling
page_type: entity
project: DVC
tags: [dvc, data-versioning, git, ml-pipeline, reproducibility]
sources: [raw/2026-04-16-topic-queue-500.md, https://doc.dvc.org]
created: 2026-04-17
updated: 2026-05-06
---

# DVC (Data Version Control)

Git 기반 데이터/모델 버전 관리 및 ML 파이프라인 추적 도구. Git이 코드를 버전 관리하듯, DVC는 대용량 데이터 파일과 모델 가중치를 S3/GCS/Azure 등 원격 스토리지에 저장하면서 Git에는 메타데이터(.dvc 파일, dvc.yaml, dvc.lock)만 커밋한다. Iterative.ai가 주도해서 만든 오픈소스이며, 동일 회사가 호스팅하는 DVC Studio UI와 결합해 풀 스택 ML 협업 환경을 구성할 수 있다.

```mermaid
flowchart LR
    Git[Git 레포] -->|코드 + .dvc 파일| Code[소스 코드]
    DVC[DVC 원격 스토리지] -->|대용량 파일| Data[데이터/모델]
    Code -.->|dvc pull| Data
    Data -.->|dvc push| DVC
```

## 핵심 가치

- **Git 친화적**: 기존 git workflow(branch, commit, PR)에 자연스럽게 결합
- **재현성**: 코드 + 데이터 + 환경 + 하이퍼파라미터를 하나의 커밋으로 응고
- **저장소 비용 분리**: 대용량 바이너리는 객체 스토리지로 분리, Git 레포는 가볍게 유지
- **파이프라인 + 실험**: 데이터 버전 관리만이 아니라 학습 파이프라인과 실험 관리를 한 도구에서 처리

## 프로젝트 구조: 핵심 파일

| 파일 | 역할 |
|------|------|
| `*.dvc` | 추적되는 개별 파일/디렉터리의 메타데이터(해시, 크기, 경로). Git에 커밋한다. |
| `dvc.yaml` | 파이프라인 정의. stages, deps, outs, params, metrics, plots 선언 |
| `dvc.lock` | 마지막 실행 결과(해시, 명령) 스냅샷. 자동 생성 |
| `.dvcignore` | DVC 추적에서 제외할 패턴 (Git의 .gitignore와 유사) |
| `.dvc/config` | 원격 스토리지/캐시/인증 설정 |

## Remote Storage 옵션

공식 문서가 명시하는 백엔드는 다음과 같다:

- **클라우드 객체 스토리지**: Amazon S3, Google Cloud Storage, Azure Blob Storage
- **개인용 / 협업**: Google Drive, WebDAV
- **온프레미스 / SSH**: SSH/SFTP, HDFS, HTTP, 로컬 디렉터리

`dvc remote add -d <name> <url>` 명령으로 등록 후 `dvc push` / `dvc pull`로 동기화한다. 한 프로젝트에 여러 remote를 지정할 수 있어 핫 데이터(S3) + 콜드 백업(Glacier) 식의 다층 구성도 가능.

## Pipeline DAG: dvc.yaml

DVC의 진가는 단순 파일 버전 관리가 아니라 **재현 가능한 ML 파이프라인 DAG**에 있다.

```yaml
stages:
  prepare:
    cmd: python src/prepare.py data/raw
    deps:
      - src/prepare.py
      - data/raw
    params:
      - prepare.split
    outs:
      - data/prepared
  featurize:
    cmd: python src/featurize.py data/prepared data/features
    deps:
      - src/featurize.py
      - data/prepared
    outs:
      - data/features
  train:
    cmd: python src/train.py data/features model.pkl
    deps:
      - src/train.py
      - data/features
    params:
      - train.learning_rate
      - train.epochs
    outs:
      - model.pkl
    metrics:
      - metrics.json:
          cache: false
    plots:
      - plots.csv:
          cache: false
```

- **stages**: 각 단계는 shell 명령(cmd)을 감싸며 deps/outs/params를 통해 입출력을 명시
- **deps**: 입력 파일/디렉터리. 해시값 비교로 변경 감지 → 변경 없으면 stage skip(증분 빌드)
- **outs**: 단계 결과물. DVC 캐시에 저장되어 자동 추적
- **params**: 구조화된 하이퍼파라미터(`params.yaml`). 정밀한 의존성 추적이 가능해 학습률만 바꿔도 train stage만 재실행
- **metrics / plots**: 작은 평가 결과/시각화는 Git에 직접 커밋(`cache: false`)
- 출력 → 다음 stage의 입력으로 연결되어 DAG가 자동 형성

`dvc repro` 한 번으로 변경된 단계만 골라 재실행하고, `dvc dag`로 의존성 그래프를 시각화한다.

## DVC Experiments (`dvc exp`)

기존 ML 실험 도구와 차별점은 **branch-less experiments**다. 실험을 일반 Git 커밋으로 만들지 않고 `.git/refs/exps`에 별도 ref로 저장해 메인 히스토리를 깔끔하게 유지한다.

```bash
dvc exp run --set-param train.learning_rate=0.01
dvc exp run --queue --set-param train.learning_rate=0.001
dvc exp run --queue --set-param train.epochs=50
dvc queue start --jobs 4   # 큐에 쌓은 실험 병렬 실행
dvc exp show               # 비교 테이블
dvc exp diff <exp1> <exp2> # 두 실험 차이
```

- **자동 네이밍**: `puffy-daks` 같은 사람이 기억하기 좋은 이름 자동 생성, `--name`으로 지정도 가능
- **큐 실행**: `--queue`로 여러 실험을 등록 후 `dvc queue start`로 병렬 처리
- **공유**: 기본은 로컬 저장이지만 push/pull로 다른 협업자에게 공유 가능
- **VS Code 확장**: DVC Extension에서 GUI로 실험 실행/비교

## DVCLive: ML 코드 내 실시간 로깅

학습 코드 안에서 metrics/plots/모델을 로깅할 때 사용하는 가벼운 라이브러리.

```python
from dvclive import Live

with Live() as live:
    for epoch in range(num_epochs):
        ...
        live.log_metric("loss", loss.item())
        live.log_metric("accuracy", acc)
        live.next_step()
    live.log_artifact("model.pt", type="model")
```

PyTorch Lightning, Hugging Face Trainer, Keras, Optuna, scikit-learn 등 주요 프레임워크와 콜백/통합이 제공된다. 결과는 `dvclive/` 디렉터리에 들어가며 `dvc exp show`/Studio에서 자동으로 인식된다.

## DVC Studio (Iterative.ai 호스팅 UI)

웹에서 GitHub/GitLab/Bitbucket 레포를 연결해:

- 실험 비교 테이블 / 인터랙티브 plot
- 모델 레지스트리(Git tag 기반 버전, 단계 승격: Development → Production)
- 협업자 코멘트, 메트릭 히스토리 시각화

CLI(개인) → Studio(팀) 식의 점진 도입이 가능.

## 다른 도구와의 비교

| 비교 대상 | 차이점 / 보완 관계 |
|----------|------------------|
| **Git LFS** | LFS는 단순 대용량 파일 추적. DVC는 파이프라인/실험까지 다룸. LFS 대비 다양한 백엔드 지원 |
| **[[mlflow]]** | MLflow는 실험·모델 레지스트리에 강점, DVC는 데이터·파이프라인에 강점. **보완 사용** 패턴 흔함 |
| **[[wandb]]** | W&B는 SaaS 기반 시각화·실험 추적. DVCLive 결과를 W&B로 동시 push 가능 |
| **Pachyderm** | Pachyderm은 컨테이너 기반 데이터 파이프라인 + 버전 관리 통합. DVC는 가벼운 파일 기반 |

## 한계와 주의점

- **거대 파일 push 속도**: 객체 스토리지 multipart upload 속도에 직접 의존. 수십~수백 GB 단위 모델은 `dvc push`만으로 시간이 오래 걸림
- **Git 동기화 복잡도**: `.dvc` 파일과 실제 캐시가 어긋나면 `dvc checkout` / `dvc fetch` 같은 별도 명령으로 정합성 회복 필요
- **권한 모델**: 원격 스토리지 ACL을 별도로 관리해야 하며 DVC 자체 권한 시스템은 없음
- **CI/CD 통합 비용**: `dvc pull`이 필요한 CI는 빌드 시간이 길어질 수 있어 캐시 전략(예: GitHub Actions cache)을 함께 설계
- **메타데이터 스케일**: 수십만 개 작은 파일을 단일 디렉터리로 추적하면 .dvc 메타데이터가 비대해짐. 디렉터리 단위 추적이 권장됨

## 관련 문서

- [[mlflow]] -- MLflow (보완적 사용)
- [[experiment-tracking]] -- 실험 추적
- [[wandb]] -- Weights & Biases
- [[ai-data-pipeline-automation]] -- 데이터 파이프라인 자동화
- [[feature-engineering]] -- 특성 공학
- [[ml-reproducibility]] -- ML 재현성

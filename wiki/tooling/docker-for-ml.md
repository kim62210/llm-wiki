---
title: Docker for ML (ML 워크로드 컨테이너화)
category: tooling
page_type: entity
tags: [tooling, entity, docker, container, gpu, nvidia-container-toolkit, reproducibility, ml-infrastructure]
sources: [raw/2026-04-14-wiki-expand-scan-2.md]
created: 2026-04-14
updated: 2026-04-14
---

# Docker for ML (ML 워크로드 컨테이너화)

## 개요

Docker는 ML 워크로드의 재현 가능한 환경 구성과 배포를 위한 사실상 표준 컨테이너 플랫폼이다. "내 로컬에서는 되는데"라는 문제를 해결하기 위해 시작된 컨테이너 기술이, GPU 드라이버 버전 불일치, CUDA 호환성, 파이썬 패키지 충돌 등 ML 특유의 환경 문제까지 포괄하게 되었다. NVIDIA Container Toolkit의 등장으로 GPU 패스스루가 네이티브에 근접한 성능을 제공하면서, ML 프로덕션 파이프라인에서 Docker 없는 워크플로우는 사실상 상상하기 어렵다.

## 왜 ML에서 Docker인가

### 재현성 문제

ML 학습 환경은 일반 소프트웨어보다 의존성 지옥이 심하다:

| 계층 | 의존성 예시 | 호환성 문제 |
|------|-----------|-----------|
| 하드웨어 | GPU 세대 (Ampere/Hopper/Blackwell) | 연산 능력(compute capability) 불일치 |
| 드라이버 | NVIDIA Driver 535/545/550 | CUDA 버전과 교차 호환 |
| 런타임 | CUDA 11.8 / 12.x | PyTorch/TensorFlow 빌드 종속 |
| 프레임워크 | PyTorch 2.x, TensorFlow 2.x | cuDNN, NCCL 버전 민감 |
| 라이브러리 | HuggingFace, DeepSpeed, vLLM | 상호 버전 제약 |

Dockerfile로 이 전체 스택을 고정하면, 6개월 후에도 동일한 학습 결과를 재현할 수 있다. 논문의 실험 재현, 규제 산업의 감사 추적(audit trail), 팀 간 환경 공유 모두 이 재현성에 의존한다.

### 이식성

한 번 빌드한 이미지가 로컬 워크스테이션, 온프레미스 클러스터, AWS/GCP/Azure 클라우드 어디서든 동일하게 실행된다. 멀티클라우드 전략이나 하이브리드 환경에서 이식성은 인프라 종속(vendor lock-in)을 줄이는 핵심 축이다.

## NVIDIA Container Toolkit

GPU를 Docker 컨테이너에서 사용하려면 NVIDIA Container Toolkit이 필수다. 이 툴킷은 컨테이너 런타임을 확장하여 호스트의 GPU를 컨테이너 내부에 노출시킨다.

### 주요 컴포넌트

- **nvidia-container-runtime**: Docker/containerd의 OCI 런타임을 래핑하여 GPU 디바이스를 자동 마운트한다
- **nvidia-container-cli**: 컨테이너에 GPU 디바이스, 드라이버 라이브러리, CUDA 런타임을 주입하는 저수준 CLI
- **nvidia-container-toolkit (CDI Hooks)**: Container Device Interface(CDI) 스펙을 통해 GPU를 표준화된 방식으로 노출한다. CDI는 OCI 표준의 일부로, Docker/Podman/containerd 등 여러 런타임에서 일관된 디바이스 접근을 제공한다
- **libnvidia-container**: GPU 격리와 디바이스 접근을 담당하는 핵심 라이브러리

### GPU 컨테이너 실행

```bash
# 단일 GPU
docker run --gpus 1 nvcr.io/nvidia/pytorch:24.03-py3 python train.py

# 전체 GPU
docker run --gpus all nvcr.io/nvidia/pytorch:24.03-py3 python train.py

# 특정 GPU 지정 (GPU 0, 2번)
docker run --gpus '"device=0,2"' nvcr.io/nvidia/pytorch:24.03-py3 python train.py
```

`--gpus` 플래그는 Docker 19.03부터 네이티브로 지원된다. 이전에는 `nvidia-docker2` 래퍼가 필요했으나, 현재는 NVIDIA Container Toolkit만 설치하면 Docker CLI에서 직접 GPU를 할당할 수 있다.

### 성능 오버헤드

컨테이너화된 GPU 워크로드의 성능 오버헤드는 일반적으로 1-3% 이내다. NVIDIA Container Toolkit은 GPU를 PCI 패스스루 방식으로 직접 노출하므로, 가상화 계층의 에뮬레이션 비용이 거의 없다. NVLink/NVSwitch를 통한 다중 GPU 통신도 네이티브 수준으로 동작한다.

## ML Dockerfile 패턴

### NVIDIA NGC 베이스 이미지

NVIDIA NGC(GPU Cloud)에서 제공하는 공식 베이스 이미지가 가장 권장된다. CUDA, cuDNN, NCCL이 사전 통합되어 있어 드라이버 호환성 문제를 최소화한다.

```dockerfile
FROM nvcr.io/nvidia/pytorch:24.03-py3

# 학습 코드와 의존성
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src/ /app/src/
WORKDIR /app
CMD ["torchrun", "--nproc_per_node=8", "src/train.py"]
```

### 멀티스테이지 빌드

학습 환경과 배포 환경을 분리하면 이미지 크기를 크게 줄일 수 있다:

```dockerfile
# 학습 스테이지
FROM nvcr.io/nvidia/pytorch:24.03-py3 AS trainer
COPY . /workspace
RUN python train.py --output /workspace/model/

# 서빙 스테이지
FROM nvcr.io/nvidia/tritonserver:24.03-py3
COPY --from=trainer /workspace/model/ /models/
```

### 볼륨 마운트 전략

대규모 데이터셋과 체크포인트는 이미지에 포함하지 않고 볼륨으로 마운트한다:

```bash
docker run --gpus all \
  -v /data/datasets:/data:ro \         # 데이터셋 (읽기 전용)
  -v /data/checkpoints:/checkpoints \   # 체크포인트 (읽기/쓰기)
  -v /data/logs:/logs \                 # 로그
  --shm-size=64g \                      # 공유 메모리 (DataLoader workers)
  training-image:latest
```

`--shm-size`는 PyTorch DataLoader의 멀티프로세스 데이터 로딩에 필수적이다. 기본값(64MB)이면 `num_workers > 0`일 때 "bus error"가 발생한다.

## Docker Compose로 분산 학습

단일 노드 내 다중 GPU 학습은 Docker Compose로 구성할 수 있다:

```yaml
services:
  trainer:
    image: my-training:latest
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    shm_size: '64gb'
    volumes:
      - ./data:/data
      - ./checkpoints:/checkpoints
```

다중 노드 분산 학습은 Docker 단독으로는 한계가 있으며, Kubernetes나 Slurm과의 통합이 필요하다. 이 부분은 [[gpu-cluster-scheduling]]에서 다룬다.

## 컨테이너 레지스트리와 CI/CD

### 이미지 관리

ML 이미지는 일반 애플리케이션보다 크기가 크다(5-20GB). 레이어 캐싱 전략이 빌드 시간과 저장 비용에 직접 영향을 미친다:

- 변경 빈도가 낮은 의존성(CUDA, 프레임워크)을 상위 레이어에 배치
- 학습 코드는 하위 레이어에 배치하여 코드 변경 시 캐시 무효화 범위를 최소화
- `.dockerignore`로 데이터셋, 체크포인트, `.git` 등을 제외

### 재현성 체크리스트

- Dockerfile에 모든 의존성 버전을 pin (`==` 또는 `~=`)
- 베이스 이미지에 태그(날짜 또는 버전) 명시 (`latest` 지양)
- `pip freeze` 또는 `conda env export` 결과를 락파일로 커밋
- 빌드 아규먼트로 GPU 아키텍처 타겟 지정 (예: `TORCH_CUDA_ARCH_LIST="8.0;9.0"`)

## 한계와 보완

Docker의 공유 커널 모델은 보안 격리 수준이 VM보다 낮다. AI 에이전트가 생성한 코드를 실행하는 샌드박스 환경에서는 [[microvm-agent-sandboxes|Firecracker/microVM]]이 더 강한 격리를 제공한다. 또한 GPU MIG(Multi-Instance GPU) 파티셔닝은 Docker 레벨이 아닌 드라이버/디바이스 레벨에서 구성해야 하며, Kubernetes의 DRA(Dynamic Resource Allocation)와 결합할 때 가장 유연하다.

## 관련 문서

- [[gpu-cluster-scheduling]] -- 다중 노드 GPU 스케줄링 (Slurm/Kubernetes)
- [[microvm-agent-sandboxes]] -- 에이전트 코드 실행을 위한 microVM 샌드박스

## 출처

- NVIDIA Container Toolkit Documentation - https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html
- Kubernetes GPU Scheduling - https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
- NVIDIA NGC Catalog - https://catalog.ngc.nvidia.com/

---
title: Kubernetes for ML (ML 오케스트레이션)
category: tooling
page_type: entity
tags: [tooling, entity, kubernetes, kubeflow, gpu-scheduling, distributed-training, ml-infrastructure]
sources: [raw/2026-04-14-wiki-expand-scan-2.md]
created: 2026-04-14
updated: 2026-04-14
---

# Kubernetes for ML (ML 오케스트레이션)

## 개요

Kubernetes(K8s)는 컨테이너 오케스트레이션의 사실상 표준이며, ML 워크로드 영역으로 빠르게 확장되고 있다. 원래 웹 서비스의 마이크로서비스 배포를 위해 설계되었으나, GPU Device Plugin, Kubeflow Training Operator, Volcano 같은 확장을 통해 분산 학습, 하이퍼파라미터 튜닝, 모델 서빙까지 포괄하는 ML 플랫폼으로 진화했다. 2026년 현재 NVIDIA Slinky를 통한 Slurm 통합, DRA(Dynamic Resource Allocation)를 통한 토폴로지 인식 GPU 할당이 프로덕션에 진입하면서 HPC와 클라우드 네이티브의 경계가 사라지고 있다.

## GPU 스케줄링

### Device Plugin 아키텍처

Kubernetes는 GPU를 확장 리소스(extended resource)로 취급한다. 각 GPU 벤더가 제공하는 Device Plugin이 노드의 GPU를 Kubernetes API에 등록하면, 스케줄러가 Pod의 리소스 요청에 따라 GPU를 할당한다.

**GPU 리소스 요청 방식** (Kubernetes 공식 문서 기준):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: training-pod
spec:
  containers:
  - name: trainer
    image: nvcr.io/nvidia/pytorch:24.03-py3
    resources:
      limits:
        nvidia.com/gpu: 4  # 4개 GPU 요청
```

GPU 리소스는 `limits` 섹션에만 명시한다. `limits`를 지정하면 `requests`가 자동으로 동일 값으로 설정되며, 둘을 모두 지정할 경우 반드시 같은 값이어야 한다. GPU는 정수 단위로만 요청할 수 있고, 컨테이너 간 공유(fraction)는 기본적으로 지원하지 않는다.

### NVIDIA GPU Operator

GPU 노드 설정을 자동화하는 Kubernetes Operator다. GPU 드라이버, CUDA 런타임, Device Plugin, DCGM(Data Center GPU Manager)을 DaemonSet으로 관리하여, 새 노드가 클러스터에 추가되면 GPU 스택이 자동으로 프로비저닝된다. 운영팀이 각 노드에 수동으로 드라이버를 설치할 필요가 없어진다.

### Node Feature Discovery (NFD)

각 노드의 GPU 하드웨어를 자동 감지하여 라벨을 부여한다. GPU 모델, 메모리 크기, 연산 능력 등이 라벨로 노출되어 Pod의 `nodeSelector` 또는 `nodeAffinity`로 특정 GPU 유형을 선택할 수 있다:

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: "gpu.nvidia.com/product"
            operator: In
            values: ["A100-SXM4-80GB", "H100-SXM5-80GB"]
```

### DRA (Dynamic Resource Allocation)

Kubernetes v1.26부터 도입된 DRA는 Device Plugin의 한계를 넘어서는 차세대 GPU 할당 메커니즘이다. Device Plugin이 단순 수량 기반 할당만 지원하는 반면, DRA는 GPU 토폴로지(NVLink 연결, PCIe 스위치 그룹 등)를 인식한 할당이 가능하다. 분산 학습에서 통신 병목을 최소화하려면 물리적으로 가까운 GPU를 묶어 할당해야 하는데, DRA가 이를 해결한다.

## Kubeflow Training Operator

Kubernetes 위에서 분산 ML 학습을 선언적으로 관리하는 오퍼레이터다. 각 프레임워크별 CRD(Custom Resource Definition)를 제공한다:

| 프레임워크 | CRD | 용도 |
|-----------|-----|------|
| PyTorch | PyTorchJob | DDP, FSDP 분산 학습 |
| TensorFlow | TFJob | Parameter Server, MirroredStrategy |
| XGBoost | XGBoostJob | 분산 그래디언트 부스팅 |
| MPI | MPIJob | Horovod, DeepSpeed 기반 학습 |
| JAX | JAXJob | TPU/GPU 분산 학습 |
| PaddlePaddle | PaddleJob | PaddlePaddle 분산 학습 |

### PyTorchJob 예시

```yaml
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: llm-finetune
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      template:
        spec:
          containers:
          - name: pytorch
            image: my-training:latest
            resources:
              limits:
                nvidia.com/gpu: 8
    Worker:
      replicas: 3
      template:
        spec:
          containers:
          - name: pytorch
            image: my-training:latest
            resources:
              limits:
                nvidia.com/gpu: 8
```

이 정의 하나로 Master 1개 + Worker 3개 = 총 32 GPU 분산 학습 Job이 생성된다. Training Operator가 `MASTER_ADDR`, `MASTER_PORT`, `WORLD_SIZE`, `RANK` 같은 환경 변수를 자동 주입하므로 학습 코드에서 분산 설정을 하드코딩할 필요가 없다.

### 생태계 통합

Training Operator는 HuggingFace Transformers, DeepSpeed, Megatron-LM 등의 분산 학습 라이브러리와 통합된다. LLM 미세조정(LoRA, QLoRA)부터 대규모 사전학습까지 선언적 Kubernetes 리소스로 관리할 수 있다.

## 배치 스케줄링

### Volcano

HPC 스타일의 배치 스케줄링을 Kubernetes에 도입하는 프로젝트다. 기본 Kubernetes 스케줄러는 Pod를 개별적으로 스케줄링하지만, 분산 학습에서는 모든 Worker가 동시에 시작해야 한다(gang scheduling). Volcano는 이 문제를 해결한다:

- **Gang Scheduling**: Job의 모든 Pod가 리소스를 확보할 때까지 대기, 부분 할당으로 인한 데드락 방지
- **Queue 관리**: 팀/프로젝트별 GPU 할당량(quota)과 우선순위 설정
- **Fair-share**: 큐 간 GPU 자원의 공정 분배
- **Preemption**: 우선순위 높은 작업이 낮은 작업을 선점

### Kueue

Kubernetes SIG Scheduling에서 관리하는 공식 작업 큐 관리자다. Volcano보다 Kubernetes 네이티브한 접근을 취하며, ResourceFlavor를 통해 이기종 GPU 클러스터(A100/H100 혼합)에서 유연한 리소스 할당을 지원한다.

## 탄력적 학습 (Elastic Training)

Kubernetes의 자동 스케일링은 ML 학습의 탄력성과 결합된다:

### torchelastic 통합

PyTorch의 `torchelastic`(torch.distributed.run)은 학습 중 Worker 수가 변해도 학습을 계속할 수 있게 한다. Kubernetes에서 노드 장애로 Pod가 재생성되거나, 자원이 추가로 확보되어 Worker가 늘어나는 상황을 처리한다.

### 장애 복구 패턴

| 전략 | 설명 | 적합 환경 |
|------|------|----------|
| Pod 자동 재시작 | 장애 Pod를 새 노드에 재생성 | 단기 학습 |
| 체크포인트 재개 | 마지막 체크포인트에서 학습 재개 | 장시간 학습 |
| Elastic scaling | Worker 수 유동적 조정 | 클라우드 spot 인스턴스 |
| 핫 스페어 | 대기 노드에서 즉시 교체 | 고가용성 프로덕션 |

## 모니터링과 관측성

### DCGM (Data Center GPU Manager)

NVIDIA DCGM이 GPU 메트릭(온도, 전력, 메모리, 활용률, ECC 에러)을 수집하고, Prometheus exporter를 통해 Kubernetes 모니터링 스택에 통합된다.

### 핵심 모니터링 지표

- **GPU 활용률**: 학습 효율의 직접 지표. 50% 미만이면 데이터 로딩 또는 통신 병목 의심
- **GPU 메모리 사용량**: OOM 예방과 배치 크기 최적화
- **노드 간 네트워크 대역폭**: 분산 학습의 통신 오버헤드
- **작업 대기 시간**: 스케줄링 효율과 클러스터 활용률

## Slurm 통합: Slinky

NVIDIA Slinky는 Slurm과 Kubernetes를 통합하는 오픈소스 프로젝트로, 두 진영의 장점을 결합한다. slurm-bridge(Kubernetes 워크로드에 Slurm 스케줄링 적용)와 slurm-operator(Kubernetes 위에 전체 Slurm 클러스터 운영) 두 모드를 지원한다. NVIDIA 내부에서 8,000+ GPU 클러스터에서 프로덕션 운영 중이며, 컨테이너화되지 않은 Slurm과 동일한 GPU 통신 성능을 달성했다. 자세한 비교는 [[gpu-cluster-scheduling]]을 참조한다.

## 실전 도입 가이드

| 환경 | 권장 구성 | 이유 |
|------|----------|------|
| 소규모 팀 (GPU < 16) | K8s + Training Operator | 운영 복잡도 최소 |
| 중규모 (GPU 16-128) | K8s + Volcano + DCGM | Gang scheduling 필요 |
| 대규모 (GPU 128+) | K8s + Slinky 또는 순수 Slurm | 토폴로지 인식, 장애 복구 고도화 |
| 학습 + 서빙 혼합 | K8s (서빙) + Slurm (학습) | 각 영역 최적화 |

## 관련 문서

- [[gpu-cluster-scheduling]] -- Slurm vs Kubernetes GPU 스케줄링 비교
- [[distributed-communication]] -- NCCL/Gloo 분산 통신 백엔드

## 출처

- Kubernetes GPU Scheduling - https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
- Kubeflow Training Operator Overview - https://www.kubeflow.org/docs/components/training/overview/
- NVIDIA GPU Operator Documentation - https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html

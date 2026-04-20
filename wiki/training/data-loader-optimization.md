---
title: 데이터 로더 최적화 (Data Loader Optimization)
category: training
page_type: concept
tags: [data-loader, io-bottleneck, webdataset, prefetching]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 데이터 로더 최적화 (Data Loader Optimization)

## 개념 요약

대규모 LLM 학습에서 데이터 로딩이 GPU 학습 속도의 병목이 되는 경우가 빈번하다. GPU가 다음 배치를 기다리며 유휴 상태(idle)가 되면 MFU(Model Flops Utilization)가 급감한다. 데이터 로더 최적화는 스토리지 I/O부터 CPU 전처리, GPU 전송까지 전체 파이프라인을 조율하는 작업이다.

## GPU 학습 I/O 병목 진단

병목 여부를 판단하는 방법:

1. GPU 활용률 모니터링: `nvidia-smi dmon`으로 SM 활용률(sm%) 확인
   - 100% 유지 -> 병목 없음
   - 주기적으로 0%로 떨어짐 -> I/O 또는 CPU 병목
2. DataLoader 프로파일링: PyTorch Profiler로 `data_loading` 시간 측정
3. 디스크 I/O 측정: `iostat -x 1` 로 디스크 read 대역폭 확인

## PyTorch DataLoader 튜닝

```python
from torch.utils.data import DataLoader

dataloader = DataLoader(
    dataset,
    batch_size=32,
    num_workers=8,           # CPU 코어 수의 절반 ~ 전체가 경험적 시작점
    pin_memory=True,         # CPU -> GPU 전송 시 페이지 고정 메모리 사용 (CUDA DMA 가속)
    persistent_workers=True, # 에폭 간 워커 프로세스 재사용 (초기화 오버헤드 제거)
    prefetch_factor=2,       # 워커당 미리 준비할 배치 수 (num_workers > 0 필요)
)
```

### 파라미터별 효과

| 파라미터 | 기본값 | 권장 설정 | 효과 |
|----------|--------|-----------|------|
| `num_workers` | 0 (메인 프로세스) | 4-16 | CPU 병렬 로딩 |
| `pin_memory` | False | True (GPU 학습 시) | Host->Device 전송 속도 향상 |
| `persistent_workers` | False | True | 에폭 간 워커 재사용 |
| `prefetch_factor` | 2 | 2-4 | 선행 배치 준비 |

`num_workers`를 무한정 늘리면 메모리 경쟁과 컨텍스트 스위칭으로 오히려 느려진다.

## WebDataset / Mosaic 스트리밍

수백 GB~수 TB 규모 데이터셋은 로컬 파일시스템에 저장하기 어렵다. 스트리밍 데이터 포맷을 활용한다.

### WebDataset

- 데이터를 `.tar` 파일(shard)로 패키징해 HTTP/S3/GCS에서 스트리밍
- shard 단위로 셔플링 -> 순수 무작위 접근 없이도 어느 정도 셔플 효과
- `webdataset` 라이브러리로 PyTorch와 통합

```python
import webdataset as wds

dataset = (
    wds.WebDataset("s3://bucket/shards/shard-{000000..001234}.tar")
    .shuffle(1000)
    .decode("rgb")
    .to_tuple("jpg", "cls")
)
```

### MosaicML Streaming

- 무작위 접근(random access)과 스트리밍을 동시 지원하는 `.mds` 포맷
- 이미 내려받은 shard를 캐시해 재학습 효율 향상
- 멀티노드에서 각 노드가 고유한 shard를 담당해 중복 다운로드 방지

## Memory-Mapped 파일

대형 데이터셋을 numpy `memmap` 또는 HuggingFace `datasets`의 Arrow 포맷으로 저장하면, 운영체제가 필요한 페이지만 메모리로 로드한다.

```python
import numpy as np

# 토큰화된 데이터를 미리 memmap으로 저장
data = np.memmap("tokens.bin", dtype="uint16", mode="r", shape=(total_tokens,))
```

- 전체 데이터를 RAM에 올리지 않아도 임의 접근 가능
- 운영체제 페이지 캐시(page cache) 활용 -> 반복 접근 빠름
- 토크나이징을 학습 전 오프라인으로 완료한 경우에 특히 효과적

## 멀티노드 데이터 분산

멀티노드 학습에서 각 노드가 겹치지 않는 데이터를 처리해야 한다:

- **Shard 할당**: 각 노드/랭크에 고유 shard 집합 지정
- **글로벌 셔플**: 에폭마다 shard 순서를 전역 시드로 셔플
- **스트라글러(straggler) 방지**: 가장 느린 노드가 데이터 로딩으로 인한 병목이 되지 않도록 버퍼링

## 관련 문서

- [[pretraining-pipeline-e2e]] - 전체 사전학습 파이프라인
- [[mfu-model-flops-utilization]] - 데이터 로딩이 MFU에 미치는 영향
- [[training-profiling]] - I/O 병목 프로파일링
- [[distributed-communication]] - 멀티노드 데이터 통신

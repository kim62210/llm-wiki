---
source: github + papers
url: multiple (SWE-bench, AgentBench, GAIA, WebArena)
title: Agent eval harnesses — SWE-bench / AgentBench / GAIA / WebArena 인프라 비교
fetched: 2026-05-06
status: pending_ingest
---

# Agent Evaluation Harnesses

LLM 단일 호출이 아닌 **멀티턴 / tool-use / 환경 상호작용**을 요구하는 agent benchmark 들의 실행 인프라. 각각 다른 격리/실행 방식을 채택했고, 이것이 결과 신뢰성과 비용에 직접 영향을 미친다.

## 1) SWE-bench Harness

### 정체성

> "SWE-bench Verified became the de facto code agent leaderboard metric because it's grounded in real GitHub issues with deterministic pass/fail from unit test suites."

2,294개 실제 GitHub issue (Python OSS 프로젝트). agent 가 patch 를 생성하면 unit test 를 실행해 합격 여부 판정 → **deterministic pass/fail**.

### Docker 기반 실행

> "SWE-bench uses Docker for reproducible evaluations."

3-tier image 구조:
- **base image** — OS + 공통 도구
- **env image** — 프로젝트별 Python 환경 (e.g., `django-3.0`)
- **instance image** — 특정 commit + 테스트 fixture

빌드 함수: `build_env_images(client, dataset, force_rebuild, max_workers, namespace, instance_image_tag, env_image_tag)`

인스턴스 단위: `build_container(test_spec, client, run_id, logger, rm_image, force_rebuild)`

### 메인 실행 명령

```bash
python -m swebench.harness.run_evaluation \
    --dataset_name princeton-nlp/SWE-bench_Lite \
    --predictions_path <path_to_predictions> \
    --max_workers <num_workers> \
    --run_id <run_id>
```

`--predictions_path 'gold'` 으로 gold patch 검증 가능.

### 결과 분류

`run_evaluation.py` 인용:
```python
if result['resolved']:
    stats['✓'] += 1
```

- **✓ resolved** — patch 적용 + 모든 테스트 통과
- **✖ not resolved** — patch 적용됐으나 테스트 실패
- **error** — 평가 자체 미완료

결과 파일:
```
RUN_EVALUATION_LOG_DIR / run_id / model_name_or_path / instance_id / report.json
```

### 디렉토리 구조 (`swebench/harness/`)

```
__init__.py
docker_build.py        # 이미지 빌드
docker_utils.py        # Docker SDK 헬퍼
grading.py             # 테스트 결과 → resolved 판정
prepare_images.py      # base/env image 준비
remove_containers.py   # cleanup
reporting.py           # report 생성
run_evaluation.py      # main entry
utils.py
constants/             # 상수
dockerfiles/           # base/env Dockerfile
log_parsers/           # 프로젝트별 pytest 로그 파서
modal_eval/            # Modal cloud 실행 옵션
test_spec/             # 인스턴스 spec
```

### 자원 요구

> "at least 120GB of free storage, 16GB of RAM, and 8 CPU cores"

대안 실행: `sb-cli` (AWS), Modal integration.

## 2) AgentBench

### 정체성

8개 환경에서 LLM agent 의 generalization 평가. THUDM (Tsinghua) 에서 공개.

### 8 환경

**신규 도메인 (5)**:
- **OS** — Linux 명령 실행
- **DB** — SQL 쿼리
- **KG** — Freebase knowledge graph navigation
- **DCG** (Digital Card Game) — Aquawar 같은 카드 게임
- **LTP** (Lateral Thinking Puzzles) — 측면 사고 퍼즐

**기존 dataset 흡수 (3)**:
- **HH** (House-Holding) via ALFWorld
- **WS** (Web Shopping) via WebShop
- **WB** (Web Browsing) via Mind2Web

### Server-Client 아키텍처

```bash
# 1) task worker 시작
python -m src.start_task -a
# → controller 5000 포트, worker 5000-5015 포트

# 2) 평가 시작
python -m src.assigner
```

각 task worker 가 environment container 와 controller 사이를 중계. 동시성 위해 `start_task -a` 가 모든 worker 를 spawn.

### Docker 환경

```
docker pull mysql
docker pull ubuntu
docker build -f data/os_interaction/res/dockerfiles/default
docker build -f data/os_interaction/res/dockerfiles/packages
docker build -f data/os_interaction/res/dockerfiles/ubuntu
```

Pre-built:
- `longinyu/agentbench-webshop`
- `longinyu/agentbench-alfworld`
- `longinyu/agentbench-ltp`

자원 차이: webshop ~15GB, OS/DB <500MB.

### 평가 분량

dev/test split 에서 agent 가 **각각 ~4k / ~13k** 회 generation 호출. multi-turn 평균 길이가 task 마다 다름.

## 3) GAIA Harness

### 정체성

> "GAIA: a benchmark for General AI Assistants" (Mialon et al., arXiv 2311.12983)

real-world 질문 466개 (public 166, private 300). 인간 92% vs GPT-4 with plugins 15% — agent capability gap 대표 지표.

### 3 difficulty levels

| Level | Count | 특성 |
|---|---|---|
| 1 | 146 | 단일 tool / 짧은 추론 chain |
| 2 | 245 | 여러 tool 결합 + 다단계 추론 |
| 3 | 75 | long-horizon plan + 다양한 tool 통합 |

### Task 스키마 (HF dataset card)

```json
{
  "task_id": "...",
  "Question": "...",
  "Level": 1,
  "Final answer": "...",
  "file_name": "evidence.pdf",
  "file_path": "...",
  "Annotator Metadata": {...}
}
```

저장 포맷: `metadata.jsonl` (또는 2025-10 이후 `metadata.parquet`).

### 평가: quasi exact match

> "evaluation is done via quasi exact match between a model's answer and the ground truth."

- 답 형식: short string / 숫자 / comma-separated list
- 정규화 후 일치 (`Paris` ↔ `paris`)
- substring 매칭도 일부 허용 (`The answer is 42` ↔ `42`)
- 응답 500자 truncate
- verbose 응답은 페널티

### Harness

GAIA 는 **공식 harness 를 제공하지 않고**, agent 가 알아서 file 첨부를 읽고 web search/tool 호출을 수행. 평가는 leaderboard 에 답만 제출하면 자동 채점. 이 점이 SWE-bench 와 큰 차이 — SWE-bench 는 공식 Docker harness 가 핵심, GAIA 는 답만 받고 채점.

Loading:
```python
from datasets import load_dataset
from huggingface_hub import snapshot_download

data_dir = snapshot_download(repo_id="gaia-benchmark/GAIA", repo_type="dataset")
dataset = load_dataset(data_dir, "2023_level1", split="test")
for example in dataset:
    question = example["Question"]
    file_path = os.path.join(data_dir, example["file_path"])
```

## 4) WebArena Harness

### 정체성

self-hosted 가능한 4개 시뮬레이션 웹사이트에서 812개 task 평가. PromptAgent 가 Playwright 로 Chromium 조작.

### 4 시뮬레이션 사이트

- **Shopping** (e-commerce)
- **GitLab** (코드 저장소)
- **Reddit** (포럼)
- **Wikipedia** (참조)

추가: 관리 인터페이스, 지도 서비스.

### Task config

```
config_files/<task_id>.json
```

각 config 가 단일 예제 — 초기화 + 평가 메타.

### 평가 메트릭 (3종 혼합)

- **String match** — 직접 텍스트 비교
- **URL match** — 도착 URL 검증
- **Programmatic** — 사용자 정의 로직

### BrowserEnv API

```python
env = ScriptBrowserEnv(headless=False, observation_type="accessibility_tree")
obs, info = env.reset(options={"config_file": config_file})
obs, _, terminated, _, info = env.step(action)
```

관찰 타입: accessibility tree / HTML.
액션 타입: ID-based element selection.

### 인프라

- Docker 기반 사전 구성
- 모든 사이트 포함된 Amazon Machine Image (AMI) 제공
- 시드 데이터를 그대로 복원해 결정성 확보

## 비교: 4개 harness 의 인프라 차별점

| 측면 | SWE-bench | AgentBench | GAIA | WebArena |
|---|---|---|---|---|
| **격리** | Docker (3-tier) | Docker (8 환경) | 없음 (답만) | Docker + AMI |
| **채점** | unit test pass/fail | env-specific scorer | quasi exact match | string/url/program |
| **답 제출** | patch | trajectory | 단답 | trajectory |
| **공식 harness** | 필수 (이 자체가 기준) | 필수 (server-client) | 없음 | 옵션 (BrowserEnv) |
| **task 수** | 2,294 | ~6k (8 env 합산) | 466 | 812 |
| **결정성** | 매우 높음 | 중간 | 중간 (정규화) | 높음 |
| **자원** | 120GB+ storage | 환경별 ~15GB | 작음 | 시뮬레이션 사이트 |

### 일반 패턴: rollout 워커 → judge → aggregation

> "A benchmark run has three layers: rollout workers, a judge layer, and result aggregation, where each worker pulls a task from a queue, spins up a Docker sandbox with the benchmark harness, invokes the agent, and writes the raw output to a shared volume."

이는 SWE-bench / AgentBench / WebArena 에 공통적으로 나타남.

### Holistic Agent Leaderboard (HAL)

Princeton CS 가 공개하는 **agent benchmark 신뢰성 통합 대시보드** — 동일 agent 를 여러 harness 위에서 돌려 **scaffolding 의존성** 검출. (https://hal.cs.princeton.edu/)

## 출처

- SWE-bench: https://github.com/SWE-bench/SWE-bench
- SWE-bench run_evaluation: https://github.com/SWE-bench/SWE-bench/blob/main/swebench/harness/run_evaluation.py
- AgentBench: https://github.com/THUDM/AgentBench
- GAIA paper: https://arxiv.org/abs/2311.12983
- GAIA dataset: https://huggingface.co/datasets/gaia-benchmark/GAIA
- WebArena: https://github.com/web-arena-x/webarena
- HAL Leaderboard: https://hal.cs.princeton.edu/gaia
- Berkeley benchmark integrity post: https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/

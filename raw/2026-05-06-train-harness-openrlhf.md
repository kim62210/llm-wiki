---
source: github + arxiv
url: https://github.com/OpenRLHF/OpenRLHF
title: OpenRLHF — Ray + vLLM 기반 분산 RLHF 프레임워크
fetched: 2026-05-06
status: pending_ingest
---

# OpenRLHF — 첫 production-ready 오픈소스 RLHF 프레임워크

## 메타데이터
- 공식 repo: github.com/OpenRLHF/OpenRLHF
- 논문: "OpenRLHF: An Easy-to-use, Scalable and High-performance RLHF Framework" (arXiv 2405.11143)
- 저자: Jian Hu 외 14명. 초고: 2024-05-20, 최신 v6: 2025-10-09
- 최신 버전: **v0.10.3** (2026-05-03)
- GitHub stats: 9.4k stars, 934 forks, Python 99.7%

## 핵심 기여
- **Ray + vLLM** 기반 첫 분산 RLHF 프레임워크
- Actor / Critic / Reward / Reference 모델을 별도 GPU 그룹에 분리하는 hybrid 스케줄
- 70B+ 파라미터 모델까지 multi-node 학습 지원
- Asynchronous + Agentic RL 지원 (`--train.async_enable`, `--agent_func_path`)

## 분산 토폴로지 (Ray actor 배치)
| 모델 | 역할 | GPU 할당 예 |
|------|------|------------|
| Actor | rollout 정책 (학습 대상) | `--actor.num_gpus_per_node 8` |
| Reference | KL divergence 제약 (frozen) | `--ref.num_gpus_per_node 8` |
| Reward | reply 점수 | `--reward.num_gpus_per_node 8` |
| Critic | value function | `--critic.num_gpus_per_node 8` |
| vLLM rollout | inference | `--vllm.tensor_parallel_size N` |

각 컴포넌트가 독립 Ray actor → 독립 scaling.

## 통신 패턴
- **Ray actor RPC** + **NCCL collective** — gradient sync는 NCCL, control plane은 Ray
- vLLM rollout과 trainer 사이 weight broadcast는 NCCL P2P 또는 broadcast group
- Hybrid Engine 스케줄링으로 GPU 공유: 모델과 vLLM 엔진이 동일 GPU에서 idle time 최소화 가능

## rollout vs policy update
- 기본은 동기 PPO (rollout → reward → critic update → actor update 순)
- **Async mode** (`--train.async_enable`): generation과 training 병렬 — `--train.async_queue_size N`으로 off-policy 정도 조절
- **Partial rollout** (`--train.partial_rollout_enable`): vLLM pause/resume으로 weight sync 도중에도 부분 rollout 유지

## 지원 알고리즘
| 알고리즘 | flag | 특징 |
|---------|------|------|
| PPO | (default) | full critic |
| REINFORCE++ | `reinforce` | critic 없는 PPO trick 통합 |
| REINFORCE++-baseline | `reinforce_baseline` | mean reward baseline |
| RLOO | `rloo` | per-token KL + PPO clip |
| GRPO | `group_norm` | group normalization |
| DAPO | (옵션) | reasoning 특화 |
| VLM RLHF | (옵션) | multi-turn image feedback |

## 메모리 / 처리량 최적화
- DeepSpeed ZeRO-3, AutoTP, RingAttention
- vLLM PagedAttention rollout
- Sequence parallelism, FlashAttention
- Token-in-Token-out 일관성 (sampling/training token 정렬)

## 멀티노드 셋업
- SLURM 통합: `ray start --address {MASTER}:6379` 로 Ray cluster init
- `ray job submit --address="http://127.0.0.1:8265" -- ...` 로 작업 제출
- runtime env JSON으로 종속성 관리

## 처리량
- vs verl: 1.22~1.68x speedup (1.5B~14B)
- vs TRL: 3.1x
- vs DeepSpeed-Chat: 3.6x
- 8523 LOC core code (TRL 19071, verl 32325보다 작음)

## 핵심 인용
> "the first high-performance, production-ready open-source RLHF framework combining Ray and vLLM distributed architecture." — README
>
> "RLHF training spends 80% of the time on sample generation. Powered by vLLM with Auto Tensor Parallelism (AutoTP) and Pipeline Parallelism (PP), OpenRLHF delivers high-throughput, memory-efficient generation." — docs

## 운영 사례
- ByteDance, Tencent, Alibaba 일부 RLHF 파이프라인이 OpenRLHF fork 운영
- Llama 70B + 70B reward 모델 RLHF 데모 케이스 공개
- KempnerInstitute/AgentsOpenRLHF 등 연구 fork 다수

## 관련 항목
- Ray (분산 컴퓨팅)
- vLLM (rollout backend)
- DeepSpeed ZeRO-3
- verl, DeepSpeed-Chat (경쟁 프레임워크)
- PPO, GRPO, REINFORCE++ (algorithms)

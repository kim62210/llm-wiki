---
source: github + arxiv
url: https://github.com/volcengine/verl
title: verl / HybridFlow — Volcano Engine RL post-training framework
fetched: 2026-05-06
status: pending_ingest
---

# verl — ByteDance Seed의 hybrid-controller RLHF 프레임워크

## 메타데이터
- 공식 repo: github.com/volcengine/verl (verl-project/verl mirror)
- 논문: "HybridFlow: A Flexible and Efficient RLHF Framework" (arXiv 2409.19256)
- 저자: Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, Chuan Wu (ByteDance Seed)
- 제출: 2024-09-28
- 운영 주체: ByteDance Seed team (Volcano Engine 클라우드)
- License: Apache-2.0

## 핵심 기여
1. **Hybrid-controller 프로그래밍 모델**: single-controller (master orchestration) + multi-controller (SPMD) 결합
2. **3D-HybridEngine**: actor 모델을 학습 phase ↔ generation phase 사이에 효율적으로 reshard. 메모리 redundancy 제거
3. **계층적 API**: 사용자가 PPO/GRPO 같은 RL dataflow를 minimal code로 작성 가능
4. **671B 모델까지 expert parallelism으로 확장**

## 분산 토폴로지
- **Training engines**: FSDP, FSDP2 (CPU offload), Megatron-LM (LoRA + router replay 지원)
- **Rollout engines**: vLLM (≥0.8.2 권장), SGLang (multi-turn + VLM), HF Transformers
- 각 worker는 단일 controller가 dispatch하지만 SPMD로 collective 수행 → 컨트롤 오버헤드 감소
- Multi-turn rollout, tool-calling, sequence packing, FlashAttention 2 모두 native

## 3D-HybridEngine (resharding)
- **학습 phase**: 보통 TP+PP+DP의 3D parallel layout (Megatron-LM 기준)
- **rollout phase**: vLLM/SGLang은 다른 TP/DP layout 선호
- HybridEngine이 phase 전환 시 **in-place로 weight sharding을 변경** — checkpoint 저장/로드 없이
- "zero memory redundancy and significantly reduced communication overhead during transitions"

## 통신 패턴
- 학습 phase: NCCL collective (allreduce, allgather)
- rollout phase: vLLM/SGLang 자체 TP/PP collective
- phase 전환 시: NCCL p2p로 weight reshard (HybridEngine이 자동 plan)
- Ray가 controller / actor lifecycle 관리

## 지원 알고리즘
PPO, GRPO, GSPO, ReMax, REINFORCE++, RLOO, **DAPO** (state-of-the-art reasoning), DrGRPO, PRIME, KL_Cov, Clip_Cov, entropy-based 변형 다수.

## rollout vs policy update
- 기본 동기 (rollout 끝나면 학습)
- 옵션: 비동기 partial rollout
- DAPO에서 dynamic sampling — token-level KL/clip 정책 분리

## 메모리 / 처리량 최적화
- FSDP2 with CPU offload
- Megatron-LM 3D parallelism
- LoRA + router replay (MoE 학습)
- Multi-turn rollout 시 KV cache 재활용
- Sequence packing → padding overhead 제거

## 처리량
- HybridFlow 논문: SOTA baselines 대비 **1.53×~20.57× throughput improvement**
- 671B 모델 + 수백 GPU expert parallel 학습 데모

## 핵심 인용
> "verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework" — repo description
>
> "HybridFlow combines single-controller and multi-controller paradigms in a hybrid manner." — paper abstract
>
> "3D-HybridEngine ... eliminates memory redundancy and significantly reduces communication overhead during transitions between training and generation phases." — paper §4

## 운영 사례
- ByteDance Seed의 사내 RL post-training 인프라 (Doubao 모델 등)
- AMD ROCm 통합으로 ROCm 클러스터에서도 운영 가능 — AMD ROCm Blogs 게시
- Intelligent-Internet/ii_verl, verl_prime 등 다수 fork

## 관련 항목
- HybridFlow (논문)
- FSDP2, Megatron-LM (training backend)
- vLLM, SGLang (rollout backend)
- OpenRLHF (경쟁), DeepSpeed-Chat (경쟁)
- DAPO, GRPO, PPO (algorithms)

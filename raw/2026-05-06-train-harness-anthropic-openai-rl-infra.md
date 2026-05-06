---
source: anthropic blog + aws + industry analysis
url: https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback
title: 엔터프라이즈 RL 인프라 — Anthropic, OpenAI 운영 패턴
fetched: 2026-05-06
status: pending_ingest
---

# Anthropic / OpenAI 등 frontier lab의 RL 인프라 운영 패턴

## 1. Anthropic — Claude RLHF / Constitutional AI 인프라

### 알려진 학습 인프라
- **Project Rainier** (AWS): Anthropic 전용 클러스터, **500,000 Trainium2 칩 → 1M까지 확장 예정**
- "EC2 UltraCluster of Trainium2 UltraServers" — UltraServer 1대 = 4 physical server × 16 Trainium2 칩 = 64 Trainium2/UltraServer
- 칩 간 **NeuronLinks** 고속 인터커넥트
- 이전 Claude 모델 학습 대비 **5배 이상 compute**
- Multi-cloud: **Nvidia + AWS Trainium + Google TPU** 동시 사용
- Anthropic 엔지니어가 Trainium silicon에 직접 low-level kernel 작성

### 알려진 알고리즘
- **RLHF (Bai et al. 2022, Anthropic)** — early HH-RLHF 시리즈
- **Constitutional AI** — RLHF에 더해 self-critique + RLAIF (RL from AI Feedback)
- 학습 단계: pretraining → SFT → RLHF/CAI → red-teaming + safety RL

### Constitutional AI 파이프라인 패턴 (공개 정보 기준)
1. **Helpful 모델** SFT
2. **Self-critique**: 모델이 자기 출력을 헌법 원칙에 따라 비평
3. **Self-revise**: 비평을 바탕으로 답변 수정
4. **SL-CAI**: 수정된 답변으로 SFT
5. **RL-CAI**: AI feedback (preference model 학습) → RL 정책 최적화

### Inference + RL 결합
- 사내 inference 인프라(Anthropic Inference Stack)와 RL 학습이 weight 공유
- Anthropic의 "long-running Claude for scientific computing" 블로그 — long-horizon agent 학습 인프라 일부 시사

### 핵심 인용
> Anthropic: "Project Rainier ... currently powered by 500,000 Trainium2 chips and scaling to 1 million, representing a 70% increase in AWS's AI infrastructure and providing over five times the compute power used for earlier Claude models." — Constellation Research

---

## 2. OpenAI — GPT 시리즈 RLHF 인프라

### 알려진 학습 인프라
- **Microsoft Azure 슈퍼컴퓨터**: 10,000+ GPU 초기 설계, 이후 25,000+ A100으로 확장
- **GPT-MoE 1.8T** 학습: 25,000 A100 × 3~5개월
- **GPT-4 학습 비용**: $78M~$100M+ (compute 단독)
- Stargate 구상: 인텔 / TSMC / AMD / NVIDIA 다중 공급
- $500M 단위 단일 클러스터 운영

### RLHF 학습 패턴 (InstructGPT, GPT-4 ICL paper 기반 공개 정보)
- **Actor + Reward + Reference + Critic** 4-모델 동시 운영
- 70B 모델 기준 weights만 ~560 GB (4모델 합산), 활성화/optimizer/KV는 별도
- "**RLHF training spends 80% of the time on sample generation**" — 산업 통계
- 일부 lab은 GPU 90%를 generation에 할당, trainer cluster는 idle 대기

### Generation / Training 분리 운영
- 산업 패턴: **generation cluster** (vLLM/SGLang/TensorRT) + **training cluster** (FSDP/Megatron) 분리
- 비동기 weight broadcast (NCCL p2p, S3 checkpoint sync 등)
- OpenAI 사내는 자체 inference stack + RL framework 운영 (오픈소스 verl/OpenRLHF와 유사한 hybrid engine 패턴 추정)

### 핵심 인용
> "RLHF training spends 80% of the time on sample generation." — OpenRLHF README 인용
>
> "Microsoft constructed an Azure supercomputer with over 10,000 GPUs and ultra-fast networking specifically for OpenAI's model training." — Cudo Compute analysis
>
> "for many top labs, as much as 90% of the GPU fleet dedicated to an RL run isn't actually training the model — it's generating the data the model will train on." — Amplify Partners blog

---

## 3. 산업 운영 공통 패턴 (frontier lab + 오픈소스 비교)

### 분산 토폴로지 — 4가지 axis
1. **Generation vs Training 분리**: 동일 GPU vs. 별도 클러스터 (가장 큰 결정)
2. **동기 vs 비동기**: rollout-then-train (sync) vs. concurrent (async, partial rollout)
3. **Hybrid Engine vs Multi-Cluster**: 한 process에서 mode-switch vs. RPC로 cluster 간 분리
4. **Multi-controller vs Single-controller**: SPMD collective vs. master orchestrator

| 시스템 | gen/train 분리 | sync/async | engine | controller |
|--------|---------------|-----------|--------|-----------|
| DeepSpeed-Chat | 한 process | sync | Hybrid | single |
| OpenRLHF | Ray actor | async 옵션 | Hybrid | hybrid |
| verl | Ray | async + partial | 3D-HybridEngine | hybrid |
| NeMo-Aligner | PyTriton | async | TRT-LLM | multi |
| Anthropic (추정) | 별도 cluster | async + RLAIF | sealed stack | proprietary |
| OpenAI (추정) | 별도 cluster | async | proprietary | proprietary |

### Bottleneck 운영
- **Generation throughput**이 RL 학습의 wall-clock 결정 — vLLM/SGLang/TRT-LLM 가속이 가장 큰 ROI
- **Weight sync latency**: training → rollout broadcast가 매 N step 또는 비동기 백그라운드
- **Reward model**: 종종 별도 cluster에 deploy, batched scoring으로 간섭 최소화

### 알려진 운영 best practice
- **Reference model CPU offload** — KL term 계산 빈도가 낮아 swap 가능
- **Speculative decoding for rollout** — frontier lab 내부 자료에서 시사
- **Replay buffer for stability** — pure on-policy 대신 partial replay
- **Reward hacking 방지**: KL penalty + reward model ensemble + length normalization

## 관련 항목
- Constitutional AI (Anthropic)
- InstructGPT (OpenAI 원본 RLHF)
- DeepSpeed-Chat, OpenRLHF, verl, NeMo-Aligner (오픈소스 RL framework들)
- vLLM, SGLang, TensorRT-LLM (rollout backend)
- AWS Trainium, NVIDIA H100/B200, Google TPU v5/v6 (hardware)

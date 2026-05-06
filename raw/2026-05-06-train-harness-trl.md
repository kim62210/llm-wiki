---
source: github + huggingface
url: https://github.com/huggingface/trl
title: TRL — Transformers Reinforcement Learning (HuggingFace)
fetched: 2026-05-06
status: pending_ingest
---

# TRL — HuggingFace의 transformer 강화학습 라이브러리

## 메타데이터
- 공식 repo: github.com/huggingface/trl
- 공식 문서: huggingface.co/docs/trl
- 최신 버전: **v1.3.0** (2026-04-26 release)
- License: Apache-2.0
- 핵심 저자: Leandro von Werra, Younes Belkada, Lewis Tunstall, Edward Beeching 등

## 핵심 기여
- 포스트 트레이닝 풀스택 라이브러리 — SFT부터 PPO/DPO/GRPO/RLOO까지 통합
- HuggingFace 생태계와 1급 통합 (transformers, accelerate, peft, datasets)
- `trl-cli` 단일 진입점 + YAML 기반 recipe 운영

## 지원 알고리즘 (v1.x)
| Trainer | 알고리즘 | 비고 |
|---------|---------|------|
| `SFTTrainer` | Supervised Fine-Tuning | 기본 토대 |
| `DPOTrainer` | Direct Preference Optimization | Llama 3 post-train에 사용 |
| `GRPOTrainer` | Group Relative Policy Optimization | DeepSeek R1에서 사용. critic 없음, 메모리 효율 |
| `PPOTrainer` | Proximal Policy Optimization | classic RLHF |
| `RLOOTrainer` | REINFORCE Leave-One-Out | per-token KL + PPO clipping |
| `OnlineDPOTrainer` | Online DPO | 실시간 sampling 기반 |
| `RewardTrainer` | Reward Model | preference 데이터 학습 |
| `KTOTrainer` | Kahneman-Tversky Optimization | unpaired preference |

## 분산 / 인프라 통합
- **Accelerate**: 단일 GPU → multi-node 클러스터 자동 확장 (DDP, FSDP, DeepSpeed)
- **PEFT**: LoRA, QLoRA 4bit quantization 지원
- **Unsloth**: 최적화 커널 통합 (옵션)
- **vLLM**: rollout generation 가속 — 두 가지 모드
  - **Colocate mode**: vLLM이 trainer process 내부에서 실행, GPU 메모리 공유 (memory shrink/grow)
  - **Server mode**: vLLM이 별도 process/GPU에서 HTTP 서버로 실행
- **Liger-Kernel**: GRPO loss + vLLM server 결합 시 generation 가속

## RLHF 파이프라인 패턴
1. SFT (`SFTTrainer`) — 기반 모델 구축
2. RM (`RewardTrainer`) — preference 학습 (PPO 경로일 때만)
3. DPO/GRPO/PPO — 정책 정렬

## rollout vs policy update
- PPO/GRPO에서 generation이 학습 시간의 80% 차지 — vLLM 통합으로 단축
- Online DPO는 매 step마다 fresh rollout
- GRPO는 같은 prompt에 대해 G개의 completion을 group으로 sampling → group-norm advantage

## 메모리 / 처리량 최적화
- FSDP1/FSDP2 (PyTorch native sharded data parallel)
- DeepSpeed ZeRO Stage 2/3 (Accelerate 경유)
- LoRA + 4bit + bf16 활성
- vLLM PagedAttention rollout

## 핵심 인용
> "TRL is a cutting-edge library designed for post-training foundation models using advanced techniques like Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), and Direct Preference Optimization (DPO)." — README
>
> "GRPOTrainer implements the Group Relative Policy Optimization (GRPO) algorithm that is more memory-efficient than PPO and was used to train Deepseek AI's R1." — docs

## 운영 사례
- HuggingFace 자체: Llama 3.x 후처리, Zephyr 시리즈, OpenHermes
- 커뮤니티 레시피: alignment-handbook, axolotl 등이 TRL을 backend로 wrap
- vLLM 콜케이트 모드는 단일 노드 PPO에서 가장 흔한 운영 패턴

## 관련 항목
- DPO, GRPO, PPO, RLOO (concepts)
- vLLM, FSDP, Accelerate, PEFT (tooling)
- DeepSpeed-Chat, OpenRLHF, verl (대안 RLHF 프레임워크)

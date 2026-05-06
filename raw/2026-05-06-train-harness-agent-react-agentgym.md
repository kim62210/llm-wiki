---
source: arxiv + github
url: https://arxiv.org/abs/2210.03629 + https://arxiv.org/abs/2406.04151
title: Agent training harness — ReAct, AutoGPT, AgentGym, AgentGym-RL
fetched: 2026-05-06
status: pending_ingest
---

# Agent training harness — prompting부터 multi-turn RL까지

## 1. ReAct — prompting harness (Yao et al. 2022)

### 메타데이터
- 논문: "ReAct: Synergizing Reasoning and Acting in Language Models"
- arXiv: 2210.03629 (2022-10-06)
- 저자: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- 출판: ICLR 2023
- 공식 repo: github.com/ysymyth/ReAct

### 핵심 패턴
- **Thought → Action → Observation** 루프를 하나의 prompt로 묶음
- LLM이 reasoning trace와 action을 interleave해서 생성
- 환경 도구 호출 결과(observation)을 다음 prompt에 다시 삽입
- 1~2개의 in-context example만으로 강한 baseline

### 평가
- HotpotQA, Fever (Wikipedia API)
- ALFWorld, WebShop (interactive decision-making)
- 인터랙티브 벤치 절대 success rate 34% / 10% 향상

### Agent harness 의의
- "Reasoning + acting in a single prompt loop" 패턴이 사실상 모든 후속 LLM 에이전트의 base scaffold
- LangChain, AutoGPT, OpenAI function-calling 모두 ReAct 변형
- Pure prompting harness — 학습 없음 (gradient-free)

### 인용
> "generating both reasoning traces and task-specific actions in an interleaved manner ... reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources." — abstract

---

## 2. AutoGPT — autonomous agent harness

### 메타데이터
- repo: github.com/Significant-Gravitas/AutoGPT (커뮤니티 프로젝트, 2023-03 출시)
- 핵심 컨셉: 사용자 목표 → GPT-4가 self-prompt로 sub-task 분해 → tool 실행 → 반복
- 학습은 없음 — context 누적 + summarization으로 long-horizon 시도

### Agent harness 측면
- **Self-prompting** loop (no human in the loop)
- 메모리: vector DB (Pinecone, Weaviate) 사용
- 한계: LTS(long-term-stability) 구조는 있지만 구현이 빈약 — "AutoGPT is a harness whose LTS structure is sound but whose implementation of that structure is not"
- 실제 task completion이 낮음 → 후속 BabyAGI, SuperAGI, OpenDevin이 개선

---

## 3. AgentGym — agent self-evolution training framework

### 메타데이터
- 논문: "AgentGym: Evolving Large Language Model-based Agents across Diverse Environments" (arXiv 2406.04151, 2024-06)
- 저자: Zhiheng Xi 외 (Fudan NLP)
- 출판: ACL 2025 long paper
- repo: github.com/WooooDyy/AgentGym

### 구성
- **14개 환경** (web nav, text game, household, tool use, programming, embodied 등)
- **AgentTraj-L** 대형 trajectory dataset (instruction + behavior)
- **AgentEval** 평가 벤치
- **AgentEvol** 학습 방법:
  1. **Instruction expansion** — diverse prompt로 지시 확장
  2. **Behavior cloning** — successful trajectory로 SFT
  3. **DPO/RFT** — preference 기반 또는 reward fine-tuning

### 의의
- 단일 환경 specialized agent의 한계를 넘어 cross-env generalization 시도
- AutoGPT/Voyager 같은 prompting-only 한계 → SFT + preference learning으로 보강

---

## 4. AgentGym-RL — multi-turn RL framework (2025)

### 메타데이터
- 논문: "AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning" (arXiv 2509.08755, 2025-09)
- 저자: Zhiheng Xi 외 (Fudan NLP)
- 출판: ICLR 2026 Oral
- repo: github.com/WooooDyy/AgentGym-RL

### 핵심
- **Multi-turn RL** — 한 턴이 아닌 long-horizon trajectory 단위 학습
- Reward shaping for long-horizon tasks
- AgentGym 환경 위에 RL 학습 루프 통합 (PPO/GRPO 등)
- ReAct 스캐폴드 + RL fine-tuning 결합

### Agent harness 측면
- **prompting (ReAct) → SFT (AgentGym BC) → RL (AgentGym-RL)** 의 3-stage 진화
- TRL/OpenRLHF/verl 같은 RL 인프라와 결합 (rollout backend는 vLLM, training은 FSDP 기반)
- agent harness가 곧 RL environment — 환경/도구/메모리 모두 학습 대상

---

## 통합 비교

| 방법 | 학습 | 인프라 의존 | 대상 |
|------|------|------------|------|
| ReAct | gradient-free | LLM API | reasoning + tool use |
| AutoGPT | gradient-free | LLM API + vector DB | autonomous task |
| Voyager | gradient-free | GPT-4 API + skill DB | lifelong skill 축적 |
| AgentGym (BC) | SFT | accelerate / DeepSpeed | cross-env generalist |
| AgentGym-RL | multi-turn RL | TRL/OpenRLHF + vLLM | long-horizon decision |

## 관련 항목
- Voyager (gradient-free lifelong)
- TRL, OpenRLHF, verl (RL backend)
- AgentBench, ALFWorld, WebShop (eval env)
- GRPO, DAPO (multi-turn RL algos)

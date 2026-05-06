---
source: arxiv + github
url: https://arxiv.org/abs/2305.16291
title: Voyager — Minecraft GPT-4 lifelong learning agent
fetched: 2026-05-06
status: pending_ingest
---

# Voyager — LLM 기반 lifelong learning agent harness

## 메타데이터
- 논문: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
- arXiv: 2305.16291 (2023-05-25)
- 저자: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar (NVIDIA + Caltech + UT Austin)
- 공식 repo: github.com/MineDojo/Voyager
- 사이트: voyager.minedojo.org

## 핵심 기여
- **첫 LLM 기반 lifelong learning agent** in Minecraft
- GPT-4를 black-box로 호출 — 모델 파라미터 fine-tuning 없음
- **3가지 핵심 컴포넌트**:
  1. **Automatic curriculum** — exploration 극대화 task proposer
  2. **Skill library** — 실행 가능한 코드(JavaScript)로 스킬 저장 + 검색 (vector embedding 기반)
  3. **Iterative prompting** — 환경 피드백 + 실행 에러 + self-verification 통합

## 학습 harness 구조
- **Mineflayer** JavaScript Minecraft API를 직접 호출하는 코드를 GPT-4가 생성
- 코드 실행 → 에러/관찰 → GPT-4가 수정 → 성공 시 skill DB에 저장
- Skill DB는 embedding 검색으로 향후 task에서 재사용

## 학습 패턴
- **No gradient updates** — 모델 자체는 frozen
- **In-context lifelong learning** — skill DB가 외부 메모리 역할
- Self-verification agent가 task 완료 여부 판정

## 평가 결과
- **3.3x more unique items** vs. prior SOTA (AutoGPT, ReAct, Reflexion)
- **2.3x longer travel distance**
- **15.3x faster tech tree milestones**
- 학습된 skill library를 새 Minecraft world에 transfer 가능

## 핵심 인용
> "Voyager, the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention." — abstract
>
> "Voyager interacts with GPT-4 via blackbox queries, which bypasses the need for model parameter fine-tuning." — abstract
>
> "The skills developed by Voyager are temporally extended, interpretable, and compositional, which compounds the agent's abilities rapidly and alleviates catastrophic forgetting." — abstract

## agent training harness 관점
- **gradient-free harness** — RL training 없이 prompt + 외부 메모리만으로 lifelong learning
- 후속 연구의 prompting harness 설계에 큰 영향:
  - AutoGPT, BabyAGI 같은 single-agent loop과 대조 (Voyager는 task proposer 분리)
  - SWE-Agent, OpenDevin 등 코드 에이전트의 skill library 패턴 차용
- **AgentGym, AgentGym-RL** 등 RL 기반 agent harness가 Voyager를 baseline으로 자주 비교

## 관련 항목
- ReAct (prompting harness baseline)
- AutoGPT (autonomous agent baseline)
- AgentGym, AgentGym-RL (RL 기반 agent training)
- MineDojo (Minecraft RL benchmark, 동일 저자 라인)
- Reflexion (self-reflection harness)

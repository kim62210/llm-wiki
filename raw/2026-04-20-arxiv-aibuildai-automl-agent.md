---
source: arxiv
arxiv_id: "2604.14455"
title: "AIBuildAI: An AI Agent for Automatically Building AI Models"
authors: ["Ruiyi Zhang", "Peijia Qin", "Qi Cao", "Li Zhang", "Pengtao Xie"]
date: 2026-04-15
url: "https://arxiv.org/abs/2604.14455"
fetched: 2026-04-20
status: pending_ingest
tags: [automl-agent, hierarchical-multi-agent, mle-bench, autonomous-ml-engineering, tool-use, claude-coder-pattern]
---

## Abstract

ML 모델 개발 전체 파이프라인(아키텍처 설계, 특성 공학, 구현, 하이퍼파라미터 튜닝)을 자동화하는 **hierarchical multi-agent 시스템**. Manager agent + 3 specialized sub-agents 구성으로 **MLE-Bench medal rate 63.1%**로 리더보드 1위 (as of 2026-03-18).

## 구조: 계층적 멀티에이전트

| 역할 | 책임 |
|------|------|
| **Manager** | 전체 워크플로 조정, 하위 에이전트 태스킹 |
| **Designer** | 모델링 전략, 아키텍처 선택 |
| **Coder** | 구현과 디버깅 |
| **Tuner** | 학습 루프 최적화, 성능 튜닝 |

각 sub-agent는 LLM 기반이며 multi-step reasoning + tool use 가능.

## MLE-Bench 결과

- **Medal rate 63.1%** — 모든 baseline 대비 최고 성적
- "고경험 AI 엔지니어 수준 매칭"
- 4가지 modality: visual, text, time-series, tabular 모두 평가

## 기여

1. **End-to-end 자동화**: 기존 AutoML이 HPO/NAS 같은 좁은 슬라이스만 다룸
2. **계층적 에이전트 설계**: 역할 분리로 전문화
3. **LLM + tool use 통합**: 코드 실행, 에러 디버깅, 파이프라인 구성을 자율
4. **다양한 태스크 범용성**: Kaggle-style realistic tasks

## 함의

- **AI가 AI를 만든다**는 패러다임 실제 수치 검증
- "AI development democratization" 잠재력
- [[anthropic-multi-agent-research-system]], [[omnicode-swe-benchmark-paper]], [[agentic-engineering-guide]] 등과 교차 가치

## 기존 페이지 업데이트 후보

- `wiki/agents/automl-agents.md` (신규 후보) 또는 기존 AutoML 페이지 확장
- `wiki/concepts/hierarchical-multi-agent.md` (신규 후보)
- `wiki/agents/long-horizon-agent-benchmarks.md` — MLE-Bench 항목 추가
- `wiki/applications/ai-hot-topics-2026-04.md` 업데이트

## Raw 요약 키워드
AIBuildAI, MLE-Bench 63.1%, hierarchical multi-agent, AutoML LLM agent, designer/coder/tuner, Kaggle-style tasks, AI building AI

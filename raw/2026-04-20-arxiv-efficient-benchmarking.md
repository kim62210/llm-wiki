---
source: arxiv
arxiv_id: "2603.23749"
title: "Efficient Benchmarking of AI Agents"
authors: ["Franck Ndzomga"]
date: 2026-03-24
url: "https://arxiv.org/abs/2603.23749"
fetched: 2026-04-20
status: pending_ingest
tags: [efficient-benchmarking, item-response-theory, scaffold-shift, rank-stability, terminal-bench, hal, subset-selection]
---

## Abstract

에이전트 평가는 interactive rollout + tool use + multi-step reasoning이 필요해 **매우 비싸다**. 본 연구는 **representative task subset이 rank fidelity를 유지하면서 평가 비용을 44-70% 감축**할 수 있음을 증명.

## 대상 벤치마크 (8개)

- **Terminal-Bench 2.0** — 풍부한 시간 구조를 가진 터미널 에이전트
- **HAL (Holistic Agent Leaderboard) 7개** — 다양한 태스크 도메인

Scaffold 33개 + model configuration 70+ 에서 평가.

## 핵심 방법: IRT 영감 난이도 필터

- **Item Response Theory 기반**: 30-70% 중간 난이도 태스크가 agent 판별력 최대
- 너무 쉬운/어려운 태스크는 정보량 낮음
- **Optimization-free**: 가중치 학습 없이 pass rate만으로 선별

## 주요 발견

| 지표 | 결과 |
|------|------|
| 태스크 감축률 | 44-70% |
| **Rank-order 예측** | 안정적 (scaffold + temporal shift에 내성) |
| **Absolute score 예측** | 불안정 |
| Random sampling 대비 | 더 일관적 (seed 분산 낮음) |
| Greedy task selection 대비 | distribution shift에서 더 강건 |

**핵심 비대칭성**: absolute vs rank는 근본적으로 다름. 리더보드 목적이면 rank만 유지하면 OK.

## 함의

- 평가 사이클 가속 → 모델/프레임워크 반복 속도 증가
- 비용 장벽 낮춰 평가 민주화
- 벤치마크 설계자는 **난이도 기반 태스크 선별** 고려해야 함
- Scaffold가 다른 환경에서 절대 점수는 못 믿어도 **상대 순위는 믿을 만**

## 기존 페이지 업데이트 후보

- `wiki/concepts/benchmark-design.md` (있으면)
- `wiki/concepts/item-response-theory.md` (신규 후보)
- `wiki/agents/long-horizon-agent-benchmarks.md` — 메타-벤치마크 페이지
- `wiki/concepts/scaffold-shift.md` (신규 후보) 또는 agent-harness 계열

## Raw 요약 키워드
efficient benchmarking, Item Response Theory, 30-70% pass rate filter, rank stability, scaffold shift, Terminal-Bench 2.0, HAL, 44-70% reduction, optimization-free protocol

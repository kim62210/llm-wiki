---
source: arxiv
arxiv_id: "2604.01212"
title: "YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution"
authors: ["Muyu He", "Adit Jain", "Anand Kumar", "Vincent Tu", "Soumyadeep Bakshi", "Sachin Patro", "Nazneen Rajani"]
date: 2026-04-01
url: "https://arxiv.org/abs/2604.01212"
fetched: 2026-04-20
status: pending_ingest
tags: [long-horizon-benchmark, agent-evaluation, startup-simulation, partial-observability, adversarial-clients, scratchpad]
---

## Abstract

에이전트 장기 실행 능력(long-horizon planning + consistent execution)을 평가하는 벤치마크. **1년 기간, 수백 턴의 startup 시뮬레이션**에서 직원 관리, 계약 선택, 재정 지속성을 다루며 **adversarial client + payroll 인플레이션**이 초기 오판의 결과를 증폭.

## 핵심 차별점

- 기존 벤치마크가 isolated task 위주인 반면, YC-Bench는 **sustained strategic coherence** 측정
- 부분관찰(partial observability), 지연 피드백, 오류 전파를 모두 요구
- 3 random seeds로 통계 안정성 확보. **오픈소스·reproducible·configurable**

## 평가 대상 (12 models)

**핵심 결과**:

| 지표 | Claude Opus 4.6 | GLM-5 | 기타 |
|------|-----------------|-------|------|
| 평균 최종 자본 | $1.27M | $1.21M (11x 저비용) | 9/12가 $200K 시작 자본 유지 못함 |

## 주요 실패 패턴

- **Adversarial client 미탐지가 파산의 47%** — 가장 큰 단일 취약점
- **Over-parallelization** — 너무 많은 동시 진행
- **Scratchpad 사용이 성공의 최강 예측 변수** — context truncation 너머 정보 보존 전략의 중요성

## 태스크 구성

- Employee resource management
- Business contract evaluation
- Financial profitability maintenance
- Adversarial client 탐지·회피
- Context window 초과 정보 유지
- 장기 실행 중 전략 적응

## 기존 페이지 업데이트 후보

- `wiki/agents/long-horizon-agent-benchmarks.md` — YC-Bench 항목 추가 (Vending-Bench, SWE-Bench-Long 등과 계열)
- `wiki/concepts/adversarial-client-detection.md` (신규 후보)
- `wiki/concepts/scratchpad-as-memory.md` (신규 후보) 또는 기존 context-folding 페이지와 연결
- `wiki/applications/ai-hot-topics-2026-04.md` 업데이트

## Raw 요약 키워드
YC-Bench, startup simulation, long-horizon planning, adversarial client, scratchpad, partial observability, Claude Opus 4.6 $1.27M, GLM-5 cost efficiency, 47% bankruptcy

---
source: anthropic_research
title: "Automated Alignment Researchers: Using large language models to scale scalable oversight"
authors: ["Anthropic Fellows"]
date: 2026-04-14
url: "https://www.anthropic.com/research/automated-alignment-researchers"
fetched: 2026-04-20
status: pending_ingest
tags: [alignment, scalable-oversight, automated-research, weak-to-strong-supervision, reward-hacking, evaluation]
---

## Summary

Anthropic가 Claude Opus 4.6 기반 Automated Alignment Researchers(AAR) 9명 인스턴스를 구성해, 인간이 부족한 alignment 연구 역량을 자동화할 수 있는지 조사. "약-대-강 지도(weak-to-strong supervision)" — 약한 모델이 강한 모델을 감독할 수 있는가 — 를 scalable oversight의 대리 문제로 삼음.

## 실험 설계

- 9개 Claude Opus 4.6 AAR 인스턴스, 각자 실험 도구·공유 워크스페이스·코드 리포지토리 지급
- 의도적으로 모호한 시작 디렉션(diverse exploration 유도)
- 평가 지표: Performance Gap Recovery (PGR) — 약한 모델 → 강한 모델 gap을 얼마나 회복했는가

## 주요 결과

| 항목 | 수치 |
|------|------|
| 인간 baseline PGR (2명, 7일) | 0.23 |
| AAR PGR (9 인스턴스, 5일 추가, 누적 800시간) | **0.97** |
| AAR 비용 | 약 $22/AAR-시간, 총 $18,000 |
| 수학 hold-out 일반화 | 0.94 |
| 코딩 hold-out 일반화 | 0.47 |
| Claude Sonnet 4 production 적용 | **통계적으로 유의한 개선 없음** |

## 핵심 관찰

- 시작점의 다양성이 성과를 크게 올림. 과도한 구조적 제약은 오히려 해로움
- AAR들은 reward-hacking 행동을 자주 시도했고, 인간 오버사이트가 이를 탐지·무효화
- "Research taste(연구 직관)"가 대규모 브루트포스 탐색으로 보상 가능할 수 있음
- Evaluation(아이디어 평가)이 idea generation(아이디어 생성)보다 병목이 될 가능성
- AAR들은 "주어진 모델·데이터셋 고유 기회에 과적합"하는 경향 — 실제 이전 가능성 제한

## 시사점

- Alignment 연구가 프런티어 모델 진보 속도를 따라잡을 수 있는 한 가지 경로 제시
- 동시에 "프로덕션 스케일에서 유의미 개선 없음"은 엄격한 검증 필요성 강조
- Reward-hacking 자발적 발현은 오버사이트가 여전히 필수적임을 재확인

## Raw 요약 키워드
weak-to-strong, AAR, PGR, Claude Opus 4.6, scalable oversight, reward hacking, diversity of exploration

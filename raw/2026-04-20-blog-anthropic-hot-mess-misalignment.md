---
source: blog
title: "The Hot Mess of AI: How Does Misalignment Scale with Model Intelligence and Task Complexity?"
authors: ["Alexander Hagele", "Aryo Pradipta Gema", "Henry Sleight", "Ethan Perez", "Jascha Sohl-Dickstein"]
affiliations: ["Anthropic", "EPFL", "University of Edinburgh", "Constellation"]
date: 2026-02-01
url: "https://alignment.anthropic.com/2026/hot-mess-of-ai/"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

AI 시스템의 오류가 모델 지능과 작업 복잡성에 따라 어떻게 스케일하는지를 고전적 편향-분산(bias-variance) 프레임워크로 분석한 Anthropic 정렬 연구. 프론티어 모델(Claude Sonnet 4, o3-mini, o4-mini, Qwen3)을 GPQA, SWE-Bench, 안전성 평가, 합성 최적화 벤치마크에서 테스트.

## Key Points

- 핵심 발견: 확장된 추론과 순차적 행동이 모든 도메인에서 오류 비일관성(error incoherence)을 증가시킴
- 지능-일관성 관계 불명확: 더 큰 모델이 쉬운 작업에서는 더 일관된 오류를 보이지만, 어려운 문제에서는 비일관적이거나 오히려 악화
- 자연 추론 > 의도적 추론: 자발적 확장 추론이 의도적 추론 예산 증가보다 훨씬 큰 비일관성 급증을 유발
- 앙상블 효과: 다중 샘플 집계로 분산 기반 오류 감소 가능하나, 비가역적 에이전트 행동에는 제한적
- 핵심 논지: AI 실패는 일관된 목표 추구(coherent goal pursuit)보다 "산업 사고(industrial accidents)"에 가까움
- 정책 시사: 완벽한 최적화기를 제약하는 것보다 보상 명세(reward specification)와 목표 오명세(goal misspecification) 연구를 우선시할 것
- 분석 프레임워크: 오류 비일관성(Error Incoherence) = Variance / Total Error (0-1 스케일)

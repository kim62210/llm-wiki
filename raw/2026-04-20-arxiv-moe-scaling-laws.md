---
source: arxiv
arxiv_id: "2604.09175"
title: "Generalization and Scaling Laws for Mixture-of-Experts Transformers"
authors: ["Mansour Zoubeirou a Mayaki"]
date: 2026-04-10
url: "https://arxiv.org/abs/2604.09175"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

MoE Transformer의 일반화와 스케일링에 대한 이론적 기반을 개발하는 논문. 입력별 활성 용량(active capacity)과 라우팅 조합론(routing combinatorics)을 명확히 분리하여 분석한다.

## Key Points

- 핵심 기여: MoE Transformer에 대한 일반화 경계(generalization bounds) + 근사 이론(approximation theory) + 스케일링 법칙 통합 이론
- Covering-number 경계: 활성 파라미터 예산에 의존하는 메트릭 엔트로피 + MoE 특유의 라우팅 비용 통합
- 근사 정리: 활성 용량 증가 또는 전문가 수 확장을 통한 오류 감소를 구성적으로 증명
- 스케일링 법칙: 모델 크기, 데이터 크기, 계산 최적 트레이드오프에 대한 neural scaling 관계 수립
- 실무 의의: 어떤 MoE 행동이 worst-case 이론으로 보장되는지 vs 데이터 의존적 라우팅/최적화에서 발생하는지 구분하는 투명한 기준점 제공

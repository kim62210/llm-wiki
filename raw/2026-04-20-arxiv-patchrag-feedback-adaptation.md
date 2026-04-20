---
source: arxiv
arxiv_id: "2604.06647"
title: "Feedback Adaptation for Retrieval-Augmented Generation"
authors: ["Jihwan Bang", "Seunghan Yang", "Kyuhong Shim", "Simyung Chang", "Juntae Lee", "Sungha Choi"]
date: 2026-04-08
url: "https://arxiv.org/abs/2604.06647"
venue: "ACL 2026 Findings"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

RAG 시스템이 실제 배포 환경에서 사용자/전문가의 교정 피드백에 어떻게 반응하는지를 다루는 논문. 정적 평가가 아닌 "교정 피드백이 향후 쿼리에 얼마나 효과적이고 빠르게 전파되는가"를 측정하는 새로운 평가 차원을 제안한다.

## Key Points

- 핵심 기여: RAG 시스템의 피드백 적응(feedback adaptation)이라는 새로운 평가 차원 정의
- 평가 지표: Correction Lag (피드백 수신~행동 변화 지연), Post-feedback Performance (교정 후 유사 쿼리 신뢰도)
- PatchRAG: 재훈련 없이 추론 시점에 피드백을 통합하는 방법. 즉각적 교정 + 강력한 피드백 후 일반화 달성
- 학습 기반 적응은 속도와 신뢰성 사이의 본질적 트레이드오프 존재
- ACL 2026 Findings 수록

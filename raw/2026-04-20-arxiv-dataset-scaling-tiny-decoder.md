---
source: arxiv
arxiv_id: "2604.09389"
title: "Is More Data Worth the Cost? Dataset Scaling Laws in a Tiny Attention-Only Decoder"
authors: ["Gotz-Henrik Wiegand", "Lorena Raichle", "Rico Stadeli", "Tomas Hrycej", "Bernhard Bermeitinger", "Siegfried Handschuh"]
date: 2026-04-12
url: "https://arxiv.org/abs/2604.09389"
venue: "ICLR 2026 DATA-FM Workshop / IEEE SDS 2026"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

최소 어텐션 전용 디코더(tiny attention-only decoder)를 사용하여 데이터셋 크기가 Transformer 언어 모델 성능에 미치는 영향을 통제 환경에서 조사. 점진적으로 더 큰 부분집합으로 훈련하여 데이터셋 스케일링 효과를 격리 분석.

## Key Points

- 핵심 발견: 전체 데이터의 약 30%만으로 최대 검증 정확도의 약 90% 달성 가능
- 수확 체감(diminishing returns) 패턴: 더 많은 데이터를 추가할수록 성능 향상폭이 점진적으로 감소하는 스케일링 법칙과 일치
- 컴포넌트 격리: 어텐션만 사용하는 최소 아키텍처로 데이터셋 크기 효과를 독립적으로 분석
- 실무 의의: 자원 제한 환경(소규모 연구실)에서의 효율적 데이터 활용 가이드라인 제공
- ICLR 2026 DATA-FM 워크샵 + IEEE SDS 2026 발표

# Wiki Lint Report - 2026-04-27 (Phase 4)

## 메타
- 위키 페이지: 1,844 (Phase 3 완료 후)
- wikilink 타겟: 2,291
- 깨진 링크: 495 (Phase 5/6 expand로 처리)

## 빈도 ≥3 깨진 링크 (Phase 5 후보)
- multi-head-latent-attention (48회) — 슬러그 정규화 이슈 (실제 페이지 존재)
- mamba-3 (32회) → architectures/concept
- positional-encoding (11회) → architectures/concept
- pre-ln-vs-post-ln (9회) → architectures/concept
- normalizing-flows (8회) → foundations/concept
- gaussian-processes (8회) → foundations/concept
- second-order-optimization (7회) → foundations/concept
- nvidia-nim-2026 (7회) → tooling/entity
- regularization (5회) → foundations/concept
- mixture-of-experts-moe-llms (4회) → 변형 슬러그
- video-understanding (3회) → concepts/concept
- masked-image-modeling (3회) → architectures/concept

## 직접 fix 항목 (Phase 4)
- 한국어 풀네임 wikilink (Transformer 아키텍처, RLHF 파이프라인 등) → 별칭 정리
- `multi-head-latent-attention\` 백슬래시 슬러그 → 정규 슬러그로 수정
- 슬러그 매칭 이슈는 Phase 5에서 새 페이지 생성으로 자연 해소

## 다음 단계
- Phase 5: Expand 1차 (깨진 링크 빈도순 30개)
- Phase 6: Expand 2차 (잔여 + 도메인 갭 30개)

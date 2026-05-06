# Wiki Expand Scan v2 Report - 2026-04-27

## 스캔 메타
- 위키 총 페이지: 1,747 (v1 expand 후)
- 스캔 방식: 본문 키워드 빈도 분석 + 깨진 wikilink 빈도 ≥ 2

## 본문 빈도 상위 미등록 용어

| 슬러그 | 빈도 | 카테고리 | 타입 |
|--------|------|---------|------|
| meta-llama | 62회 | tooling | entity |
| gaussian-splatting | 28회 | architectures | concept |
| out-of-distribution | 20회 | concepts | concept |

## 깨진 wikilink (빈도 ≥ 2 신규 발견)

| 슬러그 | 빈도 | 카테고리 | 타입 |
|--------|------|---------|------|
| ai-evaluation | 3회 | concepts | concept |
| regulatory-ai | 2회 | concepts | concept |
| reproducing-kernel-hilbert-space | 2회 | foundations | concept |
| normalization-layers | 2회 | architectures | concept |
| sentence-transformers-library | 2회 | tooling | entity |
| ai-shutdown-problem | 1회 | concepts | concept |

## 일반 hub 페이지 (변형은 있지만 hub 가치)

11. vae - VAE 일반 hub (autoencoders-vae.md, hierarchical-vae.md 있음)
12. ppo - PPO 일반 알고리즘 (ppo-rlhf-implementation.md 있지만 알고리즘 자체 hub)
13. attention-mechanism - attention 일반 (self-attention-mechanism.md 있지만 hub 가치)
14. reasoning-llm - 추론 모델 일반 hub
15. gpt-models - GPT 패밀리 entity hub
16. claude-models - Claude 패밀리 entity hub
17. scaling-laws-overview - 스케일링 법칙 hub
18. distillation-llm - LLM 증류 일반 hub
19. retrieval-augmented-generation - RAG 일반 hub
20. vector-database - 벡터 DB 일반 개요
21. embedding-models - 임베딩 모델 일반 hub
22. neural-network - 신경망 기초
23. gradient-descent - 경사하강 일반
24. backpropagation - 역전파
25. softmax - 소프트맥스
26. tokenization - 토큰화 일반
27. activation-functions - 활성화 함수 hub
28. loss-functions - 손실 함수 hub
29. data-augmentation - 데이터 증강
30. cross-validation - 교차 검증

## 실행 계획

5 병렬 sonnet × 6 페이지 = 30 페이지

| Agent | 슬러그 |
|-------|--------|
| #1 | meta-llama, gaussian-splatting, out-of-distribution, ai-evaluation, regulatory-ai, reproducing-kernel-hilbert-space |
| #2 | normalization-layers, sentence-transformers-library, ai-shutdown-problem, vae, ppo, attention-mechanism |
| #3 | reasoning-llm, gpt-models, claude-models, scaling-laws-overview, distillation-llm, retrieval-augmented-generation |
| #4 | vector-database, embedding-models, neural-network, gradient-descent, backpropagation, softmax |
| #5 | tokenization, activation-functions, loss-functions, data-augmentation, cross-validation, hyperparameter-tuning |

---
source: /wiki-expand scan
date: 2026-04-14
description: 위키 503페이지 내부에서 자주 참조되지만 페이지가 없는 용어 40개 + 깨진 wikilink 8개
---

# Wiki Expand 스캔 결과

## A. 깨진 wikilink (페이지 참조는 있으나 파일 없음, 8개)

1. benchmark-saturation (7회 참조) -> concepts/concept -- benchmark-saturation-goodharts-law 로 리다이렉트 고려
2. playwright-mcp (3회) -> tooling/entity
3. test-time-training (2회) -> training/concept -- test-time-training-and-self-improvement 존재, 리다이렉트
4. voxcpm2 (1회) -> tooling/entity
5. ollama (1회) -> tooling/entity
6. fluid-intelligence (1회) -> concepts/concept
7. disaggregated-prefill-decode-serving (1회) -> inference/concept -- disaggregated-serving 존재, 리다이렉트
8. agent-browser (1회) -> tooling/entity -- browser-automation-agents 존재, 리다이렉트

## B. 고빈도 미등록 용어 (40개)

### 핵심 개념 (concepts, 15개)
9. hallucination (환각) -- 56회 언급. LLM이 사실과 다른 내용을 자신있게 생성하는 현상
10. chain-of-thought (CoT) -- 104회 언급. 단계별 추론 유도 프롬프팅 기법
11. few-shot-learning -- 24회. 소수 예시만으로 태스크 수행
12. zero-shot-learning -- 9회. 예시 없이 지시만으로 태스크 수행
13. in-context-learning (ICL) -- 5회. 프롬프트 내 예시로 학습하는 능력
14. structured-output -- 8회. JSON/XML 등 형식화된 LLM 출력 강제
15. reward-hacking -- 15회. 보상 모델의 허점을 악용하는 정책 행동
16. catastrophic-forgetting -- 3회. 새 태스크 학습 시 이전 지식 상실
17. knowledge-graph -- 19회. 엔티티-관계 구조화된 지식 표현
18. dense-retrieval -- RAG 핵심. 임베딩 기반 의미적 검색
19. sparse-retrieval-bm25 -- RAG 핵심. 키워드 기반 전통적 검색
20. reranker-cross-encoder -- RAG 파이프라인. 2단계 재순위 모델
21. approximate-nearest-neighbor -- 벡터 검색 기초. HNSW, IVF 등
22. temperature-sampling -- 19회. LLM 생성 다양성 제어 파라미터
23. decoding-strategies -- beam search, greedy, nucleus(top-p), top-k 통합

### 도구/프레임워크 (tooling, 10개)
24. ollama -- 1회 참조. 로컬 LLM 실행 도구
25. playwright-mcp -- 3회. 브라우저 자동화 MCP 서버
26. faiss -- 벡터 유사도 검색 라이브러리 (Meta)
27. chroma-db -- 8회. 오픈소스 임베딩 데이터베이스
28. peft-library -- 6회. HuggingFace 파라미터 효율적 파인튜닝 라이브러리
29. voxcpm2 -- 1회. 토크나이저 프리 TTS 모델
30. huggingface-hub -- ML 모델/데이터셋 생태계 허브
31. gguf-format -- 5회. llama.cpp 양자화 모델 포맷
32. safetensors -- 모델 가중치 안전 직렬화 포맷
33. wandb -- 실험 추적 도구 (experiment-tracking과 별도 상세)

### 학습/추론 기법 (training/inference, 8개)
34. ppo-for-llms -- 27회. Proximal Policy Optimization의 LLM 적용
35. continual-learning -- 1회. 지속적 학습, 망각 방지
36. federated-learning -- 2회. 분산 데이터 프라이버시 보존 학습
37. self-supervised-learning -- 1회. 레이블 없이 데이터 구조에서 학습
38. active-learning -- 1회. 불확실한 샘플 우선 레이블링
39. nucleus-sampling-top-p -- top-p 샘플링 상세
40. beam-search -- 빔 탐색 디코딩 전략

### 아키텍처 (architectures, 5개)
41. diffusion-transformer (DiT) -- Stable Diffusion 3/Flux 핵심 아키텍처
42. vision-transformer (ViT) -- 이미지를 패치로 분할하여 Transformer에 입력
43. u-net -- Diffusion 모델의 노이즈 예측 네트워크
44. residual-connection -- skip connection, 깊은 네트워크 학습 안정화
45. attention-sink -- 첫 토큰에 어텐션이 집중되는 현상

### 응용 (applications, 3개)
46. semantic-search -- 의미 기반 검색 (키워드가 아닌 벡터)
47. text-classification -- NLP 기본 태스크. 감정분석, 스팸 필터 등
48. named-entity-recognition -- 개체명 인식 (NER)

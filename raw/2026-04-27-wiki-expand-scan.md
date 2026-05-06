# Wiki Expand Scan Report - 2026-04-27

## 스캔 메타
- 위키 총 페이지: 1,717
- wikilink 타겟: 2,113 (unique)
- 깨진 wikilink: 440개
- 스캔 대상: 빈도 ≥ 1 깨진 wikilink

## 생성 후보 30개 (빈도순)

### 빈도 5 이상 (필수)
1. github-copilot | GitHub Copilot | tooling | entity | 12회 -- AI 코딩 도구 시초, 모든 코딩 도구 페이지에서 비교 대상
2. time-series-forecasting | 시계열 예측 | concepts | concept | 11회 -- 공급망/에너지/예측유지보수 등 다수 응용에서 참조
3. multimodal-llm | 멀티모달 LLM | architectures | concept | 8회 -- BLIP/LLaVA/Flamingo/KOSMOS/Fuyu 등 여러 페이지에서 참조
4. vllm | vLLM 추론 엔진 | tooling | entity | 7회 -- LLM 서빙 표준, 다수 inference 페이지에서 비교
5. digital-twin | 디지털 트윈 | concepts | concept | 6회 -- 도시계획/유지보수/제조 응용 페이지에서 참조
6. llm-as-judge | LLM-as-Judge 평가 | concepts | concept | 5회 -- self-preference-bias 등에서 참조
7. cursor-editor | Cursor AI 에디터 | tooling | entity | 5회 -- 다수 코딩 도구 페이지 참조
8. ai-accelerators | AI 가속기 | tooling | concept | 5회 -- Cerebras/SambaNova/d-Matrix 페이지에서 참조
9. transformer | Transformer 아키텍처 일반 개요 | architectures | concept | 5회 -- 변형(transformer-architecture)이 없을 때 hub
10. lora | LoRA 일반 개요 | training | concept | 4회 -- DoRA/AdaLoRA 통합 개요

### 빈도 3 이상
11. rlhf | RLHF 일반 개요 | training | concept | 3회 -- DPO/SimPO/IPO 등 정렬 기법 hub
12. mcmc | Markov Chain Monte Carlo | foundations | concept | 3회 -- 베이지안/SGLD 페이지에서 참조
13. gemini-models | Gemini 모델 패밀리 hub | tooling | entity | 3회 -- 여러 페이지에서 참조
14. evaluation-bias | 평가 편향 일반 | concepts | concept | 3회 -- self-preference-bias에서 참조
15. sentence-transformer | Sentence Transformer (SBERT) | architectures | concept | 3회 -- 임베딩/RAG 페이지 참조
16. fine-tuning | 파인튜닝 일반 개요 | training | concept | 3회

### 빈도 2 이상
17. ab-testing | A/B 테스팅 일반 | concepts | concept | 3회
18. two-tower-model | 두 타워 모델 일반 | architectures | concept | 2회
19. kv-cache-optimization | KV 캐시 최적화 일반 | inference | concept | 2회
20. image-classification | 이미지 분류 일반 | concepts | concept | 2회
21. function-calling | 함수 호출 일반 | agents | concept | 2회
22. dspy | DSPy 프레임워크 entity | tooling | entity | 2회 (dspy-framework.md 있으나 일반 entity 별도 가치)
23. code-completion | 코드 완성 일반 | applications | concept | 2회
24. ai-alignment | AI 정렬 일반 | concepts | concept | 2회
25. long-context | 긴 컨텍스트 일반 | concepts | concept | 2회
26. kernel-methods | 커널 방법 | foundations | concept | 2회
27. mcp | Model Context Protocol entity | tooling | entity | 2회
28. user-modeling | 사용자 모델링 | concepts | concept | 2회
29. image-captioning | 이미지 캡셔닝 일반 | applications | concept | 2회
30. quantization | 양자화 일반 | inference | concept | 2회

## 제외 사유 (생성 안 함)

- `lora` 변형: lora-qlora-finetuning.md 존재 → 일반 hub로 신규 생성
- `cursor-editor`: cursor.md 존재 → 별칭 깨진 링크. 이번 expand 대상에서 제외 (링크 수정으로 해결)
- `vit`, `vae`: 변형 페이지 존재
- `recommendation-systems`: ai-recommendation-systems.md 존재
- `image-captioning`: image-captioning-architecture.md 존재 → 일반 응용 hub로 신규 생성
- `function-calling`: function-calling-tool-use.md 존재 → 일반 hub로 신규 생성

## 실행 계획

5 병렬 sonnet 에이전트 × 6 페이지 = 30 페이지

| Agent | 슬러그 |
|-------|--------|
| #1 | github-copilot, time-series-forecasting, multimodal-llm, vllm, digital-twin, llm-as-judge |
| #2 | ai-accelerators, rlhf, mcmc, gemini-models, evaluation-bias, sentence-transformer |
| #3 | ab-testing, two-tower-model, kv-cache-optimization, image-classification, function-calling, dspy |
| #4 | code-completion, ai-alignment, long-context, kernel-methods, mcp, word-embeddings |
| #5 | user-modeling, lora, image-captioning, quantization, fine-tuning, transformer |

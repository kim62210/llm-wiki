---
source: /wiki-expand scan (ML training deep-dive 기반 3차)
date: 2026-04-14
description: 신규 50페이지 + 전체 위키 고빈도 미등록 용어 15개 발굴
---

# Wiki Expand 3차 스캔 결과 (2026-04-14)

ML 학습 방법론 50페이지 생성 후, 위키 내부에서 자주 참조되지만 전용 페이지가 없는 용어 15개 발굴.

## 생성 대상 (15개)

### architectures (3개)
1. rotary-position-embedding -- RoPE, 15개 페이지에서 언급. 위치 인코딩의 현대적 표준
2. rmsnorm -- RMS Normalization, 7개 페이지. Llama/DeepSeek 등 현대 LLM 기본 정규화
3. bert -- BERT 모델 엔티티, NLP 사전학습 혁명. BERTScore 페이지만 있고 BERT 자체 없음

### foundations (1개)
4. cross-entropy-loss -- 11개 페이지. LLM 학습의 기본 목적함수

### training (2개)
5. adamw-optimizer -- 8개 페이지. Transformer 학습의 사실상 표준 옵티마이저
6. chinchilla-scaling-laws -- Chinchilla 논문, 컴퓨트 최적 학습의 전환점

### training/entity (1개)
7. commoncrawl -- 6개 페이지. 대부분 LLM 학습 데이터의 원천

### tooling/entity (8개)
8. nccl -- 11개 페이지. NVIDIA 분산 학습 통신 라이브러리
9. megatron-lm -- 9개 페이지. NVIDIA 대규모 모델 학습 프레임워크
10. triton-openai -- 7개 페이지. OpenAI GPU 커널 컴파일러 (Unsloth 등 사용)
11. ray-distributed -- 5개 페이지. 분산 컴퓨팅 (OpenRLHF/veRL 기반)
12. wandb -- Weights & Biases 실험 추적 도구
13. llama-cpp -- llama.cpp 로컬 추론/양자화 도구
14. langchain -- LangChain 에이전트/LLM 프레임워크
15. alpacaeval -- AlpacaEval 평가 벤치마크

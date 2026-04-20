# Wiki Expand Scan 2026-04-16

## 스캔 환경
- 기존 페이지: ~790개
- 전체 wikilink 타겟: 797개 고유
- 깨진 wikilink: 120개 (대부분 대소문자/이스케이프 문제)

## 깨진 wikilink (실제 누락)
- rag-pipeline (5 파일, 4 wikilinks)
- rl-for-agents (4 파일) -> long-horizon-rl-training과 유사하지만 일반 RL 적용
- Showboat/Rodney (각 6/5 refs) -> Simon Willison 도구, 이미 browser-automation에서 설명

## 고빈도 미등록 용어 (확정 생성 대상 12개)

| 순위 | 용어 | 언급 파일 | 카테고리 | 타입 | 근거 |
|------|------|----------|---------|------|------|
| 1 | system-prompt | 12 | concepts | concept | 프론티어 모델 사용의 기초. 프롬프트 엔지니어링과 별개 |
| 2 | rag-pipeline | 5+4wl | rag | concept | RAG 파이프라인 설계/최적화. 기존 agentic-rag과 별개 |
| 3 | extended-thinking | 7 | concepts | concept | 2026 추론 모델 핵심 기능. 테스트 타임 컴퓨트와 구현 관점 차이 |
| 4 | memorization-in-llms | 7 | concepts | concept | 프라이버시/보안 관점 LLM 기억 문제 |
| 5 | compute-optimal-training | 6 | training | concept | Chinchilla 이후 최적 배분 전략 |
| 6 | data-annotation | 5 | training | concept | 레이블링/어노테이션 파이프라인 |
| 7 | grounding-attribution | 4 | concepts | concept | 생성 근거 추적, 인용, 환각 방지 |
| 8 | web-agent | 3 | agents | concept | 브라우저 기반 자율 에이전트 |
| 9 | bi-encoder-cross-encoder | 3 | rag | concept | 검색 아키텍처 2대 패러다임 |
| 10 | lmsys-chatbot-arena | 3 | tooling | entity | LMSYS 벤치마크/아레나 허브 |
| 11 | model-serving | 2 | inference | concept | 추론 서빙 패턴 (vLLM/SGLang 상위 개념) |
| 12 | open-weights-movement | 2 | concepts | concept | 오픈 웨이트 vs 오픈소스 구분 |

## 제외 (기존 페이지 보강으로 충분)
- RLHF, Transformer, DPO, BERT 등: 대소문자 alias 문제
- tokenization, few-shot, zero-shot: 전용 페이지 이미 존재
- ai-safety: 다수 하위 페이지로 충분히 커버
- reward-model: reward-model-training.md 존재
- speculative-decoding, kv-cache 등: 전용 페이지 존재

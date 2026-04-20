---
source: /sciomc AUTO 7-stage parallel research
date: 2026-04-14
description: ML 모델 학습 방법론 심층 조사 -- 7개 스테이지, 70+ 토픽, 200+ URL
---

# ML 모델 학습 심층 조사 결과 (2026-04-14)

7개 병렬 리서치 에이전트가 수집한 학습 관련 심층 토픽과 소스.
기존 위키 52개 training 페이지를 제외한 신규 위키화 후보.

## 위키화 후보 토픽 목록 (중복 제거 후 ~50개)

### A. 사전학습 파이프라인 (6개)
1. pretraining-pipeline-e2e -- LLM 사전학습 전체 흐름 허브 페이지 (데이터->토크나이저->학습->평가)
2. training-stability -- loss spike 원인/해결, z-loss, QK-Norm, SPAM optimizer
3. batch-size-scheduling -- 배치 사이즈 점진 증가 전략 (BSS, Llama/DeepSeek 사례)
4. sequence-length-curriculum -- 시퀀스 길이 점진 확장 학습
5. data-mixing-laws -- 도메인 배합 비율의 예측 가능한 법칙 (DoReMi 확장)
6. mfu-model-flops-utilization -- 하드웨어 활용률 측정/최적화

### B. 데이터 파이프라인 (7개)
7. fineweb-dataset -- HuggingFace 15T 토큰 영어 웹 데이터셋
8. redpajama-v2 -- Together AI 30T+ 토큰 + 품질 시그널
9. dolma-dataset -- AI2 3T 토큰 OLMo 학습용
10. dclm-datacomp -- 데이터 큐레이션 벤치마크 프레임워크
11. datatrove -- HuggingFace 대규모 데이터 처리 라이브러리
12. text-dedup -- MinHash/SimHash/Exact 중복제거 도구
13. model-collapse-synthetic -- AI 생성 데이터 반복 학습 시 분포 붕괴

### C. Post-training 파이프라인 (6개)
14. post-training-pipeline-e2e -- SFT->RM->RLHF/DPO->Safety 전체 흐름 허브
15. alignment-tax -- 안전 학습으로 인한 성능 저하와 최소화 기법
16. safety-training-refusal -- 유해 출력 거부 학습, over-refusal, calibrated refusal
17. online-dpo-iterative -- DPO의 offline 한계 극복, on-policy 데이터 생성 반복
18. orpo -- SFT+선호도 최적화 통합 (Hong et al. 2024)
19. kto -- 쌍이 아닌 개별 좋음/나쁨 라벨 최적화 (Ethayarajh et al. 2024)

### D. 기술 보고서 (7개)
20. llama-3-training -- Meta 405B 학습 상세 (4D 병렬, 15.6T 토큰, 6라운드 PT)
21. deepseek-v3-training -- 671B MoE, FP8, 보조손실 없는 부하분산, $5.6M
22. qwen-25-training -- 18T 토큰, 다국어, 4단계 long-context
23. olmo-2-training -- 완전 오픈소스 2단계 커리큘럼, 모델 수핑
24. gemma-2-training -- On-policy knowledge distillation, sliding+global attention
25. phi-4-training -- 합성 데이터 40%, PTS DPO, 교사 모델 초월
26. mixtral-training -- Sparse MoE, 자연적 부하분산, top-2 라우팅

### E. 최신 논문 & 기법 (10개)
27. bitnet-1bit-training -- 1.58-bit 네이티브 LLM 학습 (Microsoft)
28. fp4-training -- NVFP4/Quartet 네이티브 4-bit 학습
29. grokking-training-dynamics -- 학습 동역학, 위상 전이, emergent abilities 통합
30. data-attribution-influence -- Data Shapley, TrackStar, 학습 데이터 영향 분석
31. learning-dynamics-finetuning -- SFT/DPO 파인튜닝 학습 동역학 (ICLR 2025 수상)
32. continual-pretraining -- LR re-warming + replay로 scratch 재학습 없는 도메인 적응
33. ast-fim-code-training -- AST 기반 구조 인식 코드 FIM 학습
34. communication-efficient-training -- SparseLoCo, EDGC 통신 효율 분산 학습
35. omni-modal-training -- 텍스트/이미지/비디오/오디오 통합 학습 전략
36. sparse-bitnet -- 1.58-bit + N:M sparsity 결합

### F. 실전 도구 & 프레임워크 (7개)
37. trl-library -- HuggingFace TRL v1.0 포스트트레이닝 풀스택
38. axolotl -- YAML 기반 파인튜닝 프레임워크
39. llama-factory -- 100+ 모델 통합 파인튜닝 (70K+ stars)
40. unsloth -- 2x 속도, 70% 메모리 절감 파인튜닝
41. openrlhf -- 분산 RLHF 프레임워크 (Ray+vLLM)
42. verl-bytedance -- ByteDance RL 학습 프레임워크 (DAPO)
43. llm-training-cost-guide -- 모델 크기별 학습 비용 가이드

### G. 학습 인프라 & 모니터링 (7개)
44. loss-spike-debugging -- loss spike 진단, 데이터 스킵, 롤백 전략
45. gradient-norm-monitoring -- gradient explosion 탐지, per-layer 추적
46. nan-inf-debugging -- NaN/Inf 디버깅, mixed-precision 수치 안정성
47. training-resumption -- 체크포인트 안전 재개, 옵티마이저/RNG 복원
48. elastic-training -- 노드 실패 대응, TorchElastic, 탄력적 학습
49. training-profiling -- torch.profiler, Nsight Systems, 통신/연산 오버랩
50. training-learning-guides -- mlabonne/llm-course, smol-course, Raschka 책 등 학습 경로

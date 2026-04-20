---
source: ML foundations gap analysis (4 parallel agents)
date: 2026-04-14
description: ML 기초/학습/평가/거버넌스 누락 토픽 ~95개 + 위키 연결성 감사 결과
---

# ML 기초 & 위키 구조 개선 소스 (2026-04-14)

## 진단 결과 요약

### 콘텐츠 갭
- foundations 카테고리: 0페이지 (수학/통계/ML 기초 전무)
- architectures 기초: 0페이지 (Transformer, Attention, MoE 등 없음)
- training 기초: 0페이지 (SFT, RLHF, DPO 등 없음)
- 평가 메트릭 기초: 0페이지 (BLEU, MMLU, perplexity 등 없음)
- 거버넌스/운영: 0페이지 (Model Cards, NIST AI RMF, fairness 등 없음)

### 연결성 문제
- 49.2% 페이지 본문 인라인 링크 0개 (하단 "관련 문서"에만 링크)
- 22개 고아 페이지 (들어오는 링크 0)
- 42개 깨진 링크
- 91.3% 페이지 보일러플레이트 오염
- training<->agents, architectures<->agents 교차 링크 0개

---

## A. ML 수학 기초 (5개)

1. linear-algebra-for-ml -- ML 핵심 선형대수 (벡터, 행렬, SVD, 고유값 분해)
2. probability-statistics-for-ml -- 베이즈 정리, 확률분포, MLE, 기대값
3. optimization-theory -- 볼록 최적화, SGD 변형, 학습률 스케줄링
4. loss-functions -- Cross-entropy, MSE, Focal Loss 등 목적함수
5. gradient-descent-backpropagation -- 자동 미분, 연쇄 법칙, 기울기 소실/폭발

## B. 핵심 ML 개념 (5개)

6. supervised-unsupervised-reinforcement -- ML 3대 패러다임
7. bias-variance-tradeoff -- 과소/과대적합 균형과 일반화
8. overfitting-regularization -- L1/L2, 조기 종료, 데이터 증강
9. cross-validation-model-evaluation -- K-fold CV, Precision/Recall/F1, AUC-ROC
10. feature-engineering -- 특성 선택, 차원 축소, 인코딩, 스케일링

## C. 신경망 기초 (5개)

11. perceptron-mlp -- 단일 뉴런에서 다층 퍼셉트론, 범용 근사 정리
12. activation-functions -- Sigmoid, ReLU, GELU, SiLU/Swish
13. batch-norm-layer-norm -- 정규화 기법 원리와 차이 (BatchNorm, LayerNorm, RMSNorm)
14. dropout -- 무작위 뉴런 비활성화로 과적합 방지
15. weight-initialization -- Xavier, He, LSUV 초기화

## D. 전통 ML 모델 (5개)

16. decision-trees-random-forests -- 정보이득, 배깅, XGBoost, LightGBM
17. support-vector-machines -- 마진 최대화, 커널 트릭
18. k-means-clustering -- 비지도 군집화
19. pca -- 주성분 분석, 차원 축소
20. logistic-regression -- 선형 분류 기초, 시그모이드

## E. 딥러닝 아키텍처 기초 (5개)

21. cnn -- 합성곱 신경망 (LeNet->ResNet->EfficientNet)
22. rnn-lstm-gru -- 순환 신경망, 장기 의존성, 게이트 메커니즘
23. autoencoders-vae -- 비지도 표현 학습, 잠재 공간, 확률적 생성
24. gans -- 생성자-판별자 경쟁, 모드 붕괴
25. diffusion-models -- DDPM/DDIM, Stable Diffusion 기초

## F. Transformer 핵심 (7개)

26. transformer-architecture -- "Attention Is All You Need" 원본 구조
27. self-attention-mechanism -- Q/K/V, Scaled Dot-Product Attention
28. multi-head-attention -- 다양한 관계 패턴 포착, 헤드 프루닝
29. positional-encoding -- 사인/코사인, RoPE, ALiBi
30. transformer-ffn -- SwiGLU/GeGLU, FFN as Key-Value Memories
31. pre-ln-vs-post-ln -- 레이어 정규화 위치별 학습 안정성
32. encoder-decoder-architectures -- BERT/GPT/T5 구조적 차이

## G. 효율적 어텐션 & 확장 (5개)

33. kv-cache-inference -- 자기회귀 캐싱, Paged Attention (기존 kv-cache 보강)
34. sparse-attention-patterns -- Longformer, BigBird 등 O(n^2) 해결
35. mixture-of-experts -- 게이팅, Switch Transformer, Mixtral
36. flash-attention-fundamentals -- IO-aware, 타일링 (기존 flashattention-4의 기초)
37. gqa-mqa -- Grouped/Multi-Query Attention (MLA의 선수 지식)

## H. 토크나이제이션 & 임베딩 (4개)

38. tokenization-bpe-sentencepiece -- 서브워드 분할 알고리즘
39. embedding-layers -- 이산 토큰 -> 연속 벡터
40. word2vec-pretrained-embeddings -- CBOW, Skip-gram, GloVe, FastText
41. contextual-embeddings -- ELMo, BERT, 사전학습-파인튜닝 패러다임

## I. 학습 기초 (18개)

42. causal-language-modeling -- CLM, GPT 계열 사전학습 목적함수
43. masked-language-modeling -- MLM, BERT 계열 양방향 학습
44. neural-scaling-laws -- Kaplan, Chinchilla 멱법칙
45. pretraining-data-curation -- 웹 크롤 필터링, 중복 제거, 품질 분류
46. tokenizer-training -- BPE/WordPiece/Unigram 학습 방법
47. supervised-fine-tuning -- SFT, instruction-response 지도학습
48. instruction-tuning -- FLAN, 자연어 지시문 zero-shot 일반화
49. transfer-learning-for-nlp -- ULMFiT, 사전학습-미세조정 패러다임
50. multi-task-learning -- T5, 여러 태스크 동시 학습
51. rlhf-pipeline -- 보상 모델 + PPO + KL 페널티 전체 파이프라인
52. direct-preference-optimization -- DPO, SimPO, KTO
53. preference-data-collection -- 인간 비교 데이터 수집/관리
54. rlaif-scalable-oversight -- AI 피드백, debate, recursive reward
55. data-mixing-curriculum-learning -- DoReMi, 데이터 도메인 비율 + 커리큘럼
56. data-decontamination -- 벤치마크 데이터 누출 방지
57. evaluation-during-training -- loss curve, perplexity, eval harness
58. reward-model-training -- Bradley-Terry, 보상 해킹
59. kl-divergence-penalty -- RLHF 정책 이탈 정규화

## J. 학습 인프라 (12개)

60. data-parallelism-fsdp -- DP, DDP, PyTorch FSDP
61. tensor-pipeline-parallelism -- Megatron-LM 텐서/파이프라인 병렬
62. deepspeed-zero -- ZeRO 1/2/3, Infinity
63. mixed-precision-training -- FP16, BF16, FP8, AMP
64. gradient-accumulation-checkpointing -- 큰 배치 구현, 활성값 재계산
65. model-checkpointing-sharding -- 체크포인트 저장/복구, 샤딩
66. gpu-cluster-scheduling -- Slurm, Kubernetes, 장애 복구, 탄력적 학습
67. training-frameworks -- PyTorch, JAX, Megatron-LM, NeMo
68. experiment-tracking -- W&B, MLflow, Neptune
69. optimizer-selection -- Adam, AdamW, Lion, Sophia
70. learning-rate-scheduling -- Warmup, cosine decay, WSD
71. distributed-communication -- NCCL, Gloo, all-reduce, all-gather

## K. 평가 메트릭 기초 (15개)

72. perplexity -- 언어모델 기본 지표
73. bleu -- 기계번역 n-gram 정밀도
74. rouge -- 요약 n-gram 재현율
75. bertscore -- BERT 임베딩 의미적 유사도
76. mmlu -- 57개 학문 분야 다지선다
77. humaneval -- 코드 생성 pass@k
78. gsm8k -- 초등 수학 추론
79. truthfulqa -- 진실성 평가
80. mt-bench -- 다중 턴 대화 LLM 판정
81. classification-metrics -- Precision, Recall, F1, AUC-ROC, Confusion Matrix
82. benchmark-contamination -- 데이터 누출 탐지
83. benchmark-saturation-goodharts-law -- 포화, 측정 대상이 목표가 되는 문제
84. ab-testing-llms -- LLM A/B 테스트 통계적 유의성
85. human-evaluation-protocols -- 인간 평가 설계/실행/신뢰도
86. evaluation-harness -- lm-evaluation-harness, OpenAI Evals

## L. 거버넌스 & 운영 (15개)

87. model-cards -- 모델 문서화 표준 (Mitchell et al.)
88. datasheets-for-datasets -- 데이터셋 문서화 (Gebru et al.)
89. nist-ai-rmf -- AI 위험 관리 프레임워크 4단계
90. iso-42001 -- AI 관리체계 인증 표준
91. fairness-metrics-bias-auditing -- 공정성 정량 측정, 편향 감사
92. responsible-ai-practices -- 윤리적 AI 개발/배포 원칙
93. model-lifecycle-management -- 버전 관리, 모니터링, 폐기
94. token-economics -- 토큰 비용, 캐싱, 배치, 모델 선택
95. batch-inference-caching -- 대량 추론, 응답 캐싱
96. ai-observability-patterns -- 로깅, 트레이싱, 모니터링 아키텍처 (도구가 아닌 패턴)
97. ai-incident-response -- AI 장애 대응 절차, 사후 분석
98. prompt-management-versioning -- 프로덕션 프롬프트 버전 관리
99. ai-supply-chain-security -- 모델/데이터셋 공급망 보안
100. ai-red-teaming-methodology -- 적대적 테스트 방법론 (도구가 아닌 개념)

---

## 위키 연결성 개선 계획

### 필요한 허브 페이지 (5개)
1. reinforcement-learning-for-llm -- training 허브: RLVR, GRPO, DAPO, PRM 연결
2. transformer-attention-mechanisms -- architectures 허브: MHA, MLA, GQA, KV, FA 연결
3. agent-protocols-and-standards -- agents 허브: A2A, ACP, MCP, AAIF 연결
4. ai-benchmarks-overview -- 벤치마크 허브: SWE-bench, HLE, BrowseComp 등 연결
5. coding-agents-landscape -- tooling 허브: Claude Code, Codex, Copilot 등 비교

### 즉시 수정 필요
- 42개 깨진 링크 수정
- 22개 고아 페이지에 역링크 추가
- 193개 페이지에 인라인 [[wikilink]] 추가 (하단만 -> 본문에도)
- 358개 페이지의 보일러플레이트 정리

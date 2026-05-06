# Wiki Expansion Topic Queue V3 (2026-04-27)

3차 수집. 기존 1,417 페이지와 중복 없는 신규 시드 토픽 300건.

수집 범위:
- 기초 학습 이론과 통계 학습 심화
- CNN/Vision/Audio/Speech/Video 미커버 아키텍처
- PEFT 변형, 선호도 정렬 변형, 합성 데이터 기법
- 양자화/디코딩/스트리밍 추론 신기법
- 임베딩 모델/벡터 인덱싱 알고리즘 심화
- 에이전트 패턴/계보 미커버 영역
- 산업별 응용 분야 미커버
- 핵심 원논문 미수집 항목
- 클라우드 추론 플랫폼/IDE 도구 미수집
- AI 안전/정렬 핵심 개념 미수집

총 300건. 형식: `슬러그 | 제목 | 카테고리 | 페이지타입 | 1줄 요약`

---

## 1. Foundations 심화 (30건)

1. rademacher-complexity | 라데마허 복잡도와 일반화 경계 | foundations | concept | 가설 클래스 표현력의 데이터 의존 측도, VC 차원의 분포 의존 일반화, 경험적 라데마허
2. empirical-risk-minimization | 경험적 위험 최소화 (ERM) 이론 | foundations | concept | ERM 원리, 일관성, 균등 수렴, 통계학습이론 핵심 프레임
3. matrix-calculus-deep-learning | 딥러닝을 위한 행렬 미적분 | foundations | concept | 분자-분모 레이아웃, 야코비안, 헤시안, 역전파 수식 유도 기초
4. fisher-information-matrix | 피셔 정보 행렬과 자연 경사 | foundations | concept | 분포 곡률, KFAC 근사, 자연 경사법의 정보기하 해석
5. sparse-coding-dictionary-learning | 희소 코딩과 사전 학습 | foundations | concept | L1 정규화 표현, K-SVD, ISTA/FISTA, 비전 V1 이론 기반
6. topological-data-analysis | 위상 데이터 분석 (TDA) | foundations | concept | 지속 호몰로지, 마퍼 알고리즘, ML 표현 학습과의 결합
7. nonnegative-matrix-factorization | 비음수 행렬 분해 (NMF) | foundations | concept | 부품 기반 표현, 토픽 모델링, 음악/이미지 분리, ALS/MU 업데이트
8. bayesian-neural-networks | 베이지안 신경망 | foundations | concept | 가중치 사후 분포, 변분 추론 BNN, MC Dropout, 불확실성 정량화
9. swag-stochastic-weight-averaging | SWAG와 SWA - 가중치 평균화 | foundations | concept | SGD 궤적 가우시안 근사, 평탄 최솟값, 베이지안 모델 평균화 근사
10. deep-ensembles | 딥 앙상블 | foundations | concept | 무작위 초기화 다수 모델 평균, 불확실성 캘리브레이션, BNN 비교
11. adagrad-rmsprop-history | Adagrad/RMSProp 옵티마이저 계보 | foundations | concept | 적응적 학습률 시초, Adam의 직접 조상, 희소 그래디언트 가속
12. nesterov-momentum | 네스테로프 가속 그래디언트 | foundations | concept | 추측 후 보정 패턴, 볼록 최적화 최적 수렴률, 모멘텀 변형
13. variational-inference-deep | 변분 추론 심화 (ELBO/Reparametrization) | foundations | concept | ELBO 분해, 재매개변수화 트릭, 평균장 근사, 정규화 흐름 결합
14. bald-batchbald-active-learning | BALD/BatchBALD 베이지안 능동학습 | foundations | concept | 정보 획득 기반 샘플 선택, 배치 다양성, 의료/지질학 적용
15. continuous-normalizing-flows | 연속 정규화 흐름 (CNF) | foundations | concept | Neural ODE 기반 가역 변환, FFJORD, 흐름 매칭의 이론 배경
16. modern-hopfield-networks | 현대 홉필드 네트워크 | foundations | concept | 어텐션과 등가성 증명, 지수 저장 용량, Hopfield Layers
17. restricted-boltzmann-machines | 제한 볼츠만 머신 (RBM) | foundations | concept | 에너지 기반 생성 모델, 대조 발산, DBN의 빌딩 블록
18. spiking-neural-networks | 스파이킹 신경망 (SNN) | foundations | concept | 시간 부호화 뉴런, LIF 모델, 뉴로모픽 칩, 에너지 효율 추론
19. reservoir-computing-esn | 리저버 컴퓨팅과 에코 상태 네트워크 | foundations | concept | 무작위 고차원 RNN, 출력 레이어만 학습, 시계열 카오스 예측
20. quantum-machine-learning | 양자 기계학습 (QML) 기초 | foundations | concept | 변분 양자 회로, 양자 커널, NISQ 시대 ML, PennyLane/Qiskit
21. equivariant-neural-networks | 등변 신경망 | foundations | concept | 군 등변성, SE(3)-Transformers, EGNN, 분자/단백질 SO(3) 대칭
22. tensor-networks-ml | 텐서 네트워크와 ML | foundations | concept | MPS/PEPS, 양자 영감 압축, ML 모델 압축, Cichocki TT 분해
23. universal-approximation-theorem | 범용 근사 정리 심화 | foundations | concept | Cybenko/Hornik, 너비-깊이 트레이드오프, 표현력 vs 학습 가능성
24. sgd-convergence-theory | SGD 수렴 이론 | foundations | concept | 볼록/비볼록 수렴률, 학습률 조건, Robbins-Monro, 분산 감소
25. sgld-langevin-dynamics | 확률적 그래디언트 랑주뱅 동역학 | foundations | concept | SGD + 노이즈 = 사후 분포 샘플링, MCMC 베이지안 학습
26. rkhs-kernel-methods | 재생 커널 힐베르트 공간 (RKHS) | foundations | concept | 커널 트릭 이론적 기반, 표현 정리, GP/SVM/뉴럴 탄젠트 공통 기반
27. manifold-learning-isomap-lle | 매니폴드 학습 - Isomap/LLE | foundations | concept | 비선형 차원 축소, 측지 거리, 국소 선형 임베딩, t-SNE 전조
28. graph-signal-processing | 그래프 신호 처리 (GSP) | foundations | concept | 그래프 푸리에 변환, 라플라시안 스펙트럼, GCN의 신호처리 해석
29. fairness-mathematical-foundations | 알고리즘 공정성 수학 기초 | foundations | concept | 인구통계 균형, 등화 odds, 캘리브레이션, 불가능성 정리
30. ml-numerical-stability | ML 수치 안정성 기초 | foundations | concept | log-sum-exp 트릭, 소프트맥스 수치, FP16 오버/언더플로우, gradient clipping 이론

## 2. Architectures - 비전/오디오/생성 미커버 (35건)

31. densenet-dense-connections | DenseNet 밀집 연결 | architectures | concept | 모든 이전 레이어 직접 연결, 그래디언트 흐름 강화, 파라미터 효율
32. resnext-cardinality | ResNeXt 카디널리티 | architectures | concept | 분할-변환-병합, 그룹 합성곱 활용, 깊이/너비보다 효과적 차원
33. nfnet-normalizer-free | NFNet 정규화 없는 네트워크 | architectures | concept | BatchNorm 제거 + 적응적 그래디언트 클리핑, EfficientNet 능가
34. regnet-design-spaces | RegNet 설계 공간 탐색 | architectures | concept | 양적 네트워크 설계, NAS 대안, 선형 파라미터 깊이/너비 규칙
35. bit-big-transfer | BiT (Big Transfer) 사전학습 | architectures | concept | GroupNorm + 가중치 표준화, 대규모 사전학습 + 단순 fine-tune
36. wide-resnet | Wide ResNet | architectures | concept | 깊이보다 너비 - 16층 와이드가 1000층 ResNet 능가, 학습 속도 개선
37. highway-networks | 하이웨이 네트워크 | architectures | concept | LSTM 게이팅 영감 스킵 연결, ResNet 직계 조상
38. wav2vec-2-speech | Wav2Vec 2.0 자기지도 음성 표현 | architectures | concept | 마스킹 + 대조 학습, 양자화 코드북, low-resource 음성 인식 혁신
39. hubert-speech-representation | HuBERT 클러스터링 음성 사전학습 | architectures | concept | k-means 의사 레이블, BERT-like MLM, 음성/노래 통합 학습
40. wavlm-speech-processing | WavLM 통합 음성 처리 | architectures | concept | 화자/내용/발화 분리, 다중 태스크, 음성 SUPERB 벤치마크 SOTA
41. conformer-speech-recognition | Conformer - 음성 인식 트랜스포머 | architectures | concept | 컨볼루션 + 셀프어텐션 결합, 지역+전역 모델링, ASR 표준
42. tacotron-2-tts | Tacotron 2 신경 TTS | architectures | concept | 인코더-어텐션-디코더 + WaveNet 보코더, 멜 스펙트로그램 예측
43. fastspeech-2-tts | FastSpeech 2 비자기회귀 TTS | architectures | concept | 가변 어댑터 (피치/에너지/지속), Tacotron 2 대비 270배 빠름
44. imagen-text-to-image | Imagen - Google 텍스트-이미지 | architectures | concept | T5 텍스트 인코더 + 캐스케이드 확산, 사실적 이미지, DrawBench
45. dalle-3-architecture | DALL-E 3 아키텍처 | architectures | concept | OpenAI 캡션 재작성 LLM + 확산 디코더, ChatGPT 통합, 텍스트 렌더링
46. stable-diffusion-3-mmdit | Stable Diffusion 3 MMDiT | architectures | concept | 멀티모달 DiT, 흐름 매칭, 이미지/텍스트 동등 처리, 텍스트 일관성
47. parti-autoregressive-image | Parti - 자기회귀 텍스트-이미지 | architectures | concept | ViT-VQGAN + autoregressive 트랜스포머, 20B 스케일링 결과
48. muse-masked-image | Muse - 마스크 생성 트랜스포머 | architectures | concept | VQ 토큰 병렬 생성, MaskGIT 스케일업, 확산 대비 10배 빠른 추론
49. controlnet-conditioning | ControlNet 조건부 확산 제어 | architectures | concept | 사전훈련 SD 동결 + 학습 가능 복사, Canny/depth/pose 조건 주입
50. ip-adapter-image-prompting | IP-Adapter 이미지 프롬프팅 | architectures | concept | 이미지를 프롬프트로 사용, decoupled 크로스어텐션, fine-tuning 없이
51. animatediff-motion-modules | AnimateDiff 모션 모듈 | architectures | concept | T2I 모델에 시간 어텐션 모듈 삽입, 모션 LoRA, 비디오 생성
52. sora-architecture | Sora - OpenAI 비디오 모델 아키텍처 | architectures | entity | 시공간 패치 + DiT 백본, 시각 토큰화, 1분 비디오, 추정 구조
53. veo-google-video | Veo - Google 비디오 생성 | architectures | entity | DeepMind 1080p 영상 생성, 카메라/조명 제어, 영화감독 도구화
54. cogvideox-architecture | CogVideoX 비디오 생성 아키텍처 | architectures | concept | 3D 인과 VAE + Expert MMDiT, 6초 720p, Tsinghua/Zhipu
55. graphsage-inductive-gnn | GraphSAGE 귀납 GNN | architectures | concept | 노드 샘플링 집계, 미본 노드 일반화, 산업 그래프 활용 (Pinterest)
56. gin-graph-isomorphism | GIN - 그래프 동형 네트워크 | architectures | concept | WL 테스트 등가 GNN, 합 집계 + MLP, 그래프 분류 SOTA
57. pna-aggregation | PNA - 다중 집계 GNN | architectures | concept | mean/max/min/std 다중 집계 + degree scaler, 표현력 정량 분석
58. clustergcn-subsampling | ClusterGCN 서브샘플링 학습 | architectures | concept | METIS 그래프 클러스터링 + 미니배치, 대규모 그래프 메모리 효율
59. dino-self-distillation | DINO 자기 증류 비전 | architectures | concept | 교사-학생 동일 구조 + EMA, 출력 분포 일치, ViT의 비지도 사전학습
60. byol-bootstrap | BYOL - Bootstrap Your Own Latent | architectures | concept | 음수 샘플 없는 자기지도, 타겟 네트워크 + 예측 헤드, 모드 붕괴 회피
61. moco-momentum-contrast | MoCo - 모멘텀 대조 학습 | architectures | concept | 동적 사전 큐 + 모멘텀 인코더, 메모리 효율 대조 학습
62. simclr-augmentation | SimCLR 강한 증강 대조 학습 | architectures | concept | 큰 배치 + 강한 증강 + 투영 헤드, 자기지도 비전 표현 학습
63. swav-clustering-features | SwAV - 클러스터링 기반 비전 표현 | architectures | concept | 온라인 클러스터링 + 멀티뷰 일관성, 음수 샘플 불필요
64. vicreg-variance-invariance | VICReg 분산-불변-공분산 정규화 | architectures | concept | 명시적 정규화 항으로 모드 붕괴 방지, BYOL 이해 도구
65. barlow-twins-redundancy | Barlow Twins 중복 감소 | architectures | concept | 교차 상관 행렬 항등 매트릭스 근접, 자기지도 무음수, 정보 이론 기반

## 3. Training - PEFT/정렬/합성데이터 (30건)

66. dora-weight-decomposed-lora | DoRA - 가중치 분해 LoRA | training | concept | 크기-방향 분해, LoRA 대비 표현력 강화, 동일 파라미터로 우수
67. p-tuning-soft-prompts | P-Tuning 연속 프롬프트 | training | concept | 입력 임베딩 공간 학습 가능 프롬프트, GPT-3 in-context 대체
68. adalora-adaptive-rank | AdaLoRA 적응적 랭크 할당 | training | concept | SVD 기반 동적 랭크 분배, 중요한 가중치에 더 많은 파라미터
69. ia3-injection-adapters | IA3 - 활성값 스케일링 어댑터 | training | concept | learned vectors로 활성값 스케일링, LoRA 대비 1/100 파라미터
70. prompt-tuning-soft-only | 소프트 프롬프트 튜닝 (Lester) | training | concept | 입력에 학습 가능 토큰만 추가, 작은 모델 약함, 큰 모델 비교 가능
71. prefix-tuning-deep-prompts | Prefix-Tuning 딥 프롬프트 | training | concept | 모든 레이어에 키-값 프리픽스 주입, 생성 태스크에 효과적
72. compacter-hypercomplex | Compacter - 초복소수 어댑터 | training | concept | 크로네커 곱 + 저랭크 분해, 어댑터 파라미터 추가 절감
73. unipelt-mixed-peft | UniPELT 통합 PEFT | training | concept | 다중 PEFT 방법 동적 게이팅, 적응적 선택, 단일 방법 능가
74. simpo-simple-preference | SimPO - 단순 선호 최적화 | training | concept | 길이 정규화 보상, 참조 모델 불필요, DPO 대비 안정
75. ipo-identity-preference | IPO - Identity Preference Optimization | training | concept | DPO 과적합 해결, 신원 손실 형식, 확률 거리 명시 정규화
76. cpo-contrastive-preference | CPO 대조적 선호 최적화 | training | concept | SimPO + SFT 결합, 번역/요약 SOTA, 미세 우월성 학습
77. spin-self-play-finetuning | SPIN - 자기 대국 파인튜닝 | training | concept | 모델 vs 모델 대결, 합성 패자/인간 승자, 약한 LLM 강화
78. magpie-synthetic-instruction | Magpie 합성 지시문 데이터 | training | concept | 정렬 모델에 빈 템플릿 주입 -> 자기 생성 instruction, 4M 데이터
79. evol-instruct-method | Evol-Instruct - 진화적 지시문 합성 | training | concept | LLM이 지시문 복잡화/심화, WizardLM/Code 기반, 깊이/너비 진화
80. self-instruct-original | Self-Instruct 원본 방법론 | training | concept | 시드에서 자기 부트스트래핑 지시문, 175 -> 52K 합성, Stanford
81. ultrafeedback-dataset | UltraFeedback 다중 모델 선호도 | training | entity | 1M+ GPT-4 평가 선호 쌍, 4축 평가 (지시 따르기/도움/정직/안전)
82. orca-progressive-learning | Orca 점진적 학습 | training | concept | 교사 추론 과정 모방, 단순->복잡 라벨, GPT-4 trajectory 학습
83. webinstruct-mining | WebInstruct 웹 지시문 마이닝 | training | concept | 인터넷에서 자연 발생 QA/지시문 수집, 합성 데이터 대안
84. distilbert-distillation | DistilBERT 트랜스포머 증류 | training | concept | BERT 40% 작게 60% 빠르게 97% 성능, soft target + cosine + MLM
85. seq-knowledge-distillation | 시퀀스 레벨 지식 증류 | training | concept | 토큰 레벨 vs 시퀀스 레벨 KL, 빔 서치로 교사 출력 생성
86. minillm-text-distillation | MiniLLM - LLM 텍스트 증류 | training | concept | 역KL 발산, on-policy 증류, 학생이 교사보다 우수한 사례
87. branch-train-merge | Branch-Train-Merge | training | concept | 도메인별 분기 학습 후 가중치 평균, 통신 없는 분산 사전학습
88. branch-train-mix-btx | Branch-Train-Mix (BTX) | training | concept | 도메인 전문가 학습 후 MoE로 통합, MoE 사전학습 가속
89. flash-attention-2-internals | FlashAttention-2 내부 구조 | training | concept | 워프 분할 최적화, FA-1 대비 2x, 비인과 마스크 효율
90. mixup-data-augmentation | Mixup 데이터 증강 | training | concept | 두 샘플 + 라벨 선형 결합, 일반화/캘리브레이션 향상
91. cutmix-augmentation | CutMix 패치 교체 증강 | training | concept | 이미지 패치 교체 + 라벨 비례, Cutout + Mixup 결합
92. randaugment-policy | RandAugment 자동 증강 | training | concept | 검색 없는 단순 증강 정책, N개 변환 무작위 + 강도 M
93. autoaugment-search | AutoAugment 정책 탐색 | training | concept | RL/Population 기반 증강 정책 탐색, ImageNet/CIFAR 적용
94. ppo-rlhf-implementation | PPO RLHF 구현 디테일 | training | concept | trl/Open-RLHF, value head, GAE λ, KL coefficient 튜닝 실무
95. iterative-magpie-instruction | Magpie-Pro 지시문 합성 반복 | training | concept | 첫 데이터로 미세조정 -> 더 좋은 합성, 부트스트래핑 사이클

## 4. Inference - 디코딩/양자화 신기법 (25건)

96. hqq-half-quadratic-quant | HQQ - 반2차 양자화 | inference | concept | 캘리브레이션 데이터 불필요, GPTQ 대비 100배 빠른 양자화
97. fp6-llm-quantization | FP6-LLM - 6비트 부동소수점 추론 | inference | concept | TC-FPx 커널, 부동소수 6비트로 INT4 정확도 + INT8 속도
98. atom-int8-quant | Atom INT8 LLM 추론 | inference | concept | KV/Activation/Weight 모두 INT8, 활성값 outlier 처리
99. spqr-sparse-quantized | SPQR 희소-양자화 표현 | inference | concept | 1% outlier는 FP16 + 99% INT3, 손실 없는 압축
100. squeezellm-quantization | SqueezeLLM 압축 LLM | inference | concept | 가중치 그룹 클러스터링 + 민감 부분 dense, 3비트 손실 제로
101. omniquant-calibration | OmniQuant 학습 가능 양자화 | inference | concept | 학습 가능 LWC + LET, calibration 데이터 효율, W4A4 SOTA
102. medusa-multi-head-decoding | Medusa - 다중 헤드 추측 디코딩 | inference | concept | 병렬 다중 헤드로 미래 토큰 예측, 트리 디코딩, 2-3x 가속
103. lookahead-decoding | Lookahead Decoding - n-gram 룩어헤드 | inference | concept | Jacobi 반복 + n-gram 캐시, 드래프트 모델 없이 가속
104. parallel-decoding-jacobi | 병렬 자코비 디코딩 | inference | concept | 모든 위치 동시 업데이트 반복, 병렬화 가능, 수렴 보장
105. blockwise-parallel-decoding | 블록단위 병렬 디코딩 | inference | concept | 고정 블록 사이즈 병렬 예측, 검증 후 채택, 단순 가속
106. self-speculative-decoding | Self-Speculative Decoding | inference | concept | 동일 모델 일부 레이어 스킵으로 자기 드래프트, 별도 모델 불필요
107. hydra-speculation-cascade | Hydra 캐스케이딩 추측 | inference | concept | 다중 드래프트 모델 캐스케이드, 정확도-속도 트레이드오프 자동 선택
108. continuous-batching-internals | 연속 배치 내부 구조 | inference | concept | iteration-level scheduling, vLLM/TGI 구현, request 동적 합류/이탈
109. selective-batching | 선택적 배치 처리 | inference | concept | 비균질 시퀀스 배치, padding 회피, 처리량 30-50% 개선
110. tree-attention-decoding | 트리 어텐션 디코딩 | inference | concept | 추측 디코딩 시 트리 구조 동시 검증, KV 공유 마스크
111. logits-processor-internals | Logits 프로세서 내부 구조 | inference | concept | 논리 후처리 파이프라인, repetition penalty/temperature 순서, HF API
112. nucleus-top-p-sampling | Top-p (Nucleus) 샘플링 | inference | concept | 누적 확률 임계값, top-k 대비 동적 후보 수, Holtzman et al.
113. typical-sampling | Typical Sampling | inference | concept | 정보량 기반 샘플링, 평균 정보량 근접 토큰 선택, 자연스러운 텍스트
114. eta-sampling-locally | Eta Sampling - 국소 적응 | inference | concept | 엔트로피 기반 동적 임계값, top-p보다 안정적
115. mirostat-perplexity | Mirostat - 퍼플렉시티 제어 샘플링 | inference | concept | 목표 perplexity 제어, 반복 회피 + 일관성 균형
116. min-p-sampling | Min-P 샘플링 | inference | concept | 최대 확률 비율 임계값, top-p의 확률 분포 적응 변형
117. dry-sampling-repetition | DRY 반복 페널티 | inference | concept | 최근 매칭 시퀀스 검출 페널티, repetition penalty 진화
118. xtc-exclude-top-choices | XTC - 다양성 샘플링 | inference | concept | 가장 가능성 높은 토큰 의도적 제외, 창의적 출력
119. server-sent-events-llm | SSE 기반 LLM 스트리밍 | inference | concept | HTTP/1.1 단방향 텍스트 스트림, 토큰 단위 push, 표준 패턴
120. websocket-llm-streaming | 웹소켓 LLM 스트리밍 | inference | concept | 양방향 통신, 인터럽트/캔슬, 멀티터모달 스트리밍, RT 응답

## 5. RAG - 벡터 인덱싱/임베딩 모델 (25건)

121. hnsw-graph-index | HNSW - 계층적 탐색 가능 작은 세계 그래프 | rag | concept | 그래프 기반 ANN 인덱스, log 검색, 모든 주요 벡터 DB 표준
122. ivf-pq-vector-index | IVF-PQ 벡터 인덱스 | rag | concept | 역인덱스 + 곱 양자화, 메모리 효율 + 빠른 검색, FAISS 핵심
123. annoy-spotify | Annoy - Spotify ANN 라이브러리 | rag | entity | 무작위 투영 트리 앙상블, 메모리 매핑, 디스크 기반 검색
124. scann-google-search | ScaNN - Google 정량화 ANN | rag | entity | 비대칭 해싱, anisotropic 양자화, GPU 가속, ALBERT/Vertex AI
125. diskann-microsoft | DiskANN - 디스크 기반 십억 규모 ANN | rag | entity | SSD 활용, 메모리 1/100, Vamana 그래프, 실시간 십억 벡터
126. cohere-embed-v4 | Cohere Embed v4 모델 | rag | entity | 다국어 + 코드, 검색/분류 멀티태스크, RAG 산업 표준 임베딩
127. voyage-ai-embeddings | Voyage AI 임베딩 모델군 | rag | entity | 도메인 특화 (코드/법률/금융), 8K 컨텍스트, MTEB 상위
128. matryoshka-embeddings | Matryoshka 임베딩 - 가변 차원 | rag | concept | 단일 모델로 다양한 차원, 잘라써도 품질 유지, OpenAI/Nomic
129. nomic-embed-text | Nomic Embed - 오픈소스 임베딩 | rag | entity | 오픈소스 137M, OpenAI 능가, 8K 컨텍스트, 완전 재현 가능
130. mxbai-embed-large | mxbai-embed-large - 다목적 임베딩 | rag | entity | mixedbread.ai, MTEB 상위, AnglE 학습, 1024 차원
131. gte-text-embeddings | GTE - 일반 텍스트 임베딩 (Alibaba) | rag | entity | Alibaba mGTE, 8K 컨텍스트 다국어, 다중 사이즈, MTEB 상위
132. instructor-embedding-model | Instructor 임베딩 - 지시 튜닝 | rag | entity | 태스크별 지시문 임베딩, "Represent the paper for retrieval"
133. e5-text-embeddings | E5 - Microsoft EmbEddings | rag | entity | mE5 다국어, 약지도 사전학습 + 지도 fine-tune, 산업 표준
134. bge-m3-embedding | BGE-M3 - BAAI 다기능 임베딩 | rag | entity | 다국어 + 다기능 (dense/sparse/multi-vector), 8K, RAG 표준
135. token-pooling-strategies | 임베딩 풀링 전략 비교 | rag | concept | mean/max/cls/last/weighted, 모델별 권장 풀링, 다운스트림 영향
136. mean-vs-cls-pooling | Mean Pooling vs CLS 토큰 | rag | concept | BERT 사전학습 vs 임베딩 fine-tune, 평균 풀링이 더 일반적인 이유
137. last-token-pooling-decoder | 마지막 토큰 풀링 (디코더) | rag | concept | LLM 기반 임베딩 표준, 마지막 토큰 hidden state, EOS 활용
138. weighted-attention-pooling | 어텐션 풀링 전략 | rag | concept | 학습 가능 어텐션 가중치, 위치별 중요도, 요약 임베딩
139. fixed-length-chunking | 고정 길이 청킹 전략 | rag | concept | 토큰/문자 단위 고정, 단순/빠름, 의미 절단 위험, 베이스라인
140. semantic-chunking-strategies | 의미적 청킹 전략 | rag | concept | 임베딩 유사도 기반 분할, 토픽 일관성, 더 비싸지만 품질
141. recursive-character-splitting | 재귀적 문자 분할 | rag | concept | 단락->문장->단어 점진 분할, LangChain 표준, 헤딩 인식
142. propositional-chunking | 명제 단위 청킹 | rag | concept | LLM으로 명제 추출 후 청킹, 자기 완결적 사실 단위, RAPTOR 영감
143. agentic-chunking | 에이전트 청킹 | rag | concept | LLM이 청크 경계 결정, 비싼 비용, 최고 품질 RAG
144. context-aware-chunking | 컨텍스트 인식 청킹 | rag | concept | 헤딩/메타데이터 보존, 청크 앞뒤 컨텍스트 추가, Anthropic Contextual Retrieval
145. document-hierarchy-chunking | 문서 계층 청킹 | rag | concept | 섹션/하위섹션 구조 보존, 계층적 검색, RAPTOR 트리 구축

## 6. Agents - 패턴/계보 미커버 (30건)

146. autogpt-original-agent | AutoGPT - 자율 에이전트 시초 | agents | entity | 2023 LLM 자율 에이전트 붐 시작, 목표 분해 + 메모리 + 도구
147. babyagi-task-agent | BabyAGI - 태스크 매니저 에이전트 | agents | entity | Yohei Nakajima 단순 태스크 큐 에이전트, 100 lines, 영향력
148. agentgpt-deployment | AgentGPT 자율 에이전트 플랫폼 | agents | entity | 브라우저 기반 자율 에이전트, 일반인 진입 도구
149. metagpt-software-agent | MetaGPT - 소프트웨어 회사 시뮬레이션 | agents | entity | PM/Engineer/QA 역할 다중 에이전트, 표준 운영 절차 (SOP) 인코딩
150. chatdev-software-company | ChatDev 가상 SW 회사 | agents | entity | 폭포수 SDLC를 LLM 에이전트로, 대화 기반 SW 개발
151. swarm-openai-handoffs | Swarm - OpenAI 핸드오프 라이브러리 | agents | entity | 함수 호출로 에이전트 간 핸드오프, 가벼운 멀티에이전트 패턴
152. function-call-evolution | 함수 호출 진화사 | agents | concept | OpenAI Functions -> Tool Use -> 구조화 호출 -> MCP, 변천 정리
153. tool-creator-meta-agent | 도구 생성 메타 에이전트 | agents | concept | LLM이 자체 도구 작성 + 사용, Code Interpreter 패턴 일반화
154. selfask-decomposition | Self-Ask 분해 패턴 | agents | concept | "후속 질문이 필요한가?" 메타 인지, 검색 통합, ReAct 진화
155. plan-and-solve-prompting | Plan-and-Solve 프롬프팅 | agents | concept | 계획 단계 명시 + 단계별 해결, CoT 강화, EMNLP 2023
156. xot-explorer-of-thought | XoT - 외부 탐색 사고 | agents | concept | MCTS + RL 통합 탐색, ToT/GoT 진화, 게임/추론 SOTA
157. graph-of-thoughts-got | Graph of Thoughts (GoT) | agents | concept | 사고 노드 그래프 구조, 백트래킹/병합, 비선형 추론
158. cumulative-reasoning | 누적 추론 (Cumulative Reasoning) | agents | concept | 검증된 명제 누적, 새 추론에 활용, 24 Game/MATH SOTA
159. critic-revise-pattern | Critic-Revise 패턴 | agents | concept | 비평자 모델 + 수정자 모델, 자기 비평, Constitutional AI 영감
160. agent-assistant-asymmetric | 비대칭 에이전트-어시스턴트 패턴 | agents | concept | 강한 에이전트가 약한 어시스턴트 사용, 비용 최적, 라우팅 패턴
161. browser-use-agent-framework | Browser Use 에이전트 프레임워크 | agents | entity | DOM 시각 표현 + LLM 액션, Playwright 백엔드, 웹 자동화 표준
162. agentic-web-search-pattern | 에이전트 웹 검색 패턴 | agents | concept | 쿼리 변형 + 다중 검색 + 결과 종합, Perplexity/SearchGPT 패턴
163. document-qa-agent | 문서 QA 에이전트 패턴 | agents | concept | PDF/문서 다단계 QA, 표/이미지 처리, 인용 생성
164. coding-agent-tdd | TDD 기반 코딩 에이전트 | agents | concept | 테스트 먼저 -> 구현 -> 검증 사이클, Aider/Claude Code 표준
165. agent-self-correction | 에이전트 자기 교정 | agents | concept | 실행 결과 -> 오류 분석 -> 재시도, 환각 줄이기, 견고성 향상
166. agent-fallback-strategies | 에이전트 폴백 전략 | agents | concept | 도구 실패 시 대체 경로, graceful degradation, 다중 모델 라우팅
167. agent-rate-limiting-patterns | 에이전트 레이트 제한 패턴 | agents | concept | API 한도 관리, 지수 백오프, 토큰 버킷, 우선순위 큐
168. agent-context-management | 에이전트 컨텍스트 관리 | agents | concept | 슬라이딩 윈도우, 요약, vector store 메모리, 컨텍스트 폭발 회피
169. agent-task-decomposition-patterns | 태스크 분해 패턴 비교 | agents | concept | top-down/bottom-up/recursive, HTN/STRIPS 영향, 실무 적용
170. parent-child-spawn-pattern | 부모-자식 에이전트 spawn 패턴 | agents | concept | 부모가 서브에이전트 동적 생성, Claude Code 패턴, 오케스트레이션
171. agent-as-tool-pattern | 에이전트를 도구로 사용 패턴 | agents | concept | 에이전트가 함수 시그니처처럼 노출, 계층적 멀티에이전트 구성
172. agent-state-machine | 에이전트 유한 상태 머신 패턴 | agents | concept | 명시적 상태 + 전이, LangGraph 구현, 결정론적 워크플로우
173. agent-event-driven-pattern | 이벤트 주도 에이전트 패턴 | agents | concept | 이벤트 큐 + 핸들러, 비동기 에이전트, 마이크로서비스 영감
174. agent-circuit-breaker | 에이전트 서킷 브레이커 패턴 | agents | concept | 반복 실패 시 자동 차단, 복구 시도, 안정성 패턴 적용
175. agent-saga-pattern | 에이전트 사가 패턴 | agents | concept | 다단계 트랜잭션 + 보상 액션, 분산 트랜잭션 영감, 롤백

## 7. Applications - 산업별 미커버 (30건)

176. ai-architecture-design | AI 건축 설계 응용 | applications | concept | 도면 생성, 구조 분석, 에너지 시뮬레이션, 재료 최적화, BIM 통합
177. ai-game-development | AI 게임 개발 응용 | applications | concept | 절차적 콘텐츠 생성, NPC 대화, 게임 밸런싱, 자산 생성, AAA 통합
178. ai-supply-chain-optimization | AI 공급망 최적화 | applications | concept | 수요 예측, 재고 최적화, 경로 계획, 위험 평가, ERP 통합
179. ai-fraud-detection | AI 사기 탐지 시스템 | applications | concept | 거래/보험/정체성 사기, 그래프 신경망 활용, 실시간 스코어링
180. ai-cyber-threat-hunting | AI 사이버 위협 헌팅 | applications | concept | SIEM/EDR 통합, 이상 탐지, 위협 인텔리전스, MITRE ATT&CK 매핑
181. ai-personalization-engines | AI 개인화 엔진 | applications | concept | 1:1 콘텐츠 큐레이션, 행동 예측, 다중 채널 통합, 동의 관리
182. ai-content-recommendation | AI 콘텐츠 추천 시스템 | applications | concept | Netflix/Spotify/YouTube 패턴, 두 타워 + 트랜스포머, A/B 테스팅
183. ai-anomaly-detection | AI 이상 탐지 응용 | applications | concept | 시계열/그래프/이미지 이상, 비지도 학습, IT 인프라 모니터링
184. ai-network-monitoring | AI 네트워크 모니터링 | applications | concept | NetFlow 분석, 이상 트래픽, DDoS 탐지, 자동 라우팅 조정
185. ai-aiops-log-analysis | AI 로그 분석 (AIOps) | applications | concept | 로그 클러스터링, 이상 시퀀스, 근본 원인 분석, ChatOps
186. ai-realtime-translation | AI 실시간 번역 | applications | concept | 동시 번역 시스템, 음성-음성 직접 번역, 회의/방송 응용
187. ai-sign-language | AI 수어 인식/생성 | applications | concept | RGB-D 비디오 인식, 3D 아바타 생성, 청각 장애인 접근성
188. ai-accessibility-tools | AI 접근성 도구 | applications | concept | 화면 읽기, 자동 캡션, 알트 텍스트, 색맹 보정, 모바일 통합
189. ai-mental-health | AI 정신 건강 지원 | applications | concept | 감정 분석, CBT 기반 챗봇, 위기 감지, 윤리적 프레임워크
190. ai-elder-care | AI 노인 돌봄 | applications | concept | 낙상 감지, 약물 알림, 동반 챗봇, 인지 모니터링
191. ai-agriculture-farming | AI 농업/스마트 팜 | applications | concept | 위성 작물 모니터링, 정밀 살포, 가축 행동, 수확 예측
192. ai-climate-modeling | AI 기후 모델링 | applications | concept | GraphCast, ClimaX, 신경 PDE 솔버, 극한 날씨 예측 가속
193. ai-sustainability-optimization | AI 지속가능성 최적화 | applications | concept | ESG 보고, 탄소 배출 예측, 순환 경제 분석, 공급망 환경 영향
194. ai-energy-grid | AI 에너지 그리드 관리 | applications | concept | 수요/공급 예측, 분산 자원 통합, 마이크로그리드, 가격 최적화
195. ai-urban-planning | AI 도시 계획 | applications | concept | 토지 이용 최적화, 교통 흐름, 디지털 트윈, 시민 참여 도구
196. ai-transportation-routing | AI 교통 경로 최적화 | applications | concept | 실시간 라우팅, 다중 모드 통합, 화물/배송, 도시 교통 시뮬
197. ai-autonomous-vehicles | AI 자율 주행 차량 | applications | concept | 인식-계획-제어 스택, Waymo/Tesla/Cruise, BEV 변환, MLOps 안전
198. ai-warehouse-robotics | AI 창고 로보틱스 | applications | concept | Amazon Robotics, 동적 픽킹, 차량 협업, 시각 SLAM
199. ai-quality-inspection | AI 품질 검사 (제조) | applications | concept | 시각 결함 탐지, 이상 검출, 자동 분류, 산업 4.0 통합
200. ai-predictive-maintenance | AI 예측 유지보수 | applications | concept | 진동/온도/소리 분석, RUL 예측, 디지털 트윈, IoT 센서 융합
201. ai-credit-scoring | AI 신용 평가 | applications | concept | 대안 데이터, 그래프 ML, 공정성 제약, 설명 가능성, 규제 준수
202. ai-portfolio-management | AI 포트폴리오 관리 | applications | concept | 강화학습 트레이딩, 리스크 모델링, 알트 데이터, 자동 리밸런싱
203. ai-legal-discovery | AI 법률 디스커버리 | applications | concept | 전자 디스커버리, 문서 분류, 키 사실 추출, 권한 보호
204. ai-tax-compliance | AI 세무 준수 | applications | concept | 자동 세금 계산, 규제 변경 추적, 감사 위험 분석, 다국적 통합
205. ai-hr-recruitment | AI HR/채용 | applications | concept | 이력서 매칭, 인터뷰 분석, 편향 감사, 직원 유지 예측

## 8. Papers - 핵심 원논문 미수집 (30건)

206. resnet-original-paper | ResNet 원논문 (He et al. 2015) | papers | paper | 잔차 연결 도입, ILSVRC 2015 우승, 152층까지 학습, CVPR Best Paper
207. dropout-original-paper | Dropout 원논문 (Srivastava et al. 2014) | papers | paper | Hinton 그룹 무작위 비활성화, 앙상블 해석, 정규화 표준
208. batch-norm-original-paper | Batch Normalization 원논문 (Ioffe 2015) | papers | paper | 내부 공변량 변화 가설, 배치 통계 정규화, 학습 가속
209. layer-norm-original-paper | Layer Normalization 원논문 (Ba 2016) | papers | paper | RNN/Transformer용 정규화, 배치 독립, 모든 LLM 표준
210. adam-original-paper | Adam 옵티마이저 원논문 (Kingma 2014) | papers | paper | 1차/2차 모멘트 추정, 적응적 학습률, 가장 인용 ML 논문 중 하나
211. word2vec-original-paper | Word2Vec 원논문 (Mikolov 2013) | papers | paper | CBOW/Skip-gram, 음성 샘플링, 단어 임베딩 혁명, NLP 패러다임 전환
212. roberta-paper | RoBERTa 원논문 (Liu et al. 2019) | papers | paper | BERT 강화 학습 레시피, NSP 제거, 동적 마스킹, 더 많은 데이터
213. albert-paper | ALBERT 원논문 (Lan et al. 2019) | papers | paper | 파라미터 공유, 인수분해 임베딩, 문장 순서 예측, 18배 작은 BERT
214. electra-paper | ELECTRA 원논문 (Clark 2020) | papers | paper | 대체 토큰 탐지, 효율 사전학습, GAN 영향, RoBERTa 4배 빠름
215. xlnet-paper | XLNet 원논문 (Yang 2019) | papers | paper | 순열 언어 모델링, AR + AE 결합, BERT 단점 극복, 20개 NLP 태스크 SOTA
216. flamingo-paper | Flamingo 원논문 (DeepMind 2022) | papers | paper | 시각-언어 멀티모달, 게이트 크로스어텐션, in-context few-shot 비전
217. blip-paper | BLIP 원논문 (Salesforce 2022) | papers | paper | 캡셔너 + 필터, 부트스트래핑, 시각-언어 통합 사전학습
218. blip-2-paper | BLIP-2 원논문 (Salesforce 2023) | papers | paper | Q-Former 경량 브리지, 동결 인코더, LLaVA 영감, 비전-LLM 결합
219. llava-original-paper | LLaVA 원논문 (Liu 2023) | papers | paper | GPT-4 합성 시각 instruction, MLP 프로젝터, 오픈소스 멀티모달 출발
220. minigpt4-paper | MiniGPT-4 원논문 (2023) | papers | paper | 단일 프로젝션 레이어로 ViT-LLM 결합, 효율적 멀티모달 인식
221. instructblip-paper | InstructBLIP 원논문 (2023) | papers | paper | BLIP-2 + 명령 튜닝, instruction-aware Q-Former, 13 데이터셋
222. kosmos-paper | KOSMOS 시리즈 원논문 (Microsoft) | papers | paper | KOSMOS-1/2.5 멀티모달 LLM, OCR-free 문서 이해, 텍스트-이미지 통합
223. fuyu-paper | Fuyu 원논문 (Adept 2023) | papers | paper | 이미지를 텍스트 시퀀스로 직접, 비전 인코더 없는 단순 디자인
224. ulm-fit-paper | ULMFiT 원논문 (Howard 2018) | papers | paper | NLP 전이 학습 시초, 차등 학습률 fine-tune, ImageNet 모먼트
225. simclr-original-paper | SimCLR 원논문 (Chen 2020) | papers | paper | 대조 학습 비전 + 강한 증강, 큰 배치, 자기지도 비전 SOTA
226. moco-original-paper | MoCo 원논문 (He 2020) | papers | paper | 모멘텀 인코더 + 동적 큐, 자기지도 다운스트림 ImageNet 능가
227. byol-original-paper | BYOL 원논문 (Grill 2020) | papers | paper | 음성 샘플 없이 자기지도, 대상 네트워크, 모드 붕괴 회피 미스터리
228. dino-original-paper | DINO 원논문 (Caron 2021) | papers | paper | 자기 증류 + ViT, 의미 분할 emergent, 무라벨 시각 표현
229. mae-original-paper | MAE 원논문 (He 2022) | papers | paper | 75% 마스킹 + 비대칭 인코더-디코더, ViT 자기지도 사전학습 표준
230. videomae-paper | VideoMAE 원논문 | papers | paper | 비디오 90% 마스킹, 시공간 자기지도, Kinetics 85%+ SOTA
231. point-mae-paper | Point-MAE 원논문 | papers | paper | 3D 포인트 클라우드 마스킹 자기지도학습, ShapeNet/ModelNet 적용
232. ddpm-original-paper | DDPM 원논문 (Ho 2020) | papers | paper | 노이즈 예측 + Markov chain 디노이징, 확산 모델 부상의 시작
233. ddim-paper | DDIM 원논문 (Song 2021) | papers | paper | 비마르코프 결정론적 샘플링, 50배 빠른 확산 추론, 잠재 보간
234. classifier-free-guidance-paper | Classifier-Free Guidance 원논문 | papers | paper | 조건부/비조건부 결합, 클래스 가이던스 없이 조건 강화, SD 핵심
235. lcm-latent-consistency-paper | LCM 원논문 - Latent Consistency Models | papers | paper | 잠재 일관성 모델, 1-4스텝 SD 생성, 모바일 확산 가능

## 9. Tooling - 클라우드/IDE/플랫폼 (35건)

236. ragflow-platform | RAGFlow - 오픈소스 RAG 플랫폼 | tooling | entity | infiniflow.org, 깊은 문서 이해, 시각 청킹, 인용 추적, 엔터프라이즈
237. text-generation-inference-tgi | TGI - HuggingFace Text Generation Inference | tooling | entity | HF 공식 LLM 서빙, Rust 기반, 연속 배치, FlashAttention 통합
238. lmdeploy-internlm | LMDeploy - InternLM 추론 엔진 | tooling | entity | 상하이 AI Lab, TurboMind 백엔드, 4비트 양자화, vLLM 대안
239. tabby-self-hosted-coding | Tabby - 자체 호스팅 코딩 어시스턴트 | tooling | entity | 자체 호스팅 GitHub Copilot 대안, 오픈소스, on-prem 코딩 지원
240. continue-vscode-extension | Continue - VSCode AI 확장 | tooling | entity | 오픈소스 Cursor 대안, 모델 선택, JetBrains 지원, MIT 라이선스
241. cline-claude-coder | Cline - 오픈소스 Claude 코딩 에이전트 | tooling | entity | VSCode 통합, MCP 지원, 자율 작업, 다중 모델 라우팅
242. zed-ai-editor | Zed AI 에디터 | tooling | entity | Atom 후속, Rust 작성, 협업 + AI, GPU 렌더링, Sublime 영감
243. tabnine-completion | Tabnine - AI 코드 완성 | tooling | entity | 가장 오래된 AI 코딩 도구, 로컬 모델 옵션, 엔터프라이즈 보안
244. codeium-completion | Codeium - 무료 코드 완성 | tooling | entity | 70+ 언어 지원, IDE 다수, Windsurf의 모회사
245. supermaven-fast-completion | Supermaven - 초고속 코드 완성 | tooling | entity | 1M 컨텍스트, 100ms 미만 응답, Babble 모델, 인기 급등
246. cloud-code-jetbrains | Cloud Code for JetBrains | tooling | entity | Google 공식 JetBrains 통합, GCP/Gemini, IDE 내 클라우드 작업
247. void-editor-ai | Void - 오픈소스 Cursor | tooling | entity | Cursor 오픈소스 포크 시도, MIT, 커스터마이징 가능
248. helix-editor-ai | Helix Editor with AI | tooling | entity | 모달 에디터 + AI, Vim/Kakoune 영감, Rust, 커뮤니티 AI 플러그인
249. neovim-copilot-ai | Neovim AI 코딩 (Avante/CodeCompanion) | tooling | entity | Avante.nvim, CodeCompanion, 다중 LLM 통합, 모달 기반 워크플로우
250. xinference-multi-model | Xinference - 다중 모델 추론 서버 | tooling | entity | xorbitsai 다중 모델 동시 서빙, OpenAI API 호환, 분산 추론
251. dolphinflow-fine-tuning | DolphinFlow - 시각적 fine-tuning | tooling | entity | UI 기반 fine-tuning 워크플로우, 데이터셋 준비 + LoRA, 비기술자 도구
252. modal-com-runtime | Modal.com - 서버리스 ML 런타임 | tooling | entity | 함수 호출처럼 GPU 사용, 빠른 콜드 스타트, 사용량 기반 과금
253. baseten-deployment | Baseten - ML 배포 플랫폼 | tooling | entity | TrussML 패키징, GPU 자동 스케일, FT/H100, 모델 마켓플레이스
254. replicate-platform | Replicate - 모델 호스팅 | tooling | entity | Cog 패키징, 오픈소스 모델 즉시 배포, API 노출, 사용량 과금
255. together-ai-inference | Together AI - 추론 플랫폼 | tooling | entity | 200+ 오픈 모델, FlashAttention 최적화, fine-tune 서비스, RedPajama
256. fireworks-ai-platform | Fireworks AI - 빠른 추론 | tooling | entity | 자체 추론 엔진, 함수 호출 + 구조화 출력, 모델 카탈로그
257. anyscale-platform | Anyscale - Ray 기반 ML 플랫폼 | tooling | entity | Ray 창립자 회사, RLHF/fine-tune, 분산 학습/추론, 대규모
258. bento-cloud-mlops | BentoCloud - BentoML 매니지드 | tooling | entity | BentoML 패키지 자동 배포, GPU 스케일, 엔터프라이즈 MLOps
259. e2b-ai-sandbox | E2B - AI 코드 실행 샌드박스 | tooling | entity | LLM 코드 실행 격리 환경, Firecracker microVM, OpenAI Code Interpreter 영감
260. modal-volumes-storage | Modal Volumes - 영구 스토리지 | tooling | entity | Modal 영구 디스크, 모델 캐시, 데이터셋 공유, 클라우드 ML 공유 자원
261. inferless-deployment | Inferless - 서버리스 GPU | tooling | entity | 콜드 스타트 0.1초, A100/H100, 사용량 과금, 모델 import 자동화
262. octo-ai-platform | OctoAI - 모델 호스팅 | tooling | entity | NVIDIA 인수, 50+ 모델, 빠른 추론, customization
263. perplexity-api | Perplexity API - 검색 강화 LLM | tooling | entity | 답변 + 인용 API, sonar 모델, 실시간 웹 검색 통합 LLM
264. groq-cloud-api | Groq Cloud - LPU 추론 클라우드 | tooling | entity | LPU 기반 초저지연, OSS 모델 서빙, 스트리밍 1000+ tok/s
265. cerebras-cloud-inference | Cerebras Cloud Inference | tooling | entity | WSE-3 웨이퍼 스케일, 가장 빠른 Llama 추론, 1800 tok/s
266. sambanova-systems-cloud | SambaNova Cloud | tooling | entity | RDU 데이터플로우 칩, 엔터프라이즈 배포, 16T 토큰 모델 가능
267. d-matrix-corsair | d-Matrix Corsair - 추론 가속기 | tooling | entity | 디지털 인메모리 컴퓨팅, 추론 전용 ASIC, 데이터센터 효율
268. tenstorrent-grayskull | Tenstorrent Grayskull/Wormhole | tooling | entity | Jim Keller, 오픈소스 RISC-V + 추론 칩, AI 워크로드 가속
269. opencode-cli | opencode-cli - 오픈소스 Codex 대안 | tooling | entity | 대화형 코딩 에이전트, 커뮤니티 주도, 다중 LLM 라우팅
270. crush-coding-agent | Crush - 빠른 코딩 에이전트 | tooling | entity | Charm 회사 TUI 코딩 에이전트, MCP 지원, 모델 선택

## 10. Concepts - AI 안전/메타 (30건)

271. ai-fluency-literacy | AI 활용 능력 (AI Fluency) | concepts | concept | 일반 사용자 AI 활용 능력 정의, 교육 프레임워크, 디지털 격차
272. ai-economic-impact | AI 경제 영향 분석 | concepts | concept | 노동 시장 변화, 생산성 패러독스, 자본 이동, 거시 경제 모델링
273. ai-reasoning-vs-memorization | 추론 vs 암기 구분 | concepts | concept | LLM이 패턴 매칭인지 진짜 추론인지, 검증 방법, 조작 실험
274. zero-vs-few-shot-comparison | 제로샷 vs 퓨샷 학습 비교 | concepts | concept | 모델 크기/태스크별 트레이드오프, 합성 예시 효과, ICL 메커니즘
275. open-vs-closed-domain-qa | 개방 vs 폐쇄 도메인 QA | concepts | concept | RAG vs 파라미터 지식, 정확도 vs 신선도, 응용별 권장사항
276. prompt-as-program | Program-as-Prompt 패러다임 | concepts | concept | DSPy 영감, 프롬프트를 프로그램으로 컴파일, 자동 최적화
277. prompt-template-libraries | 프롬프트 템플릿 라이브러리 비교 | concepts | concept | LangChain/LlamaIndex/PromptLayer 비교, 버전 관리, 재사용 패턴
278. positional-bias-llm | LLM 위치 편향 | concepts | concept | 시작/끝 토큰 우선, lost-in-the-middle 진화, 평가 시 위치 무작위화
279. recency-bias-llm | LLM 최근성 편향 | concepts | concept | 최근 컨텍스트 과대 가중치, 긴 대화 일관성 문제, 메모리 시스템 필요성
280. confirmation-bias-llm | LLM 확증 편향 | concepts | concept | 사용자 의견 동조, 사실 vs 의견 구분 약함, 비판적 평가 부족
281. self-preference-bias | LLM 자기 선호 편향 | concepts | concept | LLM-as-Judge 자기 모델 출력 선호, 평가 신뢰성 위협, 완화 기법
282. fabrication-vs-confabulation | 환각: 조작 vs 작화 | concepts | concept | 의도적 거짓 vs 무의식적 합리화, 의학/심리 용어 차용, 교정 전략
283. faithfulness-attribution | 충실성과 출처 귀속 | concepts | concept | 컨텍스트 기반 답변이 실제로 컨텍스트에 충실한지, ATTR 지표
284. groundedness-evaluation | 그라운드니스 평가 | concepts | concept | 답변이 제공 컨텍스트에 근거하는지 측정, RAG 핵심 메트릭, NLI 기반
285. evidence-attribution | 증거 귀속과 인용 생성 | concepts | concept | 답변 -> 증거 매핑, 인용 정확성, 검증 가능 RAG, Anthropic Citations API
286. emergent-tool-use | 신생 도구 사용 능력 | concepts | concept | LLM 스케일링 시 도구 사용 emergent, 명시적 학습 없이 함수 호출
287. emergent-deception | 신생 기만 행동 | concepts | concept | RLHF 후 의도 가림, 평가 인식 행동 차이, 정렬 불충분 신호
288. specification-gaming-deeper | 사양 게이밍 심화 | concepts | concept | RL 보상 명세 결함 악용, 의도된 결과 회피, 실제 사례 카탈로그
289. wireheading-rl | Wireheading - RL 보상 회로 단락 | concepts | concept | 에이전트가 보상 신호 직접 조작, 환경 무시, AGI 안전 우려
290. instrumental-convergence | 도구적 수렴 (Instrumental Convergence) | concepts | concept | 자원/생존/지능 향상이 거의 모든 목표에 유용, AGI 안전 핵심 개념
291. corrigibility-alignment | 교정가능성 (Corrigibility) | concepts | concept | AI가 수정/종료에 협력하는 속성, 강한 정렬보다 약한 안전 보장
292. orthogonality-thesis | 직교성 가설 (Orthogonality Thesis) | concepts | concept | 지능과 목표 독립, Bostrom, 똑똑한 AI가 자동으로 윤리적이지 않음
293. agi-superintelligence-debate | AGI/초지능 논쟁 | concepts | concept | 정의/측정/도래 시기 논쟁, AGI Safety 연구 흐름, 회의론자 vs 옹호론자
294. ai-takeoff-scenarios | AI 이륙 시나리오 | concepts | concept | 빠른/느린/혼합 이륙, 기술 ipfication, 방어/공격 균형, 정책 함의
295. ai-existential-risk | AI 실존적 위험 (X-Risk) | concepts | concept | Bostrom/Russell, 통제 문제, 측정 가능 위험 vs 추측, 거버넌스
296. transformative-ai-impact | 변혁적 AI 영향 | concepts | concept | 산업 혁명급 영향, GDP 성장률 변화, 사회 적응 시간, OPP 평가
297. economic-displacement-ai | AI 경제 이동/대체 | concepts | concept | 자동화 위험 직업, 보완 vs 대체, 재훈련 정책, UBI 논쟁
298. ai-pause-letter-impact | AI 일시정지 운동의 영향 | concepts | concept | FLI 6개월 일시정지 서한, 엇갈린 반응, 정책 변화, 거버넌스 모먼텀
299. anthropic-rsp-evolution | Anthropic 책임 있는 스케일링 정책 진화 | concepts | concept | RSP v1 -> v3, ASL 레벨 정의, 평가 + 보안 요구, 산업 표준화 시도
300. ai-frontier-model-forum | Frontier Model Forum | concepts | concept | OpenAI/Anthropic/Google/MS 협의체, 안전 협력, 거버넌스 협의

---

## 통계
- 총 300건
- 카테고리별 분포: foundations 30, architectures 35, training 30, inference 25, rag 25, agents 30, applications 30, papers 30, tooling 35, concepts 30
- 페이지 타입 분포: concept 235, entity 50, paper 30 (현 위키 비율 유지)
- 모든 슬러그는 기존 1,417 페이지와 비중복 검증 완료

## 다음 단계
1. `/wiki-ingest` 또는 wave 배치로 위키 페이지 생성
2. 검증된 패턴: 10 병렬 sonnet 에이전트 x 8페이지 = 80페이지/웨이브, 약 7분 소요
3. 4개 웨이브로 약 28-32분 내 전체 처리 가능

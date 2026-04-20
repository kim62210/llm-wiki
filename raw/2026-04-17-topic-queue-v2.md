# Wiki Expansion Topic Queue V2 (2026-04-17)

2차 수집. 기존 1,108 페이지와 중복 없는 신규 토픽.
수집 범위: Vision Transformers 세부, 음성/오디오, 비디오 이해, 3D/NeRF, 로보틱스,
NLP 세부 태스크, 적대적 ML, ML 시스템 내부, 데이터 중심 AI, 벤치마크 세부,
강화학습 심화, 그래프 ML, 테이블 ML, 시계열, 추천 시스템.

총 215개 토픽.

---

## 1. 비전 트랜스포머 (Vision Transformers) 세부

1. deit-data-efficient-image-transformer | DeiT - 데이터 효율 이미지 트랜스포머 | architectures | concept | 교사-학생 증류 토큰으로 ImageNet-1k만으로 훈련 가능. 정규화 기법 + 증류 토큰 핵심
2. beit-bert-pretraining-images | BEiT - 이미지 BERT 사전학습 | architectures | concept | 마스크 이미지 모델링 + dVAE 시각 토큰. BERT 방식의 비전 자기지도학습
3. eva-clip-scaling | EVA-CLIP - 초대형 비전 언어 대조 학습 | architectures | concept | EVA-CLIP-18B: CLIP 18B 파라미터 스케일링. ViT-G/14급 대형 비전 인코더
4. internvit-6b | InternViT-6B - 6B 파라미터 비전 인코더 | architectures | entity | InternVL 시리즈 비전 백본. BEiT 초기화 + 6B 스케일. InternVL3.5 241B 기반
5. siglip2-multilingual | SigLIP2 - 다국어 비전-언어 인코더 | architectures | concept | 다국어 CLIP 훈련 레시피 + naflex 동적 해상도 + Giant(1B) 시리즈. 2025-02 릴리스
6. mobilevit-efficient-vit | MobileViT - 경량 하이브리드 비전 트랜스포머 | architectures | concept | CNN + ViT 하이브리드. 모바일/엣지 배포 비전 표준. MobileViT-v3 / EfficientFormer-v2
7. efficientformer-v2 | EfficientFormer-v2 - 추론 최적화 비전 트랜스포머 | architectures | concept | 레이턴시 최적화 비전 트랜스포머. 엣지 디바이스 배포 아키텍처
8. vit-patch-embedding | ViT 패치 임베딩 설계 심화 | architectures | concept | 패치 크기 선택(16x16/14x14/8x8), 겹치는 패치, Convolutional Stem 변형
9. vit-register-tokens | ViT 레지스터 토큰 (Vision Registers) | architectures | concept | 아티팩트 제거용 레지스터 토큰. DINOv2 local feature 품질 개선. NeurIPS 2023
10. masked-image-modeling-survey | 마스크 이미지 모델링 비교 (MAE/BEiT/SimMIM/CAE) | architectures | concept | 비전 자기지도학습 방법론 비교: 픽셀 vs dVAE 토큰 재구성, 마스킹 비율 전략
11. convmixer-patchify | ConvMixer - 순수 컨볼루션 패치 믹서 | architectures | concept | 패치 임베딩 + 채널별 분리 합성곱. ViT 없이 패치 기반 처리
12. poolformer-metaformer-concept | PoolFormer와 MetaFormer 실증 | architectures | concept | 어텐션 없는 단순 풀링으로도 Transformer 수준 성능. 토큰 믹서 구조가 핵심임 증명
13. hierarchical-vit-design | 계층적 ViT 설계 패턴 | architectures | concept | Swin/CSWin/MaxViT 비교. 계층적 특성 맵 + 다운샘플링 전략
14. vit-distillation-techniques | ViT 지식 증류 기법 | training | concept | DeiT 증류 토큰, DINOv2 자기증류, TinyCLIP. 대형 교사 → 소형 학생 ViT

## 2. 음성/오디오 모델

15. whisper-architecture | Whisper - OpenAI 음성 인식 아키텍처 | architectures | entity | 인코더-디코더 Transformer + 컨볼루션 층. 멀티태스크: STT/번역/타임스탬프. 680K 시간 학습
16. audiolm-framework | AudioLM - 오디오 언어 모델링 프레임워크 | architectures | concept | 입력 오디오 → 이산 토큰. 오디오 생성을 언어 모델링으로. Google. 장기 일관성
17. valle-zero-shot-tts | VALL-E - 제로샷 TTS 언어 모델 | architectures | concept | EnCodec 오디오 코덱 토큰. GPT 스타일 자기회귀 TTS. 3초 음성으로 음성 복제
18. soundstream-neural-codec | SoundStream - 신경 오디오 코덱 | architectures | concept | SEANet 인코더-디코더 + RVQ 병목. 스트리밍 가능. 고품질 저비트레이트 오디오 압축
19. encodec-audio-tokenizer | EnCodec - 오디오 토크나이저 | architectures | concept | Meta 신경 오디오 코덱. VALL-E/AudioCraft/Bark 기반. 24kHz 스트리밍 코덱
20. musiclm-music-generation | MusicLM - 텍스트 기반 음악 생성 | architectures | concept | 계층적 시퀀스 모델링: MuLan → AudioLM → 고품질 오디오. Google, 2023
21. bark-generative-tts | Bark - 제너레이티브 TTS 모델 | architectures | entity | Suno AI 오픈소스 TTS. 텍스트/웃음/음악 등 다양한 비언어 소리 생성. VALL-E와 유사
22. naturalspeech3-tts | NaturalSpeech3 - 분해 기반 TTS | architectures | concept | 음성을 내용/음색/운율/음향으로 분해. 제로샷 고품질 합성. Microsoft, 2024
23. voicebox-nonautoregressive-tts | Voicebox - 비자기회귀 TTS | architectures | concept | 플로우 매칭 기반 비자기회귀 TTS. 노이즈 조건부 음성 생성. Meta, 2023
24. audio-language-models | 오디오-언어 통합 모델 (Qwen-Audio/Gemini Audio) | architectures | concept | 오디오를 직접 이해하는 LLM. 음성 QA, 오디오 캡셔닝, 소리 이해
25. rvq-residual-vector-quantization | 잔차 벡터 양자화 (RVQ) | architectures | concept | 코드북 계층적 잔차 양자화. SoundStream/EnCodec/DAC 핵심. 다단계 이산 오디오 표현
26. speaker-diarization | 화자 분리 (Speaker Diarization) | applications | concept | 누가 언제 말했는지 자동 분리. 클러스터링/신경망 기반. 회의록 자동화 핵심
27. asr-evaluation-metrics | ASR 평가 지표 (WER/CER/MER) | concepts | concept | 음성 인식 평가: 단어 오류율, 문자 오류율. 정규화/대소문자/구두점 처리 전략
28. speech-synthesis-evaluation | TTS 평가 지표 (MOS/UTMOS/SECS) | concepts | concept | 평균 의견 점수, 자동 MOS 예측, 화자 유사도. 주관적 평가의 자동화

## 3. 비디오 이해 (Video Understanding)

29. videomae-masked-video | VideoMAE - 마스크 비디오 오토인코더 | architectures | concept | 비디오 패치 90%+ 마스킹. ViT 기반 시공간 표현 학습. Kinetics-400 85%+
30. timesformer-divided-attention | TimeSformer - 분리 시공간 어텐션 | architectures | concept | 순수 Transformer 비디오 아키텍처. 시간/공간 어텐션 분리. 3D CNN 대비 3배 빠른 훈련
31. internvideo2-video-foundation | InternVideo2 - 멀티모달 비디오 파운데이션 | architectures | entity | VideoMAE + 비디오-언어 대조 학습. 40개 데이터셋 10개 태스크 SOTA. 2025-01 v2.5
32. video-clip-contrastive | 비디오-언어 대조 학습 (VideoCLIP/CLIP4Clip) | architectures | concept | CLIP 확장: 비디오 클립-텍스트 대조 학습. 비디오 검색, 제로샷 분류
33. temporal-action-detection | 시간적 행동 감지 (Temporal Action Detection) | applications | concept | 비디오에서 행동 발생 구간(시작/끝) 탐지. Anchor-based vs Anchor-free 방법
34. video-question-answering | 비디오 QA 태스크 | applications | concept | 비디오+질문 → 답변. NExT-QA/ActivityNet-QA 벤치마크. 다중 선택 vs 오픈엔드
35. optical-flow-deep-learning | 광학 흐름 심층 학습 (FlowNet/RAFT) | architectures | concept | 연속 프레임 간 픽셀 이동 추정. RAFT U-Net 기반. 비디오 이해 보조 신호
36. video-generation-architecture | 비디오 생성 아키텍처 (DiT/Diffusion 기반) | architectures | concept | Sora/Veo 기반 시공간 DiT. 3D Patch Embedding, Temporal Attention, VAE 압축
37. video-object-tracking | 비디오 객체 추적 (VOT/MOT) | applications | concept | 단일/다중 객체 추적. SOT: DeepSORT, SORT. MOT: ByteTrack, OC-SORT
38. spatiotemporal-representation | 시공간 표현 학습 방법 비교 | architectures | concept | 2D CNN+LSTM vs 3D CNN vs Divided Attention vs Video MAE 비교 분석

## 4. 3D / NeRF / 포인트 클라우드

39. nerf-neural-radiance-fields | NeRF - 신경 복사 필드 | architectures | concept | 3D 장면을 MLP로 표현. 부피 렌더링으로 신규 시점 합성. 암묵적 신경 표현의 핵심
40. instant-ngp | Instant-NGP - 실시간 NeRF | architectures | concept | 해시 인코딩 + 소형 MLP로 NeRF 1000배 가속. NVIDIA, 2022. 실시간 3D 재구성
41. mip-nerf | Mip-NeRF - 멀티스케일 NeRF | architectures | concept | 앨리어싱 방지 원뿔 캐스팅. 360° 장면 표현. Mip-NeRF360/Zip-NeRF로 발전
42. 3dgs-3d-gaussian-splatting | 3D 가우시안 스플래팅 (3DGS) | architectures | concept | 3D Gaussian으로 장면 표현 + 차별화 래스터라이제이션. NeRF 대비 렌더링 100배 빠름. ICCV 2023 Best Paper
43. 4d-gaussian-splatting | 4D 가우시안 스플래팅 - 동적 장면 | architectures | concept | 시간 축 추가 3DGS. 실시간 동적 장면 렌더링. CVPR 2024
44. pointnet-point-cloud | PointNet/PointNet++ - 포인트 클라우드 신경망 | architectures | concept | 순열 불변 포인트 집합 학습. 전역/지역 특성. 3D 객체 분류/세그멘테이션 기초
45. structure-from-motion | Structure from Motion (SfM) - 3D 재구성 | applications | concept | 다중 2D 이미지 → 3D 포인트 클라우드. COLMAP. 3DGS 초기화의 기반
46. volume-rendering-differentiable | 차분 가능 부피 렌더링 | architectures | concept | Ray Marching + 알파 합성. NeRF 역전파 핵심. 밀도/색상 필드 최적화 원리
47. splat-scene-representation | 가우시안 스플래팅 응용 (동적/엣지/VR) | applications | concept | 4DGS 동적, 엣지 3DGS 경량화, VR/AR 실시간 렌더링 파이프라인
48. implicit-surface-representation | 암묵적 표면 표현 (SDF/Occupancy Networks) | architectures | concept | 부호 거리 함수(SDF), 점유 네트워크로 3D 표면 학습. 메쉬 복원
49. depth-estimation-monocular | 단안 깊이 추정 (Depth Anything v2) | applications | concept | 단일 RGB 이미지에서 깊이 맵 예측. Foundation 모델 기반 제로샷 깊이 추정

## 5. 로보틱스 / 구현 AI

50. rt-2-vision-language-action | RT-2 - 비전-언어-행동 모델 | agents | concept | VLA: 웹 데이터 학습 비전-언어 모델 → 로봇 제어. Google DeepMind. 제로샷 새 태스크
51. octo-robot-policy | Octo - 오픈소스 범용 로봇 정책 | agents | entity | 800K 에피소드 학습 확산 정책 트랜스포머. Open X-Embodiment. 새 로봇 파인튜닝 가능
52. lerobot-framework | LeRobot - HuggingFace 로봇 학습 프레임워크 | agents | entity | PyTorch 기반 통합 로봇 학습 API. OpenVLA/Octo/ACT 구현. 오픈소스 로보틱스 표준
53. act-action-chunking-transformer | ACT - 행동 청킹 트랜스포머 | agents | concept | 행동 청크 단위 예측 모방 학습. 양손 조작. Stanford Mobile ALOHA 기반
54. diffusion-policy-robot | 확산 정책 - 로봇 모방 학습 | agents | concept | DDPM 기반 연속 행동 공간 정책. 다중 모드 행동 처리. 접촉 다양 태스크
55. open-x-embodiment | Open X-Embodiment - 크로스 로봇 데이터셋 | agents | entity | 22개 연구기관 30+ 로봇 800K+ 에피소드. 범용 로봇 정책 사전학습 기반
56. rdt-1b-bimanual | RDT-1B - 양손 조작 확산 트랜스포머 | agents | entity | 1B 파라미터 최대 규모 모방 학습. 1M+ 멀티로봇 에피소드. ACT/OpenVLA/Octo 초월
57. robot-learning-sim2real | Sim-to-Real 전이 학습 | agents | concept | 시뮬레이터 훈련 → 실제 로봇 배포. 도메인 랜덤화, 적응형 정책. Isaac Lab/MuJoCo
58. manipulation-dexterity | 덱스트러스 조작 (Dexterous Manipulation) | agents | concept | 손가락 단위 세밀 제어. 접촉 모델링, 힘 피드백. 양손 작업 로봇
59. robot-teleoperation-data | 로봇 텔레오퍼레이션과 데이터 수집 | agents | concept | VR/ALOHA 기반 시연 데이터 수집. 모방 학습의 데이터 병목 해결

## 6. NLP 세부 태스크

60. ner-named-entity-recognition | 개체명 인식 심화 (NER 심화) | concepts | concept | BIO/BIOES 태그, 중첩 NER, 중국어 문자 레벨 NER. SpanNER, 생성 모델 NER
61. relation-extraction | 관계 추출 (Relation Extraction) | concepts | concept | 개체 쌍 간 관계 분류. 원격 감독, 생성 모델 기반 RE. DocRED 벤치마크
62. coreference-resolution | 상호참조 해석 (Coreference Resolution) | concepts | concept | 동일 지시체 언급 연결. End-to-End 신경망, 스팬 표현, OntoNotes 벤치마크
63. dependency-parsing | 의존 구문 분석 (Dependency Parsing) | concepts | concept | 단어 간 문법 의존 관계 트리. Arc-Standard/Arc-Eager, Biaffine Parser
64. constituency-parsing | 구성 구문 분석 (Constituency Parsing) | concepts | concept | 문장을 구 단위 계층 트리로. CYK, 신경 파서, PTB 벤치마크
65. semantic-role-labeling | 의미역 레이블링 (SRL) | concepts | concept | 술어-논항 구조 인식. PropBank 역할. 사건 이해의 구조화
66. event-extraction | 사건 추출 (Event Extraction) | concepts | concept | 텍스트에서 사건 트리거와 논항 추출. ACE/ERE 데이터셋. 구조화 정보 추출
67. question-answering-extractive | 추출형 QA (Extractive QA) | concepts | concept | SQuAD 스타일 지문 내 스팬 추출. BiDAF, BERT QA Head, 불가능 질문 처리
68. information-extraction-pipeline | 정보 추출 파이프라인 | applications | concept | NER→RE→사건추출→지식그래프 구축 E2E. OpenIE, 도메인 특화 IE
69. text-summarization | 텍스트 요약 (Extractive/Abstractive) | applications | concept | 추출형 vs 생성형 요약. ROUGE 평가, 팩트 일관성, 장문 요약
70. machine-translation-modern | 현대 기계 번역 (mT5/NLLB/Seamless) | applications | concept | 200개 언어 지원. NLLB-200, SeamlessM4T 멀티모달 번역
71. sentiment-analysis-aspect | 측면 기반 감성 분석 (ABSA) | applications | concept | 문장 전체 감성이 아닌 속성(가격/서비스)별 감성. 제품 리뷰 분석
72. grammatical-error-correction | 문법 오류 교정 (GEC) | applications | concept | GEC 태스크: CoNLL-2014 벤치마크. T5/GECToR 기반. 영어 학습자 지원

## 7. 적대적 머신러닝 (Adversarial ML)

73. fgsm-fast-gradient-sign | FGSM - 고속 그래디언트 부호 공격 | concepts | concept | Goodfellow 2015. 입력 기울기 방향으로 최소 섭동. 적대적 사례의 시발점
74. pgd-adversarial-training | PGD - 투영 경사하강 적대적 훈련 | concepts | concept | Madry et al. 2018. 반복적 FGSM. PGD 적대적 훈련이 강건성 표준으로 정립
75. carlini-wagner-attack | Carlini-Wagner (C&W) 공격 | concepts | concept | 최적화 기반 적대적 공격. L2/L0/Linf 거리 최소화. 강한 기준선 공격
76. adversarial-robustness-certified | 인증된 강건성 (Certified Robustness) | concepts | concept | 섭동 반경 내 예측 보장. 랜덤화 스무싱(Cohen et al.), 형식적 검증 방법
77. robustness-generalization-tradeoff | 강건성-정확도 트레이드오프 | concepts | concept | 적대적 훈련이 표준 정확도를 낮추는 현상. 자연 강건성 vs 적대적 강건성
78. adversarial-patch-physical | 물리적 적대적 패치 | concepts | concept | 실세계에서 인쇄 가능한 패치로 객체 검출기 우회. 자율주행 안전 위협
79. natural-adversarial-examples | 자연 적대적 사례 (Natural Adversarial Examples) | concepts | concept | 조작 없이 자연 발생하는 오분류 사례. ObjectNet, ImageNet-A/O
80. data-poisoning-attacks | 데이터 오염 공격 (Data Poisoning) | concepts | concept | 훈련 데이터 조작으로 모델 성능/행동 저하. Backdoor vs Dirty-Label 공격
81. backdoor-attack-defense | 백도어 공격과 방어 (Trojan Attacks) | concepts | concept | 특정 트리거 입력 시 오작동. Neural Cleanse, Fine-Pruning 방어
82. autoattack-benchmark | AutoAttack - 표준화 강건성 평가 | concepts | concept | 앙상블 적대적 공격. 강건성 주장 검증 표준. RobustBench 리더보드

## 8. ML 시스템 내부 (ML Systems Internals)

83. deepspeed-zero-internals | DeepSpeed ZeRO 내부 구현 | tooling | concept | Stage 1/2/3 파라미터 분할 내부 메커니즘. 통신 최적화, 오프로딩 스케줄
84. megatron-lm-internals | Megatron-LM 내부 구현 | tooling | concept | 텐서/파이프라인/시퀀스 병렬화 구현 상세. 마이크로배치 스케줄링, MCore v0.11
85. pytorch-autograd-internals | PyTorch Autograd 내부 | tooling | concept | 계산 그래프 동적 구축, 역방향 패스 스케줄링, 인플레이스 연산 제약
86. pytorch-distributed-internals | PyTorch 분산 학습 내부 | tooling | concept | ProcessGroup, NCCL 백엔드, 집단 연산 구현. DDP/FSDP/TP 내부 비교
87. cuda-memory-management | CUDA 메모리 관리 | tooling | concept | 통합 메모리, HBM vs SRAM 계층, 메모리 풀링, 단편화 방지
88. triton-gpu-programming | Triton - GPU 커널 언어 | tooling | concept | Python 기반 GPU 커널 작성. FlashAttention/SoftMax 최적 커널 구현. OpenAI
89. nccl-collective-communication | NCCL 집단 통신 내부 | tooling | concept | All-Reduce/All-Gather/Reduce-Scatter 구현. Ring/Tree 알고리즘, InfiniBand/NVLink
90. model-parallelism-strategies | 모델 병렬화 전략 비교 심화 | training | concept | TP/PP/SP/EP 조합 최적화. 통신량 분석, 버블 최소화, 4D 병렬화
91. activation-recomputation | 활성화 재계산 (Gradient Checkpointing 심화) | training | concept | 순방향 재계산으로 역방향 메모리 절감. 선택적 재계산, 오프로딩 조합
92. deepspeed-arctic-lts | DeepSpeed Arctic Long Sequence Training | tooling | concept | 멀티백만 토큰 시퀀스 학습 지원. ZenFlow 비동기 오프로딩. 2025 신기능
93. megatron-bridge-checkpoint | Megatron Bridge - HF-Megatron 체크포인트 변환 | tooling | concept | HuggingFace ↔ Megatron 양방향 체크포인트 변환기. 2025-10 릴리스

## 9. 데이터 중심 AI (Data-Centric AI)

94. data-centric-ai-paradigm | 데이터 중심 AI 패러다임 | concepts | concept | 모델 고정 + 데이터 품질 개선. Andrew Ng 주창. 데이터 중심 vs 모델 중심 비교
95. data-shapley-valuation | 데이터 Shapley 가치 평가 | concepts | concept | 개별 데이터 포인트의 모델 성능 기여도. 코어셋 선택, 중독 데이터 탐지
96. influence-functions-ml | 영향 함수 (Influence Functions) | concepts | concept | Koh & Liang 2017. 훈련 포인트 제거 시 예측 변화 추정. 재학습 없이 그래디언트 기반
97. trak-attribution | TRAK - 신경망 데이터 귀속 | concepts | concept | 로지스틱 회귀 LOO 근사 → 신경망 확장. 학습 데이터 영향도 추적. 재학습 불필요
98. ggda-group-attribution | 그룹 데이터 귀속 (GGDA) | concepts | concept | 개별 → 그룹 단위 영향도 일반화. 10-50배 효율. 데이터셋 수준 기여도 분석
99. data-selection-optimal | 최적 데이터 선택 이론 | training | concept | 코어셋 선택, 커리큘럼 설계, D4 방법. 최소 데이터로 최대 성능
100. label-noise-learning | 레이블 노이즈 강건 학습 | training | concept | 노이즈 전이 행렬, 혼합 모델 기반 노이즈 모델링, 공동 학습 기법
101. dataset-distillation | 데이터셋 증류 (Dataset Distillation) | training | concept | 대형 데이터셋 → 합성 소형 대리 데이터셋. DC/MTT/CAFE 방법. 연속 학습 응용
102. data-augmentation-advanced | 고급 데이터 증강 (Mixup/CutMix/AugMix) | training | concept | Mixup/CutMix: 선형 보간 증강. AugMix: 여러 증강 체인. AutoAugment: 자동 정책 탐색
103. annotation-efficiency | 주석 효율화 기법 (Active Learning + Semi-Sup) | training | concept | 능동 학습 + 반지도 학습 조합. 레이블 비용 최소화, 불확실성 기반 쿼리

## 10. 벤치마크 세부 (Benchmarks)

104. mmlu-benchmark-details | MMLU 벤치마크 상세 | concepts | concept | 57개 과목 14,000+ 문항. 인문/STEM/전문 지식. 모델 스케일 능력 측정. 2024년 포화
105. arc-benchmark | ARC - AI2 추론 챌린지 | concepts | concept | 7,787개 초등 과학 문제. Easy/Challenge 분할. 지식+추론 결합 테스트
106. hellaswag-benchmark | HellaSwag - 상식 추론 벤치마크 | concepts | concept | 10,000개 문장 완성. 4택 선택형 상식 추론. 적대적 필터링으로 고난이도 구성
107. winogrande-benchmark | WinoGrande - 대규모 위노그라드 스키마 | concepts | concept | 44,000개 군중 소싱 + 적대적 필터링. 상식 추론. 기존 Winograd 확장
108. big-bench-hard | BIG-Bench Hard (BBH) - 어려운 추론 태스크 | concepts | concept | 23개 태스크, 단계적 복합 추론 요구. 논리 연역, 인과 추론, 알고리즘 문제
109. humaneval-mbpp | HumanEval/MBPP - 코드 생성 벤치마크 | concepts | concept | 164/374개 파이썬 프로그래밍 문제. Pass@K 평가. 함수형 정확성 테스트
110. math-benchmark | MATH 벤치마크 - 수학 문제 풀기 | concepts | concept | 12,500개 수학 경시대회 문제. 7개 분야. 단계별 해법 평가. 2024년 모델 90%+
111. gsm8k-benchmark | GSM8K - 초등 수학 문제 풀기 | concepts | concept | 8,500개 다단계 초등 수학. 체인 오브 사고(CoT) 평가 표준. 2024년 포화
112. truthfulqa-benchmark | TruthfulQA - 진실성 평가 | concepts | concept | 817개 오해 유발 질문. 인간 잘못 믿는 진술 포함. MC/생성형 평가
113. mtbench-llmjudge | MT-Bench / LLM-as-Judge 평가 | concepts | concept | 다중 턴 대화 GPT-4 심판 평가. 챗봇 아레나 ELO. 인간 평가 대안
114. livecodebench | LiveCodeBench - 오염 방지 코드 평가 | concepts | concept | 시간 기반 동적 수집. 경쟁 프로그래밍 문제. 코딩 성능 지속 추적
115. agentic-benchmarks-overview | 에이전트 벤치마크 개요 (GAIA/WebArena/OSWorld) | concepts | concept | 태스크 자동화 에이전트 평가. 도구 사용/멀티스텝/현실 환경 성공률

## 11. 강화학습 심화 (Reinforcement Learning)

116. soft-actor-critic-sac | SAC - 소프트 액터-크리틱 | foundations | concept | 엔트로피 정규화 오프-정책 연속 제어. 자동 온도 튜닝. 샘플 효율성 우수
117. td3-twin-delayed-ddpg | TD3 - 쌍둥이 지연 DDPG | foundations | concept | 이중 Q 네트워크(과대평가 방지) + 지연 정책 갱신. DDPG 개선판
118. model-based-rl-survey | 모델 기반 강화학습 (MBRL) 개요 | foundations | concept | 세계 모델 학습 + 플래닝. Dyna 프레임워크. MBPO/Dreamer/RSSM
119. dreamer-world-model | Dreamer/DreamerV3 - 잠재 세계 모델 | foundations | concept | RSSM 잠재 세계 모델로 상상 속 롤아웃 학습. 단일 알고리즘 다양한 도메인
120. offline-rl-survey | 오프라인 강화학습 개요 | foundations | concept | 고정 데이터셋으로 정책 학습. 분포 이탈 문제. CQL/IQL/TD3+BC
121. conservative-q-learning-cql | CQL - 보수적 Q-러닝 | foundations | concept | 오프라인 RL 과대평가 억제. 정책 이탈 데이터에 패널티. 오프라인 제어 표준
122. implicit-q-learning-iql | IQL - 암묵적 Q-러닝 | foundations | concept | 행동 외 보간 없이 오프라인 학습. Expectile 회귀. 오프라인 RL 단순화
123. decision-transformer | Decision Transformer - 시퀀스 모델링 RL | foundations | concept | RL을 조건부 시퀀스 생성으로. Return-to-go 조건부 자기회귀. GPT 기반 정책
124. hierarchical-rl | 계층적 강화학습 (HRL) | foundations | concept | 고수준 목표 설정 + 저수준 실행. DIAYN/HIRO/Option 프레임워크. 장기 태스크
125. multi-agent-rl-marl | 멀티에이전트 강화학습 (MARL) | foundations | concept | 여러 에이전트 협력/경쟁 학습. QMIX, MADDPG, 분산 실행-중앙 학습
126. reward-shaping-exploration | 보상 형성과 탐험 전략 | foundations | concept | 희소 보상 문제. ICM/RND 내재적 보상. Count-based 탐험. HER
127. rl-benchmark-environments | RL 벤치마크 환경 (MuJoCo/Atari/DMControl) | concepts | concept | MuJoCo 연속 제어, Atari 이산 게임, DMControl Suite, IsaacGym 로보틱스
128. inverse-rl-imitation | 역강화학습과 모방 학습 (IRL/GAIL) | foundations | concept | 보상 함수 역추론. GAIL: 전문가 데이터로 생성적 모방. BC vs DAgger

## 12. 그래프 ML (Graph ML)

129. gnn-molecular-property | GNN 분자 특성 예측 | applications | concept | 분자 그래프 → 용해도/독성/반응성 예측. MPNN/AttentiveFP. MoleculeNet 벤치마크
130. gnn-drug-discovery | GNN 기반 신약 발견 | applications | concept | 분자 생성, 약물-표적 상호작용 예측, 재창출. DMPNN/GraphDTA. FDA 파이프라인
131. ka-gnn-molecular | KA-GNN - 콜모고로프-아놀드 분자 GNN | architectures | concept | KAN 활성화 기반 분자 특성 예측 GNN. 해석 가능성 + 정확도 향상. Nature MI 2025
132. heterogeneous-graph-transformer | 이종 그래프 트랜스포머 (HGT) | architectures | concept | 다중 노드/엣지 타입 그래프 학습. 지식 그래프, 추천, 바이오 네트워크
133. link-prediction-gnn | 링크 예측 (Link Prediction) | applications | concept | 그래프 내 누락 엣지 예측. 지식 그래프 완성, 소셜 네트워크 친구 추천
134. graph-classification-pooling | 그래프 분류와 풀링 | architectures | concept | 전체 그래프 표현 학습. DiffPool/MinCutPool/SAGPool. 분자/시각 그래프 분류
135. knowledge-graph-embedding | 지식 그래프 임베딩 (TransE/RotatE) | concepts | concept | KG 트리플 → 저차원 벡터. TransE/RotatE/ComplEx. 링크 예측 + 질의 응답
136. graph-generation-molecules | 분자 그래프 생성 | applications | concept | 새로운 분자 구조 생성. GCPN/GraphAF/GDSS. 목표 특성 최적화 역설계
137. social-network-analysis-gnn | 소셜 네트워크 분석 GNN | applications | concept | 커뮤니티 탐지, 영향력 전파 예측, 허위 정보 탐지. 이종 사용자-아이템 그래프
138. protein-structure-gnn | 단백질 구조 예측 GNN | applications | concept | AlphaFold2 이후 GNN 기반 접근. 구조→기능 예측. ESMFold/ProNet
139. temporal-graph-learning | 시간적 그래프 학습 (TGN) | architectures | concept | 동적 그래프, 시간 이벤트 스트림. TGN/JODIE. 거래 그래프, 소셜 진화
140. graph-transformer-comparison | 그래프 트랜스포머 비교 (Graphormer/GPS/NodeFormer) | architectures | concept | Graphormer: 구조 인코딩 + 글로벌 어텐션. GPS: 지역+글로벌 결합 범용 아키텍처

## 13. 테이블 ML (Tabular ML)

141. xgboost-internals | XGBoost 내부 구현 심화 | foundations | concept | 2차 테일러 근사 분할 탐색. 열 샘플링/깊이 제한/정규화. 히스토그램 근사 분할
142. lightgbm-internals | LightGBM 내부 구현 심화 | foundations | concept | Leaf-wise 성장 + GOSS + EFB. XGBoost 대비 학습 속도 3-10배. 범주형 처리
143. catboost-ordered-boosting | CatBoost - 순서형 부스팅 | foundations | concept | 순서 목표 통계로 타깃 누출 방지. 범주형 특성 네이티브 처리. GPU 효율
144. tabnet-architecture | TabNet - 테이블 전용 어텐션 신경망 | architectures | concept | 순차적 어텐션 마스크로 특성 선택. 자기지도 사전학습 지원. 해석 가능
145. ft-transformer-tabular | FT-Transformer - 테이블 특성 토큰화 | architectures | concept | 각 특성을 토큰화 + 멀티헤드 셀프어텐션. 심층 학습 테이블 SOTA 경쟁
146. tabr-retrieval-augmented | TabR - 검색 증강 테이블 학습 | architectures | concept | k-NN 유사 훈련 샘플 컨텍스트 포함. 트리 기반 + 신경망 중간 성능
147. realmlp-tabular | RealMLP - 현대화된 MLP 테이블 학습 | architectures | concept | 배치 정규화/클리핑/임베딩 조합. 최신 하이퍼파라미터 튜닝. 테이블 MLP 부활
148. saint-attention-tabular | SAINT - 행열 혼합 어텐션 테이블 | architectures | concept | 행(샘플) + 열(특성) 교차 어텐션. 자기지도 사전학습. 소규모 데이터 강점
149. tabular-feature-interaction | 테이블 특성 상호작용 모델링 | concepts | concept | 2/3차 특성 상호작용. FM/DeepFM/AutoInt. 신경망이 트리 대비 유리한 시나리오
150. shap-feature-importance | SHAP 특성 중요도 설명 | concepts | concept | Shapley 값 기반 예측 설명. TreeSHAP 효율 계산. 전역/지역 해석

## 14. 시계열 (Time Series)

151. temporal-fusion-transformer | Temporal Fusion Transformer (TFT) | architectures | concept | 다변량 시계열 예측. 변수 선택 네트워크 + LSTM + 시간 어텐션. 해석 가능
152. patchtst-timeseries | PatchTST - 패치 기반 시계열 트랜스포머 | architectures | concept | 시계열을 64개 단어로 분할 패치. 채널 독립. 장기 예측 ICLR 2023. 오류 50% 감소
153. itransformer | iTransformer - 역전된 시계열 트랜스포머 | architectures | concept | 시간 스텝이 아닌 변수를 토큰화. 다변량 상관 포착 강화. ICLR 2024 Spotlight
154. timegpt-foundation | TimeGPT - 시계열 파운데이션 모델 | architectures | entity | Nixtla. 제로샷 시계열 예측. 대규모 시계열 데이터 사전학습. API 서빙
155. chronos-amazon | Chronos - Amazon 시계열 파운데이션 | architectures | entity | T5 기반 양자화 시계열 예측. 제로샷. Amazon, ICLR 2025
156. moirai-unified-forecasting | Moirai - 통합 시계열 파운데이션 (Salesforce) | architectures | entity | 다중 패치 크기 + 혼합 분포. 다양한 주기성 처리. Salesforce
157. informer-sparse-attention | Informer - 희소 어텐션 장기 예측 | architectures | concept | ProbSparse Attention으로 O(n log n) 복잡도. 인코더-디코더 장기 예측
158. n-beats-n-hits | N-BEATS/N-HiTS - 순수 MLP 시계열 | architectures | concept | 역방향+전방향 잔차 분해. 해석 가능 시계열 예측. 기저함수 분해
159. time-series-anomaly-detection | 시계열 이상 탐지 | applications | concept | 통계적 vs 신경망 기반. LSTM-AE, Transformer-AE, TranAD. 산업 IoT 모니터링
160. time-series-classification | 시계열 분류 (TSC) | applications | concept | 활동 인식, 의료 신호, 금융 패턴. ROCKET/InceptionTime/TST. UCR 아카이브
161. probabilistic-forecasting | 확률적 시계열 예측 | concepts | concept | 점 예측 → 분포/구간 예측. DeepAR, Temporal Flow, Conformal Prediction 적용
162. time-series-imputation | 시계열 결측값 보간 | applications | concept | BRITS/SAITS/TimesNet 기반 결측 처리. 의료/센서 데이터 실용 과제

## 15. 추천 시스템 (Recommendation Systems)

163. two-tower-retrieval | 두 탑 모델 (Two-Tower Retrieval) | architectures | concept | 사용자 탑 + 아이템 탑 임베딩. ANN 후보 생성. YouTube/Google 대규모 적용
164. ncf-neural-collaborative | NCF - 신경 협업 필터링 | architectures | concept | 행렬 분해 + MLP 결합. 선형/비선형 상호작용. GMF+MLP=NeuMF
165. deepfm-factorization | DeepFM - 딥 팩터라이제이션 머신 | architectures | concept | FM 2차 상호작용 + DNN 고차. 클릭률 예측. 특성 공학 없이 상호작용 학습
166. sequential-recommendation | 순차 추천 시스템 (SASRec/BERT4Rec) | architectures | concept | 사용자 행동 시퀀스 모델링. SASRec: 자기회귀 어텐션. BERT4Rec: 양방향 마스킹
167. graph-collaborative-filtering | 그래프 협업 필터링 (LightGCN/NGCF) | architectures | concept | 사용자-아이템 이분 그래프. LightGCN: 선형 전파만으로 단순화. 고차 연결성
168. dcn-deep-crossing-network | DCN-v2 - 심층 교차 네트워크 | architectures | concept | 명시적 특성 교차 + DNN. 순위 결정 모델 표준. Google, WWW 2021
169. llm-recommendation | LLM 기반 추천 시스템 | applications | concept | LLM의 언어 이해로 제로샷 추천. P5/TALLRec/BIGRec. 콜드 스타트 개선
170. multi-task-ranking | 다중 태스크 추천 순위 (MMOE/PLE) | architectures | concept | 클릭/구매/시청 다중 목표 동시 최적화. MMOE 게이팅, PLE 전문가 분리
171. cold-start-problem | 콜드 스타트 문제 | concepts | concept | 신규 사용자/아이템 추천. 콘텐츠 기반 하이브리드, 메타 학습 기반 해결
172. explore-exploit-bandit | 탐험-활용 딜레마와 밴딧 알고리즘 | concepts | concept | ε-탐욕, UCB, Thompson Sampling. 온라인 추천 A/B 테스트 대안

## 16. 개념 / 도구 / 기타

173. alexnet-imagenet-revolution | AlexNet - 딥러닝 이미지넷 혁명 | architectures | concept | 2012 ImageNet 우승. GPU 병렬 학습, ReLU, 드롭아웃 조합. 현대 딥러닝 출발점
174. vgg-deep-nets | VGGNet - 깊은 단순 CNN | architectures | concept | 3x3 합성곱 스택. 깊이의 중요성 증명. VGG-16/19. 전이 학습 백본 표준화
175. resnet-skip-connections | ResNet 잔차 학습 심화 | architectures | concept | 잔차 블록 설계 원리. 병목 블록, Pre-Activation ResNet, Wide ResNet, ResNeXt
176. inception-modules | Inception 네트워크 - 멀티스케일 합성곱 | architectures | concept | 병렬 다중 크기 합성곱. GoogLeNet/Inception-v4/Inception-ResNet. 효율적 특성 추출
177. squeeze-excitation-networks | 채널 어텐션 (SE-Net/CBAM) | architectures | concept | 채널별 중요도 재가중. SE 블록: Global Average Pool + FC. CBAM: 채널+공간 어텐션
178. deformable-convolution | 변형 가능 합성곱 (Deformable Convolution) | architectures | concept | 학습 가능한 수용 필드 오프셋. 형태 변화 강건성. Deformable DETR
179. scene-graph-generation | 장면 그래프 생성 | applications | concept | 이미지 내 객체-관계 트리플 추출. Visual Genome 데이터셋. 이미지 이해 고수준
180. image-captioning-architecture | 이미지 캡셔닝 아키텍처 | applications | concept | 인코더(CNN/ViT) + 디코더(Transformer). COCO Captions 벤치마크. 멀티모달 정렬
181. visual-question-answering | 시각적 질의응답 (VQA) | applications | concept | 이미지+질문 → 답변. VQA v2 벤치마크. 멀티모달 추론 능력 평가
182. zero-shot-learning | 제로샷 학습 (Zero-Shot Learning) | concepts | concept | 보지 않은 클래스 일반화. 속성/의미 벡터 공간 전이. CZSL vs GZSL
183. few-shot-image-classification | 퓨샷 이미지 분류 | concepts | concept | 5-way 1-shot/5-shot. Prototypical Network/Matching Network/MAML. miniImageNet
184. self-distillation | 자기 증류 (Self-Distillation) | training | concept | 같은 모델이 교사-학생 역할 동시. 레이블 스무딩 효과. Born-Again Networks
185. knowledge-graph-construction | 지식 그래프 구축 파이프라인 | applications | concept | 개체명 인식 → 관계 추출 → 온톨로지 정렬 → 지식베이스 구축 E2E
186. multimodal-alignment | 멀티모달 정렬 기법 | architectures | concept | 텍스트-이미지-오디오 표현 정렬. CLIP/SigLIP 대조 학습, 크로스 어텐션 융합
187. retrieval-augmented-generation-paper | RAG 원논문 (Lewis et al. 2020) | papers | paper | Dense Retriever + Seq2Seq 생성기 결합 최초 제안. 지식 집약적 NLP 태스크
188. t5-text-to-text | T5 - 텍스트-투-텍스트 전이 학습 | architectures | entity | 모든 NLP 태스크를 텍스트 생성으로 통합. C4 학습. 인코더-디코더 파인튜닝 표준
189. llm-calibration | LLM 보정 (Calibration) | concepts | concept | 예측 신뢰도 = 실제 정확도. Temperature Scaling/Platt. 안전 AI 필수 속성
190. uncertainty-quantification | 불확실성 정량화 (UQ) | concepts | concept | 인식론적 vs 우연적 불확실성. MC Dropout, 앙상블, 컨포멀 예측
191. emergent-abilities-llm | 창발적 능력 (Emergent Abilities) | concepts | concept | 임계 스케일 이상에서 갑자기 나타나는 능력. 소수샷 학습, 사슬 추론. 예측 불가
192. chain-of-thought-prompting | 체인 오브 사고 (Chain-of-Thought) 프롬프� | concepts | concept | 단계별 추론 예시로 복잡 문제 해결. Wei et al. 2022. Zero-shot CoT "단계적으로"
193. prompt-engineering-survey | 프롬프트 엔지니어링 종합 | concepts | concept | 제로샷/퓨샷/체인/트리/자동 프롬프트 비교. 구조화 출력, 롤 지정, 시스템 프롬프트
194. in-context-learning-mechanics | 인컨텍스트 학습 메커니즘 | concepts | concept | 가중치 갱신 없이 데모로 학습. 잠재 개념 식별, 베이지안 추론 해석, 귀납 헤드
195. tool-augmented-language-models | 도구 증강 언어 모델 (TALM/ToolFormer) | concepts | concept | LLM에 계산기/검색/코드 실행 통합. ToolFormer 자기지도 도구 학습
196. constitutional-classifiers | Constitutional Classifiers - 원칙 기반 분류기 | concepts | concept | 헌법적 원칙으로 학습된 안전 분류기. 탈옥 성공률 86%→4.4%. Anthropic 2025
197. llm-agent-security | LLM 에이전트 보안 심화 | concepts | concept | 프롬프트 인젝션/데이터 유출/권한 상승. OWASP 에이전트 Top 10 구현 대응
198. multimodal-benchmark | 멀티모달 벤치마크 (MMBench/MMMU/SeedBench) | concepts | concept | VLM 능력 종합 평가. 지각/추론/지식 다차원 평가. 다국어 지원
199. chain-of-thought-tree | Tree-of-Thought (ToT) 추론 | concepts | concept | 다중 추론 경로 탐색 + 평가. BFS/DFS 기반 복잡 문제 해결
200. model-editing-techniques | 모델 편집 기법 (ROME/MEMIT) | concepts | concept | 재학습 없이 특정 사실 수정. 인과 추적, 랭크-1 업데이트. 지식 갱신
201. sparse-mixture-of-experts-theory | MoE 이론과 부하 분산 심화 | architectures | concept | Expert Capacity, Auxiliary Loss, Load Balancing. Switch Transformer/GShard 이론
202. neural-program-synthesis | 신경 프로그램 합성 | applications | concept | 자연어/예제 → 프로그램 코드 생성. DreamCoder, AlphaCodium, 귀납적 프로그래밍
203. llm-long-context-faithfulness | 장문 컨텍스트 신뢰성 (Lost in the Middle) | concepts | concept | 중간 위치 정보 손실 현상. 위치 편향, 컨텍스트 윈도우 활용도 분석
204. mixture-of-agents-theory | MoA 이론 - 모델 앙상블 원리 | concepts | concept | LLM 앙상블의 이론적 근거. 다양성-정확도 트레이드오프. 집단 추론 품질 향상
205. activation-function-theory | 활성화 함수 이론 심화 | foundations | concept | Universal Approximation 조건. SiLU/Mish/APTx 비교. 활성화 패턴 분석
206. pruning-structured-unstructured | 프루닝 심화 (구조적/비구조적/반구조적) | inference | concept | 가중치/채널/헤드 프루닝. N:M 스파시티. SparseGPT/Wanda PTQ 프루닝
207. quantization-aware-training | 양자화 인식 학습 (QAT) | training | concept | 훈련 중 양자화 시뮬레이션. Straight-Through Estimator. PTQ vs QAT 비교
208. knowledge-distillation-theory | 지식 증류 이론 심화 | training | concept | 소프트 레이블의 "암흑 지식". 온도 매개변수. 기능/관계/어텐션 증류 유형
209. lora-theory-mechanism | LoRA 이론과 메커니즘 심화 | training | concept | 저랭크 분해의 이론적 근거. 행렬 공간 분석. 랭크 선택, AdaLoRA, DoRA 확장
210. peft-adapter-survey | PEFT 방법 전체 비교 (Adapter/Prefix/Prompt) | training | concept | 어댑터/프리픽스 튜닝/프롬프트 튜닝/LoRA/IA3 비교. 파라미터 효율 전략 선택 기준
211. evaluation-contamination-dynamic | 동적 벤치마크와 오염 방지 | concepts | concept | 정적 벤치마크 오염 문제. 시간 기반/생성형 동적 벤치마크. LiveBench/LiveCodeBench
212. mechanistic-interpretability-circuits | 메커니즘 해석가능성 - 회로 분석 | concepts | concept | 어텐션 헤드 기능 식별. 귀납 헤드/스킵 트리그램. 행동의 회로 수준 설명
213. superalignment-research | 수퍼얼라인먼트 연구 | concepts | concept | 초인간 AI 정렬 준비. Weak-to-Strong, 확장 가능한 감독, 자동화된 해석가능성
214. constitutional-ai-pipeline | Constitutional AI 파이프라인 심화 | training | concept | CAI Critique-Revision 루프 상세. RLAIF 확장. 헌법 구성 원칙 설계 방법론
215. ai-governance-regulation | AI 거버넌스와 규제 현황 | concepts | concept | EU AI Act, EO 14110, 중국 AI 규정. 고위험 AI 분류, 준수 요건, 오픈소스 예외

---

## 우선순위 가이드

**즉시 생성 권장 (기초 누락 토픽)**
- 1-14번: 비전 트랜스포머 세부 (ViT 패치 설계, BEiT, DeiT 등)
- 73-82번: 적대적 ML (FGSM/PGD/인증 강건성 - 기초 개념 전무)
- 116-128번: 강화학습 심화 (SAC/TD3/오프라인 RL - 현재 RLHF 위주)
- 141-150번: 테이블 ML (XGBoost 내부/TabNet/LightGBM - 실용 누락)
- 151-162번: 시계열 (PatchTST/TFT/iTransformer - 완전 누락 카테고리)
- 163-172번: 추천 시스템 (두 탑/NCF/DeepFM - 실용 누락)

**중간 우선순위**
- 15-28번: 음성/오디오 (Whisper/VALL-E/AudioLM 상세)
- 39-49번: 3D/NeRF (NeRF/3DGS/PointNet 기초)
- 94-103번: 데이터 중심 AI (Shapley/영향 함수)
- 104-115번: 벤치마크 상세 (MMLU/ARC/HellaSwag)

**낮은 우선순위 (관련 페이지 이미 존재)**
- 173-215번: 기타 개념 (일부 관련 페이지 존재, 심화 확장 목적)

---

*수집 기준일: 2026-04-17*
*기준 위키 규모: 1,108 페이지*
*신규 토픽 수: 215개*
*다음 배치 ingest 대상: /wiki-ingest 실행*

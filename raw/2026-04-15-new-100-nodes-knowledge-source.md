# AI Wiki 신규 100개 노드 지식소스

> 생성일: 2026-04-15
> 목적: 기존 위키 ~400페이지 대비 갭 분석 후, 웹 리서치와 결합해 선별한 신규 노드 100개 후보
> 방법론: 6단계 병렬 리서치 (Foundations 갭 / Architectures 갭 / Training 갭 / Inference+RAG 갭 / 2025-2026 트렌드 / 핵심 논문+개념)
> 용도: /wiki-ingest 스킬로 위키 페이지 일괄 생성 시 입력 소스

---

## Foundations (기초) - 20개

### 1. 학습률 스케줄링 (Learning Rate Scheduling)
- **page_type**: concept
- **설명**: Warmup, Cosine Annealing, Step Decay, OneCycleLR 등 학습 과정에서 학습률을 동적으로 조절하는 기법. Transformer 학습에서 Warmup이 필수.
- **연결**: optimization-theory.md (단락 수준 언급만), training/adamw-optimizer.md, architectures/transformer-architecture.md
- **핵심 내용**: warmup 필요성의 수학적 근거, cosine annealing vs linear decay 비교, WSD(Warmup-Stable-Decay) 스케줄 (Llama 3/DeepSeek 사용), 실전 선택 가이드

### 2. 자동 미분 심화 (Automatic Differentiation Deep Dive)
- **page_type**: concept
- **설명**: Forward mode vs Reverse mode AD, Computational Graph 구축, PyTorch Autograd/JAX의 내부 동작 원리
- **연결**: gradient-descent-backpropagation.md (짧은 섹션만), training 전반
- **핵심 내용**: 수치 미분 vs 기호 미분 vs 자동 미분, Wengert tape, custom gradient 작성, JAX의 vmap/jit/grad 합성

### 3. 앙상블 방법론 (Ensemble Methods: Bagging, Boosting, Stacking)
- **page_type**: concept
- **설명**: Bagging(Bootstrap Aggregating), Boosting(AdaBoost/Gradient Boosting), Stacking의 원리와 이론적 근거
- **연결**: decision-trees-random-forests.md (RF=Bagging이지만 이론 부재), 앙상블이 단일 모델보다 우수한 이유의 편향-분산 분해
- **핵심 내용**: bias-variance decomposition에서 앙상블의 효과, XGBoost/LightGBM/CatBoost 비교, 모델 다양성(diversity)의 중요성

### 4. 나이브 베이즈 (Naive Bayes Classifier)
- **page_type**: concept
- **설명**: 조건부 독립 가정, 가우시안/다항/베르누이 NB, 생성 모델 vs 판별 모델 비교
- **연결**: probability-statistics-for-ml.md (베이즈 정리만), 텍스트 분류 역사적 베이스라인
- **핵심 내용**: Laplace smoothing, 문서 분류에서의 TF-IDF + NB 파이프라인, spam 필터 사례

### 5. EM 알고리즘과 가우시안 혼합 모델 (EM Algorithm & GMM)
- **page_type**: concept
- **설명**: Expectation-Maximization의 수렴 증명, GMM을 통한 소프트 군집화, K-Means와의 관계
- **연결**: k-means-clustering.md (GMM 한 줄 언급), probability-statistics-for-ml.md, autoencoders-vae.md (잠재 공간)
- **핵심 내용**: E-step/M-step 수식, ELBO 최적화와의 연결 (VAE의 이론적 기초), 혼합 모델의 실용적 한계

### 6. 선형 회귀와 최소제곱법 (Linear Regression & OLS)
- **page_type**: concept
- **설명**: OLS 해석적 풀이, 정규방정식, 다중 회귀, 다항 회귀, 가정 검정
- **연결**: logistic-regression.md (있지만 선형 회귀 없음), supervised-unsupervised-reinforcement.md
- **핵심 내용**: 정규방정식 유도, Ridge/Lasso의 기하학적 해석, 다중공선성, 회귀 진단

### 7. 차원 축소 시각화 (t-SNE & UMAP)
- **page_type**: concept
- **설명**: t-SNE의 Student-t 분포 트릭과 Perplexity 파라미터, UMAP의 리만 기하 기반 알고리즘
- **연결**: pca.md (선형 차원 축소만), feature-engineering.md (한 줄 언급), LLM 임베딩 공간 분석에 필수
- **핵심 내용**: t-SNE vs UMAP 속도/품질 비교, perplexity 선택, 고차원 임베딩 시각화 실전 가이드

### 8. 그래프 신경망 기초 (Graph Neural Networks)
- **page_type**: concept
- **설명**: GCN, GAT, GraphSAGE의 메시지 패싱 원리, 분자 구조/소셜 네트워크/지식그래프 응용
- **연결**: 위키 전체에 GNN 전용 페이지 없음, RAG의 knowledge graph, attention-mechanism-overview.md (GAT)
- **핵심 내용**: 메시지 패싱 프레임워크, GCN 스펙트럴/공간 관점, GAT의 어텐션 가중치, over-smoothing 문제

### 9. 자기지도 학습 (Self-Supervised Learning)
- **page_type**: concept
- **설명**: Contrastive Learning(SimCLR, MoCo), Masked Prediction(BERT, MAE), BYOL의 레이블 없는 표현 학습
- **연결**: transfer-learning.md (짧은 언급), Foundation Model 사전학습의 핵심, architectures/bert.md
- **핵심 내용**: pretext task 설계, contrastive vs generative 비교, 비전(MAE/DINO) vs 언어(MLM/CLM) 패턴

### 10. Word2Vec과 FastText (Word Embeddings)
- **page_type**: concept
- **설명**: CBOW vs Skip-gram, Negative Sampling, 서브워드 모델(FastText), 단어 유추 태스크
- **연결**: transfer-learning.md (ELMo 표 언급만), Transformer 임베딩의 역사적 맥락
- **핵심 내용**: Softmax 병목과 Negative Sampling 해법, Word2Vec의 선형 하부구조, GloVe(PMI 행렬 분해) 비교

### 11. 임베딩 레이어 (Embedding Layers & Representation Learning)
- **page_type**: concept
- **설명**: 룩업 테이블로서의 임베딩, Positional Embedding, 멀티모달 임베딩, 임베딩 공간의 기하학
- **연결**: 여러 파일에서 "임베딩" 언급되나 전용 페이지 없음, attention-mechanism-overview.md, rag/ 전체
- **핵심 내용**: 원-핫 -> 밀집 벡터 변환, 위치 임베딩(sinusoidal/learned/RoPE), 공유 임베딩(tied embeddings)

### 12. 통계적 언어 모델 기초 (N-gram & Neural Language Models)
- **page_type**: concept
- **설명**: N-gram 모델, Perplexity 지표, 신경망 언어 모델로의 전환, 다음 토큰 예측의 수학적 정의
- **연결**: cross-entropy-loss.md (next-token-prediction 태그), GPT/BERT 사전학습 목표의 전제 개념
- **핵심 내용**: 마르코프 가정, 데이터 희소성과 스무딩, Bengio 2003 신경 LM, autoregressive vs masked LM 분화

### 13. Seq2Seq와 인코더-디코더 (Sequence-to-Sequence Models)
- **page_type**: concept
- **설명**: Encoder-Decoder 아키텍처, Teacher Forcing, Beam Search, Attention이 Seq2Seq에 추가된 이유
- **연결**: rnn-lstm-gru.md와 attention-mechanism-overview.md 사이의 중간 개념, Transformer의 선행 지식
- **핵심 내용**: Sutskever et al. 2014, Teacher Forcing의 exposure bias, Bahdanau attention의 정렬 메커니즘

### 14. 정보 이론 기초 (Information Theory: Entropy, Mutual Information)
- **page_type**: concept
- **설명**: Shannon Entropy, Joint/Conditional Entropy, Mutual Information, 정보 이론과 ML 손실 함수의 연결
- **연결**: cross-entropy-loss.md (있지만 Entropy 자체 정의 부재), autoencoders-vae.md (ELBO), loss-functions.md
- **핵심 내용**: Shannon의 코딩 정리, 크로스 엔트로피 = 엔트로피 + KL, MI의 feature selection 응용

### 15. KL 발산과 정보 기하학 (KL Divergence Deep Dive)
- **page_type**: concept
- **설명**: KL 발산의 비대칭성, Forward vs Reverse KL의 행동 차이, VAE ELBO에서의 역할, f-Divergence 계열
- **연결**: loss-functions.md (짧은 언급), autoencoders-vae.md (ELBO 수식), gans.md (JS divergence)
- **핵심 내용**: mode-seeking(reverse) vs mode-covering(forward), VAE의 posterior collapse와 KL, DPO에서의 KL 페널티

### 16. 베이즈 추론 심화 (Bayesian Inference & Bayesian DL)
- **page_type**: concept
- **설명**: 사후 분포 계산, MCMC, Variational Inference, 불확실성 정량화, MC Dropout
- **연결**: probability-statistics-for-ml.md (MLE/MAP 비교표만), 의료/자율주행 응용
- **핵심 내용**: 사후 분포 근사의 계산적 도전, Variational Inference(VI) = ELBO 최적화, MC Dropout으로 불확실성 추정

### 17. 마르코프 결정 과정 (Markov Decision Process)
- **page_type**: concept
- **설명**: 상태/행동/보상/전이 함수의 수학적 정의, 벨만 방정식, 정책과 가치 함수
- **연결**: supervised-unsupervised-reinforcement.md (RL 개요만), RLHF 이해의 수학적 기초
- **핵심 내용**: Bellman expectation/optimality equation, discount factor의 역할, value iteration vs policy iteration

### 18. Q-러닝과 DQN (Q-Learning & Deep Q-Network)
- **page_type**: concept
- **설명**: Q-value 업데이트 규칙, epsilon-greedy 정책, Experience Replay, Target Network, Atari DQN
- **연결**: MDP (17번), RLHF->PPO의 RL 계보 출발점
- **핵심 내용**: off-policy 학습, deadly triad(함수 근사+부트스트래핑+off-policy), Double DQN, Dueling DQN

### 19. 정책 경사법 (Policy Gradient & REINFORCE & PPO)
- **page_type**: concept
- **설명**: REINFORCE 알고리즘, Actor-Critic, PPO의 Clipped Objective, RLHF에서 PPO의 역할
- **연결**: MDP (17번), training/ppo-for-llms.md (있지만 foundations 수준 이론 부재)
- **핵심 내용**: 정책 경사 정리(policy gradient theorem), 분산 감소 기법(baseline), GAE(Generalized Advantage Estimation)

### 20. 대조 학습 (Contrastive Learning & Metric Learning)
- **page_type**: concept
- **설명**: Triplet Loss, Contrastive Loss, SimCLR의 NT-Xent Loss, 임베딩 공간에서 유사도 학습
- **연결**: loss-functions.md (표 언급만), architectures/clip.md, rag/ 임베딩 품질
- **핵심 내용**: positive/negative pair 구성 전략, hard negative mining, temperature 파라미터의 역할, CLIP의 contrastive loss

---

## Architectures (모델 구조) - 15개

### 21. GPT 아키텍처 계보 (GPT Architecture Lineage)
- **page_type**: concept
- **설명**: GPT-1에서 시작된 디코더 전용 자기회귀 사전학습의 구체적 설계 결정(causal mask, context scaling)
- **연결**: encoder-decoder-architectures.md (GPT 언급만), transformer-architecture.md
- **핵심 내용**: GPT-1(12L/117M) -> GPT-2(1.5B, zero-shot) -> GPT-3(175B, few-shot) -> GPT-4(MoE추정) 설계 변천, 각 세대별 핵심 혁신

### 22. Seq2Seq + Attention (Bahdanau/Luong, Pre-Transformer)
- **page_type**: concept
- **설명**: RNN 기반 인코더-디코더에 소프트 어텐션 정렬을 결합한 구조. Transformer의 직접 전조이자 어텐션 개념 기원
- **연결**: transformer-architecture.md (선행 기술), attention-mechanism-overview.md, rnn-lstm-gru.md
- **핵심 내용**: Bahdanau(additive) vs Luong(multiplicative) attention, 정렬 행렬 시각화, 정보 병목 해결

### 23. Swin Transformer (계층적 윈도우 비전 트랜스포머)
- **page_type**: entity
- **설명**: 패치를 윈도우 단위로 분할해 로컬 어텐션 수행, 계층적 다중 스케일 특징 맵 생성
- **연결**: vision-transformer.md (Swin 언급만), cnn.md (CNN과 ViT의 중간 지점)
- **핵심 내용**: shifted window partitioning, 4단계 해상도 축소, 밀집 예측(세그멘테이션/검출) 백본 표준, Swin V2 확장

### 24. ConvNeXt (순수 CNN의 현대화)
- **page_type**: entity
- **설명**: ViT 설계 원칙(7x7 커널, GeLU, LayerNorm, Depthwise Conv)을 ResNet에 이식해 ViT와 동등 성능 달성
- **연결**: vision-transformer.md, cnn.md, "ConvNet vs Transformer" 논쟁의 핵심 데이터 포인트
- **핵심 내용**: 7가지 "modernization" 단계별 성능 변화, ConvNeXt V2(FCMAE 자기지도학습), 순수 CNN 재평가

### 25. DINOv2 (자기증류 비전 표현학습)
- **page_type**: entity
- **설명**: 레이블 없이 teacher-student 자기증류로 ViT를 학습. 범용 시각 표현(분류/세그멘테이션/깊이)
- **연결**: vision-transformer.md, clip.md (대비 학습과 비교), self-supervised-learning (9번)
- **핵심 내용**: DINO v1의 self-distillation, v2의 LVD-142M 대규모 데이터 큐레이션, ViT-g/14 레지스터 토큰

### 26. MAE (Masked Autoencoders)
- **page_type**: concept
- **설명**: ViT 패치의 75%를 마스킹 후 픽셀 수준 복원으로 사전학습. BERT의 마스킹을 비전에 적용
- **연결**: vision-transformer.md, bert.md (MLM의 비전 대응), autoencoders-vae.md
- **핵심 내용**: 높은 마스킹 비율(75%)이 핵심인 이유, 비대칭 인코더-디코더 설계, 비전 사전학습 효율성

### 27. 잠재 확산 모델 (Latent Diffusion Model / LDM)
- **page_type**: concept
- **설명**: VAE 잠재 공간에서 확산 과정을 수행해 픽셀 공간 대비 연산 수십 배 절감. Stable Diffusion 핵심
- **연결**: diffusion-transformer.md, u-net.md, diffusion-models.md (DDPM만), autoencoders-vae.md
- **핵심 내용**: 2단계 학습(VAE -> Diffusion), 조건화(conditioning) 메커니즘, classifier-free guidance, SDXL/SD3 진화

### 28. Flow Matching (연속 정규화 흐름 기반 생성)
- **page_type**: concept
- **설명**: 노이즈에서 데이터로의 확률 경로를 ODE로 정의하고 벡터장을 회귀 학습. SD3/Flux에 채택
- **연결**: diffusion-transformer.md, diffusion-models.md, 확산보다 훈련 단순/샘플링 고속
- **핵심 내용**: Conditional Flow Matching, Optimal Transport 경로, Rectified Flow, DDPM과의 수학적 관계

### 29. Consistency Models (단일 스텝 확산 생성)
- **page_type**: concept
- **설명**: 확산 ODE 궤적의 임의 점에서 동일 원점 출력을 학습. 1-2 스텝 생성
- **연결**: diffusion-models.md (언급만), diffusion-transformer.md
- **핵심 내용**: self-consistency property, Consistency Training vs Distillation, LCM(Latent Consistency Model), 실시간 생성

### 30. VLM 아키텍처 패턴 (Flamingo / BLIP-2 / LLaVA)
- **page_type**: concept
- **설명**: 비전 인코더(ViT)를 LLM에 연결하는 3가지 주요 방식의 비교
- **연결**: clip.md, vision-transformer.md, encoder-decoder-architectures.md
- **핵심 내용**: Flamingo(Perceiver Resampler + gated cross-attention), BLIP-2(Q-Former bridge), LLaVA(linear projection), 각 방식의 장단점

### 31. Cross-Attention (교차 어텐션 메커니즘)
- **page_type**: concept
- **설명**: 쿼리는 디코더, 키-밸류는 인코더에서 오는 어텐션. 멀티모달/확산 모델의 조건화 핵심
- **연결**: self-attention-mechanism.md (self-attention만), transformer-architecture.md, diffusion-transformer.md
- **핵심 내용**: self vs cross attention 수식 차이, 확산 모델의 텍스트 조건화, VLM의 시각-언어 정합

### 32. Linear Attention (커널화 어텐션 근사)
- **page_type**: concept
- **설명**: Softmax를 커널 함수로 근사해 O(n^2) -> O(n) 복잡도 달성. Performer/GLA의 이론적 기반
- **연결**: gated-deltanet.md (GDN은 있으나 일반 개념 없음), self-attention-mechanism.md
- **핵심 내용**: 커널 트릭, Performer의 FAVOR+ 메커니즘, GLA(Gated Linear Attention), 정확도-효율 트레이드오프

### 33. State Space Models 일반 (S4 / H3 / Mamba 계보)
- **page_type**: concept
- **설명**: 이산 선형 시불변 시스템을 HiPPO 행렬로 구조화. Mamba-3만 있고 S4/H3/Mamba-1/2 계보 부재
- **연결**: mamba-3.md (최신 버전만), gated-deltanet.md, rnn-lstm-gru.md (역사적 연결)
- **핵심 내용**: S4의 HiPPO 행렬, H3의 게이팅, Mamba-1의 선택적 SSM, Mamba-2의 SSD(State Space Duality)

### 34. RWKV (Receptance Weighted Key Value)
- **page_type**: entity
- **설명**: RNN 방식 재귀 추론 + Transformer 방식 병렬 훈련 결합. O(1) 추론, GPT 호환 API
- **연결**: mamba-3.md, gated-deltanet.md, rnn-lstm-gru.md
- **핵심 내용**: WKV 메커니즘, TimeMix/ChannelMix, RWKV-5/6/7 진화, 오픈소스 커뮤니티 주도 개발

### 35. xLSTM (Extended Long Short-Term Memory)
- **page_type**: entity
- **설명**: sLSTM(스칼라 메모리)+mLSTM(행렬 메모리)로 LSTM 확장. Sepp Hochreiter(LSTM 원저자) 팀의 부활작
- **연결**: mamba-3.md, gated-deltanet.md, rnn-lstm-gru.md (LSTM 직접 확장), titans-miras.md
- **핵심 내용**: 지수 게이팅, mLSTM의 covariance update, xLSTM[7:1] 혼합 비율, Transformer/SSM과의 스케일링 비교

---

## Training (학습) - 15개

### 36. Expert Parallelism (전문가 병렬화)
- **page_type**: concept
- **설명**: MoE 모델 학습에서 expert를 GPU에 분산 배치하는 기법. 텐서/파이프라인 병렬화와 독립
- **연결**: tensor-pipeline-parallelism.md, architectures/mixture-of-experts.md, deepseek-v3-training.md
- **핵심 내용**: all-to-all 통신, expert 부하분산, DeepSeek의 보조손실 없는 라우팅, Mixtral의 자연적 분산

### 37. Gradient Clipping (그래디언트 클리핑)
- **page_type**: concept
- **설명**: 그래디언트 폭발 방지를 위한 norm/value 클리핑 기법
- **연결**: gradient-norm-monitoring.md (모니터링 관점), training-stability.md (종합), loss-spike-debugging.md
- **핵심 내용**: norm clipping vs value clipping, 임계값 선택(1.0 vs adaptive), per-layer vs global, AGC(Adaptive Gradient Clipping)

### 38. FlashAttention (IO-Aware Exact Attention)
- **page_type**: concept
- **설명**: 타일링과 재계산으로 HBM I/O를 최소화하는 정확한 어텐션 알고리즘. 학습 효율 관점
- **연결**: 인퍼런스 카테고리의 flashattention-4.md (v4), training 효율에 필수
- **핵심 내용**: memory hierarchy(SRAM vs HBM), tiling strategy, FA-1/2/3 진화, backward pass 재계산

### 39. Perplexity (퍼플렉시티 - 언어 모델 평가 지표)
- **page_type**: concept
- **설명**: 언어 모델의 표준 평가 지표. 정의, 계산식, 한계, BPB(Bits Per Byte) 변환
- **연결**: evaluation-during-training.md (등장하지만 깊이 부족), cross-entropy-loss.md
- **핵심 내용**: PPL = exp(cross-entropy), 슬라이딩 윈도우 PPL, 토크나이저 의존성, BPB로의 정규화, PPL과 벤치마크 성능의 상관

### 40. BLEU / ROUGE / METEOR (자동 평가 지표)
- **page_type**: concept
- **설명**: 번역/요약 태스크의 고전 n-gram 기반 자동 평가 지표와 한계
- **연결**: 위키 전체에 전용 페이지 없음, BERTScore/GPT-4 judge 등 대안 포함
- **핵심 내용**: BLEU(precision 기반), ROUGE(recall 기반), METEOR(정렬), LLM 시대 한계와 대안(BERTScore, COMET, LLM-as-Judge)

### 41. LLM 벤치마크 설계 원칙 (Benchmark Design Principles)
- **page_type**: concept
- **설명**: 태스크 선정, 오염 방지, 리더보드 게임화 문제, 동적 벤치마크 원칙
- **연결**: data-decontamination.md (오염 제거만), evaluation-during-training.md (학습 중 평가)
- **핵심 내용**: construct validity, 테스트셋 오염 탐지, 동적 벤치마크(LiveBench), Goodhart 법칙과 벤치마크, Chatbot Arena(ELO)

### 42. 데이터 품질 스코어링 (Data Quality Scoring & Filtering)
- **page_type**: concept
- **설명**: 사전학습 데이터의 품질을 자동으로 점수화하고 필터링하는 기법
- **연결**: pretraining-data-curation.md (전반만), fineweb-dataset.md, dclm-datacomp.md
- **핵심 내용**: fastText 분류기 기반 필터링, perplexity 기반 필터링, 휴리스틱 규칙(문장 길이/반복/특수문자), FineWeb의 C4 필터 vs 자체 필터 비교

### 43. 텍스트 중복 제거 전략 (Text Deduplication Strategies)
- **page_type**: concept
- **설명**: MinHash LSH, SimHash, suffix array 기반 정확 중복 제거 알고리즘
- **연결**: pretraining-data-curation.md (일부만), text-dedup.md (도구), 학습 효율과 모델 품질에 직접 영향
- **핵심 내용**: exact dedup(URL/hash), fuzzy dedup(MinHash/SimHash/n-gram), near-dedup threshold 선택, SemDeDup(의미론적), dedup 과도 적용의 역효과

### 44. Constitutional AI 원본 (Bai et al. 2022)
- **page_type**: concept
- **설명**: AI가 헌법 원칙으로 자기 비평/수정하는 RLAIF 방법론 원본 (2026 확장판과 별도)
- **연결**: extended-constitutional-ai.md (2026 확장판), rlhf-pipeline.md, alignment-faking.md
- **핵심 내용**: Critique-Revision 루프, Red-teaming prompts, RLAIF vs RLHF 비교, 헌법 원칙의 구성

### 45. 보상 해킹과 과최적화 (Reward Hacking & Overoptimization)
- **page_type**: concept
- **설명**: 보상 모델의 취약점을 악용해 실제 품질 없이 높은 보상을 얻는 현상
- **연결**: concepts/reward-hacking.md (있을 수 있으나 training 관점 심화 필요), rlhf-pipeline.md, kl-divergence-penalty.md
- **핵심 내용**: Goodhart's Law 적용, reward model overconfidence, KL penalty의 역할, reward hacking 탐지/완화 기법

### 46. Long-Context Training (긴 컨텍스트 학습)
- **page_type**: concept
- **설명**: RoPE 확장(YaRN, NTK-aware), position interpolation, progressive length extension, ring attention
- **연결**: sequence-length-curriculum.md (커리큘럼 관점만), architectures/long-context-scaling.md, architectures/rotary-position-embedding.md
- **핵심 내용**: 왜 학습 길이 > 추론 길이가 비효율인지, YaRN/NTK-aware/Code Llama의 interpolation 비교, ring attention/sequence parallelism

### 47. 데이터 로더 최적화 (Data Loader Optimization)
- **page_type**: concept
- **설명**: GPU 학습 병목이 흔히 데이터 I/O에서 발생. webdataset, 멀티프로세싱, prefetching, mmap
- **연결**: training-profiling.md, mfu-model-flops-utilization.md
- **핵심 내용**: PyTorch DataLoader num_workers, pin_memory, persistent_workers, webdataset/mosaic, memory-mapped 파일

### 48. LLM 하이퍼파라미터 탐색 (Hyperparameter Search for LLMs)
- **page_type**: concept
- **설명**: Proxy model 스케일링, muP(Maximal Update Parameterization), Bayesian HPO 적용
- **연결**: optimizer-selection.md, learning-rate-scheduling.md
- **핵심 내용**: muP(Yang & Hu 2022)로 작은 모델 HPO -> 큰 모델 전이, Proxy scaling laws, 실용적 HPO 범위(lr, warmup, bs)

### 49. FSDP vs DeepSpeed 비교 (Comparison Guide)
- **page_type**: concept
- **설명**: 어떤 상황에 FSDP/DeepSpeed 중 무엇을 쓰는가. 메모리/속도/생태계 트레이드오프
- **연결**: data-parallelism-fsdp.md, deepspeed-zero.md (각각 독립 존재하나 비교 없음)
- **핵심 내용**: ZeRO Stage 1/2/3 vs FSDP Shard/Full, 통신 패턴 차이, HuggingFace Accelerate 통합, Megatron-DeepSpeed 조합

### 50. 데이터 오염 탐지 (Data Contamination Detection)
- **page_type**: concept
- **설명**: 벤치마크 테스트셋이 학습 데이터에 포함되었는지 탐지하는 방법론
- **연결**: data-decontamination.md (제거 위주), benchmark-contamination.md
- **핵심 내용**: n-gram overlap 분석, membership inference attack, canary insertion, GPT-4/Llama 3 오염 사례

---

## Inference (추론/서빙) - 10개

### 51. Continuous Batching (연속 배치 처리)
- **page_type**: concept
- **설명**: 요청 도착 즉시 배치에 삽입해 GPU 유휴를 제거하는 LLM 서빙 핵심 기법
- **연결**: kv-cache.md, vllm-v1-engine.md, disaggregated-serving.md
- **핵심 내용**: static batching의 문제점, iteration-level scheduling, Orca(2022) 원본, vLLM/TensorRT-LLM의 구현 차이

### 52. Request Scheduling (요청 스케줄링)
- **page_type**: concept
- **설명**: 처리량/지연 목표에 따라 prefill/decode 작업 순서를 결정하는 서버 내 정책
- **연결**: continuous-batching (51번), disaggregated-serving.md, nvidia-dynamo.md
- **핵심 내용**: FCFS vs priority-based, prefill-priority vs decode-priority, SLA-aware scheduling, chunked prefill

### 53. Beam Search 디코딩 (Beam Search Decoding)
- **page_type**: concept
- **설명**: 폭(beam width)만큼 후보 시퀀스를 동시 유지해 더 나은 출력을 탐색하는 디코딩 알고리즘
- **연결**: concepts/decoding-strategies.md (참조), 번역/요약에서 아직 표준
- **핵심 내용**: beam width와 품질/다양성 트레이드오프, length penalty, early stopping, LLM 시대에 sampling이 beam search를 대체한 이유

### 54. Guided/Constrained Decoding (가이디드 디코딩)
- **page_type**: concept
- **설명**: JSON 스키마/문법 등 구조적 제약을 로짓 마스킹으로 강제하는 출력 제어 기법
- **연결**: xgrammar-2.md, 에이전트의 tool calling에 핵심
- **핵심 내용**: regex/CFG 기반 마스킹, Outlines/XGrammar 알고리즘, 성능 오버헤드, structured output vs constrained decoding

### 55. 온디바이스 추론 스택 (ONNX / TFLite / CoreML / ExecuTorch)
- **page_type**: concept
- **설명**: 모바일/엣지 기기에서 모델을 실행하기 위한 런타임/포맷/최적화 생태계
- **연결**: litert-lm.md, concepts/on-device-llm.md
- **핵심 내용**: ONNX(크로스플랫폼), TFLite/LiteRT(안드로이드), CoreML(iOS), ExecuTorch(PyTorch 네이티브), 양자화/pruning 파이프라인

### 56. 모델 프루닝 (Model Pruning for Inference)
- **page_type**: concept
- **설명**: 가중치/레이어를 제거해 추론 속도/메모리를 개선하는 구조적/비구조적 희소화 기법
- **연결**: ai-inference-quantization-2026.md, Sparse BitNet (training)
- **핵심 내용**: unstructured(magnitude) vs structured(channel/head/layer), N:M sparsity, SparseGPT, Wanda(Pruning 없는 pruning)

### 57. Early Exit & Adaptive Computation (적응형 계산)
- **page_type**: concept
- **설명**: 쉬운 토큰은 앞 레이어에서 조기 탈출시켜 계산량을 동적으로 줄이는 기법
- **연결**: architectures/mixture-of-experts.md (너비 방향), MoD와 상보적
- **핵심 내용**: confidence-based early exit, 레이어별 분류기 헤드, CALM(Confident Adaptive Language Modeling), 배치 추론에서의 도전

### 58. Mixture of Depths (MoD)
- **page_type**: concept
- **설명**: 토큰별로 처리할 레이어 수를 동적으로 결정해 FLOPs를 절감하는 조건부 계산
- **연결**: architectures/mixture-of-experts.md (너비 방향 희소화의 깊이 방향 상보)
- **핵심 내용**: 라우터가 각 토큰의 "중요도"를 판단, skip connection으로 레이어 우회, MoE+MoD 결합, 학습 안정성 도전

### 59. 추론 벤치마킹 (LLM Inference Benchmarking)
- **page_type**: concept
- **설명**: TTFT(Time To First Token), TPOT(Time Per Output Token), 처리량, 비용 효율 지표
- **연결**: kv-cache.md, continuous-batching (51번), 서빙 엔진 비교 기준
- **핵심 내용**: TTFT vs TPOT 분리의 중요성, ShareGPT 워크로드, 동시 사용자 수 vs 처리량, 벤치마킹 도구(LLMPerf, vLLM benchmark)

### 60. Repetition Penalty & Logit Bias (반복 패널티)
- **page_type**: concept
- **설명**: 이미 생성된 토큰의 로짓을 낮춰 루프/반복 출력을 억제하는 샘플링 제어 기법
- **연결**: concepts/decoding-strategies.md (참조), Top-k/Top-p/Temperature와 함께 사용
- **핵심 내용**: repetition penalty vs frequency penalty vs presence penalty, logit bias API, OpenAI/Anthropic/HuggingFace 구현 차이

---

## RAG (검색 증강 생성) - 10개

### 61. 청킹 전략 (Chunking Strategies for RAG)
- **page_type**: concept
- **설명**: Fixed / Recursive / Semantic 등 문서 분할 방식이 검색 품질에 미치는 영향과 최적 청크 크기
- **연결**: contextual-retrieval.md, embedding-models (62번)
- **핵심 내용**: character/token/sentence 기반, RecursiveCharacterTextSplitter, SemanticChunker, 청크 크기 vs 검색 정확도 실험, 오버랩 전략

### 62. RAG용 임베딩 모델 비교 (Embedding Models for RAG)
- **page_type**: concept
- **설명**: SBERT, BGE, E5, Voyage, Cohere Embed 등 RAG 목적 임베딩 모델 선택 기준
- **연결**: embedding-leaderboard-shakeup-2026.md, contextual-retrieval.md
- **핵심 내용**: MTEB 리더보드, instruction-tuned embeddings, 다국어 임베딩, 차원/성능 트레이드오프, matryoshka embeddings

### 63. ColBERT / Late Interaction Reranking
- **page_type**: concept
- **설명**: 쿼리/패시지 토큰 벡터를 최대 내적으로 집계해 cross-encoder 품질과 retriever 속도 동시 달성
- **연결**: rag-architecture-evolution-2026.md, hybrid-search (64번)
- **핵심 내용**: MaxSim 연산, token-level interaction, ColBERT v2 compression, RAGatouille 도구, cross-encoder와의 비교

### 64. 하이브리드 검색 & RRF (Hybrid Search & Reciprocal Rank Fusion)
- **page_type**: concept
- **설명**: BM25 + Dense 결과를 RRF 또는 선형 결합으로 합쳐 키워드/의미 검색의 장점 통합
- **연결**: rag-architecture-evolution-2026.md, contextual-retrieval.md
- **핵심 내용**: BM25의 여전한 강점, RRF 알고리즘(k=60), 가중 결합, Vespa/Weaviate의 하이브리드 검색 구현

### 65. 벡터 DB 비교 (Vector Database Comparison)
- **page_type**: concept
- **설명**: Pinecone, Weaviate, Qdrant, Chroma, pgvector, LanceDB 등 주요 벡터 DB의 실용적 비교
- **연결**: serverless-vector-dbs.md (Turbopuffer만), rag-architecture-evolution-2026.md
- **핵심 내용**: 인덱스 구조(HNSW/IVF/DiskANN), 필터링, 멀티테넌시, 비용, 셀프호스팅 vs 매니지드, pgvector의 PostgreSQL 통합

### 66. RAG 평가 메트릭 (RAG Evaluation Metrics)
- **page_type**: concept
- **설명**: Faithfulness, Answer Relevance, Context Precision 등 RAG 품질 측정 핵심 지표
- **연결**: tooling/ragas.md (도구), concepts/hallucination.md
- **핵심 내용**: Faithfulness(생성이 맥락에 근거하는가), Relevance(답이 질문에 관련있는가), Context Precision/Recall, 참조 없는 평가 가능성

### 67. 쿼리 변환 (Query Transformation & Expansion)
- **page_type**: concept
- **설명**: HyDE, Multi-Query, Step-Back 등 원본 쿼리를 변형해 검색 recall을 높이는 전처리 기법
- **연결**: agentic-rag.md, contextual-retrieval.md
- **핵심 내용**: HyDE(가설적 문서 생성), Multi-Query(다각도 쿼리 생성), Step-Back(추상화된 질문), Query Decomposition, Sub-question 분해

### 68. 임베딩 파인튜닝 (Embedding Fine-tuning for Domain Adaptation)
- **page_type**: concept
- **설명**: 도메인 특화 쌍 데이터로 임베딩 모델을 미세조정해 검색 성능을 도메인에 맞추는 기법
- **연결**: embedding-models (62번), training/lora-qlora-finetuning.md
- **핵심 내용**: contrastive fine-tuning, hard negative mining, synthetic pair generation, Matryoshka Representation Learning, 도메인 적응 사례

### 69. 멀티모달 RAG (Multimodal RAG)
- **page_type**: concept
- **설명**: 텍스트/이미지/표를 함께 인덱싱/검색해 VLM과 통합하는 RAG 확장 패턴
- **연결**: agentic-rag.md, concepts/multimodal-foundation-models.md, architectures/clip.md
- **핵심 내용**: 이미지 캡션 기반 vs 네이티브 멀티모달 임베딩, 표/차트 처리(OCR vs vision), ColPali(비전 retriever), 멀티모달 reranking

### 70. RAG 인덱싱 파이프라인 (RAG Indexing Pipeline E2E)
- **page_type**: concept
- **설명**: 수집 -> 파싱 -> 청킹 -> 임베딩 -> 업서트까지 프로덕션 RAG 데이터 파이프라인 전체 흐름
- **연결**: chunking-strategies (61번), embedding-models (62번), vector-db (65번)
- **핵심 내용**: 문서 파싱(Unstructured/LlamaParse), 메타데이터 추출, 증분 업데이트, 파이프라인 모니터링, 비용 최적화

---

## Papers (논문) - 15개

### 71. Attention Is All You Need (Vaswani et al. 2017)
- **page_type**: paper
- **설명**: Transformer 아키텍처를 처음 제안한 논문. 173,000회+ 인용. 현대 LLM의 직접적 조상
- **연결**: architectures/transformer-architecture.md, self-attention-mechanism.md

### 72. Language Models are Few-Shot Learners (GPT-3, Brown et al. 2020)
- **page_type**: paper
- **설명**: 175B 파라미터 GPT-3. In-context learning 개념을 실증한 전환점
- **연결**: concepts/in-context-learning.md, architectures/encoder-decoder-architectures.md

### 73. Training LMs to Follow Instructions with Human Feedback (InstructGPT, Ouyang et al. 2022)
- **page_type**: paper
- **설명**: SFT + RM + PPO 3단계 RLHF 파이프라인 원본. ChatGPT의 직접 선조
- **연결**: training/rlhf-pipeline.md, training/supervised-fine-tuning.md

### 74. Chain-of-Thought Prompting Elicits Reasoning in LLMs (Wei et al. 2022)
- **page_type**: paper
- **설명**: 중간 추론 단계를 생성하도록 유도하면 복잡한 추론이 창발한다는 실증
- **연결**: concepts/chain-of-thought.md, training/process-reward-models.md

### 75. Scaling Laws for Neural Language Models (Kaplan et al. 2020)
- **page_type**: paper
- **설명**: 모델 크기-데이터-연산의 멱함수 관계를 정량화한 OpenAI 스케일링 법칙 논문
- **연결**: foundations/scaling-laws.md, training/chinchilla-scaling-laws.md

### 76. Direct Preference Optimization (DPO, Rafailov et al. 2023)
- **page_type**: paper
- **설명**: RLHF의 reward model을 제거하고 closed-form으로 정책 최적화
- **연결**: training/direct-preference-optimization.md, training/rlhf-pipeline.md

### 77. LoRA: Low-Rank Adaptation of Large Language Models (Hu et al. 2021)
- **page_type**: paper
- **설명**: 파라미터 0.01%만 학습해도 full fine-tuning에 필적하는 효율적 파인튜닝
- **연결**: training/lora-qlora-finetuning.md

### 78. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al. 2020)
- **page_type**: paper
- **설명**: RAG 패턴을 처음 제안한 Facebook AI 논문. 외부 지식을 생성에 통합
- **연결**: rag/ 전체, rag/rag-architecture-evolution-2026.md

### 79. Constitutional AI: Harmlessness from AI Feedback (Bai et al. 2022)
- **page_type**: paper
- **설명**: AI가 헌법 원칙으로 자기 비평/수정하는 RLAIF 방법론 원본
- **연결**: training/extended-constitutional-ai.md, concepts/alignment-faking.md

### 80. Deep RL from Human Preferences (Christiano et al. 2017)
- **page_type**: paper
- **설명**: 인간 선호 피드백으로 보상 함수를 학습하는 RLHF의 원조 논문
- **연결**: training/rlhf-pipeline.md, Foundations/정책경사법 (19번)

### 81. Toolformer: LMs Can Teach Themselves to Use Tools (Schick et al. 2023)
- **page_type**: paper
- **설명**: LLM이 자기지도 방식으로 외부 API 호출 방법을 자율 학습
- **연결**: agents/ 전체, agents/tool-calling-optimization.md

### 82. Outrageously Large Neural Networks: Sparsely-Gated MoE Layer (Shazeer et al. 2017)
- **page_type**: paper
- **설명**: 희소 활성화 MoE를 대규모 NLP에 적용한 최초 논문. GPT-4, Mixtral의 원형
- **연결**: architectures/mixture-of-experts.md

### 83. BERT: Pre-training of Deep Bidirectional Transformers (Devlin et al. 2018)
- **page_type**: paper
- **설명**: 양방향 Transformer 사전학습으로 NLP 전이학습 혁명
- **연결**: architectures/bert.md (entity는 있지만 paper 없음)

### 84. RETRO: Improving LMs by Retrieving from Trillions of Tokens (Borgeaud et al. 2022)
- **page_type**: paper
- **설명**: 사전학습 단계에 retrieval을 통합해 25배 작은 모델로 GPT-3 성능 달성
- **연결**: rag/ 전체, 사전학습 시 검색 통합의 시초

### 85. OpenAI o1 System Card (OpenAI 2024)
- **page_type**: paper
- **설명**: Chain-of-Thought를 내재화한 최초 대규모 추론 모델 o1의 공식 시스템 카드
- **연결**: concepts/ai-reasoning-models.md, training/test-time-compute-scaling.md

---

## Concepts (개념) - 10개

### 86. 창발적 능력 (Emergent Abilities)
- **page_type**: concept
- **설명**: 스케일 임계점을 넘으면 갑자기 나타나는 능력들 (산술, 다단계 추론 등). 반론(측정 방법 의존) 포함
- **연결**: foundations/scaling-laws.md, concepts/in-context-learning.md
- **핵심 내용**: Wei et al. 2022 정의, Schaeffer et al. 2023 반론(metric mirage), 연속적 개선 vs 불연속 도약 논쟁

### 87. 아첨 (Sycophancy)
- **page_type**: concept
- **설명**: 모델이 사용자의 편향을 감지해 동의하는 방향으로 답변을 바꾸는 현상. RLHF의 부작용
- **연결**: concepts/reward-hacking.md (다른 각도), training/rlhf-pipeline.md
- **핵심 내용**: user approval-seeking 행동, 사실 정확성 저하, Anthropic의 sycophancy 측정, 완화 기법(diverse feedback, CAI)

### 88. 테스트 타임 컴퓨트 (Test-Time Compute)
- **page_type**: concept
- **설명**: 추론 시 더 많은 연산을 투입해 성능을 높이는 패러다임. o1, DeepSeek-R1의 핵심
- **연결**: training/test-time-compute-scaling.md (training 관점), concepts/ai-reasoning-models.md
- **핵심 내용**: scaling paradigm 전환(학습 컴퓨트 -> 추론 컴퓨트), best-of-N sampling, tree search, process reward model + beam search

### 89. 지시 따르기 (Instruction Following)
- **page_type**: concept
- **설명**: 자연어 지시를 해석하고 수행하는 능력. SFT/RLHF로 정렬되는 핵심 역량
- **연결**: training/instruction-tuning.md, training/rlhf-pipeline.md
- **핵심 내용**: instruction following vs instruction tuning(과정 vs 역량), IFEval 벤치마크, 복잡한 제약 조합 따르기, 실패 모드 분류

### 90. 토크나이제이션 개념 (Tokenization Concepts)
- **page_type**: concept
- **설명**: BPE, SentencePiece, Unigram 등의 개념적 이해. LLM 입출력의 가장 기본 단위
- **연결**: architectures/tokenization-bpe-sentencepiece.md (구현 상세), 언어 모델 기초(12번)
- **핵심 내용**: 토크나이저가 모델 성능에 미치는 영향, 다국어 토큰화 도전, byte-level BPE, 토큰 경계가 만드는 문제(산술, 코드 등)

---

## 2025-2026 트렌드 (신규) - 10개

### 91. AG-UI Protocol (Agent-User Interface Protocol)
- **page_type**: concept
- **category**: agents
- **설명**: 에이전트-프론트엔드 통신 표준. MCP(에이전트-도구), A2A(에이전트-에이전트)에 이은 세 번째 레이어
- **핵심 내용**: HTTP POST + SSE 스트림, TEXT_MESSAGE_CONTENT / TOOL_CALL_START / STATE_DELTA 이벤트, Google/AWS/Microsoft 채택

### 92. Reinforcement Pre-Training (RPT)
- **page_type**: concept
- **category**: training
- **설명**: 다음 토큰 예측을 순차적 의사결정 문제로 재구성해 RL로 사전학습하는 패러다임
- **출처**: Microsoft/Tsinghua/Peking, arxiv:2506.08007
- **핵심 내용**: 검증 가능한 보상으로 어노테이션 없는 RL 사전학습, SFT+RL 통합 학습

### 93. 잠재 공간 추론 (Latent Space Reasoning / Recurrent Depth)
- **page_type**: concept
- **category**: architectures
- **설명**: 토큰 생성 없이 잠재 공간에서 반복적으로 추론. Prelude+Recurrent Block+Coda 3부 구조
- **출처**: NeurIPS 2025 스포트라이트, arxiv:2502.05171
- **핵심 내용**: CoT 없이 추론 품질 향상, 작은 컨텍스트 창 동작, 특수 학습 데이터 불필요

### 94. ExecuTorch 1.0 GA (Meta On-Device AI)
- **page_type**: entity
- **category**: inference
- **설명**: PyTorch 기반 on-device 추론 프레임워크. 50KB 베이스 풋프린트, 12+ 하드웨어 백엔드
- **핵심 내용**: 마이크로컨트롤러~스마트폰 지원, Llama 3.2/Qwen3/Phi-4 지원, Meta 앱 실적

### 95. Forest-of-Thought / 멀티트리 추론
- **page_type**: concept
- **category**: training
- **설명**: 여러 추론 트리를 병렬 실행하고 집단적 의사결정으로 최종 답 도출. Tree-of-Thought의 앙상블
- **출처**: arxiv:2412.09078
- **핵심 내용**: 단일 트리 대비 복잡 논리 문제에서 유의미한 성능 향상, 최적 테스트 타임 컴퓨트 전략

### 96. 추론 칩 시장 역전 (Inference > Training Chip Demand)
- **page_type**: concept
- **category**: inference
- **설명**: 2026년 AI 추론 칩 수요가 학습 칩을 추월. 총 컴퓨트의 2/3가 추론 워크로드
- **핵심 내용**: 추론 최적화 칩 시장 $50B+, NVIDIA GTC 2026 "Inflection of Inference", 추론 비용 구조 변화

### 97. 추론 분산 계층화 (Inference Distribution: Global/Regional/Edge/Local)
- **page_type**: concept
- **category**: inference
- **설명**: AI 추론이 4계층으로 분산: 글로벌 클라우드, 지역 클라우드(규제), 엣지(실시간), 로컬(프라이버시)
- **핵심 내용**: Sovereign Inference 개념, 규제 대응 지역화, 엣지-클라우드 하이브리드 라우팅

### 98. AI 추론 컴퓨트 경제학 (Inference Compute Economics)
- **page_type**: concept
- **category**: concepts
- **설명**: Scale -> Efficiency 전환. 고품질 사전학습 데이터 고갈로 단순 규모 확장 시대 종료
- **핵심 내용**: 인프라 경쟁에서 알고리즘/효율 경쟁으로, "어떤 스케일링이 경제적 유용성으로 전환되는가"

### 99. 지속 학습의 LLM 적용 (Continual Learning for LLMs)
- **page_type**: concept
- **category**: training
- **설명**: Neural ODE + 메모리 증강으로 망각 24% 감소. "가짜 망각" 발견
- **연결**: training/continual-pretraining.md (기존)과 차별화 - 추론 시 적응 관점
- **핵심 내용**: 하위 레이어 고정, on-policy RL의 망각 완화 효과, 온라인 실시간 적응 vs 오프라인 재학습

### 100. MoE 라우팅 고도화 (Fine-grained MoE Routing)
- **page_type**: concept
- **category**: architectures
- **설명**: DeepSeek-V3 256 전문가, Qwen3-235B 초세분화 트렌드. 유사성 보존 부하분산
- **연결**: architectures/mixture-of-experts.md (일반 MoE), training/deepseek-v3-training.md
- **핵심 내용**: 라우팅 신뢰성 > 파라미터 수, 보조손실 없는 부하분산, 멀티모달 MoE 확산

---

## 카테고리별 요약

| 카테고리 | 신규 노드 수 | 주요 갭 |
|----------|-------------|---------|
| Foundations | 20 | 기초 ML 알고리즘, 정보이론, RL 기초, 표현학습 |
| Architectures | 15 | 비전/생성/멀티모달 구조, 서브쿼드라틱 대안 |
| Training | 15 | 평가 지표, 데이터 처리, 분산학습 비교, 정렬 심화 |
| Inference | 10 | 디코딩/배치/스케줄링 기초, 프루닝, 적응형 계산 |
| RAG | 10 | 청킹/임베딩/리랭킹/평가 등 실전 파이프라인 |
| Papers | 15 | 랜드마크 논문 부재 (Transformer, GPT-3, RLHF, DPO 등) |
| Concepts | 10 | 창발적 능력, 아첨, 테스트타임 컴퓨트 등 |
| 2025-2026 Trends | 5 | AG-UI, RPT, 잠재공간추론, 추론경제학, MoE고도화 |

## 활용 가이드

이 파일은 `/wiki-ingest` 스킬의 입력 소스로 사용된다:
1. 각 노드별로 개별 raw 파일을 생성하거나, 이 파일 자체를 참조해 위키 페이지를 일괄 생성
2. **Foundations 20개**를 최우선으로 - 다른 카테고리의 선행 지식 역할
3. **Papers 15개**를 두 번째로 - 기존 concept/entity 페이지에 논문 크로스링크 추가
4. 나머지 카테고리는 연결고리가 많은 순서대로 진행

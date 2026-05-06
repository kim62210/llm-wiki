# 2026-04 OpenSource AI Harvest

수집일: 2026-04-27
수집 범위: HuggingFace 트렌딩, 신규 오픈소스 모델/라이브러리, 오픈웨이트 발표 (2026년 4월 기준)

---

## 1. deepseek-v4-pro-flash | DeepSeek V4 Pro/Flash - 1.6조 파라미터 오픈웨이트 MoE | architectures | entity

- **출처**: https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/ / https://hf.co/deepseek-ai/DeepSeek-V4-Pro
- **요약**: 2026년 4월 22일 출시. V4-Pro(1.6조 파라미터, 490억 활성)와 V4-Flash 두 변형이 MIT 라이선스 오픈웨이트로 공개됨. 두 모델 모두 100만 토큰 컨텍스트 윈도우를 지원하는 MoE 구조. V4-Pro는 현재 최대 규모 오픈웨이트 모델.
- **핵심 키워드**: DeepSeek-V4, MoE, 1M context, open-weight, MIT license

---

## 2. qwen3-6-27b | Qwen3.6-27B - 에이전트 코딩 특화 27B 밀집 모델 | architectures | entity

- **출처**: https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/ / https://hf.co/Qwen/Qwen3.6-27B
- **요약**: 2026년 4월 21일 공개. 27B 밀집 모델임에도 397B MoE 모델(Qwen3.5-397B-A17B)을 에이전트 코딩 벤치마크에서 능가. Apache 2.0 라이선스. 이미지-텍스트 멀티모달 지원. HuggingFace 트렌딩 스코어 852.
- **핵심 키워드**: Qwen3.6, dense model, agentic coding, Apache 2.0, multimodal

---

## 3. qwen3-6-35b-a3b | Qwen3.6-35B-A3B - 오픈소스 MoE 멀티모달 모델 | architectures | entity

- **출처**: https://hf.co/Qwen/Qwen3.6-35B-A3B
- **요약**: 2026년 4월 15-16일 HuggingFace Hub 및 ModelScope에 등록된 Qwen3.6 시리즈 첫 MoE 모델. 35B 전체 파라미터에 3B 활성 파라미터. Apache 2.0 라이선스. 다운로드 수 140만 회 기록.
- **핵심 키워드**: Qwen3.6, MoE, 3B active, Apache 2.0, trending

---

## 4. kimi-k2-6 | Kimi K2.6 - 장기 코딩 에이전트 스웜 모델 | agents | entity

- **출처**: https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/ / https://hf.co/moonshotai/Kimi-K2.6
- **요약**: 2026년 4월 20일 Moonshot AI 공개. 1조 파라미터 MoE 아키텍처 기반으로 300개 서브에이전트, 4,000 단계 협업 지원. SWE-Bench Pro에서 58.6점 기록(GPT-5.4 57.7, Claude Opus 4.6 53.4 상회). 장기 자율 실행(long-horizon execution)에 특화.
- **핵심 키워드**: Kimi K2.6, long-horizon, agent swarm, 1T MoE, SWE-Bench

---

## 5. tencent-hy3-preview | Tencent Hy3 Preview - 295B MoE 추론 언어 모델 | architectures | entity

- **출처**: https://www.caixinglobal.com/2026-04-23/tencent-unveils-new-ai-model-to-close-gap-with-rivals-102437241.html / https://hf.co/tencent/Hy3-preview
- **요약**: 2026년 4월 13일 출시. 295B 파라미터, 21B 활성, 256K 컨텍스트 지원 MoE 모델. Tencent AI 수장 Yao Shunyu 체제 하 첫 주요 모델. 빠른-느린 사고 융합(fast-and-slow-thinking fused) 설계로 복잡 추론, 코딩, 에이전트 워크로드 대응.
- **핵심 키워드**: Hunyuan, Hy3, Tencent, MoE, fast-slow thinking

---

## 6. tencent-hy-world-2 | Tencent HY-World 2.0 - 멀티모달 3D 월드 생성 모델 | architectures | entity

- **출처**: https://github.com/Tencent-Hunyuan/HY-World-2.0 / https://hf.co/tencent/HY-World-2.0
- **요약**: 2026년 4월 10-15일 공개. 텍스트/단일뷰 이미지/멀티뷰 이미지/비디오를 입력받아 3D 월드(메쉬, Gaussian Splatting, 포인트 클라우드)를 생성하는 4단계 파이프라인(HY-Pano 2.0 → WorldNav → WorldStereo 2.0 → WorldMirror 2.0). Unity, Unreal Engine, Blender 직접 임포트 가능. WorldMirror 2.0(약 1.2B)은 Apache 오픈소스.
- **핵심 키워드**: HY-World, 3DGS, Gaussian Splatting, world model, multimodal 3D

---

## 7. llada-2-uni | LLaDA 2.0-Uni - 멀티모달 이해/생성 통합 확산 언어 모델 | architectures | entity

- **출처**: https://arxiv.org/abs/2512.15745 / https://hf.co/inclusionAI/LLaDA2.0-Uni
- **요약**: 2026년 4월 22일 출시. Ant Group의 InclusionAI 팀이 개발. 기존 자기회귀(AR) 모델을 이산 확산(discrete diffusion) 언어 모델로 변환해 100B 파라미터까지 스케일링. LLaDA2.0-Uni는 멀티모달 이해와 생성을 단일 프레임워크 내에서 통합. 병렬 디코딩으로 535 tokens/s 달성.
- **핵심 키워드**: LLaDA2.0, diffusion LLM, dLLM, discrete diffusion, multimodal

---

## 8. exaone-4-5 | EXAONE 4.5 - LG AI 연구소 33B 멀티모달 추론 모델 | architectures | entity

- **출처**: https://www.prnewswire.com/news-releases/lg-reveals-next-gen-multimodal-ai-exaone-4-5-302736993.html / https://www.koreaherald.com/article/10714004
- **요약**: 2026년 4월 9일 발표. 33B 파라미터 멀티모달(텍스트+이미지) 모델. 5대 STEM 벤치마크 평균 77.3점으로 GPT-5-mini(73.5), Claude 4.5 Sonnet(74.6), Qwen-3 235B(77.0)를 상회. K-EXAONE(236B)의 1/7 크기로 유사 성능. 한국 AI 연구소 플래그십 모델.
- **핵심 키워드**: EXAONE 4.5, LG AI, multimodal, STEM, Korean model

---

## 9. openai-privacy-filter | OpenAI Privacy Filter - 오픈소스 온디바이스 PII 탐지/마스킹 모델 | tooling | entity

- **출처**: https://openai.com/index/introducing-openai-privacy-filter/ / https://hf.co/openai/privacy-filter
- **요약**: 2026년 4월 22일 Apache 2.0 라이선스로 공개. 1.5B 파라미터(활성 50M) Sparse MoE 기반 토큰 분류 모델. 이름/주소/이메일/전화번호/URL/날짜/계좌번호/시크릿 8개 카테고리 PII 탐지. 128K 컨텍스트, 클라우드 전송 없이 온프레미스 실행. PII-Masking-300k 벤치마크 F1 96%.
- **핵심 키워드**: PII, privacy, token-classification, Sparse MoE, Apache 2.0, on-premise

---

## 10. dflash-speculative-decoding | DFlash - 블록 확산 기반 Flash 스펙울레이티브 디코딩 | inference | concept

- **출처**: https://arxiv.org/abs/2602.06036 / https://hf.co/z-lab/Qwen3.6-35B-A3B-DFlash
- **요약**: 2026년 2월 논문 발표, 4월 오픈소스 커뮤니티에서 바이럴. 경량 블록 확산 드래프트 모델로 병렬 토큰 생성 후 타겟 모델이 검증하는 스펙울레이티브 디코딩 방식. EAGLE-3 대비 2.5배 추가 속도 향상, 총 6배 이상 무손실 가속. SGLang, vLLM 통합 지원.
- **핵심 키워드**: DFlash, speculative decoding, block diffusion, 6x speedup, EAGLE-3

---

## 11. mistral-voxtral-tts | Mistral Voxtral TTS - 오픈웨이트 4B 다국어 TTS 모델 | architectures | entity

- **출처**: https://mistral.ai/news/voxtral-tts / https://huggingface.co/mistralai/Voxtral-4B-TTS-2603
- **요약**: 2026년 3월 26일 공개, 4월 본격 커뮤니티 활용. 4B 파라미터, 9개 언어(영어/프랑스어/독일어/스페인어/네덜란드어/포르투갈어/이탈리아어/힌디어/아랍어) 지원. 10초 샘플 500자 기준 TTFA 90ms, RTF 6배. 5초 이하 음성 샘플로 커스텀 보이스 복제 가능. CC BY NC 4.0 오픈웨이트.
- **핵심 키워드**: Voxtral TTS, text-to-speech, 4B, multilingual, voice cloning

---

## 12. mistral-small-4-unified | Mistral Small 4 - 추론/멀티모달/코딩 통합 119B MoE | architectures | entity

- **출처**: https://mistral.ai/news/mistral-small-4 / https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide
- **요약**: 2026년 3월 16일 출시. 119B 전체 파라미터, 6B 활성 파라미터 MoE. Magistral(추론), Pixtral(멀티모달), Devstral(에이전트 코딩) 역량을 단일 모델로 통합. 256K 컨텍스트. 추론 강도 조절 가능(빠른 응답 ↔ 깊은 추론). vLLM/llama.cpp/SGLang/Transformers 지원.
- **핵심 키워드**: Mistral Small 4, unified model, MoE, reasoning, multimodal, 256K

---

## 13. cohere-tiny-aya | Cohere Tiny Aya - 70+ 언어 지원 3.35B 온디바이스 다국어 모델 | architectures | entity

- **출처**: https://cohere.com/blog/cohere-labs-tiny-aya / https://huggingface.co/CohereLabs/tiny-aya-global
- **요약**: 2026년 2월 17일 공개. 3.35B 파라미터로 70+ 언어 지원. iPhone 17 Pro에서 32 tokens/s 실행. Earth(아프리카어), Fire(남아시아), Water(아태/유럽) 지역별 변형 제공. WMT24++ 번역 태스크에서 61개 언어 중 46개에서 Gemma 3-4B 능가. 오픈웨이트 공개.
- **핵심 키워드**: Tiny Aya, on-device, 70+ languages, 3B, multilingual edge AI

---

## 14. pytorch-2-7 | PyTorch 2.7 - FlexAttention CPU 지원 및 추론 최적화 | tooling | entity

- **출처**: https://pytorch.org/blog/pytorch-2-7/ / https://dev-discuss.pytorch.org/t/pytorch-2-7-0-general-availability/2938
- **요약**: 3,262 커밋, 457 기여자. 주요 추가: GQA/PagedAttention 지원 추론 백엔드, FlexAttention x86 CPU 지원 강화(C++ micro-GEMM 템플릿), Context Parallel API(Flash/Efficient/cuDNN attention 3종 백엔드), Intel GPU Windows 11 torch.compile 지원. LLM 추론 처리량 개선에 초점.
- **핵심 키워드**: PyTorch 2.7, FlexAttention, Context Parallel, Intel GPU, inference optimization

---

## 15. vllm-0-18-0-19 | vLLM v0.18/v0.19 - gRPC 서빙 및 FlexKV 오프로딩 | tooling | entity

- **출처**: https://fazm.ai/blog/vllm-update-april-2026 / https://github.com/vllm-project/vllm/releases
- **요약**: 4월 두 메이저 버전 릴리스. v0.18: gRPC 서빙 도입, FlexKV 오프로딩 백엔드(고빈도 블록만 CPU에 선별 오프로딩), 다중 KV 그룹 지원, 비동기 스케줄링 기본화. v0.19: Gemma 4 전 변형(E2B/E4B/26B MoE/31B Dense) 완전 지원, CVE-2026-0994 보안 패치 포함.
- **핵심 키워드**: vLLM, gRPC, FlexKV, speculative decoding, Gemma 4, async scheduling

---

## 16. langgraph-1-0 | LangGraph 1.0 / LangChain 1.0 GA | tooling | entity

- **출처**: https://blog.langchain.com/langchain-langgraph-1dot0/ / https://changelog.langchain.com/announcements/langgraph-1-0-is-now-generally-available
- **요약**: LangGraph 1.0 및 LangChain 1.0 첫 메이저 버전 동시 GA. LangGraph: 영구 상태 자동 저장(built-in persistence), human-in-the-loop API 일급 지원, 타입 세이프 스트리밍(v2 옵션), 비블로킹 백그라운드 서브에이전트 태스크. LangChain: 핵심 에이전트 루프 집중, 미들웨어 개념 도입. `langgraph.prebuilt`는 `langchain.agents`로 이전.
- **핵심 키워드**: LangGraph 1.0, LangChain 1.0, durable state, human-in-the-loop, persistence

---

## 17. hf-transformers-5 | HuggingFace Transformers 5.x - Mistral 4/PP-OCRv5 등 다종 모델 지원 | tooling | entity

- **출처**: https://github.com/huggingface/transformers/releases / https://releasebot.io/updates/huggingface/transformers
- **요약**: 4월 기준 v5.4-5.6 계열 릴리스. 주요 추가 모델: Mistral 4(PR #44760), Jina Embeddings v3, VidEoMT(비디오 번역), UVDoc(문서 이해), PI0(로봇 정책), SLANeXt(OCR), PP-OCRv5. 양자화/토크나이저/커널/캐시/병렬화 전반 성능 향상. Torch 2.7 + CUDA 12.8 기반 TGI 업데이트 병행.
- **핵심 키워드**: Transformers 5.x, Mistral 4, multimodal, PP-OCRv5, quantization speedup

---

## 18. unsloth-gemma4-support | Unsloth v0.1.36 - Gemma 4 훈련 지원 및 MoE 속도 개선 | tooling | entity

- **출처**: https://unslothai.substack.com/p/unsloth-2026-update-faster-moe / https://github.com/unslothai/unsloth/releases
- **요약**: 2026년 4월 8일 v0.1.36-beta 릴리스. Gemma 4 훈련 정상화(이전 손실 폭발 300-400 버그 수정). Gemma-4-E2B를 8GB VRAM으로 학습 가능, FA2 대비 약 1.5배 빠르고 약 60% VRAM 절약. 그라디언트 누적 손실 스파이크 수정, Unsloth Dynamic 2.0 GGUF 포맷 업데이트.
- **핵심 키워드**: Unsloth, Gemma 4, 8GB VRAM, MoE training, GGUF

---

## 19. zerogpu-prepaid-credits | HuggingFace ZeroGPU 유료 크레딧 확장 | tooling | concept

- **출처**: https://huggingface.co/changelog/zerogpu-overquota / https://releasebot.io/updates/huggingface
- **요약**: 2026년 4월 HuggingFace PRO 사용자 대상 ZeroGPU 선불 크레딧 구매 기능 출시. 일일 무료 할당량 초과 시 $1/10분 요금제로 지속 사용 가능. ZeroGPU는 Spaces에 동적 GPU 할당을 제공하는 HuggingFace 무료 GPU 공유 서비스. 이전 고정 할당 모델에서 사용량 기반 과금 모델로 전환.
- **핵심 키워드**: ZeroGPU, prepaid credits, Spaces, dynamic GPU, HuggingFace PRO

---

## 20. bytedance-doubao-2 | ByteDance Doubao 2.0 생태계 - 멀티모달 트리펙타 | applications | entity

- **출처**: https://renovateqr.com/blog/chinese-ai-models-april-2026 / https://chatlyai.app/news
- **요약**: 2026년 1분기 1억 신규 사용자 확보, 3월 MAU 3억 4,500만. Doubao 2.0(LLM) + Seedream 5.0(이미지 생성) + Seedance 2.0(비디오 생성) 멀티모달 트리펙타 구성. Douyin 배포 채널과의 수직 통합으로 중국 AI 챗봇 시장 1위 유지.
- **핵심 키워드**: Doubao 2.0, ByteDance, Seedream, Seedance, multimodal trifecta

---

## 21. smollm3 | SmolLM3-3B - 이중 모드 추론 지원 경량 다국어 모델 | architectures | entity

- **출처**: https://huggingface.co/blog/smollm3 / https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- **요약**: HuggingFace TB팀 개발 3B 경량 언어 모델. 11.2T 토큰 3단계 훈련(웹+수학+코드 데이터 비율 점진적 조정). 이중 모드(dual mode) 추론(일반 vs 추론 모드) 지원, 6개 언어 지원, 롱 컨텍스트 처리. 소형 모델의 한계를 넓히는 HuggingFace 자체 연구 성과.
- **핵심 키워드**: SmolLM3, 3B, dual-mode reasoning, multilingual, 11.2T tokens

---

## 22. llama-factory-2026 | LLaMA-Factory 최신 업데이트 - 멀티모달 파인튜닝 통합 | tooling | entity

- **출처**: https://github.com/hiyouga/LLaMA-Factory/releases
- **요약**: 4월 기준 LLaMA-Factory는 Qwen3.6, Gemma 4, DeepSeek V4 등 최신 모델 파인튜닝 지원 추가. WebUI 기반 훈련 설정, 통합 PEFT(LoRA/QLoRA/DoRA) 지원, GRPO/DPO/PPO 정렬 파이프라인. 멀티모달 이미지-텍스트 파인튜닝 기능 강화. [교차검증 필요: 4월 구체적 버전 릴리스 날짜는 공식 GitHub에서 확인 권장]
- **핵심 키워드**: LLaMA-Factory, fine-tuning, PEFT, multimodal, GRPO

---

## 23. hf-hub-dataset-viewer-2026 | HuggingFace Hub 데이터셋 뷰어 개선 - SQL 쿼리 지원 | tooling | concept

- **출처**: https://releasebot.io/updates/huggingface
- **요약**: 2026년 4월 HuggingFace Hub 데이터셋 뷰어에 DuckDB 기반 SQL 쿼리 인터페이스 정식 제공. Parquet 포맷 자동 변환 및 스트리밍 프리뷰 성능 개선. ZeroGPU Spaces와 연동한 데이터셋 탐색 워크플로우 강화. [교차검증 필요: 구체적 기능 출시 날짜는 공식 HuggingFace 블로그에서 확인 권장]
- **핵심 키워드**: HuggingFace Hub, Dataset Viewer, DuckDB, SQL query, Parquet

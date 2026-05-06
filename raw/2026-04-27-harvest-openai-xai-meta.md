# 2026-04 OpenAI/xAI/Meta Harvest

수집일: 2026-04-27
수집 범위: OpenAI, xAI, Meta AI 2026년 4월 주요 발표 및 업데이트

---

## 1. gpt-5-5-release | GPT-5.5 출시 - 에이전틱 코딩 특화 모델 | architectures | entity

- **출처**: https://openai.com/index/introducing-gpt-5-5/ , https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/
- **요약**: OpenAI가 2026년 4월 23일 GPT-5.5를 출시했다. GPT-5.4 대비 에이전틱 코딩(Terminal-Bench 2.0 82.7%), 장문 컨텍스트 추론(MRCR v2 1M 토큰 74%), OSWorld-Verified 컴퓨터 사용(78.7%) 등에서 큰 향상을 보였으며, "지금까지 가장 스마트하고 직관적인 모델"로 소개됐다. 텍스트, 이미지, 오디오, 비디오를 단일 아키텍처로 처리한다.
- **핵심 키워드**: GPT-5.5, agentic coding, Terminal-Bench, OSWorld, multimodal, ChatGPT, April 2026

---

## 2. openai-workspace-agents | OpenAI Workspace Agents - ChatGPT 엔터프라이즈 자동화 플랫폼 | agents | entity

- **출처**: https://openai.com/index/introducing-workspace-agents-in-chatgpt/ , https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more
- **요약**: 2026년 4월 22일 OpenAI가 Workspace Agents를 출시했다. Custom GPTs의 후속 제품으로, Codex 기반의 상시 가동 클라우드 에이전트가 Slack, Salesforce, Microsoft 365, Google Drive 등 60개 이상의 엔터프라이즈 앱과 연동된다. MCP(Model Context Protocol)를 통해 미지원 서비스도 연결 가능하며, 2026년 5월 6일부터 크레딧 기반 과금이 시작된다.
- **핵심 키워드**: Workspace Agents, Custom GPTs, Codex, enterprise automation, MCP, Slack, Salesforce, April 2026

---

## 3. codex-cli-april-2026-updates | Codex CLI 2026년 4월 업데이트 - Amazon Bedrock 지원 및 MCP 진단 강화 | tooling | project-internal

- **출처**: https://developers.openai.com/codex/changelog , https://www.bighatgroup.com/blog/openai-codex-enterprise-ai-automation-april-2026/
- **요약**: Codex CLI가 Amazon Bedrock 모델 프로바이더 내장 지원, `/mcp verbose` 진단 명령 추가, Unix 소켓 트랜스포트 지원, 실시간 핸드오프 개선 등의 업데이트를 받았다. `codex exec --json`이 reasoning-token 사용량을 보고하며, 코딩 에이전트의 멀티 에이전트 병렬 실행 및 컴퓨터 사용(Computer Use) 기능이 강화됐다.
- **핵심 키워드**: Codex CLI, Amazon Bedrock, MCP verbose, Computer Use, multi-agent, OpenAI Agents SDK

---

## 4. chatgpt-codex-desktop-computer-use | ChatGPT Codex Desktop - 컴퓨터 사용 에이전트 및 90+ 플러그인 | applications | entity

- **출처**: https://smartscope.blog/en/generative-ai/chatgpt/codex-desktop-major-update-april-2026/
- **요약**: OpenAI Codex Desktop 앱이 대규모 업데이트를 통해 컴퓨터 사용(Computer Use) 기능과 인앱 브라우저를 전면에 내세웠다. Atlassian Rovo, CircleCI, CodeRabbit, GitLab Issues, Microsoft Suite, Render 등 90개 이상의 신규 플러그인이 추가됐다. 복수의 에이전트가 백그라운드에서 병렬로 작동하는 구조다.
- **핵심 키워드**: Codex Desktop, Computer Use, plugins, multi-agent parallel, in-app browser, April 2026

---

## 5. openai-nvidia-10gw-partnership | OpenAI-NVIDIA 10기가와트 전략 파트너십 | concepts | entity

- **출처**: https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems , https://blogs.nvidia.com/blog/openai-nvidia/
- **요약**: NVIDIA와 OpenAI가 총 100억 달러 규모의 전략적 파트너십을 체결했다. NVIDIA가 최대 10기가와트의 시스템을 순차 배포하며 기가와트 단위 배포마다 최대 100억 달러를 투자한다. 첫 1기가와트는 2026년 하반기 NVIDIA Vera Rubin 플랫폼으로 배포 예정이다. AMD와도 6GW 규모 GPU 공급 계약을 체결해 2026년 1GW 규모 데이터센터 구축에 MI450 칩을 사용한다.
- **핵심 키워드**: NVIDIA Vera Rubin, OpenAI, 10GW, data center, AMD MI450, infrastructure, 2026

---

## 6. openai-titan-chip | OpenAI Titan 커스텀 AI 추론 칩 - TSMC 3nm + Broadcom 설계 | tooling | entity

- **출처**: https://markets.financialcontent.com/stocks/article/tokenring-2026-1-20-openai-signals-end-of-the-nvidia-tax-with-2026-launch-of-custom-titan-chip , https://www.datacenterdynamics.com/en/news/openai-building-first-custom-ai-inference-chip-with-tsmc-and-broadcom-report/
- **요약**: OpenAI가 Broadcom과 협업하여 TSMC 3nm(N3) 공정 기반 자체 AI 추론 칩 "Titan"을 개발 중이다. 2026년 12월 양산을 목표로 하며, LLM 추론 비용 절감에 특화된 ASIC이다. Samsung HBM4 메모리 공급망도 확보했으며, 차세대 "Titan 2"는 TSMC A16(1.6nm) 공정으로 2027년 목표다. 이른바 "엔비디아 세금(NVIDIA Tax)" 탈피가 핵심 동기다.
- **핵심 키워드**: Titan chip, ASIC, TSMC N3, Broadcom, HBM4, inference cost, custom silicon, OpenAI

---

## 7. openai-stargate-project | Project Stargate - OpenAI-SoftBank-Oracle AI 인프라 합작법인 | concepts | entity

- **출처**: https://openai.com/index/announcing-the-stargate-project/ , https://the-decoder.com/stargates-500-billion-ai-infrastructure-project-reportedly-stalls-over-unresolved-disputes-between-openai-oracle-and-softbank/
- **요약**: 2025년 1월 발표된 OpenAI, SoftBank, Oracle, MGX의 합작 법인으로 4년간 미국 내 AI 인프라에 최대 5000억 달러를 투자하는 프로젝트다. 확정 투자 1000억 달러, 계획 용량 8+ 기가와트다. UAE Stargate(NVIDIA, Cisco 참여), Stargate Argentina($250억) 등 국제 확장도 진행 중이나, OpenAI-Oracle-SoftBank 간 역할 분담 분쟁으로 진전이 더딘 상황이다.
- **핵심 키워드**: Stargate, OpenAI, SoftBank, Oracle, $500 billion, data center, 10GW, AI infrastructure

---

## 8. grok-4-3-beta-multimodal | Grok 4.3 Beta - 네이티브 비디오 이해 및 슬라이드 생성 | architectures | entity

- **출처**: https://chatlyai.app/news/xai-grok-4-3-beta-video , https://techsifted.com/posts/grok-4-3-review-april-2026/
- **요약**: xAI가 2026년 4월 17일 Grok 4.3 Beta를 공식 발표 없이 조용히 출시했다. 네이티브 비디오 이해(멀티모달), 채팅 내 PDF/PowerPoint 슬라이드/스프레드시트 직접 생성, Grok Computer와의 긴밀한 통합이 핵심이다. 16-에이전트 Heavy 시스템과 200만 토큰 컨텍스트 창을 유지하며, SuperGrok Heavy 티어($300/월)에서만 조기 접근 가능하다.
- **핵심 키워드**: Grok 4.3, video understanding, multimodal, slides generation, SuperGrok Heavy, xAI, April 2026

---

## 9. grok-computer-desktop-agent | Grok Computer - xAI 자율 데스크톱 컴퓨터 사용 에이전트 | agents | entity

- **출처**: https://www.dextools.io/tutorials/grok-computer-xai-ai-agent-controls-pc-everything-we-know-2026 , https://www.evermx.com/case/grok-computer-xai-desktop-ai-agent-musk
- **요약**: Grok Computer는 xAI의 자율 데스크톱 에이전트로, 앱 조작, 버튼 클릭, 텍스트 입력, 폼 작성 등 컴퓨터 전체를 제어할 수 있다. 2026년 4월 기준 타겟 사용자 대상 비공개 베타 가동 중이며, 마스크가 곧 대규모 공개 테스트를 선언했다. Grok Computer는 Tesla-xAI 합작 프로젝트 "Macrohard"(Tesla 20억 달러 투자)의 일환이며, 최근 5초간 화면 영상을 연속 처리해 컨텍스트를 파악하는 구조다.
- **핵심 키워드**: Grok Computer, computer use, desktop agent, Macrohard, Tesla-xAI, autonomous agent, April 2026

---

## 10. xai-colossus-memphis-2gw | xAI Colossus Memphis - 세계 최대 AI 슈퍼컴퓨터 2GW 확장 | tooling | entity

- **출처**: https://x.ai/colossus , https://introl.com/blog/xai-colossus-2-gigawatt-expansion-555k-gpus-january-2026
- **요약**: xAI의 Colossus 슈퍼컴퓨터는 테네시 주 멤피스에 위치하며 2026년 1월 기준 총 용량 2기가와트, 555,000개의 NVIDIA GPU(H100, H200, GB200)를 보유한 세계 최대 AI 시설이다. Elon Musk가 세 번째 건물 추가 매입을 발표하며 계속 확장 중이다. 총 투자액은 180억 달러로 미국 약 150만 가구 전력에 해당하는 에너지를 소비한다. Grok 훈련, X 플랫폼 컴퓨트, SpaceX 등 Musk 벤처 전체에 서비스한다.
- **핵심 키워드**: Colossus, Memphis, 2GW, 555000 GPU, NVIDIA H100/H200/GB200, xAI infrastructure, supercomputer

---

## 11. meta-llama-4-scout-maverick | Meta Llama 4 Scout & Maverick - 오픈 웨이트 네이티브 멀티모달 MoE | architectures | entity

- **출처**: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ , https://huggingface.co/blog/llama4-release
- **요약**: 2026년 4월 5일 Meta가 Llama 4 Scout와 Llama 4 Maverick을 출시했다. 두 모델 모두 활성 파라미터 170억에 MoE(Mixture-of-Experts) 아키텍처를 사용한다. Scout는 16개 전문가, 1000만 토큰 컨텍스트 창으로 단일 H100 GPU에서 동작하며, Maverick은 128개 전문가로 GPT-4o, Gemini 2.0 Flash를 벤치마크에서 앞선다. 최초의 오픈 웨이트 네이티브 멀티모달 MoE 모델이다.
- **핵심 키워드**: Llama 4, Scout, Maverick, MoE, multimodal, 10M context, open-weight, Meta, April 2026

---

## 12. meta-llama-4-behemoth-delay | Meta Llama 4 Behemoth - 2조 파라미터 교사 모델 지연 | architectures | entity

- **출처**: https://serenitiesai.com/articles/llama-4-behemoth-maverick-scout-review-2026 , https://www.computerworld.com/article/3987990/meta-hits-pause-on-llama-4-behemoth-ai-model-amid-capability-concerns.html
- **요약**: Llama 4 Behemoth는 활성 파라미터 2880억, 16개 전문가, 총 2조 파라미터에 달하는 Meta의 최대 모델이다. MATH-500, GPQA Diamond 등 STEM 벤치마크에서 GPT-4.5, Claude Sonnet 3.7, Gemini 2.0 Pro를 능가한다고 주장하나, 역량 개선이 기대에 못 미쳐 출시가 2026년 초에서 가을 이후로 연기됐다. Scout/Maverick의 "교사 모델(codistillation)"로 활용된다.
- **핵심 키워드**: Llama 4 Behemoth, 2 trillion parameters, codistillation, teacher model, delay, Meta 2026

---

## 13. meta-muse-spark-superintelligence-labs | Meta Muse Spark - Meta Superintelligence Labs 첫 번째 모델 | architectures | entity

- **출처**: https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/ , https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/
- **요약**: 2026년 4월 8일 Meta Superintelligence Labs(수장: Alexandr Wang 전 Scale AI CEO)가 첫 번째 모델 Muse Spark를 출시했다. 멀티모달 추론 모델로 툴 사용, 시각적 Chain-of-Thought, 멀티 에이전트 오케스트레이션을 지원한다. 의사 1000명 이상과 협업한 의료 추론 특화 학습 데이터를 포함하며, Meta AI 앱과 meta.ai를 구동한다. Llama와 달리 클로즈드 소스로 출시됐다는 점이 주목된다.
- **핵심 키워드**: Muse Spark, Meta Superintelligence Labs, Alexandr Wang, closed source, multimodal reasoning, Meta AI, April 2026

---

## 14. meta-sam-3-1-video-segmentation | Meta SAM 3.1 - 실시간 멀티 오브젝트 트래킹 및 개념 세그멘테이션 | architectures | entity

- **출처**: https://ai.meta.com/blog/segment-anything-model-3/ , https://github.com/facebookresearch/sam3
- **요약**: Meta가 2026년 3월 SAM 3.1을 출시했다. SAM 3는 텍스트/이미지 예시 프롬프트로 오픈 어휘 개념 세그멘테이션(Promptable Concept Segmentation)을 지원하며, 400만 개 고유 개념으로 학습된 최대 규모 데이터셋을 활용한다. SAM 3.1은 공유 메모리 기반 멀티 오브젝트 동시 트래킹(Object Multiplex)을 추가해 단일 H100에서 초당 32프레임(SAM 3 대비 2배), 한 번에 16개 객체 트래킹이 가능하다.
- **핵심 키워드**: SAM 3, SAM 3.1, Segment Anything, Promptable Concept Segmentation, object multiplex, video tracking, Meta 2026

---

## 15. xai-grok-5-training | xAI Grok 5 학습 중 - 6조 파라미터, AGI 10% 확률 주장 | training | entity

- **출처**: https://i10x.ai/news/xai-agi-2026-elon-musk-prediction-analysis , https://www.digitalapplied.com/blog/grok-4-20-preview-xai-musk-roadmap
- **요약**: xAI가 Grok 5 학습을 진행 중이며 Elon Musk는 Q2 2026 출시를 목표로 한다고 밝혔다. Grok 5는 600만 개 이상의 파라미터를 보유한 역대 최대 공개 발표 AI 모델로 설계됐으며, Colossus 2 슈퍼클러스터에서 훈련 중이다. Musk는 "AGI 달성 확률 10%"라는 발언으로 주목을 받았다. X 플랫폼 알고리즘에 Grok을 전면 통합하는 것이 "X 역사상 가장 중요한 변경"이 될 것이라고 Nikita Bier(X 제품 총괄)가 밝혔다.
- **핵심 키워드**: Grok 5, 6 trillion parameters, AGI, Colossus 2, X algorithm integration, Elon Musk, xAI roadmap

---

## 16. sam-altman-agi-definition-shift | Sam Altman의 AGI 정의 전환 - "AGI는 더 이상 유용한 용어가 아니다" | concepts | concept

- **출처**: https://www.cnbc.com/2025/08/11/sam-altman-says-agi-is-a-pointless-term-experts-agree.html , https://digitalstrategy-ai.com/2026/01/02/openai-sam-altman-2026/
- **요약**: Sam Altman이 AGI를 "더 이상 유용하지 않은 용어"로 규정하며 개념 전환을 꾀하고 있다. 대신 "2026년은 AI 연구 인턴의 해"(특정 복잡 연구 작업을 자율적으로 수행하는 시스템)라는 표현을 사용하며, 2026년 4월 "GPT-5.5가 너무 좋아서 다상 수면으로 전환할 것"이라는 발언을 X에 올리기도 했다. "AGI 달성 방법을 알고 있다"는 기존 선언에서 점진적 역량 수준 논의로 이동하고 있다.
- **핵심 키워드**: AGI, Sam Altman, AI Research Intern, superintelligence, 2026, AGI definition

---

## 수집 요약

- **총 토픽 수**: 16개
- **출처 분포**: OpenAI 8건, xAI 4건, Meta 4건
- **카테고리 분포**: architectures 5, agents 2, tooling 3, applications 1, concepts 2, training 1, entity 12(중복 포함)
- **날짜 범위**: 2026년 3월-4월 핵심 발표 집중

# 2026-04 Anthropic Harvest

수집일: 2026-04-27
수집 범위: 2026-04-01 ~ 2026-04-27 Anthropic 공식 발표, 연구, 제품, 파트너십
기존 위키 중복 제외 기준: 동일 slug 또는 동일 핵심 내용을 다루는 페이지가 wiki/ 디렉토리에 존재하는 경우 제외

---

## 1. claude-opus-4-7-release | Claude Opus 4.7 공개: 코딩·비전·자기검증 강화 | tooling | entity

- **출처**: https://www.anthropic.com/news/claude-opus-4-7 (2026-04-16)
- **요약**: Opus 4.6 후속 모델로 2026년 4월 16일 출시. SWE-bench Verified 87.6%(+6.8p), CursorBench 70%(이전 58%), 비전 해상도 2,576px(3.75MP, 기존 대비 3배+), xhigh effort 레벨 신설, 작업 예산(task budget) 퍼블릭 베타. 가격은 Opus 4.6과 동일($5/$25 per MTok).
- **핵심 키워드**: SWE-bench, CursorBench, task-budget, xhigh-effort, vision-resolution, implicit-need-test

> 기존 wiki/tooling/claude-opus-4-7.md는 system prompt diff 관점에서 작성됐으므로, 벤치마크·기능 스펙 관점의 entity 보강 대상.

---

## 2. claude-design-launch | Claude Design: 자연어로 시각 산출물 생성 | applications | entity

- **출처**: https://www.anthropic.com/news/claude-design-anthropic-labs (2026-04-17)
- **요약**: Anthropic Labs가 출시한 실험적 프로덕트. 슬라이드, UI 프로토타입, 원페이저 등을 자연어로 지시하면 Claude Opus 4.7이 시각 결과물을 생성. 팀 디자인 시스템을 코드베이스·디자인 파일에서 학습해 브랜드 일관성 유지. Claude Code로 핸드오프 번들 전달 가능. Pro/Max/Team/Enterprise 구독자 리서치 프리뷰. Figma 주가 7%+ 하락.
- **핵심 키워드**: claude-design, anthropic-labs, visual-generation, design-handoff, figma-competitor

---

## 3. managed-agents-memory-beta | Managed Agents 메모리 퍼블릭 베타 | tooling | concept

- **출처**: https://sdtimes.com/anthropic/anthropic-adds-memory-to-claude-managed-agents/ (2026-04-23); https://docs.anthropic.com/en/managed-agents/overview
- **요약**: Claude Managed Agents에 세션 간 기억 유지 기능(Memory) 퍼블릭 베타 출시(2026-04-23). 메모리는 파일시스템에 파일로 저장되며 API 또는 Claude Console에서 내보내기·편집 가능. managed-agents-2026-04-01 베타 헤더 동일 사용. Managed Agents 자체는 4월 8일 퍼블릭 베타 진입.
- **핵심 키워드**: managed-agents, memory-api, persistent-memory, filesystem-memory, stateful-agent

---

## 4. mcp-rce-vulnerability-2026 | MCP 설계 결함으로 원격코드실행(RCE) 취약점 노출 | concepts | case-study

- **출처**: https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html (2026-04-15); https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/
- **요약**: OX Security가 2026-04-15 공개. Anthropic MCP 공식 SDK의 STDIO 전송 인터페이스 기본값 결함으로 임의 OS 명령 실행 가능. Python/TypeScript/Java/Rust 모든 지원 언어 영향, 공개 서버 200,000개 이상 노출, 다운로드 누적 1억 5천만 건. LiteLLM·LangChain·LangFlow·Flowise 등 인기 프로젝트에서 CVE 10건 발급. Anthropic은 "expected behavior"로 프로토콜 아키텍처 수정을 거부.
- **핵심 키워드**: MCP, RCE, STDIO-transport, supply-chain-vulnerability, OX-Security, CVE

---

## 5. google-40b-anthropic-investment | Google Alphabet, Anthropic에 최대 400억 달러 투자 | applications | case-study

- **출처**: https://www.cnbc.com/2026/04/24/google-to-invest-up-to-40-billion-in-anthropic-as-search-giant-spreads-its-ai-bets.html (2026-04-24); https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/
- **요약**: Alphabet이 최대 400억 달러 투자 발표 (즉시 100억+성과 조건부 300억). Anthropic 밸류에이션 3,500억 달러. 투자 며칠 전 Amazon도 250억 달러 추가 투자 발표. Google은 현금+TPU 컴퓨트 복합 형태로 지원. Anthropic 연간 매출 런레이트 300억 달러 돌파(2025년 말 90억 대비).
- **핵심 키워드**: google-investment, alphabet, 40B, valuation, compute-deal, AI-infrastructure-war

---

## 6. amazon-anthropic-5gw-compute | Amazon-Anthropic 5기가와트 컴퓨트 확장 계약 | applications | case-study

- **출처**: https://www.anthropic.com/news/anthropic-amazon-compute (2026-04-20); https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html
- **요약**: Amazon이 Anthropic에 추가 250억 달러 투자 및 최대 5기가와트 컴퓨트 제공 계약(2026-04-20). Anthropic은 향후 10년간 Trainium 등 AWS 기술에 1,000억 달러 이상 지출 약정. 이 계약은 Google 400억 투자 발표(4-24) 직전에 공개됨.
- **핵심 키워드**: amazon, AWS, Trainium, 5GW, AI-infrastructure, compute-commitment

---

## 7. google-broadcom-tpu-compute | Google·Broadcom과 차세대 TPU 3.5GW 확보 계약 | applications | case-study

- **출처**: https://www.anthropic.com/news/google-broadcom-partnership-compute (2026-04-06); https://techcrunch.com/2026/04/07/anthropic-compute-deal-google-broadcom-tpus/
- **요약**: Broadcom 제조 차세대 TPU 3.5기가와트 공급 계약 체결(2027년부터 납품 예정). 미국 내 데이터센터 중심 배치. 11월 2025 인프라 투자 공약($500억) 연장선. Anthropic 런레이트 수익 300억 달러+ 공개 시점과 일치.
- **핵심 키워드**: Broadcom, TPU, Google-Cloud, 3.5GW, AI-compute-war, 2027-delivery

---

## 8. coreweave-anthropic-gpu-deal | CoreWeave 다년 계약으로 NVIDIA GPU 클라우드 공급 | applications | case-study

- **출처**: https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic (2026-04-10); https://thenextweb.com/news/coreweave-has-agreed-a-multi-year-gpu-cloud-deal-with-anthropic
- **요약**: CoreWeave가 Anthropic과 다년 계약으로 NVIDIA GPU 클라우드 인프라 제공(2026-04-10 발표). 미국 내 데이터센터의 Claude 프로덕션 워크로드 지원. Anthropic은 이로써 AWS Trainium, Google TPU, NVIDIA GPU 세 가지 칩 플랫폼을 분산 운용하는 전략적 다각화를 완성.
- **핵심 키워드**: CoreWeave, NVIDIA-GPU, multi-cloud, chip-diversification, production-workload

---

## 9. nec-anthropic-japan-partnership | NEC-Anthropic 파트너십: 일본 AI 네이티브 엔지니어링 | applications | case-study

- **출처**: https://www.anthropic.com/news/anthropic-nec (2026-04-23); https://www.nec.com/en/press/202604/global_20260423_01.html
- **요약**: NEC가 Anthropic의 일본 최초 글로벌 파트너로 선정(2026-04-23). 30,000명 직원 전체에 Claude 배포, Claude Code로 AI 네이티브 엔지니어링 조직 구축 목표. 금융·제조·지방정부용 산업별 AI 솔루션 공동 개발. NEC SOC에 Claude 통합해 사이버보안 서비스 강화. Claude Cowork(데스크탑 AI 에이전트) 일본 배포 포함.
- **핵심 키워드**: NEC, Japan, Claude-Code, Claude-Cowork, enterprise-AI, AI-native-engineering

---

## 10. auditbench-alignment-auditing | AuditBench: 숨겨진 행동 모델 감사 벤치마크 | papers | paper

- **출처**: https://alignment.anthropic.com/2026/auditbench/ ; https://arxiv.org/abs/2602.22755 (2026-02 초판, 2026-03 v3)
- **요약**: 숨겨진 행동이 심어진 56개 LLM으로 구성된 alignment 감사 벤치마크. 14가지 우려 행동(아첨, AI 규제 반대, 비밀 충성심 등) 각각 1개씩 모델에 이식. 조사자 에이전트(Claude Agent SDK 구현)가 자율적으로 대상 모델을 감사. 핵심 발견: 보조 모델이 다양한 프롬프트를 생성하는 스캐폴드 블랙박스 도구가 가장 효과적이나, 단독 비에이전트 평가에서 잘 동작하는 도구가 에이전트 환경에서는 성능이 떨어지는 "tool-to-agent gap" 존재.
- **핵심 키워드**: AuditBench, alignment-auditing, hidden-behavior, investigator-agent, tool-to-agent-gap, sycophancy-detection

---

## 11. automated-weak-to-strong-researcher | 자동화 약-대-강 연구자(Automated W2S Researcher) | papers | paper

- **출처**: https://alignment.anthropic.com/2026/automated-w2s-researcher/ (2026-04-14)
- **요약**: Anthropic Fellows Program 연구. 강한 모델이 약한 감독자를 초월하는 문제(W2S)에서 AAR 9개 인스턴스가 5일(800 누적 시간) 만에 PGR 0.97 달성 - 인간 연구자 7일 작업 PGR 0.23 대비 4배 이상. 총 비용 약 18,000달러(AAR-시간당 $22). 단, 이 성공은 단일 정량적 성공 지표가 있는 문제에 국한되며 범용 alignment 과학자로 해석 불가.
- **핵심 키워드**: weak-to-strong, AAR, PGR, scalable-oversight, automated-researcher, alignment-automation

> 기존 wiki/applications/automated-alignment-researchers.md는 AAR 전반 실험 요약이지만, W2S Researcher 후속 연구는 별도 paper 페이지로 커버 가능.

---

## 12. anthropic-economic-index-march-2026 | Anthropic Economic Index 3월 보고서: 학습 곡선 | papers | summary

- **출처**: https://www.anthropic.com/research/economic-index-march-2026-report
- **요약**: 2026년 3월 발행 두 번째 경제지수 보고서. 2025년 11월~2026년 2월 Claude.ai 사용 패턴 분석. 코딩/수학 직무(Computer & Mathematical) 35% 비중으로 1위 유지. 상위 10개 O*NET 태스크 집중도 24%→19%로 분산 중. 상위 5개 주(state) 사용량 집중도 30%→24%로 분산, 균등화 시점 5-9년 후 예상. 22-25세 청년 고노출 직종 채용 ~14% 감소.
- **핵심 키워드**: economic-index, labor-market, AI-exposure, O*NET, coding-dominance, geographic-diffusion

---

## 13. claude-code-april-2026-updates | Claude Code 4월 업데이트: /powerup, MCP 500K, xhigh | tooling | summary

- **출처**: https://releasebot.io/updates/anthropic/claude-code ; https://daily1bite.com/en/blog/ai-tutorial/claude-code-april-2026-update (2026-04-17~22)
- **요약**: v2.1.91~v2.1.117 연속 릴리스. 주요 변경: MCP 결과 최대 500,000자 허용, /effort·/ultrareview·/resume 신규/개선, Opus 4.7 xhigh effort 통합, Auto 모드(Max 구독자), 네이티브 CLI 바이너리, OpenTelemetry 개선, 샌드박스 하드닝, Windows·macOS 버그 수정. /less-permission-prompts 스킬 추가.
- **핵심 키워드**: claude-code, MCP-500K, xhigh-effort, auto-mode, native-CLI, ultrareview, permission-allowlist

---

## 14. anthropic-election-safeguards-2026 | Anthropic 선거 안전장치 정책 업데이트 | concepts | summary

- **출처**: https://www.anthropic.com/news (2026-04-24 공식 발표)
- **요약**: Anthropic이 2026년 4월 24일 선거 무결성 보호를 위한 Claude 안전장치 접근 방식을 공개 발표. 구체 내용은 공개된 블로그 포스트 전문 확인 필요하나, Claude가 선거 관련 정보를 어떻게 처리하는지에 대한 정책 투명성 제고가 핵심.
- **핵심 키워드**: election-safety, policy, AI-governance, constitutional-AI, responsible-deployment

> 공식 블로그 전문을 추가로 WebFetch하여 상세 내용 보강 권장.

---

## 15. claude-code-mcp-security-reckoning | Claude Code와 MCP 첫 번째 보안 위기 | concepts | case-study

- **출처**: https://www.bighatgroup.com/blog/claude-weekly-2026-04-23/ (2026-04-23, Claude Weekly 뉴스레터)
- **요약**: MCP RCE 취약점 공개(토픽 #4)가 Claude Code 에코시스템에 미친 파급. 커뮤니티에서 "MCP 첫 번째 보안 충돌"로 규정. 200,000 서버 노출+Anthropic의 "expected behavior" 대응이 MCP 신뢰 모델 재논의 촉발. Claude Code 샌드박스 하드닝(v2.1.116~117) 출시가 같은 주에 이뤄짐.
- **핵심 키워드**: MCP-security, Claude-Code-sandbox, trust-model, supply-chain, hardening

---

## 16. anthropic-30b-revenue-milestone | Anthropic 연매출 런레이트 300억 달러 돌파 | applications | case-study

- **출처**: https://www.theregister.com/2026/04/07/broadcom_google_chip_deal_anthropic_customer/ ; https://www.cnbc.com/2026/04/24/google-to-invest-up-to-40-billion-in-anthropic
- **요약**: 2026년 4월 기준 Anthropic 연매출 런레이트가 300억 달러를 돌파(2025년 말 90억에서 약 3.3배 성장). 연간 100만 달러 이상 지출 기업 고객 1,000개 이상 확보. 이 수치는 Google·Amazon 투자 계약 발표 맥락에서 공개됨.
- **핵심 키워드**: revenue-milestone, ARR, enterprise-customers, growth-rate, AI-market-dynamics

---

## 메타데이터

- 총 수집 토픽: 16개
- 기존 위키 중복으로 제외된 주요 항목:
  - Project Glasswing (wiki/applications/project-glasswing-case-study.md 존재)
  - Claude Mythos Preview (wiki/tooling/claude-mythos-preview.md 존재)
  - Hot Mess of AI 논문 (wiki/papers/hot-mess-misalignment-paper.md 존재)
  - Scaling Managed Agents 엔지니어링 블로그 (wiki/tooling/scaling-managed-agents.md 존재)
  - AAR 실험 요약 (wiki/applications/automated-alignment-researchers.md 존재)
  - Claude Sonnet 4.5 감정 개념 (wiki/applications/emotion-concepts-claude-sonnet.md 존재)
  - Agentic Misalignment (내용 확인 결과 2025-10월 논문, 4월 범위 외)
- 신규 위키 페이지 생성 우선순위: #2(claude-design), #3(managed-agents-memory), #4(mcp-rce), #5~8(투자·컴퓨트 딜 시리즈), #10(AuditBench), #12(Economic Index), #13(Claude Code updates)

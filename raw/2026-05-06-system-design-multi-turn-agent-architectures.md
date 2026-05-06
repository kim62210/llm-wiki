---
source: cognition.ai + replit + langchain breakoutagents + zenml
url: https://cognition.ai/blog/devin-2 + https://www.langchain.com/breakoutagents/replit
title: "Multi-Turn Agent Architecture - Devin, Replit Agent, GitHub Copilot Workspace"
fetched: 2026-05-06
status: pending_ingest
---

# Production Multi-Turn Agent Architectures

## 1. Cognition Devin (Devin 2.0+)

### 핵심 메트릭
- SWE-bench: **13.86% end-to-end resolution** (이전 baseline ~2%)
- 18개월 운영 후 (2025 review): 장기 reasoning + 학습 + 오류 수정 강화

### 아키텍처
- **샌드박스된 컴퓨팅 환경**: shell, code editor, browser
- Devin 2.0: 클라우드 dev 환경 → 여러 Devin 인스턴스를 isolated VM에서 병렬 실행
- 자체 모델: **SWE-1.5 model families** (reasoning + execution speed + cost 균형)

### Multi-turn 디자인
- 매 step마다 관련 컨텍스트 recall + 학습 + mistake 수정
- 사용자와 능동적 collab: 진행 상황 실시간 보고, 피드백 수용, 디자인 결정 협의
- "수천 번의 결정"이 필요한 복잡한 엔지니어링 task 계획 + 실행

### 핵심 인사이트
- **Multi-instance 병렬화**: 동시에 여러 프로젝트 처리
- **Long-horizon reasoning**: 수천 step 의사결정 + 도구 사용 + plan 적응
- **Native dev env**: shell/editor/browser를 표준 dev 도구로 사용 (DSL 추상화 X)

## 2. Replit Agent (Agent 3, Agent 4)

### Multi-Agent Architecture (LangChain breakoutagents 사례)

> Replit Agent adopted a multi-agent architecture where each agent is constrained to perform the smallest possible task, as having a single agent manage all tools increased the chance of error.

3가지 specialized agent:

| 역할 | 책임 |
|---|---|
| Manager agent | 전체 워크플로우 감독 + 다른 agent 조율 |
| Editor agent | specific coding task에 집중 (focused expertise) |
| Verifier agent | code quality 체크 + 사용자와 빈번히 상호작용 (HITL) |

> The verifier agent exemplifies human-in-the-loop design by frequently falling back to user interaction rather than making autonomous decisions.

### Plan/Build 모드 분리 (Agent 4)

> Plan mode allows users to brainstorm, ask questions, and map out projects before Agent changes any code, breaking down complex projects into ordered task lists and reviewing them before any code is written.

흐름:
1. 사용자 요구사항 → Plan 생성
2. 사용자 review/approve
3. Build 모드 자동 실행

### Long-Horizon (Agent 3, 2025-09)

> Agent 3 is designed to carry out tasks over an extended period of time, with the system able to operate for up to 200 minutes continuously, giving it the capacity to plan, write, test, and refine entire software components without requiring constant user intervention.

핵심: **self-testing and debugging loop**
> Once it generates code, the agent executes it, identifies errors, applies fixes, and reruns the code until it passes tests or meets the specified requirements.

### Tool Invocation: 코드 생성 방식 (DSL)

> Rather than using traditional function calling APIs, Replit chose to generate code to invoke tools themselves for improved reliability, and wrote a restricted Python-based DSL (Domain-Specific Language) to handle these invocations.

이유: function calling API보다 코드 생성이 더 reliable (코드 모델 학습 데이터에 더 가까움).

### 병렬 실행 (Agent 4)

> Every request to Agent 4 is broken into discrete tasks that run in parallel in the background, with Agent 4 intelligently sequencing and executing them in the optimal order.

### 핵심 인사이트
- **Single agent ≠ best**: 모든 도구를 한 agent에 주면 error rate 증가
- **Plan 분리**: 코드 변경 전 명시적 계획 단계
- **Test-Debug 루프 자동화**: 모델이 직접 실행+수정+재실행
- **DSL > function calling**: 코드 생성으로 tool invocation 신뢰성 향상
- **HITL via verifier**: verifier agent가 명시적 인간 개입 trigger

## 3. GitHub Copilot Workspace

### 디자인 철학 (공개 자료 기반)

GitHub의 long-horizon coding agent. Issue → Spec → Plan → Implementation → Tests의 4단계 파이프라인:

1. **Spec**: 자연어 issue를 구조화된 작업 명세로
2. **Plan**: 구현 전 변경 계획
3. **Implementation**: 코드 변경 (multi-file)
4. **Tests**: 테스트 실행 + iterate

명시적 단계별 사용자 검토 가능.

(공식 spec 디테일은 GitHub Copilot Workspace docs 추가 조사 필요)

## 비교 표

| 차원 | Devin | Replit Agent | Copilot Workspace |
|---|---|---|---|
| Agent 분할 | Single-agent (장시간 동작) | Multi-agent (manager/editor/verifier) | Sequential phases |
| Tool 호출 | shell/editor/browser native | Restricted Python DSL | git/file ops + GitHub Actions |
| Long-horizon | 수천 결정, 18개월 학습 | 200분 자율 (Agent 3) | issue 단위 |
| Plan 분리 | 암묵적 | 명시 (Plan vs Build mode) | 명시 (Spec → Plan) |
| HITL | 필요 시 사용자 collab | verifier가 빈번히 사용자 호출 | 단계별 사용자 review |
| Parallel | Multi-VM 인스턴스 | Tasks in parallel (Agent 4) | issue 단위 |

## 공통 패턴

1. **Specialized roles vs single-agent**: 작은 task 단위로 agent 분할이 reliability 향상 (Replit)
2. **Test-Debug auto-loop**: 코드 → 실행 → 오류 → 수정의 자동 사이클
3. **Plan-then-execute**: 명시적 plan 단계가 사용자 신뢰 + 검증 향상
4. **Long-horizon = recall + learn + correct**: Devin 강조 — 매 step 컨텍스트 회상 + 학습 + 수정
5. **Sandboxed dev env**: shell/editor/browser native 사용 또는 제한된 DSL
6. **HITL은 architecture-level**: verifier agent를 분리해 사용자 fallback 강제

## 참고

- Cognition Devin 2.0: https://cognition.ai/blog/devin-2
- Devin 2025 Performance Review: https://cognition.ai/blog/devin-annual-performance-review-2025
- Devin 2.0 Technical Design (Medium): https://medium.com/@takafumi.endo/agent-native-development-a-deep-dive-into-devin-2-0s-technical-design-3451587d23c0
- Replit Agent (LangChain breakoutagents): https://www.langchain.com/breakoutagents/replit
- Replit Agent 3 (InfoQ): https://www.infoq.com/news/2025/09/replit-agent-3/
- Replit ZenML LLMOps DB: https://www.zenml.io/llmops-database/building-reliable-ai-agents-for-application-development-with-multi-agent-architecture
- Replit Agent 4: https://blog.replit.com/introducing-agent-4-built-for-creativity

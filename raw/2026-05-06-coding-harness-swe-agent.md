---
source: SWE-agent 공식 문서 + GitHub + arXiv
url:
  - https://arxiv.org/abs/2405.15793
  - https://swe-agent.com/0.7/background/aci/
  - https://swe-agent.com/latest/
  - https://github.com/SWE-agent/SWE-agent
  - https://github.com/SWE-agent/SWE-agent/blob/main/docs/background/aci.md
title: SWE-agent — Agent-Computer Interface (ACI) 설계 철학과 도구
fetched: 2026-05-06
status: pending_ingest
tags: [swe-agent, princeton, stanford, aci, agent-computer-interface, mini-swe-agent, swe-bench, neurips-2024, file-viewer, linter]
---

# SWE-agent (Princeton/Stanford)

## 한국어 요약 — 핵심 포인트

NeurIPS 2024 발표(Yang et al., Princeton + Stanford). "Agent-Computer Interface(ACI)" 라는 개념을 정립한 표지석 논문. 핵심 명제: **언어 모델 에이전트는 새로운 카테고리의 end user이며, 이들의 needs/abilities에 맞춘 specially-built interface가 필요하다.**

1. **ACI 설계 원칙** — 언어 모델은 raw bash 환경에서는 잘 동작하지 않음. tool 명령, 출력 포맷, 피드백 모두 LM 친화적으로 재설계.
2. **핵심 도구 4종**:
   - 파일 뷰어 (per-turn 100 lines, 스크롤·검색)
   - 디렉토리 검색 (매칭 파일만 리스팅, 매치 컨텍스트는 안 보여줌 — 모델 혼동 방지)
   - 파일 편집기 + linter 통합 (구문 오류 시 edit 거부)
   - Empty output 처리 ("ran successfully and did not produce any output")
3. **벤치 결과** — SWE-bench 12.5% pass@1, HumanEvalFix 87.7% pass@1. 비대화형 LM SOTA를 압도.
4. **mini-swe-agent 후계** — 더 단순한 아키텍처로 동등 성능. SWE-agent는 maintenance-only.
5. **Configuration** — 단일 yaml 파일로 agents/models/tools/environments/demonstrations 통제. "Free-flowing & generalizable: Leaves maximal agency to the LM"가 모토.

## 1. ACI 설계 철학 (Yang et al. 2024)

### 핵심 명제
> "LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces."

### 문제
> "good ACI design leads to much better results when using agents"

> "a baseline agent without a well-tuned ACI does much worse than SWE-agent"

→ raw bash + 단순한 read/write 도구로는 코딩 에이전트가 잘 동작하지 않음. 무엇을 보여주고 어떻게 피드백하는지가 결정적.

### 접근
> 고정된 LM 가정. ACI 자체를 설계해 "shaping the actions, their documentation, and environment feedback to complement an LM's limitations and abilities."

## 2. 핵심 도구 4종 (swe-agent.com background/aci)

### A. Linter integration on edit
> "a linter that runs when an edit command is issued, and do not let the edit command go through if the code isn't syntactically correct."

→ 구문 오류 코드가 commit되어 후속 단계까지 cascading 하는 것을 차단.

### B. Special-built file viewer
> "works best when displaying just 100 lines in each turn"

스크롤 + 검색 기능 내장. `cat` 같은 raw 도구는 한 번에 너무 많은 컨텍스트를 쏟아내 LM 주의를 분산. 100 라인 슬라이딩 윈도우는 의도적 정보 절약.

### C. Special-built full-directory search
> "we simply list each file that had at least one match. Showing the model more context about each match proved to be too confusing for the model."

→ grep 같은 도구가 매칭 라인까지 전부 보여주면 모델이 노이즈에 압도된다는 경험적 발견. 매치된 파일만 리스팅하는 단순화.

### D. Empty output handling
> "When commands have an empty output we return a message saying 'Your command ran successfully and did not produce any output.'"

→ 빈 출력 = 에러로 잘못 해석할 수 있음. 명시적 성공 메시지로 처리.

## 3. 벤치마크 결과

- **SWE-bench**: 12.5% pass@1
- **HumanEvalFix**: 87.7% pass@1

> "far exceeded the previous state-of-the-art achieved with non-interactive language models"

(이전 SOTA 1.96% → 12.5%로 ~6배 도약. SWE-agent가 SWE-bench라는 "에이전트 코딩" 평가 기준 자체를 정착시킴.)

## 4. Mini-SWE-agent 계승 (swe-agent.com/latest/)

### 현 상태
> "Most of our current development effort is on mini-swe-agent, which has superseded SWE-agent."

> mini-swe-agent "matches the performance of SWE-agent, while being much simpler"

SWE-agent 자체는 "in maintenance-only mode."

### 의미
ACI의 설계 lesson은 정착되었고, 더 작은 코드베이스로 동등 성능 가능 → 결국 ACI 핵심은 "시스템의 간결함이 LM 친화성의 함수"라는 시사.

## 5. SWE-agent Configuration (GitHub README)

### 모토
- "Free-flowing & generalizable: Leaves maximal agency to the LM"
- "Configurable & fully documented: Governed by a single yaml file"
- "Simple & hackable by design"

### Configuration scope
- Agents
- Models
- Tools
- Environments
- Demonstrations

### Container/sandbox
- `.devcontainer` 디렉토리 — VS Code dev container 지원
- GitHub Codespaces 통합
- (별도 sandbox 메커니즘은 mini-swe-agent에서 더 단순화)

## 6. 설계 lesson summary (실무 시사)

| Lesson | 메커니즘 | Why |
|---|---|---|
| 정보 절약 | 100-line viewer | LM 주의 분산 방지 |
| 노이즈 제거 | 매치된 파일만 리스팅 | 매치 컨텍스트가 오히려 혼동 |
| 빠른 피드백 | Linter on edit | syntactic 오류 cascading 차단 |
| 명시성 | Empty output 메시지 | 침묵 = 에러로 오해 방지 |
| 도구 간결성 | yaml 단일 설정 | 재현 가능성 + 쉬운 hacking |

## 7. 다른 하네스와 차이

- **vs Aider**: Aider는 git auto-commit + repo-map 중심. SWE-agent는 SWE-bench 자율 issue 해결 중심으로 ACI 자체 설계에 더 집중.
- **vs OpenHands CodeAct**: CodeAct는 모든 액션을 코드 실행으로 표현. SWE-agent는 명시적 도구 호출 (file viewer, search, edit) 중심.
- **vs Claude Code**: Claude Code는 native multi-tool. SWE-agent는 ACI 자체가 연구 산출물로 분리되어 있음.

## 8. 인용 / 영향

> Yang et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", NeurIPS 2024. arXiv:2405.15793

이 논문이 코딩 에이전트 도구 디자인 분야의 표준 reference로 자리잡았다. 다음 연구에 직접적 영향:
- OpenHands (CodeAct + ACI 결합)
- SWE-Bench/SWE-Bench Verified의 평가 인프라
- Aider 등 도구가 ACI lesson을 internal 도구 디자인에 차용
- mini-swe-agent로 직접 계승

## 출처
- https://arxiv.org/abs/2405.15793 (SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, NeurIPS 2024)
- https://swe-agent.com/0.7/background/aci/ (Agent-Computer Interface 백그라운드)
- https://swe-agent.com/latest/ (최신 docs - mini-swe-agent 계승 안내)
- https://github.com/SWE-agent/SWE-agent (GitHub repo)
- https://github.com/SWE-agent/SWE-agent/blob/main/docs/background/aci.md (ACI markdown)
- https://proceedings.neurips.cc/paper_files/paper/2024/file/5a7c947568c1b1328ccc5230172e1e7c-Paper-Conference.pdf (NeurIPS 2024 paper)

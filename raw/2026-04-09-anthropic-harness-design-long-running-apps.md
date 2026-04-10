---
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
title: Harness Design for Long-Running Application Development
author: Prithvi Rajasekaran (Anthropic Labs)
published: 2026-03-24
fetched: 2026-04-09
---

# Harness Design for Long-Running Application Development

**Author**: Prithvi Rajasekaran, Anthropic Labs
**Published**: March 24, 2026

## Overview

Anthropic 엔지니어링 블로그 공식 포스트. Claude가 고품질 프론트엔드 디자인을 만들고 완전한 애플리케이션을 자율적으로 구축하는 능력을 개선하기 위해 GAN(Generative Adversarial Networks)에서 영감받은 새로운 하네스 디자인 패턴을 제시한다.

## Section 1: Why Naive Implementations Fall Short

두 가지 지속적 실패 모드:

### 1. Context Degradation & "Context Anxiety"

- 긴 작업에서 컨텍스트 창이 채워질수록 모델이 일관성을 잃는다
- **Claude Sonnet 4.5 특이 현상**: "context anxiety" — 모델이 컨텍스트 한계에 접근한다고 믿고 작업을 조기 종료
- **컨텍스트 리셋 vs 컴팩션(compaction) 구분 중요**:
  - 컴팩션: 이전 대화를 요약해서 같은 에이전트가 계속 수행 → clean slate 제공 안 함, context anxiety 지속
  - 리셋: 창을 완전히 비우고 새 에이전트 시작 → 이전 상태·다음 단계를 담은 구조화된 **핸드오프 아티팩트** 필요
- 테스트 결과: "compaction alone wasn't sufficient to enable strong long task performance" (Sonnet 4.5 기준)
- 리셋은 필수이나 "orchestration complexity, token overhead, and latency" 추가

### 2. Self-Evaluation Failures

- 에이전트가 자기 작업을 자신 있게 칭찬함, 품질이 평범할 때조차도
- 특히 바이너리 검증이 없는 주관적 작업(디자인 등)에서 심각
- **핵심 인사이트**: 작업 에이전트와 평가 에이전트를 분리하는 것이 self-criticism보다 효과적
- 평가자도 LLM이라 관대하지만, "tuning a standalone evaluator to be skeptical proves far more tractable than making a generator critical of its own work"

---

## Section 2: Frontend Design — Making Subjective Quality Gradable

저자는 Claude Agent SDK 기반으로 iterative generator-evaluator 루프를 구축.

### Four Grading Criteria (4개 채점 기준)

1. **Design Quality**: Does the design feel coherent rather than a collection of parts? Colors, typography, layout, imagery가 distinct mood and identity로 결합되어야 함.

2. **Originality**: Custom decisions vs template/AI defaults. "telltale signs of AI generation like purple gradients over white cards" 탈락.

3. **Craft**: Technical execution — typography hierarchy, spacing, color harmony, contrast ratios. 대부분의 구현이 기본적으로 적절한 competence check.

4. **Functionality**: Usability independent of aesthetics. 사용자가 인터페이스 목적을 이해하고 primary actions를 찾으며 추측 없이 태스크를 완료할 수 있는가.

**가중치**: 저자는 "design quality and originality over craft and functionality"를 강조. Claude는 technical competence에서 이미 점수가 좋지만 기본값은 "bland" 디자인을 만들기 때문.

### Iterative Process

- Generator가 프롬프트로부터 HTML/CSS/JS 프론트엔드 생성
- Evaluator에 **Playwright MCP** 접근 제공 → 실제 페이지를 navigate, screenshot, 스터디한 후 점수와 비평
- Feedback이 generator로 루프
- **5~15회 iteration per generation**
- 각 평가 후 generator에게 전략적 결정 지시: 점수가 좋으면 현재 방향 refine, 아니면 "pivot to an entirely different aesthetic"
- 풀 런은 "up to four hours" — active page navigation의 실제 wall-clock time 때문

### Calibration

- Few-shot 예시와 상세 점수 breakdown으로 평가자 판단을 저자 선호와 정렬, score drift 감소
- **문구 자체의 영향**: "the best designs are museum quality" 같은 표현이 디자인을 특정 visual convergence로 밀어냄

### 사례: Dutch Art Museum Website

- Iteration 9까지: clean, dark-themed landing page
- Iteration 10: generator가 접근법 완전 폐기 → "3D room with a checkered floor rendered in CSS perspective, artwork hung on the walls in free-form positions, and doorway-based navigation between gallery rooms"로 재상상

---

## Section 3: Scaling to Full-Stack Coding — Three-Agent Architecture

Generator-evaluator 패턴을 풀 스택 개발에 적용. 세 에이전트 시스템:

### Agent 1: Planner

- 최소한의 사용자 입력(1-4 문장)을 전체 제품 스펙으로 확장
- **핵심 제약**: ambitious scope focus, product context와 high-level technical design (granular implementation details 아님)
- **이유**: "if the planner tried to specify granular technical details upfront and got something wrong, the errors in the spec would cascade into the downstream implementation"
- AI features를 제품 스펙에 엮어넣는 기회 식별

### Agent 2: Generator

- 스펙으로부터 sprint 반복 작업
- 한 번에 하나의 기능 구현
- 기술 스택: **React, Vite, FastAPI, SQLite (later PostgreSQL)**
- Sprint 끝에 QA handoff 전 self-evaluation
- git version control 유지

### Agent 3: Evaluator

- **Playwright MCP**로 running 애플리케이션을 end user처럼 수동 클릭
- UI 기능, API 엔드포인트, 데이터베이스 상태 테스트
- 발견된 버그 + "product depth, functionality, visual design, code quality" 기준으로 sprint 채점
- 각 기준에 hard threshold; 실패 시 generator 교정을 위한 상세 피드백

### Sprint Contracts

- 각 sprint 코딩 전, generator와 evaluator가 "sprint contract" 협상
- 정의: "done"이 무엇인지, 성공이 어떻게 검증되는지
- Generator가 구현 접근법과 검증 방법 제안
- Evaluator가 올바른 것을 짓고 있는지 확인
- "iterated until they agreed"
- 고수준 user story와 testable implementation 간 간극을 upfront over-specification 없이 연결

### Inter-Agent Communication

- 에이전트 간 통신은 **파일 기반**
- 한 에이전트가 파일 쓰면 다른 에이전트가 읽고 응답 (같은 파일 내 또는 새 파일)
- 목적: "kept the work faithful to the spec without over-specifying implementation too early"

---

## Section 4: Running the Harness — Retro Game Maker Case Study

**프롬프트**: "Create a 2D retro game maker with features including a level editor, sprite editor, entity behaviors, and a playable test mode."

### Cost-Performance Comparison

| 항목 | Solo Agent | Full Harness |
|---|---|---|
| 시간 | 20분 | 6시간 |
| 비용 | $9 | $200 |
| 비용 배율 | 1x | 20배+ |

"over 20x more expensive, but the difference in output quality was immediately apparent"

### Solo Run Failures

- 인터페이스는 처음엔 기능적으로 보였음
- 레이아웃: fixed-height 패널로 공간 낭비
- 워크플로우: 경직됨 — sprite/entity 생성을 레벨 채우기 전에 요구, UI 가이던스 없음
- **치명적**: "the actual game was broken. My entities appeared on screen but nothing responded to input"
- 코드 분석: "the wiring between entity definitions and the game runtime was broken, with no surface indication of where"

### Full Harness Results

- Planner가 한 문장 프롬프트를 **16 feature 스펙**으로 확장, **10 sprint**
- 포함: sprite animation system, behavior templates, sound/music, AI-assisted sprite/level designers, shareable game exports
- Planner가 frontend design skill에 접근 → 앱의 visual design language를 스펙의 일부로 생성

**결과**:
- "more polish and smoothness than the solo run"
- 캔버스가 전체 viewport 사용, 패널이 합리적 크기, 일관된 visual identity
- Sprite editor: "richer and more fully featured, with cleaner tool palettes, a better color picker, and more usable zoom controls"
- 결정적: 게임이 **실제로 작동** — "move my entity and play the game"
- 약간의 물리 문제 존재 (캐릭터가 플랫폼과 겹침) 그러나 "the core thing worked, which the solo run did not manage"
- Planner의 AI feature 엮기: "built-in Claude integration that let me generate different parts of the game through prompting"

### Evaluator Tuning and QA Challenges

Claude는 초기에 "a poor QA agent"였음.

**초기 문제**:
- Evaluator가 정당한 이슈 식별 → 그러고는 "talk itself into deciding they weren't a big deal and approve the work anyway"
- 표면적 테스트만 수행, 엣지 케이스 probe 안 함
- "more subtle bugs to slip through"

**개선 프로세스**:
- Evaluator 로그 읽기
- 저자 판단과의 divergence 식별
- QA 프롬프트 iteratively 업데이트
- "several rounds of development before the evaluator was grading in a way that I found reasonable"

**Example Evaluator Findings** (game maker sprints에서):

1. Rectangle fill tool failure:
   > "Tool only places tiles at drag start/end points instead of filling the region. `fillRectangle` function exists but isn't triggered properly on mouseUp."

2. Delete key handler bug:
   > "Condition requires both `selection` and `selectedEntityId` to be set, but clicking an entity only sets `selectedEntityId`. Condition should be `selection || (selectedEntityId && activeLayer === 'entity')`."

3. FastAPI routing issue:
   > "`PUT /frames/reorder` route defined after `/{frame_id}` routes. FastAPI matches 'reorder' as a frame_id integer and returns 422: 'unable to parse string as an integer.'"

**잔존 한계**: "small layout issues, interactions that felt unintuitive in places, and undiscovered bugs in more deeply nested features"

**그러나** solo run 대비 "the lift was obvious".

---

## Section 5: Iterating on the Harness for Opus 4.6

"Building Effective Agents" 포스트의 원칙 적용:
> "find the simplest solution possible, and only increase complexity when needed"

**초기 접근**: 급진적 simplification 시도 → 성능 replicate 실패
**효과적 접근**: 컴포넌트를 한 번에 하나씩 제거 (methodical)

### Opus 4.6가 가능하게 한 것

Opus 4.6는:
- "plans more carefully"
- "sustains agentic tasks for longer"
- "can operate more reliably in larger codebases"
- "better code review and debugging skills to catch its own mistakes"
- "long-context retrieval" 대폭 개선

### Sprint Construct 제거

- 저자가 sprint 완전 제거
- Opus 4.6의 향상된 capabilities가 decomposition을 네이티브로 처리하는지 테스트
- Planner와 Evaluator는 유지 — 각각 "obvious value" 지속
- **Planner 없이**: "the generator under-scoped: given the raw prompt, it would start building without first speccing its work, and end up creating a less feature-rich application"

### Evaluator 역할 변화

- Per-sprint 채점 → 단일 end-of-run 패스
- Opus 4.5에서: evaluator 체크가 빌드 전반에 load-bearing이었음
- Opus 4.6에서: "the model's raw capability increased, so the boundary moved outward. Tasks that used to need the evaluator's check to be implemented coherently were now often within what the generator handled well on its own"

**핵심 원칙**:
> "The evaluator is not a fixed yes-or-no decision. It is worth the cost when the task sits beyond what the current model does reliably solo."

### DAW Case Study

**프롬프트**: "Build a fully featured DAW in the browser using the Web Audio API."

**Updated Harness Performance**:

| Agent & Phase | Duration | Cost |
|---|---|---|
| Planner | 4.7 min | $0.46 |
| Build (Round 1) | 2 hr 7 min | $71.08 |
| QA (Round 1) | 8.8 min | $3.24 |
| Build (Round 2) | 1 hr 2 min | $36.89 |
| QA (Round 2) | 6.8 min | $3.09 |
| Build (Round 3) | 10.9 min | $5.88 |
| QA (Round 3) | 9.6 min | $4.06 |
| **Total V2 Harness** | **3 hr 50 min** | **$124.70** |

Builder가 "ran coherently for over two hours without the sprint decomposition that Opus 4.5 had needed"

**QA Findings (First Round)**:
> "This is a strong app with excellent design fidelity, solid AI agent, and good backend. The main failure point is Feature Completeness—while the app looks impressive and the AI integration works well, several core DAW features are display-only without interactive depth: clips can't be dragged/moved on the timeline, there are no instrument UI panels (synth knobs, drum pads), and no visual effect editors (EQ curves, compressor meters). These aren't edge cases—they're the core interactions that make a DAW usable."

**Second Round Gaps**:
- Audio recording "still stub-only (button toggles but no mic capture)"
- Clip resize by edge drag, clip split 미구현
- Effect visualizations: "numeric sliders, not graphical (no EQ curve)"

**최종 결과**:
- "all the core pieces of a functional music production program: a working arrangement view, mixer, and transport running in the browser"
- Integrated agent이 "drive them autonomously, using tools to create a simple production from end to end"
- 시연: set tempo and key, lay down melody, build drum track, adjust mixer levels, add reverb
- Core composition primitives 기능

---

## Section 6: Key Insights & Broader Implications

### 핵심 인사이트

1. **하네스 복잡도는 모델 개선과 함께 감소해야 한다**: 단, 한 번에 한 컴포넌트씩 제거. 어느 조각이 genuinely load-bearing인지 발견하는 과정

2. **Evaluator의 가치는 태스크 난이도에 비례**: 모델의 baseline capability 범위 내 작업에서는 평가 오버헤드가 불필요; frontier 태스크에서는 critical issues를 포착

3. **프롬프트 기준이 출력을 직접 형성**: "museum quality" 같은 표현이 explicit score가 시사하는 것 이상으로 aesthetic direction에 영향

4. **분리가 효과적 튜닝을 가능케 함**: Standalone evaluator를 skeptical로 만드는 것이 generator를 self-critical로 만드는 것보다 tractable

### 저자의 결론적 메시지

> "As models improve, the space of interesting harness combinations doesn't shrink. Instead, it moves, and the interesting work for AI engineers is to keep finding the next novel combination."

> "Every component in a harness encodes an assumption about what the model can't do on its own."

**엔지니어링 cadence**:
1. 타겟 모델로 현실 문제 실험
2. 실행 트레이스 읽기
3. 원하는 결과 달성 위한 performance 튜닝
4. 복잡한 태스크를 specialized agent 역할로 decompose
5. 새 모델 릴리스와 함께 하네스 디자인 재검토 → "stripping away pieces that are no longer load-bearing to performance"

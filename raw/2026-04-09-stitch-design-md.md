---
source_urls:
  - https://stitch.withgoogle.com/docs/design-md/overview/
  - https://stitch.withgoogle.com/docs/design-md/format/
  - https://stitch.withgoogle.com/docs/design-md/usage/
author: Google Stitch Documentation
fetched: 2026-04-09
note: Stitch 공식 문서 3개 페이지(overview/format/usage)의 한국어 요약 + 영어 핵심 구절 보존
---

# Google Stitch — DESIGN.md 문서 (통합 원본)

Stitch는 Google의 AI 기반 디자인 도구. 이 문서는 DESIGN.md 섹션 3개 페이지를 수집한 것이다.

---

## 1. "What is DESIGN.md?" (overview 페이지)

### 요지
모든 프로젝트에는 색상, 폰트, 간격, 컴포넌트 스타일 같은 시각적 아이덴티티가 있다. 전통적으로 이는 Figma 파일, 브랜드 PDF, 또는 디자이너의 머릿속에 존재한다. **이 중 어느 것도 AI 에이전트가 읽을 수 없다.** DESIGN.md가 이를 바꾼다.

DESIGN.md는 사람과 에이전트 모두 읽고, 편집하고, 강제할 수 있는 평문 디자인 시스템 문서다. AGENTS.md의 디자인 버전이라고 생각하면 된다.

### README.md / AGENTS.md / DESIGN.md 비교표

| 파일 | 읽는 주체 | 정의하는 것 |
|------|-----------|-------------|
| README.md | 사람 | 프로젝트가 무엇인지 |
| AGENTS.md | 코딩 에이전트 | 프로젝트를 어떻게 빌드하는지 |
| DESIGN.md | 디자인 에이전트 | 프로젝트가 어떻게 보이고 느껴져야 하는지 |

### 무엇을 얻는가 (What it gives you)

Stitch 같은 디자인 에이전트가 DESIGN.md를 읽으면, 생성하는 모든 화면이 같은 시각 규칙을 따른다: 색상 팔레트, 타이포그래피, 컴포넌트 패턴. 없으면 각 화면이 독립적이다. 있으면 함께 속한 것처럼 보인다.

> "DESIGN.md is a **living artifact**, not a static config file. It evolves as your design evolves."

DESIGN.md는 살아있는 산출물이지 정적 설정 파일이 아니다. 디자인이 진화하면 같이 진화한다. 에이전트가 생성하고, 사용자가 다듬고, 반복하면서 화면에 재적용된다.

### 생성 경로 3가지 (How they're created)

1. **에이전트가 생성하도록 맡기기 (Let the agent generate it)**
   - 분위기(vibe)를 설명
   - 에이전트가 미적 의도를 토큰과 가이드라인으로 번역
   - 예시 프롬프트: "A playful coffee shop ordering app with warm colors, rounded corners, and a friendly feel"

2. **브랜딩에서 파생 (Derive from branding)**
   - 이미 브랜드가 있으면 URL이나 이미지를 제공
   - 에이전트가 팔레트, 타이포그래피, 스타일 패턴을 추출

3. **직접 작성 (Write it by hand)**
   - 고급 사용자는 DESIGN.md를 직접 작성 가능
   - 정확한 디자인 선호를 인코딩
   - **각 섹션은 그냥 마크다운. 특수 문법·도구 필요 없음.**

### 최소 예시 (다크 테마 생산성 앱)

```markdown
# Design System

## Overview
A focused, minimal dark interface for a developer productivity tool.
Clean lines, low visual noise, high information density.

## Colors
- **Primary** (#2665fd): CTAs, active states, key interactive elements
- **Secondary** (#475569): Supporting UI, chips, secondary actions
- **Surface** (#0b1326): Page backgrounds
- **On-surface** (#dae2fd): Primary text on dark backgrounds
- **Error** (#ffb4ab): Validation errors, destructive actions

## Typography
- **Headlines**: Inter, semi-bold
- **Body**: Inter, regular, 14–16px
- **Labels**: Inter, medium, 12px, uppercase for section headers

## Components
- **Buttons**: Rounded (8px), primary uses brand blue fill
- **Inputs**: 1px border, subtle surface-variant background
- **Cards**: No elevation, relies on border and background contrast

## Do's and Don'ts
- Do use the primary color sparingly, only for the most important action
- Don't mix rounded and sharp corners in the same view
- Do maintain 4:1 contrast ratio for all text
```

---

## 2. "The DESIGN.md format" (format 페이지)

### 요지
> "A `DESIGN.md` file has two faces. The **markdown** is what you read and edit, a human-friendly summary of your design system. Underneath, Stitch maintains **structured tokens**, the precise values it uses to enforce consistency during generation."

DESIGN.md는 두 얼굴을 가진다: **마크다운**(사람이 읽고 편집)과 **structured tokens**(Stitch가 생성 시 일관성 강제에 사용하는 정확한 값). 이 페이지는 마크다운에 들어가는 내용을 문서화한다.

### Sections (섹션 목록)

모든 DESIGN.md는 같은 구조를 따른다. 섹션은 프로젝트와 무관하면 생략 가능하지만, **순서는 보존**되어야 한다.

#### 2.1 Overview (개요)

디자인의 look and feel에 대한 전체적 설명. 여기서 퍼스널리티를 묘사한다: 장난스러운가 전문적인가? 밀도가 높은가 여유로운가? 이 섹션은 특정 토큰이 적용되지 않을 때 에이전트의 하이레벨 결정을 가이드한다.

예시:
```markdown
## Overview
A calm, professional interface for a healthcare scheduling platform.
Accessibility-first design with high contrast and generous touch targets.
```

#### 2.2 Colors (색상)

primary, secondary, tertiary, neutral 팔레트. 각 색상은 hex 값과 역할(role)을 포함해야 한다.

예시:
```markdown
## Colors
- **Primary** (#2665fd): CTAs, active states, key interactive elements
- **Secondary** (#6074b9): Supporting actions, chips, toggle states
- **Tertiary** (#bd3800): Accent highlights, badges, decorative elements
- **Neutral** (#757681): Backgrounds, surfaces, non-chromatic UI
```

에이전트는 이 base 값에서 **named colors**도 생성한다: `surface`, `on-primary`, `error`, `outline` 등. Material color role 관례를 따르며 structured tokens에서 사용 가능.

#### 2.3 Typography (타이포그래피)

폰트 패밀리와 타이포그래피 계층(display, headline, title, body, label)에서의 역할.

예시:
```markdown
## Typography
- **Headline Font**: Inter
- **Body Font**: Inter
- **Label Font**: Inter

Headlines use semi-bold weight. Body text uses regular weight at 14–16px.
Labels use medium weight at 12px with uppercase for section headers.
```

headline과 body 폰트의 관계가 중요하다. 같은 패밀리(예: Inter)는 균일함을 전달. 다른 패밀리(예: serif headline + sans-serif body) 혼용은 에이전트가 의도적으로 유지하는 시각적 대비를 생성.

#### 2.4 Elevation (엘리베이션)

깊이(depth)와 계층을 전달하는 방식. 어떤 디자인은 그림자를 쓰고, 어떤 건 평면을 유지.

예시:
```markdown
## Elevation
This design uses no shadows. Depth is conveyed through border contrast
and surface color variation (surface, surface-container, surface-bright).
```

Elevation을 사용하면 shadow 속성(spread, blur, color)과 어떤 컴포넌트가 elevated되어야 하는지 명시.

#### 2.5 Components (컴포넌트)

컴포넌트 atom 스타일 가이드. 애플리케이션에 가장 관련 있는 컴포넌트에 집중.

| 컴포넌트 | 명시할 내용 |
|----------|-------------|
| Buttons | Variants (primary, secondary, tertiary), sizing, padding, corner radius, states |
| Chips | Selection, filter, action variants |
| Lists | Item styling, dividers, leading/trailing elements |
| Inputs | Text fields, text areas, labels, helper text, error states |
| Checkboxes | Checked, unchecked, indeterminate states |
| Radio buttons | Selected and unselected states |
| Tooltips | Positioning, colors, timing |

예시:
```markdown
## Components
- **Buttons**: Rounded (8px), primary uses brand blue fill, secondary uses outline
- **Inputs**: 1px border, surface-variant background, 12px padding
- **Cards**: No elevation, 1px outline border, 12px corner radius
```

#### 2.6 Do's and Don'ts

실천 가이드라인과 일반적 함정. 디자인 생성 시 가드레일 역할.

예시:
```markdown
## Do's and Don'ts
- Do use the primary color only for the single most important action per screen
- Don't mix rounded and sharp corners in the same view
- Do maintain WCAG AA contrast ratios (4.5:1 for normal text)
- Don't use more than two font weights on a single screen
```

### 이중 표현 (The dual representation)

> "The markdown you see is one side. Stitch also stores a **structured version** of the same information: hex values, font enums, spacing scales, and the full named color palette. When you edit the markdown, Stitch reconciles both representations."

사용자가 보는 마크다운은 한쪽 면. Stitch는 같은 정보의 **structured version**도 저장한다: hex 값, font enum, spacing scale, 전체 named color 팔레트. 마크다운을 편집하면 Stitch가 양쪽 표현을 reconcile한다.

이는 마크다운에서 **근사치**로 쓸 수 있다는 뜻("warm colors, rounded feel") — Stitch가 정확한 토큰으로 번역. 또는 **정확하게** 쓸 수 있다("#2665fd", "8px radius") — Stitch가 문자 그대로 존중.

> "Both representations describe the same design system. The markdown is for collaboration. The tokens are for enforcement."

두 표현 모두 같은 디자인 시스템을 묘사. **마크다운은 협업용, 토큰은 강제용**.

---

## 3. "View, edit, and export" (usage 페이지)

### View the design system

**Design System** 패널을 열면 어떤 화면에 대해서든 활성 디자인 시스템을 볼 수 있다. 패널에는 resolved 토큰이 표시된다: 색상, 폰트, roundedness, spacing, 컴포넌트 패턴.

프로젝트에 여러 디자인 시스템이 있으면, 패널은 현재 선택된 화면에 적용된 것을 표시한다.

### Set a default design system

디자인 시스템을 프로젝트의 모든 미래 화면에 적용하려면 프로젝트 기본값으로 선택. 이후 생성되는 새 화면은 자동으로 해당 토큰을 상속.

**기존 화면은 소급 업데이트되지 않는다.** 정렬하려면 디자인 시스템을 개별 적용.

### Edit via the Design System panel

Design System 패널은 활성 디자인 시스템의 직접 편집을 지원. 여기서의 변경은 structured tokens와 DESIGN.md 요약 **양쪽**을 업데이트.

편집 가능 속성:
- **Color palette**: primary, secondary, tertiary, neutral base 색상
- **Typography**: headline, body, label 폰트 패밀리
- **Roundedness**: corner radius scale

더 세밀한 변경(컴포넌트 가이드라인, do's/don'ts, overview narrative)은 DESIGN.md 마크다운을 직접 편집.

### Export with your project

프로젝트를 export하면 DESIGN.md 파일이 생성된 화면과 함께 zip에 포함된다. 이를 통해 downstream consumer(개발자, 다른 디자인 도구, 다른 에이전트)에게 디자인 시스템의 portable 기록을 제공.

> "The exported DESIGN.md is a **standalone document**. It doesn't depend on Stitch to be useful."

export된 DESIGN.md는 standalone 문서. Stitch 없이도 유용하다. 이것이 **portability**의 핵심.

---

## 네비게이션 구조 (Stitch 문서 사이트)

```
STITCH
├── Everything you need to know
├── Effective Prompting
├── Device Types
├── Design Modes
├── Generate design variations
└── Controls & Hotkeys

MCP
├── Setup & Authentication
├── Guide
└── Reference

SDK
├── Build your first design
├── Use with AI SDK
├── Agent-driven workflows
├── How to edit a screen
├── How to generate variants
├── How to download artifacts
├── How to extract themes
├── Reference
└── Architecture

DESIGN.MD
├── What is DESIGN.md?       ← 이 ingest에서 수집
├── The format               ← 이 ingest에서 수집
└── View, edit, and export   ← 이 ingest에서 수집
```

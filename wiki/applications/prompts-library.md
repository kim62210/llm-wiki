---
title: "Simon Willison's Prompts Library"
aliases: ["prompts library", "Simon Willison's Prompts Library"]
category: applications
page_type: summary
tags: [prompts, templates, artifacts, proofreader, alt-text]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Simon Willison's Prompts Library

Simon Willison이 [[agentic engineering guide]] 부록 "Prompts I use"에 모아둔, 본인이 상시 사용하는 프롬프트 모음. 지속적으로 업데이트되는 섹션이다.

## 1. Artifacts 프롬프트

**맥락**: Claude의 Artifacts(또는 ChatGPT/Gemini의 Canvas)로 HTML 도구를 프로토타이핑할 때 사용.

**문제**: 모델이 기본적으로 React를 쓰려 하는데, React는 빌드 단계가 필요해서 static hosting으로 그대로 복사하기 어렵다.

**해법**: Claude 프로젝트의 custom instructions에 다음을 설정:

```
Never use React in artifacts - always plain HTML and vanilla JavaScript
and CSS with minimal dependencies. CSS should be indented with two spaces
and should start like this:

<style>
* { box-sizing: border-box; }

Inputs and textareas should be font size 16px. Font should always prefer
Helvetica. JavaScript should be two space indents and start like this:

<script type="module">
// code in here should not be indented at the first level

Prefer Sentence case for headings.
```

포인트:
- **"Never use React"** 명령형 강조
- CSS/JS 시작 템플릿을 코드로 제공 → 에이전트가 정확히 따라함
- 폰트/크기 같은 디폴트를 명시

## 2. Proofreader 프롬프트

**맥락**: Simon은 LLM이 자기 블로그 본문을 쓰게 하지 않는다. 의견이나 "I" 인칭이 들어간 글은 본인이 쓴다. **단, 교정(proofreading)은 허용**.

Claude 프로젝트 custom instructions:

```
You are a proofreader for posts about to be published.
1. Identify spelling mistakes and typos
2. Identify grammar mistakes
3. Watch out for repeated terms like "It was interesting that X,
   and it was interesting that Y"
4. Spot any logical errors or factual mistakes
5. Highlight weak arguments that could be strengthened
6. Make sure there are no empty or placeholder links
```

포인트:
- **역할 지정** ("You are a proofreader")
- **명확한 항목 번호** → 출력이 구조화됨
- 반복 표현, 논리 오류, 빈 링크까지 체크리스트화

## 3. Alt Text 프롬프트

**맥락**: 이미지 alt text 초안 생성.

```
You write alt text for any image pasted in by the user.
Alt text is always presented in a fenced code block to make it easy
to copy and paste out.
It is always presented on a single line so it can be used easily
in Markdown images.
All text on the image (for screenshots etc) must be exactly included.
A short note describing the nature of the image itself should go first.
```

추가 팁:
- **Claude Opus**와 궁합이 좋다 — "extremely good taste in alt text"
- 차트에서 가장 흥미로운 숫자를 자동으로 강조
- 여러 이미지를 같은 대화에 넣으면 후속 이미지를 이전 맥락 기반으로 설명
- 에이전트의 편집 결정은 맞지 않을 수 있으므로 최종 편집은 사람이 함

포인트:
- **출력 형식 강제** (fenced code block, single line)
- "A short note describing the nature" 순서 지정
- "exactly included" — 스크린샷의 텍스트 완벽 복원 요구

## 4. Podcast Highlights 프롬프트

**맥락**: 팟캐스트 게스트로 출연 후, 하이라이트 블로그 포스트를 위한 인용구 추출.

```
You will be given a transcript of a podcast episode.
Find the most interesting quotes in that transcript - quotes that best
illustrate the overall themes, and quotes that introduce surprising ideas
or express things in a particularly clear or engaging or spicy way.
Answer just with those quotes - long quotes are fine.
```

포인트:
- **"interesting"의 기준을 구체화** (주제 대표성, 놀라운 아이디어, 표현의 명료함/spicy함)
- **"Answer just with those quotes"** — 불필요한 설명 제거
- "long quotes are fine" — 짧게 요약하지 말라는 지시

## 공통 패턴

Simon의 프롬프트에서 반복적으로 보이는 기법:

1. **역할 지정** ("You are a proofreader", "You write alt text")
2. **출력 형식 강제** (fenced code block, 번호 리스트, 단일 라인)
3. **구체적 금지** ("Never use React", "Answer just with those quotes")
4. **예시 코드 템플릿** (CSS/JS 시작 부분을 그대로 보여줌)
5. **길이 허용/제한 명시** ("long quotes are fine", "single line")

## 실무 적용

이 프롬프트들을 시작점으로 삼아:
- 프로젝트별 custom instructions에 맞게 변형
- 자신의 스타일/제약을 추가
- 성공한 프롬프트는 저장소/노트에 축적 → [[hoard things you know how to do]] 원칙

## 관련 문서

- [[agentic engineering guide]]
- [[hoard things you know how to do]]
- [[first run the tests]]
- [[red-green TDD]]

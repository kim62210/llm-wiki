---
source: simonwillison.net
title: "Research: Claude system prompts as a git timeline"
author: "Simon Willison"
date: 2026-04-18
url: "https://simonwillison.net/2026/Apr/18/extract-system-prompts/"
repo: "https://github.com/simonw/research/tree/main/extract-system-prompts"
fetched: 2026-04-20
status: pending_ingest
tags: [system-prompt-archaeology, prompts-as-code, git-workflow, claude-code, anthropic-transparency, agentic-tooling]
---

## 프로젝트 개요

Anthropic이 공개한 시스템 프롬프트 마크다운 문서를 **Claude Code로 자동 분해**해 모델/패밀리/버전별 파일로 재구성하고, 타임스탬프 커밋으로 **가짜(synthetic) git history**를 만든 연구.

## 목적

- 모놀리식 마크다운에서 버전 간 변경을 수작업으로 찾는 대신
- `git log`, `git diff`, `git blame`을 통해 **프롬프트 진화 타임라인 분석** 가능케 함
- GitHub commit view로 브라우저 UI 활용

## 메서드

1. Anthropic published system prompts markdown를 소스로 수집
2. Claude Code CLI로 파일 분해 (model x family x revision 구조)
3. 각 변경에 timestamp 기반 commit을 생성해 synthetic git history 형성
4. 분석은 standard git tooling으로 수행

## 실제 활용

Willison은 이 도구를 써서 **Opus 4.6 → 4.7 변경 분석 (2026-04-18)**을 작성. 별도 블로그 포스트 "Changes in the system prompt between Claude Opus 4.6 and 4.7"의 근거 자료.

## 방법론적 시사점

**프롬프트를 버전 관리 아티팩트로 취급**한다는 패러다임 전환:

- 시스템 프롬프트 변경은 소프트웨어 변경과 동급의 **기술 역사(technical history)**
- `git diff`로 언어 미묘한 차이까지 추적 가능 (ex: `<critical_child_safety_instructions>` 신설, `acting_vs_clarifying` 섹션 추가)
- 연구자는 타임라인으로 안전 강화 패턴, 기능 추가 패턴을 귀납적으로 분석 가능

## 저장소

`https://github.com/simonw/research/tree/main/extract-system-prompts`

README가 구조와 방법론 설명.

## 기존 페이지 업데이트 후보

- `wiki/applications/opus-4-7-system-prompt-diff.md` — 분석 근거 도구로 이 저장소 추가 언급
- `wiki/concepts/system-prompt-archaeology.md` (신규 concept 후보) — "프롬프트를 git으로 추적" 일반 패턴
- `wiki/applications/claude-code-research-workflows.md` (있으면) — Claude Code를 연구 도구로 사용한 사례

## Raw 요약 키워드
system prompt extraction, git timeline synthesis, Claude Code as research tool, prompts as code, Anthropic transparency, synthetic commit history, prompt diff analysis

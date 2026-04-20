---
title: Git with Coding Agents
aliases: [git with coding agents]
category: tooling
page_type: concept
tags: [git, version-control, coding-agents, prompts]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-13
---
# Git with Coding Agents

Simon Willison이 [[agentic-engineering-guide]] Section 2에서 다루는 주제. [[git-worktree-isolation|Git worktree]]을 포함한 Git을 코딩 에이전트의 "시간 여행 도구"로 활용하는 법.

## 왜 Git이 에이전트에게 중요한가

- 변경 **추적, 조사, 되돌리기** 가능
- 에이전트가 망친 것을 복원
- 실험 브랜치로 리스크 격리
- 히스토리를 통해 과거 의도 파악

## Git 기본 (복습)

- **Repository**: 파일 변경을 commit으로 추적하는 폴더
- **Commit**: 타임스탬프가 찍힌 변경 묶음 + 메시지 + 저자
- **Branch**: 독립 실험 후 병합(merge)
- **Clone**: 히스토리를 보존한 복사
- **Remote**: 협업/백업을 위한 원격 복사 (GitHub이 대표)

## 에이전트가 이해하는 자연어 Git 프롬프트

Simon이 예시한, 에이전트가 잘 처리하는 요청들:

| 자연어 프롬프트 | 실제 명령 |
|----------------|-----------|
| "Start a new Git repo here" | `git init` |
| "Commit these changes" | 스테이징 + 커밋 + 메시지 |
| "Add username/repo as a github remote" | `git remote add` |
| "Review changes made today" | `git log` + 필터 |
| "Integrate latest changes from main" | `git fetch` + merge/rebase |
| "Discuss options for integrating changes from main" | merge 전략 설명 |
| "Sort out this git mess for me" | conflict + staging 정리 |
| "Find and recover my code that does..." | `reflog` + branch 검색 |
| "Use git bisect to find when this bug was introduced..." | `git bisect` 실행 |

에이전트는 Git 용어를 충분히 이해하고 있어서 **정확한 명령을 모르는 사용자도 자연어로 지시 가능**하다.

## History 재작성

Simon의 중요한 관점:

> "Consider history as 'deliberately authored story' rather than permanent record."

히스토리는 "있었던 그대로"가 아니라 **의도적으로 저술된 이야기**로 취급하라. 즉 커밋을 재구성할 수 있다.

### Undo / Rewrite

| 프롬프트 | 효과 |
|---------|------|
| "Undo last commit" | `git reset --soft HEAD~1` |
| "Remove [file] from that last commit" | 외과적 커밋 편집 |
| "Combine last three commits with a better commit message" | squash + 메시지 재작성 |

### 저장소에서 저장소 만들기

에이전트는 **커밋 히스토리를 유지한 채 일부 코드를 추출**할 수 있다:
- 라이브러리 분리 (거대 저장소에서 하나의 패키지를 독립시키기)
- 모노레포 → 멀티 저장소 리팩토링
- 기여자 히스토리 보존

## 실무 팁

### 작은 커밋으로 쪼개기
[[anti-patterns|안티패턴 문서]]에서 Simon이 권장하는 것: 여러 작은 PR이 하나의 큰 PR보다 낫다. 에이전트에게 "이 변경을 논리적 단위별 커밋으로 나눠라"라고 지시 가능.

### 리뷰 가능한 diff 유지
에이전트가 만든 diff를 `git log -p`, `git diff` 같은 도구로 본인이 직접 검토. 커밋 메시지도 반드시 본인이 확인.

### 안전망으로서의 브랜치
실험적 변경은 항상 브랜치에서. 실패하면 브랜치 삭제, 성공하면 병합.

## 주의

- **에이전트의 destructive Git 명령은 신중히** — `git reset --hard`, `git push --force`, `git clean -fd` 등
- 중요한 변경 전 `git stash`, `git tag`, 또는 브랜치 백업
- PR 설명도 에이전트가 만들면 반드시 리뷰 ([[anti-patterns]])

## 관련 문서

- [[anti-patterns]]
- [[how-coding-agents-work]]
- [[agentic-engineering-guide]]

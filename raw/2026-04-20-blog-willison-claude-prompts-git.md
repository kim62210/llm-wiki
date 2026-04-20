---
source: blog
title: "Claude system prompts as a git timeline"
author: "Simon Willison"
date: 2026-04-18
url: "https://simonwillison.net/2026/Apr/18/extract-system-prompts/"
fetched: 2026-04-20
status: pending_ingest
---

## Summary

Simon Willison이 Anthropic의 공개된 Claude 시스템 프롬프트를 git 기반 연구 도구로 변환한 프로젝트 문서화. 단일 마크다운 문서를 모델별/패밀리별/리비전별로 분리된 타임스탬프 파일로 재구성하여, git 명령어(git log, diff, blame)로 프롬프트 진화를 추적할 수 있게 함.

## Key Points

- Anthropic은 Claude 시스템 프롬프트를 공개적으로 게시
- 단일 문서를 granular 파일 구조로 변환하여 버전 관리 가능하게 함
- Claude Code를 사용해 마크다운에서 개별 파일로의 변환 자동화 (가짜 커밋 날짜 포함)
- Claude Opus 4.6과 4.7 간의 구체적 차이점 분석에 활용
- 공개 기술 문서를 버전 관리 시스템으로 재구성하면 새로운 연구 방법론이 가능함을 시연

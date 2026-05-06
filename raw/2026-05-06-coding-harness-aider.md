---
source: Aider 공식 문서 + 블로그
url:
  - https://aider.chat/docs/more/edit-formats.html
  - https://aider.chat/docs/repomap.html
  - https://aider.chat/docs/usage/modes.html
  - https://aider.chat/docs/unified-diffs.html
  - https://aider.chat/docs/faq.html
title: Aider 하네스 — repo-map, edit format 6종, architect mode, udiff 벤치마크
fetched: 2026-05-06
status: pending_ingest
tags: [aider, harness, repo-map, edit-format, udiff, architect-mode, search-replace, paul-gauthier, terminal-coding-agent]
---

# Aider 하네스 아키텍처

## 한국어 요약 — 핵심 포인트

Aider(Paul Gauthier)는 터미널 기반 페어 프로그래밍 도구로, 수년에 걸쳐 다양한 모델에서 SWE-bench/내부 벤치 SOTA를 갱신해왔다. 핵심 아키텍처:

1. **Repo map** — git 저장소를 그래프로 모델링(파일=노드, 의존성=엣지). graph ranking 알고리즘으로 가장 중요한 클래스/함수의 시그니처와 타입을 1k 토큰(기본) 안에 압축.
2. **Edit format 6종** — `whole`, `diff` (SEARCH/REPLACE), `diff-fenced` (Gemini용), `udiff` (GPT-4 Turbo용), `editor-diff`, `editor-whole` (architect mode 전용).
3. **Architect mode** — 두 모델 분업. main(architect)이 계획 → editor가 형식 맞춰 편집. o1 + GPT-4o/Sonnet 조합 권장.
4. **Git auto-commit** — 모든 편집을 자동 커밋, 적절한 attribution.
5. **Udiff 혁신** — GPT-4 Turbo의 lazy coding(`# include original method body...`) 행동 3배 감소. 20%→61% 벤치 점수 도약. flexible patching이 9x 에러 감소.

## 1. Repo map (aider.chat/docs/repomap.html)

### 동기
> "Aider sends a repo map to the LLM along with each change request from the user"

> 최선의 코딩을 위해 LLM에게 "the most important classes and functions along with their types and call signatures" 전달.

### 알고리즘
> "analyzing the full repo map using a graph ranking algorithm, computed on a graph where each source file is a node and edges connect files which have dependencies."

(특정 알고리즘 이름은 docs에 명시 안 됨. PageRank 변형으로 알려졌으나 [교차검증 필요])

### Token budget
> `--map-tokens` 기본 1k. "Aider adjusts the size of the repo map dynamically based on the state of the chat."

> "It will usually stay within that setting's value. But it does expand the repo map significantly at times, especially when no files have been added to the chat and aider needs to understand the entire repo as best as possible."

→ 사용자가 명시적으로 파일 추가 안 한 상황에서는 repo map을 확장해 전체 구조를 가능한 한 많이 노출.

## 2. Edit Formats 6종 (aider.chat/docs/more/edit-formats.html)

### Whole
가장 단순. 전체 파일 내용을 fenced code block으로 반환.
```
show_greeting.py
```python
import sys
def greeting(name):
    print("Hey", name)
```
```
> "slow and costly because the LLM has to return the entire file"

### Diff (SEARCH/REPLACE)
효율적, 변경 부분만.
```
mathweb/flask/app.py
```
<<<<<<< SEARCH
from flask import Flask
=======
import math
from flask import Flask
>>>>>>> REPLACE
```
```

### Diff-Fenced
파일 경로를 fence 안쪽에 둠.
> "Primarily used with the Gemini family of models"

### Udiff (Unified diff)
> "GPT-4 Turbo family of models, because it reduced their lazy coding tendencies"

```diff
--- mathweb/flask/app.py
+++ mathweb/flask/app.py
@@ ... @@
-class MathWeb:
+import sympy
+
+class MathWeb:
```

> "Aider tells GPT not to include line numbers, and just interprets each hunk from the unified diffs as a search and replace operation"

### Editor-Diff & Editor-Whole
Architect mode 전용. Architect가 변경을 명세하면 editor가 syntactic하게 정확한 diff/whole을 생성.

## 3. Chat modes (aider.chat/docs/usage/modes.html)

| Mode | Purpose | Model usage |
|---|---|---|
| **Code** (default) | 코드 변경 | 단일 main model |
| **Ask** | 토론, 질문 답변, 변경 X | 단일 main model |
| **Architect** | 2단계: 계획 → 편집 | architect + editor 두 모델 |
| **Help** | Aider 자체 사용법 | 단일 main model |

### Architect 권장 조합
> "pairing an o1 architect with an editor model like GPT-4o or Sonnet will give the best results"

같은 모델을 architect와 editor 양쪽에 써도 OK. editor model의 edit format은 `--editor-edit-format`으로 별도 지정.

## 4. Unified diff format 혁신 (aider.chat/docs/unified-diffs.html)

### Lazy coding 문제
> "lazy coding, where it writes code with comments like '…add logic here…'"

벤치: 89개 python refactoring tasks. GPT-4 Turbo가 12개 task에서 lazy 행동.

### 4가지 설계 원칙
1. **FAMILIAR** — "Choose an edit format that GPT is already familiar with"
2. **SIMPLE** — "Choose a simple format that avoids escaping, syntactic overhead"
3. **HIGH LEVEL** — "Encourage GPT to structure edits as new versions of substantive code blocks"
4. **FLEXIBLE** — "Strive to be maximally flexible when interpreting GPT's edit instructions"

### 메커니즘
> "With unified diffs, GPT acts more like it's writing textual data intended to be read by a program, not talking to a person. Diffs are usually consumed by the patch program, which is fairly rigid. This seems to encourage rigor, making GPT less likely to leave informal editing instructions."

### 벤치마크 결과 (gpt-4-1106-preview)
- SEARCH/REPLACE format: 20%, lazy 12개 task
- Unified diff: 61%, lazy 4개 task → 3배 감소

### 벤치마크 결과 (gpt-4-0613)
- SEARCH/REPLACE: 26%
- Unified diff: 59%

> "Aider's new unified diff editing format outperforms other solutions I evaluated by a wide margin."

### Flexible patching 계층
1. Hunk 정규화: 의도된 버전 간 실제 unified diff 수행
2. Unmarked addition 발견: 원본 파일과 diff
3. "Relative leading white space"로 indentation 변동 처리
4. 큰 hunk를 overlap된 작은 hunk로 분할 후 독립 적용
5. Context window 크기 변동으로 localization

> "Experiments where flexible patching is disabled show a 9X increase in editing errors"

### High-level diff 효과
> "Experiments without 'high level diff' prompting produce a 30-50% increase in editing errors, where diffs fail to apply or apply incorrectly and produce invalid code."

### Folk remedy 검증
> "It's worse to add a prompt that says the user is blind, has no hands, will tip $2000 and fears truncated code trauma. Widely circulated 'emotional appeal' folk remedies produced worse benchmark scores."

## 5. FAQ technical details (aider.chat/docs/faq.html)

### 컨텍스트 전달
> "It does this by analyzing your entire codebase in light of the current chat to build a compact repository map."

### 파일 추가 vs repo map
> "Adding a bunch of files that are mostly irrelevant to the task at hand will often distract or confuse the LLM."

→ 명시적 파일 추가는 수정 대상에 한정. 그 외는 repo map으로.

### Git 통합
> "Aider is tightly integrated with git so all of aider's code changes are committed to the repo with proper attribution."

### Conflict 처리
새 파일 추가가 필요해 사용자 승인되면 "it will re-submit the original request" — 원래 요청을 새로운 파일과 함께 재시도.

### 비용 최적화
> "it's usually best to just add the files to the chat that will need to be modified"

## 6. 엔터프라이즈 / 프로덕션 관점

- **모델 무관성** — Claude/GPT/Gemini/Ollama 모두 지원. 모델별로 최적 edit format 자동 선택.
- **Git-native** — 모든 변경이 commit으로 record → 감사 추적이 자연스럽게 수행.
- **로컬 실행** — 별도 서버 / 클라우드 인프라 없음. 사용자 머신에서 동작.
- **터미널 우선** — IDE 의존성 없어 SSH 환경, 컨테이너, CI에서도 활용 가능.

## 출처
- https://aider.chat/docs/more/edit-formats.html (Edit formats)
- https://aider.chat/docs/repomap.html (Repository map)
- https://aider.chat/docs/usage/modes.html (Chat modes)
- https://aider.chat/docs/unified-diffs.html (Unified diffs make GPT-4 Turbo 3X less lazy)
- https://aider.chat/docs/faq.html (FAQ)

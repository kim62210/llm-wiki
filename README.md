# LLM Wiki

AI/ML 개발 학습용 지식 베이스. Andrej Karpathy의 LLM Wiki 패턴을 기반으로, 일반 개념 노드와 특정 프로젝트/사례 문서를 **페이지 타입** 축으로 분리 관리한다. Obsidian Vault로 바로 사용 가능.

## 디렉토리 구조

```
llm-wiki/
├── CLAUDE.md      # 스키마·타입·편집 규칙 (Claude Code가 작업 시 참조)
├── README.md      # 이 파일
├── index.md       # 전체 페이지 카탈로그 (카테고리 × 타입별)
├── log.md         # 활동 기록 (append-only)
├── raw/           # 원본 소스 (불변, 읽기 전용)
└── wiki/          # 컴파일된 페이지
    ├── foundations/
    ├── architectures/
    ├── training/
    ├── inference/
    ├── rag/
    ├── agents/
    ├── applications/
    ├── papers/
    ├── tooling/
    └── concepts/
```

## 두 축 분류 모델

- **카테고리(category)** — 주제 영역 (foundations/architectures/.../concepts)
- **페이지 타입(page_type)** — 문서 성격

| 타입 | 설명 |
|------|------|
| `concept` | source-agnostic 일반 개념 (여러 소스에서 누적) |
| `entity` | 특정 프로젝트/도구/인물 허브 |
| `project-internal` | 특정 프로젝트 내부 구현·기능 디테일 |
| `case-study` | "어떻게 만들었나" narrative |
| `summary` | 특정 소스의 압축 요약 |
| `paper` | 논문 요약 + 인사이트 |

상세 규칙은 [`CLAUDE.md`](./CLAUDE.md) 참조.

## Obsidian Vault로 열기

1. **Obsidian 설치**: https://obsidian.md
2. **"Open folder as vault"** 선택 → 이 저장소 루트(`llm-wiki/`) 지정
3. 처음 열면 Obsidian이 `.obsidian/` 디렉토리를 자동 생성 (vault 설정 저장)

### 권장 Obsidian 설정

- **Settings → Files & Links**
  - *Use [[Wikilinks]]*: ON
  - *Default location for new notes*: `wiki/concepts` (또는 주로 쓰는 카테고리)
  - *New link format*: `Shortest path when possible`
- **Settings → Appearance → Theme**: 원하는 것
- **Settings → Core plugins**: 다음 활성화 추천
  - Graph view (개념 네트워크 시각화)
  - Backlinks (어떤 페이지가 이 페이지를 참조하는지)
  - Outgoing links
  - Tag pane
  - Search
  - Templates (새 페이지 템플릿)
  - Page preview (링크 hover 시 미리보기)

### 위키링크 해결 방식

모든 페이지는 frontmatter의 `aliases:` 필드를 가진다. 현재 위키는 파일명을 kebab-case(`agentic-engineering-guide.md`)로, 본문 위키링크는 공백형(`[[agentic engineering guide]]`)으로 사용하는데 Obsidian은 aliases로 이 갭을 해결한다.

예:

```yaml
---
title: Agentic Engineering Patterns 가이드 (Simon Willison)
aliases: ["agentic engineering guide", "Agentic Engineering Patterns"]
category: applications
page_type: summary
---
```

본문의 `[[agentic engineering guide]]`는 이 파일의 alias와 매치되어 자동 연결된다.

### Mermaid 다이어그램

Obsidian은 Mermaid를 기본 지원. 기존 8개 페이지에 이미 Mermaid 다이어그램이 있고, 새 페이지 작성 시에도 `CLAUDE.md`의 "다이어그램 작성 규칙 (Mermaid)" 섹션을 따른다.

### Graph View

Obsidian의 Graph view를 열면 페이지 간 위키링크 관계가 인터랙티브 그래프로 시각화된다. `concept` 노드가 허브로 떠오르는 구조라 지식 네트워크 탐색에 유용하다.

## 새 페이지 추가

Claude Code에서 다음 스킬을 사용:

- `/wiki-ingest <URL 또는 파일>` — 소스를 raw/에 저장하고 wiki/로 컴파일
- `/wiki-query <질문>` — 기존 페이지에서 답변 합성
- `/wiki-lint` — 모순/고아 페이지/지식 갭 점검

스킬은 `CLAUDE.md`의 타입 체계와 다이어그램 규칙을 따라 자동으로 페이지를 생성·갱신한다.

## 동기화

저장소 원격: `git@github:kim62210/llm-wiki.git`

Obsidian 파일은 모두 일반 마크다운이므로 git으로 관리된다. 여러 기기에서 쓰려면:
- `git pull` / `git push`로 동기화
- 또는 Obsidian Sync, 또는 커뮤니티 플러그인 "Obsidian Git" 사용

## 라이선스

개인 학습 노트 — 저작권은 각 원본 소스에 귀속. `wiki/` 하위의 요약·정리는 원본 링크와 함께 제공된다.

# AI Development Study Wiki

## 개요
AI/ML 개발 학습을 위한 LLM 기반 지식 위키. Andrej Karpathy의 LLM Wiki 패턴을 따른다.
LLM이 원본 소스를 읽고 구조화된 마크다운 위키로 컴파일하는 방식.

## 디렉토리 구조

```
ai-wiki/
  raw/             # 원본 소스 (논문, 기사, 코드 스니펫 등) - 불변, 읽기 전용
  wiki/            # LLM이 생성/관리하는 마크다운 파일들
  index.md         # 전체 페이지 카탈로그 (카테고리별, 1줄 요약)
  log.md           # 활동 기록 (append-only, 최신이 위)
  CLAUDE.md        # 이 파일 - 스키마/규칙 정의
```

## 카테고리

| 카테고리 | 설명 |
|----------|------|
| foundations | 수학, 통계, 선형대수, 확률론 등 기초 |
| architectures | Transformer, Attention, MoE, SSM 등 모델 구조 |
| training | 사전학습, 파인튜닝, RLHF, DPO 등 학습 기법 |
| inference | 양자화, KV 캐시, 스펙디코딩, 서빙 최적화 |
| rag | 검색 증강 생성, 임베딩, 벡터DB, 청킹 전략 |
| agents | LLM 에이전트, 도구 사용, 계획, 멀티에이전트 |
| applications | 실제 구현 사례, 프로덕션 패턴, 프레임워크 |
| papers | 논문 요약 및 핵심 인사이트 |
| tooling | 개발 도구, 라이브러리, 인프라 |
| concepts | 핵심 개념, 용어 정의, 비교 |

## 페이지 템플릿

모든 위키 페이지는 다음 YAML 프론트매터로 시작한다:

```yaml
---
title: 페이지 제목
category: 카테고리명
tags: [태그1, 태그2]
sources: [raw/파일명.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## 작업 규칙

### Ingest (수집)
1. 소스를 `raw/`에 저장 (원본 보존, 수정 금지)
2. 소스를 읽고 요약 페이지를 `wiki/`에 생성
3. 관련 엔티티/개념 페이지 10-15개를 생성하거나 갱신
4. 페이지 간 `[[위키링크]]` 교차참조 추가
5. `index.md` 업데이트
6. `log.md`에 활동 기록 추가

### Query (질의)
1. `index.md`를 읽고 관련 페이지 식별
2. 관련 페이지를 읽고 답변 합성
3. 좋은 답변이 나오면 새 위키 페이지로 저장 고려
4. 출처가 불분명한 내용은 추측하지 않고 "조사 필요"로 표시

### Lint (점검)
1. 페이지 간 모순 식별
2. 오래된 정보 표시
3. 고아 페이지 (index에 없는 페이지) 정리
4. 누락된 교차참조 추가
5. 지식 갭 식별 및 `index.md`에 TODO로 기록

## 교차참조 규칙
- 같은 개념이 여러 페이지에 등장하면 `[[개념명]]` 형식으로 링크
- 페이지 하단에 `## 관련 문서` 섹션으로 연관 페이지 목록
- 약어는 첫 등장 시 풀네임 병기 (예: RLHF (Reinforcement Learning from Human Feedback))

## 작성 스타일
- 한국어 기본, 기술 용어는 영어 병기
- 간결하고 실용적인 설명 우선
- 코드 예시는 Python 기본
- 수식은 LaTeX 형식 (`$...$`)
- "왜 중요한가", "실무에서 어떻게 쓰이나" 관점 포함

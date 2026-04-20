---
title: 문법 오류 교정 (Grammatical Error Correction)
category: applications
page_type: concept
tags: [nlp, gec, grammar, seq2seq, llm, writing-assistance]
sources: [raw/2026-04-17-topic-queue-v2.md]
created: 2026-04-17
updated: 2026-04-17
---

# 문법 오류 교정 (Grammatical Error Correction, GEC)

**문법 오류 교정(Grammatical Error Correction, GEC)**은 텍스트 내의 문법적 오류를 자동으로 탐지하고 수정하는 NLP 태스크다. 원어민이 아닌 언어 학습자의 글쓰기 지원, 문서 품질 향상, 교육 도구 등 다양한 실용적 응용이 있다.

## 오류 유형 분류

GEC에서 다루는 오류는 체계적으로 분류된다. **ERRANT(ERRor ANnotation Toolkit)** 기준의 주요 유형:

| 오류 유형 | 예시 | 교정 |
|-----------|------|------|
| 관사(Article) | "I have a apple" | "I have **an** apple" |
| 전치사(Preposition) | "arrived to school" | "arrived **at** school" |
| 동사 시제(Verb Tense) | "She go yesterday" | "She **went** yesterday" |
| 주어-동사 일치(SVA) | "He don't know" | "He **doesn't** know" |
| 명사 수(Noun Number) | "two book" | "two **books**" |
| 철자(Spelling) | "recieve" | "**receive**" |
| 어순(Word Order) | "always I eat" | "I always eat" |

## 세 가지 주요 접근 방식

### 1. 시퀀스 태깅 (Sequence Tagging)

입력 토큰 각각에 **편집 레이블(edit label)**을 부여하는 방식이다. KEEP(유지), DELETE(삭제), INSERT(삽입), REPLACE(교체) 등의 태그를 예측하여 원본 텍스트를 편집한다.

대표 모델: **GECToR(Grammatical Error Correction: Tag, not Rewrite)**

```mermaid
flowchart LR
    Input["She go yesterday"] --> Tagger[시퀀스 태거\nBERT 기반]
    Tagger --> Tags["She:KEEP / go:REPLACE_went / yesterday:KEEP"]
    Tags --> Output["She went yesterday"]
```

장점: 빠른 추론 속도, 해석 가능성
단점: 복잡한 재구조화(어순 변경 등)에 제한적

### 2. [[seq2seq]] 방식

오류 문장을 소스 시퀀스로, 교정 문장을 타겟 시퀀스로 설정하여 번역처럼 학습하는 방식이다. [[transformer-architecture]] 기반 인코더-디코더 구조(T5, BART 등)가 주로 사용된다.

```mermaid
flowchart LR
    Src["오류 문장\n(소스)"] --> Enc[인코더]
    Enc --> Dec[디코더]
    Dec --> Tgt["교정 문장\n(타겟)"]
```

장점: 복잡한 오류 패턴 처리 가능, 전체 문장 재구성 지원
단점: 느린 추론, 할루시네이션(내용 변경) 위험

### 3. LLM 기반 접근

대규모 언어모델(GPT-4, Claude 등)에 프롬프트를 주어 교정을 요청하는 방식이다. 별도 파인튜닝 없이도 높은 성능을 보이며, 교정 이유 설명(feedback)까지 생성할 수 있다.

```python
# LLM 기반 GEC 예시
prompt = """
다음 문장의 문법 오류를 교정하라. 교정된 문장만 출력하라.
원문: She don't like the musics.
교정:
"""
# 출력: She doesn't like music.
```

장점: 제로샷/퓨샷 적용 가능, 설명 생성 가능
단점: 비용, 속도, 일관성 이슈

## 학습 데이터

GEC 모델 학습에는 **오류 문장 - 교정 문장 쌍(parallel corpus)**이 필요하다.

| 데이터셋 | 언어 | 규모 | 특징 |
|----------|------|------|------|
| FCE(First Certificate in English) | 영어 | 33K 문장 | 영어 학습자 에세이 |
| CoNLL-2014 Shared Task | 영어 | 1,312 문장 | GEC 표준 벤치마크 |
| JFLEG | 영어 | 1,601 문장 | 유창성 교정 포함 |
| Lang-8 | 다국어 | 수백만 | 언어 교환 학습자 작성 |
| W&I+LOCNESS | 영어 | 43.2K | 다양한 영어 능숙도 수준 |

## 평가 지표

- **M2(MaxMatch) F0.5**: 정밀도에 더 가중치를 두는 F-beta 스코어. 과교정(overcorrection)을 억제하기 위해 F0.5 사용
- **ERRANT F0.5**: ERRANT 오류 유형별 세분화 평가
- **GLEU**: BLEU의 GEC 변형 버전, JFLEG에서 주로 사용

## 현대 GEC 시스템의 특징

현재 최고 성능 시스템은 다음 기법을 조합한다:

1. **사전학습 언어모델** ([[bert]], DeBERTa 등)로 문맥 표현 강화
2. **데이터 증강**: 정상 텍스트에 인공 오류를 주입하여 학습 데이터 확대
3. **앙상블**: 태깅 방식 + seq2seq 방식 조합으로 상호 보완
4. **반복 교정(Iterative correction)**: 한 번에 모든 오류를 교정하는 대신 여러 라운드에 걸쳐 단계적으로 교정

## 실무 배포 고려사항

- **보수성(Conservatism)**: 오류가 아닌 부분을 수정하는 과교정(overcorrection)은 신뢰를 해친다. F0.5를 쓰는 이유
- **원본 의미 보존**: 교정이 원본의 의미를 바꾸면 안 된다
- **사용자 인터페이스**: 교정 위치와 이유를 함께 표시하여 학습 효과 제공
- **도메인 특화**: 법률 문서, 학술 논문 등 도메인별 스타일 가이드 반영 필요

## 관련 문서

- [[seq2seq]] - GEC의 주요 접근 방식인 시퀀스-투-시퀀스 학습 구조
- [[transformer-architecture]] - seq2seq 기반 GEC 모델의 핵심 아키텍처
- [[text-classification]] - GEC와 유사한 문장 수준 NLP 태스크

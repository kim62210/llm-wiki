---
title: 시퀀스 레벨 지식 증류
category: training
page_type: concept
tags: [지식증류, 시퀀스학습, 기계번역, NMT, 빔서치]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# 시퀀스 레벨 지식 증류 (Sequence-Level Knowledge Distillation)

시퀀스 레벨 지식 증류(Sequence-Level KD)는 Kim & Rush(2016)가 제안한 방법으로, 교사 모델의 지식을 **토큰 단위**가 아닌 **전체 시퀀스(문장) 단위**로 전달한다. 기계 번역(NMT) 분야에서 처음 제안되었으며, 이후 모든 자기회귀 언어 모델 증류의 기초 방법론이 되었다.

## 토큰 레벨 vs 시퀀스 레벨 증류

```mermaid
flowchart TD
    subgraph TokenLevel["토큰 레벨 증류 (Word-Level KD)"]
        T_Teacher[교사 모델] --> T_Logit[각 위치의 토큰 로짓\np(y_t | y_{<t}, x)]
        T_Student[학생 모델] --> T_Match[각 위치에서 KL 발산 최소화]
        T_Logit --> T_Match
    end

    subgraph SeqLevel["시퀀스 레벨 증류 (Seq-Level KD)"]
        S_Teacher[교사 모델] --> S_Beam[빔 서치로\n최적 번역 생성]
        S_Beam --> S_Corpus[교사 번역 코퍼스\n합성 데이터]
        S_Corpus --> S_Train[학생 모델\n합성 코퍼스로 학습]
    end
```

핵심 차이: 토큰 레벨은 각 위치에서 교사의 소프트 레이블을 직접 모방하고, 시퀀스 레벨은 교사가 생성한 완성된 문장을 새 학습 데이터로 활용한다.

## 3가지 증류 방식

Kim & Rush(2016)는 세 가지 방식을 제안하고 비교했다.

### 방식 1: 단어 레벨 지식 증류 (Word-Level KD)

교사의 소프트 레이블을 각 타임스텝마다 직접 학습한다.

$$L_{word} = -\sum_t \sum_v p_T(v | y_{<t}, x) \log p_S(v | y_{<t}, x)$$

장점: 교사의 불확실성 정보(불확실한 후보 토큰들) 전달
단점: 어휘 크기(|V|) 만큼 교사 forward pass 필요 -> 메모리/연산 부담

### 방식 2: 시퀀스 레벨 지식 증류 (Sequence-Level KD) - 핵심

교사 모델로 빔 서치를 실행하여 최적 번역을 생성하고, 이를 새 학습 데이터로 사용한다.

```python
def create_seq_level_dataset(teacher_model, source_sentences, beam_size=4):
    """시퀀스 레벨 KD 데이터셋 생성"""
    seq_kd_corpus = []

    for src in source_sentences:
        # 교사 모델로 빔 서치 번역 생성
        teacher_translations = teacher_model.beam_search(
            src,
            beam_size=beam_size,
            max_length=200
        )
        # 최고 점수 번역 선택
        best_translation = teacher_translations[0]
        seq_kd_corpus.append((src, best_translation))

    return seq_kd_corpus

# 학생 모델 학습: 합성 코퍼스로 일반 크로스 엔트로피
student_model.train(seq_kd_corpus, loss_fn="cross_entropy")
```

장점: 구현 단순, 추가 메모리 부담 없음, 병렬 데이터 생성 가능
단점: 빔 서치의 결과만 학습 (다양성 부족)

### 방식 3: 시퀀스 보간 지식 증류 (Sequence-Level Interpolation)

원본 정답(gold)과 교사 번역을 모두 활용하여 보간한다.

$$L_{interp} = \lambda L_{seq-KD} + (1-\lambda) L_{gold}$$

## 왜 시퀀스 레벨이 효과적인가

### 교사 번역의 "단순화" 효과

교사 모델이 생성한 번역은 원본 인간 번역보다 **예측 가능하고 일관된 패턴**을 보인다. 학생 모델 입장에서는 이런 "단순화된" 패턴이 더 학습하기 쉽다.

```mermaid
flowchart LR
    Src[원본 소스\n"I love cats"] --> HumanTrans[인간 번역\n"나는 고양이를 사랑합니다"\n다양한 표현 존재]
    Src --> TeacherTrans[교사 번역\n"나는 고양이를 사랑합니다"\n일관된 패턴]

    HumanTrans --> Hard[학생 학습 어려움\n다양성으로 인한 혼란]
    TeacherTrans --> Easy[학생 학습 용이\n일관된 신호]
```

이를 "데이터 단순화(data simplification)" 효과라고 부른다.

### 노출 편향(Exposure Bias) 완화

기존 MLE 학습은 학습 시 정답 이전 토큰을 보여주지만, 추론 시에는 모델 자신의 이전 출력을 입력으로 사용한다(teacher forcing vs free running). 교사 번역으로 학습하면 학생 모델이 자신의 출력 분포와 더 유사한 환경에서 학습하게 된다.

## 적용 범위 확장

시퀀스 레벨 KD는 기계 번역 외에도 광범위하게 적용되었다.

### 자동 요약
```python
# 교사 모델(대형)로 요약 생성
teacher_summaries = [
    teacher.summarize(article) for article in documents
]
# 학생 모델은 교사 요약을 타겟으로 학습
student.train(documents, teacher_summaries)
```

### 대화 시스템
교사 모델의 응답 패턴을 소형 학생 모델이 흉내내도록 학습.

### LLM 경량화
GPT-4 같은 대형 모델의 출력을 타겟으로 소형 모델을 학습하는 패턴 - DistilGPT-2, Phi-1.5 등이 이 방식의 변형을 사용.

## 빔 크기와 성능 트레이드오프

빔 서치의 빔 크기(beam size)는 생성 품질과 다양성에 영향을 준다.

| 빔 크기 | 교사 번역 품질 | 데이터 다양성 | 데이터 생성 속도 |
|--------|-------------|------------|--------------|
| 1 (탐욕적) | 보통 | 매우 낮음 | 매우 빠름 |
| 4-8 | 좋음 | 낮음 | 빠름 |
| 12-20 | 매우 좋음 | 중간 | 느림 |

실무에서는 빔 크기 4-8을 주로 사용한다.

## 시퀀스 레벨 KD의 한계

### 최빈값 추구 편향 (Mode-Seeking)
빔 서치는 가장 확률 높은 시퀀스만 선택하므로, 교사 분포의 다양성을 포착하지 못한다. 이 한계를 극복하기 위해 [[minillm-text-distillation]]은 역KL 발산을 활용한다.

### 교사 오류 전파
교사 모델의 실수가 학습 데이터에 포함되어 학생에게 전파된다.

### 계산 비용
대규모 코퍼스에 빔 서치를 적용하는 것은 시간이 오래 걸린다. 병렬화가 필수.

## 역사적 맥락

시퀀스 레벨 KD는 원래 NMT 모델 경량화를 위해 제안되었지만, 이후:

1. **LLM 사전학습 증류**: Phi-1, Phi-1.5 등이 교사 LLM 출력으로 소형 모델 학습
2. **합성 데이터 생성**: [[self-instruct-original]], [[orca-progressive-learning]] 등이 유사 철학 적용
3. **MiniLLM**: 역KL 발산으로 이 방법론을 발전시킴

## 관련 문서

- [[knowledge-distillation]] - 지식 증류 기본 개념
- [[distilbert-distillation]] - 트랜스포머에서의 증류 대표 사례
- [[minillm-text-distillation]] - 시퀀스 레벨 KD의 발전된 형태
- [[supervised-fine-tuning]] - 증류된 데이터로 학습하는 방법
- [[orca-progressive-learning]] - 교사 출력 활용의 또 다른 관점

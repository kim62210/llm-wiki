---
title: BLEU / ROUGE / METEOR (자동 평가 지표)
category: training
page_type: concept
tags: [bleu, rouge, meteor, evaluation, nlp]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# BLEU / ROUGE / METEOR (자동 평가 지표)

## 개념 요약

BLEU, ROUGE, METEOR는 생성 텍스트를 참조 텍스트(reference)와 비교해 자동으로 품질을 측정하는 전통적인 NLP 지표다. 번역/요약/생성 태스크의 개발 사이클을 가속하는 데 유용하지만, LLM 시대에는 한계가 뚜렷하게 드러나 보완적 지표들이 등장하고 있다.

## BLEU (Bilingual Evaluation Understudy)

**용도**: 기계 번역 평가 (Papineni et al., 2002)

**원리**: 생성문에서 n-gram이 참조문에 얼마나 등장하는지 **정밀도(precision)** 기반으로 측정한다.

$$
\text{BLEU} = \text{BP} \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)
$$

- $p_n$: n-gram precision (1~4-gram 가중 평균)
- BP(Brevity Penalty): 너무 짧은 생성문에 패널티
- BLEU-4가 가장 널리 사용됨

**한계**:
- Recall을 고려하지 않아 너무 짧은 정답을 선호
- 의미적 동의어를 구분하지 못함 ("car" vs "automobile")
- 언어별, 도메인별 절대값 의미가 상이함

## ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

**용도**: 텍스트 요약 평가 (Lin, 2004)

**원리**: 참조 요약과의 n-gram **재현율(recall)** 기반 측정.

주요 변형:
- **ROUGE-N**: n-gram 재현율 (`ROUGE-1`, `ROUGE-2` 가장 일반적)
- **ROUGE-L**: 최장 공통 부분 수열(LCS, Longest Common Subsequence) 기반
- **ROUGE-S**: Skip-bigram 기반

$$
\text{ROUGE-N} = \frac{\sum_{\text{ref}} \sum_{n\text{-gram}} \text{Count}_{match}}{\sum_{\text{ref}} \sum_{n\text{-gram}} \text{Count}_{ref}}
$$

**한계**: 어순, 의미적 유사성을 반영하지 못함.

## METEOR (Metric for Evaluation of Translation with Explicit ORdering)

**용도**: 번역 평가, BLEU의 대안 (Banerjee & Lavie, 2005)

**원리**: Precision/Recall의 F-score + **어순 패널티(fragmentation penalty)**.

- 어간 일치(stemming)와 동의어 사전(WordNet) 기반 정렬 수행
- 단어 순서 연속성이 점수에 반영됨
- BLEU보다 인간 판단과의 상관관계가 높음

## 세 지표 비교표

| 지표 | 기반 | 주 용도 | 강점 | 약점 |
|------|------|---------|------|------|
| BLEU | Precision | 번역 | 빠른 계산, 광범위 사용 | Recall 무시, 의미 맹목 |
| ROUGE-N | Recall | 요약 | Recall 반영 | 어순 무시, 의미 맹목 |
| ROUGE-L | LCS | 요약 | 어순 부분 반영 | 장거리 순서 민감도 낮음 |
| METEOR | F-score + 정렬 | 번역 | 동의어/어간 처리 | 언어별 자원 필요 |

## LLM 시대 대안 지표

기존 지표들의 한계를 극복하기 위해 다음 지표들이 주목받고 있다:

- **BERTScore**: BERT 임베딩 기반 코사인 유사도 비교. 의미론적 유사성을 포착
- **COMET**: 학습 기반 번역 품질 추정(QE) 모델. 소스 문장도 활용
- **LLM-as-Judge**: GPT-4 등 LLM이 직접 평가. 열린 형태의 생성 평가에 강력
- **UniEval**: 일관성/유창성/관련성 등 여러 차원을 동시 측정

## 자동 평가의 근본적 한계

```mermaid
flowchart LR
    HumanJudgment[인간 판단\n(Ground Truth)] -.약한 상관.-> AutoMetric[자동 지표\nBLEU/ROUGE]
    AutoMetric -->|최적화| Model[모델]
    Model -.Goodhart's Law.-> HumanJudgment
```

- 자동 지표를 직접 최적화 대상으로 삼으면 지표는 높아지지만 실제 품질은 저하되는 Goodhart 문제 발생
- 따라서 개발/디버깅 보조 지표로 사용하되, 최종 평가는 인간 평가나 LLM-as-Judge를 병행해야 한다

## 관련 문서

- [[perplexity-metric]] - 언어 모델의 다른 자동 지표
- [[benchmark-design-principles]] - 평가 설계의 원칙
- [[evaluation-during-training]] - 학습 중 평가 전략
- [[instruction-tuning]] - 평가가 중요한 SFT 단계

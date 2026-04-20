---
title: Synthetic Eval Data Generation
category: concepts
page_type: concept
tags: [concepts, concept, [[synthetic-data-training|synthetic]], eval, data, generation, evals-and-observability]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/synthetic-eval-data-generation.md, raw/hot-topics-sources/2026-04-10/252-data-swarms-optimizable-generation-of-synthetic-[[rubric-based-evals|evaluation]]-data.md, raw/hot-topics-sources/2026-04-10/253-on-llms-driven-synthetic-data-generation-curation-and-evaluation-a-survey.md, raw/hot-topics-sources/2026-04-10/254-synthetic-data-generation-using-llms-advances-in-text-and-code.md, raw/hot-topics-sources/2026-04-10/255-data-flywheels-for-llm-applications.md, raw/hot-topics-sources/2026-04-10/256-who-validates-the-validators-evalgen.md]
created: 2026-04-10
updated: 2026-04-15
---
# Synthetic Eval Data Generation

LLM을 사용해 평가용 테스트 케이스를 자동으로 생성하고, 다양성과 난이도를 조절해 실제 인간 평가와 높은 상관관계를 갖는 평가 데이터셋을 구축하는 방법론.

## 왜 필요한가

수작업 골든 데이터셋(golden dataset) 구축의 한계:
- **확장성**: 인간 레이블러 비용이 에이전트 성능 향상 속도를 따라가지 못함
- **다양성**: 사람이 예상하는 케이스에만 편중 -> 모델이 보지 못한 분포 공백
- **난이도 조절**: 쉬운 케이스 위주 -> 변별력 낮은 평가셋
- **지속성**: 모델이 발전할수록 기존 테스트 셋이 포화 상태에 도달

합성 데이터 생성은 이 제약을 완화하지만, "평가자 오염(evaluator contamination)" 문제를 새로 야기한다.

## 생성 파이프라인

```mermaid
flowchart TD
    A[시드 입력\nSeed Prompts] --> B[다양화\nDiversification]
    B --> B1[주제 변형]
    B --> B2[복잡도 변형]
    B --> B3[스타일 변형]
    B --> B4[엣지 케이스 생성]

    B1 --> C[합성 테스트 케이스]
    B2 --> C
    B3 --> C
    B4 --> C

    C --> D[품질 필터링]
    D --> D1{인간 검토\n(샘플링)}
    D1 -->|통과| E[골든 셋 추가]
    D1 -->|실패| F[폐기]

    E --> G[평가 실행]
    G --> H[인간-자동 상관 분석]
    H -->|상관 낮음| I[생성 파이프라인 개선]
    H -->|상관 높음| J[확장 배포]
```

## Data Swarms: 적대적 생성

2025년 등장한 **Data Swarms** 방법론은 PSO(Particle Swarm Optimization)을 사용해 "모델이 틀리기 쉬운" 어려운 테스트 케이스를 적대적으로 생성한다:

1. 입자(particle) = 테스트 케이스의 변형 파라미터
2. 적합도(fitness) = 대상 모델이 틀리는 정도
3. PSO가 최악의 케이스를 향해 수렴

이 방법으로 기존 수작업 데이터셋에서 발견하지 못한 체계적 실패 패턴을 발견할 수 있다.

## EvalGen: 평가자 검증

"누가 평가자를 검증하는가?(Who Validates the Validators?)"의 답으로 제안된 EvalGen:
- 합성 생성된 eval 케이스를 소규모 인간 패널로 검증
- 인간 판단과 일치하는 케이스만 골든 셋에 포함
- 자동화된 eval 기준의 인간 정렬도를 지속적으로 측정

## 다양성 확보 전략

| 전략 | 방법 | 효과 |
|------|------|------|
| 의미적 다양화 | 임베딩 클러스터링으로 중복 제거 | 분포 편향 감소 |
| 난이도 계층화 | 쉬움/중간/어려움 균등 분배 | 변별력 향상 |
| 실패 모드 타게팅 | 에러 분석에서 발견된 패턴 집중 생성 | 취약점 커버리지 |
| 반사실 생성 | "만약 이랬다면" 변형 케이스 | 로버스트니스 측정 |
| 언어/문화 다양화 | 다국어, 다문화 케이스 포함 | 일반화 측정 |

## 데이터 플라이휠 (Data Flywheel)

Shreya Shankar의 데이터 플라이휠 개념:

```mermaid
flowchart LR
    A[프로덕션 사용] --> B[트레이스 수집]
    B --> C[실패 케이스 추출\n자동 + 사용자 피드백]
    C --> D[합성 변형 생성\n유사 어려운 케이스]
    D --> E[골든 셋 추가]
    E --> F[모델 개선\n파인튜닝 or 프롬프트]
    F --> A
```

이 루프가 돌수록 평가셋이 실제 프로덕션 분포에 가까워진다.

## 주의사항: 평가자 오염

합성 데이터 생성 모델과 평가 대상 모델이 같을 경우, 평가 데이터가 모델의 편향을 그대로 반영할 수 있다:
- GPT-4로 생성한 데이터를 GPT-4로 평가 -> 자기 확인 루프
- 해결책: 생성 모델과 평가 모델을 다른 제품군으로 분리

## 인간 평가와의 상관 검증

합성 평가셋의 유효성 확인 기준:
- 인간 판단과 Pearson 상관 > 0.7 이상
- 100-200개 샘플을 인간이 직접 검토
- 시스템 레벨 랭킹이 인간 선호와 일치하는지 확인

## 대표 자료

- [Data Swarms: Optimizable Generation of Synthetic Evaluation Data (arXiv:2506.00741)](https://arxiv.org/abs/2506.00741)
- [On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey (arXiv:2406.15126)](https://arxiv.org/abs/2406.15126)
- [Synthetic Data Generation Using LLMs: Advances in Text and Code (arXiv:2503.14023)](https://arxiv.org/abs/2503.14023)
- [Data Flywheels for LLM Applications (Shreya Shankar)](https://www.sh-reya.com/blog/ai-engineering-flywheel/)
- [Who Validates the Validators? EvalGen (arXiv:2404.12272)](https://arxiv.org/abs/2404.12272)

## 관련 문서

- [[error-analysis-for-evals|Error Analysis for Evals]]
- [[llm-as-judge-calibration|LLM-as-Judge Calibration]]
- [[rubric-based-evals|Rubric-Based Evaluation Frameworks]]
- [[llm-observability-platforms|LLM Observability Platforms]]

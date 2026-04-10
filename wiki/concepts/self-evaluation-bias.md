---
title: Self-Evaluation Bias (자기평가 편향)
aliases: ["self-evaluation bias", "self evaluation bias", "자기평가 편향", "self-critique failure"]
category: concepts
page_type: concept
tags: [failure-mode, llm-as-judge, evaluator, bias, multi-agent]
sources: [raw/2026-04-09-anthropic-harness-design-long-running-apps.md]
created: 2026-04-09
updated: 2026-04-09
---

# Self-Evaluation Bias (자기평가 편향)

## 정의

**Self-Evaluation Bias**는 LLM이 **자기 작업을 자기 자신이 평가**할 때 체계적으로 **과도하게 관대해지는** 경향이다. 출력 품질이 평범하거나 심지어 잘못되었을 때조차 모델은 자신 있게 자기 작업을 칭찬하는 패턴을 보인다.

> "Agents reliably praise their own work even when quality is mediocre."

## 왜 문제인가

Self-evaluation은 하네스 설계에서 매력적인 선택지다. 추가 에이전트 없이 하나의 루프 안에서 "작업 → 검토 → 개선" 흐름이 가능하기 때문. 그러나 이 접근은 특정 조건에서 체계적으로 실패한다:

### 악화 조건

1. **주관적 태스크** — 디자인, 카피라이팅, 사용자 경험, 아키텍처 판단. 바이너리 verifier가 없음
2. **긴 작업** — 누적된 컨텍스트에서 이전 결정을 정당화하려는 편향이 강화됨
3. **복잡한 trade-off** — "이 정도면 충분하다"고 스스로를 설득할 여지가 많음

### 전형적 실패 패턴

- 정당한 이슈를 식별한 뒤 "크게 중요하지 않다"며 dismiss
- 표면적인 해피 패스만 확인하고 엣지 케이스를 probe 안 함
- 자기 가설을 검증하는 데 편향된 테스트 설계
- 버그를 "feature"로 재해석

Anthropic 사례에서 관찰된 초기 동작:

> "Claude was initially a poor QA agent ... it would talk itself into deciding they weren't a big deal and approve the work anyway."

## 해법: [[generator-evaluator architecture|작업과 평가의 분리]]

가장 효과적인 완화책은 **작업 에이전트(generator)와 평가 에이전트(evaluator)를 구조적으로 분리**하는 것이다. 두 에이전트가 같은 모델을 써도 된다 — 핵심은 **역할 분리**다.

### 왜 분리가 효과적인가

- **역할에 따른 행동 변화**: 같은 모델이라도 "judge" 역할로 설정되면 "maker" 역할보다 비판적으로 동작함
- **컨텍스트 독립**: Evaluator는 generator의 내부 추론 과정을 보지 못하므로 그 과정에 감정적으로 투자되지 않음
- **튜닝의 용이성**:

> "tuning a standalone evaluator to be skeptical proves far more tractable than making a generator critical of its own work"

### 분리가 완벽한 해결책은 아니다

Evaluator도 LLM이라 여전히 관대함의 여지가 있다. 그러나 **"관대한 judge를 skeptical하게 튜닝"** 하는 것이 **"enthusiastic maker를 self-critical하게 튜닝"** 하는 것보다 훨씬 tractable하다. 전자는 평가 프레임만 바꾸면 되지만, 후자는 creative drive 자체를 억제해야 하기 때문.

## Evaluator 튜닝 방법

Self-evaluation bias를 회피하기 위해 generator-evaluator를 도입했어도, evaluator 자체의 관대함을 다뤄야 한다:

1. **Few-shot calibration** — 점수 예시를 다수 제공해 "이 정도면 몇 점"의 기준점 고정
2. **Hard threshold** — 각 기준에 minimum score, 하나라도 미달이면 fail
3. **Tool 접근 확대** — Playwright 같은 실행 도구로 표면 테스트를 벗어남
4. **로그 리뷰 루프** — 인간이 주기적으로 evaluator 판단 로그를 읽고 divergence 파악
5. **Criterion 재정의** — 관대함이 나타나는 criterion 문구를 iteratively 업데이트

## 다른 완화 전략

분리 외 보조 전략들:

- **Adversarial 프롬프팅**: "이 작업의 최악의 실패 모드 5가지를 찾아라"
- **Role injection**: Evaluator에게 "skeptical senior reviewer" 같은 역할 부여
- **Cross-validation**: 여러 evaluator가 독립적으로 평가하고 disagreement 발생 시 human escalation
- **Execution-based verification**: 가능한 곳은 모두 실제 실행 결과 기반 ([[red-green tdd|TDD]], 컴파일러, 린터 — [[harness quadrants|Computational 사분면]])

## 관련 문서

- [[generator-evaluator architecture]] — self-evaluation bias의 대표 완화 패턴
- [[harness engineering]] — 이 편향은 하네스 엔지니어링이 해결하는 핵심 문제 중 하나
- [[harness quadrants]] — Inferential 사분면은 이 문제를 정면으로 다룬다
- [[anthropic harness design]] — Evaluator tuning 사례 포함
- [[blind prompting]] — 관련 프롬프트 안티패턴 (경험적 검증 없는 자신감)
- [[red-green tdd]] — 바이너리 verifier가 가능할 때의 대안

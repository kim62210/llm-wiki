---
source: github
url: https://github.com/openai/simple-evals
title: simple-evals (OpenAI) — 가벼운 zero-shot CoT 평가 프레임워크
fetched: 2026-05-06
status: pending_ingest
---

# simple-evals (OpenAI)

## 한 줄 요약

> "We are emphasizing the _zero-shot, chain-of-thought_ setting, with simple instructions like 'Solve the following multiple choice problem'."

OpenAI 가 공개한 minimal evaluation framework. **comprehensive `evals` framework 와 별개**로, instruction-tuned 모델 평가를 위한 단순 zero-shot CoT 패턴에 집중. 활발히 유지보수되지 않으나 (모델 launch 시점 결과 공개용), 동시에 GPT-5, GPT-5.5 등 주요 launch 의 reference benchmark 로 쓰인다.

## 위치 및 의도

> "This repository is NOT intended as a replacement for the comprehensive evals collection."
>
> — README

zero-shot CoT 가 base model 보다 instruction-tuned model 의 실제 사용에 더 가깝다는 가정. few-shot prompt engineering 이 모델 비교를 왜곡할 수 있다는 우려에서 출발.

## 포함된 9개 eval

| Eval | 도메인 |
|---|---|
| MMLU | 57 subject 다과목 이해 |
| MATH | 수학 문제 해결 |
| GPQA | 대학원 수준 추론 |
| DROP | discrete reasoning RC |
| MGSM | multilingual GSM |
| HumanEval | Python 코드 생성 |
| SimpleQA | short-form factuality |
| BrowseComp | web browsing agent |
| HealthBench | 의료 LLM 평가 |

## 핵심 추상화: SamplerBase

`sampler/chat_completion_sampler.py`:

```python
class ChatCompletionSampler(SamplerBase):
    """Sample from OpenAI's chat completion API"""
```

생성자:
- `model` — 기본 `"gpt-3.5-turbo"`
- `system_message` — optional
- `temperature` — 기본 0.5
- `max_tokens` — 기본 1024

추상 인터페이스: `__call__(MessageList) -> SamplerResponse` (`response_text`, `metadata` 포함).

미리 준비된 system message 두 가지:
1. API default: `"You are a helpful assistant."`
2. ChatGPT 스타일: `"You are ChatGPT, a large language model trained by OpenAI, based on the GPT-4 architecture.\nKnowledge cutoff: 2023-12\nCurrent date: 2024-04-01"`

에러 핸들링: rate limit 시 exponential backoff, `BadRequestError` 별도 처리.

## CLI

```bash
# 모델 목록 확인
python -m simple-evals.simple_evals --list-models

# 실행
python -m simple-evals.simple_evals --model <model_name> --examples <num_examples>
```

## MMLU 구현 디테일

- 영어 dataset 은 OpenAI public URL 에서 CSV 로 fetch
- multilingual: 14개 언어 professionally translated MMLU test set 지원

## 유지보수 정책

> "the team is not accepting new evals."

bug fix, 새 모델 결과 추가만 받음. 즉 framework 라기보다 reference benchmark suite.

## 다른 harness 와의 포지셔닝

| 측면 | simple-evals | OpenAI Evals (구) | lm-eval-harness |
|---|---|---|---|
| 코드 양 | very small | medium | large |
| 평가 패턴 | zero-shot CoT | match/model-graded | log-likelihood + generate |
| 외부 contributor | 거부 | 한때 받았으나 닫힘 | 활발히 받음 |
| 모델 backend | sampler 단일 패턴 | CompletionFn 시스템 | 11+ 백엔드 |
| 사용처 | OpenAI launch 발표 | OpenAI 내부 | 업계 표준 |

simple-evals 는 OpenAI 가 GPT-5, GPT-5.5 launch 발표 시 인용하는 reference 라는 점에서 **모델 비교 신뢰도** 측면에서 가치가 있다. 다른 회사 (Z.ai 의 GLM-simple-evals fork 등) 도 같은 prompt 패턴을 사용하기 위해 fork.

## 파생

- `zai-org/glm-simple-evals` — GLM-4.5 시리즈 평가용 fork

## 출처

- README: https://github.com/openai/simple-evals
- Multilingual MMLU: https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md
- Sampler: https://github.com/openai/simple-evals/blob/main/sampler/chat_completion_sampler.py
- DeepWiki: https://deepwiki.com/openai/simple-evals/

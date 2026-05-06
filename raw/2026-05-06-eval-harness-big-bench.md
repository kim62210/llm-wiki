---
source: github + bigbench docs
url: https://github.com/google/BIG-bench
title: BIG-bench — JSON task vs programmatic task harness
fetched: 2026-05-06
status: pending_ingest
---

# BIG-bench (Beyond the Imitation Game) Harness

## 한 줄 요약

> "The Beyond the Imitation Game Benchmark (BIG-bench) is a _collaborative_ benchmark intended to probe large language models and extrapolate their future capabilities."
>
> — README

200+개의 collaborative task로 구성. **두 종류의 task spec**을 가진 사상 최초의 대규모 collaborative LLM benchmark — (1) `task.json`만으로 정의하는 단순 입출력 task와 (2) 코드로 정의하여 multi-round model 호출이 가능한 programmatic task. TMLR 2023 게재.

## Scale

- **200+ tasks** total
- **BIG-bench Lite (BBL)**: 24 diverse JSON tasks 서브셋 — "a canonical measure of model performance, while being far cheaper to evaluate"
- BIG-bench Hard (BBH): 별도 변형, 23 tasks 추가 채택

## 두 종류 task

### 1) JSON task

`task.json` 파일 하나로 정의. 두 하위 타입:

- **Text-to-text**: model output을 target output string과 비교
- **Multiple-choice**: model이 가능한 outputs들에 score 매김 (target_scores 이용)

#### task.json 필수 필드

```json
{
  "name": "...",          // plot legend 용 짧은 이름
  "description": "...",   // 비전문가용 plaintext 설명
  "keywords": ["..."],    // task 분류 keyword
  "metrics": ["..."],     // 평가에 사용할 metric 이름
  "canary": "...",        // 데이터 오염 방지용 GUID 문자열
  "examples": [
    {
      "input": "...",
      "target": "...",          // text-to-text 의 경우
      "target_scores": {...}    // multiple-choice 의 경우
    }
  ]
}
```

#### task.json 선택 필드

- `task_prefix` — 모든 예시 앞에 붙는 prefix
- `example_input_prefix` / `example_output_prefix`
- `choice_prefix` — multiple-choice 옵션 prefix
- `few_shot_example_separator`
- `stop_string` — generation 중지 토큰
- `output_regex` — generation 후 답 추출

#### 허용 metric

- **Text-to-text**: `bleu`, `bleurt`, `rouge`, `exact_str_match`
- **Multiple-choice**: `multiple_choice_grade`, `calibration_multiple_choice_brier_score`

(BLEURT는 BERT 기반 유사도 판정.)

### 2) Programmatic task

코드로 정의 (`task.py`). multi-round 가능 — 첫 응답으로 다음 prompt 구성.

#### Task 클래스 인터페이스

```python
class Task(task.Task):
    def get_task_details(self) -> task.TaskMetadata:
        return task.TaskMetadata(
            name=...,
            description=...,
            keywords=...,
            max_input_length_per_query=...,
            max_queries=...
        )

    def evaluate_model(self, model) -> list[task.ScoreData]:
        # model.generate_text(...) — 텍스트 생성
        # model.cond_log_prob(...) — log-prob 측정
        ...
```

#### ScoreData 구조

```python
task.ScoreData(
    score_dict={'metric_1': value_1, ...},
    preferred_score=...,
    number_of_shots=...,
    low_score=...,
    high_score=...,
    subtask_description=...
)
```

## 모델 인터페이스

BIG-bench가 model에 요구하는 추상 인터페이스 (programmatic 에서 호출):

- `model.generate_text(inputs, max_length, stop_string, output_regex)`
- `model.cond_log_prob(inputs, targets)` — input 조건 하 target log-prob

JSON task 의 평가는 위 두 메서드를 자동으로 호출하므로 별도 코드 불필요.

## 평가 파이프라인

```bash
# 평가 실행
python bigbench/evaluate_task.py --task my_task --model_name <model> --output_path results.json
```

> "evaluation results are written to a JSON file."

각 task 디렉토리: `bigbench/benchmark_tasks/<task_name>/`

## 다른 harness 와의 포지셔닝

- **Collaborative crowdsourced 이 핵심 차별점** — 450+ contributor 가 task 제출 (논문 저자 list 만으로도 unique)
- **JSON / programmatic 이중 구조** — programmatic 은 multi-round 평가 (추론 chain, agent-like 동작) 지원하지만 lm-eval-harness 의 generate_until 보다 일찍 등장한 패턴
- **LM 자체 평가 중심**: tool-use, sandbox, agent 평가 인프라는 없음
- **BBH 와 BBL** 로 인해 본체보다 서브셋이 더 자주 평가됨 (full benchmark 평가 비용이 큼)
- 사실상 **lm-evaluation-harness 가 BIG-bench task 들을 흡수** — `bbh` group 으로 통합되어 평가됨

## 출처

- README: https://github.com/google/BIG-bench
- Documentation: https://github.com/google/BIG-bench/blob/main/docs/doc.md
- Task list: https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/keywords_to_tasks.md
- Sample task.json: https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/simple_arithmetic_json_multiple_choice/task.json
- evaluate_task.py: https://github.com/google/BIG-bench/blob/main/bigbench/evaluate_task.py
- Paper: TMLR 2023 (Srivastava et al.)

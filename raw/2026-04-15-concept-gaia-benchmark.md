---
source: web
title: "GAIA Benchmark - General AI Assistants Evaluation"
url: "https://hal.cs.princeton.edu/gaia"
date: 2026-01-01
fetched: 2026-04-15
status: pending_ingest
---

## Overview

GAIA(General AI Assistants)는 범용 AI 어시스턴트의 실제적 자율 능력을 평가하는 벤치마크. 466개 태스크로 구성되며, 추론, 멀티모달 처리, 웹 브라우징, 도구 사용 등 기본 능력을 요구.

## Design

- 466개 질문, 3단계 난이도
- 모호하지 않은 정답
- 멀티스텝 추론 + 멀티모달 입력
- 웹 브라우징, 파일 파싱, 다문서 추론 체이닝

## Performance History

| 시점 | 모델/에이전트 | 점수 |
|------|-------------|------|
| 2023 (출시) | GPT-4 + plugins | ~15% |
| 2023 | 인간 | ~92% |
| 2026.04 | 최상위 에이전트 | ~75% |

## Why GAIA Matters

- AgentBench: 특정 환경에서의 멀티턴 추론 평가
- BFCL: 함수 호출 정확도 테스트
- GAIA: **범용 자율성** 평가 -- 실제 세계 적용성 강조
- 2026년 기준 독립적 평가 기준으로 GAIA와 CUB(Computer Use Benchmark)가 표준

## Key Characteristics

- 도구 사용 필수: 브라우저, 계산기, 파일 리더 등
- 다단계 추론: 단순 QA가 아닌 복합 추론
- 실제적(grounded): 실세계 정보 기반
- 검증 가능: 명확한 정답 존재

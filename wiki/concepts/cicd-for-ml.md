---
title: CI/CD for ML (머신러닝 CI/CD)
category: concepts
page_type: concept
tags: [concepts, concept, cicd, mlops, devops, model-deployment, dvc, cml, github-actions]
sources: [raw/2026-04-14-wiki-expand-scan-2.md]
created: 2026-04-14
updated: 2026-04-14
---
# CI/CD for ML (머신러닝 CI/CD)

머신러닝 파이프라인에 지속적 통합(CI)과 지속적 배포(CD) 원칙을 적용하여, 모델 학습-테스트-배포-모니터링을 자동화하는 실천. 전통적 소프트웨어 CI/CD가 코드 변경만 추적하는 것과 달리, ML CI/CD는 **코드, 데이터, 모델** 세 축의 변경을 모두 관리해야 한다.

## 왜 중요한가

ML 프로젝트의 실험에서 프로덕션까지의 간극은 악명이 높다. 구글의 "Hidden Technical Debt in Machine Learning Systems" 논문이 지적했듯, 실제 ML 시스템에서 모델 학습 코드는 전체의 극히 일부이고, 나머지는 데이터 수집/검증, 피처 추출, 서빙 인프라, 모니터링 등 "접착 코드(glue code)"가 차지한다. CI/CD 자동화 없이는 실험 재현이 불가능하고, 모델 성능 회귀를 탐지하지 못하며, 배포 주기가 수개월 단위로 늘어난다.

## 소프트웨어 CI/CD와의 차이

| 측면 | 소프트웨어 CI/CD | ML CI/CD |
|------|-----------------|----------|
| 추적 대상 | 코드 | 코드 + 데이터 + 모델 |
| 테스트 | 단위/통합/E2E | 데이터 검증 + 모델 성능 + 단위/통합 |
| 아티팩트 | 바이너리/컨테이너 | 모델 가중치 + 메타데이터 + 피처 파이프라인 |
| 트리거 | 코드 커밋 | 코드 커밋 + 데이터 변경 + 스케줄(재학습) |
| 롤백 | 이전 버전 배포 | 이전 모델 버전 + 피처 호환성 검증 |

## 핵심 도구

### DVC (Data Version Control)

Git으로 데이터와 모델을 버전 관리하는 오픈소스 도구. 실제 데이터는 원격 스토리지(S3, GCS, Azure Blob)에 저장하고, Git에는 메타정보(.dvc 파일)만 커밋한다. 별도의 버전 관리 데이터베이스나 특수 디렉토리 구조가 필요 없으며, 기존 Git 워크플로우에 자연스럽게 통합된다.

**핵심 기능:**
- `dvc push` / `dvc pull`: 원격 스토리지와 데이터 동기화
- `dvc repro`: 파이프라인 재현 (데이터 전처리 -> 학습 -> 평가 의존 그래프 실행)
- `dvc metrics diff`: 브랜치/커밋 간 성능 지표 비교
- `dvc plots`: 학습 곡선, 혼동 행렬 등 시각화 생성

### CML (Continuous Machine Learning)

ML 프로젝트에 특화된 CI/CD 오픈소스 라이브러리로, Iterative(DVC 개발사)가 개발했다. 기술 독립적(technology agnostic)이며 GitHub Actions와 GitLab CI 모두에서 동작한다.

**핵심 기능:**
- PR에 자동 실험 보고서 생성 (메트릭 비교, 시각화 포함)
- `dvc metrics diff`와 `dvc plots`를 CI 파이프라인에 통합
- 클라우드 GPU 러너 자동 프로비저닝 (AWS, GCP, Azure)
- 팀이 PR 코멘트로 실험 결과를 리뷰하고 데이터 기반 의사결정

### GitHub Actions

MLOps CI/CD에서 가장 널리 사용되는 CI 도구. 퍼블릭 레포에서 무료이며, AWS/Azure/GCP와 마켓플레이스 액션으로 네이티브 통합된다.

## 전형적 파이프라인 구조

### CI: 자동화된 테스트와 검증

```
코드 푸시 / 데이터 변경
    |
    v
[데이터 검증] -- 스키마 일관성, 분포 이동(drift), 이상치 탐지
    |
    v
[파이프라인 재현] -- dvc repro: 전처리 -> 피처 추출 -> 학습 -> 평가
    |
    v
[모델 테스트]
    |- 성능 회귀 테스트 (정확도/F1 등 임계값)
    |- 편향/공정성 검사
    |- 추론 지연 시간 벤치마크
    |- 단위 테스트 (전처리 함수, 피처 엔지니어링)
    |
    v
[PR 보고서] -- CML로 메트릭/시각화 자동 코멘트
```

### CD: 자동화된 배포와 모니터링

```
PR 머지 / 릴리스 태그
    |
    v
[모델 레지스트리] -- MLflow, DVC, Weights & Biases에 모델 등록
    |
    v
[스테이징 배포] -- 카나리/섀도우 배포로 프로덕션 트래픽 일부 라우팅
    |
    v
[자동화된 검증] -- A/B 테스트, 성능 지표 임계값 확인
    |
    v
[프로덕션 배포] -- 쿠버네티스, SageMaker, Vertex AI 등
    |
    v
[모니터링] -- 데이터 드리프트, 모델 성능 저하, 인프라 건강성
```

## ML 테스트 전략

전통적 소프트웨어 테스트와 ML 테스트는 근본적으로 다르다. ML 시스템에서는 코드가 정확하더라도 데이터나 모델이 퇴화할 수 있다.

| 테스트 유형 | 대상 | 예시 |
|------------|------|------|
| 데이터 검증 | 입력 데이터 품질 | 스키마 검증, null 비율, 분포 이동 탐지 |
| 모델 성능 | 예측 품질 | 정확도/F1/AUC 임계값, 슬라이스별 성능 |
| 편향/공정성 | 모델 공정성 | 인구통계 그룹별 성능 격차 |
| 인프라 | 서빙 안정성 | 지연 시간, 처리량, 메모리 사용량 |
| 피처 | 피처 파이프라인 | 피처 값 범위, 결측치, 시간 일관성 |

## CT (Continuous Training)

CI/CD 너머의 ML 고유 개념. 프로덕션 데이터의 드리프트(drift)를 감지하면 자동으로 모델을 재학습하는 루프이다. Evidently AI, Whylabs 등의 모니터링 도구가 데이터 드리프트를 탐지하고, 임계값 초과 시 재학습 파이프라인을 트리거한다.

## 실전 워크플로우 예시

DVC + CML + GitHub Actions를 조합한 전형적 구성:

1. **데이터 변경**: 새 학습 데이터를 `dvc push`로 원격 스토리지에 업로드
2. **PR 생성**: .dvc 파일 변경이 포함된 브랜치에서 PR 오픈
3. **CI 자동 실행**: GitHub Actions가 `dvc pull`로 데이터를 가져오고 `dvc repro`로 파이프라인 재현
4. **보고서 생성**: CML이 `dvc metrics diff`로 main 브랜치 대비 성능 차이를 계산하고, ROC 곡선/정밀도-재현율 그래프와 함께 PR 코멘트로 게시
5. **팀 리뷰**: PR 코멘트에서 메트릭을 확인하고 머지 여부 결정
6. **자동 배포**: 머지 시 CD 파이프라인이 모델을 레지스트리에 등록하고 서빙 환경에 배포

## 대표 레퍼런스

- [CI/CD for Machine Learning (DVC)](https://dvc.org/doc/use-cases/ci-cd-for-machine-learning)
- [Continuous Integration with CML and GitHub Actions (MLOps Guide)](https://mlops-guide.github.io/CICD/cml_testing/)
- [CI/CD for Machine Learning - MLOps Guide](https://mlops-guide.github.io/MLOps/CICDML/)

## 관련 문서

- [[ai-observability-patterns|AI Observability Patterns]]
- [[agentic-ai-production|Agentic AI Production]]

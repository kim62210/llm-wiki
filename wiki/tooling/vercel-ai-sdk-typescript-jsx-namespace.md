---
title: Vercel AI SDK TypeScript JSX Namespace Troubleshooting
aliases: ["AI SDK Cannot find namespace JSX", "TypeScript error Cannot find namespace JSX", "docs/troubleshooting/typescript-cannot-find-namespace-jsx"]
category: tooling
page_type: project-internal
project: Vercel AI SDK
tags: [vercel-ai-sdk, troubleshooting, typescript, jsx, react-types, hono]
sources: [raw/2026-04-13-vercel-ai-sdk-typescript-jsx-namespace.md]
created: 2026-04-13
updated: 2026-04-13
---

# Vercel AI SDK TypeScript JSX Namespace Troubleshooting

이 문서는 [[vercel-ai-sdk|Vercel AI SDK 6]] 공식 troubleshooting 페이지 중 `TypeScript error "Cannot find namespace 'JSX'"` 항목을 위키화한 project-internal 노드다. 원래 빈 placeholder는 AI SDK 공식 문서 navigation의 `/docs/troubleshooting/typescript-cannot-find-namespace-jsx` 링크에서 생성된 것으로 보인다. 제목만 남겨 두면 “React를 쓰지 않는 서버 프로젝트에서 왜 JSX namespace 오류가 나는가”라는 실제 운영 질문이 사라지므로, 삭제가 아니라 제품별 troubleshooting 노드로 승격했다.

## 문제 상황

공식 문서가 다루는 증상은 TypeScript `TS2503: Cannot find namespace 'JSX'` 오류다. 예시 맥락은 React 애플리케이션이 아니라 Hono server 같은 non-React 프로젝트에서 AI SDK를 사용하는 경우다. 이런 프로젝트는 UI 렌더링을 하지 않으므로 개발자는 JSX namespace가 필요 없다고 기대한다. 그런데 AI SDK를 설치하거나 타입을 통과시키는 과정에서 TypeScript가 `JSX` namespace를 찾으려고 하면서 오류가 발생한다.

이 문제는 “프로젝트가 React를 잘못 import했다”는 단순한 실수로만 보면 안 된다. 공식 troubleshooting의 핵심 배경은 AI SDK 쪽 dependency가 `@types/react`와 연결되어 있고, 그 패키지가 `JSX` namespace를 정의한다는 점이다. 즉 오류는 애플리케이션 코드가 JSX를 직접 쓰지 않더라도 타입 dependency graph에서 발생할 수 있다.

## 공식 해결책

공식 문서가 제시한 해결책은 간단하다. `@types/react`를 dependency로 설치한다.

```bash
npm install @types/react
```

이 명령은 non-React 서버 코드에 React runtime을 추가하는 것과 다르다. 여기서 필요한 것은 runtime component가 아니라 TypeScript가 참조할 타입 namespace다. 따라서 이 해결책은 “서버 프로젝트에 React를 도입한다”가 아니라 “AI SDK의 현재 타입 dependency가 요구하는 ambient type을 명시적으로 제공한다”로 이해하는 편이 정확하다.

```mermaid
flowchart TD
    App[Non-React 서버 프로젝트] --> SDK[Vercel AI SDK]
    SDK --> Types[타입 의존성 그래프]
    Types --> JSX[JSX namespace 필요]
    JSX --> Error[TS2503 오류]
    Error --> Fix[@types/react 설치]
```

이 다이어그램은 runtime 경로가 아니라 type-check 경로를 보여준다. 실제 요청 처리나 모델 호출이 React로 바뀌는 것이 아니라, TypeScript compile 단계가 필요한 namespace 정의를 찾게 되는 구조다.

## 왜 project-internal인가

이 문서는 일반 TypeScript 개념 페이지로 만들지 않았다. `JSX namespace` 자체는 TypeScript/React 생태계의 일반 개념이지만, 여기서 중요한 것은 Vercel AI SDK v6 문서가 설명한 특정 의존성 상태와 공식 workaround다. 또한 공식 페이지는 이 dependency가 AI SDK의 다음 major version에서 제거될 예정이라고 설명한다. 이 말은 시간에 따라 유효성이 바뀔 수 있는 제품별 상태라는 뜻이다.

따라서 `page_type: project-internal`, `project: Vercel AI SDK`가 더 안전하다. 일반 concept 페이지로 승격하면 “모든 non-React TypeScript 서버 프로젝트는 `@types/react`를 설치해야 한다”는 잘못된 일반화를 만들 수 있다. 반대로 삭제하면 AI SDK docs corpus에서 실제 troubleshooting edge case가 빠진다. 현재 위키에서는 제품별 troubleshooting note로 남겨 두고, 향후 AI SDK major version이 바뀌면 갱신 대상으로 표시하는 것이 맞다.

## 실무 판별 절차

| 질문 | 해석 |
|---|---|
| 오류 코드가 TS2503인가? | 이 노드의 대상일 가능성이 높다 |
| 메시지가 `Cannot find namespace 'JSX'`인가? | 공식 troubleshooting과 일치한다 |
| 프로젝트가 React UI가 아닌 Hono 등 서버 프로젝트인가? | 공식 예시와 일치한다 |
| AI SDK를 dependency로 사용 중인가? | 제품별 workaround 적용 후보 |
| React runtime이 필요한가? | 이 문서의 해결책은 runtime이 아니라 타입 설치다 |
| AI SDK major version이 바뀌었는가? | 공식 문서 재확인 필요 |

이 절차는 blind install을 막기 위한 것이다. 오류 원인이 AI SDK가 아니라 다른 JSX transform 설정, `jsxImportSource`, tsconfig 문제라면 이 문서의 해결책만으로 충분하지 않을 수 있다. 그러나 공식 AI SDK troubleshooting과 동일한 조건이라면 `@types/react` 설치가 가장 좁은 조치다.

## 운영 메모

이 항목은 [[vercel-ai-sdk-core-overview|AI SDK Core Overview]]보다 더 낮은 수준의 troubleshooting 노드다. 일반 사용자는 처음부터 읽을 필요가 없지만, 서버 전용 프로젝트에서 AI SDK를 붙이다가 TypeScript가 실패하면 바로 연결되어야 한다. 따라서 [[vercel-ai-sdk|Vercel AI SDK 6]] 허브와 index에서 접근 가능하게 두는 것이 좋다.

또한 이 문서는 “정의되지 않은 위키항목”을 처리할 때 삭제와 ingest 사이의 판단 기준을 보여준다. 비어 있던 파일이 원문 navigation의 실재하는 official docs URL에 대응하면, 무조건 불필요한 문서로 삭제하지 않는다. 먼저 공식 문서의 현재 내용을 확인하고, reusable concept인지 product-specific detail인지 판정한 뒤 적절한 page_type으로 위키화한다.

## 향후 재검증 포인트

공식 문서는 이 dependency가 다음 major version에서 제거될 예정이라고 설명한다. 그러므로 AI SDK 7 또는 그 이후 버전에서 동일 오류가 계속 발생하는지는 재검증해야 한다. 제거가 완료되면 이 페이지는 “v6 시점 troubleshooting”으로 시간 범위를 명확히 하거나, 더 이상 필요하지 않은 과거 호환성 노트로 축소할 수 있다.


## 운영 해석 보강

이 troubleshooting 항목의 핵심은 React 사용 여부와 TypeScript 타입 의존성 여부를 분리해서 보는 것이다. 서버 프로젝트에서 React component를 렌더링하지 않는다는 사실은 runtime 관점에서는 맞지만, TypeScript compiler가 참조하는 declaration graph 관점에서는 충분한 설명이 아니다. 어떤 library가 `JSX` namespace를 포함하는 타입을 노출하면, application code가 JSX 문법을 쓰지 않아도 compile 단계에서 namespace 정의가 필요할 수 있다.

따라서 이 해결책은 불필요한 UI dependency를 runtime에 끌어들이는 조치로 해석하면 안 된다. 공식 문서의 안내는 타입 패키지를 설치해 compiler가 요구하는 namespace를 찾게 만드는 최소 workaround다. package policy가 엄격한 저장소에서는 `dependencies`와 `devDependencies` 중 어디에 둘지, 배포 빌드에서 type-check를 언제 수행하는지, monorepo package boundary에서 해당 타입이 전파되는지까지 함께 확인해야 한다. Hono 같은 서버 환경에서는 runtime bundle에 React가 포함되는지보다, TypeScript project reference와 lockfile에 어떤 타입 패키지가 들어가는지가 더 직접적인 검토 대상이다.

또 하나의 주의점은 시간 범위다. 공식 문서는 이 dependency가 다음 major version에서 제거될 예정이라고 적고 있으므로, 이 문서는 2026-04-13에 확인한 AI SDK v6 기준 troubleshooting으로 읽어야 한다. 향후 AI SDK v7 이상에서 같은 오류가 발생한다면 원인이 달라졌을 수 있다. 그때는 이 노드의 해결책을 그대로 반복하기보다 공식 troubleshooting 페이지와 package release note를 다시 확인하고, 이 문서를 “v6 호환성 노트”로 축소할지 결정해야 한다.


## triage 예시

예를 들어 백엔드 전용 패키지에서 AI SDK를 사용해 provider 호출만 수행하고, UI는 다른 애플리케이션이 담당한다고 하자. 이때 TypeScript가 `JSX` namespace를 찾지 못하면 개발자는 tsconfig의 `jsx` 옵션을 먼저 의심할 수 있다. 하지만 이 troubleshooting 노드의 조건에서는 문제를 더 좁게 본다. 애플리케이션이 JSX를 쓰는지가 아니라, AI SDK가 노출한 타입이 `@types/react`에 정의된 namespace를 참조하는지가 핵심이다. 그래서 해결 순서는 “tsconfig를 크게 바꾼다”가 아니라 “공식 문서가 요구한 type package를 설치하고, lockfile과 type-check 결과를 확인한다”가 된다.

이 판단은 불필요한 설정 변경을 막는다. `skipLibCheck`를 켜서 오류를 숨기거나, 전역 declaration을 임시로 만들어 `JSX` namespace를 흉내 내면 당장은 빌드가 지나갈 수 있다. 그러나 그런 우회는 이후 SDK 업데이트나 다른 패키지 타입과 충돌할 가능성이 있다. 공식 troubleshooting이 제공하는 좁은 workaround가 존재할 때는 먼저 그 경로를 적용하고, 실패할 때만 더 넓은 TypeScript 설정 문제로 확장하는 편이 안전하다.

## 관련 문서

- [[vercel-ai-sdk|Vercel AI SDK 6]] — 상위 제품 허브
- [[vercel-ai-sdk-core-overview|AI SDK Core Overview]] — Core primitive 맥락
- [[vercel-ai-sdk-agents-overview|Vercel AI SDK Agents Overview]] — AI SDK의 agent 레이어
- [[vercel-ai-sdk-extract-json-middleware|Vercel AI SDK extractJsonMiddleware]] — 같은 AI SDK docs reference에서 승격한 API 노드

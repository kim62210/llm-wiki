---
title: OMC Delegation Categories
aliases: [OMC Delegation Categories]
category: concepts
page_type: project-internal
project: oh-my-claudecode
tags: [omc, delegation, category, temperature, thinking-budget]
sources: [raw/2026-04-09-omc-FEATURES.md]
created: 2026-04-09
updated: 2026-04-13
---
# OMC Delegation Categories

> 태스크 프롬프트를 자동 분류해 모델 티어 + temperature + thinking budget을 한 번에 결정하는 시스템.

## 핵심 아이디어

에이전트별 기본 모델 매핑([[omc-model-routing]])은 **역할 기준**이다. 하지만 같은 executor 에이전트라도 단순 텍스트 수정 vs 복잡한 race condition 디버깅은 다른 처리가 필요하다. Delegation Categories는 **태스크 내용**을 보고 실행 파라미터를 동적으로 결정한다.

## 7개 카테고리

| Category | Tier | Temp | Thinking | 사용 용도 |
|---|---|---|---|---|
| `visual-engineering` | HIGH | 0.7 | high | UI/UX, frontend, 디자인 시스템 |
| `ultrabrain` | HIGH | 0.3 | max | 복잡한 추론, 아키텍처, 디버깅 |
| `artistry` | MEDIUM | 0.9 | medium | 창의적 해결, 브레인스토밍 |
| `quick` | LOW | 0.1 | low | 단순 lookup, 기본 동작 |
| `writing` | MEDIUM | 0.5 | medium | 문서, 기술 글쓰기 |
| `unspecified-low` | LOW | 0.1 | low | 단순 태스크의 기본값 |
| `unspecified-high` | HIGH | 0.5 | high | 복잡 태스크의 기본값 |

## 파라미터 해석

- **Tier**: LOW=haiku, MEDIUM=sonnet, HIGH=opus ([[omc-model-routing]])
- **Temperature**: 낮을수록 결정론적(0.1), 높을수록 창의적(0.9)
  - `ultrabrain` 0.3: 논리적 추론은 변덕 없이 정확하게
  - `artistry` 0.9: 창의적 해법은 확률 분포 넓게
- **Thinking budget**: Extended Thinking 할당
  - `low | medium | high | max`
  - `ultrabrain` max: 가장 많은 extended thinking 토큰

## 동작 흐름

```
1. User request → task prompt
2. detectCategoryFromPrompt(taskPrompt) → category (또는 null)
3. resolveCategory(category) → { tier, temperature, thinkingBudget, ... }
4. enhancePromptWithCategory(prompt, category)
   → 카테고리별 guidance append
5. Task 툴로 자식 에이전트 스폰 시 결정된 모델·파라미터 사용
```

## 코어 API (TypeScript)

```typescript
// 카테고리 설정 해석
resolveCategory(category: DelegationCategory): ResolvedCategory

// 프롬프트 자동 감지
detectCategoryFromPrompt(taskPrompt: string): DelegationCategory | null

// 컨텍스트 포함 조회
getCategoryForTask(context: CategoryContext): ResolvedCategory

// 프롬프트 강화 (카테고리 지침 추가)
enhancePromptWithCategory(taskPrompt: string, category: DelegationCategory): string

// 개별 접근자
getCategoryTier(category): ComplexityTier
getCategoryTemperature(category): number
getCategoryThinkingBudget(category): ThinkingBudget
getCategoryThinkingBudgetTokens(category): number
getCategoryPromptAppend(category): string
```

## 타입 정의

```typescript
type DelegationCategory =
  | 'visual-engineering'
  | 'ultrabrain'
  | 'artistry'
  | 'quick'
  | 'writing'
  | 'unspecified-low'
  | 'unspecified-high';

type ThinkingBudget = 'low' | 'medium' | 'high' | 'max';

interface ResolvedCategory {
  category: DelegationCategory;
  tier: ComplexityTier;
  temperature: number;
  thinkingBudget: ThinkingBudget;
  description: string;
  promptAppend?: string;
}

interface CategoryContext {
  taskPrompt: string;
  [[coding-agent|agent]]Type?: string;
  explicitCategory?: DelegationCategory;
  explicitTier?: ComplexityTier;
}
```

## 사용 예시

```typescript
import {
  getCategoryForTask,
  enhancePromptWithCategory
} from '@/features/delegation-categories';

const userRequest = 'Debug the race condition in payment processor';

// 자동 감지
const resolved = getCategoryForTask({ taskPrompt: userRequest });
// resolved.category === 'ultrabrain'
// resolved.temperature === 0.3
// resolved.thinkingBudget === 'max'

// 프롬프트에 카테고리 가이드 주입
const enhancedPrompt = enhancePromptWithCategory(userRequest, resolved.category);
// "Debug the race condition in payment processor\n\nThink deeply and systematically.
//  Consider all edge cases..."
```

## 우선순위 규칙

`getCategoryForTask`는 다음 우선순위로 결정:

1. `explicitCategory` 지정 시 → 그 값 사용
2. `explicitTier` 지정 시 → 매칭되는 `unspecified-*` 사용
3. `taskPrompt`에서 자동 감지 → 성공 시 그 값 사용
4. `agentType`에서 추론 → 에이전트 기본 매핑에 의존
5. 최종 fallback → `unspecified-high`

## ultrabrain vs ultrathink

두 개념이 비슷해 보이지만 다름:

- **ultrabrain** (delegation category): 복잡한 추론 태스크를 opus + temperature 0.3 + max thinking budget으로 처리하도록 **자동 분류**
- **ultrathink** (magic keyword): 사용자가 명시적으로 "think hard"를 요청할 때 extended reasoning 모드를 켜는 **명시 트리거**

일반적으로 ultrabrain은 OMC가 알아서 결정하고, ultrathink는 사용자가 "이거 깊이 생각해봐"라고 말할 때 수동 부스트다.

## 실무 고려사항

- **자동 감지의 한계**: 프롬프트 키워드로 추론하므로 애매한 태스크는 오분류 가능 → 중요한 태스크는 `explicitCategory` 지정
- **비용**: `ultrabrain`은 opus + max thinking → 토큰 비용 크게 증가. 남발 금지
- **temperature 영향**: 창의성이 필요 없는 코드 태스크에 높은 temp를 쓰면 환각 확률 증가

## 관련 문서

- [[oh-my-claudecode]]
- [[omc-model-routing]]
- [[omc-magic-keyword]]
- [[multi-agent-orchestration]]

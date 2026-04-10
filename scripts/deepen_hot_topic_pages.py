from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse
import re


ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    meta = {}
    for line in text[4:end].splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            meta[k] = v
    return meta, text[end + 5 :]


def format_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for key in ["title", "aliases", "category", "page_type", "project", "tags", "sources", "created", "updated"]:
        value = meta.get(key)
        if value is None:
            continue
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(value)}]")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def parse_sources(raw: str) -> list[str]:
    if raw.startswith("[") and raw.endswith("]"):
        return [x.strip() for x in raw[1:-1].split(",") if x.strip()]
    return []


def find_lead(body: str) -> str:
    lines = body.splitlines()
    seen_h1 = False
    for line in lines:
        s = line.strip()
        if s.startswith("# "):
            seen_h1 = True
            continue
        if not seen_h1 or not s:
            continue
        if s.startswith("## "):
            break
        return s
    return ""


def count_domains(source_paths: list[str]):
    domains = []
    for src in source_paths:
        if not src.startswith("raw/hot-topics-sources/2026-04-10/") or "/topics/" in src:
            continue
        path = ROOT / src
        if not path.exists():
            continue
        meta, _ = parse_frontmatter(path)
        url = meta.get("final_url") or meta.get("source_url") or ""
        if url:
            domains.append(urlparse(url).netloc.replace("www.", ""))
    counts = {}
    for domain in domains:
        counts[domain] = counts.get(domain, 0) + 1
    return counts


def domain_summary(counts: dict[str, int]) -> str:
    items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return ", ".join(f"{domain}×{count}" for domain, count in items[:5]) if items else "source 다양성 정보 없음"


def source_character(counts: dict[str, int]) -> str:
    keys = set(counts)
    research = any(k in keys for k in ["arxiv.org", "aclanthology.org", "openreview.net", "openreview.net/forum"])
    docs = any(k.endswith("anthropic.com") or k.endswith("openai.com") or "docs" in k or k == "help.openai.com" for k in keys)
    repos = "github.com" in keys
    if research and docs and repos:
        return "연구·공식문서·구현체가 모두 섞여 있어서 개념과 운영을 함께 추적하기 좋다."
    if research and docs:
        return "연구 논문과 공식 문서가 함께 있어 원리와 제품화 흐름을 같이 읽을 수 있다."
    if research and repos:
        return "연구 신호와 구현체가 같이 보여서 실험 결과와 적용 방법을 연결해 보기 좋다."
    if docs and repos:
        return "공식 문서와 구현 저장소가 같이 있어 실제 도입 관점의 정보가 강한 편이다."
    if research:
        return "연구 논문 비중이 높아 메커니즘·평가·한계 쪽 정보가 중심이다."
    if docs:
        return "공식 문서/엔지니어링 글 비중이 높아 운영·제품 맥락이 강하다."
    if repos:
        return "구현 저장소 비중이 높아 실제 사용·통합 관점이 두드러진다."
    return "source 구성이 비교적 고르게 분포해 허브형 개요 문서로 읽기 좋다."


CATEGORY_GUIDANCE = {
    "agents": "실무에서는 장기 실행, 상태 관리, 실패 복구, 평가 루프를 함께 설계해야 이 토픽이 효과를 낸다. 즉 개별 아이디어보다 에이전트 시스템 전체의 제약 속에서 읽는 것이 중요하다.",
    "inference": "실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.",
    "rag": "실무에서는 검색 품질만이 아니라 컨텍스트 예산, chunking, 메모리 구조, 재랭킹, 운영 비용까지 함께 고려해야 한다. 그래서 이 토픽은 검색 정확도보다 '어떤 상황에서 어떤 구조를 쓰는가' 관점으로 읽는 것이 유용하다.",
    "tooling": "도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.",
    "training": "학습/후학습 기법은 이름보다 목적 함수와 검증 방식이 중요하다. 보상 신호를 어떻게 만들고 어떤 실패 모드를 줄이는지, 그리고 추론 성능과 운영 비용이 어떻게 바뀌는지를 함께 봐야 실무 의미가 생긴다.",
    "concepts": "개념 페이지는 용어 정의에서 끝나지 않고, 어떤 시스템 설계 문제를 해결하려고 등장했는지와 어디까지가 적용 범위인지까지 함께 봐야 한다.",
}


def remove_section(body: str, header: str) -> str:
    pattern = rf"\n## {re.escape(header)}.*?(?=\n## |\Z)"
    return re.sub(pattern, "", body, flags=re.S)


def build_deepening(meta: dict, body: str, counts: dict[str, int]) -> str:
    title = meta["title"]
    category = meta["category"]
    page_type = meta["page_type"]
    lead = find_lead(body)
    count = sum(counts.values())
    summary = domain_summary(counts)
    character = source_character(counts)
    guidance = CATEGORY_GUIDANCE.get(category, "이 페이지는 개념보다 적용 맥락과 경계 조건을 같이 읽을수록 가치가 커진다.")

    if page_type == "entity":
        first = f"{title}는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 {lead}이며, 직접 수집한 source {count}건은 {summary}처럼 여러 채널에 걸쳐 분포한다."
    elif page_type == "project-internal":
        first = f"{title}는 일반 개념이라기보다 특정 프로젝트 내부 기능을 설명하는 문서다. 현재 페이지의 핵심 정의는 {lead}이며, source {count}건이 이 기능의 설계 배경과 운영 맥락을 보강한다."
    elif page_type == "summary":
        first = f"{title}는 개별 source를 빠르게 따라잡기 위한 요약 허브다. 현재 본문은 {lead}를 중심으로 구성되어 있고, 수집된 근거 {count}건이 요약의 배경을 받쳐준다."
    elif page_type == "case-study":
        first = f"{title}는 특정 시점의 사례를 묶어 보는 문서다. 출발점은 {lead}이며, source {count}건이 이 사례가 실제로 어떤 맥락에서 중요해졌는지를 보여준다."
    else:
        first = f"{title}는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 {lead}이며, 직접 수집한 source {count}건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다."

    section = "\n".join(
        [
            "## 핵심 포인트",
            "",
            first,
            "",
            "## source로 보면",
            "",
            f"수집된 source는 {summary}로 분포한다. {character}",
            "",
            "## 실무 관점",
            "",
            guidance,
            "",
        ]
    )
    return section


def main():
    changed = 0
    for page in sorted((ROOT / "wiki").rglob("*.md")):
        meta, body = parse_frontmatter(page)
        if meta.get("sources", "").find("raw/2026-04-10-hot-ai-topics-100.md") == -1:
            continue
        if meta.get("page_type") == "summary" and meta.get("category") == "applications":
            continue
        counts = count_domains(parse_sources(meta.get("sources", "")))
        if sum(counts.values()) == 0:
            continue
        # already rich legacy pages don't need another generic layer
        if len(body) > 7000:
            continue
        for header in ["핵심 포인트", "source로 보면", "실무 관점"]:
            body = remove_section(body, header)
        insert = build_deepening(meta, body, counts)
        if "## source 기반 참고" in body:
            body = body.replace("## source 기반 참고", insert + "\n## source 기반 참고", 1)
        elif "## 관련 문서" in body:
            body = body.replace("## 관련 문서", insert + "\n## 관련 문서", 1)
        else:
            body = body.rstrip() + "\n\n" + insert
        page.write_text(format_frontmatter(meta) + "\n" + body.lstrip())
        changed += 1
    print(f"deepened={changed}")


if __name__ == "__main__":
    main()

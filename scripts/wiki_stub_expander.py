from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = ROOT / "wiki"
AUDIT_PATH = ROOT / ".omx" / "empty-doc-audit.json"
THRESHOLD = 250
TODAY = "2026-04-10"

BOILERPLATE_HEADINGS = {
    "skip to main content",
    "navigation",
    "search",
    "core concepts",
    "about mcp",
    "on this page",
    "access paper:",
    "submission history",
    "references & citations",
    "bibliographic and citation tools",
    "bookmark",
    "message types",
    "tool execution",
    "participants",
    "layers",
    "scope",
    "quick links",
    "get started",
    "examples",
    "developer tools",
}


def split_list(value: str) -> list[str]:
    value = value.strip()
    if not value.startswith("[") or not value.endswith("]"):
        return []
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [item.strip() for item in inner.split(",") if item.strip()]


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    meta_lines = text[4:end].splitlines()
    meta: dict[str, object] = {}
    for line in meta_lines:
        if ": " not in line:
            continue
        key, value = line.split(": ", 1)
        if value.startswith("[") and value.endswith("]"):
            meta[key] = split_list(value)
        else:
            meta[key] = value
    body = text[end + 5 :]
    return meta, body


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


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def parse_raw_source(path_str: str) -> dict:
    path = ROOT / path_str
    if not path.exists():
        return {
            "path": path_str,
            "title": Path(path_str).stem,
            "url": "",
            "abstract": "",
            "headings": [],
        }

    meta, body = parse_frontmatter(path)
    raw_text = body
    if "Markdown Content:" in raw_text:
        raw_text = raw_text.split("Markdown Content:", 1)[1]
    elif "## 원문 추출" in raw_text:
        raw_text = raw_text.split("## 원문 추출", 1)[1]
    elif "## 추출 본문" in raw_text:
        raw_text = raw_text.split("## 추출 본문", 1)[1]
    raw_text = raw_text.strip()

    abstract = ""
    for pattern in [
        r">\s*Abstract:(.*?)(?=\n\s*(?:Subjects:|Comments:|Cite as:|Submission history|##|$))",
        r"Abstract:(.*?)(?=\n\s*(?:Subjects:|Comments:|Cite as:|Submission history|##|$))",
    ]:
        match = re.search(pattern, raw_text, re.S)
        if match:
            abstract = re.sub(r"\s+", " ", match.group(1)).strip()
            break

    headings: list[str] = []
    for line in raw_text.splitlines():
        stripped = line.strip()
        if not re.match(r"^#{1,6}\s+", stripped):
            continue
        heading = re.sub(r"^#{1,6}\s+", "", stripped).strip()
        heading = re.sub(r"\[.*?\]\(.*?\)", "", heading).strip()
        heading = re.sub(r"\s+", " ", heading)
        low = heading.lower()
        if not heading or low in BOILERPLATE_HEADINGS:
            continue
        if heading.startswith("[") and "]" in heading:
            continue
        if len(heading) > 70:
            continue
        if heading not in headings:
            headings.append(heading)
        if len(headings) >= 6:
            break

    return {
        "path": path_str,
        "title": str(meta.get("title") or Path(path_str).stem),
        "url": str(meta.get("final_url") or meta.get("source_url") or ""),
        "abstract": abstract,
        "headings": headings,
    }


def compact_title(title: str) -> str:
    return title.replace("[", "").replace("]", "").strip()


def infer_focus(meta: dict, page_path: str) -> str:
    page_type = str(meta.get("page_type", ""))
    title = str(meta.get("title", Path(page_path).stem))
    tokens = f"{title} {meta.get('category', '')} {page_type}".lower()

    if page_type == "paper":
        if any(k in tokens for k in ["context", "compression", "long-context", "fold", "kv", "memory"]):
            return "긴 컨텍스트/메모리 병목을 어떻게 줄이는가"
        if any(k in tokens for k in ["agent", "research", "planning", "tree", "loop"]):
            return "장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가"
        if any(k in tokens for k in ["rl", "reward", "reason", "swe", "code"]):
            return "에이전트 학습/검증 신호를 어떻게 강화하는가"
        return "장기 과제에서 모델/에이전트 성능을 어떻게 끌어올리는가"

    if page_type == "entity":
        return "도구 자체보다 운영 경계와 도입 전제를 어떻게 읽어야 하는가"
    if page_type == "case-study":
        return "사례를 재현 가능한 운영 교훈으로 어떻게 바꿀 것인가"
    if page_type == "concept":
        return "이 개념이 실제 병목과 설계 판단에 어떻게 연결되는가"
    return "원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가"


def generic_axes(meta: dict) -> list[str]:
    page_type = str(meta.get("page_type", "summary"))
    if page_type == "entity":
        return ["이 대상이 맡는 역할", "연동 방식과 권한 경계", "도입 시 운영 제약"]
    if page_type == "concept":
        return ["문제가 드러나는 조건", "완화 전략", "인접 개념과의 차이"]
    if page_type == "case-study":
        return ["문제 배경", "개입 방식", "재사용 가능한 교훈"]
    return ["입문 경로", "핵심 구조", "다음에 읽을 세부 문서"]


def section_content_with_heading(section: str) -> str:
    return section.split("\n\n", 1)[1].strip()


def source_scope_section(meta: dict, source_infos: list[dict]) -> str:
    title = str(meta.get("title", "이 문서"))
    page_type = str(meta.get("page_type", "summary"))
    headings: list[str] = []
    for info in source_infos:
        headings.extend(info["headings"])
    headings = list(dict.fromkeys(headings))[:5]

    if headings:
        seq = " → ".join(f"`{h}`" for h in headings)
        if page_type == "summary":
            intro = f"원문은 대체로 {seq} 순서로 전개된다. 따라서 `{title}` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다."
        elif page_type == "entity":
            intro = f"관련 source를 묶어 보면 `{title}`는 {seq} 축으로 설명된다. 즉 기능 목록 하나보다 **정체성·연동 방식·운영 경계**를 같이 봐야 이 항목의 의미가 선명해진다."
        elif page_type == "case-study":
            intro = f"원문은 {seq} 흐름으로 사례를 쌓아 간다. 그래서 이 페이지는 결과 수치만 보는 대신 **문제 배경 → 개입 방식 → 얻은 교훈**의 순서로 읽는 것이 적절하다."
        else:
            intro = f"수집된 source는 {seq} 흐름을 반복한다. 즉 `{title}`는 단일 정의보다 **구조·실행 순서·제약 조건**을 함께 보아야 이해되는 문서다."
    else:
        intro = f"참조 source는 `{title}`를 하나의 정의로 닫지 않고, 주변 설계 맥락과 읽기 순서를 함께 제공한다. 그래서 짧은 소개문만으로 끝내기보다 **구조와 적용 포인트**를 같이 정리해야 위키 문서로서 가치가 생긴다."

    axes = generic_axes(meta)
    lines = []
    if headings:
        lines.append(f"- 따라가야 할 순서: {', '.join(headings)}")
    lines.append(f"- 위키에 남겨야 할 축: {', '.join(axes)}")
    return "## 원문이 다루는 흐름\n\n" + intro + "\n\n" + "\n".join(lines) + "\n"


def reading_points_section(meta: dict, page_path: str, source_infos: list[dict]) -> str:
    page_type = str(meta.get("page_type", "summary"))
    title = str(meta.get("title", Path(page_path).stem))
    focus = infer_focus(meta, page_path)
    lines = [
        f"- 이 문서는 **{focus}**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.",
        "- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.",
    ]
    if page_type == "entity":
        lines.append(f"- `{title}` 같은 entity 페이지는 기능 카탈로그가 아니라 허브이므로, 주변 summary/paper 문서와 연결해서 읽어야 도입 판단 기준이 생긴다.")
    elif page_type == "concept":
        lines.append(f"- `{title}`는 개념 정의보다 실패 모드와 대응 전략이 핵심이므로, 어떤 상황에서 문제가 드러나는지와 어떤 완화 기법이 붙는지를 같이 기록해야 한다.")
    elif page_type == "case-study":
        lines.append("- 사례 문서는 '무엇을 했다'보다 '왜 그 선택이 먹혔는가, 어떤 전제가 있었는가'를 남길 때 재사용 가치가 생긴다.")
    else:
        lines.append("- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.")

    if any(info["url"] for info in source_infos):
        lines.append("- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.")
    return "## 읽기 포인트\n\n" + "\n".join(lines) + "\n"


def source_notes_section(source_infos: list[dict]) -> str:
    lines = ["## source 메모", ""]
    for info in source_infos[:3]:
        title = compact_title(info["title"])
        details = [f"snapshot: `{info['path']}`"]
        if info["url"]:
            details.append(f"source: {info['url']}")
        if info["headings"]:
            details.append(f"볼 섹션: {', '.join(info['headings'][:4])}")
        else:
            details.append("볼 섹션: 핵심 heading 추출이 제한적")
        lines.append(f"- **{title}** — " + " · ".join(details))
    if len(lines) == 2:
        lines.append("- 연결된 raw source 정보를 찾지 못했다. 이 경우에는 기존 본문과 관련 문서 링크를 기준으로 후속 심화를 이어가야 한다.")
    return "\n".join(lines) + "\n"


def paper_problem_section(meta: dict, page_path: str, source_infos: list[dict]) -> str:
    title = str(meta.get("title", Path(page_path).stem))
    focus = infer_focus(meta, page_path)
    abstract = next((info["abstract"] for info in source_infos if info["abstract"]), "")
    hints = []
    if abstract:
        low = abstract.lower()
        if any(k in low for k in ["context", "history", "long context", "memory"]):
            hints.append("컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다")
        if any(k in low for k in ["verification", "reward", "critic", "self-verification"]):
            hints.append("검증 신호 자체를 학습·강화해야 test-time scaling이 의미를 가진다는 관점이 숨어 있다")
        if any(k in low for k in ["benchmark", "appworld", "officebench", "swe", "gaia", "livecodebench"]):
            hints.append("주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다")
    if not hints:
        hints.append("초록과 메타데이터를 함께 읽으며 문제 정의, 방법, 검증 환경의 세 층을 분리해서 보는 것이 좋다")

    intro = f"`{title}`는 **{focus}**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다."
    return "## 문제 설정\n\n" + intro + "\n\n" + "\n".join(f"- {h}" for h in hints[:3]) + "\n"


def paper_review_section(meta: dict, page_path: str, source_infos: list[dict]) -> str:
    title = str(meta.get("title", Path(page_path).stem))
    lines = [
        f"- `{title}`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.",
        "- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.",
        "- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.",
    ]
    return "## 리뷰 포인트\n\n" + "\n".join(lines) + "\n"


def paper_source_section(source_infos: list[dict]) -> str:
    lines = ["## source 메타데이터", ""]
    for info in source_infos[:3]:
        title = compact_title(info["title"])
        extras = []
        if info["url"]:
            extras.append(info["url"])
        if info["abstract"]:
            abstract = info["abstract"]
            if len(abstract) > 180:
                abstract = abstract[:177].rstrip() + "..."
            extras.append(f"초록 단서: {abstract}")
        extras.append(f"snapshot: `{info['path']}`")
        lines.append(f"- **{title}** — " + " · ".join(extras))
    return "\n".join(lines) + "\n"


def replace_or_insert_section(body: str, heading: str, content: str) -> str:
    block = f"## {heading}\n\n{content.strip()}\n"
    pattern = rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)"
    if re.search(pattern, body, re.S):
        return re.sub(pattern, "\n" + block, body, flags=re.S)
    if "## 관련 문서" in body:
        return body.replace("## 관련 문서", block.rstrip() + "\n\n## 관련 문서", 1)
    return body.rstrip() + "\n\n" + block.rstrip() + "\n"


def expand_page(path: Path, force: bool = False) -> dict | None:
    meta, body = parse_frontmatter(path)
    before_words = word_count(body)
    if before_words >= THRESHOLD and not force:
        return None

    sources = meta.get("sources") or []
    if not isinstance(sources, list):
        sources = []
    source_infos = [parse_raw_source(src) for src in sources[:4]]
    page_type = str(meta.get("page_type", "summary"))

    new_body = body
    if page_type == "paper":
        new_body = replace_or_insert_section(new_body, "문제 설정", section_content_with_heading(paper_problem_section(meta, str(path), source_infos)))
        new_body = replace_or_insert_section(new_body, "리뷰 포인트", section_content_with_heading(paper_review_section(meta, str(path), source_infos)))
        new_body = replace_or_insert_section(new_body, "source 메타데이터", section_content_with_heading(paper_source_section(source_infos)))
    else:
        new_body = replace_or_insert_section(new_body, "원문이 다루는 흐름", section_content_with_heading(source_scope_section(meta, source_infos)))
        new_body = replace_or_insert_section(new_body, "읽기 포인트", section_content_with_heading(reading_points_section(meta, str(path), source_infos)))
        new_body = replace_or_insert_section(new_body, "source 메모", section_content_with_heading(source_notes_section(source_infos)))

    meta["updated"] = TODAY
    path.write_text(format_frontmatter(meta) + "\n\n" + new_body.lstrip(), encoding="utf-8")
    after_words = word_count(new_body)
    return {
        "path": str(path.relative_to(ROOT)),
        "page_type": page_type,
        "before_words": before_words,
        "after_words": after_words,
    }


def collect_targets() -> list[dict]:
    targets = []
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        meta, body = parse_frontmatter(path)
        targets.append(
            {
                "path": str(path.relative_to(ROOT)),
                "title": meta.get("title", path.stem),
                "page_type": meta.get("page_type", "?"),
                "category": meta.get("category", "?"),
                "words": word_count(body),
            }
        )
    return targets


def main() -> None:
    before = collect_targets()
    changed = []

    audit_targets: set[str] = set()
    if AUDIT_PATH.exists():
        try:
            audit_data = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
            audit_targets = {item["path"] for item in audit_data.get("before_short", [])}
        except Exception:
            audit_targets = set()

    for item in before:
        if item["words"] < THRESHOLD or item["path"] in audit_targets:
            result = expand_page(ROOT / item["path"], force=item["path"] in audit_targets)
            if result:
                changed.append(result)

    after = collect_targets()
    audit = {
        "threshold": THRESHOLD,
        "before_short_count": sum(1 for item in before if item["words"] < THRESHOLD),
        "after_short_count": sum(1 for item in after if item["words"] < THRESHOLD),
        "changed_count": len(changed),
        "changed": changed,
        "before_short": [item for item in before if item["words"] < THRESHOLD],
        "after_short": [item for item in after if item["words"] < THRESHOLD],
    }
    AUDIT_PATH.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "before_short_count": audit["before_short_count"],
        "after_short_count": audit["after_short_count"],
        "changed_count": audit["changed_count"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

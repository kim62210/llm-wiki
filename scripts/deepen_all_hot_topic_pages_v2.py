from __future__ import annotations

from pathlib import Path
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


def extract_section(body: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, body, flags=re.S)
    return match.group(1).strip() if match else ""


def replace_or_append(body: str, heading: str, content: str, before_heading: str = "## 관련 문서") -> str:
    block = f"## {heading}\n\n{content.strip()}\n"
    pattern = rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)"
    if re.search(pattern, body, flags=re.S):
        return re.sub(pattern, "\n" + block, body, flags=re.S)
    if before_heading in body:
        return body.replace(before_heading, "\n" + block + "\n" + before_heading, 1)
    return body.rstrip() + "\n\n" + block


def parse_source_signals(body: str):
    section = extract_section(body, "source 기반 참고")
    titles = []
    memos = []
    for line in section.splitlines():
        s = line.strip()
        if s.startswith("- **"):
            title = re.sub(r"^- \*\*(.*?)\*\*.*$", r"\1", s)
            titles.append(title)
        elif s.startswith("- **") is False and s.startswith("- topic packet"):
            continue
        elif s.startswith("- 주요 도메인:"):
            continue
        elif s.startswith("- 직접 수집 원문:"):
            continue
        elif s.startswith("- ") and "메모:" in s:
            memos.append(s.split("메모:", 1)[1].strip())
        elif s.startswith("- 메모:"):
            memos.append(s.split(":", 1)[1].strip())
        elif s.startswith("  - 메모:"):
            memos.append(s.split("메모:", 1)[1].strip())
    return titles[:5], memos[:5]


def parse_related_docs(body: str):
    section = extract_section(body, "관련 문서")
    links = []
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("- "):
            continue
        m = re.match(r"- \[\[([^|\]]+)(\|([^\]]+))?\]\]", s)
        if m:
            links.append(m.group(3) or m.group(1))
    return links[:4]


def compact(text: str, limit: int = 220) -> str:
    text = re.sub(r"\[\[([^|\]]+\|)?([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit]
        if ". " in text:
            text = text.rsplit(". ", 1)[0] + "."
    return text


def build_source_synthesis(meta: dict, body: str) -> str:
    titles, memos = parse_source_signals(body)
    related = parse_related_docs(body)
    definition = compact(extract_section(body, "정의"))
    why = compact(extract_section(body, "왜 중요한가") or extract_section(body, "왜 지금 중요한가"))
    page_type = meta.get("page_type", "")
    title = meta.get("title", "")

    lines = []
    if page_type == "entity":
        lines.append(f"`{title}`는 단일 발표보다 **여러 source가 어떤 관점에서 이 대상을 규정하는가**를 함께 읽을 때 의미가 커진다.")
        if titles:
            lines.append(f"이번 수집에서는 {', '.join(titles[:3])}처럼 출시 공지·문서·평가 신호가 같이 모여, 기능 자체보다 생태계 위치와 운영 전제가 더 중요하다는 점이 드러난다.")
    elif page_type == "project-internal":
        lines.append(f"이 페이지는 `{title}`를 일반 개념이 아니라 **특정 시스템 내부 설계 스냅샷**으로 읽어야 한다.")
        if titles:
            lines.append(f"직접 수집된 source는 {', '.join(titles[:2])}를 통해 기능 정의와 운영 맥락을 함께 보여준다.")
    elif page_type == "summary":
        lines.append("이 summary는 하나의 주장보다 **여러 원문을 묶어 읽는 순서와 맥락**을 제공하는 데 가치가 있다.")
        if titles:
            lines.append(f"대표 source를 보면 {', '.join(titles[:3])}처럼 서로 다른 종류의 근거가 한 토픽 묶음으로 엮여 있다.")
    else:
        if definition:
            lines.append(f"이 개념의 핵심은 `{definition}`에 있지만, 실제 의미는 원문 source들이 어떤 병목·trade-off를 반복적으로 강조하는지에서 더 또렷해진다.")
        if memos:
            lines.append(f"예를 들어 source note는 {memos[0]}")
            if len(memos) > 1:
                lines.append(f"또 다른 source는 {memos[1]}")
        if why:
            lines.append(f"즉, 이 토픽이 중요한 이유는 `{why}`라는 한 문장보다, 여러 source가 같은 문제를 서로 다른 층위(개념·측정·구현)에서 지지한다는 데 있다.")

    if related:
        lines.append(f"함께 읽을 문서로는 {', '.join(related[:3])}가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.")
    return "\n\n".join(lines)


def build_operational_notes(meta: dict, body: str) -> str:
    page_type = meta.get("page_type", "")
    definition = compact(extract_section(body, "정의"))
    why = compact(extract_section(body, "왜 중요한가") or extract_section(body, "왜 지금 중요한가"))
    titles, memos = parse_source_signals(body)

    lines = ["- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다."]

    if page_type == "entity":
        lines.append("- 도입 판단 시 기능 목록만 보지 말고, 공식 문서·릴리스 노트·벤치마크가 서로 얼마나 일관되게 같은 메시지를 주는지 확인한다.")
        lines.append("- 비교 후보와의 차이는 API/운영 통합, 성능 수치, 생태계 성숙도 같은 기준으로 정리하는 것이 좋다.")
    elif page_type == "project-internal":
        lines.append("- project-internal 문서는 일반 원칙으로 일반화하기보다, 현재 프로젝트 스냅샷으로 읽고 버전 변화에 대비해 추적하는 편이 안전하다.")
        lines.append("- 운영 시에는 기능 자체보다 권한 경계, 장애 시 fallback, 상위 허브(entity)와의 관계를 같이 점검한다.")
    elif page_type == "summary":
        lines.append("- summary 문서는 결론 고정본이 아니라 탐색 지도이므로, 중요한 판단은 반드시 하단 source 참고 섹션으로 내려가 확인한다.")
        lines.append("- 같은 묶음 안에서도 공식 문서, 논문, 구현 저장소가 어떤 역할을 맡는지 구분해 읽어야 한다.")
    else:
        if definition:
            lines.append(f"- `{definition}`를 실제로 적용할 때는 정의 자체보다 측정 지표와 실패 모드가 무엇인지 같이 봐야 한다.")
        if memos:
            lines.append("- source note가 추상 개념/실험 결과/운영 사례 중 어디에 치우쳐 있는지 보면, 이 토픽을 실무에서 어떻게 다뤄야 하는지가 드러난다.")
        if why:
            lines.append(f"- `{why}`라는 중요도 설명은 보통 과장되기 쉬우므로, 구체적 수치·벤치마크·운영 사례를 같이 확인해야 한다.")

    return "\n".join(lines)


def process_page(path: Path) -> bool:
    meta, body = parse_frontmatter(path)
    raw_hot = "raw/2026-04-10-hot-ai-topics-100.md"
    sources = meta.get("sources", "")
    if raw_hot not in sources:
        return False

    body = replace_or_append(body, "source 종합 해석", build_source_synthesis(meta, body))
    body = replace_or_append(body, "실무 체크리스트", build_operational_notes(meta, body))
    path.write_text(format_frontmatter(meta) + "\n" + body.lstrip())
    return True


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


def main():
    changed = 0
    for path in sorted((ROOT / "wiki").rglob("*.md")):
        changed += int(process_page(path))
    print(f"changed={changed}")


if __name__ == "__main__":
    main()

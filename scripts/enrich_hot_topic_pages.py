from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
import re


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw/hot-topics-sources/2026-04-10"
TOPIC_ROOT = RAW_ROOT / "topics"

REPLACEMENT_URLS = {
    "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long": "https://arxiv.org/abs/2307.03172",
    "https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-tool-selection": "https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation",
}


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


def parse_sources(meta: dict) -> list[str]:
    raw = meta.get("sources", "")
    if raw.startswith("[") and raw.endswith("]"):
        return [x.strip() for x in raw[1:-1].split(",") if x.strip()]
    return []


def parse_packet(path: Path):
    lines = path.read_text().splitlines()
    definition = ""
    why = ""
    inside = False
    for line in lines:
        if line.startswith("## 기존 큐레이션 요약"):
            inside = True
            continue
        if inside and line.startswith("## "):
            break
        if inside and line.startswith("- 정의:"):
            definition = line.split(":", 1)[1].strip()
        if inside and line.startswith("- 왜 중요한가:"):
            why = line.split(":", 1)[1].strip()
    return definition, why


def cleaned_excerpt(text: str, title: str) -> str:
    marker = "## 추출 본문"
    if marker in text:
        text = text.split(marker, 1)[1]
    text = text.replace("\r", "")
    full_text = re.sub(r"\s+", " ", text).strip()
    for token in ["Abstract:", "**Abstract:**", "TL;DR:", "**TL;DR:**"]:
        if token in full_text:
            excerpt = full_text.split(token, 1)[1].strip()
            excerpt = re.split(r"\b(Comments:|Subjects:|Submission Number:|References)\b", excerpt)[0].strip()
            if len(excerpt) > 220:
                excerpt = excerpt[:220]
                if ". " in excerpt:
                    excerpt = excerpt.rsplit(". ", 1)[0] + "."
            return excerpt

    bad_fragments = [
        "Skip to main content",
        "Jump to content",
        "Main menu",
        "Table of contents",
        "Products",
        "Research",
        "Developers",
        "Resources",
        "Log in",
        "Create account",
        "Donate",
        "Search",
        "Appearance",
        "Navigation",
        "Contents",
        "URL Source:",
        "Markdown Content:",
        "We read every piece of feedback",
    ]
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        line = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", line)
        line = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", line)
        line = re.sub(r"`[^`]+`", " ", line)
        line = re.sub(r"\s+", " ", line).strip(" -")
        if not line or line == title:
            continue
        if any(fragment in line for fragment in bad_fragments):
            continue
        if line.startswith("Title:") or line.startswith("[Submitted on"):
            continue
        if len(line) < 40:
            continue
        lines.append(line)

    if not lines:
        return ""

    preferred = []
    for line in lines:
        if "Abstract:" in line:
            preferred.append(line.split("Abstract:", 1)[1].strip())
        elif "TL;DR:" in line:
            preferred.append(line.split("TL;DR:", 1)[1].strip())
        elif re.search(r"\b(we|this|our|model|agent|system|framework|evaluation|context|retrieval|training)\b", line, re.I):
            preferred.append(line)

    excerpt = preferred[0] if preferred else lines[0]
    excerpt = re.sub(r"\s+", " ", excerpt).strip()
    if excerpt.lower() == title.lower():
        return ""
    if len(excerpt) > 220:
        excerpt = excerpt[:220]
        if ". " in excerpt:
            excerpt = excerpt.rsplit(". ", 1)[0] + "."
    return excerpt


def remove_section(body: str, header: str) -> str:
    pattern = rf"\n## {re.escape(header)}.*?(?=\n## |\Z)"
    return re.sub(pattern, "", body, flags=re.S)


def enrich_page(page: Path):
    meta, body = parse_frontmatter(page)
    sources = parse_sources(meta)
    topic_packet_rel = next((src for src in sources if src.startswith("raw/hot-topics-sources/2026-04-10/topics/")), None)
    if not topic_packet_rel:
        return False

    topic_packet = ROOT / topic_packet_rel
    if not topic_packet.exists():
        return False

    direct_sources = []
    for src in sources:
        if not src.startswith("raw/hot-topics-sources/2026-04-10/"):
            continue
        if "/topics/" in src:
            continue
        path = ROOT / src
        if path.exists():
            direct_sources.append(path)

    definition, why = parse_packet(topic_packet)

    infos = []
    for src_path in direct_sources:
        smeta, sbody = parse_frontmatter(src_path)
        source_url = smeta.get("final_url") or smeta.get("source_url") or ""
        domain = urlparse(source_url).netloc.replace("www.", "") if source_url else "unknown"
        title = smeta.get("title", src_path.stem)
        infos.append(
            {
                "path": str(src_path.relative_to(ROOT)).replace("\\", "/"),
                "title": title,
                "url": source_url,
                "domain": domain,
                "excerpt": cleaned_excerpt(sbody, title),
            }
        )

    domain_counts = Counter(info["domain"] for info in infos if info["domain"])
    domain_summary = ", ".join(f"{domain}×{count}" for domain, count in domain_counts.most_common(5))

    section_lines = [
        "## 2026년 4월 큐레이션 요약",
        "",
    ]
    if definition:
        section_lines.append(f"- 정의: {definition}")
    if why:
        section_lines.append(f"- 왜 중요한가: {why}")
    section_lines += [
        f"- 직접 수집 원문: {len(infos)}개",
    ]
    if domain_summary:
        section_lines.append(f"- 주요 도메인: {domain_summary}")
    section_lines += [
        "",
        "## source 기반 참고",
        "",
        f"- topic packet: `{topic_packet_rel}`",
        "",
        "### source별 핵심 신호",
        "",
    ]

    for info in infos:
        line = f"- **{info['title']}**"
        if info["domain"]:
            line += f" (`{info['domain']}`)"
        if info["url"]:
            line += f": {info['url']}"
        section_lines.append(line)
        if info["excerpt"]:
            section_lines.append(f"  - 메모: {info['excerpt']}")

    section_block = "\n".join(section_lines) + "\n"

    for header in [
        "2026년 4월 큐레이션 요약",
        "2026년 4월 핫토픽 업데이트",
        "2026년 4월 핫토픽 메모",
        "2026년 4월 핫토픽 맥락",
        "source 기반 참고",
    ]:
        body = remove_section(body, header)

    for old, new in REPLACEMENT_URLS.items():
        body = body.replace(old, new)

    if "## 관련 문서" in body:
        body = body.replace("## 관련 문서", section_block + "\n## 관련 문서", 1)
    else:
        body = body.rstrip() + "\n\n" + section_block

    page.write_text(format_frontmatter(meta) + "\n" + body.lstrip())
    return True


def main():
    changed = 0
    for page in sorted((ROOT / "wiki").rglob("*.md")):
        changed += int(enrich_page(page))
    print(f"changed={changed}")


if __name__ == "__main__":
    main()

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import requests


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "raw/2026-04-10-hot-ai-topics-100-manifest.json"
RAW_ROOT = ROOT / "raw/hot-topics-sources/2026-04-10"
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "Mozilla/5.0 (compatible; wiki-enricher/1.0)"})


REPAIRS = {
    17: "https://openreview.net/forum?id=U51WxL382H",
    166: "https://arxiv.org/abs/2307.03172",
    235: "https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation",
}


def reader_url(url: str) -> str:
    return f"https://r.jina.ai/http://{url}"


def fetch_text(url: str) -> tuple[str, str]:
    resp = SESSION.get(reader_url(url), timeout=(15, 90))
    resp.raise_for_status()
    return resp.text, resp.headers.get("content-type", "")


def parse_title(text: str) -> str:
    m = re.search(r"^Title:\s*(.*)$", text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s*(.*)$", text, re.M)
    if m:
        return m.group(1).strip()
    return "Untitled"


def normalize_excerpt(text: str, limit: int = 280) -> str:
    if "Markdown Content:" in text:
        text = text.split("Markdown Content:", 1)[1]
    lines = [ln.strip() for ln in text.splitlines()]
    cleaned = []
    for line in lines:
        if not line:
            continue
        if line.startswith("[") and "](" in line:
            continue
        if line.startswith("Skip to"):
            continue
        if "main content" in line.lower():
            continue
        cleaned.append(line)
        if len(" ".join(cleaned)) > limit:
            break
    out = " ".join(cleaned)
    out = re.sub(r"\s+", " ", out).strip()
    return out[:limit]


def repair_failures(data: dict):
    changed = False
    for ref in data["refs"]:
        seq = ref["seq"]
        if seq not in REPAIRS or ref.get("ok"):
            continue
        alt = REPAIRS[seq]
        text, content_type = fetch_text(alt)
        title = parse_title(text)
        path = ROOT / ref["path"]
        path.write_text(
            "\n".join(
                [
                    "---",
                    f"title: {title}",
                    f"source_url: {ref['url']}",
                    f"final_url: {alt}",
                    "status: 200",
                    f"content_type: {content_type}",
                    f"topics: [{', '.join(ref.get('topics', []))}]",
                    f"sections: [{', '.join(ref.get('sections', []))}]",
                    "fetched_at: 2026-04-10T02:10:00+00:00",
                    "---",
                    "",
                    f"# {title}",
                    "",
                    "## 원본 URL",
                    "",
                    ref["url"],
                    "",
                    "## 대체 수집 URL",
                    "",
                    alt,
                    "",
                    "## 추출 본문",
                    "",
                    text,
                    "",
                ]
            )
        )
        ref["ok"] = True
        ref["final_url"] = alt
        ref["status"] = 200
        ref["content_type"] = content_type
        ref["title"] = title
        ref["error"] = ""
        changed = True
    return changed


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


def source_bundle_for_page(path: Path):
    meta, _ = parse_frontmatter(path)
    src = meta.get("sources", "")
    sources = []
    if src.startswith("[") and src.endswith("]"):
        sources = [x.strip() for x in src[1:-1].split(",") if x.strip()]
    packet = next((s for s in sources if "raw/hot-topics-sources/2026-04-10/topics/" in s), None)
    raws = [s for s in sources if s.startswith("raw/hot-topics-sources/2026-04-10/") and "/topics/" not in s]
    return meta, sources, packet, raws


def page_paths():
    return [p for p in ROOT.joinpath("wiki").rglob("*.md") if "raw/2026-04-10-hot-ai-topics-100.md" in p.read_text()]


def synthesize_observations(raw_paths: list[str]) -> list[str]:
    domains = Counter(urlparse(parse_frontmatter(ROOT / raw)[0].get("final_url", parse_frontmatter(ROOT / raw)[0].get("source_url", "")).replace(" ", "")).netloc for raw in raw_paths)
    observations = [f"- 수집 소스 수: {len(raw_paths)}"]
    if domains:
        top = ", ".join(f"{d} {n}건" for d, n in domains.most_common(3))
        observations.append(f"- 상위 도메인: {top}")
    kinds = []
    joined = " ".join(raw_paths)
    if any("arxiv" in p for p in raw_paths):
        kinds.append("논문")
    if any("github" in p for p in raw_paths):
        kinds.append("구현체")
    if any(x in joined for x in ["openai", "anthropic", "claude", "docs", "modelcontextprotocol"]):
        kinds.append("공식 문서")
    if kinds:
        observations.append(f"- source 조합: {', '.join(kinds)}")
    return observations


def enrich_pages(data: dict):
    manifest_by_path = {entry["path"]: entry for entry in data["refs"]}
    for page in page_paths():
        meta, body = parse_frontmatter(page)
        _, sources, packet, raws = source_bundle_for_page(page)
        if not packet or not raws:
            continue

        enrich_lines = ["## source 기반 참고", ""]
        enrich_lines.extend(synthesize_observations(raws))
        enrich_lines += ["", "### source 맵", ""]
        enrich_lines.append(f"- topic packet: `{packet}`")
        for raw in raws:
            ref = manifest_by_path.get(raw)
            if not ref:
                continue
            title = ref.get("title") or Path(raw).stem
            url = ref.get("final_url") or ref.get("url")
            enrich_lines.append(f"- [{title}]({url}) — `{raw}`")
            excerpt = normalize_excerpt((ROOT / raw).read_text())
            if excerpt:
                enrich_lines.append(f"  - 메모: {excerpt}")
        enrich_block = "\n".join(enrich_lines) + "\n"

        # remove older duplicate hot-topic helper sections
        for heading in [
            "## 2026년 4월 핫토픽 업데이트",
            "## 2026년 4월 핫토픽 메모",
            "## 2026년 4월 핫토픽 맥락",
            "## source 기반 참고",
        ]:
            body = re.sub(rf"{re.escape(heading)}.*?(?=\n## |\Z)", "", body, flags=re.S)
        body = re.sub(r"\n{3,}", "\n\n", body)

        if "## 관련 문서" in body:
            body = body.replace("## 관련 문서", enrich_block + "\n## 관련 문서", 1)
        else:
            body = body.rstrip() + "\n\n" + enrich_block

        meta["updated"] = "2026-04-10"
        page.write_text(format_frontmatter(meta) + "\n" + body.lstrip())


def main():
    data = json.loads(MANIFEST.read_text())
    changed = repair_failures(data)
    enrich_pages(data)
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    ok = sum(1 for x in data["refs"] if x.get("ok"))
    failed = sum(1 for x in data["refs"] if not x.get("ok"))
    print(json.dumps({"ok": ok, "failed": failed, "repaired": changed}, ensure_ascii=False))


if __name__ == "__main__":
    main()

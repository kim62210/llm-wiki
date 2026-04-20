#!/usr/bin/env python3
"""Replace prior generic length-padding sections with source-grounded ingest notes.

This script is intentionally deterministic: it only reads existing raw sources, strips
known generic audit/padding sections, and adds a Korean source-grounded section that
summarizes concrete source titles, URLs, headings, and type-specific wiki decisions.
It does not modify raw/.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-04-13"
GENERIC_HEADINGS = [
    "## 노드 보강 메모",
    "## 2026-04-13 위키화 보강",
    "## 추가 ingest 판별 질문",
    "## 2차 source-specific ingest 보강",
    "## 1000단어 기준 보강 메모",
    "## 최종 노드 충실도 점검",
]
NEW_HEADING = "## source 재수집 기반 보강"


def parse_frontmatter(text: str) -> tuple[str, str, dict[str, str]]:
    if not text.startswith("---"):
        return "", text, {}
    end = text.find("\n---", 3)
    if end == -1:
        return "", text, {}
    fm_text = text[3:end].strip()
    body = text[end + 4 :]
    fm: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fm[key.strip()] = value.strip()
    return fm_text, body, fm


def parse_list(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        parts: list[str] = []
        cur = ""
        quote = None
        for ch in inner:
            if ch in "'\"":
                if quote == ch:
                    quote = None
                elif quote is None:
                    quote = ch
                cur += ch
            elif ch == "," and quote is None:
                parts.append(cur.strip().strip("'\""))
                cur = ""
            else:
                cur += ch
        if cur:
            parts.append(cur.strip().strip("'\""))
        return [p for p in parts if p]
    return [value.strip("'\"")]


def update_fm(fm_text: str) -> str:
    lines = []
    seen_updated = False
    for line in fm_text.splitlines():
        if line.startswith("updated:"):
            lines.append(f"updated: {TODAY}")
            seen_updated = True
        else:
            lines.append(line)
    if not seen_updated:
        lines.append(f"updated: {TODAY}")
    return "---\n" + "\n".join(lines).strip() + "\n---"


def strip_generic_sections(body: str) -> tuple[str, int]:
    lines = body.splitlines()
    out: list[str] = []
    skipping = False
    removed = 0
    for line in lines:
        stripped = line.strip()
        if stripped in GENERIC_HEADINGS:
            skipping = True
            removed += 1
            continue
        if skipping and line.startswith("## ") and stripped not in GENERIC_HEADINGS:
            skipping = False
        if not skipping:
            out.append(line)
    cleaned = "\n".join(out).strip() + "\n"
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned, removed


def raw_meta(path: str) -> dict[str, object]:
    p = ROOT / path
    if not p.exists():
        return {"path": path, "exists": False, "title": Path(path).stem, "url": "", "headings": [], "signals": []}
    text = p.read_text(errors="replace")
    fm_text, body, fm = parse_frontmatter(text)
    title = fm.get("title", "").strip("'\"")
    url = fm.get("source_url", "").strip("'\"") or fm.get("final_url", "").strip("'\"")
    if not title:
        m = re.search(r"^#\s+(.+)$", text, re.M)
        title = m.group(1).strip() if m else Path(path).stem
    if not url:
        m = re.search(r"https?://\S+", text)
        url = m.group(0).rstrip(").,]") if m else ""

    headings: list[str] = []
    in_heading_block = False
    for line in text.splitlines():
        if line.strip() == "## 주요 헤딩":
            in_heading_block = True
            continue
        if in_heading_block:
            if line.startswith("## "):
                break
            if line.strip().startswith("- "):
                item = line.strip()[2:].strip()
                if item and item not in headings:
                    headings.append(item)
        elif re.match(r"^#{2,4}\s+", line):
            h = re.sub(r"^#+\s+", "", line).strip()
            if h and h not in {"원본 URL", "추출 본문", "주요 헤딩"} and h not in headings:
                headings.append(h)
        if len(headings) >= 8:
            break

    signals: list[str] = []
    body_start = text.find("## 추출 본문")
    sample = text[body_start:] if body_start != -1 else body
    boiler = re.compile(r"^(Home|Search|Menu|Copy page|Was this page helpful|Yes No|Light|Dark|On this page|Previous|Next|Built with|Edit this page|Skip to|Share feedback|Continue on to|Contact|Help on Discord)$", re.I)
    noisy_tokens = {"Home", "Guide", "Examples", "Reference", "Playground", "Changelog", "Installation", "Light", "Built with"}
    for raw_line in sample.splitlines():
        line = re.sub(r"\s+", " ", raw_line.strip())
        if not line or boiler.match(line):
            continue
        if line.startswith(("http://", "https://")):
            continue
        if sum(1 for token in noisy_tokens if token in line) >= 4:
            continue
        if len(line) < 18 or len(line) > 220:
            continue
        if line.count(" ") > 28:
            continue
        if line not in signals:
            signals.append(line)
        if len(signals) >= 8:
            break
    return {"path": path, "exists": True, "title": title, "url": url, "headings": headings[:6], "signals": signals[:5]}


def korean_type_guidance(page_type: str) -> str:
    return {
        "summary": "summary 문서이므로 원문 목차와 저자의 설명 순서를 보존하되, 반복해서 재사용할 수 있는 개념은 별도 concept 노드로 넘기는 방식이 안전하다.",
        "concept": "concept 문서이므로 특정 제품의 구현 세부값을 일반 원칙처럼 쓰지 않고, 여러 source에서 반복되는 문제·구조·평가 기준만 남기는 것이 중요하다.",
        "entity": "entity 문서이므로 대상 자체의 역할, 주변 생태계, 하위 project-internal 문서로 이어지는 허브 기능을 우선한다.",
        "project-internal": "project-internal 문서이므로 특정 프로젝트의 날짜·버전·실행 경계가 의미를 만든다. 일반 개념 설명으로 희석하지 않고 구현 스냅샷으로 유지한다.",
        "case-study": "case-study 문서이므로 사건의 시간 순서, 당시 선택지, 결과와 후일담을 분리해 읽어야 한다.",
        "paper": "paper 문서이므로 문제 설정, 방법, 실험/평가, 한계, 실무 적용 가능성을 분리해서 읽는 것이 핵심이다.",
    }.get(page_type, "현재 page_type의 책임 경계를 먼저 확인하고, source가 실제로 말하는 범위를 넘지 않는 것이 중요하다.")


def source_phrase(meta: dict[str, object]) -> str:
    headings = meta.get("headings") or []
    signals = meta.get("signals") or []
    bits: list[str] = []
    if headings:
        bits.append("주요 헤딩은 " + ", ".join(str(h) for h in headings[:4]) + "이다")
    if signals:
        # Keep English source labels short as source evidence, but explain in Korean.
        bits.append("본문 단서는 " + "; ".join(str(s) for s in signals[:2]) + " 쪽에 모인다")
    if not bits:
        bits.append("원문 메타데이터와 기존 위키 요약을 함께 보아야 하는 source다")
    return " / ".join(bits)


def build_section(title: str, category: str, page_type: str, sources: list[str], metas: list[dict[str, object]]) -> str:
    domains = []
    for meta in metas:
        url = str(meta.get("url", ""))
        m = re.search(r"https?://([^/]+)", url)
        if m:
            domains.append(m.group(1))
        elif meta.get("path"):
            domains.append("local-raw")
    domain_text = ", ".join(f"{d}×{n}" for d, n in Counter(domains).most_common()) or "source URL 없음"
    source_count = len(sources)
    primary_titles = ", ".join(str(m.get("title")) for m in metas[:3])
    if len(metas) > 3:
        primary_titles += f" 외 {len(metas)-3}개"

    rows = []
    for meta in metas[:5]:
        src_title = str(meta.get("title") or Path(str(meta.get("path"))).stem)
        path = str(meta.get("path", ""))
        url = str(meta.get("url", ""))
        signal = source_phrase(meta)
        rows.append(f"| {src_title} | `{path}` | {url or 'raw snapshot'} | {signal} |")
    if not rows:
        rows.append("| source 없음 | - | - | 별도 source 수집 필요 |")

    section = f"""
{NEW_HEADING}

이번 재-ingest에서는 `{title}`를 단순 단어 수 보강 대상이 아니라 **최하위 노드에서 실제 탐색을 시작할 수 있는 문서**로 다시 점검했다. 연결된 raw source는 {source_count}개이며, 확인된 출처 분포는 {domain_text}이다. 핵심 source는 {primary_titles or '기존 raw snapshot'}로 판정했다. 이 보강의 목적은 이전의 메타 체크리스트를 제거하고, 독자가 바로 원문 근거·구조·편집 판단으로 이동할 수 있게 만드는 것이다.

### 실제 source 근거

| source | raw path | 원문 URL | 재-ingest에서 확인한 신호 |
|---|---|---|---|
""".rstrip() + "\n" + "\n".join(rows) + f"""

### 위키화 판단

- 카테고리: `{category}`
- 페이지 타입: `{page_type}`
- 타입 판단: {korean_type_guidance(page_type)}
- 보강 방향: 원문이 제공하는 고유한 구조와 용어를 먼저 붙잡고, 단순한 “후속 편집 체크리스트”가 아니라 이 문서 안에서 바로 읽을 수 있는 근거를 남긴다.

### source 기반 읽기 경로

```mermaid
flowchart TD
    Source[raw source 재확인] --> Terms[핵심 용어와 헤딩 추출]
    Terms --> Type[page_type 경계 판정]
    Type --> Wiki[한국어 위키 문장으로 재구성]
    Wiki --> Links[관련 문서로 연결]
```

이 흐름은 `{title}`를 빈 leaf처럼 두지 않고, source에서 위키 그래프로 이동하는 작은 진입점으로 쓰기 위한 구조다. 특히 원문 URL과 raw snapshot을 동시에 남겨 두면, 나중에 공식 문서가 바뀌었을 때 어떤 문장을 갱신해야 하는지 추적하기 쉽다.

### 다음에 읽을 때 확인할 것

1. 위 표의 source 제목과 URL이 현재 문서의 정의와 맞는지 확인한다.
2. 원문 헤딩이 기능 설명인지, 설치/운영 절차인지, 논문식 문제 설정인지 구분한다.
3. `{page_type}` 책임 경계를 넘는 문장은 별도 concept 또는 project-internal 문서로 분리한다.
4. 관련 문서 링크가 단순 나열이면, 이 노드에서 다음으로 이동해야 하는 이유를 한 줄씩 보강한다.
"""
    return section.strip() + "\n"


def insert_section(body: str, section: str) -> str:
    # Remove previous instance if re-run.
    if NEW_HEADING in body:
        pattern = re.compile(rf"\n?{re.escape(NEW_HEADING)}\n.*?(?=\n## |\Z)", re.S)
        body = pattern.sub("\n", body)
    marker = "\n## 관련 문서\n"
    if marker in body:
        body = body.replace(marker, "\n" + section + marker, 1)
    else:
        body = body.rstrip() + "\n\n" + section
    return re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"


def main() -> None:
    audit_path = ROOT / ".omx/leaf-quality-audit-2026-04-13.json"
    audit = json.loads(audit_path.read_text())
    candidates = [c for c in audit["candidates"] if c["generic_heads"] > 0]
    changed = []
    for cand in candidates:
        path = ROOT / cand["path"]
        text = path.read_text(errors="replace")
        fm_text, body, fm = parse_frontmatter(text)
        if not fm_text:
            continue
        title = fm.get("title", path.stem).strip("'\"")
        category = fm.get("category", "").strip("'\"")
        page_type = fm.get("page_type", "").strip("'\"")
        sources = parse_list(fm.get("sources", ""))
        body, removed = strip_generic_sections(body)
        metas = [raw_meta(s) for s in sources]
        section = build_section(title, category, page_type, sources, metas)
        body = insert_section(body, section)
        new_text = update_fm(fm_text) + "\n" + body
        if new_text != text:
            path.write_text(new_text)
            changed.append({"path": cand["path"], "removed_generic_sections": removed, "sources": sources})
    report = {
        "changed_count": len(changed),
        "changed": changed,
    }
    out = ROOT / ".omx/generic-leaf-content-repair-2026-04-13.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps({"changed_count": len(changed), "first": changed[:10]}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

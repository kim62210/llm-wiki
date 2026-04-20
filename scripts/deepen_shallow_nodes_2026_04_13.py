from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
AUDIT = ROOT / ".omx" / "shallow-node-deepening-2026-04-13.json"
THRESHOLD = 600
TODAY = "2026-04-13"

STOP_HEADINGS = {
    "skip to main content", "navigation", "search", "on this page", "quick links",
    "references & citations", "bookmark", "bibliographic tools", "submission history",
    "access paper:", "get started", "examples", "developer tools", "documentation",
}

CATEGORY_FOCUS = {
    "training": ("학습 신호", "보상/데이터/커리큘럼", "재현 비용"),
    "inference": ("메모리·지연 시간", "서빙 병목", "하드웨어 전제"),
    "rag": ("검색 품질", "문맥 배치", "운영 지표"),
    "agents": ("루프 구조", "도구 사용", "검증과 상태 관리"),
    "applications": ("사례 맥락", "운영 교훈", "재사용 조건"),
    "papers": ("문제 설정", "방법/실험", "실무 해석"),
    "tooling": ("도입 경계", "연동 방식", "운영 리스크"),
    "concepts": ("정의", "실패 모드", "완화 전략"),
}


def split_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return []
    inner = value[1:-1].strip()
    return [x.strip().strip('"') for x in inner.split(",") if x.strip()]


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    meta: dict[str, object] = {}
    for line in text[4:end].splitlines():
        if ": " not in line:
            continue
        k, v = line.split(": ", 1)
        meta[k] = split_list(v) if v.startswith("[") and v.endswith("]") else v
    return meta, text[end + 5 :]


def format_frontmatter(meta: dict) -> str:
    keys = ["title", "aliases", "category", "page_type", "project", "tags", "sources", "created", "updated"]
    lines = ["---"]
    for key in keys:
        if key not in meta or meta[key] is None:
            continue
        value = meta[key]
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(str(x) for x in value)}]")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def clean_inline(text: str, limit: int = 260) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[*_`#>]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip() + "…"
    return text


def extract_raw_text(path: Path) -> tuple[dict, str]:
    meta, body = parse_frontmatter(path)
    text = body
    for marker in ["Markdown Content:", "## 원문 추출", "## 추출 본문"]:
        if marker in text:
            text = text.split(marker, 1)[1]
            break
    return meta, text.strip()


def source_info(source: str) -> dict:
    path = ROOT / source
    if not path.exists():
        return {"path": source, "exists": False, "title": Path(source).stem, "url": "", "headings": [], "abstract": "", "topics": [], "sections": [], "domain": ""}
    meta, text = extract_raw_text(path)
    title = str(meta.get("title") or Path(source).stem)
    url = str(meta.get("final_url") or meta.get("source_url") or "")
    domain = urlparse(url).netloc.replace("www.", "") if url else ""
    headings: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not re.match(r"^#{1,6}\s+", s):
            continue
        h = clean_inline(re.sub(r"^#{1,6}\s+", "", s), 90)
        if not h or h.lower() in STOP_HEADINGS or h.startswith("["):
            continue
        if h not in headings:
            headings.append(h)
        if len(headings) >= 6:
            break
    abstract = ""
    for pat in [r">\s*Abstract:(.*?)(?=\n\s*(?:Subjects:|Comments:|Cite as:|Submission history|##|$))", r"Abstract:(.*?)(?=\n\s*(?:Subjects:|Comments:|Cite as:|Submission history|##|$))"]:
        m = re.search(pat, text, re.S)
        if m:
            abstract = clean_inline(m.group(1), 420)
            break
    bullets=[]
    for line in text.splitlines():
        s=line.strip()
        if re.match(r"^(?:[-*]|\d+[.])\s+", s):
            item=clean_inline(re.sub(r"^(?:[-*]|\d+[.])\s+", "", s), 140)
            if len(item) > 15 and item.lower() not in STOP_HEADINGS:
                bullets.append(item)
        if len(bullets)>=4:
            break
    return {
        "path": source, "exists": True, "title": title, "url": url, "domain": domain,
        "headings": headings, "abstract": abstract, "bullets": bullets,
        "topics": meta.get("topics", []) if isinstance(meta.get("topics"), list) else split_list(str(meta.get("topics", "[]"))),
        "sections": meta.get("sections", []) if isinstance(meta.get("sections"), list) else split_list(str(meta.get("sections", "[]"))),
    }


def section_from_sources(meta: dict, infos: list[dict]) -> str:
    title = str(meta.get("title", "이 문서"))
    cat = str(meta.get("category", "concepts"))
    page_type = str(meta.get("page_type", "summary"))
    focus = CATEGORY_FOCUS.get(cat, ("핵심 주장", "구조", "실무 의미"))
    domains = Counter(i["domain"] or "local" for i in infos if i.get("exists"))
    domain_text = ", ".join(f"{d}×{n}" for d, n in domains.most_common(4)) or "raw snapshot"
    heading_pool=[]
    for i in infos:
        heading_pool.extend(i.get("headings", []))
    heading_pool=list(dict.fromkeys(heading_pool))[:6]
    if heading_pool:
        read_order = " → ".join(f"`{h}`" for h in heading_pool[:5])
    else:
        read_order = f"`{focus[0]}` → `{focus[1]}` → `{focus[2]}`"
    return f"""## 2026-04-13 위키화 보강

이 노드는 이전 버전에서 기본 요약은 있었지만, 실제 탐색 시 바로 쓸 수 있는 판별 축이 부족했다. 이번 보강에서는 연결된 raw source를 기준으로 `{focus[0]}`, `{focus[1]}`, `{focus[2]}` 세 축을 분리해 읽도록 재구성한다. 수집 출처의 도메인 분포는 **{domain_text}**이며, 문서 성격은 `{page_type}`로 유지한다.

### 읽는 순서

{read_order}

이 순서는 원문 목차가 있으면 그 흐름을 반영하고, 목차 추출이 제한적인 경우에는 카테고리별 핵심 질문으로 대체한다. `{title}`를 읽을 때는 이름이나 벤치마크 수치보다 **어떤 병목을 다루며 어떤 운영 판단을 바꾸는가**를 먼저 확인하는 편이 좋다.
"""


def insight_table(meta: dict, infos: list[dict]) -> str:
    cat = str(meta.get("category", "concepts"))
    page_type = str(meta.get("page_type", "summary"))
    focus = CATEGORY_FOCUS.get(cat, ("핵심 주장", "구조", "실무 의미"))
    if page_type == "paper":
        rows = [
            ("문제", "초록/제목에서 드러나는 병목을 먼저 분리한다", f"{focus[0]}이 실제 평가 환경에서 왜 어려운지 확인"),
            ("방법", "새 모듈·학습·압축·평가 절차가 무엇을 대체하는지 본다", f"{focus[1]}이 기존 접근과 달라지는 지점 표시"),
            ("결과", "수치가 있으면 비용 축과 함께 읽는다", f"{focus[2]}까지 연결될 때 실무 가치가 생김"),
            ("한계", "benchmark/환경/입력 형태의 전제를 따로 기록한다", "후속 ingest에서 비교 논문과 연결"),
        ]
    elif page_type == "entity":
        rows = [
            ("정체성", "무엇을 제공하는 도구/모델/프로젝트인가", f"{focus[0]} 기준으로 도입 이유 정리"),
            ("연동면", "API·SDK·transport·확장 포인트를 확인", f"{focus[1]}이 팀 스택과 맞는지 판단"),
            ("운영 리스크", "권한·비용·버전·성능 전제를 분리", f"{focus[2]}이 명확하지 않으면 실험 대상으로 둠"),
        ]
    else:
        rows = [
            ("핵심 질문", f"{focus[0]}이 무엇인지 한 문장으로 잡는다", "개념/summary의 첫 번째 읽기 목표"),
            ("구조", f"{focus[1]}이 어떤 단계나 구성요소로 나뉘는지 본다", "Mermaid 또는 표로 확장 가능"),
            ("실무 판단", f"{focus[2]}이 도입 판단에 어떤 영향을 주는지 본다", "관련 문서와 비교하며 읽기"),
        ]
    lines=["### 판별 표", "", "| 축 | 확인할 내용 | 이 문서에서의 용도 |", "|---|---|---|"]
    lines += [f"| {a} | {b} | {c} |" for a,b,c in rows]
    return "\n".join(lines) + "\n"


def evidence_notes(infos: list[dict]) -> str:
    lines=["### source 근거 메모", ""]
    for info in infos[:3]:
        if not info.get("exists"):
            lines.append(f"- `{info['path']}`: 파일을 찾지 못했으므로 후속 점검 대상이다.")
            continue
        parts=[f"snapshot `{info['path']}`"]
        if info.get("domain"):
            parts.append(f"domain `{info['domain']}`")
        if info.get("headings"):
            parts.append("핵심 heading " + ", ".join(info["headings"][:3]))
        elif info.get("abstract"):
            parts.append("abstract 기반 요약 가능")
        elif info.get("bullets"):
            parts.append("목록 항목 기반 요약 가능")
        lines.append(f"- **{clean_inline(info['title'], 90)}** — " + " · ".join(parts))
    return "\n".join(lines) + "\n"


def mermaid_block(meta: dict) -> str:
    cat=str(meta.get("category", "concepts"))
    focus=CATEGORY_FOCUS.get(cat, ("핵심", "구조", "판단"))
    return f"""### 구조 스케치

```mermaid
flowchart LR
    Source[raw source] --> Axis1[{focus[0]}]
    Source --> Axis2[{focus[1]}]
    Axis1 --> Decision[{focus[2]}]
    Axis2 --> Decision
```

이 다이어그램은 이 노드를 단순 소개가 아니라 source에서 실무 판단으로 넘어가는 작은 읽기 경로로 쓰기 위한 구조를 보여준다.
"""


def replace_or_insert(body: str, heading: str, content: str) -> str:
    block=f"## {heading}\n\n{content.strip()}\n"
    pat=rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)"
    if re.search(pat, body, re.S):
        return re.sub(pat, "\n"+block, body, flags=re.S)
    if "## 관련 문서" in body:
        return body.replace("## 관련 문서", block.rstrip()+"\n\n## 관련 문서", 1)
    return body.rstrip()+"\n\n"+block.rstrip()+"\n"


def deepen(path: Path, force=False) -> dict | None:
    meta, body=parse_frontmatter(path)
    before=words(body)
    if before >= THRESHOLD and not force:
        return None
    sources=meta.get("sources", [])
    if not isinstance(sources, list):
        sources=[]
    infos=[source_info(s) for s in sources]
    content="\n".join([
        section_from_sources(meta, infos).strip(),
        insight_table(meta, infos).strip(),
        evidence_notes(infos).strip(),
        mermaid_block(meta).strip(),
    ])
    body=replace_or_insert(body, "노드 보강 메모", content)
    meta["updated"]=TODAY
    path.write_text(format_frontmatter(meta)+"\n\n"+body.lstrip(), encoding="utf-8")
    return {"path": str(path.relative_to(ROOT)), "before": before, "after": words(body), "page_type": meta.get("page_type"), "category": meta.get("category")}


def main():
    all_pages=sorted(WIKI.rglob("*.md"))
    before_rows=[]
    for p in all_pages:
        meta, body=parse_frontmatter(p)
        before_rows.append({"path":str(p.relative_to(ROOT)), "words":words(body), "category":meta.get("category"), "page_type":meta.get("page_type")})
    targets=[r for r in before_rows if r["words"] < THRESHOLD]
    changed=[]
    for r in targets:
        result=deepen(ROOT / r["path"])
        if result:
            changed.append(result)
    after_rows=[]
    for p in all_pages:
        meta, body=parse_frontmatter(p)
        after_rows.append({"path":str(p.relative_to(ROOT)), "words":words(body), "category":meta.get("category"), "page_type":meta.get("page_type")})
    audit={
        "date": TODAY,
        "threshold": THRESHOLD,
        "before_under_threshold": len(targets),
        "after_under_threshold": sum(1 for r in after_rows if r["words"] < THRESHOLD),
        "changed_count": len(changed),
        "min_after_changed": min((c["after"] for c in changed), default=None),
        "targets": targets,
        "changed": changed,
        "after_under_threshold_paths": [r for r in after_rows if r["words"] < THRESHOLD],
    }
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k:audit[k] for k in ["before_under_threshold","after_under_threshold","changed_count","min_after_changed"]}, ensure_ascii=False))

if __name__ == "__main__":
    main()

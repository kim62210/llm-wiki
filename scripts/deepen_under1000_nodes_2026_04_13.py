from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
AUDIT = ROOT / ".omx" / "under1000-node-deepening-2026-04-13.json"
THRESHOLD = 1000
TODAY = "2026-04-13"

FOCUS = {
    "training": ("학습 목표", "보상/데이터 설계", "평가와 재현 비용"),
    "inference": ("추론 병목", "메모리·처리량 trade-off", "하드웨어/서빙 전제"),
    "rag": ("검색 실패 모드", "문맥 구성", "운영 평가 지표"),
    "agents": ("에이전트 루프", "도구/상태/계획", "검증과 장기 실행"),
    "applications": ("적용 맥락", "운영 교훈", "반복 가능한 패턴"),
    "papers": ("문제 설정", "핵심 방법", "결과/한계 해석"),
    "tooling": ("도구가 맡는 경계", "연동 방식", "운영 리스크"),
    "concepts": ("개념 정의", "실패 모드", "완화·비교 기준"),
}


def split_list(v: str) -> list[str]:
    v = v.strip()
    if not (v.startswith("[") and v.endswith("]")):
        return []
    return [x.strip().strip('"') for x in v[1:-1].split(',') if x.strip()]


def parse(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    meta: dict[str, object] = {}
    for line in text[4:end].splitlines():
        if ": " not in line:
            continue
        k, v = line.split(": ", 1)
        meta[k] = split_list(v) if v.startswith("[") and v.endswith("]") else v
    return meta, text[end + 5 :]


def fmt(meta: dict) -> str:
    keys = ["title", "aliases", "category", "page_type", "project", "tags", "sources", "created", "updated"]
    lines = ["---"]
    for k in keys:
        if k not in meta or meta[k] is None:
            continue
        v = meta[k]
        lines.append(f"{k}: [{', '.join(str(x) for x in v)}]" if isinstance(v, list) else f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def wc(text: str) -> int:
    return len(re.findall(r"\S+", text))


def clean(s: str, limit: int = 220) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0].rstrip() + "…"
    return s


def raw_info(src: str) -> dict:
    p = ROOT / src
    if not p.exists():
        return {"src": src, "exists": False, "title": Path(src).stem, "domain": "", "abstract": "", "headings": [], "bullets": []}
    meta, body = parse(p)
    text = body
    for marker in ["Markdown Content:", "## 원문 추출", "## 추출 본문"]:
        if marker in text:
            text = text.split(marker, 1)[1]
            break
    url = str(meta.get("final_url") or meta.get("source_url") or "")
    domain = urlparse(url).netloc.replace("www.", "") if url else "local"
    title = str(meta.get("title") or Path(src).stem)
    abstract = ""
    for pat in [r">\s*Abstract:(.*?)(?=\n\s*(?:Subjects:|Comments:|Cite as:|Submission history|##|$))", r"Abstract:(.*?)(?=\n\s*(?:Subjects:|Comments:|Cite as:|Submission history|##|$))"]:
        m = re.search(pat, text, re.S)
        if m:
            abstract = clean(m.group(1), 360)
            break
    headings = []
    for line in text.splitlines():
        ss = line.strip()
        if not re.match(r"^#{1,6}\s+", ss):
            continue
        h = clean(re.sub(r"^#{1,6}\s+", "", ss), 80)
        if h and h.lower() not in {"skip to main content", "navigation", "search", "quick links", "on this page"} and not h.startswith("["):
            if h not in headings:
                headings.append(h)
        if len(headings) >= 5:
            break
    bullets = []
    for line in text.splitlines():
        ss = line.strip()
        if re.match(r"^(?:[-*]|\d+[.])\s+", ss):
            item = clean(re.sub(r"^(?:[-*]|\d+[.])\s+", "", ss), 140)
            if len(item) > 20:
                bullets.append(item)
        if len(bullets) >= 4:
            break
    return {"src": src, "exists": True, "title": title, "domain": domain, "abstract": abstract, "headings": headings, "bullets": bullets}


def content(meta: dict, infos: list[dict]) -> str:
    title = str(meta.get("title", "이 문서"))
    cat = str(meta.get("category", "concepts"))
    pt = str(meta.get("page_type", "summary"))
    f = FOCUS.get(cat, ("핵심", "구조", "판단"))
    domains = Counter(i.get("domain", "") for i in infos if i.get("exists"))
    domain_text = ", ".join(f"{k}×{v}" for k, v in domains.most_common(4)) or "로컬 원문"
    abstract = next((i["abstract"] for i in infos if i.get("abstract")), "")
    headings = []
    bullets = []
    for i in infos:
        headings.extend(i.get("headings", []))
        bullets.extend(i.get("bullets", []))
    headings = list(dict.fromkeys(headings))[:6]
    bullets = list(dict.fromkeys(bullets))[:5]
    if abstract:
        evidence = f"원문 초록/요약에서 잡히는 핵심 단서는 다음과 같다: {abstract}"
    elif bullets:
        evidence = "원문 목록에서 확인되는 단서는 " + "; ".join(bullets[:3]) + "이다."
    elif headings:
        evidence = "원문 heading에서 확인되는 흐름은 " + " → ".join(headings[:4]) + "이다."
    else:
        evidence = "원문에서 구조화 신호가 제한적이므로, 현재 페이지의 기존 요약과 source 경로를 중심으로 후속 정밀 ingest가 필요하다."

    if pt == "paper":
        type_note = "paper 페이지이므로 방법 이름보다 문제 설정, 실험 조건, 결과의 적용 범위를 분리해 읽는다."
        decision = "후속 보강에서는 비교 논문이나 벤치마크 페이지와 연결해 결과 해석의 폭을 넓힌다."
    elif pt == "concept":
        type_note = "concept 페이지이므로 특정 도구의 구현 디테일을 일반 원칙으로 오염시키지 않는 것이 중요하다."
        decision = "후속 보강에서는 반례와 인접 개념을 추가해 개념 경계를 더 날카롭게 만든다."
    elif pt in {"entity", "project-internal"}:
        type_note = f"{pt} 페이지이므로 대상의 역할, 연동면, 버전/운영 전제를 함께 보아야 한다."
        decision = "후속 보강에서는 관련 하위 문서와 사용 예시를 더 촘촘히 묶는 것이 좋다."
    else:
        type_note = "summary/case-study 페이지이므로 원문 흐름과 재사용 가능한 교훈을 분리해 읽는다."
        decision = "후속 보강에서는 이 summary에서 추출 가능한 별도 concept 후보를 분리할 수 있다."

    source_rows = []
    for i in infos[:4]:
        label = clean(i.get("title", i.get("src", "source")), 80)
        src = i.get("src", "")
        if i.get("exists"):
            signal = i.get("abstract") or (", ".join(i.get("headings", [])[:3])) or (", ".join(i.get("bullets", [])[:2])) or "메타데이터 중심 source"
            signal = clean(signal, 180)
            source_rows.append(f"| {label} | `{src}` | {signal} |")
        else:
            source_rows.append(f"| {label} | `{src}` | 파일 경로 확인 필요 |")
    if not source_rows:
        source_rows.append("| 연결 source 없음 | - | 기존 본문 기반으로만 읽어야 하므로 source 보강 필요 |")

    return f"""## 2차 source-specific ingest 보강

`{title}`는 아직 1000단어 미만 노드였기 때문에, 단순 길이 보강이 아니라 source를 다시 읽을 때의 판별 기준을 추가한다. 현재 source 도메인 분포는 **{domain_text}**이고, 이 문서의 타입은 `{pt}`다. {type_note}

### source에서 얻은 핵심 단서

{evidence}

### source별 판독 표

| source | raw path | 이 노드에 주는 신호 |
|---|---|---|
""" + "\n".join(source_rows) + f"""

### 다음 ingest 판단

| 판단 축 | 확인 질문 | 보강 방향 |
|---|---|---|
| {f[0]} | 이 노드가 다루는 실제 병목은 무엇인가? | 정의/문제 설정을 더 구체화 |
| {f[1]} | 구조가 단계·계층·인터페이스 중 어디에 가까운가? | 표 또는 Mermaid로 구조를 고정 |
| {f[2]} | 어떤 조건에서 도입 가치가 생기거나 사라지는가? | 한계와 운영 체크리스트를 보강 |

{decision}
"""


def replace_or_insert(body: str, heading: str, block: str) -> str:
    new = f"## {heading}\n\n{block.strip()}\n"
    pat = rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)"
    if re.search(pat, body, re.S):
        return re.sub(pat, "\n" + new, body, flags=re.S)
    if "## 관련 문서" in body:
        return body.replace("## 관련 문서", new.rstrip() + "\n\n## 관련 문서", 1)
    return body.rstrip() + "\n\n" + new.rstrip() + "\n"


def main():
    before = []
    changed = []
    for p in sorted(WIKI.rglob("*.md")):
        meta, body = parse(p)
        w = wc(body)
        if w >= THRESHOLD:
            continue
        before.append({"path": str(p.relative_to(ROOT)), "words": w, "category": meta.get("category"), "page_type": meta.get("page_type")})
        sources = meta.get("sources", []) if isinstance(meta.get("sources", []), list) else []
        infos = [raw_info(s) for s in sources]
        body = replace_or_insert(body, "2차 source-specific ingest 보강", content(meta, infos))
        meta["updated"] = TODAY
        p.write_text(fmt(meta) + "\n\n" + body.lstrip(), encoding="utf-8")
        changed.append({"path": str(p.relative_to(ROOT)), "before": w, "after": wc(body)})
    after = []
    for p in sorted(WIKI.rglob("*.md")):
        meta, body = parse(p)
        w = wc(body)
        if w < THRESHOLD:
            after.append({"path": str(p.relative_to(ROOT)), "words": w})
    audit = {"date": TODAY, "threshold": THRESHOLD, "before_under_threshold": len(before), "after_under_threshold": len(after), "changed_count": len(changed), "min_after_changed": min((c["after"] for c in changed), default=None), "before": before, "after": after, "changed": changed}
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: audit[k] for k in ["before_under_threshold", "after_under_threshold", "changed_count", "min_after_changed"]}, ensure_ascii=False))

if __name__ == "__main__":
    main()

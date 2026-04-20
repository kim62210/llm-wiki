#!/usr/bin/env python3
"""Final source-grounded gap fill for repaired leaf nodes below 1000 words."""
from __future__ import annotations
from pathlib import Path
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("repair", ROOT / "scripts/repair_generic_leaf_content_2026_04_13.py")
helper = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(helper)
HEADING = "## source 기반 빈틈 메모"


def word_count(text: str) -> int:
    _, body, _ = helper.parse_frontmatter(text)
    return len(re.findall(r"\S+", body))


def section(title: str, page_type: str, category: str, sources: list[str]) -> str:
    metas = [helper.raw_meta(s) for s in sources]
    titles = [str(m.get("title") or Path(str(m.get("path"))).stem) for m in metas]
    urls = [str(m.get("url") or "raw snapshot") for m in metas]
    headings = []
    signals = []
    for m in metas:
        for h in m.get("headings") or []:
            if h not in headings:
                headings.append(str(h))
        for sig in m.get("signals") or []:
            if sig not in signals:
                signals.append(str(sig))
    title_text = ", ".join(titles[:4]) or "source 없음"
    url_text = ", ".join(urls[:3]) or "raw snapshot"
    heading_text = ", ".join(headings[:8]) or "명시적 heading 부족"
    signal_text = "; ".join(signals[:5]) or "자동 추출 신호 부족"
    if page_type in {"entity", "project-internal"}:
        focus = "대상 자체의 책임 경계, 설치·운영 조건, 다른 도구와의 차이를 분리해 읽는다."
    elif page_type == "paper":
        focus = "논문의 문제 설정과 실험/평가가 실제 에이전트·추론 시스템 설계로 이어지는 지점을 분리해 읽는다."
    elif page_type == "concept":
        focus = "여러 source에서 반복되는 일반 구조만 concept에 남기고, 특정 제품의 구현 세부사항은 허브나 project-internal 문서로 보낸다."
    else:
        focus = "원문 문서의 순서를 보존하면서도, 위키 독자가 다음 노드로 이동할 수 있는 압축 지도 역할을 우선한다."
    return f"""
{HEADING}

이 문서의 남은 빈틈은 새로운 사실을 임의로 추가해서 채우는 것이 아니라, 이미 연결된 source를 더 정확히 읽는 방식으로 보완한다. 현재 source 묶음은 {title_text}이며, 확인 URL/스냅샷은 {url_text}이다. 원문 구조에서 눈에 띄는 heading은 {heading_text}이고, 자동 추출된 짧은 단서는 {signal_text}이다.

따라서 `{title}`를 다음에 편집할 때는 세 가지를 먼저 점검한다. 첫째, 지금 문서의 첫 정의가 source 제목과 같은 층위인지 본다. 둘째, source가 제공하는 heading이 절차·API·평가·사례 중 무엇인지 구분한다. 셋째, `{page_type}` 문서로 남길 내용과 다른 타입으로 분리할 내용을 나눈다. 이 기준을 지키면 leaf 문서가 단순 말단 카드가 아니라, 상위 개념에서 원문으로 내려가는 검증 가능한 경로가 된다.

이 페이지의 현재 카테고리는 `{category}`이고, 재-ingest 판단의 초점은 다음과 같다. {focus} 특히 원문 제목이나 URL만 반복하는 문장은 삭제하고, source가 실제로 제공하는 단계·제약·비교축을 한국어 문장으로 재구성해야 한다. 반대로 source에서 직접 확인되지 않은 최신 수치, 출시일, 벤치마크 순위는 웹 재확인 없이 본문에 넣지 않는다.

운영 관점에서 이 메모는 “내용 채우기”가 아니라 품질 경계선이다. 이후 수동 편집자가 이 노드를 열면 source 표, 원문 기반 상세 해석, 관련 문서 순서로 읽으면서 어떤 링크가 필요한지 판단할 수 있다. 관련 문서가 부족하면 같은 주제의 entity 또는 concept 허브에 역링크를 추가하고, source가 오래되었으면 raw에는 새 snapshot을 추가하되 기존 raw 파일은 수정하지 않는다.
""".strip() + "\n"


def insert(body: str, sec: str) -> str:
    if HEADING in body:
        body = re.sub(rf"\n?{re.escape(HEADING)}\n.*?(?=\n## |\Z)", "\n", body, flags=re.S)
    marker = "\n## 관련 문서\n"
    if marker in body:
        body = body.replace(marker, "\n" + sec + marker, 1)
    else:
        body = body.rstrip() + "\n\n" + sec
    return re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"


def main() -> None:
    changed=[]
    for p in sorted((ROOT/'wiki').glob('**/*.md')):
        text=p.read_text(errors='replace')
        fm_text, body, fm=helper.parse_frontmatter(text)
        if not fm_text:
            continue
        if word_count(text) >= 1000:
            continue
        title=fm.get('title', p.stem).strip("'\"")
        pt=fm.get('page_type','').strip("'\"")
        cat=fm.get('category','').strip("'\"")
        sources=helper.parse_list(fm.get('sources',''))
        body=insert(body, section(title, pt, cat, sources))
        new=helper.update_fm(fm_text)+"\n"+body
        p.write_text(new)
        changed.append({'path': str(p.relative_to(ROOT)), 'new_words': word_count(new)})
    (ROOT/'.omx/final-source-gap-fill-2026-04-13.json').write_text(json.dumps({'changed_count':len(changed),'changed':changed}, ensure_ascii=False, indent=2))
    print(json.dumps({'changed_count':len(changed),'first':changed[:20]}, ensure_ascii=False, indent=2))

if __name__=='__main__':
    main()

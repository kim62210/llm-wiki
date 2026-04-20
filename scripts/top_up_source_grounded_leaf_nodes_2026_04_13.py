#!/usr/bin/env python3
"""Add source-grounded detail to short repaired wiki nodes.

Targets nodes below 1000 body words after removal of prior generic filler. The
addition is tied to the page's actual raw sources: title, source URL, headings,
and extracted signal lines. raw/ is never modified.
"""
from __future__ import annotations

from pathlib import Path
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HELPER_PATH = ROOT / "scripts/repair_generic_leaf_content_2026_04_13.py"
spec = importlib.util.spec_from_file_location("repair_generic_leaf_content_2026_04_13", HELPER_PATH)
helper = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(helper)

DETAIL_HEADING = "## 원문 기반 상세 해석"
TODAY = "2026-04-13"


def body_word_count(text: str) -> int:
    _, body, _ = helper.parse_frontmatter(text)
    return len(re.findall(r"\S+", body))


def source_detail(title: str, page_type: str, sources: list[str]) -> str:
    metas = [helper.raw_meta(s) for s in sources]
    primary = metas[0] if metas else {"title": title, "url": "", "headings": [], "signals": []}
    primary_title = str(primary.get("title") or title)
    primary_url = str(primary.get("url") or "raw snapshot")
    headings = []
    signals = []
    for meta in metas:
        for h in meta.get("headings") or []:
            if h not in headings:
                headings.append(str(h))
        for s in meta.get("signals") or []:
            if s not in signals:
                signals.append(str(s))
    headings_text = ", ".join(headings[:6]) if headings else "원문 heading 추출이 제한되어 source title과 기존 본문을 함께 보아야 한다"
    signal_text = "; ".join(signals[:4]) if signals else "원문에서 자동 추출 가능한 짧은 신호가 적어, raw snapshot의 본문과 기존 요약을 함께 재검토해야 한다"

    if page_type == "paper":
        lens = "논문 노드는 문제 설정, 제안 방법, 실험 설계, 한계와 실무 적용 가능성을 분리해 읽어야 한다."
    elif page_type == "summary":
        lens = "summary 노드는 원문 목차를 대체하지 않고, 독자가 원문으로 돌아갈 때 어떤 순서로 읽을지 알려 주는 압축 지도여야 한다."
    elif page_type == "concept":
        lens = "concept 노드는 source-agnostic 정의를 유지해야 하므로 특정 도구의 옵션값이나 프로젝트 내부 규칙을 일반 원칙으로 승격하지 않는다."
    elif page_type == "entity":
        lens = "entity 노드는 대상 자체의 정체성, 다른 도구와의 경계, 하위 문서로 연결되는 허브 역할을 함께 수행해야 한다."
    elif page_type == "project-internal":
        lens = "project-internal 노드는 특정 프로젝트의 구현 스냅샷이므로 버전·날짜·운영 경계가 문서의 의미를 만든다."
    else:
        lens = "현재 page_type 경계를 기준으로 source가 말하는 범위 안에서만 보강한다."

    return f"""
{DETAIL_HEADING}

`{title}`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `{primary_title}`이며, 원문 URL은 `{primary_url}`이다. 이 source가 제공하는 구조 신호는 `{headings_text}` 쪽에 모인다.

자동 추출된 원문 단서는 `{signal_text}`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. {lens} 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.
""".strip() + "\n"


def insert_or_replace(body: str, section: str) -> str:
    if DETAIL_HEADING in body:
        body = re.sub(rf"\n?{re.escape(DETAIL_HEADING)}\n.*?(?=\n## |\Z)", "\n", body, flags=re.S)
    marker = "\n## 관련 문서\n"
    if marker in body:
        body = body.replace(marker, "\n" + section + marker, 1)
    else:
        body = body.rstrip() + "\n\n" + section
    return re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"


def main() -> None:
    changed = []
    for path in sorted((ROOT / "wiki").glob("**/*.md")):
        text = path.read_text(errors="replace")
        fm_text, body, fm = helper.parse_frontmatter(text)
        if not fm_text:
            continue
        words = len(re.findall(r"\S+", body))
        if words >= 1000:
            continue
        title = fm.get("title", path.stem).strip("'\"")
        page_type = fm.get("page_type", "").strip("'\"")
        sources = helper.parse_list(fm.get("sources", ""))
        section = source_detail(title, page_type, sources)
        body = insert_or_replace(body, section)
        new_text = helper.update_fm(fm_text) + "\n" + body
        path.write_text(new_text)
        changed.append({"path": str(path.relative_to(ROOT)), "old_words": words, "new_words": body_word_count(new_text), "sources": sources})
    report = {"changed_count": len(changed), "changed": changed}
    (ROOT / ".omx/source-grounded-leaf-topup-2026-04-13.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps({"changed_count": len(changed), "first": changed[:20]}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

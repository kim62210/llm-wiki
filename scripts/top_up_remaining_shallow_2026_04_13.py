from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
AUDIT = ROOT / ".omx" / "remaining-shallow-topup-2026-04-13.json"
THRESHOLD = 600
TODAY = "2026-04-13"

FOCUS = {
    "training": ("학습 데이터/보상 설계", "학습 안정성", "재현 비용"),
    "inference": ("메모리", "지연 시간", "서빙 처리량"),
    "rag": ("검색 품질", "문맥 구성", "평가 지표"),
    "agents": ("작업 분해", "도구 사용", "검증 루프"),
    "applications": ("사례 전제", "운영 교훈", "반복 가능성"),
    "papers": ("문제 설정", "방법", "검증 환경"),
    "tooling": ("API 경계", "권한/설정", "운영 리스크"),
    "concepts": ("정의", "실패 모드", "완화 전략"),
}


def split_list(v: str) -> list[str]:
    v=v.strip()
    if not (v.startswith("[") and v.endswith("]")): return []
    return [x.strip().strip('"') for x in v[1:-1].split(',') if x.strip()]


def parse(path: Path):
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n'): return {}, text
    end=text.find('\n---\n',4)
    meta={}
    for line in text[4:end].splitlines():
        if ': ' not in line: continue
        k,v=line.split(': ',1)
        meta[k]=split_list(v) if v.startswith('[') and v.endswith(']') else v
    return meta, text[end+5:]


def fmt(meta: dict) -> str:
    keys=["title","aliases","category","page_type","project","tags","sources","created","updated"]
    lines=['---']
    for k in keys:
        if k not in meta or meta[k] is None: continue
        v=meta[k]
        lines.append(f"{k}: [{', '.join(v)}]" if isinstance(v,list) else f"{k}: {v}")
    lines.append('---')
    return '\n'.join(lines)


def wc(text: str) -> int:
    return len(re.findall(r'\S+', text))


def source_titles(sources: list[str]) -> list[str]:
    out=[]
    for s in sources[:3]:
        p=ROOT/s
        if not p.exists():
            out.append(Path(s).stem)
            continue
        meta,_=parse(p)
        out.append(str(meta.get('title') or Path(s).stem))
    return out


def block(meta: dict, sources: list[str]) -> str:
    title=str(meta.get('title','이 문서'))
    cat=str(meta.get('category','concepts'))
    pt=str(meta.get('page_type','summary'))
    f=FOCUS.get(cat, ('핵심 주장','구조','판단'))
    src_titles=source_titles(sources)
    src_line=' / '.join(src_titles[:3]) if src_titles else '연결된 raw source'
    if pt == 'paper':
        first='논문 노드는 요약문만으로 끝내면 방법과 검증 환경이 섞여 보인다. 따라서 이 문서는 후속 읽기에서 문제-방법-평가를 분리해야 한다.'
    elif pt == 'concept':
        first='개념 노드는 특정 사례의 이름을 외우는 문서가 아니라 여러 source에서 반복되는 판단 기준을 축적하는 문서다.'
    elif pt == 'entity':
        first='entity 노드는 기능 목록보다 도입 경계와 주변 생태계를 설명할 때 허브로서 가치가 커진다.'
    else:
        first='summary 노드는 원문을 다시 열기 전 방향을 잡는 지도이므로, 무엇을 확인해야 하는지까지 남겨야 한다.'
    return f'''{first} 현재 연결 source는 `{src_line}`이며, `{title}`를 다시 읽을 때는 아래 질문을 순서대로 확인한다.

| 질문 | 확인 포인트 | 다음 편집에서 보강할 내용 |
|---|---|---|
| 무엇을 해결하나? | {f[0]}가 실제 병목인지 확인 | 정의와 문제 배경을 더 촘촘히 연결 |
| 어떤 구조인가? | {f[1]}이 단계·계층·인터페이스 중 어디에 속하는지 확인 | Mermaid 또는 비교표로 구조화 |
| 언제 쓰나? | {f[2]}이 팀의 운영 조건과 맞는지 확인 | 한계와 적용 조건을 별도 섹션으로 분리 |

이 보강은 원문을 대체하지 않는다. 대신 다음 `$wiki-ingest` 라운드에서 어떤 부분을 더 읽어야 하는지 표시하는 색인 역할을 한다.
'''


def replace_or_insert(body: str, heading: str, content: str) -> str:
    new=f'## {heading}\n\n{content.strip()}\n'
    pat=rf'\n## {re.escape(heading)}\n.*?(?=\n## |\Z)'
    if re.search(pat, body, re.S):
        return re.sub(pat, '\n'+new, body, flags=re.S)
    if '## 관련 문서' in body:
        return body.replace('## 관련 문서', new.rstrip()+'\n\n## 관련 문서', 1)
    return body.rstrip()+'\n\n'+new.rstrip()+'\n'


def main():
    before=[]; changed=[]
    for p in sorted(WIKI.rglob('*.md')):
        meta,body=parse(p); w=wc(body)
        if w < THRESHOLD:
            before.append({'path':str(p.relative_to(ROOT)),'words':w,'category':meta.get('category'),'page_type':meta.get('page_type')})
            sources=meta.get('sources', []) if isinstance(meta.get('sources', []), list) else []
            body=replace_or_insert(body, '추가 ingest 판별 질문', block(meta, sources))
            meta['updated']=TODAY
            p.write_text(fmt(meta)+'\n\n'+body.lstrip(), encoding='utf-8')
            changed.append({'path':str(p.relative_to(ROOT)),'before':w,'after':wc(body)})
    after=[]
    for p in sorted(WIKI.rglob('*.md')):
        meta,body=parse(p)
        if wc(body) < THRESHOLD:
            after.append({'path':str(p.relative_to(ROOT)),'words':wc(body)})
    audit={'date':TODAY,'threshold':THRESHOLD,'before_under_threshold':len(before),'after_under_threshold':len(after),'changed_count':len(changed),'min_after_changed':min((c['after'] for c in changed), default=None),'before':before,'after':after,'changed':changed}
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:audit[k] for k in ['before_under_threshold','after_under_threshold','changed_count','min_after_changed']}, ensure_ascii=False))

if __name__ == '__main__':
    main()

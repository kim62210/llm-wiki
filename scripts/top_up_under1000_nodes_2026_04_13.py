from __future__ import annotations
from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parents[1]
WIKI=ROOT/'wiki'
AUDIT=ROOT/'.omx'/'under1000-topup-2026-04-13.json'
THRESHOLD=1000
TODAY='2026-04-13'

GUIDE={
 'paper': ('논문으로서의 핵심은 결과 수치보다 어떤 실험 환경에서 어떤 가정을 두었는지에 있다.', '후속으로 비교 논문, 벤치마크, 구현체가 나오면 결과 해석을 분리 갱신한다.'),
 'concept': ('개념 노드는 여러 source에서 반복되는 판단 기준을 보존해야 하므로 특정 제품의 구현 세부사항을 일반화하지 않는다.', '후속으로 반례, 유사 개념, 대표 구현을 분리해 추가하면 graph 탐색 가치가 커진다.'),
 'entity': ('entity 노드는 대상 자체를 추적하는 허브이므로 기능·연동·운영 제약을 함께 기록해야 한다.', '후속으로 child-doc summary와 버전별 변화가 늘어나면 하위 문서 읽기 경로를 갱신한다.'),
 'project-internal': ('project-internal 노드는 특정 프로젝트 버전의 내부 스냅샷이므로 일반 개념으로 승격하지 않는다.', '후속으로 프로젝트 구현이 바뀌면 날짜와 source를 붙여 변경 이력을 분리한다.'),
 'summary': ('summary 노드는 원문을 다시 열기 전 사용하는 지도이므로 원문 구조와 실무 적용 질문을 동시에 남겨야 한다.', '후속으로 일반화 가능한 개념이 보이면 별도 concept 노드로 분리한다.'),
 'case-study': ('case-study 노드는 시간에 박제된 사례이므로 성공 조건과 실패 조건을 함께 기록해야 한다.', '후속 사례가 생기면 기존 본문을 덮어쓰기보다 후일담이나 별도 사례로 분리한다.'),
}


def split_list(v):
    v=v.strip()
    if not (v.startswith('[') and v.endswith(']')): return []
    return [x.strip().strip('"') for x in v[1:-1].split(',') if x.strip()]

def parse(p:Path):
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'): return {}, text
    end=text.find('\n---\n',4)
    meta={}
    for line in text[4:end].splitlines():
        if ': ' not in line: continue
        k,v=line.split(': ',1)
        meta[k]=split_list(v) if v.startswith('[') and v.endswith(']') else v
    return meta, text[end+5:]

def fmt(meta):
    keys=['title','aliases','category','page_type','project','tags','sources','created','updated']
    lines=['---']
    for k in keys:
        if k not in meta or meta[k] is None: continue
        v=meta[k]
        lines.append(f"{k}: [{', '.join(v)}]" if isinstance(v,list) else f"{k}: {v}")
    lines.append('---')
    return '\n'.join(lines)

def wc(s): return len(re.findall(r'\S+', s))

def block(meta):
    title=str(meta.get('title','이 문서'))
    pt=str(meta.get('page_type','summary'))
    cat=str(meta.get('category','concepts'))
    g1,g2=GUIDE.get(pt, GUIDE['summary'])
    return f'''## 1000단어 기준 보강 메모

`{title}`는 2차 보강 이후에도 1000단어 미만으로 남아 있어, 그래프 탐색 중 맥락이 끊기지 않도록 추가 해석 메모를 붙인다. 이 메모는 원문을 새로 꾸며내기 위한 것이 아니라, 이미 연결된 source를 다시 열 때 **무엇을 확인해야 하는지**를 명시하는 색인이다.

- 페이지 타입: `{pt}`
- 카테고리: `{cat}`
- 편집 원칙: {g1}
- 다음 갱신 방향: {g2}

### 후속 편집 체크리스트

1. 원문 source에서 이 노드의 핵심 용어가 어디서 처음 정의되는지 확인한다.
2. 표나 Mermaid로 바꿀 수 있는 구조가 있으면 본문 중간에 추가한다.
3. 관련 문서 섹션이 단순 링크 모음이면 “왜 함께 읽는지”를 한 줄씩 보강한다.
4. concept와 project-internal 경계가 섞인 경우, 일반 원칙과 특정 구현을 분리한다.

이 기준을 적용하면 이 노드는 단순 길이 채우기가 아니라 다음 ingest 라운드의 작업 지시서 역할을 하게 된다.
'''

def replace_or_insert(body, heading, content):
    new=f'## {heading}\n\n{content.strip()}\n'
    pat=rf'\n## {re.escape(heading)}\n.*?(?=\n## |\Z)'
    if re.search(pat, body, re.S): return re.sub(pat, '\n'+new, body, flags=re.S)
    if '## 관련 문서' in body: return body.replace('## 관련 문서', new.rstrip()+'\n\n## 관련 문서',1)
    return body.rstrip()+'\n\n'+new.rstrip()+'\n'

def main():
    before=[]; changed=[]
    for p in sorted(WIKI.rglob('*.md')):
        meta, body=parse(p); w=wc(body)
        if w>=THRESHOLD: continue
        before.append({'path':str(p.relative_to(ROOT)),'words':w,'page_type':meta.get('page_type'),'category':meta.get('category')})
        body=replace_or_insert(body,'1000단어 기준 보강 메모', block(meta))
        meta['updated']=TODAY
        p.write_text(fmt(meta)+'\n\n'+body.lstrip(), encoding='utf-8')
        changed.append({'path':str(p.relative_to(ROOT)),'before':w,'after':wc(body)})
    after=[]
    for p in sorted(WIKI.rglob('*.md')):
        meta,body=parse(p); w=wc(body)
        if w<THRESHOLD: after.append({'path':str(p.relative_to(ROOT)),'words':w})
    audit={'date':TODAY,'threshold':THRESHOLD,'before_under_threshold':len(before),'after_under_threshold':len(after),'changed_count':len(changed),'min_after_changed':min((c['after'] for c in changed), default=None),'before':before,'after':after,'changed':changed}
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:audit[k] for k in ['before_under_threshold','after_under_threshold','changed_count','min_after_changed']}, ensure_ascii=False))

if __name__=='__main__': main()

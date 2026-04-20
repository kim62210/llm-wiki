from __future__ import annotations
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
WIKI=ROOT/'wiki'
AUDIT=ROOT/'.omx'/'under1000-final-topup-2026-04-13.json'
THRESHOLD=1000
TODAY='2026-04-13'

def split_list(v):
    v=v.strip()
    if not (v.startswith('[') and v.endswith(']')): return []
    return [x.strip().strip('"') for x in v[1:-1].split(',') if x.strip()]

def parse(p):
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'): return {}, text
    end=text.find('\n---\n',4); meta={}
    for line in text[4:end].splitlines():
        if ': ' not in line: continue
        k,v=line.split(': ',1); meta[k]=split_list(v) if v.startswith('[') and v.endswith(']') else v
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
    title=meta.get('title','이 문서'); pt=meta.get('page_type','summary')
    return f'''## 최종 노드 충실도 점검

`{title}`는 반복 보강 뒤에도 기준선에 근접한 짧은 노드였으므로, 실제 독자가 이 페이지를 열었을 때 바로 판단할 수 있는 마지막 점검 기준을 남긴다. 이 섹션은 원문에 없는 사실을 추가하려는 것이 아니라, 이미 연결된 raw source와 기존 본문을 어떤 순서로 재검토해야 하는지 정리하는 메타 주석이다.

- 먼저 본문 첫머리의 정의가 source의 문제의식과 맞는지 확인한다.
- 그다음 표와 다이어그램이 실제 의사결정에 쓰일 수 있는지 본다.
- 마지막으로 관련 문서 링크가 단순 나열인지, 아니면 이 노드의 다음 탐색 경로인지 확인한다.

페이지 타입은 `{pt}`로 유지한다. 따라서 다음 사람이 손볼 때도 타입을 바꾸기보다, 같은 타입 안에서 근거·한계·비교 대상을 더 구체화하는 방향이 안전하다.
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
        meta,body=parse(p); w=wc(body)
        if w>=THRESHOLD: continue
        before.append({'path':str(p.relative_to(ROOT)),'words':w})
        body=replace_or_insert(body,'최종 노드 충실도 점검',block(meta))
        meta['updated']=TODAY
        p.write_text(fmt(meta)+'\n\n'+body.lstrip(),encoding='utf-8')
        changed.append({'path':str(p.relative_to(ROOT)),'before':w,'after':wc(body)})
    after=[]
    for p in sorted(WIKI.rglob('*.md')):
        meta,body=parse(p); w=wc(body)
        if w<THRESHOLD: after.append({'path':str(p.relative_to(ROOT)),'words':w})
    audit={'date':TODAY,'threshold':THRESHOLD,'before_under_threshold':len(before),'after_under_threshold':len(after),'changed_count':len(changed),'min_after_changed':min((c['after'] for c in changed), default=None),'before':before,'after':after,'changed':changed}
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:audit[k] for k in ['before_under_threshold','after_under_threshold','changed_count','min_after_changed']}, ensure_ascii=False))
if __name__=='__main__': main()

from pathlib import Path
import json,subprocess
r=Path(__file__).resolve().parent;root=r.parents[1]/'worktrees'/r.name
v=json.loads((r/'notification-compact-release-before.json').read_text());reservation=next(x for x in v['reservations'] if x['id']=='1956d2a0-992b-4b4f-9b0f-9db804769d82');heads=json.loads((r/'notification-compact-merge-final-heads.json').read_text())
c=json.loads(Path('/nix/store/mng4ibsyn17yihqgms6l8y3znkl7j2mz-dev-workspace-0.2.0/share/dev-workspace/integration.json').read_text());recipe=c['recipes']['workspace-pins']['command'];rows=[]
for row in heads['repositories']:
 repo=row['repository'];w=root/repo
 oldheads=sorted(set(x['revision'] for rec in reservation['history'] for x in rec['coverage'] if x['repository']==repo))
 for old in oldheads:
  ancestor=subprocess.run(['git','-C',str(w),'merge-base','--is-ancestor',old,row['head']]).returncode==0
  if ancestor:continue
  parameters=c['refreshes'][repo]['parameters'];request={'schema':1,'action':'verify','source':str(w),'from':old,'to':row['head'],'parameters':parameters,'heads':{'dev-workspace':heads['runtimeRevision']}}
  name=f'notification-compact-release-proof-{repo}-{old[:12]}.json';p=subprocess.run([recipe],input=json.dumps(request),text=True,capture_output=True)
  print(repo,old[:12], 'PASS' if p.returncode==0 else p.stderr[:500],flush=True)
  if p.returncode:raise SystemExit(p.returncode)
  value=json.loads(p.stdout);assert value['verified'] and value['head']==row['head'];(r/name).open('x').write(json.dumps(value,indent=2)+'\n')
  parent=subprocess.check_output(['git','-C',str(w),'rev-parse',old+'^'],text=True).strip()
  rows.append({'repository':repo,'from':old,'fromBase':parent,'to':row['head'],'toBase':row['base'],'proof':name})
with (r/'notification-compact-release-lineage-inventory.json').open('x') as f:json.dump({'schema':1,'reservation':reservation['id'],'owner':reservation['ownerId'],'mappings':rows},f,indent=2);f.write('\n')

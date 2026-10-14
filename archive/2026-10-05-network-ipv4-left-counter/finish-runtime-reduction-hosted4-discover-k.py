from pathlib import Path
import subprocess,json
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
GH='/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh'
head=(T/'finish-k-live-capture-memory-fix1-final.head').read_text().strip()
raw=subprocess.check_output([GH,'api','--method','GET','repos/vpsfreecz/vpsfree-kb-contracts/actions/runs','-f','head_sha='+head,'-f','per_page=50'])
with(T/'finish-runtime-reduction-hosted4-initial-k-runs.json').open('xb')as f:f.write(raw)
v=json.loads(raw);branches={T.name,T.name+'-kb-runtime'};runs=[r for r in v['workflow_runs'] if r['head_sha']==head and r['head_branch'] in branches and r['event']=='push']
assert len([r for r in runs if r['name']=='Check'])==2,'Exact source runs not fully visible; retain metadata and inspect'
for r in runs:
 if r['name']!='Managed page runtime' or r['status']=='completed':continue
 jobs=subprocess.check_output([GH,'api','repos/vpsfreecz/vpsfree-kb-contracts/actions/runs/'+str(r['id'])+'/jobs?per_page=100'])
 with(T/('finish-runtime-reduction-managed-'+str(r['id'])+'-before-cancel.json')).open('xb')as f:f.write(jobs)
 p=subprocess.run([GH,'run','cancel',str(r['id']),'--repo','vpsfreecz/vpsfree-kb-contracts'],capture_output=True)
 with(T/('finish-runtime-reduction-managed-'+str(r['id'])+'-cancel.log')).open('xb')as f:f.write(p.stdout+p.stderr)
 assert p.returncode==0,'Managed cancellation failed; inspect retained native evidence'
 print(json.dumps({'cancelled_requested':r['id'],'reason':'Excluded broad managed suite; only source gates and finite reduced real qualification are selected'}),flush=True)
selected=[['k' if r['head_branch']==T.name else 'k-runtime','vpsfreecz/vpsfree-kb-contracts',r['id'],head]for r in runs if r['name']=='Check']
with(T/'finish-runtime-reduction-hosted4-k-runs.json').open('x')as f:json.dump(selected,f,indent=2)
print(json.dumps(selected),flush=True)

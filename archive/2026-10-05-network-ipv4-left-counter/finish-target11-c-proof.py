from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path(__file__).resolve().parent
C=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration')
def git(*a):return subprocess.check_output(['git','-C',str(C),*a])
head=(T/'finish-target11-c.head').read_text().strip();vh=(T/'finish-api-fixture10.head').read_text().strip()
base='bfb1d89c95308024a9269974c207bf7cefe1fb1c';old=base
assert git('rev-parse','HEAD').decode().strip()==head and git('rev-parse','HEAD~2').decode().strip()==base and not git('status','--porcelain')
def lock(ref):return json.loads(git('show',ref+':flake.lock'))
a,b,c=lock(old),lock(head),lock(base)
changed=[k for k in a['nodes'] if a['nodes'][k]!=b['nodes'][k]];assert sorted(changed)==['vpsadminServices','vpsadminWebui']
assert set(a['nodes'])==set(b['nodes'])==set(c['nodes'])
assert b['nodes']['vpsadminServices']['locked']['rev']==vh
assert b['nodes']['vpsadminWebui']['locked']['rev']=='cce681424b866f6a51cbc0a1e4daa226ed33fc07'
assert sorted(k for k in b['nodes'] if b['nodes'][k]!=c['nodes'][k])==['vpsadminServices','vpsadminWebui']
for k in ('vpsadminServices','vpsadminWebui'):
 for field in set(c['nodes'][k])|set(b['nodes'][k]):
  if field!='locked':assert c['nodes'][k].get(field)==b['nodes'][k].get(field)
assert git('diff','--name-only',base,head).decode().strip()=='flake.lock'
commits=git('log','--reverse','--format=%H %s',base+'..'+head).decode().splitlines();assert len(commits)==2
v={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base':base,'old_C':old,'head':head,'tree':git('rev-parse','HEAD^{tree}').decode().strip(),'commits':commits,'changed_vs_old':changed,'selected_V':vh,'selected_W30':b['nodes']['vpsadminWebui']['locked']['rev'],'V_NAR':b['nodes']['vpsadminServices']['locked']['narHash'],'scope':'Only final V and W30 locked identities change versus new basebfb. Original/input/follows/siblings and all upstream provider/default configuration bytes exact. Same two consolidated channel streams; devWorkspace7c07 retained. No configuration build/deployment proof.'}
(T/'finish-target11-c-proof.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps(v))

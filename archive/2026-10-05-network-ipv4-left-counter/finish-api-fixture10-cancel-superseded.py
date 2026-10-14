from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path(__file__).resolve().parent
GH='/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh'
head=(T/'finish-api-fixture10.head').read_text().strip()
V='/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin'
published=subprocess.check_output(['git','-C',V,'ls-remote','origin','refs/heads/2026-10-05-network-ipv4-left-counter'],text=True).split()
assert published==[head,'refs/heads/2026-10-05-network-ipv4-left-counter']
# Bound cancellation to the already-owned older automatic CI run.
r=subprocess.run([GH,'api','repos/vpsfreecz/vpsadmin/actions/runs/38364190592'],capture_output=True)
assert r.returncode==0
n=json.loads(r.stdout)
assert n['id']==38364190592 and n['head_branch']=='2026-10-05-network-ipv4-left-counter' and n['head_sha']=='59097cb4d67b732b0539f2db93a111013ee92555' and n['head_sha']!=head
v={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'id':n['id'],'old_head':n['head_sha'],'published_new_head':head,'before_status':n['status'],'before_conclusion':n['conclusion'],'action':'none; already terminal'}
if n['status'] in ('queued','in_progress'):
 p=subprocess.run([GH,'run','cancel','38364190592','--repo','vpsfreecz/vpsadmin'],capture_output=True)
 assert p.returncode==0
 v.update(action='cancel exact superseded owned run',command_exit=p.returncode)
(T/'finish-api-fixture10-cancel-superseded.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps(v))

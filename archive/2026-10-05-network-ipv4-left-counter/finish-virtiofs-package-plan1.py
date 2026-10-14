#!/usr/bin/env python3
import datetime,json,os,pathlib,subprocess,sys,hashlib
TRACK=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
G='725c325e8b4971931e5d16df86bafa8584358ecb'
NIX='/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix'
gate=json.loads((TRACK/'finish-virtiofs-review1-acceptance.json').read_text());assert gate['source_gate_complete'] and gate['exported_evidence_direct_fix_verified'] and gate['k']==G
env={k:os.environ[k] for k in ['HOME','USER','LOGNAME','XDG_RUNTIME_DIR'] if k in os.environ}
env['PATH']=str(pathlib.Path(NIX).parent)+':/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin:/run/current-system/sw/bin'
env['LANG']='C.UTF-8'
env['NIX_CONFIG']='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 1\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n'
argv=[NIX,'build','--dry-run','--no-link','--no-write-lock-file','github:vpsfreecz/vpsfree-kb-contracts/'+G+'#runtime-verify']
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
paths=[pathlib.Path('/tmp/finish-virtiofs-package-plan1.'+x) for x in ['stdout','stderr']]
handles=[]
try:
 for p in paths:handles.append(os.fdopen(os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600),'wb'))
 result=subprocess.run(argv,cwd='/home/aither',env=env,input=b'',stdout=handles[0],stderr=handles[1],close_fds=True)
finally:
 for f in handles:f.close()
record={'schema':1,'generator':G,'argv':argv,'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':result.returncode,'scope':'Exact corrected verifier package dry-run; no realization/image/guest/check/CI/lifecycle operation','evidence':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
output=TRACK/'finish-virtiofs-package-plan1.json'
with output.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'exit_code':result.returncode,'record':str(output),'logs':[str(p) for p in paths]}));sys.exit(result.returncode)

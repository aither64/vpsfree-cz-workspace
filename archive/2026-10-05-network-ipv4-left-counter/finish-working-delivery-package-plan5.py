from pathlib import Path
from datetime import datetime,timezone
import subprocess,time,json,hashlib
root=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
name='finish-working-delivery-package-plan5'
argv=['/nix/store/iirndnicd13h4zjr8xwwj8hq2cghpfjn-nix-2.34.8/bin/nix','build','--dry-run','--no-link','--no-write-lock-file','github:vpsfreecz/vpsfree-kb-contracts/b5e39e6fe9b44d2c31800dce75ad287d85981844#runtime-verify']
stdout=root/(name+'.stdout');stderr=root/(name+'.stderr');receipt=root/(name+'.json')
assert not any(p.exists() for p in (stdout,stderr,receipt))
begin=datetime.now(timezone.utc).isoformat();clock=time.monotonic()
with stdout.open('xb') as out,stderr.open('xb') as err:
 result=subprocess.run(argv,cwd=root,stdout=out,stderr=err)
d={'argv':argv,'cwd':str(root),'start_utc':begin,'end_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-clock,'native_exit_status':result.returncode,'scope':'immutable tool-package dry-run; no guest config/image/kernel/VM construction'}
for kind,path in [('stdout',stdout),('stderr',stderr)]:
 d[kind+'_path']=str(path);d[kind+'_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
receipt.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'native_exit_status':result.returncode,'elapsed_seconds':d['elapsed_seconds'],'receipt':str(receipt)}))
raise SystemExit(result.returncode)

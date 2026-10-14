from pathlib import Path
from datetime import datetime,timezone
import subprocess,time,json,hashlib,os,stat
root=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
name='finish-working-delivery-package-realize6'
link=Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-working-package6')
assert not link.exists() and not link.is_symlink()
s=link.parent.lstat();assert stat.S_ISDIR(s.st_mode) and s.st_uid==os.getuid()
argv=['/nix/store/iirndnicd13h4zjr8xwwj8hq2cghpfjn-nix-2.34.8/bin/nix','build','--no-write-lock-file','--json','--max-jobs','1','--cores','1','--out-link',str(link),'github:vpsfreecz/vpsfree-kb-contracts/d0b4f40708cc8b59aab7c91ae05fba695abc233c#runtime-verify']
stdout=root/(name+'.stdout');stderr=root/(name+'.stderr');receipt=root/(name+'.json')
assert not any(p.exists() for p in (stdout,stderr,receipt))
begin=datetime.now(timezone.utc).isoformat();clock=time.monotonic()
with stdout.open('xb') as out,stderr.open('xb') as err:
 result=subprocess.run(argv,cwd=root,stdout=out,stderr=err)
d={'argv':argv,'cwd':str(root),'out_link':str(link),'start_utc':begin,'end_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-clock,'native_exit_status':result.returncode,'scope':'reviewed immutable tool wrappers only; no guest config/image/kernel/VM/recovery/reset'}
for kind,path in [('stdout',stdout),('stderr',stderr)]:
 d[kind+'_path']=str(path);d[kind+'_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
receipt.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'native_exit_status':result.returncode,'elapsed_seconds':d['elapsed_seconds'],'receipt':str(receipt)}))
raise SystemExit(result.returncode)

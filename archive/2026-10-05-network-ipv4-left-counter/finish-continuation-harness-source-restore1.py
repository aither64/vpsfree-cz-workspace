from pathlib import Path
import json,subprocess,hashlib,os,datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
N='/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix'
S='/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix-store'
G='/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin'
ref='git+ssh://git@github.com/vpsfreecz/vpsfree-kb-contracts.git?rev=8e1804afce64ebe63cf623f098cf1a4032ca37e8'
expected=json.loads((T/'finish-fixture-tcp-selection-source-metadata1.json').read_text())
env=dict(os.environ);env['PATH']=G+':'+str(Path(N).parent)+':'+env.get('PATH','')
with (T/'finish-continuation-harness-source-restore1-metadata.json').open('xb')as out,(T/'finish-continuation-harness-source-restore1.stderr').open('xb')as err:
 r=subprocess.run([N,'flake','metadata','--refresh','--json',ref],stdout=out,stderr=err,env=env)
if r.returncode:raise SystemExit(r.returncode)
actual=json.loads((T/'finish-continuation-harness-source-restore1-metadata.json').read_text())
assert actual['path']==expected['path']and actual['revision']==expected['revision']and actual['locked']['narHash']==expected['locked']['narHash']
assert Path(actual['path']).is_dir()
root=Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14-public-continuation1/harness-source')
assert not root.exists()and not root.is_symlink()
with (T/'finish-continuation-harness-source-restore1-root.stdout').open('xb')as out,(T/'finish-continuation-harness-source-restore1-root.stderr').open('xb')as err:
 r=subprocess.run([S,'--add-root',str(root),'--indirect','--realise',actual['path']],stdout=out,stderr=err,env=env)
if r.returncode:raise SystemExit(r.returncode)
assert root.is_symlink()and str(root.resolve())==actual['path']
proof={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'revision':actual['revision'],'source':actual['path'],'narHash':actual['locked']['narHash'],'gc_root':str(root),'root_target_exact':True,'fetch_exit':0,'root_exit':0,'command':'Exact published Git-flake metadata source fetch and root existing source; no package/guest/image derivation build, evaluation test, VM or lifecycle operation.'}
with(T/'finish-continuation-harness-source-restore1.json').open('x')as f:json.dump(proof,f,indent=2);f.write('\n')
print(json.dumps(proof))

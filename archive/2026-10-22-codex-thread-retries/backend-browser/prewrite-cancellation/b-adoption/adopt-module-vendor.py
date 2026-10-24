
from pathlib import Path
import json, subprocess, time, os
repo=Path.cwd(); out=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-browser/prewrite-cancellation/b-adoption')
version='v0.0.0-20261024144044-11ec57d2203f'
def run(name, argv, cwd=repo):
    before=time.monotonic()
    result=subprocess.run(argv,cwd=cwd,capture_output=True)
    (out/(name+'.stdout')).write_bytes(result.stdout); (out/(name+'.stderr')).write_bytes(result.stderr)
    (out/(name+'.json')).write_text(json.dumps({'argv':argv,'cwd':str(cwd),'exit':result.returncode,'elapsed':time.monotonic()-before},indent=2)+'\n')
    if result.returncode: raise SystemExit(name+' failed; preserved raw logs')
    return result.stdout
run('module-edit',['go','mod','edit','-require=github.com/aither64/codex-web@'+version],repo/'portal')
mod=json.loads(run('module-download',['go','mod','download','-json','github.com/aither64/codex-web@'+version],repo/'portal'))
assert mod['Version']==version and mod['Sum']=='h1:cod93lovFHu5adtEqQy7QyE1E5YIFJrTkCnjB3phFgw=' and mod['GoModSum']=='h1:SfoFFfEnXQusGm701eWJpCbrkwia5g1biF5KD9RIqr0=',mod
run('module-tidy',['go','mod','tidy'],repo/'portal')
run('pin-check',['bash','nix/check-codex-web-pin.sh','portal/go.mod',version,'jq'])
vendor=Path('/tmp/codex-thread-retries-vendor-11ec57d2203f-b-adoption')
assert not vendor.exists(), 'refuse reuse of existing vendor output'
run('module-vendor',['go','mod','vendor','-o',str(vendor)],repo/'portal')
hash_value=run('vendor-hash',['nix','hash','path','--sri',str(vendor)]).decode().strip()
assert hash_value.startswith('sha256-')
p=repo/'nix/workspace-portal.nix'; old='sha256-bNeFZMHChen0znapzj7liBwO6YluoxWeZQUO35rVOHc='
s=p.read_text(); assert s.count(old)==1; p.write_text(s.replace(old,hash_value))
print(json.dumps({'module':mod,'vendorDirectory':str(vendor),'vendorHash':hash_value}))

"""Guarded public read-only guest mount observation for the retained update."""
import datetime, hashlib, json, os, pathlib, shlex, subprocess, sys
os.umask(0o077)
T = pathlib.Path(__file__).resolve().parent
prep = json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text())
packet = json.loads(pathlib.Path(prep['packet_path']).read_text())
root = pathlib.Path(packet['campaign_root'])
selection = json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text())['selection']
before = json.loads((root/'accepted-runtime.json').read_text())
context = root.parent/'update-store-mount-observation5'
context.mkdir(mode=0o700)
closure = before['provenance']['machine_toplevels']['services']
identity = pathlib.Path(closure)/'etc/vpsfree-kb-capture.json'
assert json.loads(identity.read_text()) == before['provenance']['guest_identity']
guard = 'set -eu\ntest "$(sha256sum /etc/vpsfree-kb-capture.json | cut -d " " -f 1)" = '+hashlib.sha256(identity.read_bytes()).hexdigest()+'\ntest "$(readlink -f /run/current-system)" = '+shlex.quote(closure)+'\n'
script = guard + '''findmnt --json --target / --output TARGET,FSTYPE,SOURCE,OPTIONS,FSROOT
findmnt --json --target /nix/store --output TARGET,FSTYPE,SOURCE,OPTIONS,FSROOT
findmnt --json --target /nix/var/nix/db --output TARGET,FSTYPE,SOURCE,OPTIONS,FSROOT
'''
argv = [selection['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state'),'ssh','same-slug','services','--','sh','-s']
with (context/'stdout').open('xb') as out, (context/'stderr').open('xb') as err:
    result = subprocess.run(argv, input=script.encode(), stdout=out, stderr=err, env=packet['environment'], cwd='/home/aither')
mounts = []
if result.returncode == 0:
    raw = (context/'stdout').read_text(); decoder = json.JSONDecoder()
    while raw.strip():
        value, end = decoder.raw_decode(raw.lstrip()); raw = raw.lstrip()[end:]
        assert list(value) == ['filesystems'] and len(value['filesystems']) == 1
        fs = value['filesystems'][0]
        assert set(fs) == {'target','fstype','source','options','fsroot'}
        mounts.append(fs)
    assert len(mounts) == 3
record = {'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_exit_code':result.returncode,'mounts':mounts,'original_source_ids':{k:before[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256')},'candidate_generator':prep['generator'],'stdout_sha256':hashlib.sha256((context/'stdout').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((context/'stderr').read_bytes()).hexdigest(),'scope':'Guest identity/current-system guarded public read-only findmnt. No remount/config/import/update continuation/capture.'}
for p in (context/'proof.json',T/'finish-working-delivery-update-store-mount-observation5.json'):
    with p.open('x') as f: json.dump(record,f,indent=2); f.write('\n')
print(json.dumps({'native_exit_code':result.returncode,'mounts':mounts}),flush=True)
sys.exit(result.returncode)

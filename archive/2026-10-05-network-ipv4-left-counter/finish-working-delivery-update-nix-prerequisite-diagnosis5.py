import datetime,hashlib,json,os,pathlib,shlex,subprocess,sys
os.umask(0o077);T=pathlib.Path(__file__).resolve().parent
prep=json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text());packet=json.loads(pathlib.Path(prep['packet_path']).read_text());root=pathlib.Path(packet['campaign_root'])
a=json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text());s=a['selection'];before=json.loads((root/'accepted-runtime.json').read_text())
context=root.parent/'update-nix-prerequisite-diagnosis5';context.mkdir(mode=0o700)
closure=before['provenance']['machine_toplevels']['services'];identity=pathlib.Path(closure)/'etc/vpsfree-kb-capture.json';assert json.loads(identity.read_text())==before['provenance']['guest_identity']
guard='set -eu\ntest "$(sha256sum /etc/vpsfree-kb-capture.json | cut -d " " -f 1)" = '+hashlib.sha256(identity.read_bytes()).hexdigest()+'\ntest "$(readlink -f /run/current-system)" = '+shlex.quote(closure)+'\n'
script=guard+'''if command -v nix >/dev/null 2>&1; then printf 'nix_available=1\n'; else printf 'nix_available=0\n'; fi
if command -v nix-store >/dev/null 2>&1; then printf 'nix_store_available=1\n'; else printf 'nix_store_available=0\n'; fi
if test -w /nix/store; then printf 'store_writable=1\n'; else printf 'store_writable=0\n'; fi
if test -w /nix/var/nix/db; then printf 'database_writable=1\n'; else printf 'database_writable=0\n'; fi
if nix --version >/dev/null 2>&1; then printf 'nix_version_status=0\n'; else printf 'nix_version_status=%s\n' "$?"; fi
if nix path-info --recursive --json "$1" >/dev/null 2>&1; then printf 'plain_path_info_status=0\n'; else printf 'plain_path_info_status=%s\n' "$?"; fi
if nix --extra-experimental-features nix-command path-info --recursive --json "$1" >/dev/null 2>&1; then printf 'explicit_feature_path_info_status=0\n'; else printf 'explicit_feature_path_info_status=%s\n' "$?"; fi
'''
argv=[s['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state'),'ssh','same-slug','services','--','sh','-s','--',closure]
with (context/'stdout').open('xb') as o,(context/'stderr').open('xb') as e:
 result=subprocess.run(argv,input=script.encode(),stdout=o,stderr=e,env=packet['environment'],cwd='/home/aither')
raw=(context/'stdout').read_text();values={}
if result.returncode==0:
 for line in raw.splitlines():
  k,v=line.split('=',1);assert v.isdigit();values[k]=int(v)
record={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_exit_code':result.returncode,'values':values,'original_source_ids':{k:before[k] for k in ['instance_id','run_id','artifact_id','artifact_sha256']},'candidate_generator':prep['generator'],'stdout_sha256':hashlib.sha256((context/'stdout').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((context/'stderr').read_bytes()).hexdigest(),'scope':'Guarded read-only ordinary public SSH prerequisite diagnosis; plain versus explicit nix-command path-info. No guest config/store/credential change, import/update retry or capture.'}
(context/'proof.json').write_text(json.dumps(record,indent=2)+'\n');(T/'finish-working-delivery-update-nix-prerequisite-diagnosis5.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'native_exit_code':result.returncode,'values':values}),flush=True);sys.exit(result.returncode)

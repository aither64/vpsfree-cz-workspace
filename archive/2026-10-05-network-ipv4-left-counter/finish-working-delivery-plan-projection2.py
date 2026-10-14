#!/usr/bin/env python3
"""Project public immutable planning fields only; no instance/credential preparation."""
import datetime,hashlib,json,os,pathlib,subprocess,sys
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
os.umask(0o077)
a=json.loads((T/'finish-working-delivery-package-realize2-acceptance.json').read_text())
c=json.loads((T/'finish-working-delivery-private-config2.json').read_text())
assert a['accepted'] and a['generator']==c['generator']
s=a['selection'];private=pathlib.Path(c['private_parent']);logs=private/'planning';logs.mkdir(mode=0o700)
config=pathlib.Path(c['configuration']['path']);assert hashlib.sha256(config.read_bytes()).hexdigest()==c['configuration']['sha256']
nix=next(str(pathlib.Path(p)/'nix') for p in s['path'].split(':') if pathlib.Path(p,'nix').is_file())
env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ}
env.update(PATH=s['path'],LANG='C.UTF-8',TMPDIR=str(logs),NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],VPSADMIN_DEVCLUSTER_SLUG='same-slug',VPSADMIN_DEVCLUSTER_TOPOLOGY='single',VPSADMIN_DEVCLUSTER_NETWORK='local',VPSADMIN_DEVCLUSTER_CONFIG_FILE=str(config),NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 1\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
apply="""plan: { machines = builtins.mapAttrs (_: machine: { inherit (machine) spin memory cpus kernel initrd toplevel disks; kernelOutput = builtins.dirOf machine.kernel; kernelContext = builtins.getContext machine.kernel; toplevelContext = builtins.getContext (toString machine.toplevel); } // (if machine ? diskImage then { inherit (machine) diskImage; imageContext = builtins.getContext machine.diskImage; } else {})) plan.machines; }"""
argv=[nix,'eval','--impure','--no-write-lock-file','--json','path:'+a['source']+'#runtimePlan','--apply',apply]
record={'schema':1,'generator':a['generator'],'metadata_sha256':a['metadata_sha256'],'source':a['source'],'configuration_sha256':c['configuration']['sha256'],'argv':argv,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Public runtimePlan projection only; placeholders are not final credentials, instance, accepted artifact or guest closures.'}
with (logs/'projection.stdout').open('xb') as out,(logs/'projection.stderr').open('xb') as err:r=subprocess.run(argv,cwd='/home/aither',env=env,stdout=out,stderr=err)
record['exit_code']=r.returncode
if r.returncode==0:
 value=json.loads((logs/'projection.stdout').read_text());m=value['machines'];assert sorted(m)==['node1','services'];assert [m[k]['memory'] for k in sorted(m)]==[2048,2048];assert m['node1']['disks'][0]['size']=='8G';record['projection']=value
record['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();record['evidence']={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [logs/'projection.stdout',logs/'projection.stderr']}
with (T/'finish-working-delivery-plan-projection2.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'exit_code':r.returncode,'receipt':'finish-working-delivery-plan-projection2.json'}));sys.exit(r.returncode)

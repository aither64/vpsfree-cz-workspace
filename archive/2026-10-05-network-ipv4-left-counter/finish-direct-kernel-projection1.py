#!/usr/bin/env python3
import datetime,hashlib,json,os,pathlib,subprocess,sys
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');a=json.loads((T/'finish-direct-package-realize1-acceptance.json').read_text()); c=json.loads((T/'finish-direct-private-configs1.json').read_text());s=a['selection'];private=pathlib.Path(c['private_parent']);logs=private/'kernel-planning';logs.mkdir(mode=0o700)
assert a['accepted'] and a['generator']=='ab09bd437b310f57e4ff2453ec0432555d85eaca'
nix=next(str(pathlib.Path(p)/'nix') for p in s['path'].split(':') if pathlib.Path(p,'nix').is_file())
env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ};env.update(PATH=s['path'],LANG='C.UTF-8',TMPDIR=str(logs),NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],VPSADMIN_DEVCLUSTER_SLUG='same-slug',VPSADMIN_DEVCLUSTER_TOPOLOGY='single',VPSADMIN_DEVCLUSTER_NETWORK='local',NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 4\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
record={'schema':1,'generator':a['generator'],'metadata_sha256':a['metadata_sha256'],'source':a['source'],'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Targeted public kernel-only runtimePlan projection; no full config/image realization, source check or fabricated instance identity.','commands':[]}
for cfg in c['configurations']:
 name=cfg['name'];env['VPSADMIN_DEVCLUSTER_CONFIG_FILE']=cfg['path'];assert hashlib.sha256(pathlib.Path(cfg['path']).read_bytes()).hexdigest()==cfg['sha256']
 argv=[nix,'eval','--impure','--no-write-lock-file','--json','path:'+a['source']+'#runtimePlan','--apply','plan: builtins.mapAttrs (_: machine: { inherit (machine) spin kernel; kernelOutput = builtins.dirOf machine.kernel; derivationContext = builtins.getContext machine.kernel; }) plan.machines']
 with (logs/(name+'.stdout')).open('xb') as out,(logs/(name+'.stderr')).open('xb') as err:result=subprocess.run(argv,cwd='/home/aither',env=env,stdout=out,stderr=err)
 item={'configuration':name,'configuration_sha256':cfg['sha256'],'argv':argv,'exit_code':result.returncode,'evidence':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [logs/(name+'.stdout'),logs/(name+'.stderr')]}}
 if result.returncode==0:item['projection']=json.loads((logs/(name+'.stdout')).read_text())
 record['commands'].append(item)
 if result.returncode:break
record['exit_code']=record['commands'][-1]['exit_code'];record['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (T/'finish-direct-kernel-projection1.json').open('x') as out:json.dump(record,out,indent=2);out.write('\n')
print(json.dumps({'exit_code':record['exit_code'],'receipt':str(T/'finish-direct-kernel-projection1.json')}));sys.exit(record['exit_code'])

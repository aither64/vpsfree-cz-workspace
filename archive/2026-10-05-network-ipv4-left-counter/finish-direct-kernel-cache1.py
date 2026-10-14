#!/usr/bin/env python3
import datetime,hashlib,json,os,pathlib,subprocess,sys
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');a=json.loads((T/'finish-direct-package-realize1-acceptance.json').read_text());c=json.loads((T/'finish-direct-private-configs1.json').read_text());p=json.loads((T/'finish-direct-kernel-projection2.json').read_text());assert p['exit_code']==0
projections=[r['projection'] for r in p['commands']];assert all(r==projections[0] for r in projections)
s=a['selection'];logs=pathlib.Path(c['private_parent'])/'kernel-cache1';logs.mkdir(mode=0o700)
nix=next(str(pathlib.Path(path)/'nix') for path in s['path'].split(':') if pathlib.Path(path,'nix').is_file())
env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ};env.update(PATH=s['path'],LANG='C.UTF-8',TMPDIR=str(logs),NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 4\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
record={'schema':1,'generator':a['generator'],'projection_sha256':hashlib.sha256((T/'finish-direct-kernel-projection2.json').read_bytes()).hexdigest(),'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Exact observed guest-kernel dry-run and cache NarInfo queries; no builds or VM launch.','commands':[]}
def run(name,argv):
 with (logs/(name+'.stdout')).open('xb') as out,(logs/(name+'.stderr')).open('xb') as err:r=subprocess.run(argv,cwd='/home/aither',env=env,stdout=out,stderr=err)
 item={'name':name,'argv':argv,'exit_code':r.returncode,'evidence':{str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in [logs/(name+'.stdout'),logs/(name+'.stderr')]}}
 if r.returncode==0:item['result']=json.loads((logs/(name+'.stdout')).read_text())
 record['commands'].append(item);return r.returncode
selectors=[]
for machine,value in projections[0].items():
 ctx=value['derivationContext'];assert len(ctx)==1;drv,entry=next(iter(ctx.items()));assert entry['outputs']==['out'];selectors.append(drv+'^out')
code=run('dry-run',[nix,'build','--dry-run','--no-link','--json',*selectors])
if code==0:
 for machine,value in projections[0].items():
  cache='https://cache.vpsadminos.org' if machine=='node1' else 'https://cache.nixos.org'
  run(machine+'-cache',[nix,'path-info','--json','--store',cache,value['kernelOutput']])
record['exit_code']=code;record['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (T/'finish-direct-kernel-cache1.json').open('x') as out:json.dump(record,out,indent=2);out.write('\n')
print(json.dumps({'dry_run_exit_code':code,'query_exit_codes':[r['exit_code'] for r in record['commands']],'receipt':str(T/'finish-direct-kernel-cache1.json')}));sys.exit(code)

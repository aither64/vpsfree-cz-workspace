#!/usr/bin/env python3
import datetime,hashlib,json,os,pathlib,subprocess,sys,time
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');a=json.loads((T/'finish-direct-package-realize1-acceptance.json').read_text());c=json.loads((T/'finish-direct-private-configs1.json').read_text());p=json.loads((T/'finish-direct-kernel-projection2.json').read_text());facts=json.loads((T/'finish-direct-kernel-cache1.json').read_text());assert facts['exit_code']==0
s=a['selection'];private=pathlib.Path(c['private_parent']);logs=private/'kernel-realize1';logs.mkdir(mode=0o700)
nix=next(str(pathlib.Path(path)/'nix') for path in s['path'].split(':') if pathlib.Path(path,'nix').is_file()); env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ};env.update(PATH=s['path'],LANG='C.UTF-8',TMPDIR=str(logs),NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 0\ncores = 4\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
record={'schema':1,'generator':a['generator'],'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Targeted exact kernel substitution only with local builders disabled; no CI/VM.','commands':[]}
for machine,value in p['commands'][0]['projection'].items():
 drv=next(iter(value['derivationContext']));link=private/('kernel-'+machine);assert not os.path.lexists(link)
 argv=[nix,'build','--max-jobs','0','--json','--out-link',str(link),drv+'^out']
 with (logs/(machine+'.stdout')).open('xb') as out,(logs/(machine+'.stderr')).open('xb') as err:r=subprocess.run(argv,cwd='/home/aither',env=env,stdout=out,stderr=err)
 item={'machine':machine,'argv':argv,'exit_code':r.returncode,'gc_root':str(link),'evidence':{str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in [logs/(machine+'.stdout'),logs/(machine+'.stderr')]}}
 if r.returncode==0:
  assert link.resolve()==pathlib.Path(value['kernelOutput']); assert pathlib.Path(value['kernel']).is_file();item['result']=json.loads((logs/(machine+'.stdout')).read_text())
 record['commands'].append(item)
 if r.returncode:break
record['exit_code']=record['commands'][-1]['exit_code'];record['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (T/'finish-direct-kernel-realize1.json').open('x') as out:json.dump(record,out,indent=2);out.write('\n')
print(json.dumps({'exit_code':record['exit_code'],'receipt':str(T/'finish-direct-kernel-realize1.json')}));sys.exit(record['exit_code'])

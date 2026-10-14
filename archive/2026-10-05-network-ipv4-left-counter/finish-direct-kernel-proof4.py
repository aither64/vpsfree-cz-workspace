import pathlib,json,hashlib,subprocess,os,datetime,sys
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');a=json.loads((T/'finish-direct-package-realize3-acceptance.json').read_text());c=json.loads((T/'finish-direct-private-configs3.json').read_text());p=json.loads((T/'finish-direct-kernel-projection4.json').read_text());historical=json.loads((T/'finish-direct-kernel-projection2.json').read_text());assert p['exit_code']==0 and len(p['commands'])==3 and p['generator']==a['generator']
values=[q['projection'] for q in p['commands']];assert all(q==values[0] for q in values) and values[0]==historical['commands'][0]['projection']
for q in p['commands']:
 for f,h in q['evidence'].items():assert hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()==h
s=a['selection'];logs=pathlib.Path(c['private_parent'])/'kernel-proof4';logs.mkdir(mode=0o700);nix=next(str(pathlib.Path(q)/'nix') for q in s['path'].split(':') if pathlib.Path(q,'nix').is_file());env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ};env.update(PATH=s['path'],LANG='C.UTF-8',NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 0\ncores = 4\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
record={'schema':1,'generator':a['generator'],'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Fresh exact kernel derivation/output and local closure facts, public dry-run only; no kernel build or guest launch.','projection_sha256':hashlib.sha256((T/'finish-direct-kernel-projection4.json').read_bytes()).hexdigest(),'commands':[]}
def run(name,args):
 with (logs/(name+'.stdout')).open('xb') as out,(logs/(name+'.stderr')).open('xb') as err:r=subprocess.run(args,cwd='/home/aither',env=env,stdout=out,stderr=err)
 q={'name':name,'argv':args,'exit_code':r.returncode,'evidence':{str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in [logs/(name+'.stdout'),logs/(name+'.stderr')]}}
 if r.returncode==0:q['result']=json.loads((logs/(name+'.stdout')).read_text())
 record['commands'].append(q);return r.returncode,q
selectors=[];outputs=[];code=0
for machine,value in values[0].items():
 drv=next(iter(value['derivationContext']));code,q=run(machine+'-derivation',[nix,'derivation','show',drv])
 if code:break
 assert q['result']['version']==4; derivation=q['result']['derivations'][pathlib.Path(drv).name];declared=derivation['outputs'];selected=[derivation['env'][name] for name in declared];assert all(pathlib.Path(derivation['env'][name]).name==entry['path'] for name,entry in declared.items());assert value['kernelOutput'] in selected;outputs+=selected;selectors.append(drv+'^*')
if not code:code,q=run('all-local-closures',[nix,'path-info','--recursive','--json',*outputs])
if not code:code,q=run('all-output-dry-run',[nix,'build','--dry-run','--no-link','--json',*selectors])
record.update(exit_code=code,outputs=sorted(set(outputs)),finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
with (T/'finish-direct-kernel-proof4.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (T/'finish-direct-kernel-proof4.exit').open('x') as f:f.write(str(code)+'\n')
print(json.dumps({'exit_code':code,'receipt':str(T/'finish-direct-kernel-proof4.json'),'outputs':record['outputs']}));sys.exit(code)

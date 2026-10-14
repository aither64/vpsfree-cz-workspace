#!/usr/bin/env python3
"""Observe exact projected kernels and builder memory through public Nix commands."""
import datetime,hashlib,json,os,pathlib,re,shlex,subprocess,sys
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
os.umask(0o077)
a=json.loads((T/'finish-working-delivery-package-realize2-acceptance.json').read_text());c=json.loads((T/'finish-working-delivery-private-config2.json').read_text());p=json.loads((T/'finish-working-delivery-plan-projection2.json').read_text());assert p['exit_code']==0 and p['generator']==a['generator']
s=a['selection'];logs=pathlib.Path(c['private_parent'])/'kernel-builder-proof';logs.mkdir(mode=0o700);nix=next(str(pathlib.Path(q)/'nix') for q in s['path'].split(':') if pathlib.Path(q,'nix').is_file());env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ};env.update(PATH=s['path'],LANG='C.UTF-8',NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 1\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
r={'schema':1,'generator':a['generator'],'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Actual projected kernel derivations/all-output local closure and dry-run proof; native builder memory inspection. No realization, final guest closure or payload-fit proof.','commands':[]}
def run(name,args):
 with (logs/(name+'.stdout')).open('xb') as out,(logs/(name+'.stderr')).open('xb') as err:q=subprocess.run(args,cwd='/home/aither',env=env,stdout=out,stderr=err)
 item={'name':name,'argv':args,'exit_code':q.returncode,'evidence':{str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in [logs/(name+'.stdout'),logs/(name+'.stderr')]}};r['commands'].append(item);assert q.returncode==0,name
 return json.loads((logs/(name+'.stdout')).read_text()),(logs/(name+'.stderr')).read_text()
def record(drv,name):
 v,_=run(name,[nix,'derivation','show',drv]);assert v['version']==4 and list(v['derivations'])==[pathlib.Path(drv).name];return v['derivations'][pathlib.Path(drv).name]
m=p['projection']['machines'];selectors=[];outputs=[];drvs=[]
for machine,value in m.items():
 context=value['kernelContext'];assert len(context)==1;drv=next(iter(context));d=record(drv,machine+'-kernel-derivation');chosen=[d['env'][name] for name in d['outputs']];assert all(pathlib.Path(d['env'][name]).name==entry['path'] for name,entry in d['outputs'].items());assert value['kernelOutput'] in chosen;outputs+=chosen;selectors.append(drv+'^*');drvs.append(drv)
local,_=run('kernel-local-closures',[nix,'path-info','--recursive','--json',*sorted(set(outputs))]);_,native=run('kernel-all-output-dry-run',[nix,'build','--dry-run','--no-link','--json',*selectors]);assert not any(re.search(r'^\s+'+re.escape(drv)+r'\s*$',native,re.M) for drv in drvs),'kernel compilation planned'
ctx=m['services']['imageContext'];images=[d for d in ctx if d.endswith('.drv')];assert len(images)==1;d=record(images[0],'services-image-derivation');tokens=shlex.split(d['structuredAttrs']['env']['QEMU_OPTS']);options=lambda flag:[tokens[i+1] for i,t in enumerate(tokens[:-1]) if t==flag];assert options('-m')==['2048'];objects=[x for x in options('-object') if x.startswith('memory-backend-')];backends=[x for machine in options('-machine') for x in machine.split(',') if x.startswith('memory-backend=')];assert objects==['memory-backend-memfd,id=mem,size=2048M,share=on'] and backends==['memory-backend=mem']
r.update(exit_code=0,kernel_outputs=sorted(set(outputs)),kernel_derivations=drvs,kernel_map={k:v['kernel'] for k,v in m.items()},builder_memory_mib=2048,image_derivation=images[0],finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
with (T/'finish-working-delivery-kernel-builder-proof2.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'exit_code':0,'receipt':'finish-working-delivery-kernel-builder-proof2.json','builder_memory_mib':2048,'kernel_outputs':r['kernel_outputs']}))

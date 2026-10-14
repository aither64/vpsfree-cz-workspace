#!/usr/bin/env python3
import pathlib,json,os,subprocess,hashlib,datetime
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');os.umask(0o077)
a=json.loads((T/'finish-working-delivery-package-realize3-acceptance.json').read_text());c=json.loads((T/'finish-working-delivery-private-config3.json').read_text());p=json.loads((T/'finish-working-delivery-closure-plan3.json').read_text());assert p['exit_code']==0 and not p['kernel_derivations_to_build']
s=a['selection'];logs=pathlib.Path(c['private_parent'])/'missing-closure-facts';logs.mkdir(mode=0o700)
nix=next(str(pathlib.Path(q)/'nix')for q in s['path'].split(':')if pathlib.Path(q,'nix').is_file());env={x:os.environ[x]for x in ['HOME','USER','LOGNAME','XDG_RUNTIME_DIR']if x in os.environ};env.update(PATH=s['path'],LANG='C.UTF-8',TMPDIR=str(logs),NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 1\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
records={};commands=[]
def query(paths,url,name):
 argv=[nix,'path-info','--json','--store',url,*paths]
 out=logs/(name+'.stdout');err=logs/(name+'.stderr')
 with out.open('xb')as o,err.open('xb')as e:q=subprocess.run(argv,cwd='/home/aither',env=env,stdout=o,stderr=e)
 commands.append({'argv':argv,'exit_code':q.returncode,'evidence':{str(f):hashlib.sha256(f.read_bytes()).hexdigest()for f in [out,err]}})
 try:value=json.loads(out.read_text())
 except json.JSONDecodeError:return
 if isinstance(value,list):value={r['path']:r for r in value if r is not None}
 for path,r in value.items():
  if r is not None:
   assert isinstance(r['narSize'],int)and r['narSize']>0
   records[path]={'path':path,'kind':'closure','nar_size':r['narSize'],'download_size':r.get('downloadSize'),'nar_hash':r.get('narHash'),'signatures':r.get('signatures',r.get('sigs',[])),'references':r.get('references',[]),'cache':url,'currently_local':pathlib.Path(path).exists()}
if p['fetched_paths']:query(p['fetched_paths'],'https://cache.nixos.org','nixos')
missing=[x for x in p['fetched_paths']if x not in records]
if missing:query(missing,'https://cache.vpsadminos.org','vpsadminos')
missing=[x for x in p['fetched_paths']if x not in records]
r={'schema':1,'generator':a['generator'],'configuration_sha256':c['configuration']['sha256'],'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':commands,'missing_facts':missing,'paths':[records[x]for x in p['fetched_paths']if x in records],'nar_bytes':sum(x['nar_size']for x in records.values()),'scope':'Read-only substituter path metadata under the selected cache configuration. Actual native fetch verifies trusted signatures; metadata availability alone is not a signature verification or realized closure certificate. No realization or guest operation.'}
with(T/'finish-working-delivery-missing-closure-facts3.json').open('x')as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'recorded_paths':len(records),'missing_fact_count':len(missing),'nar_bytes':r['nar_bytes'],'receipt':'finish-working-delivery-missing-closure-facts3.json'}));raise SystemExit(0 if not missing else 1)

#!/usr/bin/env python3
import pathlib,json,hashlib,os,subprocess,datetime,re
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');os.umask(0o077)
a=json.loads((T/'finish-working-delivery-package-realize3-acceptance.json').read_text());c=json.loads((T/'finish-working-delivery-private-config3.json').read_text());p=json.loads((T/'finish-working-delivery-plan-projection3.json').read_text());k=json.loads((T/'finish-working-delivery-kernel-builder-proof3.json').read_text());assert p['exit_code']==k['exit_code']==0
s=a['selection'];logs=pathlib.Path(c['private_parent'])/'closure-planning';logs.mkdir(mode=0o700)
nix=next(str(pathlib.Path(q)/'nix')for q in s['path'].split(':')if pathlib.Path(q,'nix').is_file());env={x:os.environ[x]for x in ['HOME','USER','LOGNAME','XDG_RUNTIME_DIR']if x in os.environ}
env.update(PATH=s['path'],LANG='C.UTF-8',TMPDIR=str(logs),NIX_SSL_CERT_FILE=s['certificates'],SSL_CERT_FILE=s['certificates'],VPSADMIN_DEVCLUSTER_SLUG='same-slug',VPSADMIN_DEVCLUSTER_TOPOLOGY='single',VPSADMIN_DEVCLUSTER_NETWORK='local',VPSADMIN_DEVCLUSTER_CONFIG_FILE=c['configuration']['path'],NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 1\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
selectors=[]
for value in p['projection']['machines'].values():
 for name in ['toplevelContext','imageContext']:
  if name not in value:continue
  for drv,context in value[name].items():
   assert drv.endswith('.drv') and context['outputs'];selectors.append(drv+'^'+','.join(context['outputs']))
argv=[nix,'build','--dry-run','--no-link','--no-write-lock-file','--impure','--json',*sorted(set(selectors)),'path:'+a['source']+'#runner']
with(logs/'dry-run.stdout').open('xb')as out,(logs/'dry-run.stderr').open('xb')as err:q=subprocess.run(argv,cwd='/home/aither',env=env,stdout=out,stderr=err)
record={'schema':1,'generator':a['generator'],'source':a['source'],'configuration_sha256':c['configuration']['sha256'],'argv':argv,'exit_code':q.returncode,'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Read-only exact runtimePlan-derived toplevel/image/runner construction plan. Default planning credentials/identity are NOT actual instance preparation; final actual closure/image attestation remains public-start obligation. No realization or guest launch.','evidence':{str(f):hashlib.sha256(f.read_bytes()).hexdigest()for f in [logs/'dry-run.stdout',logs/'dry-run.stderr']}}
if q.returncode==0:
 native=(logs/'dry-run.stderr').read_text();paths=re.findall(r'^\s+(/nix/store/[^\s]+)\s*$',native,re.M);record['planned_derivations']=[x for x in paths if x.endswith('.drv')];record['fetched_paths']=[x for x in paths if not x.endswith('.drv')];record['native_fetch_totals']=re.findall(r'these \d+ paths will be fetched \([^\n]+\)',native);record['kernel_derivations_to_build']=[x for x in record['planned_derivations']if re.search(r'-(?:linux-[0-9]|kernel)',pathlib.Path(x).name)]
 record['planning_outputs']=json.loads((logs/'dry-run.stdout').read_text())
with(T/'finish-working-delivery-closure-plan3.json').open('x')as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'exit_code':q.returncode,'planned_derivation_count':len(record.get('planned_derivations',[])),'fetched_path_count':len(record.get('fetched_paths',[])),'kernel_compile_plan':record.get('kernel_derivations_to_build'),'receipt':'finish-working-delivery-closure-plan3.json'}));raise SystemExit(q.returncode)

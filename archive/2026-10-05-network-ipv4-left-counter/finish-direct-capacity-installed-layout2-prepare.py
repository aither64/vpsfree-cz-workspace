import pathlib,json,hashlib,os,subprocess,datetime
T=pathlib.Path.cwd();a=json.loads((T/'finish-direct-package-realize2-acceptance.json').read_text());c=json.loads((T/'finish-direct-private-configs2.json').read_text());private=pathlib.Path(c['private_parent']);assert private.stat().st_mode&0o777==0o700;assert not pathlib.Path(c['campaign_root']).exists()
configs=[]
for q in c['configurations']:
 p=pathlib.Path(q['path']);assert p.stat().st_mode&0o777==0o600;assert hashlib.sha256(p.read_bytes()).hexdigest()==q['sha256'];configs.append(json.loads(p.read_text()))
prior=json.loads((T/'finish-direct-capacity-installed-layout1.json').read_text());value=json.loads(pathlib.Path(prior['private_receipt_path']).read_text());s=a['selection'];meta=json.loads(pathlib.Path(s['metadata']).read_text());plan=json.loads((T/'finish-direct-predecessor-plan2.json').read_text());assert plan['exit_code']==0
for p,h in plan['evidence'].items():assert hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()==h
outputs=json.loads((T/'finish-direct-predecessor-plan2.stdout').read_text());native=(T/'finish-direct-predecessor-plan2.stderr').read_text();assert '-linux-6.' not in native and '-linux-5.' not in native
assert len(outputs)==2
value['bindings']={'source':meta,'selection':s,'configurations':configs,'predecessor_ref':'github:vpsfreecz/vpsfree-kb-contracts/68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e','root':c['campaign_root'],'configuration_sha256':[q['sha256'] for q in c['configurations']]}
value['observed_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
for role,p in [('state_images',c['campaign_root']),('store','/nix/store'),('builder_scratch','/nix/var/nix/builds')]:
 existing=pathlib.Path(p)
 while not existing.exists():existing=existing.parent
 value['roles'][role]={'path':p,'device':existing.stat().st_dev,'mountpoint':subprocess.check_output(['findmnt','-n','-o','TARGET','-T',str(existing)],text=True).strip(),'fstype':subprocess.check_output(['findmnt','-n','-o','FSTYPE','-T',str(existing)],text=True).strip()}
assert len(set(v['device'] for v in value['roles'].values()))==1
fs=os.statvfs('/nix/store');free=fs.f_bavail*fs.f_frsize;G=1024**3;assert free>=(92+32+64)*G
retained=json.loads((T/'finish-direct-retained-growth1.json').read_text())
for disk in retained['disks']:
 st=pathlib.Path(disk['path']).stat();assert st.st_dev==disk['device'] and st.st_ino==disk['inode'] and st.st_size==disk['apparent_bytes']
value['build_plan']['assessment']='INSTALLED-LAYOUT ONLY: reviewed G6 verifier package is realized. Fresh exact immutable K68 runtime+metadata public dry-run passed with only source metadata/runtime wrapper construction, two signed cache substitutions of about 7.6 MiB unpacked, no kernel. Shared filesystem currently has '+str(free)+' bytes available. Protect full 92 GiB new eventual output growth, 32 GiB reserve (16 GiB host plus 16 GiB retained incomplete G4 sparse tank growth) and 64 GiB operator-assessed positive build headroom. Wrapper size and builder scratch are not mathematically bounded; 64 GiB is admission headroom, NOT scratch proof. No guest construction/start admitted by this receipt; refresh exact kernel/cache/closure evidence before isolation. Live reserve monitoring required; cancelling the owned child does not prove daemon cleanup.'
value['build_plan']['derivations']=[row['drvPath'] for row in outputs]
value['build_plan']['kernel_substitutions']=['Installed-layout phase only: fresh exact K68 public runtime+metadata dry-run exit0, native stderr SHA256 '+hashlib.sha256((T/'finish-direct-predecessor-plan2.stderr').read_bytes()).hexdigest()+'. Only two metadata/runtime wrapper derivations, no planned kernel; two substitutions have retained native signed cache NAR/download metadata. This is NOT guest-kernel cache proof.']
value['owned_output']={'allocated_bytes':0,'apparent_bytes':0};value['realized_paths']=list(dict.fromkeys([a['package'],s['runtime'],s['capture'],s['metadata']]+[row['outputs']['out'] for row in outputs if pathlib.Path(row['outputs']['out']).exists()]));value['missing_paths']=[{'path':p,'kind':'closure','nar_size':e['narSize'],'download_size':e['downloadSize']} for p,e in json.loads((T/'finish-direct-predecessor-cache2.stdout').read_text()).items()]
value['filesystems']=[{'device':value['roles']['store']['device'],'reserve_bytes':32*G,'build_headroom_bytes':64*G,'observed_available_bytes':free}]
p=private/'capacity-installed-layout2.json';fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
with os.fdopen(fd,'w') as f:json.dump(value,f,indent=2);f.write('\n')
public={'schema':1,'generator':a['generator'],'phase_scope':'installed-layout only; refresh before guests','private_receipt_path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'available_bytes':free,'reserve_bytes':32*G,'assessed_headroom_bytes':64*G,'scratch_bound':'unknown','old_g4_retained':True,'private_contents_exported':False}
with (T/'finish-direct-capacity-installed-layout2.json').open('x') as f:json.dump(public,f,indent=2);f.write('\n')
script=(T/'finish-direct-installed-layout1.py').read_text().replace('installed-layout1','installed-layout2').replace('realize1-acceptance','realize2-acceptance').replace('private-configs1','private-configs2').replace('ab09bd437b310f57e4ff2453ec0432555d85eaca',a['generator']).replace('free<16*1024**3','free<32*1024**3').replace("cancel='untouched host reserve lost'","cancel='host plus retained G4 sparse-growth reserve lost'")
with (T/'finish-direct-installed-layout2.py').open('x') as f:f.write(script)
print(json.dumps(public))

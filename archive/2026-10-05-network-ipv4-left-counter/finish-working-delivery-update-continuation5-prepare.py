"""Fresh admission for one exact already-built public journal continuation."""
import datetime, hashlib, json, os, pathlib, stat
os.umask(0o077)
T=pathlib.Path(__file__).resolve().parent
old=json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text())
packet=json.loads(pathlib.Path(old['packet_path']).read_text())
failure=json.loads((T/'finish-working-delivery-public-update5-failure-disposition.json').read_text())
operator=json.loads((T/'finish-working-delivery-update-guest-preparation5.json').read_text())
assert operator['complete'] and operator['native_exit_code']==0
root=pathlib.Path(packet['campaign_root']); directory=root/'state/clusters/same-slug'
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
journal=json.loads((directory/'update.json').read_text())
assert all(journal[k]==v for k,v in failure['journal'].items()) and journal['stage']=='preparing'
artifact=directory/('artifact-'+journal['artifact_id']+'.json')
assert sha(artifact)==failure['candidate_artifact_sha256']
assert sha(root/'config.json')==old['configuration_sha256']
assert sha(directory/'credentials/known_hosts')==old['known_hosts_sha256']
image=pathlib.Path(failure['candidate_image']['path']); st=image.lstat()
assert stat.S_ISREG(st.st_mode) and st.st_uid==0 and stat.S_IMODE(st.st_mode)==0o444 and st.st_size==8589934592
prior=json.loads((T/'finish-working-delivery-update-admission5-observation.json').read_text())
retained=[]; retained_growth=0
for row in prior['other_retained_disks']:
    p=pathlib.Path(row['path']); x=p.lstat()
    assert stat.S_ISREG(x.st_mode) and (x.st_dev,x.st_ino,x.st_size)==(row['device'],row['inode'],row['apparent_bytes'])
    immutable=str(p).startswith('/nix/store/')
    assert x.st_uid==(0 if immutable else os.getuid())
    growth=0 if immutable else max(0,x.st_size-x.st_blocks*512)
    retained_growth+=growth
    retained.append(dict(row,allocated_bytes=x.st_blocks*512,remaining_writable_growth_bytes=growth))
own=[]; own_growth=0
for row in prior['own_disks']:
    x=(directory/'disks'/row['name']).lstat()
    assert stat.S_ISREG(x.st_mode) and x.st_uid==os.getuid() and (x.st_dev,x.st_ino,x.st_size)==(row['device'],row['inode'],row['apparent_bytes'])
    growth=max(0,x.st_size-x.st_blocks*512);own_growth+=growth
    own.append(dict(row,allocated_bytes=x.st_blocks*512,remaining_writable_growth_bytes=growth))
G=1024**3;protected=retained_growth+own_growth+16*G
assessment=3*G;runway=G
fs=os.statvfs('/nix/store');free=fs.f_bavail*fs.f_frsize
ram=int(next(v for v in pathlib.Path('/proc/meminfo').read_text().splitlines() if v.startswith('MemAvailable:')).split()[1])*1024
shm=os.statvfs('/dev/shm');shm_free=shm.f_bavail*shm.f_frsize
assert all(pathlib.Path(p).stat().st_dev==st.st_dev for p in (root,'/nix/store','/nix/var/nix/builds'))
admitted=free>=protected+assessment+runway and ram>=6*G and shm_free>=5*G
observation={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'generator':old['generator'],'exact_journal':failure['journal'],'candidate_artifact_sha256':sha(artifact),'image':{'path':str(image),'device':st.st_dev,'inode':st.st_ino,'apparent_bytes':st.st_size,'allocated_bytes':st.st_blocks*512},'other_retained_disks':retained,'own_disks':own,'protected_obligations_bytes':protected,'additional_headroom_assessment_bytes':assessment,'unassigned_minimum_bytes':runway,'free_bytes':free,'required_bytes':protected+assessment+runway,'ram_available_bytes':ram,'shm_available_bytes':shm_free,'real_admission':admitted,'assessment':'Already-built candidate and existing writable disks are reused. No image/root/tank/build allocation is charged again. Actual allocated candidate bytes already reduce current availability. Retained writable growth and16GiB reserve unchanged; separately assess3GiB import/observation/scratch headroom with1GiB runway. Exact guest import capacity remains mandatory and unproved. No new pair/rebuild/config substitution.'}
with (T/'finish-working-delivery-update-continuation5-admission.json').open('x') as f:json.dump(observation,f,indent=2);f.write('\n')
assert admitted,'fresh continuation capacity refused; no context/service created'
context=root.parent/'public-update-continuation-context5';context.mkdir(mode=0o700)
packet.update(phase='exact-candidate-update-continuation',unit='kb-verify-network-counter-working5-public-update-continuation.service',context=str(context),reserve_bytes=protected+runway)
packet['bound_files'] += [{'path':str(artifact),'sha256':sha(artifact)},{'path':str(T/'finish-working-delivery-update-guest-preparation5.json'),'sha256':sha(T/'finish-working-delivery-update-guest-preparation5.json')}]
packet_path=context/'packet.json'
with packet_path.open('x') as f:json.dump(packet,f,indent=2);f.write('\n')
new=dict(old,at=observation['at'],phase=packet['phase'],unit=packet['unit'],context=str(context),packet_path=str(packet_path),packet_sha256=sha(packet_path),disk_required_bytes=observation['required_bytes'],real_admission=True,continuation_of=failure['native_result_sha256'],exact_journal=failure['journal'],guest_preparation_sha256=sha(T/'finish-working-delivery-update-guest-preparation5.json'),filesystem=observation,assessment=observation['assessment'])
with (T/'finish-working-delivery-update-continuation5-preparation.json').open('x') as f:json.dump(new,f,indent=2);f.write('\n')
print(json.dumps({'real_admission':True,'free_GiB':round(free/G,3),'required_GiB':round(observation['required_bytes']/G,3),'candidate':journal['artifact_id'],'new_image_or_pair':False}),flush=True)

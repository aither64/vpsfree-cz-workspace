"""Prepare captures only after accepted update proof and operator restoration."""
import datetime,hashlib,json,os,pathlib,stat,sys
os.umask(0o077)
T=pathlib.Path(__file__).resolve().parent
old=json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text())
post=json.loads((T/'finish-working-delivery-public-update5-proof.json').read_text())
restoration=json.loads((T/'finish-working-delivery-update-guest-restoration5.json').read_text())
assert post['complete'] and post['old_complete_process_receipt'] and post['public_member_api_php_and_lease']
assert restoration['complete'] and restoration['native_exit_code']==0 and restoration['source_ids']==post['source_ids']
packet=json.loads(pathlib.Path(old['packet_path']).read_text());root=pathlib.Path(packet['campaign_root'])
directory=root/'state/clusters/same-slug';sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert sha(root/'config.json')==old['configuration_sha256']
assert sha(directory/'credentials/known_hosts')==old['known_hosts_sha256']
prior=json.loads((T/'finish-working-delivery-update-continuation5-admission.json').read_text())
other=0
for row in prior['other_retained_disks']:
    p=pathlib.Path(row['path']);x=p.lstat();assert stat.S_ISREG(x.st_mode) and (x.st_dev,x.st_ino,x.st_size)==(row['device'],row['inode'],row['apparent_bytes'])
    if not str(p).startswith('/nix/store/'):other+=max(0,x.st_size-x.st_blocks*512)
own=0
for row in prior['own_disks']:
    x=(directory/'disks'/row['name']).lstat();assert stat.S_ISREG(x.st_mode) and x.st_uid==os.getuid() and (x.st_dev,x.st_ino,x.st_size)==(row['device'],row['inode'],row['apparent_bytes'])
    own+=max(0,x.st_size-x.st_blocks*512)
G=1024**3;protected=other+own+16*G
fs=os.statvfs('/nix/store');free=fs.f_bavail*fs.f_frsize
ram=int(next(v for v in pathlib.Path('/proc/meminfo').read_text().splitlines() if v.startswith('MemAvailable:')).split()[1])*1024
shm=os.statvfs('/dev/shm');shm_free=shm.f_bavail*shm.f_frsize
assert free>=protected+G and ram>=2*G and shm_free>=G,'fresh incremental capture admission refused'
context=root.parent/'operator-capture-working5';context.mkdir(mode=0o700)
output=context/'output';output.mkdir(mode=0o700)
export=context/'export'
packet.update(phase='standalone-bilingual-capture',unit='kb-verify-network-counter-working5-operator-capture.service',context=str(context),argv=[os.path.realpath(sys.executable),str(T/'finish-working-delivery-operator-capture-window5.py')],reserve_bytes=protected,minimum_host_ram_bytes=G,minimum_host_shm_bytes=G//2)
for p in (T/'finish-working-delivery-operator-capture-window5.py',T/'finish-working-delivery-fixture-resource-proof5.cjs',T/'finish-working-delivery-public-update5-proof.json',T/'finish-working-delivery-update-guest-restoration5.json'):
    packet['bound_files'].append({'path':str(p),'sha256':sha(p)})
packet_path=context/'packet.json'
with packet_path.open('x') as f:json.dump(packet,f,indent=2);f.write('\n')
prep=dict(old,at=datetime.datetime.now(datetime.timezone.utc).isoformat(),phase=packet['phase'],unit=packet['unit'],context=str(context),packet_path=str(packet_path),packet_sha256=sha(packet_path),output_root=str(output),export_root=str(export),typed_resource_script=str(T/'finish-working-delivery-fixture-resource-proof5.cjs'),other_retained_growth_bytes=other,real_admission=True,source_ids=post['source_ids'],host={'free_bytes':free,'protected_obligations_bytes':protected,'capture_headroom_bytes':G,'ram_available_bytes':ram,'shm_available_bytes':shm_free,'incremental_ram_required_bytes':2*G,'incremental_shm_required_bytes':G},assessment='Same accepted candidate/run; recorded operator config and store options restored. Stock4GiB node unchanged; no guest reserve tweak, image build/new pair/Campaign replay. Current published lease and exact guest/fixture/resource proof still required by each public capture. Export only existing five-file allowlist; visual/strict exact-media hosted gate later.')
with (T/'finish-working-delivery-operator-capture-working5-preparation.json').open('x') as f:json.dump(prep,f,indent=2);f.write('\n')
print(json.dumps({'real_admission':True,'source_ids':post['source_ids'],'free_GiB':round(free/G,3),'required_GiB':round((protected+G)/G,3),'output':str(output)}),flush=True)

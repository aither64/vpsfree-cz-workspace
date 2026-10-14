from pathlib import Path
import json,os,stat,datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');old=json.loads((T/'finish-continuation-capacity-observation1.json').read_text()); entries=[]
for entry in old['files']:
 p=Path(entry['path']);st=p.lstat();assert stat.S_ISREG(st.st_mode) and not p.is_symlink() and st.st_dev==entry['device'] and st.st_ino==entry['inode'] and st.st_size==entry['apparent_bytes'],str(p)
 if not str(p).startswith('/nix/store/'):assert st.st_uid==os.getuid()
 value=dict(entry);value['allocated_bytes']=st.st_blocks*512;value['remaining_writable_growth_bytes']=0 if str(p).startswith('/nix/store/') else max(st.st_size-st.st_blocks*512,0);entries.append(value)
free=os.statvfs('/home/aither/.local/state/vpsfree-kb-verification').f_bavail*os.statvfs('/home/aither/.local/state/vpsfree-kb-verification').f_frsize
ram=int(next(line.split()[1] for line in Path('/proc/meminfo').read_text().splitlines() if line.startswith('MemAvailable:')))*1024
shm=os.statvfs('/dev/shm').f_bavail*os.statvfs('/dev/shm').f_frsize
growth=sum(x['remaining_writable_growth_bytes'] for x in entries);base=16*1024**3;extra=2*1024**3
proof={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Named read-only retained disks and current host availability for reuse, no build/new disk/pair/lifecycle operation','files':entries,'retained_writable_growth_bytes':growth,'free_bytes':free,'ram_available_bytes':ram,'shm_available_bytes':shm,'base_reserve_bytes':base,'assessed_incremental_logs_browser_capture_headroom_bytes':extra,'reuse_reserved_envelope_bytes':growth+base+extra,'free_after_growth_base_incremental':free-growth-base-extra,'minimum_pre_resume_ram_bytes':6*1024**3,'minimum_pre_resume_shm_bytes':5*1024**3,'reused_output_new_extent_bytes':0,'cleanup_credit':False,'builder':'No build selected; original immutable image and all tools already present. Unrelated daemon scratch remains unbounded by these measurements.','monitor':'Conservative fixed envelope; no foreign-state cleanup credit.','operation_admission':False}
with (T/'finish-continuation-capacity-observation2.json').open('x') as f:json.dump(proof,f,indent=2);f.write('\n')
print(json.dumps({k:proof[k] for k in ['at','free_bytes','retained_writable_growth_bytes','base_reserve_bytes','assessed_incremental_logs_browser_capture_headroom_bytes','free_after_growth_base_incremental','ram_available_bytes','shm_available_bytes','operation_admission']}))

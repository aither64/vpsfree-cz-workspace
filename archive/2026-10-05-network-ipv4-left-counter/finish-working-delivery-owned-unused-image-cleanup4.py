import json,pathlib,os,stat,hashlib,datetime,subprocess,sys
os.umask(0o077);T=pathlib.Path(__file__).resolve().parent
reset=json.loads((T/'finish-working-delivery-practical-owned-reset4.json').read_text());old=json.loads((T/'finish-working-delivery-public-continuity5-proof.json').read_text())
assert reset['native_exit_code']==0 and reset['cluster_tree_absent'] and reset['private_backup_files_verified']==206 and reset['original_failed_attempt_unchanged']
assert old['generator']==reset['generator'] and old['complete_exit']['complete']
image=old['continuity']['images'][0];assert len(old['continuity']['images'])==1
file=pathlib.Path(image['path']);target=file.parent
assert str(target)=='/nix/store/iivpp1k84m9jfw60f5z93f17qdyqjfx9-nixos-test-disk-image'
currentprep=json.loads((T/'finish-working-delivery-runtime-smoke5-preparation.json').read_text());packet=json.loads(pathlib.Path(currentprep['packet_path']).read_text());root=pathlib.Path(packet['campaign_root'])
current=json.loads((root/'continuity.json').read_text());assert all(x['path']!=str(file) for x in current['identities']['images'])
st=file.lstat();assert stat.S_ISREG(st.st_mode) and st.st_uid==0 and stat.S_IMODE(st.st_mode)==0o444
assert all(getattr(st,{'device':'st_dev','inode':'st_ino','size':'st_size'}[k])==image[k] for k in ['device','inode','size'])
context=root.parent/'unused-working4-image-removal';context.mkdir(mode=0o700)
store='/nix/store/iirndnicd13h4zjr8xwwj8hq2cghpfjn-nix-2.34.8/bin/nix-store'
records=[]
def call(name,args):
 with (context/(name+'.stdout')).open('xb') as o,(context/(name+'.stderr')).open('xb') as e:
  r=subprocess.run([store,*args],stdout=o,stderr=e,stdin=subprocess.DEVNULL)
 row={'name':name,'exit_code':r.returncode}
 records.append(row)
 if r.returncode:raise RuntimeError('native Nix command refused; no override selected')
 return (context/(name+'.stdout')).read_text()
before=os.statvfs('/nix/store');before_free=before.f_bavail*before.f_frsize
failure=None;nar_hash=None
try:
 assert not call('roots',['--query','--roots',str(target)]).strip()
 assert not call('referrers',['--query','--referrers',str(target)]).strip()
 nar_hash=call('registered-hash',['--query','--hash',str(target)]).strip();assert nar_hash
 call('specific-delete',['--delete',str(target)])
 assert not target.exists()
except BaseException as e:failure={'class':type(e).__name__}
after=os.statvfs('/nix/store')
value={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete':failure is None,'failure':failure,'scope':'Only one positively attributed unrooted/unreferenced reproducible services image from already stopped/reset/privately-backed-up working4. No broad GC, ignore-liveness, guest/disk/source/receipt deletion or other store path selected. Native Nix liveness checks remain active.','original_generator':reset['generator'],'image':str(target),'original_identity':image,'allocated_bytes_before':st.st_blocks*512,'registered_nar_hash':nar_hash,'free_bytes_before':before_free,'free_bytes_after':after.f_bavail*after.f_frsize,'native_commands':records,'current_working5_image_distinct':True,'evidence_backup_sha256':reset['private_backup_manifest_sha256'],'limits':'Measured free-space delta can include concurrent activity; no guessed cleanup credit, retained growth/reserve unchanged.'}
(context/'proof.json').write_text(json.dumps(value,indent=2)+'\n');(T/'finish-working-delivery-owned-unused-image-cleanup4.json').write_text(json.dumps(value,indent=2)+'\n')
print(json.dumps({'complete':value['complete'],'failure':failure,'allocated_bytes_before':value['allocated_bytes_before'],'free_bytes_before':before_free,'free_bytes_after':value['free_bytes_after']}),flush=True)
sys.exit(0 if failure is None else 1)

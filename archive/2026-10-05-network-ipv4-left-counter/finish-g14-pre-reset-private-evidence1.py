from pathlib import Path
import shutil,json,os,stat,hashlib,datetime
tracking=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
source=Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14/campaign/state/clusters/same-slug')
backup=Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14-pre-reset-evidence1')
parent=backup.parent; p=parent.lstat(); assert stat.S_ISDIR(p.st_mode) and not parent.is_symlink() and p.st_uid==os.getuid() and p.st_mode&0o777==0o700
assert not os.path.lexists(backup)
os.umask(0o077)
def ignored(path,names):
 return ['services-root.img','node1-tank.img'] if Path(path)==source/'disks' else []
shutil.copytree(source,backup,symlinks=True,ignore=ignored)
manifest=[];total=0
for path,dirs,files in os.walk(backup,followlinks=False):
 Path(path).chmod(0o700)
 for name in files:
  q=Path(path)/name; rel=q.relative_to(backup); original=source/rel
  if q.is_symlink():
   assert original.is_symlink() and os.readlink(q)==os.readlink(original) and rel.name.startswith('result-') and str(original.resolve()).startswith('/nix/store/')
   manifest.append({'path':rel.as_posix(),'kind':'immutable-store-symlink','target':os.readlink(q)})
  else:
   assert q.is_file() and original.is_file() and not original.is_symlink()
   q.chmod(0o600);a=hashlib.sha256(q.read_bytes()).hexdigest();b=hashlib.sha256(original.read_bytes()).hexdigest();assert a==b
   total+=q.stat().st_size;manifest.append({'path':rel.as_posix(),'kind':'ordinary-private-file','bytes':q.stat().st_size,'sha256':a})
for n in ('services-root.img','node1-tank.img'):assert not os.path.lexists(backup/'disks'/n)
private={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(source),'backup':str(backup),'files':manifest,'excluded_disks':['disks/services-root.img','disks/node1-tank.img'],'scope':'Opaque private non-disk evidence copy only; no reset or disk copy'}
m=backup/'private-evidence-manifest.json';m.open('x').write(json.dumps(private,indent=2)+'\n');m.chmod(0o600)
public={'schema':1,'at':private['at'],'generator':'725c325e8b4971931e5d16df86bafa8584358ecb','instance_id':'31f2a709-4906-45fe-8224-dec594ce9471','backup':str(backup),'parent_mode':'0700','ordinary_file_mode':'0600','ordinary_file_count':sum(x['kind']=='ordinary-private-file' for x in manifest),'known_store_symlink_count':sum(x['kind']=='immutable-store-symlink' for x in manifest),'copied_bytes':total,'private_manifest_sha256':hashlib.sha256(m.read_bytes()).hexdigest(),'all_copied_bytes_verified':True,'excluded_disk_count':2,'original_disks_and_state_retained':True,'reset_selected':False,'limits':'No file contents, private inputs, accounts or credentials exported; no restore/adoption/lifecycle authority. Original failed Campaign outside the cluster remains unchanged.'}
out=tracking/'finish-g14-pre-reset-private-evidence1.json';out.open('x').write(json.dumps(public,indent=2)+'\n');print(json.dumps({'proof':out.name,'private_files':public['ordinary_file_count'],'bytes':total,'reset':False}))

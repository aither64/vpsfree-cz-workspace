from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter'); R=T.parent.parent/'worktrees'/T.name/'vpsfree-kb-contracts-runtime'
G='/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git'
head=(T/'finish-k-fixture-tcp-selection-publish1-final.head').read_text().strip(); metadata=json.loads((T/'finish-fixture-tcp-selection-source-metadata1.json').read_text());source=Path(metadata['path'])
assert metadata['locked']['rev']==head
entries=[]
for line in subprocess.check_output([G,'ls-tree','-r',head],cwd=R,text=True).splitlines():
 ident,path=line.split('\t',1); mode,kind,blob=ident.split(); assert kind=='blob' and mode in ['100644','100755']
 expected=subprocess.check_output([G,'cat-file','blob',blob],cwd=R); actual=(source/path).read_bytes(); assert actual==expected,path
 assert bool((source/path).stat().st_mode&0o111)==(mode=='100755'),path
 entries.append({'path':path,'git_blob':blob,'mode':mode,'sha256':hashlib.sha256(actual).hexdigest()})
subject=Path('/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source')
owners=['cluster/lib/'+n for n in ['kb_runtime.rb','kb_state.rb','kb_process.rb','kb_source.rb','kb_resources.rb']]
assert all((source/n).read_bytes()==(subject/n).read_bytes() for n in owners)
assert len(entries)==259
value={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'revision':head,'source':str(source),'all_git_files_exact':True,'file_count':len(entries),'files':entries,'g725_imported_sdk_owners_exact':owners,'real_operations':'not admitted or started','generator':'725c325e8b4971931e5d16df86bafa8584358ecb','limit':'New source is harness only; it does not regenerate or relabel retained G725 guests/media.'}
with (T/'finish-lease-observation-source-binding2.json').open('x') as f:json.dump(value,f,indent=2);f.write('\n')
print(json.dumps({k:value[k] for k in ['revision','source','all_git_files_exact','file_count','g725_imported_sdk_owners_exact']}))

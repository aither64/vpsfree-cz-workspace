#!/usr/bin/env python3
"""Bind a realized verifier package to reviewed Git objects; no product code execution."""
import datetime,hashlib,json,os,pathlib,re,subprocess
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
W=T.parents[1]/'worktrees'/'2026-10-05-network-ipv4-left-counter'/'vpsfree-kb-contracts-runtime'
GIT='/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git'
g=json.loads((T/'finish-virtiofs-review1-acceptance.json').read_text());G='725c325e8b4971931e5d16df86bafa8584358ecb';assert g['source_gate_complete'] and g['exported_evidence_direct_fix_verified'] and g['k']==G
r=json.loads((T/'finish-virtiofs-package-realize1.json').read_text());assert r['generator']==G and r['exit_code']==0 and r['cancel_reason'] is None
p=pathlib.Path(r['gc_root']).resolve(strict=True);wrapper=(p/'bin/vpsfree-kb-verify').read_text();match=re.search(r'--selection (/nix/store/[a-z0-9]{32}-vpsfree-kb-verify-selection[.]json)',wrapper);assert match
selection_path=pathlib.Path(match.group(1));selection=json.loads(selection_path.read_text());source=pathlib.Path(selection['source']);metadata_path=pathlib.Path(selection['metadata']);metadata=json.loads(metadata_path.read_text());assert metadata['schema']==1 and metadata['revision']==G and metadata['source']==str(source);assert str(source)+'/tools/runtime-verify.rb' in wrapper
assert str(metadata_path) in (pathlib.Path(selection['runtime'])/'bin/vpsfree-kb-devcluster').read_text()
assert str(metadata_path) in (pathlib.Path(selection['capture'])/'bin/vpsfree-kb-capture').read_text()
assert str(metadata_path) in (pathlib.Path(selection['capture'])/'bin/vpsfree-kb-validate').read_text()
entries=subprocess.check_output([GIT,'-C',str(W),'ls-tree','-r','-z',G]).split(b'\0');count=0
for line in entries:
 if not line:continue
 header,name=line.split(b'\t');mode,kind,blob=header.split();assert kind==b'blob';target=source/os.fsdecode(name);expected=subprocess.check_output([GIT,'-C',str(W),'cat-file','blob',blob.decode()]);actual=os.readlink(target).encode() if mode==b'120000' else target.read_bytes();assert expected==actual,os.fsdecode(name)
 if mode!=b'120000':assert bool(target.stat().st_mode&0o111)==(mode==b'100755'),os.fsdecode(name)
 count+=1
assert metadata['lock_sha256']==hashlib.sha256((source/'flake.lock').read_bytes()).hexdigest()
names=['fixtures/production-shape.json','fixtures/prepare.cjs'];fixture=hashlib.sha256('\n'.join(name+'\0'+hashlib.sha256((source/name).read_bytes()).hexdigest() for name in names).encode()).hexdigest();assert fixture==metadata['fixture_sha256']
assert metadata['inputs']['vpsadmin']['rev']=='ebe4fab3d50a51bda1f94014ca95c73ba2a967a8'
measurements=[json.loads(x) for x in (pathlib.Path('/tmp/finish-virtiofs-package-realize1.measurements.jsonl')).read_text().splitlines()]
a={'accepted':True,'accepted_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'generator':G,'package':str(p),'gc_root':r['gc_root'],'source':str(source),'selection_path':str(selection_path),'selection':selection,'metadata_path':str(metadata_path),'metadata_sha256':hashlib.sha256(metadata_path.read_bytes()).hexdigest(),'lock_sha256':metadata['lock_sha256'],'fixture_sha256':fixture,'vpsadmin_revision':metadata['inputs']['vpsadmin']['rev'],'all_git_blobs_verified':count,'native_receipt':'finish-virtiofs-package-realize1.json','monitored_minimum_free_bytes':min(x['store_available_bytes'] for x in measurements),'scope':'Exact immutable package/source binding only; no guest, payload-fit, runtime or capture proof','real_campaign_admitted':False}
with (T/'finish-virtiofs-package-realize1-acceptance.json').open('x') as f:json.dump(a,f,indent=2);f.write('\n')
print(json.dumps({'accepted':True,'generator':G,'package':str(p),'all_git_blobs_verified':count}))

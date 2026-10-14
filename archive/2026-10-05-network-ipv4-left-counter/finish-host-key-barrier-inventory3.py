from pathlib import Path
import json,subprocess,hashlib,datetime,copy,argparse
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
a=argparse.ArgumentParser();a.add_argument('--k',required=True);a.add_argument('--e',required=True);a.add_argument('--d',required=True);q=a.parse_args()
out=copy.deepcopy(json.loads((T/'finish-virtiofs-inventory3.json').read_text()))
def g(r,*args):return subprocess.check_output(['/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git',*args],cwd=r)
for item in out['repositories']:
 r=Path(item['worktree']);key=item['key'];base=item['base'];head={'k':q.k,'e':q.e,'d':q.d,'c':'b5c37e01957b9bde4c382a9fa0e47ae9c8db93ba'}.get(key,item['head'])
 if key=='c':base='6e4947b52abe103c582bfab2d0b37a8f17a7c02d'
 assert g(r,'rev-parse','HEAD').decode().strip()==head and not g(r,'status','--porcelain')
 assert g(r,'merge-base',base,head).decode().strip()==base and not g(r,'rev-list','--merges',base+'..'+head)
 item.update(base=base,head=head,tree=g(r,'rev-parse',head+'^{tree}').decode().strip(),merge_base=base,clean=True)
 item['commits']=[{'sha':x.split(' ',1)[0],'subject':x.split(' ',1)[1]}for x in g(r,'log','--reverse','--format=%H %s',base+'..'+head).decode().splitlines()]
 assert len(item['commits'])=={'v':4,'w':1,'c':2,'k':2,'d':3,'e':2}[key]
 item['changed_paths']=g(r,'diff','--name-only',base,head).decode().splitlines();item['artifacts']=[]
 for suffix,args in [('diff',['diff','--binary','--full-index',base,head]),('history',['log','--reverse','--format=fuller',base+'..'+head])]:
  b=g(r,*args);p=T/('finish-host-key-barrier-inventory3-'+key+'.'+suffix)
  with p.open('xb')as f:f.write(b)
  item['artifacts'].append({'kind':suffix,'path':p.name,'sha256':hashlib.sha256(b).hexdigest()})
k=Path(next(x['worktree']for x in out['repositories']if x['key']=='k'));aux=k.parent/'vpsfree-kb-contracts'
assert g(aux,'rev-parse','HEAD').decode().strip()==q.k and not g(aux,'status','--porcelain')
out.update(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),at=datetime.datetime.now(datetime.timezone.utc).isoformat(),same_combined_k_auxiliary_head=q.k,status='Final committed persistent SSH configuration with pinned plain-string run composition corrected; affected review pending',local_ci=False,history_disposition='finish-host-key-barrier-history-disposition3.json',review='Prior completed whole-branch conclusions retained for unchanged objects; five-path host-key configuration/test/contract correction and exact E selection pending affected four-lane review')
out['preserved_consumed_sources']['g14']='725c325e8b4971931e5d16df86bafa8584358ecb'
out['preserved_consumed_sources']['g13']='9c551c6ad68650d12f3d8e91f8bf33a76e2ffe0e'
out['preserved_consumed_sources']['public_stdin_g492']='49221a07e2fabbee4a3621979f814eac8c8bad9d'
with(T/'finish-host-key-barrier-inventory3.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'source_heads':{x['key']:x['head']for x in out['repositories']},'complete_histories':True}))

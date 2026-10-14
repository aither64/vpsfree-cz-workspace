from pathlib import Path
import subprocess,hashlib,json
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-kb-contracts-runtime';C=R.parent/'vpsfree-kb-contracts'
old='9df0a9cb19fdd0087c5fc7c571d9f547daf93177';base='873758fd6aec0c03f50a94600e0ceab97946f255';path='tools/test-runtime-verify.rb';packet=T/'finish-k-runtime-reduction-structured-attrs-fix1';branch=T.name+'-kb-runtime'
def g(*a,repo=R):
 p=subprocess.run(['git',*a],cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr: print(p.stderr.decode(),end='',flush=True)
 return p.stdout

def save(suffix,data):
 with(T/('finish-k-runtime-reduction-structured-attrs-fix1-'+suffix)).open('xb') as f:f.write(data)
# Packet integrity is inspected separately by root before this normal commit.
assert g('rev-parse','HEAD').decode().strip()==old and g('status','--porcelain')==b' M tools/test-runtime-verify.rb\n'
assert g('rev-parse','HEAD',repo=C).decode().strip()==old and not g('status','--porcelain',repo=C)
assert not g('diff','--cached','--binary') and not g('diff','--cached','--binary',repo=C)
assert g('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/vpsfree-kb-contracts.git'
assert g('diff','--binary','--full-index')==Path(str(packet)+'.diff').read_bytes()
names=g('ls-files').decode().splitlines()
hooks=Path(g('rev-parse','--git-path','hooks').decode().strip());hooks=hooks if hooks.is_absolute() else R/hooks
assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','config','--get','core.hooksPath'],cwd=R,capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in names)
protected={n:g('ls-tree',old,'--',n) for n in names if n!=path}
oldseries=g('rev-list','--reverse',base+'..HEAD').decode().splitlines(); assert len(oldseries)==2
# Preserve published failing source as provenance outside the final series.
g('update-ref','refs/heads/preserve/finish-generator-reduced-attrs-failed',old,'0'*40)
g('fetch','origin')
assert g('rev-parse','origin/master').decode().strip()==base,'upstream advanced; reassess instead of silently changing base'
delta=g('diff','--binary','--full-index');g('add','--',path);assert g('diff','--cached','--binary','--full-index')==delta
expected_tree=g('write-tree').decode().strip();save('staged.diff',delta)
print(g('commit','--amend','-F',str(T/'finish-k-runtime-reduction-owning.message')).decode(),flush=True)
head=g('rev-parse','HEAD').decode().strip();tree=g('rev-parse','HEAD^{tree}').decode().strip();assert tree==expected_tree and not g('status','--porcelain')
series=g('rev-list','--reverse',base+'..HEAD').decode().splitlines();assert len(series)==2 and series[0]==oldseries[0] and not g('rev-list','--merges',base+'..HEAD')
assert g('diff','--binary','--full-index',old,head)==delta
for n,entry in protected.items():assert g('ls-tree','HEAD','--',n)==entry,n
g('restore','--source='+head,'--staged','--worktree','--',path,repo=C)
g('update-ref','refs/heads/'+T.name,head,old,repo=C)
assert not g('status','--porcelain',repo=C) and g('rev-parse','HEAD',repo=C).decode().strip()==head
for b in [branch,T.name]:
 assert g('ls-remote','origin','refs/heads/'+b).decode()==old+'\trefs/heads/'+b+'\n'
 save('push-'+b+'.log',g('push','--force-with-lease=refs/heads/'+b+':'+old,'origin',head+':refs/heads/'+b))
 assert g('ls-remote','origin','refs/heads/'+b).decode()==head+'\trefs/heads/'+b+'\n'
save('final.head',(head+'\n').encode());save('final.diff',g('diff','--binary','--full-index',base,'HEAD'));save('final.history',g('log','--reverse','--format=fuller',base+'..HEAD'))
proof={'old':old,'head':head,'tree':tree,'base':base,'series':series,'normal_commit':True,'source_delta_exact':True,'protected_count':len(protected),'both_worktrees_clean':True,'publication':'both exact SSH feature refs verified','hosted':'unproved','real_guest':'unperformed'}
save('proof.json',(json.dumps(proof,indent=2)+'\n').encode());print(json.dumps(proof),flush=True)

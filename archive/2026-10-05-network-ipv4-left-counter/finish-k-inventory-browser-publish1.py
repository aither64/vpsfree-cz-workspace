from pathlib import Path
import subprocess,json,hashlib
t=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime')
original=r.parent/'vpsfree-kb-contracts'
base='873758fd6aec0c03f50a94600e0ceab97946f255'
old='e45520e27ced8c1eb28def9995bb2aea4a58fd1d'
branches=['2026-10-05-network-ipv4-left-counter','2026-10-05-network-ipv4-left-counter-kb-runtime']
path='tools/test-ip-inventory.cjs'
def git(*args,repo=r):
 p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr: print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(name,data):
 if isinstance(data,str):data=data.encode()
 with (t/('finish-k-inventory-browser-publish1-'+name)).open('xb') as f:f.write(data)
subprocess.run(['sha256sum','--check',str(t/'finish-k-inventory-browser-fix1.sha256')],cwd=t,check=True)
subprocess.run(['sha256sum','--check',str(t/'finish-k-inventory-browser-fix1.source.sha256')],cwd=r,check=True)
assert git('rev-parse','HEAD').decode().strip()==old
assert git('diff','--binary','--full-index')==(t/'finish-k-inventory-browser-fix1.diff').read_bytes()
assert git('status','--porcelain=v1','--untracked-files=all')==b' M '+path.encode()+b'\n'
assert git('diff','--cached','--binary')==b''
assert git('rev-parse','HEAD',repo=original).decode().strip()==old
assert git('status','--porcelain=v1','--untracked-files=all',repo=original)==b''
git('fetch','origin','master')
assert git('rev-parse','origin/master').decode().strip()==base
assert git('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/vpsfree-kb-contracts.git'
for b in branches:assert git('ls-remote','origin','refs/heads/'+b).decode()==old+'\trefs/heads/'+b+'\n'
hooks=Path(git('rev-parse','--git-path','hooks').decode().strip())
if not hooks.is_absolute():hooks=r/hooks
assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','-C',str(r),'config','--get','core.hooksPath'],capture_output=True).returncode==1
git('update-ref','refs/heads/preserve/finish-generator-g2',old,'0'*40)
message=t/'finish-k-inventory-browser-publish1-runtime.message'
with message.open('xb') as f:f.write(git('show','-s','--format=%B','HEAD'))
git('add','--',path)
assert git('diff','--cached','--name-only').decode()==path+'\n'
tree=git('write-tree').decode().strip()
print(git('commit','--amend','-F',str(message)).decode(),flush=True)
head=git('rev-parse','HEAD').decode().strip()
assert git('rev-parse','HEAD^{tree}').decode().strip()==tree
assert git('rev-parse','HEAD^')==git('rev-parse',old+'^')
assert git('diff','--name-only',old,head).decode()==path+'\n'
assert git('status','--porcelain=v1','--untracked-files=all')==b''
print(git('rebase','--onto',head,old,repo=original).decode(),flush=True)
assert git('rev-parse','HEAD',repo=original).decode().strip()==head
assert git('status','--porcelain=v1','--untracked-files=all',repo=original)==b''
assert git('rev-list','--count',base+'..HEAD').decode().strip()=='2'
assert git('rev-list','--merges',base+'..HEAD')==b''
save('head',head+'\n');save('diff',git('diff','--binary','--full-index',base,head));save('history',git('log','--reverse','--format=fuller',base+'..HEAD'));save('correction.diff',git('diff','--binary','--full-index',old,head))
save('proof.json',json.dumps({'base':base,'old':old,'head':head,'tree':tree,'only_changed_path':path,'source_sha256':hashlib.sha256((r/path).read_bytes()).hexdigest(),'commits':2,'both_worktrees_clean_same_head':True,'local_ci':False,'normal_hooks':True},indent=2)+'\n')
git('fetch','origin','master')
assert git('rev-parse','origin/master').decode().strip()==base
push=['push','--atomic']
for b in branches:push.append('--force-with-lease=refs/heads/'+b+':'+old)
push+=['origin',*[head+':refs/heads/'+b for b in branches]]
print(git(*push).decode(),flush=True)
remote=git('ls-remote','origin',*['refs/heads/'+b for b in branches]);save('remote',remote)
assert sorted(remote.decode().splitlines())==sorted([head+'\trefs/heads/'+b for b in branches])
print('Published corrected combined generator '+head,flush=True)

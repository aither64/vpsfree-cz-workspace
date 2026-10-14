from pathlib import Path
import subprocess, json, hashlib, os
p=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace')
old='d2d64f2e2a2167a1171e2bca17fe99ff2375d231'
base='c51ba3c0ca0d41d237ef71c56accd564beb70a33'
remoteold='51aba080b264c28f5584867b6cf006bf423ae2f3'
branch='2026-10-05-network-ipv4-left-counter'
paths=['portal/internal/web/operation_state_test.go','portal/internal/web/server_test.go']
def git(*a):
 result=subprocess.run(['git','-C',str(r),*a],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if result.stderr: print(result.stderr.decode(),end='',flush=True)
 return result.stdout
def save(suffix,data):
 if isinstance(data,str):data=data.encode()
 with (p/('finish-d-force-fixture-publish1-'+suffix)).open('xb') as f:f.write(data)
subprocess.run(['sha256sum','--check',str(p/'finish-d-force-fixture-source1.sha256')],cwd=p,check=True)
subprocess.run(['sha256sum','--check',str(p/'finish-d-force-fixture-source1.source.sha256')],cwd=r,check=True)
assert git('rev-parse','HEAD').decode().strip()==old
assert git('branch','--show-current').decode().strip()==branch
assert git('status','--porcelain=v1','--untracked-files=all')==(' M '+paths[0]+'\n M '+paths[1]+'\n').encode()
assert git('diff','--binary','--full-index')==(p/'finish-d-force-fixture-source1.diff').read_bytes()
assert git('diff','--cached','--binary')==b''
assert git('remote','get-url','origin').decode().strip()=='git@github.com:aither64/dev-workspace.git'
git('fetch','origin','master');assert git('rev-parse','origin/master').decode().strip()==base
assert git('ls-remote','origin','refs/heads/'+branch).decode()==remoteold+'\trefs/heads/'+branch+'\n'
hooks=Path(git('rev-parse','--git-path','hooks').decode().strip())
if not hooks.is_absolute():hooks=r/hooks
assert not [x for x in hooks.iterdir() if x.is_file() and not x.name.endswith('.sample')]
assert subprocess.run(['git','-C',str(r),'config','--get','core.hooksPath'],capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in git('ls-files').decode().splitlines())
message=p/'finish-d-force-fixture-source1.message';assert max(map(len,message.read_text().splitlines()))<=80
before={n:hashlib.sha256(git('show','HEAD:'+n)).hexdigest() for n in git('ls-files').decode().splitlines() if n not in paths}
git('add','--',*paths);assert git('diff','--cached','--name-only').decode().splitlines()==paths
save('staged.diff',git('diff','--cached','--binary','--full-index'))
tree=git('write-tree').decode().strip();print(git('commit','-F',str(message)).decode(),flush=True)
head=git('rev-parse','HEAD').decode().strip();assert git('rev-parse','HEAD^').decode().strip()==old
assert git('rev-parse','HEAD^{tree}').decode().strip()==tree
assert git('status','--porcelain=v1','--untracked-files=all')==b''
assert git('rev-list','--count',base+'..HEAD').decode().strip()=='3'
assert git('rev-list','--merges',base+'..HEAD')==b''
for n,digest in before.items():assert hashlib.sha256(git('show','HEAD:'+n)).hexdigest()==digest,n
save('head',head+'\n');save('history',git('log','--reverse','--format=fuller',base+'..HEAD'));save('final.diff',git('diff','--binary','--full-index',base,head))
save('proof.json',json.dumps({'base':base,'previous_rebased_head':old,'old_published_head':remoteold,'head':head,'tree':tree,'commits':3,'test_only_delta_paths':paths,'production_and_other_files_exact':True,'normal_hooks':True,'local_ci':False},indent=2)+'\n')
git('fetch','origin','master');assert git('rev-parse','origin/master').decode().strip()==base
print(git('push','--force-with-lease=refs/heads/'+branch+':'+remoteold,'origin',head+':refs/heads/'+branch).decode(),flush=True)
remote=git('ls-remote','origin','refs/heads/'+branch);assert remote.decode()==head+'\trefs/heads/'+branch+'\n';save('remote',remote)
print('Published corrected D '+head,flush=True)

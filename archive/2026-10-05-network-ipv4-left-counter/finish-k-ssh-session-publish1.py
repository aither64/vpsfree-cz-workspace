from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-kb-contracts-runtime';O=R.parent/'vpsfree-kb-contracts';OLD='7dc4d70830e535f4559bccfa668cf65cdce1de2d';BASE='873758fd6aec0c03f50a94600e0ceab97946f255';BRANCHES=[T.name,T.name+'-kb-runtime'];PREFIX='finish-k-ssh-session-publish1-'
def git(*args,repo=R):
 p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr:print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(name,data):
 if isinstance(data,str):data=data.encode()
 with (T/(PREFIX+name)).open('xb') as f:f.write(data)
files=json.loads((T/'finish-k-ssh-session-source1.files.json').read_text());paths=sorted(f['path'] for f in files);expected={f['path']:f['sha256'] for f in files}
assert git('rev-parse','HEAD').decode().strip()==OLD and git('branch','--show-current').decode().strip()==BRANCHES[1]
assert git('diff','--cached','--binary')==b''
assert git('status','--porcelain=v1','--untracked-files=all').decode()==''.join(' M '+p+'\n' for p in paths)
assert git('diff','--binary','--full-index')==(T/'finish-k-ssh-session-source1.full.diff').read_bytes()
for path,sha in expected.items():assert hashlib.sha256((R/path).read_bytes()).hexdigest()==sha,path
assert git('rev-parse','HEAD',repo=O).decode().strip()==OLD and git('status','--porcelain=v1','--untracked-files=all',repo=O)==b''
assert git('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/vpsfree-kb-contracts.git'
git('fetch','origin','master');assert git('rev-parse','FETCH_HEAD').decode().strip()==BASE
for branch in BRANCHES:assert git('ls-remote','origin','refs/heads/'+branch).decode()==OLD+'\trefs/heads/'+branch+'\n'
hooks=Path(git('rev-parse','--git-path','hooks').decode().strip());assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','-C',str(R),'config','--get','core.hooksPath'],capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in git('ls-files').decode().splitlines())
save('old.diff',git('diff','--binary','--full-index',BASE,OLD));save('old.history',git('log','--reverse','--format=fuller',BASE+'..'+OLD));save('working.diff',git('diff','--binary','--full-index'))
git('update-ref','refs/heads/preserve/finish-generator-g6',OLD,'0'*40)
message=T/(PREFIX+'message');original=git('show','-s','--format=%B',OLD).decode(); extra='Discover all machine SSH keys within one readiness deadline, retaining private\nnative diagnostics and refusing partial or changed trust. Give the runner its\nown POSIX session before machine creation; containing cgroup and host failures\nstill require complete ownership and exit proof.\n\n'; assert original.count('Legacy state and sockets')==1;message.write_text(original.replace('Legacy state and sockets',extra+'Legacy state and sockets'));assert all(len(line)<=80 for line in message.read_text().splitlines())
git('add','--',*paths);assert git('diff','--cached','--name-only').decode().splitlines()==paths
TREE=git('write-tree').decode().strip();print(git('commit','--amend','-F',str(message)).decode(),flush=True)
HEAD=git('rev-parse','HEAD').decode().strip();assert git('rev-parse','HEAD^{tree}').decode().strip()==TREE and git('rev-parse','HEAD^')==git('rev-parse',OLD+'^')
assert sorted(git('diff','--name-only',OLD,HEAD).decode().splitlines())==paths and git('status','--porcelain=v1','--untracked-files=all')==b''
print(git('rebase','--onto',HEAD,OLD,repo=O).decode(),flush=True);assert git('rev-parse','HEAD',repo=O).decode().strip()==HEAD and git('status','--porcelain=v1','--untracked-files=all',repo=O)==b''
assert git('rev-list','--count',BASE+'..HEAD').decode().strip()=='2' and git('rev-list','--merges',BASE+'..HEAD')==b''
save('head',HEAD+'\n');save('history',git('log','--reverse','--format=fuller',BASE+'..HEAD'));save('diff',git('diff','--binary','--full-index',BASE,HEAD));save('correction.diff',git('diff','--binary','--full-index',OLD,HEAD))
save('proof.json',json.dumps(dict(base=BASE,old=OLD,head=HEAD,tree=TREE,paths=paths,sha256=expected,commits=2,both_worktrees_clean_same_head=True,old_generator_preserved='preserve/finish-generator-g6',old_real_campaign_retained=True,local_ci=False,normal_hooks=True),indent=2)+'\n')
git('fetch','origin','master');assert git('rev-parse','FETCH_HEAD').decode().strip()==BASE
push=['push','--atomic']+['--force-with-lease=refs/heads/'+b+':'+OLD for b in BRANCHES]+['origin']+[HEAD+':refs/heads/'+b for b in BRANCHES]
print(git(*push).decode(),flush=True);remote=git('ls-remote','origin',*['refs/heads/'+b for b in BRANCHES]);save('remote',remote);assert sorted(remote.decode().splitlines())==sorted(HEAD+'\trefs/heads/'+b for b in BRANCHES)
print('Published corrected combined generator '+HEAD,flush=True)

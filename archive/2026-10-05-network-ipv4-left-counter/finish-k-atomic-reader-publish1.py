from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-kb-contracts-runtime';O=R.parent/'vpsfree-kb-contracts';OLD='ab09bd437b310f57e4ff2453ec0432555d85eaca';BASE='873758fd6aec0c03f50a94600e0ceab97946f255';BRANCHES=[T.name,T.name+'-kb-runtime'];PREFIX='finish-k-atomic-reader-publish1-'
def git(*args,repo=R):
 p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr:print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(name,data):
 if isinstance(data,str):data=data.encode()
 with (T/(PREFIX+name)).open('xb') as f:f.write(data)
paths=['README.md','cluster/lib/kb_state.rb','cluster/runtime-contract.md','docs/webui-change-workflow.md','tools/test-runtime.rb'];expected={'cluster/lib/kb_state.rb':'97a9e06b3d0f1a902e3e7ab708af01f6ef86cc447c8864307fedbcbc4f0fa108','tools/test-runtime.rb':'ea52a674adf7ca12b31b09e044a2a713f9831b19940a66e8793cb2c047f0446e',**json.loads((T/'finish-direct-owner-prose2.json').read_text())['paths']}
assert git('rev-parse','HEAD').decode().strip()==OLD and git('branch','--show-current').decode().strip()==BRANCHES[1]
assert git('diff','--cached','--binary')==b''
assert git('status','--porcelain=v1','--untracked-files=all').decode()==''.join(' M '+p+'\n' for p in paths)
assert git('diff','--binary','--full-index','--','cluster/lib/kb_state.rb','tools/test-runtime.rb')==(T/'finish-k-atomic-reader-source1.diff').read_bytes()
for path,sha in expected.items():assert hashlib.sha256((R/path).read_bytes()).hexdigest()==sha,path
assert git('rev-parse','HEAD',repo=O).decode().strip()==OLD and git('status','--porcelain=v1','--untracked-files=all',repo=O)==b''
assert git('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/vpsfree-kb-contracts.git'
git('fetch','origin','master');assert git('rev-parse','FETCH_HEAD').decode().strip()==BASE
for branch in BRANCHES:assert git('ls-remote','origin','refs/heads/'+branch).decode()==OLD+'\trefs/heads/'+branch+'\n'
hooks=Path(git('rev-parse','--git-path','hooks').decode().strip());assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','-C',str(R),'config','--get','core.hooksPath'],capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in git('ls-files').decode().splitlines())
save('old.diff',git('diff','--binary','--full-index',BASE,OLD));save('old.history',git('log','--reverse','--format=fuller',BASE+'..'+OLD));save('working.diff',git('diff','--binary','--full-index'))
git('update-ref','refs/heads/preserve/finish-generator-g4',OLD,'0'*40)
message=T/(PREFIX+'message');message.write_bytes(git('show','-s','--format=%B',OLD));assert all(len(line)<=80 for line in message.read_text().splitlines())
git('add','--',*paths);assert git('diff','--cached','--name-only').decode().splitlines()==paths
TREE=git('write-tree').decode().strip();print(git('commit','--amend','-F',str(message)).decode(),flush=True)
HEAD=git('rev-parse','HEAD').decode().strip();assert git('rev-parse','HEAD^{tree}').decode().strip()==TREE and git('rev-parse','HEAD^')==git('rev-parse',OLD+'^')
assert git('diff','--name-only',OLD,HEAD).decode().splitlines()==paths and git('status','--porcelain=v1','--untracked-files=all')==b''
print(git('rebase','--onto',HEAD,OLD,repo=O).decode(),flush=True);assert git('rev-parse','HEAD',repo=O).decode().strip()==HEAD and git('status','--porcelain=v1','--untracked-files=all',repo=O)==b''
assert git('rev-list','--count',BASE+'..HEAD').decode().strip()=='2' and git('rev-list','--merges',BASE+'..HEAD')==b''
save('head',HEAD+'\n');save('history',git('log','--reverse','--format=fuller',BASE+'..HEAD'));save('diff',git('diff','--binary','--full-index',BASE,HEAD));save('correction.diff',git('diff','--binary','--full-index',OLD,HEAD))
save('proof.json',json.dumps(dict(base=BASE,old=OLD,head=HEAD,tree=TREE,paths=paths,sha256=expected,commits=2,both_worktrees_clean_same_head=True,old_generator_preserved='preserve/finish-generator-g4',old_real_campaign_retained=True,local_ci=False,normal_hooks=True),indent=2)+'\n')
git('fetch','origin','master');assert git('rev-parse','FETCH_HEAD').decode().strip()==BASE
push=['push','--atomic']+['--force-with-lease=refs/heads/'+b+':'+OLD for b in BRANCHES]+['origin']+[HEAD+':refs/heads/'+b for b in BRANCHES]
print(git(*push).decode(),flush=True);remote=git('ls-remote','origin',*['refs/heads/'+b for b in BRANCHES]);save('remote',remote);assert sorted(remote.decode().splitlines())==sorted(HEAD+'\trefs/heads/'+b for b in BRANCHES)
print('Published corrected combined generator '+HEAD,flush=True)

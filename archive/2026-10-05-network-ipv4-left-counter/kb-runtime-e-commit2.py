import pathlib, subprocess, hashlib, json, os, stat
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
R=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
B='0ff827df13e82dfab4b536ff29979280f264e8f5'
os.chdir(R)
def git(*args,env=None,data=None):
 return subprocess.check_output(['git',*args],input=data,env=env)
def save(name,data):
 with (T/name).open('xb') as f:f.write(data)
assert git('rev-parse','HEAD').decode().strip()==B
assert git('branch','--show-current').decode().strip()=='2026-10-05-network-ipv4-left-counter'
assert git('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/dev-workspace.git'
assert not git('diff','--cached')
assert git('status','--porcelain=v1','--untracked-files=all')==(T/'kb-runtime-e-final1-source.status').read_bytes()
subprocess.run(['sha256sum','-c',str(T/'kb-runtime-e-final1-source.manifest')],check=True,stdout=subprocess.DEVNULL)
files=json.loads((T/'kb-runtime-e-final1-source.files.json').read_text())
paths=[f['path'] for f in files]
assert len(paths)==23
for f in files:
 p=R/f['path'];assert p.is_file() and not p.is_symlink()
 assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
 assert stat.S_IMODE(p.stat().st_mode)==int(f['mode'],8)
for prefix in ['kb-runtime-e-integrated-quick1','kb-runtime-e-public-quick1','kb-runtime-e-inputs1']:
 receipts=list(T.glob(prefix+'*.exit'));assert receipts
 for p in receipts:assert p.read_text().strip()=='0',p
assert subprocess.run(['git','config','--get','core.hooksPath'],stdout=subprocess.DEVNULL).returncode==1
hooks=pathlib.Path(git('rev-parse','--git-path','hooks').decode().strip())
assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert not [p for p in git('ls-files').decode().splitlines() if any(x in p.lower() for x in ['.overcommit','.pre-commit-config','lefthook','.husky'])]
assert not any(k in os.environ for k in ['OVERCOMMIT_DISABLE','SKIP','HUSKY'])
subprocess.run(['git','fetch','origin','refs/heads/master:refs/remotes/origin/master'],check=True)
assert git('rev-parse','origin/master').decode().strip()==B
assert not git('ls-remote','--heads','origin','refs/heads/2026-10-05-network-ipv4-left-counter')
idx=T/'kb-runtime-e-expected-final.index';assert not idx.exists()
env=dict(os.environ,GIT_INDEX_FILE=str(idx))
git('read-tree',B,env=env);git('add','--',*paths,env=env)
expected=git('write-tree',env=env).decode().strip();save('kb-runtime-e-expected-final.tree',(expected+'\n').encode())
old=git('show',B+':flake.nix')
needle=b'    dev-workspace.url = "github:aither64/dev-workspace/6a972b9ab01077611b2c60e0fc726c185e050315";\n'
assert old.count(needle)==1
partial=old.replace(needle,b'    dev-workspace.url = "github:aither64/dev-workspace/51aba080b264c28f5584867b6cf006bf423ae2f3";\n    kb-runtime.url = "github:vpsfreecz/vpsfree-kb-contracts/93a16d6cecb6bc847ec9335a3f170eb8b301ab56";\n')
blob=git('hash-object','-w','--stdin',data=partial).decode().strip()
git('update-index','--cacheinfo','100644,'+blob+',flake.nix');git('add','--','flake.lock')
assert sorted(git('diff','--cached','--name-only').decode().splitlines())==['flake.lock','flake.nix']
assert git('show',':flake.nix')==partial
save('kb-runtime-e-inputs-staged.diff',git('diff','--cached','--full-index','--binary'))
subprocess.run(['git','diff','--cached','--check'],check=True)
subprocess.run(['git','commit','-F',str(T/'kb-runtime-e-final1-source-inputs.message')],check=True)
first=git('rev-parse','HEAD').decode().strip();save('kb-runtime-e-inputs-committed.sha',(first+'\n').encode())
git('add','--',*[p for p in paths if p!='flake.lock'])
assert sorted(git('diff','--cached','--name-only').decode().splitlines())==sorted(p for p in paths if p!='flake.lock')
for f in files:assert hashlib.sha256(git('show',':'+f['path'])).hexdigest()==f['sha256']
assert git('write-tree').decode().strip()==expected
save('kb-runtime-e-provider-staged.diff',git('diff','--cached','--full-index','--binary'))
subprocess.run(['git','diff','--cached','--check'],check=True)
subprocess.run(['git','commit','-F',str(T/'kb-runtime-e-final1-source-provider.message')],check=True)
assert not git('status','--porcelain=v1')
assert git('rev-parse','HEAD^{tree}').decode().strip()==expected
assert git('rev-list','--count',B+'..HEAD').decode().strip()=='2'
save('kb-runtime-e-committed.sha',git('rev-parse','HEAD'))
save('kb-runtime-e-whole-history.txt',git('log','--reverse','--format=fuller',B+'..HEAD'))
save('kb-runtime-e-whole.diff',git('diff','--full-index','--binary',B,'HEAD'))
save('kb-runtime-e-whole.stat',git('diff','--stat',B,'HEAD'))
print('E two normal commits, exact checked final tree:',git('rev-parse','HEAD').decode().strip())

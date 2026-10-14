#!/usr/bin/env python3
"""Root-owned dependent commit; refuses unverified or changed source."""
import hashlib, json, os, pathlib, subprocess, tempfile
T = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
R = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime')
OLD = '93a16d6cecb6bc847ec9335a3f170eb8b301ab56'
PIN = 'a50f8c1a11ea642edf823f04521f9eaa97132fd2'
BASE = '873758fd6aec0c03f50a94600e0ceab97946f255'
BRANCH = '2026-10-05-network-ipv4-left-counter-kb-runtime'
P = 'kb-runtime-review-fix-quick2'
OUT = 'kb-runtime-review-fix-consolidated'
def call(*args, env=None):
    return subprocess.check_output(args, cwd=R, env=env)
def git(*args, env=None): return call('git', *args, env=env)
def check(condition, message):
    if not condition: raise SystemExit(message)
def same(name, actual): check((T/name).read_bytes() == actual, 'changed evidence/source: '+name)
check(not (T/(OUT+'.sha')).exists(), 'committed receipt already exists')
for suffix in ['', '-toolchain', '-syntax', '-node', '-runtime']:
    check((T/(P+suffix+'.exit')).read_text().strip() == '0', 'required passing gate absent: '+suffix)
subprocess.run(['sha256sum','--check',str(T/(P+'.sha256'))], cwd=T, check=True, stdout=subprocess.DEVNULL)
subprocess.run(['sha256sum','--check',str(T/(P+'-source.sha256'))], cwd=T, check=True, stdout=subprocess.DEVNULL)
check(git('rev-parse','HEAD').decode().strip() == OLD, 'unexpected source head')
check(git('branch','--show-current').decode().strip() == BRANCH, 'unexpected branch')
check(git('remote','get-url','origin').decode().strip() == 'git@github.com:vpsfreecz/vpsfree-kb-contracts.git', 'unexpected SSH remote')
check(git('rev-parse','HEAD^').decode().strip() == PIN, 'runtime parent changed')
check(git('rev-list','--count',BASE+'..HEAD').decode().strip() == '2', 'unexpected complete history')
paths = (T/(P+'-paths.txt')).read_text().splitlines()
check(len(paths)==13 and len(set(paths))==13, 'unexpected owned path set')
same(P+'-source.status', git('status','--porcelain=v1','--untracked-files=all'))
same(P+'-source.index', git('diff','--cached','--binary'))
check(not git('diff','--cached','--name-only'), 'index must be empty')
same(P+'-source.diff', git('diff','--binary','--',*paths))
protected=(T/(P+'-protected-paths.txt')).read_text().splitlines()
check(not git('diff','HEAD','--binary','--',*protected), 'protected source changed')
rows=json.loads((T/(P+'-source.files.json')).read_text())
check({x['path'] for x in rows}==set(paths),'source inventory mismatch')
for row in rows:
    stat=(R/row['path']).stat()
    check('0o'+oct(stat.st_mode & 0o777)[2:]==row['mode'] and stat.st_size==row['bytes'],'source mode/size changed')
for name in ['OVERCOMMIT_DISABLE','SKIP','HUSKY','HUSKY_SKIP_HOOKS','PRE_COMMIT_ALLOW_NO_CONFIG']:
    check(name not in os.environ, 'hook control environment requires inspection: '+name)
for name in ['.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml','.lefthook.yml','.husky']:
    check(not (R/name).exists(), 'unexpected hook framework')
hook_config=subprocess.run(['git','config','--get','core.hooksPath'],cwd=R,capture_output=True)
check(hook_config.returncode==1,'unexpected hooksPath')
hooks=pathlib.Path(git('rev-parse','--git-path','hooks').decode().strip())
check(not any(p.is_file() and not p.name.endswith('.sample') for p in hooks.iterdir()),'unexpected active hooks')
message=T/'kb-runtime-review-fix-final.message'
check(hashlib.sha256(message.read_bytes()).hexdigest()=='d0cbfd5227d551a30f9c8cbddc05c54f9ffba2680de4ad00bbc67d3d279b31f0','commit message changed')
check(all(len(x)<=80 for x in message.read_text().splitlines()),'message line exceeds80')
subprocess.run(['git','fetch','origin','master'],cwd=R,check=True)
check(git('rev-parse','origin/master').decode().strip()==BASE,'default advanced: inspect/reconcile before commit')
subprocess.run(['git','merge-base','--is-ancestor','origin/master','HEAD'],cwd=R,check=True)
for label,args in [('old-history',('log','--format=fuller',BASE+'..HEAD')),('old-tree',('rev-parse','HEAD^{tree}')),('old-full',('diff','--binary','--full-index',BASE+'..HEAD'))]:
    with (T/(OUT+'-'+label)).open('xb') as f:f.write(git(*args))
with tempfile.TemporaryDirectory(prefix='kb-review-fix-index-') as temporary:
    temporary_index=pathlib.Path(temporary)/'index'
    env=dict(os.environ,GIT_INDEX_FILE=str(temporary_index))
    git('read-tree','HEAD',env=env)
    git('add','--',*paths,env=env)
    expected=git('write-tree',env=env).decode().strip()
    staged=git('diff','--cached','--binary','--full-index',env=env)
    changed=git('diff','--cached','--name-only',env=env).decode().splitlines()
    check(set(changed)==set(paths),'expected staged path inventory differs')
    for row in rows:
        check(hashlib.sha256(git('show',':'+row['path'],env=env)).hexdigest()==row['sha256'],'expected staged bytes differ')
        mode=git('ls-files','--stage','--',row['path'],env=env).decode().split()[0]
        check(mode==('100755' if row['mode']=='0o755' else '100644'),'expected staged mode differs')
with (T/(OUT+'-expected.tree')).open('x') as f:f.write(expected+'\n')
with (T/(OUT+'-correction.diff')).open('xb') as f:f.write(staged)
# Mutation starts only after all readiness/source/history/upstream/hook guards.
git('add','--',*paths)
check(git('write-tree').decode().strip()==expected,'actual staged tree differs')
check(git('diff','--cached','--binary','--full-index')==staged,'actual staged diff differs')
subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True)
check(not git('diff','--binary','--',*paths),'unstaged source appeared')
subprocess.run(['git','commit','--amend','-F',str(message)],cwd=R,check=True)
head=git('rev-parse','HEAD').decode().strip()
check(git('rev-parse','HEAD^{tree}').decode().strip()==expected,'final tree differs')
check(git('rev-parse','HEAD^').decode().strip()==PIN,'inherited pin was rewritten')
check(git('rev-list','--count',BASE+'..HEAD').decode().strip()=='2','unexpected final series')
check(not git('rev-list','--merges',BASE+'..HEAD'),'merge commit appeared')
check(not git('status','--porcelain=v1','--untracked-files=all'),'final tree not clean')
for row in rows:
    expected_hash=row['sha256']
    check(hashlib.sha256(git('show','HEAD:'+row['path'])).hexdigest()==expected_hash,'committed bytes differ')
check(git('diff','--binary','--full-index',OLD+'..HEAD')==staged,'amend changed more than frozen correction')
for label,args in [('history',('log','--format=fuller',BASE+'..HEAD')),('tree',('rev-parse','HEAD^{tree}')),('full.diff',('diff','--binary','--full-index',BASE+'..HEAD')),('range-diff',('range-diff',BASE+'..'+OLD,BASE+'..HEAD'))]:
    with (T/(OUT+'-'+label)).open('xb') as f:f.write(git(*args))
with (T/(OUT+'.sha')).open('x') as f:f.write(head+'\n')
print(head)

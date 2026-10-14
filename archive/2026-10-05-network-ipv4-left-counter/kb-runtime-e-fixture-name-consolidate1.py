import hashlib,json,os,pathlib,subprocess
tracking=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
repo=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
old='f6d2c080469b224ac77765aecd76a6d531358363'; base='0ff827df13e82dfab4b536ff29979280f264e8f5'; parent='5b987ca60567076e63095e0c79c84cfc403610fc'; branch='2026-10-05-network-ipv4-left-counter'; path='test/fixtures/kb-config.json'
def git(*args):return subprocess.check_output(['git','-C',str(repo),*args])
def write(suffix,data):
 with (tracking/('kb-runtime-e-fixture-name-consolidated.'+suffix)).open('xb') as f:f.write(data)
assert git('rev-parse','HEAD').decode().strip()==old
assert git('rev-parse','HEAD^').decode().strip()==parent
assert git('branch','--show-current').decode().strip()==branch
assert git('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/dev-workspace.git'
assert git('diff','--cached','--name-only')==b''
assert git('status','--porcelain=v1','--untracked-files=all')==(' M '+path+'\n').encode()
fixture=(repo/path).read_bytes(); original=git('show',old+':'+path)
assert fixture==original.replace(b'.aitherdev.int.vpsfree.cz',b'.example.test')
assert hashlib.sha256(fixture).hexdigest()=='299facc59c5e9b94d8f808381e2bc59f495421c152b5531114c59272c7370d27'
json.loads(fixture)
subprocess.run(['sha256sum','--check',str(tracking/'kb-runtime-e-fixture-name-fix1.sha256')],check=True,stdout=subprocess.DEVNULL)
assert not subprocess.run(['git','-C',str(repo),'config','--get','core.hooksPath'],stdout=subprocess.PIPE).stdout
hooks=pathlib.Path(git('rev-parse','--git-path','hooks').decode().strip())
assert all(p.name.endswith('.sample') for p in hooks.iterdir() if p.is_file())
tracked=git('ls-files','-z').split(b'\0')
frameworks={b'.overcommit.yml',b'.pre-commit-config.yaml',b'lefthook.yml',b'lefthook.yaml',b'.husky',b'.huskyrc',b'.huskyrc.json'}
assert not any(n.split(b'/')[0] in frameworks for n in tracked)
assert not any(b'aitherdev' in n.lower() or b'aitherdev' in (repo/os.fsdecode(n)).read_bytes().lower() for n in tracked if n and (repo/os.fsdecode(n)).is_file())
subprocess.run(['git','-C',str(repo),'fetch','origin','master'],check=True)
assert git('rev-parse','origin/master').decode().strip()==base
assert git('ls-remote','--heads','origin','refs/heads/'+branch).decode().strip()==old+'\trefs/heads/'+branch
write('old.full.diff',git('diff','--binary','--full-index',base,old));write('old.history',git('log','--reverse','--format=%H %s',base+'..'+old))
message=git('show','-s','--format=%B',old)
msg=tracking/'kb-runtime-e-fixture-name-provider.message'
with msg.open('xb') as f:f.write(message)
subprocess.run(['git','-C',str(repo),'add','--',path],check=True)
assert git('diff','--cached','--name-only').decode()==path+'\n'
subprocess.run(['git','-C',str(repo),'diff','--cached','--check'],check=True)
expected=git('write-tree').decode().strip()
subprocess.run(['git','-C',str(repo),'commit','--amend','-F',str(msg)],check=True)
head=git('rev-parse','HEAD').decode().strip()
assert git('rev-parse','HEAD^').decode().strip()==parent
assert git('rev-parse','HEAD^{tree}').decode().strip()==expected
assert git('status','--porcelain=v1','--untracked-files=all')==b''
assert git('diff','--name-only',old,head).decode()==path+'\n'
assert git('show',head+':'+path)==fixture
assert git('rev-list','--count',base+'..'+head).decode().strip()=='2'
assert git('rev-list','--merges',base+'..'+head)==b''
write('head.sha',(head+'\n').encode());write('tree.sha',(expected+'\n').encode());write('full.diff',git('diff','--binary','--full-index',base,head));write('history',git('log','--reverse','--format=%H %s',base+'..'+head));write('correction.diff',git('diff','--binary','--full-index',old,head))
write('proof.json',(json.dumps({'old':old,'head':head,'base':base,'parent':parent,'tree':expected,'only_path':path,'replacement_count':original.count(b'.aitherdev.int.vpsfree.cz'),'local_ci':False,'normal_hooks':True,'review_policy':'step9 direct source-only fixture correction; prior review remains exactf6'},indent=2)+'\n').encode())
print(head)

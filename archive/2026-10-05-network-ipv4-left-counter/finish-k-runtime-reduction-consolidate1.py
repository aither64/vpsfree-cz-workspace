from pathlib import Path
import subprocess,json,hashlib
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
R=T.parent.parent/'worktrees'/T.name/'vpsfree-kb-contracts-runtime'
O=R.parent/'vpsfree-kb-contracts'
base='873758fd6aec0c03f50a94600e0ceab97946f255'
old='922e71e5eb75b6eb416bf55e39160e9a7236e654'
first=['680e0b1d937fac7df3f6f99f002ed01c09a96fdc','d9cbed0c61929353e17b77b90cacd67e7c192a69']
paths=['README.md','cluster/nix/test.nix','cluster/runtime-contract.md','docs/webui-change-workflow.md','tools/runtime-verify.rb','tools/test-runtime-verify.rb']
branch='2026-10-05-network-ipv4-left-counter'
def g(*a,repo=R):
 p=subprocess.run(['git',*a],cwd=repo,capture_output=True,check=True)
 if p.stderr: print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(suffix,data):
 with (T/('finish-k-runtime-reduction-'+suffix)).open('xb') as f:f.write(data)
assert g('rev-parse','HEAD').decode().strip()==old
assert g('rev-parse','origin/master').decode().strip()==base
assert g('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/vpsfree-kb-contracts.git'
assert g('diff','--cached','--binary')==b'' and g('ls-files','--others','--exclude-standard')==b''
assert sorted(g('diff','--name-only').decode().splitlines())==sorted(paths)
expected=(T/'finish-k-runtime-reduction-source1.full.diff').read_bytes()
assert g('diff','--binary','--full-index')==expected
prose=json.loads((T/'finish-runtime-reduction-prose1.json').read_text())
for name,digest in prose['owners'].items(): assert hashlib.sha256((R/name).read_bytes()).hexdigest()==digest,name
assert g('rev-parse','HEAD',repo=O).decode().strip()==old and g('status','--porcelain',repo=O)==b''
names=g('ls-files').decode().splitlines()
hooks=Path(g('rev-parse','--git-path','hooks').decode().strip());hooks=hooks if hooks.is_absolute() else R/hooks
assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','config','--get','core.hooksPath'],cwd=R,capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in names)
protected={n:hashlib.sha256(g('show',old+':'+n)).hexdigest() for n in names if n not in paths}
assert g('rev-list','--reverse',base+'..HEAD').decode().splitlines()==first+[old]
for suffix in ['', '-kb-runtime']:
 remote=g('ls-remote','origin','refs/heads/'+branch+suffix)
 assert remote.decode()==old+'\trefs/heads/'+branch+suffix+'\n'
 save('remote-before'+('runtime' if suffix else 'original')+'.txt',remote)
save('old.history',g('log','--reverse','--format=fuller',base+'..HEAD'))
save('old.diff',g('diff','--binary','--full-index',base,'HEAD'))
g('update-ref','refs/heads/preserve/finish-generator-g12',old,'0'*40)
g('add','--',*paths)
assert g('diff','--cached','--binary','--full-index')==expected and g('diff','--binary')==b''
expected_tree=g('write-tree').decode().strip();save('staged.diff',expected)
message=T/'finish-k-runtime-reduction-source1.verifier.message'
assert all(len(line)<=80 for line in message.read_text().splitlines())
print(g('commit','--amend','-F',str(message)).decode(),flush=True)
# The historical verifier approach is superseded. Fold its final replacement
# into the owning portable runtime instead of keeping the discarded approach
# as an intermediate unmerged feature commit.
print(g('-c','sequence.editor=python3 '+str(T/'finish-k-runtime-reduction-sequence1.py'),
    '-c','rebase.updateRefs=false','rebase','-i',base).decode(),flush=True)
print(g('commit','--amend','-F',str(T/'finish-k-runtime-reduction-owning.message')).decode(),flush=True)
head=g('rev-parse','HEAD').decode().strip();tree=g('rev-parse','HEAD^{tree}').decode().strip()
series=g('rev-list','--reverse',base+'..HEAD').decode().splitlines()
assert series==[first[0],head] and tree==expected_tree and not g('status','--porcelain')
assert g('diff','--binary','--full-index',old,head)==expected
for name,digest in protected.items():assert hashlib.sha256(g('show',head+':'+name)).hexdigest()==digest,name
g('restore','--source='+head,'--staged','--worktree','--',*paths,repo=O)
g('update-ref','refs/heads/'+branch,head,old)
assert g('rev-parse','HEAD',repo=O).decode().strip()==head and g('status','--porcelain',repo=O)==b''
save('final.head',(head+'\n').encode());save('final.history',g('log','--reverse','--format=fuller',base+'..HEAD'))
save('final.diff',g('diff','--binary','--full-index',base,'HEAD'))
save('range-diff',g('range-diff',base+'..'+old,base+'..HEAD'))
proof={'old_head':old,'head':head,'tree':tree,'base':base,'series':series,'scope':paths,'staged_diff_sha256':hashlib.sha256(expected).hexdigest(),'normal_commits_and_hooks':True,'clean_original_and_runtime':True,'publication':'pending','hosted':'pending','real_operations':'held'}
save('commit-proof.json',(json.dumps(proof,indent=2)+'\n').encode());print(json.dumps(proof),flush=True)

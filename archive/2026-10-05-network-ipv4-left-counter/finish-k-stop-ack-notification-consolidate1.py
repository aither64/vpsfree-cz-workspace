from pathlib import Path
import subprocess,json,hashlib,shlex
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-kb-contracts-runtime';O=R.parent/'vpsfree-kb-contracts'
base='873758fd6aec0c03f50a94600e0ceab97946f255';old='29b17bf4bb151fbbb6b693c559cb16a196fa41c5';owner='b301c4a1976a0827eac826cdb1f98ca1e33389f4'
paths=['cluster/lib/devcluster_runner.rb','cluster/runtime-contract.md','tools/test-machine.rb']
def g(*a,repo=R):
 p=subprocess.run(['git',*a],cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr:print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(suffix,data):
 with(T/('finish-k-stop-ack-notification-'+suffix)).open('xb')as f:f.write(data)
assert g('rev-parse','HEAD').decode().strip()==old
assert g('rev-parse','origin/master').decode().strip()==base
assert g('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/vpsfree-kb-contracts.git'
assert g('diff','--cached','--binary')==b''
assert g('ls-files','--others','--exclude-standard')==b''
expected=(T/'finish-k-stop-ack-notification-source1.full.diff').read_bytes()
assert g('diff','--binary','--full-index')==expected
assert g('rev-parse','HEAD',repo=O).decode().strip()==old and g('status','--porcelain',repo=O)==b''
save('old.history',g('log','--reverse','--format=fuller',base+'..HEAD'))
save('old.diff',g('diff','--binary','--full-index',base,'HEAD'))
verify_message=g('show','-s','--format=%B',old)
verify_patch=g('show',old,'--pretty=format:','--binary')
p=subprocess.run(['git','patch-id','--stable'],input=verify_patch,stdout=subprocess.PIPE,check=True)
patch_id=p.stdout.decode().split()[0]
g('update-ref','refs/heads/preserve/finish-generator-29b',old,'0'*40)
g('add','--',*paths)
assert g('diff','--cached','--binary','--full-index')==expected
assert g('diff','--binary')==b''
expected_tree=g('write-tree').decode().strip()
save('staged1.diff',g('diff','--cached','--binary','--full-index'))
print(g('commit','-F',str(T/'finish-k-stop-ack-notification-fixup1.message')).decode(),flush=True)
editor='python3 '+shlex.quote(str(T/'finish-k-stop-ack-notification-rebase-editor1.py'))
print(g('-c','sequence.editor='+editor,'-c','rebase.updateRefs=false','rebase','-i','--autosquash',base).decode(),flush=True)
head=g('rev-parse','HEAD').decode().strip();tree=g('rev-parse','HEAD^{tree}').decode().strip()
series=g('rev-list','--reverse',base+'..HEAD').decode().splitlines()
assert len(series)==3 and series[0]=='680e0b1d937fac7df3f6f99f002ed01c09a96fdc'
assert not g('rev-list','--merges',base+'..HEAD') and g('status','--porcelain')==b''
assert tree==expected_tree
assert g('diff','--binary','--full-index',old,head)==expected
assert g('show','-s','--format=%B',head)==verify_message
nowpatch=g('show',head,'--pretty=format:','--binary')
assert subprocess.run(['git','patch-id','--stable'],input=nowpatch,stdout=subprocess.PIPE,check=True).stdout.decode().split()[0]==patch_id
assert g('show','-s','--format=%B',series[1]).rstrip()==(T/'finish-k-stop-ack-notification-runtime-amend1.message').read_bytes().rstrip()
# Synchronize only the three owned paths in the clean same-session companion.
g('restore','--source='+head,'--staged','--worktree','--',*paths,repo=O)
g('update-ref','refs/heads/2026-10-05-network-ipv4-left-counter',head,old)
assert g('rev-parse','HEAD',repo=O).decode().strip()==head and g('status','--porcelain',repo=O)==b''
save('final.head',(head+'\n').encode());save('final.history',g('log','--reverse','--format=fuller',base+'..HEAD'));save('final.diff',g('diff','--binary','--full-index',base,'HEAD'))
save('range-diff',g('range-diff',base+'..'+old,base+'..HEAD'))
proof={'old_head':old,'head':head,'tree':tree,'base':base,'series':series,'staged_diff_sha256':hashlib.sha256(expected).hexdigest(),'verifier_patch_id_preserved':patch_id,'normal_commits_and_hooks':True,'clean_original_and_runtime':True,'publication':'pending','hosted':'pending','real_operations':'held'}
save('commit1-proof.json',(json.dumps(proof,indent=2)+'\n').encode());print(json.dumps(proof),flush=True)

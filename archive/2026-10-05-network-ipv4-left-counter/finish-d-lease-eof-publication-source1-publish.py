from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'dev-workspace'
old='b1ec1bf1c3bc6413b066816ca58468b67ad5e5a6';base='c51ba3c0ca0d41d237ef71c56accd564beb70a33';first='730d33e12a01a738e16fec4c51cd9ce4a19c69c4';owner='test/workspace_host/commands_and_locks_test.rb';P='finish-d-lease-eof-publication-source1';branch=T.name
GIT='/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git'
def g(*a):
 p=subprocess.run([GIT,*a],cwd=R,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr:print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(suffix,data):
 with(T/(P+'-'+suffix)).open('xb')as f:f.write(data)
def patchid(sha):return subprocess.check_output([GIT,'patch-id','--stable'],input=g('show',sha,'--pretty=format:','--binary')).decode().split()[0]
assert json.loads((T/(P+'-acceptance.json')).read_text())['source_accepted']
assert g('rev-parse','HEAD').decode().strip()==old and g('status','--porcelain')==(' M '+owner+'\n').encode() and not g('diff','--cached','--binary')
assert g('remote','get-url','origin').decode().strip()=='git@github.com:aither64/dev-workspace.git'
# Original consumed package retained outside the final series; no default integration.
g('update-ref','refs/heads/preserve/finish-runtime-stream-before-eof-fixture',old,'0'*40)
series=g('rev-list','--reverse',base+'..HEAD').decode().splitlines();assert len(series)==3 and series[0]==first
messages=[g('show','-s','--format=%B',sha)for sha in series];unchanged_patches=[patchid(sha)for sha in series[1:]]
names=g('ls-files').decode().splitlines();protected={n:g('ls-tree',old,'--',n)for n in names if n!=owner}
hooks=Path(g('rev-parse','--git-path','hooks').decode().strip());hooks=hooks if hooks.is_absolute()else R/hooks
assert not [p for p in hooks.iterdir()if p.is_file()and not p.name.endswith('.sample')]
assert subprocess.run([GIT,'config','--get','core.hooksPath'],cwd=R,capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'}or '/.husky/'in'/'+n for n in names)
g('fetch','origin','master')
save('current-upstream.txt',g('rev-parse','origin/master'))
# Scope is fixture publication on the accepted selected package baseline. Upstream feature/input advance is recorded, not silently adopted.
assert g('merge-base','origin/master',old).decode().strip()==base
expected_delta=g('diff','--binary','--full-index');assert expected_delta==(T/(P+'.diff')).read_bytes()
g('add','--',owner);assert g('diff','--cached','--binary','--full-index')==expected_delta
expected_tree=g('write-tree').decode().strip();save('staged.diff',expected_delta)
msg=T/(P+'-fixup.message')
with msg.open('x')as f:f.write('fixup! cluster: mediate capture leases through the generation guard\n\nPublish the fixture EOF marker only after its complete payload is closed,\nso early observers retain the exact lease and generation-guard assertions.\n')
print(g('commit','-F',str(msg)).decode(),flush=True)
print(g('-c','sequence.editor=true','-c','rebase.updateRefs=false','rebase','-i','--autosquash',base).decode(),flush=True)
head=g('rev-parse','HEAD').decode().strip();tree=g('rev-parse','HEAD^{tree}').decode().strip();newseries=g('rev-list','--reverse',base+'..HEAD').decode().splitlines()
assert tree==expected_tree and len(newseries)==3 and not g('rev-list','--merges',base+'..HEAD')and not g('status','--porcelain')
assert [g('show','-s','--format=%B',x)for x in newseries]==messages
assert [patchid(x)for x in newseries[1:]]==unchanged_patches
assert g('diff','--binary','--full-index',old,head)==expected_delta
for n,b in protected.items():assert g('ls-tree','HEAD','--',n)==b,n
assert g('ls-remote','origin','refs/heads/'+branch).decode()==old+'\trefs/heads/'+branch+'\n'
save('final.head',(head+'\n').encode());save('final.diff',g('diff','--binary','--full-index',base,'HEAD'));save('final.history',g('log','--reverse','--format=fuller',base+'..HEAD'));save('range-diff',g('range-diff',base+'..'+old,base+'..HEAD'))
save('push.log',g('push','--force-with-lease=refs/heads/'+branch+':'+old,'origin',head+':refs/heads/'+branch));remote=g('ls-remote','origin','refs/heads/'+branch);assert remote.decode()==head+'\trefs/heads/'+branch+'\n';save('remote.txt',remote)
proof={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'old':old,'head':head,'tree':tree,'base':base,'series':newseries,'normal_commits':True,'protected_count':len(protected),'source_delta_exact':True,'unrelated2patches_and3messages_preserved':True,'default_integration':False,'publication':'exact SSH feature ref','hosted':'unproved'}
save('proof.json',(json.dumps(proof,indent=2)+'\n').encode());print(json.dumps(proof),flush=True)

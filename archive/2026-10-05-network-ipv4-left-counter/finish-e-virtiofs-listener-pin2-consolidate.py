from pathlib import Path
import subprocess,json,hashlib,runpy
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-dev-workspace';K=R.parent/'vpsfree-kb-contracts-runtime';D=R.parent/'dev-workspace'
old='874adbd3f477d04f0c81f52afc8d777b91814187';base='3e5dc4681b0343ec236c3f3dfc0d6f725577c376';first='f2b3f6a56424386902c93c614902c14ca8181285';oldk='4d9c47923d6d5cbc2e1e4147e4fcbbf203cd9e89';oldd='b1ec1bf1c3bc6413b066816ca58468b67ad5e5a6';headd='91c47ad2d6205b6c3275701855bffed190c51323';headk=(T/'finish-k-virtiofs-fixture-config-fix1-final.head').read_text().strip();branch='2026-10-05-network-ipv4-left-counter'
def g(*a,repo=R):
 p=subprocess.run(['/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git',*a],cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr:print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(suffix,data):
 with(T/('finish-e-virtiofs-listener-pin2-'+suffix)).open('xb')as f:f.write(data)
assert g('rev-parse','HEAD').decode().strip()==old and g('rev-parse','origin/master').decode().strip()==base
assert g('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/dev-workspace.git'
assert g('status','--porcelain')==b' M flake.lock\n M flake.nix\n' and not g('diff','--cached','--binary')
assert (T/'finish-e-virtiofs-listener-pin2-generate1.exit').read_text().strip()=='0'
assert (R/'flake.nix').read_bytes()==(T/'finish-e-virtiofs-listener-pin2-before.flake.nix').read_bytes().replace(oldk.encode(),headk.encode()).replace(oldd.encode(),headd.encode())
assert (R/'flake.lock').read_bytes()==(T/'finish-e-virtiofs-listener-pin2-generated1.lock').read_bytes()
lib=runpy.run_path(str(T/'finish-e-generator-graph-lib1.py'));graph,resolve=lib['graph'],lib['resolve']
before=json.loads((T/'finish-e-virtiofs-listener-pin2-before.flake.lock').read_bytes());after=json.loads((R/'flake.lock').read_bytes())
assert graph(after,('kb-runtime',),owned_prefix=True)==graph(json.loads(g('show',headk+':flake.lock',repo=K)))
assert graph(after,('dev-workspace',),owned_prefix=True)==graph(json.loads(g('show','HEAD:flake.lock',repo=D)))
key=resolve(before,('kb-runtime',));assert key==resolve(after,('kb-runtime',))
expected=json.loads(json.dumps(before));selected=after['nodes'][key]
assert before['nodes'][key]['locked']['rev']==oldk
assert selected['locked']['rev']==selected['original']['rev']==headk
for field in ['rev','narHash','lastModified']:expected['nodes'][key]['locked'][field]=selected['locked'][field]
expected['nodes'][key]['original']['rev']=headk
dkey=resolve(before,('dev-workspace',));assert dkey==resolve(after,('dev-workspace',))
assert before['nodes'][dkey]['locked']['rev']==oldd
assert after['nodes'][dkey]['locked']['rev']==after['nodes'][dkey]['original']['rev']==headd
for field in ['rev','narHash','lastModified']:expected['nodes'][dkey]['locked'][field]=after['nodes'][dkey]['locked'][field]
expected['nodes'][dkey]['original']['rev']=headd
assert expected==after
for name in before['nodes'][before['root']]['inputs']:
 if name not in ['kb-runtime','dev-workspace']:assert graph(before,(name,))==graph(after,(name,))
save('graph.json',(json.dumps({'selected_k':selected,'selected_d':after['nodes'][resolve(after,('dev-workspace',))]['locked'],'k_own_graph_exact':True,'d_own_graph_exact':True,'whole_lock_only_k_d_selectors_changed':True,'unrelated_roots_and_follows_exact':True,'k_resolved_paths':len(graph(after,('kb-runtime',),True)),'d_resolved_paths':len(graph(after,('dev-workspace',),True))},indent=2)+'\n').encode())
provider_message=g('show','-s','--format=%B',old);input_message=g('show','-s','--format=%B',first)
patch=g('show',old,'--pretty=format:','--binary');patchid=subprocess.run(['git','patch-id','--stable'],input=patch,stdout=subprocess.PIPE,check=True).stdout.decode().split()[0]
names=g('ls-files').decode().splitlines();protected={n:hashlib.sha256(g('show',old+':'+n)).hexdigest() for n in names if n not in ['flake.nix','flake.lock']}
hooks=Path(g('rev-parse','--git-path','hooks').decode().strip());hooks=hooks if hooks.is_absolute() else R/hooks
assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','config','--get','core.hooksPath'],cwd=R,capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in names)
g('update-ref','refs/heads/preserve/finish-extension-virtiofs-before-fixture-pair',old,'0'*40)
save('old.history',g('log','--reverse','--format=fuller',base+'..HEAD'));save('old.diff',g('diff','--binary','--full-index',base,'HEAD'))
delta=g('diff','--binary','--full-index');g('add','--','flake.nix','flake.lock');assert g('diff','--cached','--binary','--full-index')==delta
expected_tree=g('write-tree').decode().strip();save('staged.diff',delta)
message=T/'finish-e-virtiofs-listener-pin2-fixup.message'
with message.open('x')as f:f.write('fixup! flake: pin portable KB and streaming workspace runtimes\n\nSelect the corrected virtiofs and EOF fixtures while preserving owning\nruntime graphs and provider implementation.\n')
print(g('commit','-F',str(message)).decode(),flush=True)
print(g('-c','sequence.editor=true','-c','rebase.updateRefs=false','rebase','-i','--autosquash',base).decode(),flush=True)
head=g('rev-parse','HEAD').decode().strip();tree=g('rev-parse','HEAD^{tree}').decode().strip();series=g('rev-list','--reverse',base+'..HEAD').decode().splitlines()
assert tree==expected_tree and len(series)==2 and not g('rev-list','--merges',base+'..HEAD') and not g('status','--porcelain')
assert g('show','-s','--format=%B',head)==provider_message and g('show','-s','--format=%B',series[0])==input_message
assert subprocess.run(['git','patch-id','--stable'],input=g('show',head,'--pretty=format:','--binary'),stdout=subprocess.PIPE,check=True).stdout.decode().split()[0]==patchid
for n,h in protected.items():assert hashlib.sha256(g('show','HEAD:'+n)).hexdigest()==h,n
assert g('diff','--binary','--full-index',old,head)==delta
assert g('ls-remote','origin','refs/heads/'+branch).decode()==old+'\trefs/heads/'+branch+'\n'
save('final.head',(head+'\n').encode());save('final.history',g('log','--reverse','--format=fuller',base+'..HEAD'));save('final.diff',g('diff','--binary','--full-index',base,'HEAD'));save('range-diff',g('range-diff',base+'..'+old,base+'..HEAD'))
save('push.log',g('push','--force-with-lease=refs/heads/'+branch+':'+old,'origin',head+':refs/heads/'+branch))
remote=g('ls-remote','origin','refs/heads/'+branch);assert remote.decode()==head+'\trefs/heads/'+branch+'\n';save('remote.txt',remote)
proof={'old_head':old,'head':head,'tree':tree,'base':base,'series':series,'selected_k':headk,'provider_patch_id_preserved':patchid,'normal_commits_no_bypass':True,'whole_graph_exact':True,'clean':True,'publication':'exact SSH feature ref verified','hosted':'pending','real_operations':'held'}
save('proof.json',(json.dumps(proof,indent=2)+'\n').encode());print(json.dumps(proof),flush=True)

from pathlib import Path
import subprocess, json, hashlib, os, runpy
t=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
k=r.parent/'vpsfree-kb-contracts-runtime'
d=r.parent/'dev-workspace'
base='0ff827df13e82dfab4b536ff29979280f264e8f5'
old='02c77f1a46f5878054ada009e3e893a58e207568'
first='aa3bdee7b1c9d77bda5cb4de00b14b8bb96399bb'
g=(t/'finish-k-g4-stop-path-publish1-head').read_text().strip()
newd=(t/'finish-d-force-fixture-publish1-head').read_text().strip()
oldd='b1ec1bf1c3bc6413b066816ca58468b67ad5e5a6'
oldk='25539d837dea07f868b807db79dca436ab5075f7'
branch='2026-10-05-network-ipv4-left-counter'
def git(*args,input=None,repo=r):
 p=subprocess.run(['git','-C',str(repo),*args],input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr: print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(suffix,data):
 if isinstance(data,str): data=data.encode()
 with (t/('finish-e-generator-pin6-'+suffix)).open('xb') as f:f.write(data)
assert git('rev-parse','HEAD').decode().strip()==old
assert git('branch','--show-current').decode().strip()==branch
assert git('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/dev-workspace.git'
assert git('status','--porcelain=v1','--untracked-files=all')==b' M flake.lock\n M flake.nix\n'
assert git('diff','--cached','--binary')==b''
assert (r/'flake.lock').read_bytes()==(t/'finish-e-generator-pin6-generated.lock').read_bytes()
assert (r/'flake.nix').read_bytes()==(t/'finish-e-generator-pin6-before.flake.nix').read_bytes().replace(oldk.encode(),g.encode()).replace(oldd.encode(),newd.encode())
assert git('rev-parse','HEAD',repo=k).decode().strip()==g
assert git('rev-parse','HEAD',repo=d).decode().strip()==newd
git('fetch','origin','master')
assert git('rev-parse','origin/master').decode().strip()==base
assert git('ls-remote','origin','refs/heads/'+branch).decode()==old+'\trefs/heads/'+branch+'\n'
save('old.history',git('log','--reverse','--format=fuller',base+'..'+old))
save('old.diff',git('diff','--binary','--full-index',base,old))
git('update-ref','refs/heads/preserve/finish-e02c77',old,'0'*40)
assert (t/'finish-e-generator-pin6-generate.exit').read_text().strip()=='0'
assert (r/'flake.lock').read_bytes()==(t/'finish-e-generator-pin6-generated.lock').read_bytes()
lib=runpy.run_path(str(t/'finish-e-generator-graph-lib1.py'))
graph,resolve=lib['graph'],lib['resolve']
before=json.loads((t/'finish-e-generator-pin6-before.flake.lock').read_bytes())
after=json.loads((r/'flake.lock').read_bytes())
selected_k=json.loads(git('show',g+':flake.lock',repo=k))
selected_d=json.loads(git('show','HEAD:flake.lock',repo=d))
assert set(before['nodes'])==set(after['nodes'])
assert before['root']==after['root'] and before['version']==after['version']
assert graph(after,('kb-runtime',),owned_prefix=True)==graph(selected_k)
assert graph(after,('dev-workspace',),owned_prefix=True)==graph(selected_d)
root=before['nodes'][before['root']]['inputs']
assert root==after['nodes'][after['root']]['inputs']
for name in set(root)-{'kb-runtime'}: assert graph(before,(name,))==graph(after,(name,)),name
expected=json.loads(json.dumps(before))
changed=[]
for path,oldrev,newrev in [(('kb-runtime',),oldk,g)]:
 key=resolve(before,path); assert key==resolve(after,path)
 a,b=before['nodes'][key],after['nodes'][key]
 assert a['locked']['rev']==a['original']['rev']==oldrev
 assert b['locked']['rev']==b['original']['rev']==newrev
 for field in ['rev','narHash','lastModified']: expected['nodes'][key]['locked'][field]=b['locked'][field]
 expected['nodes'][key]['original']['rev']=newrev
 changed.append({'path':list(path),'node':key,'locked':b['locked']})
assert expected==after,'whole-lock widened; candidate retained'
save('graph.json',json.dumps({'changes':changed,'k_own_graph_exact':True,'selected_d_graph_exact':True,'other_root_graphs_exact':True,'whole_lock_exact':True},indent=2)+'\n')
assert git('status','--porcelain=v1','--untracked-files=all')==b' M flake.lock\n M flake.nix\n'
assert git('diff','--cached','--binary')==b''
save('generated.diff',git('diff','--binary','--full-index'))
provider_message=git('show','-s','--format=%B',old)
input_message=git('show','-s','--format=%B',first)
expected_files={name:hashlib.sha256(git('show',old+':'+name)).hexdigest() for name in git('ls-files').decode().splitlines() if name not in ['flake.nix','flake.lock']}
hooks=Path(git('rev-parse','--git-path','hooks').decode().strip())
if not hooks.is_absolute(): hooks=r/hooks
assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','-C',str(r),'config','--get','core.hooksPath'],capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in git('ls-files').decode().splitlines())
final_flake=(r/'flake.nix').read_bytes()
final_lock=(r/'flake.lock').read_bytes()
# The correction delta contains only the URL and generated lock; autosquash
# applies that delta to the original input commit and replays the provider.
for name,content in [('flake.nix',final_flake),('flake.lock',final_lock)]:
 blob=git('hash-object','-w','--stdin',input=content).decode().strip()
 git('update-index','--cacheinfo','100644,'+blob+','+name)
assert git('diff','--cached','--name-only')==b'flake.lock\nflake.nix\n'
save('input.staged.diff',git('diff','--cached','--binary','--full-index'))
message=t/'finish-e-generator-pin6-fixup.message'
with message.open('xb') as f:f.write(b'fixup! flake: pin portable KB and streaming workspace runtimes\n\nSelect the corrected atomic-reader capture generator while retaining its\nown dependency graph, provider and generic dispatcher.\n')
print(git('commit','-F',str(message)).decode(),flush=True)
assert git('diff','--binary')==b''
print(git('-c','sequence.editor=true','-c','rebase.updateRefs=false','rebase','-i','--autosquash',base).decode(),flush=True)
head=git('rev-parse','HEAD').decode().strip()
commits=git('rev-list','--reverse',base+'..HEAD').decode().splitlines()
assert len(commits)==2 and git('rev-list','--merges',base+'..HEAD')==b''
assert git('status','--porcelain=v1','--untracked-files=all')==b''
assert git('show','-s','--format=%B',head)==provider_message
assert git('show','-s','--format=%B',commits[0])==input_message
assert (r/'flake.nix').read_bytes()==final_flake and (r/'flake.lock').read_bytes()==final_lock
assert git('show',commits[0]+':flake.nix')==git('show',first+':flake.nix').replace(oldk.encode(),g.encode()).replace(oldd.encode(),newd.encode())
for name,digest in expected_files.items(): assert hashlib.sha256(git('show','HEAD:'+name)).hexdigest()==digest,name
save('head',head+'\n')
save('history',git('log','--reverse','--format=fuller',base+'..HEAD'))
save('final.diff',git('diff','--binary','--full-index',base,'HEAD'))
save('range-diff',git('range-diff',base+'..'+old,base+'..HEAD'))
save('proof.json',json.dumps({'base':base,'old':old,'head':head,'tree':git('rev-parse','HEAD^{tree}').decode().strip(),'commits':commits,'provider_content_and_message_exact':True,'graph_exact':True,'normal_hooks':True,'local_ci':False},indent=2)+'\n')
# Fresh default/ref guards immediately before ordinary exact feature push.
git('fetch','origin','master')
assert git('rev-parse','origin/master').decode().strip()==base
git('merge-base','--is-ancestor',base,head)
assert git('ls-remote','origin','refs/heads/'+branch).decode()==old+'\trefs/heads/'+branch+'\n'
save('push.log',git('push','--force-with-lease=refs/heads/'+branch+':'+old,'origin',head+':refs/heads/'+branch))
remote=git('ls-remote','origin','refs/heads/'+branch)
assert remote.decode()==head+'\trefs/heads/'+branch+'\n'
save('remote',remote)
print('Published exact interim E/G/corrected-D composition: '+head,flush=True)

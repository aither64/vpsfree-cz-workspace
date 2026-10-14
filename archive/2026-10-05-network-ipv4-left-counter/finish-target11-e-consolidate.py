from pathlib import Path
import subprocess, json, hashlib, runpy
T = Path(__file__).resolve().parent
R = T.parents[1] / 'worktrees' / T.name / 'vpsfree-dev-workspace'
base = '7157c8098dcf60127aa4df823fab82b4185ad22a'
old = '78463762fcf79b94ae026ea1acc3a36354938cd1'
new_d = (T/'finish-target11-d.head').read_text().strip()
def git(*args, repo=R):
    p = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, check=True)
    if p.stderr: print(p.stderr.decode(), end='', flush=True)
    return p.stdout
def save(name, data):
    if isinstance(data, str): data = data.encode()
    with (T/('finish-target11-e-'+name)).open('xb') as f: f.write(data)
assert git('rev-parse','HEAD').decode().strip() == old
assert git('status','--porcelain') == b' M flake.lock\n M flake.nix\n'
assert not git('diff','--cached')
assert (T/'finish-target11-e-generate.exit').read_text().strip() == '0'
before = json.loads((T/'finish-target11-e-before.flake.lock').read_bytes())
after = json.loads((R/'flake.lock').read_bytes())
lib = runpy.run_path(str(T/'finish-e-generator-graph-lib1.py'))
graph, resolve = lib['graph'], lib['resolve']
node = resolve(after, ('dev-workspace',))
assert after['nodes'][node]['locked']['rev'] == new_d
changed = [k for k in before['nodes'] if before['nodes'][k] != after['nodes'][k]]
assert set(before['nodes']) == set(after['nodes'])
assert set(changed) == {node, resolve(after, ('dev-workspace','codex-web'))}
assert before['root'] == after['root'] and before['version'] == after['version']
assert graph(after, ('dev-workspace',), True) == graph(json.loads(git('show',new_d+':flake.lock',repo=R.parent/'dev-workspace')))
assert graph(after, ('kb-runtime',), True) == graph(json.loads(git('show','HEAD:flake.lock',repo=R.parent/'vpsfree-kb-contracts-runtime')))
for name in before['nodes'][before['root']]['inputs']:
    if name != 'dev-workspace': assert graph(before,(name,)) == graph(after,(name,)), name
old_d = '16d949b39e162870cc21a6f23d2d138b2e642887'
assert (R/'flake.nix').read_bytes() == (T/'finish-target11-e-before.flake.nix').read_bytes().replace(old_d.encode(),new_d.encode())
def normalized(c):
    return b'\n'.join(l for l in git('show','--format=','--binary','--full-index',c).splitlines() if not l.startswith(b'index '))
provider = normalized(old)
provider_message = git('show','-s','--format=%B',old)
inputs_message = git('show','-s','--format=%B',old+'~1')
protected = {n: hashlib.sha256(git('show',old+':'+n)).hexdigest() for n in git('ls-files').decode().splitlines() if n not in ('flake.nix','flake.lock')}
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in git('ls-files').decode().splitlines())
save('generated.diff',git('diff','--binary','--full-index'))
git('diff','--check')
message = T/'finish-target11-e-fixup.message'
message.write_text('fixup! flake: pin portable KB and streaming workspace runtimes\n\nSelect the rebased streaming runtime while preserving current upstream\nprovider admission, recovery contracts and the independent KB graph.\n')
git('add','--','flake.nix','flake.lock')
print(git('commit','-F',str(message)).decode(),flush=True)
print(git('-c','sequence.editor=true','-c','rebase.updateRefs=false','rebase','-i','--autosquash',base).decode(),flush=True)
head = git('rev-parse','HEAD').decode().strip()
assert not git('status','--porcelain')
assert git('rev-list','--count',base+'..HEAD').decode().strip() == '2'
assert normalized(head) == provider
assert git('show','-s','--format=%B',head) == provider_message
assert git('show','-s','--format=%B',head+'~1') == inputs_message
for name,digest in protected.items(): assert hashlib.sha256(git('show',head+':'+name)).hexdigest() == digest, name
save('range-diff',git('range-diff','--no-color',base+'..'+old,base+'..'+head))
save('head',head+'\n')
save('proof.json',json.dumps({'base':base,'old':old,'head':head,'tree':git('rev-parse','HEAD^{tree}').decode().strip(),'selected_D':new_d,'selected_K':'706b9d8c18edde528af4fb5279786491aedd47fa','D_narHash':after['nodes'][node]['locked']['narHash'],'changed_nodes':changed,'whole_owning_K_D_graphs_equal':True,'all_non_D_sibling_graphs_equal':True,'provider_normalized_bytes_message_equal':True,'two_consolidated_commits':True,'protected_paths':len(protected),'local_suite_run':False,'quick_check':'git diff --check passed','hooks':'No declared hook framework; no bypass'},indent=2)+'\n')
print(head,flush=True)

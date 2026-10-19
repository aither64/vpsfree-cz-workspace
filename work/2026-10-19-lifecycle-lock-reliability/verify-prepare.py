from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json, subprocess, time, os
tracking = Path(__file__).resolve().parent
workspace = tracking.parents[1]
sources = workspace / 'worktrees' / tracking.name
inventory = json.loads((tracking / 'branch-inventory.json').read_text())
for name, item in inventory.items():
    assert subprocess.check_output(['git','rev-parse','HEAD'], cwd=sources/name, text=True).strip() == item['head']
    assert not subprocess.check_output(['git','status','--porcelain'], cwd=sources/name, text=True)
assert (tracking/'final-review.md').is_file()
env = os.environ | {'DEV_SESSION_SLUG':tracking.name,'DEV_SESSION_WORKSPACE':str(workspace),'TMPDIR':'/tmp'}
def run(name, cmd, cwd):
    started = time.monotonic()
    with (tracking/(name+'.stdout')).open('w') as out, (tracking/(name+'.log')).open('w') as err:
        p = subprocess.run(cmd, cwd=cwd, env=env, stdout=out, stderr=err)
    result = {'name':name,'command':cmd,'exitStatus':p.returncode,'elapsed':time.monotonic()-started,'revisions':{n:i['head'] for n,i in inventory.items()}}
    (tracking/(name+'-result.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    return p.returncode
jobs = [
 ('packaged', ['nix','build','--no-link','--print-out-paths','--print-build-logs','.#checks.x86_64-linux.package','.#checks.x86_64-linux.session-archive-lifecycle'],sources/'dev-workspace'),
 ('machine-prepare',['nix','develop','--command','dev-session','coordination','prepare',tracking.name,'--as-is','--request',str(tracking/'machine-prepare-request.json'),'--json'],sources/'vpsfree-cz-configuration'),
 ('profile-prepare',['dev-session','coordination','prepare',tracking.name,'--as-is','--request',str(tracking/'profile-prepare-request.json'),'--json'],workspace),
]
with ThreadPoolExecutor(max_workers=3) as pool:
    statuses = list(pool.map(lambda args:run(*args),jobs))
raise SystemExit(next((s for s in statuses if s),0))

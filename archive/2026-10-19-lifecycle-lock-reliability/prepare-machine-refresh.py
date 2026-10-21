from pathlib import Path
import json,subprocess,os,time
out=Path(__file__).resolve().parent
workspace=out.parents[1]
config=workspace/'worktrees'/out.name/'vpsfree-cz-configuration'
assert (out/'config-refresh-review.md').exists()
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=config,text=True).strip()=='0067299ab9739f522fec0780cda98649ae630406'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=config,text=True)
cmd=['nix','develop','--command','dev-session','coordination','prepare',out.name,'--as-is','--request',str(out/'machine-refresh-prepare-request.json'),'--json']
start=time.monotonic()
with (out/'machine-refresh-prepare.stdout').open('w') as stdout,(out/'machine-refresh-prepare.log').open('w') as stderr:
    p=subprocess.run(cmd,cwd=config,stdout=stdout,stderr=stderr,env=os.environ|{'DEV_SESSION_SLUG':out.name,'DEV_SESSION_WORKSPACE':str(workspace),'TMPDIR':'/tmp'})
result={'exitStatus':p.returncode,'elapsed':time.monotonic()-start,'command':cmd,'configurationRevision':'0067299ab9739f522fec0780cda98649ae630406'}
(out/'machine-refresh-prepare-result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
raise SystemExit(p.returncode)

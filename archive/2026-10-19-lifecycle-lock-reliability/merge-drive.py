from pathlib import Path
import subprocess,os,json,time
out=Path(__file__).resolve().parent;root=out.parents[1]
cmd=['dev-session','coordination','integrate',out.name,'--as-is','--request',str(out/'merge-integration-request.json'),'--json']
start=time.monotonic()
with (out/'merge-drive.stdout').open('w') as stdout,(out/'merge-drive.log').open('w') as stderr:
    p=subprocess.run(cmd,cwd=root,env=os.environ|{'DEV_SESSION_SLUG':out.name,'DEV_SESSION_WORKSPACE':str(root)},stdout=stdout,stderr=stderr)
result={'exitStatus':p.returncode,'elapsed':time.monotonic()-start,'runId':json.loads((out/'merge-integration-request.json').read_text())['requestId']}
(out/'merge-drive-result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
raise SystemExit(p.returncode)

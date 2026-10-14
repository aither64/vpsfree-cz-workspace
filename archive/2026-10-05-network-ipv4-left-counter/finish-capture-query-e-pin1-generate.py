from pathlib import Path
import subprocess,os,json,hashlib
T=Path(__file__).resolve().parent
R=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
env={k:v for k,v in os.environ.items() if not k.startswith(('VPSADMIN_DEVCLUSTER_','VPSADMIN_KB_'))}
with (T/'finish-capture-query-e-pin1-generate.stdout').open('xb') as out,(T/'finish-capture-query-e-pin1-generate.stderr').open('xb') as err:
 r=subprocess.run(['/nix/store/iirndnicd13h4zjr8xwwj8hq2cghpfjn-nix-2.34.8/bin/nix','flake','update','kb-runtime'],cwd=R,env=env,stdout=out,stderr=err)
(T/'finish-capture-query-e-pin1-generate.exit').write_text(str(r.returncode)+'\n')
print(json.dumps({'native_exit':r.returncode,'lock_sha256':hashlib.sha256((R/'flake.lock').read_bytes()).hexdigest()}),flush=True)
raise SystemExit(r.returncode)

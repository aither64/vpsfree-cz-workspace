
from pathlib import Path
import subprocess,json,time,hashlib,shutil
repo=Path.cwd(); out=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-browser/prewrite-cancellation/diagnostics-implementation')
def run(name,argv):
 start=time.monotonic();r=subprocess.run(argv,capture_output=True);(out/(name+'.stdout')).write_bytes(r.stdout);(out/(name+'.stderr')).write_bytes(r.stderr);(out/(name+'.json')).write_text(json.dumps({'argv':argv,'cwd':str(repo),'exit':r.returncode,'wallSeconds':time.monotonic()-start},indent=2)+'\n');assert r.returncode==0,(name,r.stderr.decode());return r.stdout
paths={n:shutil.which(n) for n in ['go','gcc','ruby','node','git']};assert all(paths.values());(out/'nix-tools.json').write_text(json.dumps(paths,indent=2)+'\n')
run('gofmt',['gofmt','-w','portal/internal/web/retry_backend_browser_test.go'])
run('node-syntax',['node','--check','portal/internal/web/retry_backend_browser_test.cjs'])
run('diff-check',['git','diff','--check'])
run('compile-only',['go','-C','portal','test','-mod=readonly','./internal/web','-run','^$'])
print('gofmt, Node syntax, diff and compile-only PASS')

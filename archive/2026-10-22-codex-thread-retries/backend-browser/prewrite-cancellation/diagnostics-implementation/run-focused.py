
from pathlib import Path
import json,subprocess,time,hashlib
repo=Path.cwd(); out=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-browser/prewrite-cancellation/diagnostics-implementation')
def inputs():
 paths=subprocess.check_output(['git','ls-files','*.go'],text=True).splitlines()+['portal/go.mod','portal/go.sum','portal/internal/web/retry_backend_browser_test.cjs','flake.nix','flake.lock','nix/workspace-portal.nix'];return {p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in sorted(set(paths))}
before=inputs();(out/'quick-inputs-before.json').write_text(json.dumps(before,indent=2)+'\n')
for name,race in [('normal',False),('race',True)]:
 argv=['go','-C','portal','test','-mod=readonly']+(['-race'] if race else [])+['./internal/web','-run','^TestRetryBackendBrowserDiagnostics$','-count=1','-timeout=30s','-json'];start=time.monotonic()
 with (out/(name+'.stdout.jsonl')).open('xb') as stdout,(out/(name+'.stderr.log')).open('xb') as stderr:r=subprocess.run(argv,stdout=stdout,stderr=stderr)
 after=inputs();(out/(name+'-inputs-after.json')).write_text(json.dumps(after,indent=2)+'\n')
 events=[json.loads(line) for line in (out/(name+'.stdout.jsonl')).read_text().splitlines()];passed=[e['Test'] for e in events if e.get('Action')=='pass' and e.get('Test')];bad=[e for e in events if e.get('Action') in ('fail','build-fail','skip')];packages=[e for e in events if e.get('Action')=='pass' and not e.get('Test')]
 result={'argv':argv,'cwd':str(repo),'exit':r.returncode,'wallSeconds':time.monotonic()-start,'passed':passed,'passCount':len(passed),'failSkip':bad,'packages':packages,'beforeAfterInputsEqual':before==after,'inputCount':len(before)};(out/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
 assert r.returncode==0 and not bad and packages and len(passed)==13 and before==after,name+' failed; no automatic rerun'

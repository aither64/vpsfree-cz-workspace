
from pathlib import Path
import subprocess,json,hashlib,time,shutil,os
repo=Path.cwd();out=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-successor/root-retirement-discovery')
def run(name,argv):
 start=time.monotonic();r=subprocess.run(argv,capture_output=True);(out/(name+'.stdout')).write_bytes(r.stdout);(out/(name+'.stderr')).write_bytes(r.stderr);(out/(name+'.json')).write_text(json.dumps({'argv':argv,'exit':r.returncode,'seconds':time.monotonic()-start},indent=2)+'\n');assert r.returncode==0,name
run('final-gofmt',['gofmt','-w','portal/internal/workspacecodex/client.go','portal/internal/workspacecodex/client_test.go']);run('final-diff-check',['git','diff','--check'])
tools={n:shutil.which(n) for n in ['go','gcc','git']};assert all(tools.values());tools.update(GOFLAGS=os.environ.get('GOFLAGS'),GOWORK=os.environ.get('GOWORK'));assert tools['GOFLAGS']=='' and tools['GOWORK']=='off';(out/'final-nix-tools.json').write_text(json.dumps(tools,indent=2)+'\n')
paths=subprocess.check_output(['git','ls-files'],text=True).splitlines()
def inputs():return {p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in paths}
before=inputs();(out/'final-quick-inputs-before.json').write_text(json.dumps(before,indent=2)+'\n')
for name,race in [('final-normal',False),('final-race',True)]:
 argv=['go','-C','portal','test','-mod=readonly']+(['-race'] if race else [])+['./internal/workspacecodex','-run','^(TestRetireThread|TestRetirementDiscovery|TestProveArchivedRootThread)','-count=1','-timeout=30s','-json'];start=time.monotonic()
 with (out/(name+'.stdout.jsonl')).open('xb') as stdout,(out/(name+'.stderr')).open('xb') as stderr:r=subprocess.run(argv,stdout=stdout,stderr=stderr)
 after=inputs();(out/(name+'-inputs-after.json')).write_text(json.dumps(after,indent=2)+'\n');events=[json.loads(line) for line in (out/(name+'.stdout.jsonl')).read_text().splitlines()];passed=[e['Test'] for e in events if e.get('Action')=='pass' and e.get('Test')];bad=[e for e in events if e.get('Action') in ('fail','build-fail','skip')];packages=[e for e in events if e.get('Action')=='pass' and not e.get('Test')]
 receipt={'argv':argv,'cwd':str(repo),'exit':r.returncode,'seconds':time.monotonic()-start,'passed':passed,'passCount':len(passed),'bad':bad,'packages':packages,'inputsCount':len(before),'beforeAfterInputsEqual':before==after};(out/(name+'.json')).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True);assert r.returncode==0 and not bad and packages and before==after,name+' failed; no automatic rerun'

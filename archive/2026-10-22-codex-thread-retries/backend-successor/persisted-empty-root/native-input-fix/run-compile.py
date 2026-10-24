from pathlib import Path
import subprocess,json,hashlib,time,shutil,os
repo=Path.cwd();out=Path(__file__).parent
file='portal/cmd/workspace-portal/retire_empty_native_integration_test.go'
subprocess.run(['gofmt','-w',file],check=True);subprocess.run(['git','diff','--check'],check=True)
paths=subprocess.check_output(['git','ls-files'],text=True).splitlines()
def inputs():return {p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in paths}
before=inputs();(out/'inputs-before.json').write_text(json.dumps(before,indent=2)+'\n')
tools={n:shutil.which(n) for n in ['go','gcc','git']};assert all(tools.values());assert os.environ['GOFLAGS']=='' and os.environ['GOWORK']=='off';(out/'tools.json').write_text(json.dumps(tools,indent=2)+'\n')
argv=['go','-C','portal','test','-mod=readonly','-tags=live_switch_integration','./cmd/workspace-portal','-run','^$','-count=1','-timeout=30s','-json'];start=time.monotonic()
with (out/'compile.stdout.jsonl').open('xb') as stdout,(out/'compile.stderr').open('xb') as stderr:r=subprocess.run(argv,stdout=stdout,stderr=stderr)
after=inputs();(out/'inputs-after.json').write_text(json.dumps(after,indent=2)+'\n');events=[json.loads(l) for l in (out/'compile.stdout.jsonl').read_text().splitlines()];bad=[e for e in events if e.get('Action') in ('fail','build-fail','skip')];tests=[e for e in events if e.get('Test')];packages=[e for e in events if e.get('Action')=='pass' and not e.get('Test')]
receipt={'argv':argv,'exit':r.returncode,'seconds':time.monotonic()-start,'bad':bad,'testsRun':len(tests),'packages':packages,'inputCount':len(before),'inputsUnchanged':before==after};(out/'compile.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True);assert r.returncode==0 and not bad and not tests and packages and before==after

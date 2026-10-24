from pathlib import Path
import subprocess,json,time,hashlib
repo=Path.cwd();out=Path(__file__).resolve().parent
paths=['portal/internal/teamruntime/deletion.go','portal/internal/teamruntime/deletion_test.go']
assert not subprocess.check_output(['gofmt','-l',*paths])
subprocess.run(['git','diff','--check','--',*paths],check=True)
inputs={str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (repo/'portal').rglob('*.go')}
for name in ['portal/go.mod','portal/go.sum']:inputs[name]=hashlib.sha256((repo/name).read_bytes()).hexdigest()
cmd=['go','-C','portal','test','-mod=readonly','./internal/teamruntime','-run','^TestPrepareDelete','-count=1','-timeout=30s','-json'];start=time.monotonic()
with (out/'quick.stdout.jsonl').open('x') as stdout,(out/'quick.stderr').open('x') as stderr:r=subprocess.run(cmd,stdout=stdout,stderr=stderr)
passed=[];failed=[];skipped=[];packages=[]
for line in (out/'quick.stdout.jsonl').read_text().splitlines():
 e=json.loads(line)
 if e.get('Action')=='pass':
  if e.get('Test'):passed.append(e['Test'])
  else:packages.append(e.get('Elapsed'))
 if e.get('Action') in ('fail','build-fail'):failed.append(e.get('Test','package'))
 if e.get('Action')=='skip':skipped.append(e.get('Test','package'))
assert all(hashlib.sha256((repo/p).read_bytes()).hexdigest()==h for p,h in inputs.items())
record={'argv':cmd,'exit':r.returncode,'elapsed':time.monotonic()-start,'passedTestsAndSubtests':len(passed),'topNames':sorted(p for p in passed if '/' not in p),'packageElapsed':packages,'failed':failed,'skipped':skipped,'formatDiffPass':True,'goSourceInputs':inputs,'scope':'D1 focused teamruntime Go verification only; peer workspace-host/Ruby/docs not read or tested'}
(out/'quick.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k!='goSourceInputs'}));assert r.returncode==0 and len(passed)==40 and packages and not failed and not skipped

from pathlib import Path
import subprocess,json,time,hashlib,sys
repo=Path.cwd();out=Path(__file__).resolve().parent;label=sys.argv[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
subprocess.run(['gofmt','-w','portal/internal/web/retry_backend_browser_test.go'],check=True);subprocess.run(['git','diff','--check'],check=True)
inputs={str(p.relative_to(repo)):sha(p) for p in (repo/'portal').rglob('*.go')}
for p in ['portal/go.mod','portal/go.sum','portal/internal/web/retry_backend_browser_test.cjs']:inputs[p]=sha(repo/p)
cmd=['go','-C','portal','test','-mod=readonly','./internal/web','-run','^(TestRetryBackendBrowserFixtureConstruction|TestRetryBackendBrowserPolicyReplyLoss)$','-count=1','-timeout=30s','-json'];start=time.monotonic()
with (out/(label+'.stdout.jsonl')).open('x') as stdout,(out/(label+'.stderr')).open('x') as stderr:r=subprocess.run(cmd,stdout=stdout,stderr=stderr)
passed=[];failed=[];skipped=[];packages=[]
for line in (out/(label+'.stdout.jsonl')).read_text().splitlines():
 e=json.loads(line)
 if e.get('Action')=='pass':
  if e.get('Test'):passed.append(e['Test'])
  else:packages.append({'package':e['Package'],'elapsed':e.get('Elapsed')})
 if e.get('Action') in ('fail','build-fail'):failed.append(e.get('Test','package'))
 if e.get('Action')=='skip':skipped.append(e.get('Test','package'))
record={'argv':cmd,'exit':r.returncode,'elapsed':time.monotonic()-start,'passed':passed,'failed':failed,'skipped':skipped,'packages':packages,'inputsBefore':inputs,'inputsAfter':{p:sha(repo/p) for p in inputs}}
(out/(label+'.json')).write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k not in ('inputsBefore','inputsAfter')}),flush=True)
assert record['inputsBefore']==record['inputsAfter']
if label=='baseline':
 assert r.returncode==1 and set(failed)=={'TestRetryBackendBrowserPolicyReplyLoss/root','TestRetryBackendBrowserPolicyReplyLoss/member','TestRetryBackendBrowserPolicyReplyLoss','package'} and not skipped
else:
 assert r.returncode==0 and len(passed)==8 and len(packages)==1 and not failed and not skipped

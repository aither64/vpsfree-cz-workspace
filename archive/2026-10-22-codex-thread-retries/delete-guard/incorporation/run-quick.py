from pathlib import Path
import subprocess,json,time,re,concurrent.futures,hashlib
repo=Path.cwd();out=Path(__file__).resolve().parent
handoff=json.loads((out/'owner3-handoff.json').read_text())
changed_go=[r['path'] for r in handoff['files'] if r['path'].endswith('.go')]
assert not subprocess.check_output(['gofmt','-l',*changed_go]),'Go format changed'
subprocess.run(['git','diff','--check'],check=True)
with (out/'syntax.stdout').open('x') as stdout,(out/'syntax.stderr').open('x') as stderr:
 subprocess.run(['ruby','-c','libexec/dev-session'],stdout=stdout,stderr=stderr,check=True)
 subprocess.run(['node','--check','portal/internal/web/retry_backend_browser_test.cjs'],stdout=stdout,stderr=stderr,check=True)
names=re.findall(r'^\s*def (test_[A-Za-z0-9_]+)',(repo/'test/dev_session/deletion_recovery_test.rb').read_text(),re.M)
assert len(names)==25
selector='^(TestPrepareDelete.*|TestTeamPrepareDelete.*|TestRequireIdleAll.*|TestRetryBackendBrowserFixtureConstruction)$'
commands={
 'go':['go','-C','portal','test','-mod=readonly','./internal/teamruntime','./cmd/workspace-portal','./internal/web','-run',selector,'-count=1','-timeout=45s','-json'],
 'ruby':['ruby','test/dev_session_test.rb','--name','/\\A(?:'+'|'.join(names)+')\\z/']}
(out/'quick-plan.json').write_text(json.dumps({'commands':commands,'rubyNames':names,'scope':'Focused normal disposable checks only; no actual browser/fork/pressure/live/native daemon/build/CI'},indent=2)+'\n')
def run(name,command):
 start=time.monotonic()
 with (out/(name+'.stdout'+('.jsonl' if name=='go' else ''))).open('x') as stdout,(out/(name+'.stderr')).open('x') as stderr:r=subprocess.run(command,stdout=stdout,stderr=stderr)
 return name,{'command':command,'exit':r.returncode,'elapsed':time.monotonic()-start}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: results=dict(pool.map(lambda item:run(*item),commands.items()))
passed=[];skipped=[];failed=[];packages=[]
for line in (out/'go.stdout.jsonl').read_text().splitlines():
 e=json.loads(line);action=e.get('Action');test=e.get('Test')
 if action=='pass':
  if test:passed.append(test)
  else:packages.append({'package':e['Package'],'elapsed':e.get('Elapsed')})
 if action=='skip':skipped.append(test or e['Package'])
 if action in ('fail','build-fail'):failed.append(test or e['Package'])
text=(out/'ruby.stdout').read_text();match=re.search(r'(\d+) runs, (\d+) assertions, (\d+) failures, (\d+) errors, (\d+) skips',text)
ruby=list(map(int,match.groups())) if match else None
record={'results':results,'goPassedTopNames':sorted(t for t in passed if '/' not in t),'goPassedTestsAndSubtests':len(passed),'goPackages':packages,'goFailed':failed,'goSkipped':skipped,'rubySummary':ruby,'allEightAcceptedFileHashesMatch':all(hashlib.sha256((repo/r['path']).read_bytes()).hexdigest()==r['sha256'] for r in handoff['files']),'syntaxAndFormat':True}
(out/'quick.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
assert all(r['exit']==0 for r in results.values()) and not failed and not skipped and len(packages)==3
assert ruby==[25,158,0,0,0] and record['allEightAcceptedFileHashesMatch']

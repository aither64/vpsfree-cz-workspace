from pathlib import Path
import subprocess,json,hashlib,time,shutil,os,sys
repo=Path.cwd();out=Path(__file__).parent
paths=subprocess.check_output(['git','ls-files'],text=True).splitlines()
native='portal/cmd/workspace-portal/retire_empty_native_integration_test.go'
if (repo/native).exists() and native not in paths:paths.append(native)
def inputs():return {p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in paths}
mode=sys.argv[1]
files=['portal/internal/workspacecodex/client.go','portal/internal/workspacecodex/client_test.go']+([native] if (repo/native).exists() else [])
subprocess.run(['gofmt','-w']+files,check=True);subprocess.run(['git','diff','--check'],check=True)
toolmap={n:shutil.which(n) for n in ['go','gcc','git']};assert all(toolmap.values());assert os.environ['GOFLAGS']=='' and os.environ['GOWORK']=='off'
(out/(mode+'-tools.json')).write_text(json.dumps(toolmap,indent=2)+'\n')
before=inputs();(out/(mode+'-inputs-before.json')).write_text(json.dumps(before,indent=2)+'\n')
runs=[('red',False,'^TestRetireThreadPersistedEmptyRootAbsentFromDiscovery$',False)] if mode=='red' else [('normal',False,'^(TestRetireThread|TestRetirementDiscovery|TestProveMaterializedActiveThread|TestProveArchivedRootThread)',False),('race',True,'^(TestRetireThread|TestRetirementDiscovery|TestProveMaterializedActiveThread|TestProveArchivedRootThread)',False),('native-compile',False,'^$',True)]
for name,race,selector,native_compile in runs:
 argv=['go','-C','portal','test','-mod=readonly']+(['-race'] if race else [])+(['-tags=live_switch_integration'] if native_compile else [])+[('./cmd/workspace-portal' if native_compile else './internal/workspacecodex'),'-run',selector,'-count=1','-timeout=30s','-json']
 start=time.monotonic()
 with (out/(name+'.stdout.jsonl')).open('xb') as stdout,(out/(name+'.stderr')).open('xb') as stderr:r=subprocess.run(argv,stdout=stdout,stderr=stderr)
 after=inputs();(out/(name+'-inputs-after.json')).write_text(json.dumps(after,indent=2)+'\n');events=[json.loads(l) for l in (out/(name+'.stdout.jsonl')).read_text().splitlines()];passed=[e['Test'] for e in events if e.get('Action')=='pass' and e.get('Test')];bad=[e for e in events if e.get('Action') in ('fail','build-fail','skip')];packages=[e for e in events if e.get('Action')=='pass' and not e.get('Test')]
 receipt={'argv':argv,'exit':r.returncode,'seconds':time.monotonic()-start,'passed':passed,'passCount':len(passed),'bad':bad,'packages':packages,'inputCount':len(before),'inputsUnchanged':before==after};(out/(name+'.json')).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)
 assert before==after
 if mode=='red':assert r.returncode==1 and any(e.get('Test')=='TestRetireThreadPersistedEmptyRootAbsentFromDiscovery' and e['Action']=='fail' for e in bad) and not any(e['Action']=='skip' for e in bad)
 else:assert r.returncode==0 and not bad and packages,name+' failed, no automatic rerun'

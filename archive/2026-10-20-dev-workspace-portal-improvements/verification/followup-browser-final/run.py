import datetime,json,os,subprocess,time
from pathlib import Path
packet=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-browser-final')
operation=packet/'run'
if operation.exists(): raise SystemExit('Existing supplement run retained; refusing overwrite or retry')
operation.mkdir(mode=0o700)
(operation/'roots').mkdir(mode=0o700)
(operation/'status').write_text('RUNNING\n')
started=time.monotonic()
results=[]
def run(label,argv):
    log=operation/(label+'.log')
    wall=datetime.datetime.now(datetime.timezone.utc).isoformat()
    start=time.monotonic()
    with log.open('w') as output:
        result=subprocess.run(argv,cwd=packet,stdout=output,stderr=subprocess.STDOUT)
    receipt={'stage':label,'argv':argv,'startedAt':wall,'elapsedSeconds':round(time.monotonic()-start,6),'exitCode':result.returncode,'log':str(log)}
    (operation/(label+'.result.json')).write_text(json.dumps(receipt,indent=2)+'\n')
    results.append(receipt)
    print(json.dumps(receipt),flush=True)
    return result.returncode
preflight=run('source-guards',['bash',str(packet/'guards.sh')])
if preflight==0:
    stages=[('B-full-browser',['bash',str(packet/'B-full-browser.sh')]),('A-paging',['bash',str(packet/'A-paging.sh')])]
    stages += [('C-'+name,['bash',str(packet/'C-check.sh'),name]) for name in ['agent-instructions','deployment-contract','cluster-provider-composition']]
    for label,argv in stages:
        run(label,argv)
passed=preflight==0 and len(results)==6 and all(r['exitCode']==0 for r in results)
result={'status':'PASS' if passed else 'FAIL','elapsedSeconds':round(time.monotonic()-started,6),'stages':results,'retries':0}
(operation/'result.json').write_text(json.dumps(result,indent=2)+'\n')
(operation/'status').write_text(result['status']+'\n')
print(json.dumps({'status':result['status'],'elapsedSeconds':result['elapsedSeconds'],'result':str(operation/'result.json')}),flush=True)
raise SystemExit(0 if passed else 1)

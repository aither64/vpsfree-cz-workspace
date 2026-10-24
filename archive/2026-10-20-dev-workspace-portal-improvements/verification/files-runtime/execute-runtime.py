import json,pathlib,subprocess,time,sys
p=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-runtime')
a=['bash',str(p/'run.sh'),'483d4e7eafeda974dfe19de45687795562072d7d']
started=time.monotonic()
with (p/'operation.log').open('xb') as out,(p/'operation.stderr').open('xb') as err:
 result=subprocess.run(a,cwd='/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace',stdout=out,stderr=err)
value={'exitCode':result.returncode,'elapsedSeconds':time.monotonic()-started,'argv':a,'testedHead':a[-1]}
(p/'operation-result.json').write_text(json.dumps(value,indent=2)+'\n')
print(json.dumps(value),flush=True)
sys.exit(result.returncode)

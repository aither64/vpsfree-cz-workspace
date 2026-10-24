import hashlib,json,os,subprocess,sys,time
from pathlib import Path
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/codex-web')
e=Path(__file__).resolve().parent
label=sys.argv[1];race='race' in label
selector='^(TestCanceledWriteWaiterDoesNotDisconnectSibling|TestAlreadyCanceledWriteDoesNotDisconnect|TestWriteRejectsAStaleConnectionGeneration|TestPromptResponseRejectsConnectionChangeBeforeSending|TestPromptWriteFailureDoesNotClaimTheAnswerWasUnsent|TestReissuedOfferWhileAnswerWaitsForWrite|TestStaleDisconnectDoesNotClearReplacementConnection)$'
argv=['nix','shell','--inputs-from','.', 'nixpkgs#go','nixpkgs#gcc','-c','env','GOFLAGS=','GOWORK=off','go','test','-mod=readonly','-count=1','-timeout=30s','-json']+(['-race'] if race else [])+['./codex','-run',selector]
def hashes():
 return {str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(r.rglob('*')) if p.is_file() and '.git' not in p.relative_to(r).parts}
before=hashes();t=time.monotonic()
(e/(label+'.command.json')).write_text(json.dumps({'argv':argv,'cwd':str(r),'environment':{'GOFLAGS':'','GOWORK':'off'},'sourceInputsBefore':before},indent=2)+'\n')
with (e/(label+'.stdout.jsonl')).open('wb') as out,(e/(label+'.stderr')).open('wb') as err:
 p=subprocess.run(argv,cwd=r,stdout=out,stderr=err)
after=hashes()
events=[json.loads(x) for x in (e/(label+'.stdout.jsonl')).read_text().splitlines() if x.startswith('{')]
result={'argv':argv,'cwd':str(r),'exit':p.returncode,'seconds':time.monotonic()-t,'before':before,'after':after,'sourceUnchanged':before==after,'passes':[x.get('Test') for x in events if x.get('Action')=='pass' and x.get('Test')],'fails':[x.get('Test') for x in events if x.get('Action')=='fail' and x.get('Test')],'skips':[x.get('Test') for x in events if x.get('Action')=='skip']}
(e/(label+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['before','after','argv']},indent=2),flush=True)
if p.returncode:
 print((e/(label+'.stderr')).read_text()[-2500:])
 print(''.join(x.get('Output','') for x in events if x.get('Action')=='output')[-6000:])
sys.exit(p.returncode)

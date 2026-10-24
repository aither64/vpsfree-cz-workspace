from pathlib import Path
import subprocess,json,time,hashlib,shutil
repo=Path.cwd();out=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
path='portal/internal/web/creation_test.go';ruby=repo/'libexec/dev-session'
subprocess.run(['gofmt','-w',path],check=True);subprocess.run(['git','diff','--check','--',path],check=True)
inputs={str(p.relative_to(repo)):sha(p) for p in (repo/'portal').rglob('*.go')}
for p in ['portal/go.mod','portal/go.sum']:inputs[p]=sha(repo/p)
rubyHash=sha(ruby);shutil.copy2(ruby,out/'dev-session.tested.rb');shutil.copy2(repo/path,out/'creation_test.tested.go')
selector='^(TestCreationEvidenceGapDeletionRetiresTheExactRequest|TestCreationReclaimsDeletedReceiptsForUnrelatedAdmissionAndStartup)$'
cmd=['go','-C','portal','test','-mod=readonly','./internal/web','-run',selector,'-count=1','-timeout=45s','-json'];start=time.monotonic()
with (out/'quick.stdout.jsonl').open('x') as stdout,(out/'quick.stderr').open('x') as stderr:r=subprocess.run(cmd,stdout=stdout,stderr=stderr)
passed=[];failed=[];skipped=[];packagePass=False
for line in (out/'quick.stdout.jsonl').read_text().splitlines():
 e=json.loads(line)
 if e.get('Action')=='pass':
  if e.get('Test'):passed.append(e['Test'])
  else:packagePass=True
 if e.get('Action') in ('fail','build-fail'):failed.append(e.get('Test','package'))
 if e.get('Action')=='skip':skipped.append(e.get('Test','package'))
record={'argv':cmd,'exit':r.returncode,'elapsed':time.monotonic()-start,'passed':passed,'failed':failed,'skipped':skipped,'packagePass':packagePass,'goSourceInputs':inputs,'rubyProducerPath':'libexec/dev-session','rubyProducerBeforeSHA256':rubyHash,'rubyProducerAfterSHA256':sha(ruby),'allGoInputsUnchangedDuringRun':all(sha(repo/p)==h for p,h in inputs.items()),'creationTestSHA256':sha(repo/path),'provisionalProducerBytes':True,'scope':'Actual Ruby removal metadata serialization -> real Go CompletedRemovalHistory/schema3 receipt load+retirement only; separate from owner0 public host producer fixture; no full-system pass/no creation dispatch','wholeWorkingTreeVerificationClaim':False}
(out/'quick.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k!='goSourceInputs'}),flush=True)
required={'TestCreationEvidenceGapDeletionRetiresTheExactRequest','TestCreationEvidenceGapDeletionRetiresTheExactRequest/direct-new-schema3/failed','TestCreationReclaimsDeletedReceiptsForUnrelatedAdmissionAndStartup'}
assert r.returncode==0 and packagePass and required.issubset(set(passed)) and not failed and not skipped
assert record['rubyProducerBeforeSHA256']==record['rubyProducerAfterSHA256'] and record['allGoInputsUnchangedDuringRun']

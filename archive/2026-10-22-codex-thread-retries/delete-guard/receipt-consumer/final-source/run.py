from pathlib import Path
import subprocess,json,time,hashlib,shutil
repo=Path.cwd();out=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected={'libexec/dev-session':'396b42fb80a55da8dc1f99fa568197082f6f48f8fecf90c395df86cf94fa39ca','libexec/workspace-host':'acf46cb6ac8b2efdb85f9328d8dc43984dd53cb1f5b23c422fc5c85148c8ef63','docs/session-archive-recovery.md':'5cf4ea352507dadf85e6510465b446823b6ef10bace4b8c06fed25a6ee6af7f0','portal/internal/web/creation_test.go':'10ba5cd41a7ca4ce5df6e7cebea63a9d1f4a60e3fc30cd4fb70b84ea0781f4ae'}
assert all(sha(repo/p)==h for p,h in expected.items()),'frozen source mismatch'
assert not subprocess.check_output(['gofmt','-l','portal/internal/web/creation_test.go'],text=True).strip()
subprocess.run(['git','diff','--check'],check=True)
inputs={str(p.relative_to(repo)):sha(p) for p in (repo/'portal').rglob('*.go')}
for p in ['portal/go.mod','portal/go.sum']:inputs[p]=sha(repo/p)
for p in expected:shutil.copy2(repo/p,out/Path(p).name)
cmd=['go','-C','portal','test','-mod=readonly','./internal/web','-run','^(TestCreationEvidenceGapDeletionRetiresTheExactRequest|TestCreationReclaimsDeletedReceiptsForUnrelatedAdmissionAndStartup)$','-count=1','-timeout=45s','-json']
start=time.monotonic()
with (out/'stdout.jsonl').open('x') as stdout,(out/'stderr.log').open('x') as stderr:r=subprocess.run(cmd,stdout=stdout,stderr=stderr)
passed=[];failed=[];skipped=[];packages=[]
for line in (out/'stdout.jsonl').read_text().splitlines():
 e=json.loads(line)
 if e.get('Action')=='pass':
  if e.get('Test'):passed.append(e['Test'])
  else:packages.append({'name':e['Package'],'elapsed':e.get('Elapsed')})
 if e.get('Action') in ('fail','build-fail'):failed.append(e.get('Test','package'))
 if e.get('Action')=='skip':skipped.append(e.get('Test','package'))
record={'argv':cmd,'exit':r.returncode,'elapsed':time.monotonic()-start,'passed':passed,'failed':failed,'skipped':skipped,'packages':packages,'goSourceInputsBefore':inputs,'goSourceInputsAfter':{p:sha(repo/p) for p in inputs},'frozenSourceBefore':expected,'frozenSourceAfter':{p:sha(repo/p) for p in expected},'scope':'Actual Ruby removal serialization -> real Go CompletedRemovalHistory/schema3 receipt load and retirement; separate from public host producer fixture; no full-system pass or creation dispatch','wholeWorkingTreeVerificationClaim':False}
(out/'quick.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if not k.startswith('goSourceInputs')}),flush=True)
required={'TestCreationEvidenceGapDeletionRetiresTheExactRequest','TestCreationEvidenceGapDeletionRetiresTheExactRequest/direct-new-schema3/failed','TestCreationReclaimsDeletedReceiptsForUnrelatedAdmissionAndStartup'}
assert r.returncode==0 and len(packages)==1 and len(passed)==11 and required.issubset(set(passed)) and not failed and not skipped
assert record['goSourceInputsBefore']==record['goSourceInputsAfter'] and record['frozenSourceBefore']==record['frozenSourceAfter']

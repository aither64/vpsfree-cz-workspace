import hashlib,json,re,subprocess,uuid
from pathlib import Path
root=Path('/home/aither/workspace/ai/vpsfree.cz')
t=root/'work/2026-10-13-workspace-coordination'
for name in ['verification','candidate-build','system-build']:
    assert (t/f'creation-provider-{name}.status').read_text().strip()=='0'
ci=json.loads((t/'creation-provider-ci-final.json').read_text())
assert ci['databaseId']==38470155400 and ci['headSha']=='a10af6c4539c4c7a6a97a883d89825346d5451ad'
assert ci['status']=='completed' and ci['conclusion']=='success'
heads={i['repository']:i['head'] for i in json.loads((t/'creation-provider-final-inventory.json').read_text())}
names=re.findall(r'^([0-9]{4}-[0-9]{2}-[0-9]{2}--[0-9]{2}-[0-9]{2}-[0-9]{2})$',(t/'creation-provider-system-build.log').read_text(),re.MULTILINE)
assert len(names)==1
path=root/'worktrees/2026-10-13-workspace-coordination/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev'/names[0]/'generation.json'
g=json.loads(path.read_text())
assert g['inputs_info']['devWorkspace']['rev']==heads['dev-workspace']
prior='ef4ec58d1838ed01706c0e85e306117821a0a114'
changed=set(subprocess.check_output(['git','-C',str(root/'worktrees/2026-10-13-workspace-coordination/dev-workspace'),'diff','--name-only',prior,heads['dev-workspace']],text=True).splitlines())
assert changed=={'libexec/dev-session','test/dev_session/codex_runtime_test.rb'}
files=['creation-provider-review.md','creation-provider-runner-fix.md','creation-provider-final-inventory.json','creation-provider-composition.log','creation-provider-quick-corrected-fixture.log','creation-provider-reproduction.log','creation-provider-verification.sh','creation-provider-candidate-build.log','creation-provider-workspace-checks.log','creation-provider-system-build.log','creation-provider-recovery-vm.log','creation-provider-ci-final.json','operations-tab-acceptance-evidence.json','operations-tab-deployed-live-acceptance.json']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v={'schema':1,'heads':heads,'candidatePackage':(t/'creation-provider-candidate.path').read_text().strip(),'systemPackage':g['toplevel'],'systemGeneration':names[0],'systemGenerationSha256':sha(path),'ci':ci,'checks':{'packagedSessionProvider':'passed','package':'passed','workspace':'passed','matchingSystem':'passed','sessionRecoveryVM':'passed'},'reusedChecks':{'head':prior,'sourceDelta':sorted(changed),'reason':'Host/worker/portal/UI and VM source unchanged; caller provider regression and session recovery VM rerun for this head.','hostModuleIdempotency':'passed previously','liveBrowserUI':'passed previously'},'files':{n:sha(t/n) for n in files}}
p=t/'creation-provider-acceptance-evidence.json';assert not p.exists();p.write_text(json.dumps(v,indent=2)+'\n')
evidence=[{'kind':kind,'path':str((t/name).relative_to(root)),'sha256':sha(t/name)} for kind,name in [('review','creation-provider-review.md'),('verification',p.name)]]
request={'schema':1,'requestId':str(uuid.uuid4()),'approvalQuote':'you can deploy it to aitherdev using vpsfree-cz-configuration','evidence':evidence,'target':'aitherdev'}
p=t/'creation-provider-bootstrap-prepare-request.json';assert not p.exists();p.write_text(json.dumps(request,indent=2)+'\n')
print('Exact creation-fix verification frozen; new deployment request prepared')

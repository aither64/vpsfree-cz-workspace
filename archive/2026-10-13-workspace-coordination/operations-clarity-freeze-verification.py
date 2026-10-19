import hashlib,json,re,uuid
from pathlib import Path
root=Path('/home/aither/workspace/ai/vpsfree.cz');t=root/'work/2026-10-13-workspace-coordination'
assert (t/'operations-clarity-verification.status').read_text().strip()=='0'
assert (t/'operations-clarity-candidate-build.status').read_text().strip()=='0'
assert (t/'operations-clarity-system-build.status').read_text().strip()=='0'
ci=json.loads((t/'operations-clarity-ci-final.json').read_text())
assert ci['headSha']=='84dde222628bb52e6e3149a8527700d753c2151e' and ci['status']=='completed' and ci['conclusion']=='success'
heads={i['repository']:i['head'] for i in json.loads((t/'operations-clarity-final-inventory.json').read_text())}
generation_names=re.findall(r'^([0-9]{4}-[0-9]{2}-[0-9]{2}--[0-9]{2}-[0-9]{2}-[0-9]{2})$',(t/'operations-clarity-system-build.log').read_text(),re.MULTILINE)
assert len(generation_names)==1
generation_path=root/'worktrees/2026-10-13-workspace-coordination/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev'/generation_names[0]/'generation.json'
generation=json.loads(generation_path.read_text())
assert generation['inputs_info']['devWorkspace']['rev']==heads['dev-workspace']
files=['operations-clarity-review.md','operations-clarity-review-reconciliation.md','operations-clarity-final-inventory.json','operations-clarity-composition-final.log','operations-clarity-browser-final.log','operations-clarity-go-corrected-final.log','operations-clarity-package-layout-quick.log','operations-clarity-quick-final.log','operations-clarity-verification.sh','operations-clarity-candidate-build.log','operations-clarity-workspace-checks.log','operations-clarity-vm-checks.log','operations-clarity-system-build.log','operations-clarity-ci-final.json']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v={'schema':1,'heads':heads,'candidatePackage':(t/'operations-clarity-candidate.path').read_text().strip(),'ci':ci,'checks':{'package':'passed','workspace':'passed','hostModuleIdempotency':'passed locally with KVM','sessionRecoveryBoot':'passed locally with KVM','matchingSystem':'passed','quickChecks':'passed'},'files':{name:sha(t/name) for name in files},'limits':{'githubDispatch':'403 token access; local equivalent passed','supersededCancellation':'403 token access; old run not accepted'}}
v.update(systemPackage=generation['toplevel'],systemGeneration=generation_names[0],systemGenerationSha256=sha(generation_path))
p=t/'operations-clarity-acceptance-evidence.json';assert not p.exists();p.write_text(json.dumps(v,indent=2)+'\n')
evidence=[]
for kind,name in [('review','operations-clarity-review.md'),('review','operations-clarity-review-reconciliation.md'),('verification','operations-clarity-acceptance-evidence.json')]:
 evidence.append({'kind':kind,'path':str((t/name).relative_to(root)),'sha256':sha(t/name)})
request={'schema':1,'requestId':str(uuid.uuid4()),'approvalQuote':'you can deploy it to aitherdev using vpsfree-cz-configuration','evidence':evidence,'target':'aitherdev'}
p=t/'operations-clarity-bootstrap-prepare-request.json';assert not p.exists();p.write_text(json.dumps(request,indent=2)+'\n')
print('Final verification evidence frozen; deployment request prepared')

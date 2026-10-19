import hashlib,json,os,subprocess,uuid
from pathlib import Path
root=Path('/home/aither/workspace/ai/vpsfree.cz');t=root/'work/2026-10-13-workspace-coordination'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unit(name):
 fields=dict(line.split('=',1) for line in subprocess.check_output(['systemctl','--user','show',name,'-p','ActiveState','-p','Result','-p','ExecMainStatus','-p','InvocationID'],text=True).splitlines())
 assert fields['ActiveState']=='inactive' and fields['Result']=='success' and fields['ExecMainStatus']=='0', fields
 return fields
for name in ['operations-candidate-build.status','operations-system-build.status','operations-incarnation-go-final.status']:assert (t/name).read_text().strip()=='0'
units={kind:unit('workspace-coordination-operations-'+suffix+'-20261013.service') for kind,suffix in [('package','candidate'),('system','system-build')]}
inventory=json.loads((t/'operations-incarnation-inventory.json').read_text())
heads={}
for item in inventory:
 repo=Path(item['worktree']);head=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
 assert head==item['head'] and not subprocess.check_output(['git','-C',str(repo),'status','--porcelain'],text=True)
 assert len(item['commits'])==2 and item['migrations']==[]
 heads[item['repository']]=head
runtime=json.loads((t/'operations-runtime-ci.json').read_text());extension=json.loads((t/'library-extension-ci.json').read_text())
assert runtime['conclusion']=='success' and runtime['headSha']==heads['dev-workspace']
assert extension['conclusion']=='success' and extension['headSha']==heads['vpsfree-dev-workspace']
candidate=(t/'operations-candidate.path').read_text().strip();assert (t/'operations-candidate-gc-root').resolve()==Path(candidate)
assert (Path(candidate)/'bin/workspace-host').is_file()
generation=json.loads((root/'worktrees/2026-10-13-workspace-coordination/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev/2026-10-13--20-15-02/generation.json').read_text())
assert generation['inputs_info']['devWorkspace']['rev']==heads['dev-workspace']
old=json.loads((t/'deployed-live-acceptance.json').read_text())
assert old['outcome']=='passed'
for name,value in old['files'].items():assert sha(t/name)==value['sha256'],name
files=['operations-review-retained.md','operations-incarnation-inventory.json','operations-incarnation-quick-results.json','operations-incarnation-quick.log','operations-incarnation-go-final.log','operations-incarnation-go-final.status','operations-incarnation-composition.log','operations-candidate-build.log','operations-candidate-build.status','operations-candidate-check.log','operations-system-build.log','operations-system-build.status','operations-runtime-ci.json','library-extension-ci.json','deployed-live-acceptance.json','operations-activation-baseline.json']
for item in inventory:files.extend([Path(item['finalDiff']).name,Path(item['rangeDiff']).name])
evidence={'schema':1,'heads':heads,'candidatePackage':candidate,'systemPackage':generation['toplevel'],'ci':{'runtime':runtime,'extension':extension},'units':units,'verification':{'review':'All four retained independent Astra/xhigh lanes and complete histories completed; one Important cache finding fixed within requested minimal scope, directly verified under skill step 9. No migrations.','quick':'Browser 5/5; Ruby holders 3/28; focused Go initial/cached page, replacement and unchanged Automatic archival checks passed.','package':'Exact composed package and packaged suite passed after independent review; complete Nix check log retained.','system':'Exact matching system built; no local kernel compilation.','baselineAcceptance':'Unchanged original VM/systemd/native behavior covered by retained deployed-live-acceptance.json and its frozen checksummed predecessor evidence.'},'files':{name:{'sha256':sha(t/name)} for name in files}}
path=t/'operations-acceptance-evidence.json';assert not path.exists();path.write_text(json.dumps(evidence,indent=2)+'\n')
request={'schema':1,'requestId':str(uuid.uuid4()),'approvalQuote':'you can deploy it to aitherdev using vpsfree-cz-configuration','evidence':[{'kind':kind,'path':str((t/name).relative_to(root)),'sha256':sha(t/name)} for kind,name in [('review','operations-review-retained.md'),('verification','operations-acceptance-evidence.json')]],'target':'aitherdev'}
path=t/'operations-bootstrap-prepare-request.json';assert not path.exists();path.write_text(json.dumps(request,indent=2)+'\n');print(json.dumps({'requestId':request['requestId'],'candidate':candidate,'system':generation['toplevel']}))

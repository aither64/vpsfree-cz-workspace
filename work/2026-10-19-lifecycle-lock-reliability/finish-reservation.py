from pathlib import Path
import subprocess,json,hashlib,uuid,os
root=Path('/home/aither/workspace/ai/vpsfree.cz');out=root/'work/2026-10-19-lifecycle-lock-reliability';slug=out.name
integration=json.loads((out/'merge-integration-request.json').read_text());run_id=integration['requestId'];ledger=json.loads(Path('/home/aither/.local/state/dev-workspaces/coordination/ledger.json').read_text());journal=json.loads((Path('/home/aither/.local/state/dev-workspaces/coordination/integrations')/(run_id+'.json')).read_text());assert journal['phase']=='complete',journal.get('reason')
reservation=ledger['reservations']['441300ed-f84b-4b68-921d-a0fd2ccf4ad1'];owner=reservation['ownerId'];final=[];replacements=[]
def git(path,*args):return subprocess.check_output(['git','-C',str(path),*args],text=True)
def ev(kind,path):return {'kind':kind,'path':str(path.relative_to(root)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
for name,operation in journal['operations'].items():
    job=ledger['jobs'][journal['jobs']['merge:'+name]]
    assert job['state']=='succeeded' and job['result']['outcome']=='applied'
    snapshot=job['snapshot'];op=snapshot['operation'];head=op['featureHead'];path=root/'worktrees'/slug/name
    operation=operation | {'approvalId':job['approvalId']}
    assert git(path,'rev-parse','HEAD').strip()==head
    assert job['result']['observed']['head']==head
    subprocess.run(['git','-C',str(path),'fetch','origin','refs/heads/master'],check=True)
    remote=git(path,'rev-parse','FETCH_HEAD').strip()
    subprocess.run(['git','-C',str(path),'merge-base','--is-ancestor',head,remote],check=True)
    final.append({'repository':name,'target':'refs/heads/master','head':head})
    for record in reservation['history']:
        if record['outcome']!='applied': continue
        if not any(c.get('owned') and c['repository']==name for c in record['coverageContracts']):continue
        for coverage in record['coverage']:
            if coverage['repository']!=name:continue
            old=coverage['revision']
            if subprocess.run(['git','-C',str(path),'merge-base','--is-ancestor',old,head]).returncode==0:continue
            assert name in ['workspace','dev-workspace']
            assert old=={'workspace':'4b22d04f0fefddfd01e744f990d6d9ebb5cbea12','dev-workspace':'6ab3b48f57981f4358094b47cac1ba724c458396'}[name]
            oldbase={'workspace':'dc97c0f0f422e0d6cc6e250c7241c12fe6b73de8','dev-workspace':'09a407953026514ae84be81dab9442fd74b6a362'}[name];newbase=op['comparisonBase']
            mapping={'repository':name,'target':'refs/heads/master','from':old,'fromBase':oldbase,'to':head,'toBase':newbase,'relation':'patch_equivalent','approvalId':operation['approvalId']}
            range_path=out/('merge-release-'+name+'-range.diff');range_path.write_text(git(path,'range-diff','--no-color','--creation-factor=80',oldbase+'..'+old,newbase+'..'+head))
            ids=[]
            for base,end in [(oldbase,old),(newbase,head)]:
                patches=[]
                for sha in git(path,'rev-list','--reverse',base+'..'+end).splitlines():
                    data=subprocess.check_output(['git','-C',str(path),'show','--format=','--binary',sha]);patches.append(subprocess.check_output(['git','patch-id','--stable'],input=data,text=False).decode().split()[0])
                ids.append(patches)
            assert ids[0]==ids[1]
            verification=out/('merge-release-'+name+'-verification.json');verification.write_text(json.dumps({'orderedPatchIds':ids,'match':True,'equivalence':ev('equivalence',out/'merge-workspace-equivalence.json') if name=='workspace' else ev('review',out/'merge-runtime-followup-review.md'),'deploymentAcceptance':ev('verification',out/'deployment-acceptance.json')},indent=2)+'\n')
            receipt={'schema':1,'ownerId':owner,'reservationId':reservation['id'],'mapping':mapping,'decision':'accepted','reviewer':'/root/final_review gpt-6-astra/xhigh; original review and merge-runtime-followup-review.md','artifacts':[ev('range_diff',range_path),ev('verification',verification),ev('migration_review',out/'merge-runtime-followup-review.md')]}
            receipt_path=out/('merge-release-'+name+'-lineage.json');receipt_path.write_text(json.dumps(receipt,indent=2)+'\n');replacement=mapping|{'evidence':ev('review',receipt_path)}
            if replacement not in replacements:replacements.append(replacement)
request={'schema':1,'requestId':str(uuid.uuid4()),'expectedRevision':reservation['revision'],'deploymentWorkFinished':True,'evidence':'User: okay, merge it and release aitherdev. All requested merges completed, exact deployed system/profile acceptance verified; final-review.md, config-refresh-review.md, merge-workspace-equivalence.json, deployment-acceptance.json and archive-acceptance.json retain evidence.','finalHeads':final,'replacements':replacements}
p=out/'release-aitherdev-request.json'
if p.exists():
    saved=json.loads(p.read_text());assert saved['finalHeads']==request['finalHeads'];request=saved
else:p.write_text(json.dumps(request,indent=2)+'\n')
command=['dev-session','coordination','finish',slug,reservation['id'],'--as-is','--request',str(p),'--json']
with (out/'release-aitherdev-receipt.json').open('w') as stdout,(out/'release-aitherdev.log').open('w') as stderr:
    process=subprocess.run(command,cwd=root,env=os.environ|{'DEV_SESSION_SLUG':slug,'DEV_SESSION_WORKSPACE':str(root)},stdout=stdout,stderr=stderr)
print('finish exitStatus',process.returncode);raise SystemExit(process.returncode)

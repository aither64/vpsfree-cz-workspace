#!/usr/bin/env python3
import datetime,hashlib,json,pathlib,subprocess,sys
S=pathlib.Path(__file__).resolve().parent
W=S.parent.parent
slug=S.name
provider='5436d3d7c36d3d5174eab3c44e3578830749d3db'
ref='refs/heads/'+slug
project=sys.argv[1]
item=next(p for p in json.loads((S/'package-c-r-branches.json').read_text()) if p['project']==project)
wt=pathlib.Path(item['worktree']); canonical=W/'repos'/(project+'.git')
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def cmd(argv,cwd=None): return subprocess.check_output(argv,cwd=cwd,stderr=subprocess.STDOUT).decode().strip()
def git(*args): return cmd(['git',*args],wt)
receipt=S/'package-c-r-publication.json'
r=json.loads(receipt.read_text()) if receipt.exists() else {'provider':provider,'review':'review-r-report.md','review_sha256':hashlib.sha256((S/'review-r-report.md').read_bytes()).hexdigest(),'projects':[],'started_utc':now()}
assert not any(p['project']==project for p in r['projects']), 'Existing attempt requires reconciliation'
provider_proof=cmd(['git','ls-remote','git@github.com:vpsfreecz/confctl.git',ref])
assert provider_proof.split()[0]==provider,provider_proof
assert git('remote','get-url','origin')=='git@github.com:vpsfreecz/'+project+'.git'
assert git('symbolic-ref','--short','HEAD')==slug
assert git('rev-parse','HEAD')==item['head']
assert not git('status','--porcelain=v1','--untracked-files=normal')
assert git('rev-parse','HEAD:flake.lock')==git('rev-parse',item['base']+':flake.lock')
fetch=cmd(['git','--git-dir',str(canonical),'fetch','origin'])
refs=dict(line.split()[::-1] for line in git('ls-remote','origin','refs/heads/'+item['target'],ref).splitlines())
assert refs['refs/heads/'+item['target']]==item['base'], 'DEFAULT MOVED: '+str(refs)
assert refs[ref]==item['remote_lease_head'],'FEATURE LEASE MOVED: '+str(refs)
p={'project':project,'head':item['head'],'base':item['base'],'target':item['target'],'lease':item['remote_lease_head'],'pre_push_remote_refs':refs,'provider_remote_proof':provider_proof,'checked_at_utc':now(),'fetch_output':fetch,'unchanged_lock_blob':git('rev-parse','HEAD:flake.lock')}
r['projects'].append(p)
def save(): receipt.write_text(json.dumps(r,indent=2)+'\n')
save()
argv=['nix','develop','--no-write-lock-file','-c','git','push','--force-with-lease='+ref+':'+item['remote_lease_head'],'origin','HEAD:'+ref]
log=S/('package-c-r-publication-'+project+'.log')
p.update(command=argv,log=str(log));save()
with log.open('wb') as f:
 result=subprocess.run(argv,cwd=wt,stdout=f,stderr=subprocess.STDOUT)
p['push_status']=result.returncode
p['post_push_remote_proof']=git('ls-remote','origin',ref,'refs/heads/'+item['target'])
p['log_sha256']=hashlib.sha256(log.read_bytes()).hexdigest()
p['finished_utc']=now();p['clean']=not git('status','--porcelain=v1','--untracked-files=normal');save()
assert result.returncode==0, 'Push failed; fresh proof recorded, reconcile before retry'
post=dict(line.split()[::-1] for line in p['post_push_remote_proof'].splitlines())
assert post[ref]==item['head'] and post['refs/heads/'+item['target']]==item['base'],post
assert p['clean']
p['published']=True
r['complete']=len(r['projects'])==5 and all(x.get('published') for x in r['projects']);save()
print(project+' push0; exact reviewed remote head '+item['head']+'; default unchanged; clean')

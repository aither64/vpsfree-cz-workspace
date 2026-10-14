from pathlib import Path
import json,subprocess,datetime,sys
T=Path(__file__).resolve().parent
project=sys.argv[1]
row=next(r for r in json.loads((T/'finish-kb-scope12-final-target-check.json').read_bytes())['rows'] if r['project']==project)
if project=='vpsfree-cz-configuration':
 c=json.loads((T/'finish-merge13-c-proof.json').read_bytes());row['expected_tip']=c['base'];row['published_feature']=c['head']
R=Path(row['worktree']);target=row['target'];head=row['published_feature'];base=row['expected_tip']
def git(*args,repo=R):
 p=subprocess.run(['git','-C',str(repo),*args],capture_output=True)
 log.write('$ git '+' '.join(args)+'\n'+p.stdout.decode()+p.stderr.decode());log.flush()
 if p.returncode:raise RuntimeError((args,p.returncode))
 return p.stdout
P=R.parent/('integration13-'+project)
with (T/('finish-merge13-'+project+'.log')).open('a') as log:
 if P.exists():
  assert git('rev-parse','HEAD',repo=P).decode().strip()==base
  assert not git('status','--porcelain',repo=P)
 assert git('rev-parse','HEAD').decode().strip()==head
 assert not git('status','--porcelain')
 refs=dict((ref,sha) for sha,ref in (line.split() for line in git('ls-remote','origin','refs/heads/'+target,'refs/heads/'+row['feature_branch']).decode().splitlines()))
 assert refs['refs/heads/'+target]==base,(project,'default changed')
 assert refs['refs/heads/'+row['feature_branch']]==head
 git('merge-base','--is-ancestor',base,head)
 if not P.exists():git('worktree','add','--detach',str(P),base)
 git('merge','--ff-only',head,repo=P)
 assert git('rev-parse','HEAD',repo=P).decode().strip()==head
 assert not git('status','--porcelain',repo=P)
 git('diff','--check',base,head,repo=P)
 git('push','origin','HEAD:refs/heads/'+target,repo=P)
 published=git('ls-remote','origin','refs/heads/'+target).decode().split()[0];assert published==head
 git('fetch','origin')
 git('worktree','remove',str(P))
 result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'project':project,'target':target,'before':base,'head':head,'remote_tip':published,'method':'git merge --ff-only then non-force SSH push','feature_branch':row['feature_branch'],'feature_preserved':True,'temporary_worktree_removed':True,'existing_exact_head_checks_retained':True,'deployment':False}
 (T/('finish-merge13-'+project+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(project+' '+target+' integrated '+head,flush=True)

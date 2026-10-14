from pathlib import Path
import subprocess,json,datetime,concurrent.futures
T=Path(__file__).resolve().parent
prior=json.loads((T/'finish-target11-final-target-check.json').read_bytes())
new={'vpsfree-kb-contracts':'ce2c8cd9358c3636e5d39343e595df813a0b197f','vpsfree-dev-workspace':'505ffc457b3329af0b124075f417953c9cc42edd'}
def check(r):
 R=Path(r['worktree']);target=r['target'];feature=r['feature_branch'];head=new.get(r['project'],r['published_feature'])
 def git(*a):return subprocess.check_output(['git','-C',str(R),*a])
 raw=git('ls-remote','origin','refs/heads/'+target,'refs/heads/'+feature).decode()
 refs=dict((ref,sha) for sha,ref in (line.split() for line in raw.splitlines()))
 assert refs['refs/heads/'+target]==r['expected_tip'],r['project']+' target advanced'
 assert refs['refs/heads/'+feature]==head
 assert git('rev-parse','HEAD').decode().strip()==head
 assert not git('status','--porcelain')
 subprocess.run(['git','-C',str(R),'merge-base','--is-ancestor',r['expected_tip'],head],check=True)
 return {**r,'tip':refs['refs/heads/'+target],'unchanged':True,'published_feature':head,'feature_descends_default':True,'clean':True}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(check,prior['rows']))
(T/'finish-kb-scope12-final-target-check.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows,'all_targets_unchanged':True,'all_features_published_clean_and_descend_targets':True,'approval':None,'limits':'Read-only SSH freshness; no merge. Repeat immediately before any explicitly approved integration.'},indent=2)+'\n')
print('All six current targets unchanged; exact final feature heads published, clean and descend targets.')

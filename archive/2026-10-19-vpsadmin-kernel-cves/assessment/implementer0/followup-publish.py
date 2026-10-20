import datetime,hashlib,json,os,subprocess
from pathlib import Path
session=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');out=session/'assessment/implementer0/followup-publication';out.mkdir(exist_ok=True)
head='0b2f060e61c5480ccd09e93d2ecbace39bcb27a1';anchor='8d1413efb041ab410d1a629c34d8aaf921439901';base='ea6247687fd02417f87e1e5593fecd8b9055925d';branch='2026-10-19-vpsadmin-kernel-cves';default='2026-07-13-security-advisory-automation'
def git(*a):return subprocess.check_output(['git',*a],text=True).strip()
def operation(name,args):
 r=subprocess.run(args,text=True,capture_output=True)
 (out/(name+'.log')).write_text(r.stdout+r.stderr)
 if r.returncode:raise RuntimeError(f'{name} failed exit{r.returncode}; see {out/(name+".log")}')
 return r.stdout
assert git('rev-parse','HEAD')==head and git('branch','--show-current')==branch
assert not git('status','--porcelain=v1')and not git('diff','--cached','--name-only')
assert git('remote','get-url','origin')==git('remote','get-url','--push','origin')=='git@github.com:vpsfreecz/security-advisories.git'
assert git('rev-list','--count',base+'..'+head)=='69'and git('rev-list','--count',anchor+'..'+head)=='2'
prep=json.loads((session/'assessment/implementer0/followup-review-reconcile-preparation.json').read_text())
assert git('rev-list','--reverse',base+'..'+anchor).splitlines()==prep['consumed_prefix_commits']
assert git('rev-parse',prep['backup_ref'])==prep['reviewed_head']
heads_before=git('show-ref','--heads')
baselines=json.loads((session/'assessment/implementer0/followup-baseline-submissions.json').read_text())
def invariants():
 assert git('rev-parse','HEAD')==head
 assert not git('status','--porcelain=v1')and not git('diff','--cached','--name-only')
 assert hashlib.sha256(Path('.state/evidence.json').read_bytes()).hexdigest()=='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
 assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==sha for p,sha in baselines.items())
invariants()
for key in ('OVERCOMMIT_DISABLE','SKIP','ONLY','OVERCOMMIT_UNSAFE'):assert not os.environ.get(key),key
hook=Path(git('rev-parse','--git-path','hooks/pre-push'));assert hook.is_file()and os.access(hook,os.X_OK)and'overcommit'in hook.read_text().lower()
operation('fetch',['git','fetch','origin'])
def remote():
 text=operation('ls-remote-'+datetime.datetime.now(datetime.timezone.utc).strftime('%H%M%S'),['git','ls-remote','--symref','origin','HEAD','refs/heads/'+default,'refs/heads/'+branch])
 refs={ref:sha for sha,ref in (line.split('\t')for line in text.splitlines()if'\t'in line and not line.startswith('ref:'))}
 assert 'ref: refs/heads/'+default+'\tHEAD'in text
 assert refs['refs/heads/'+default]==base and refs['HEAD']==base,refs
 return refs
before=remote();assert before['refs/heads/'+branch]==anchor,before
assert git('rev-parse','refs/remotes/origin/'+default)==base
assert git('rev-parse','refs/remotes/origin/'+branch)==anchor
subprocess.run(['git','merge-base','--is-ancestor',anchor,head],check=True)
(out/'remote-before.json').write_text(json.dumps(before,indent=2)+'\n')
invariants();print('Expectedremote/default/feature verified; pushing exact2commit fast-forward',flush=True)
operation('push',['git','push','origin','refs/heads/'+branch+':refs/heads/'+branch])
after=remote();assert after['refs/heads/'+branch]==head,after
(out/'remote-after.json').write_text(json.dumps(after,indent=2)+'\n')
invariants();assert git('show-ref','--heads')==heads_before
assert git('rev-parse','refs/remotes/origin/'+branch)==head
series=git('log','--reverse','--format=%H%x09%P%x09%s',base+'..'+head);assert len(series.splitlines())==69
(out/'complete-series.tsv').write_text(series+'\n')
(out/'complete-diff-stat.txt').write_text(git('diff','--stat',base,head)+'\n')
(out/'followup-diff.patch').write_text(git('diff',anchor,head)+'\n')
subprocess.run(['git','diff','--check',base,head],check=True)
# Query exact-head workflow metadata once; monitoring remains with the lead's watcher.
runs=json.loads(operation('ci-run-list',['gh','run','list','--repo','vpsfreecz/security-advisories','--branch',branch,'--commit',head,'--limit','20','--json','databaseId,url,status,conclusion,headSha,name,event,workflowName,createdAt']))
assert all(row['headSha']==head for row in runs)
(out/'ci-runs.json').write_text(json.dumps(runs,indent=2)+'\n')
r={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'previous_remote_feature':anchor,'remote_default':base,'origin':'git@github.com:vpsfreecz/security-advisories.git','fetch_push_and_remote_readback':'PASS; normalSSH/Nix/hooks;featureonlyfastforward','remote_before':before,'remote_after':after,'complete_source_commits':69,'unchanged_consumed_prefix_commits':67,'logical_followups':2,'whole_worktree_clean':True,'index_empty':True,'all_local_head_refs_preserved':True,'all_consumed_submission_hashes_preserved':True,'frozen_evidence_sha256':'61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274','diff_check':'PASS','ci_runs':runs,'CI_waited':False,'Git_slot_returned_to':'lead','no_operations':['advisoryAPI','sync','ready','advisorypublication','email','recollection','newtests','rebase','amend','forcepush','defaultmerge','PR','lifecycle'],'session_url':'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/'}
(out/'publication-receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'head':head,'remote_exact':True,'clean':True,'index_empty':True,'ci_runs':runs,'receipt':str(out/'publication-receipt.json')},indent=2),flush=True)

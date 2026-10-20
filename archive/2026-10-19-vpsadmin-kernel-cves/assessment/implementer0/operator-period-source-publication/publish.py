import datetime,hashlib,json,os,shutil,subprocess
from pathlib import Path
session=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');owner=session/'assessment/implementer0';other=session/'assessment/implementer2';out=owner/'operator-period-source-publication'
head='57eea8950b38e22831f7ef87d0de2399b4783281';anchor='cfef162049f632016c9e67bca0e400c58c8618d2';base='ea6247687fd02417f87e1e5593fecd8b9055925d';branch='2026-10-19-vpsadmin-kernel-cves';default='2026-07-13-security-advisory-automation'
def git(*a):return subprocess.check_output(['git',*a],text=True).strip()
def operation(name,args):
 r=subprocess.run(args,text=True,capture_output=True);(out/(name+'.log')).write_text(r.stdout+r.stderr)
 if r.returncode:raise RuntimeError(f'{name} exit{r.returncode}; stop, no automatic retry')
 return r.stdout
assert git('rev-parse','HEAD')==head and git('branch','--show-current')==branch
assert not git('status','--porcelain=v1')and not git('diff','--cached','--name-only')
assert git('remote','get-url','origin')==git('remote','get-url','--push','origin')=='git@github.com:vpsfreecz/security-advisories.git'
receipt=json.loads((other/'operator-period-commit-receipt.json').read_text());assert receipt['head']==head
assert git('rev-list','--count',base+'..'+head)=='74'and git('rev-list','--count',anchor+'..'+head)=='2'
prefix=[x.split('\t')[0]for x in(owner/'followup-final-publication/complete-series.tsv').read_text().splitlines()]
assert len(prefix)==72 and git('rev-list','--reverse',base+'..'+anchor).splitlines()==prefix
hashes=json.loads((owner/'operator-period-baseline-submissions.json').read_text());assert len(hashes)==111
heads=git('show-ref','--heads')
def invariants():
 assert git('rev-parse','HEAD')==head
 assert not git('status','--porcelain=v1')and not git('diff','--cached','--name-only')
 assert hashlib.sha256(Path('.state/evidence.json').read_bytes()).hexdigest()=='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
 assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==sha for p,sha in hashes.items())
invariants()
for k in ('OVERCOMMIT_DISABLE','SKIP','ONLY','OVERCOMMIT_UNSAFE'):assert not os.environ.get(k),k
hook=Path(git('rev-parse','--git-path','hooks/pre-push'));assert hook.is_file()and os.access(hook,os.X_OK)and'overcommit'in hook.read_text().lower()
# Reuse reviewed inventory artifacts only after exact hashes and actual Git-byte checks.
checks={
 'operator-period-full-series.tsv':['log','--reverse','--format=%H%x09%P%x09%aI%x09%s',base+'..'+head],
 'operator-period-full-final.diff':['diff','--full-index','--binary',base,head],
 'operator-period-full-final.stat':['diff','--stat',base,head],
 'operator-period-full-final.paths':['diff','--name-status',base,head],
 'operator-period-full-final.numstat':['diff','--numstat',base,head],
 'operator-period-two-source-commits.tsv':['log','--reverse','--format=%H%x09%P%x09%s',anchor+'..'+head],
 'operator-period-two-source-commits.diff':['diff','--full-index','--binary',anchor,head],
 'operator-period-two-source-commits.stat':['diff','--stat',anchor,head],
 'operator-period-two-source-commits.paths':['diff','--name-status',anchor,head]}
reuse=[]
for name,args in checks.items():
 p=other/name;raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==receipt['review_artifacts'][name]['sha256'],name
 actual=subprocess.check_output(['git',*args]);assert actual==raw,(name,'Gitbytesdiffer')
 shutil.copyfile(p,out/name);reuse.append({'artifact':name,'sha256':hashlib.sha256(raw).hexdigest(),'actualGitbyte_match':True})
subprocess.run(['git','diff','--check',base,head],check=True)
(out/'preflight.json').write_text(json.dumps({'head':head,'anchor':anchor,'complete_commits':74,'consumed_prefix_unchanged':72,'all111submissionhashes_unchanged':True,'all63recoveryboundaries_preserved':True,'frozen61904':True,'reviewed_inventory_byte_reuse':reuse,'clean':True},indent=2)+'\n')
operation('fetch',['git','fetch','origin'])
def remote(name):
 t=operation(name,['git','ls-remote','--symref','origin','HEAD','refs/heads/'+default,'refs/heads/'+branch])
 refs={ref:sha for sha,ref in(line.split('\t')for line in t.splitlines()if'\t'in line and not line.startswith('ref:'))}
 assert 'ref: refs/heads/'+default+'\tHEAD'in t and refs['HEAD']==refs['refs/heads/'+default]==base,refs
 return refs
before=remote('remote-before');assert before['refs/heads/'+branch]==anchor,before
assert git('rev-parse','refs/remotes/origin/'+default)==base and git('rev-parse','refs/remotes/origin/'+branch)==anchor
subprocess.run(['git','merge-base','--is-ancestor',anchor,head],check=True)
invariants();print('Exact74history/111submission/inventory invariants PASS; expectedSSHrefs confirmed; featureFFpush now',flush=True)
operation('push',['git','push','origin','refs/heads/'+branch+':refs/heads/'+branch])
after=remote('remote-after');assert after['refs/heads/'+branch]==head,after
invariants();assert git('show-ref','--heads')==heads
assert git('rev-parse','refs/remotes/origin/'+branch)==head
runs=json.loads(operation('ci-run-list',['gh','run','list','--repo','vpsfreecz/security-advisories','--branch',branch,'--commit',head,'--limit','20','--json','databaseId,url,status,conclusion,headSha,name,event,workflowName,createdAt']))
assert all(row['headSha']==head for row in runs)
(out/'ci-runs.json').write_text(json.dumps(runs,indent=2)+'\n')
r={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'source_anchor':anchor,'base':base,'origin':'git@github.com:vpsfreecz/security-advisories.git','normalSSHfetch_featureFFpush_exactreadback':'PASS;singleNixenvironment;activehooksnotdisabled','remote_before':before,'remote_after':after,'complete_commits':74,'consumed_prefix_unchanged':72,'new_source_units':2,'all111submission_files_byte_preserved':True,'all63external_recovery_boundaries_preserved':True,'frozen_evidence_sha256':'61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274','reviewed_inventory_byte_reuse':reuse,'all_local_head_refs_preserved':True,'whole_worktree_clean':True,'index_empty':True,'diff_checks':'PASS','ci_runs':runs,'CI_waited':False,'slot_returned_to':'lead','no_operations':['advisoryAPI','sourcechanges','reevaluation','recollection','rebase','amend','forcepush','defaultmerge','PR','lifecycle','newtests'],'session_url':'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/'}
(out/'publication-receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'head':head,'remote_exact':True,'clean':True,'index_empty':True,'ci_runs':runs,'receipt':str(out/'publication-receipt.json')},indent=2),flush=True)

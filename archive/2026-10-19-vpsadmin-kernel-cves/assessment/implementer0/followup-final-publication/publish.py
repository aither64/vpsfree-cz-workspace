import datetime,hashlib,json,os,re,subprocess
from pathlib import Path
session=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');owner=session/'assessment/implementer0';out=owner/'followup-final-publication'
head='cfef162049f632016c9e67bca0e400c58c8618d2';source='0b2f060e61c5480ccd09e93d2ecbace39bcb27a1';base='ea6247687fd02417f87e1e5593fecd8b9055925d';branch='2026-10-19-vpsadmin-kernel-cves';default='2026-07-13-security-advisory-automation'
expected_commits=['fb6575f8be054b0be86458304ecdc122b78c9c21','8bdc4f87f3764059c7ad1c629d5de9fbf7a34f78',head]
expected_ids=['CVE-2026-74753','CVE-2026-53260','CVE-2026-72069'];paths={f'advisories/{c}/submission.yml'for c in expected_ids}
def git(*a):return subprocess.check_output(['git',*a],text=True).strip()
def operation(name,args):
 r=subprocess.run(args,text=True,capture_output=True);(out/(name+'.log')).write_text(r.stdout+r.stderr)
 if r.returncode:raise RuntimeError(f'{name} exit{r.returncode}; inspect retained log; no automatic retry')
 return r.stdout
assert git('rev-parse','HEAD')==head and git('branch','--show-current')==branch
assert not git('status','--porcelain=v1')and not git('diff','--cached','--name-only')
assert git('remote','get-url','origin')==git('remote','get-url','--push','origin')=='git@github.com:vpsfreecz/security-advisories.git'
ledgerpath=session/'assessment/implementer1/draft-sync/updates-ledger.json';ledgerhash=hashlib.sha256(ledgerpath.read_bytes()).hexdigest();assert ledgerhash=='c07a5fc8a891cc71938c79774bcc67139cfda2412097f616f34477dd8146f815'
ledger=json.loads(ledgerpath.read_text());completion=json.loads((ledgerpath.parent/'updates-completion.json').read_text());assert completion['final_head']==head and completion['source_head']==source
assert completion['checkpoint_shas']==expected_commits and completion['content_revisions']==[25,14,14]
assert ledger['count']==len(ledger['rows'])==3
assert git('rev-list','--reverse',source+'..'+head).splitlines()==expected_commits
assert git('rev-list','--count',base+'..'+head)=='72'
old69=[line.split('\t')[0]for line in (owner/'followup-publication/complete-series.tsv').read_text().splitlines()]
assert len(old69)==69 and git('rev-list','--reverse',base+'..'+source).splitlines()==old69
assert set(git('diff','--name-only',source,head).splitlines())==paths
checkpoint_rows=[]
for i,(cve,row,commit)in enumerate(zip(expected_ids,ledger['rows'],expected_commits)):
 parent=git('rev-parse',commit+'^');assert parent==(source if i==0 else expected_commits[i-1])
 assert row['cve']==cve and row['checkpoint_sha']==commit and row['state']=='draft'
 path=f'advisories/{cve}/submission.yml';assert git('diff-tree','--no-commit-id','--name-status','-r',commit)=='M\t'+path
 text=git('show',commit+':'+path);fields=dict(re.findall(r'^([a-z_]+): (.*)$',text,re.M))
 assert fields['schema_version']=='2'and fields['source_commit']==parent
 assert int(fields['advisory_id'])==row['advisory_id']and int(fields['remote_content_revision'])==row['content_revision']
 evaluation=json.loads(Path(f'advisories/{cve}/evaluation.json').read_text());assert fields['dossier_digest']==evaluation['dossier_digest']and row['node_counts']==evaluation['completeness']['states']
 checkpoint_rows.append({'cve':cve,'advisory_id':row['advisory_id'],'revision':row['content_revision'],'checkpoint':commit,'source_commit':parent,'path':path,'schema':2,'node_counts':row['node_counts']})
# Original checkpoint commit objects and their actual source parents stay intact.
originalpath=ledgerpath.parent/'ledger.json';assert hashlib.sha256(originalpath.read_bytes()).hexdigest()=='509aadea80374705f3ca392f27064228ed3a8ed9ffce249ba7b898351ca244bf'
original=json.loads(originalpath.read_text())['rows'];assert len(original)==60
original_proof=[]
for row in original:
 commit=row['checkpoint_sha'];assert commit in old69
 path=f'advisories/{row["cve"]}/submission.yml';fields=dict(re.findall(r'^([a-z_]+): (.*)$',git('show',commit+':'+path),re.M))
 assert fields['source_commit']==git('rev-parse',commit+'^')
 assert int(fields['advisory_id'])==row['advisory_id']and fields['remote_content_revision']=='13'
 original_proof.append({'cve':row['cve'],'checkpoint':commit,'source_commit':fields['source_commit'],'original_baseline_preserved_in_commit':True})
old_baselines=json.loads((owner/'followup-baseline-submissions.json').read_text());unchanged={p:sha for p,sha in old_baselines.items()if p not in paths}
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==sha for p,sha in unchanged.items())
assert sum(row['cve']not in expected_ids for row in original)==57
final_baselines={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in Path('advisories').glob('*/submission.yml')}
heads_before=git('show-ref','--heads')
def invariants():
 assert git('rev-parse','HEAD')==head
 assert not git('status','--porcelain=v1')and not git('diff','--cached','--name-only')
 assert hashlib.sha256(Path('.state/evidence.json').read_bytes()).hexdigest()=='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
 assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==sha for p,sha in final_baselines.items())
invariants()
for key in ('OVERCOMMIT_DISABLE','SKIP','ONLY','OVERCOMMIT_UNSAFE'):assert not os.environ.get(key),key
hook=Path(git('rev-parse','--git-path','hooks/pre-push'));assert hook.is_file()and os.access(hook,os.X_OK)and'overcommit'in hook.read_text().lower()
(out/'three-checkpoint-inventory.json').write_text(json.dumps(checkpoint_rows,indent=2)+'\n');(out/'original60-boundary-proof.json').write_text(json.dumps(original_proof,indent=2)+'\n')
(out/'preflight.json').write_text(json.dumps({'head':head,'source':source,'base':base,'complete_commits':72,'unchanged_prefix':69,'new_external_checkpoints':3,'other57_baselines_unchanged':True,'other_unrelated_baselines_unchanged':True,'original60_boundaries_preserved':True,'updates_ledger_sha256':ledgerhash,'frozen61904':True,'clean':True},indent=2)+'\n')
operation('fetch',['git','fetch','origin'])
def remote(name):
 text=operation(name,['git','ls-remote','--symref','origin','HEAD','refs/heads/'+default,'refs/heads/'+branch])
 refs={ref:sha for sha,ref in (line.split('\t')for line in text.splitlines()if'\t'in line and not line.startswith('ref:'))}
 assert 'ref: refs/heads/'+default+'\tHEAD'in text and refs['HEAD']==refs['refs/heads/'+default]==base,refs
 return refs
before=remote('remote-before');assert before['refs/heads/'+branch]==source,before
assert git('rev-parse','refs/remotes/origin/'+default)==base and git('rev-parse','refs/remotes/origin/'+branch)==source
subprocess.run(['git','merge-base','--is-ancestor',source,head],check=True)
invariants();print('All72history/source/checkpoint invariants PASS; expectedSSHrefs confirmed; normal featureFFpush now',flush=True)
operation('push',['git','push','origin','refs/heads/'+branch+':refs/heads/'+branch])
after=remote('remote-after');assert after['refs/heads/'+branch]==head,after
invariants();assert git('show-ref','--heads')==heads_before
assert git('rev-parse','refs/remotes/origin/'+branch)==head
(out/'complete-series.tsv').write_text(git('log','--reverse','--format=%H%x09%P%x09%s',base+'..'+head)+'\n')
(out/'complete-final.diff').write_text(git('diff','--binary',base,head)+'\n');(out/'complete-diff-stat.txt').write_text(git('diff','--stat',base,head)+'\n');(out/'complete-path-inventory.tsv').write_text(git('diff','--numstat',base,head)+'\n')
(out/'three-submission.diff').write_text(git('diff',source,head)+'\n');(out/'three-submission-stat.txt').write_text(git('diff','--stat',source,head)+'\n')
subprocess.run(['git','diff','--check',base,head],check=True);subprocess.run(['git','diff','--check',source,head],check=True)
runs=json.loads(operation('ci-run-list',['gh','run','list','--repo','vpsfreecz/security-advisories','--branch',branch,'--commit',head,'--limit','20','--json','databaseId,url,status,conclusion,headSha,name,event,workflowName,createdAt']))
assert all(row['headSha']==head for row in runs)
(out/'ci-runs.json').write_text(json.dumps(runs,indent=2)+'\n')
r={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'source_head':source,'base':base,'origin':'git@github.com:vpsfreecz/security-advisories.git','normalSSH_fetch_and_feature_only_FFpush':'PASS;singleownedNixenvironment;activehooksnotdisabled','remote_before':before,'remote_after':after,'full_history_commits':72,'unchanged_consumed_prefix_commits':69,'new_distinct_external_recovery_checkpoints':checkpoint_rows,'original60_boundaries_preserved':True,'other57_baselines_unchanged':True,'all_unrelated_baselines_unchanged':True,'source_evaluations_unchanged_except3submission_baselines':True,'all_final_baseline_hashes_unchanged_during_publication':True,'updates_ledger_sha256':ledgerhash,'frozen_evidence_sha256':'61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274','all_local_head_refs_preserved':True,'whole_worktree_clean':True,'index_empty':True,'diff_checks':'PASS','ci_runs':runs,'CI_waited':False,'slot_returned_to':'lead','no_operations':['advisoryAPI','sourcechanges','recollection','rebase','amend','squash','forcepush','defaultmerge','PR','sync','ready','advisorypublication','email','tests','lifecycle'],'session_url':'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/'}
(out/'publication-receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'head':head,'remote_exact':True,'commits':72,'clean':True,'index_empty':True,'ci_runs':runs,'receipt':str(out/'publication-receipt.json')},indent=2),flush=True)

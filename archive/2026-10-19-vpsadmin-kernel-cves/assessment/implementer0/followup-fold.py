import datetime,hashlib,json,os,subprocess
from pathlib import Path
s=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves/assessment/implementer0')
prep=json.loads((s/'followup-review-reconcile-preparation.json').read_text());anchor=prep['consumed_anchor'];reviewed=prep['reviewed_head']
def git(*a):return subprocess.check_output(['git',*a],text=True).strip()
remote=subprocess.run(['git','ls-remote','origin','refs/heads/2026-10-19-vpsadmin-kernel-cves','refs/heads/2026-07-13-security-advisory-automation'],text=True,capture_output=True,check=True)
refs={ref:sha for sha,ref in (line.split('\t')for line in remote.stdout.splitlines()if '\trefs/heads/'in line)}
assert refs['refs/heads/2026-10-19-vpsadmin-kernel-cves']==anchor,refs
assert refs['refs/heads/2026-07-13-security-advisory-automation']=='ea6247687fd02417f87e1e5593fecd8b9055925d',refs
fixup=git('rev-parse','HEAD');assert git('rev-parse','HEAD^')==reviewed
assert git('rev-list','--count',anchor+'..'+fixup)=='3'
assert not git('status','--porcelain=v1')
assert git('rev-parse',prep['backup_ref'])==reviewed
expected=[('pick','15530eff4733933c3f6e1cefd8bf124096e1ed8d'),('fixup',fixup),('pick',reviewed)]
editor=Path('.state/implementer0/followup-autosquash-editor.py').resolve()
program='''#!/usr/bin/env python3
import json, pathlib, sys
expected = EXPECTED
p = pathlib.Path(sys.argv[1])
rows = [line.split()[:2] for line in p.read_text().splitlines() if line.strip() and not line.startswith('#')]
assert len(rows) == 3, rows
assert all(action == want and full.startswith(short) for (action, short), (want, full) in zip(rows, expected)), rows
pathlib.Path(RECEIPT).write_text(json.dumps({'validated_todo': rows, 'bounded_anchor': ANCHOR}, indent=2) + '\\n')
'''.replace('EXPECTED',repr(expected)).replace('RECEIPT',repr(str(s/'followup-review-autosquash-todo.json'))).replace('ANCHOR',repr(anchor))
editor.write_text(program);editor.chmod(0o700)
(s/'followup-review-rebase-preflight.json').write_text(json.dumps({'fixup':fixup,'remote_refs':refs,'remote_rechecked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rebase_anchor':anchor,'sequence_editor':str(editor),'expected_sequence':expected,'setup_output_parser_failure':'Prior attempt stopped before any rebase; corrected by parsing only Git ref lines.'},indent=2)+'\n')
env=os.environ.copy();env['GIT_SEQUENCE_EDITOR']=str(editor)
print('Remote/backup/clean3commitprefix verified; folding bounded unpublished followup',flush=True)
subprocess.run(['git','rebase','--interactive','--autosquash','--no-update-refs',anchor],env=env,check=True)
head=git('rev-parse','HEAD');commits=git('rev-list','--reverse',anchor+'..'+head).splitlines();assert len(commits)==2
assert git('rev-parse',commits[0]+'^')==anchor
assert git('rev-parse',commits[1]+'^')==commits[0]
assert all(not git('show','-s','--format=%s',c).startswith(('fixup!','squash!'))for c in commits)
paths=['advisories/CVE-2026-74753/analysis.md','advisories/CVE-2026-74753/evaluation.json']
assert set(git('diff','--name-only',reviewed,head).splitlines())==set(paths)
assert not git('status','--porcelain=v1')and not git('diff','--cached','--name-only')
assert git('rev-parse',prep['backup_ref'])==reviewed
oldrefs=dict(line.split(' ',1)for line in prep['heads_before'].splitlines());newrefs=dict(line.split(' ',1)for line in git('for-each-ref','--format=%(refname) %(objectname)','refs/heads/').splitlines())
for ref,sha in oldrefs.items():
 if ref!='refs/heads/2026-10-19-vpsadmin-kernel-cves':assert newrefs[ref]==sha,(ref,sha,newrefs[ref])
assert git('rev-list','--reverse','ea6247687fd02417f87e1e5593fecd8b9055925d..'+anchor).splitlines()==prep['consumed_prefix_commits']
for path,sha in json.loads((s/'followup-baseline-submissions.json').read_text()).items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha,path
snap=hashlib.sha256(Path('.state/evidence.json').read_bytes()).hexdigest();assert snap=='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
old=json.loads((s/'followup-review-reconcile-baseline.json').read_text());current=json.loads(Path(paths[1]).read_text());strip=lambda x:{k:v for k,v in x.items()if k not in ('dossier_digest','evaluated_at')};assert strip(old)==strip(current)
subprocess.run(['git','diff','--check',anchor,head],check=True)
subprocess.run(['git','diff','--check',reviewed,head],check=True)
subprocess.run(['git','show','--format=','--check',head],check=True)
# Both new commit patches are focused; B must be exactly the reviewed RT patch.
rt_old=git('diff','15530eff4733933c3f6e1cefd8bf124096e1ed8d',reviewed)
rt_new=git('diff',commits[0],commits[1]);assert rt_old==rt_new
ruby='''r=SecurityAdvisories::Reconciler.new(client:nil)
a=SecurityAdvisories::Advisory.load('CVE-2026-74753')
saved=JSON.parse(File.read('advisories/CVE-2026-74753/evaluation.json'))
raise 'digest mismatch' unless saved['dossier_digest']==a.digest
fresh=r.evaluate(a,persist:false)
raise 'result drift' unless saved.except('evaluated_at')==fresh.except('evaluated_at')
puts 'Final normal74753 loader/digest/frozen fullconclusion equality PASS'
'''
subprocess.run(['ruby','-Ilib','-rsecurity_advisories','-rjson','-e',ruby],check=True)
(s/'followup-reconciled-series.txt').write_text(git('log','--reverse','--format=%H%x09%P%x09%s',anchor+'..'+head)+'\n')
(s/'followup-review-two-path.diff').write_text(git('diff',reviewed,head)+'\n')
(s/'followup-review-range-diff.txt').write_text(git('range-diff',anchor+'..'+reviewed,anchor+'..'+head)+'\n')
r={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_anchor':anchor,'reviewed_head':reviewed,'head':head,'new_A':commits[0],'new_B':commits[1],'backup_ref':prep['backup_ref'],'backup_head':reviewed,'fixup_folded':fixup,'commits_after_anchor':2,'final_tree_vs_reviewed_only_paths':paths,'RT_B_patch_byte_identical':True,'accepted_code_docs_specs_RT_nodes_unchanged':True,'all67_consumed_prefix_commits_unchanged':True,'all_consumed_submission_hashes_unchanged':True,'all_preexisting_backup_heads_unchanged':True,'remote_verified_before_fold':refs,'frozen_evidence_sha256':snap,'all_evaluation_fields_equal_except':['dossier_digest','evaluated_at'],'normal_validate_evaluate74753':'PASS','final_normal_loader_digest_full_reproduction':'PASS','normal_fixup_hooks':'PASS; nonblocking>72bodywarningwithin80, discardedwithfixupmessage','autosquash':'exact3line validatedtodo, --no-update-refs; no hooks disabled','diff_checks':'PASS','whole_worktree_clean':True,'index_empty':True,'slot_returned_to':'lead','no_operations':['API','sourcepush','fetch','defaultmerge','sync','recollection','publication','email','lifecycle']}
(s/'followup-review-reconciliation-receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'head':head,'A':commits[0],'B':commits[1],'backup_ref':prep['backup_ref'],'two_path_only':True,'RTpatch_unchanged':True,'consumed_prefix67_unchanged':True,'clean':True,'index_empty':True},indent=2),flush=True)

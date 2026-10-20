import hashlib,json,pathlib,subprocess
P=pathlib.Path('assessment/implementer1');W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');receipt=json.load(open(P/'primary-citation-fix-preparation.json'));ids=json.load(open('assessment/packages.json'))['groups']['implementer1'];BASE='605d274310890aac5f514924d9b6566033feaee4';START='e617335a60a1a63c7820d1282c29aaed20f8e4fe'
def git(*a):return subprocess.check_output(['git',*a],cwd=W)
assert git('rev-parse','HEAD').decode().strip()==START;assert not git('diff','--cached','--name-only').strip()
expected={'advisories/'+c+'/'+f for c in ids for f in ['analysis.md','evaluation.json']};assert set(git('diff','--name-only').decode().splitlines())==expected
rows=[]
for r in receipt['rows']:
 c=r['cve'];path='advisories/'+c+'/';original=git('show',BASE+':'+path+'analysis.md');current=(W/path/'analysis.md').read_bytes();assert current==original.replace(r['old_url'].encode(),r['replacement_url'].encode())
 assert (W/path/'advisory.yml').read_bytes()==git('show',BASE+':'+path+'advisory.yml')
 old=json.loads(git('show',BASE+':'+path+'evaluation.json'));new=json.load(open(W/path/'evaluation.json'));changed={k for k in set(old)|set(new) if old.get(k)!=new.get(k)};assert changed<= {'dossier_digest','evaluated_at'};assert old['nodes']==new['nodes'] and old['completeness']==new['completeness']
 rows.append({'cve':c,'direct_committed_analysis_url_only':True,'public_yaml_byte_identical':True,'evaluation_changed_keys':sorted(changed),'all_conclusions_unchanged':True})
(P/'citation-direct-blob-validation.json').write_text(json.dumps({'compared_commit':BASE,'start_head':START,'rows':rows},indent=2)+'\n')
subprocess.run(['git','add','--',*sorted(expected)],cwd=W,check=True);assert set(git('diff','--cached','--name-only').decode().splitlines())==expected;subprocess.run(['git','diff','--cached','--check'],cwd=W,check=True)
msg='''fixup! 605d274310890aac5f514924d9b6566033feaee4

Correct primary-record citations to the immutable Linux security/vulns
provider at the already-reviewed source revision. The replacement records
are byte-identical to retained evidence. Refresh evaluation digests while
preserving every node conclusion and all member-facing text.
''';assert max(map(len,msg.splitlines()))<=80;(P/'citation-fixup-message.txt').write_text(msg)
print('Direct committed-blob checks PASS20; staged exact40 analysis/evaluation files')

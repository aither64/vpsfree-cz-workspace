import collections,hashlib,json,pathlib,re,subprocess
W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');P=pathlib.Path('assessment/implementer1/history-consolidation');A='69027fd51efc5c7eb0a4711947b4f9d08190940e';R='34ad7d5785382215cbe00b5140174cad5661a132';session=pathlib.Path.cwd()
def git(*a):return subprocess.check_output(['git',*a],cwd=W)
pre=json.load(open(P/'pre-rebase.json'));head=git('rev-parse','HEAD').decode().strip();assert git('rev-parse','HEAD^{tree}').decode().strip()==pre['tree'],'Rebase changed final tree';assert not git('status','--porcelain','--untracked-files=all').strip();assert not git('diff','--cached','--name-only').strip();assert git('merge-base',A,'HEAD').decode().strip()==A
series=git('log','--reverse','--format=%H %s',A+'..HEAD').decode();assert len(series.splitlines())==5,series;assert not re.search(r'fixup!|squash!|tidy',series,re.I);(P/'series-after.txt').write_text(series)
refs_before=dict(line.split(' ',1) for line in (P/'refs-before.txt').read_text().splitlines());refs_after=dict(line.split(' ',1) for line in git('for-each-ref','--format=%(refname) %(objectname)','refs/heads','refs/remotes').decode().splitlines())
for ref,sha in refs_before.items():
 if ref!='refs/heads/2026-10-19-vpsadmin-kernel-cves':assert refs_after.get(ref)==sha,(ref,sha,refs_after.get(ref))
assert refs_after[pre['retained_backup_ref']]==pre['head'];assert subprocess.run(['git','merge-base','--is-ancestor',R,pre['retained_backup_ref']],cwd=W).returncode==0
changed=git('diff','--name-only',R,'HEAD').decode().splitlines();assert len(changed)==80,len(changed);assert all(re.fullmatch(r'advisories/CVE-2026-\d+/(analysis.md|evaluation.json)',f) for f in changed)
analyses=[f for f in changed if f.endswith('analysis.md')];evaluations=[f for f in changed if f.endswith('evaluation.json')];assert len(analyses)==len(evaluations)==40
maps=[]
for owner in ['implementer0','implementer1']:
 maps+=json.load(open(session/'assessment'/owner/'primary-citation-fix-preparation.json'))['rows']
mapping={r['cve']:r for r in maps};rows=[];kvm_diffs=[]
for path in analyses:
 c=path.split('/')[1];old=git('show',R+':'+path);new=git('show','HEAD:'+path);m=mapping[c];expected=old.replace(m['old_url'].encode(),m['replacement_url'].encode());extra=new!=expected
 if extra:kvm_diffs.append(c)
 epath=path.replace('analysis.md','evaluation.json');eold=json.loads(git('show',R+':'+epath));enew=json.loads(git('show','HEAD:'+epath));ek={k for k in set(eold)|set(enew) if eold.get(k)!=enew.get(k)};assert ek<={'dossier_digest','evaluated_at'},(c,ek);assert eold['nodes']==enew['nodes'] and eold['completeness']==enew['completeness'];rows.append({'cve':c,'citation_only':not extra,'extra_kvm_paragraph':extra,'evaluation_changed_keys':sorted(ek),'all_conclusions_unchanged':True})
assert set(kvm_diffs)=={'CVE-2026-89929','CVE-2026-89930','CVE-2026-89932','CVE-2026-98720'},kvm_diffs
(P/'range-diff.txt').write_bytes(git('range-diff','--no-color',A+'..'+R,A+'..HEAD'));(P/'final-tree-diff.txt').write_bytes(git('diff','--no-ext-diff','--no-color',R,'HEAD'));(P/'final-changed-paths.txt').write_text('\n'.join(changed)+'\n');subprocess.run(['git','diff','--check',R,'HEAD'],cwd=W,check=True)
sha=hashlib.sha256((W/'.state/evidence.json').read_bytes()).hexdigest();assert sha=='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274';r={'schema':1,'anchor':A,'original_reviewed_head':R,'pre_squash_head':pre['head'],'final_head':head,'final_tree':git('rev-parse','HEAD^{tree}').decode().strip(),'pre_squash_tree_identical':True,'logical_commits_above_anchor':5,'logical_commits_including_anchor':6,'original_reviewed_reachable_backup':pre['retained_backup_ref'],'remote_default_other_refs_unchanged':True,'whole_worktree_clean':True,'index_empty':True,'changed_paths':len(changed),'analysis_count':40,'evaluation_count':40,'public_yaml_code_schema_specs_other_files_byte_identical':True,'all_node_conclusions_unchanged':True,'extra_kvm_paragraph_cves':kvm_diffs,'snapshot_sha256':sha,'rows':rows};(P/'final-proof.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2));print(series)

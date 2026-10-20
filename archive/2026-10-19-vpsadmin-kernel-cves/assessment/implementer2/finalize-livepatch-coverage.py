import collections, datetime, hashlib, json
from pathlib import Path
S=Path(__file__).resolve().parents[2]
W=S.parents[1]/'worktrees'/S.name/'security-advisories'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
identity_path=S/'assessment/implementer0/livepatch-source-identities.json'
identities=load(identity_path)
expected='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
assert identities['snapshot_sha256']==sha(W/'.state/evidence.json')==expected
precheck={r['os_revision']:r for r in load(S/'assessment/implementer2/livepatch-content-precheck.json')}
positive={r for r,v in precheck.items() if v['has_active_guard'] and v['has_release_deactive']}
assert positive=={'97a8c8fc64b1ef6339bca9e85a8ccdd6884cb3e0','93014dd1f7126798617a927f1e8a3a556faf046c','80a0017d7b35cdfd4d11311876f487d2d56e3e3d'}
source_by_revision={r['vpsadminos_revision']:r for r in identities['sources']}
for rev,r in precheck.items():
 p=S/r['source_file'];assert sha(p)==r['patch_sha256']
 start=p.read_text().index('diff --git a/fs/nfs/nfs4proc.c ')
 end=p.read_text().find('\ndiff --git ',start+1)
 section=p.read_text()[start:end if end!=-1 else None]
 # Precheck hashes the section without its separating final newline.
 assert hashlib.sha256(section.encode()).hexdigest()==r['nfs_section_sha256']
 for source in source_by_revision[rev]['recipes']+source_by_revision[rev]['payloads']:
  assert sha(S/source['file'])==source['sha256']
accepted=[t for t in identities['unique_bound_tuples'] if t['vpsadminos_revision'] in positive]
assert len(accepted)==3 and all(t['id']=='livepatch_6' and t['patch_version']=='6' for t in accepted)
rows=[]
for r in identities['rows']:
 bound=[b for b in r['candidate_bindings'] if b['vpsadminos_revision'] in positive]
 if r['disposition']=='unresolved_sparse_metadata':
  decision='unresolved_sparse_identity';reason='No independent acceptance: missing module version/kernel identity. Existing evaluator may inherit only from its immediately preceding permitted same-boot snapshot; this receipt invents no tuple.'
 elif bound:
  decision='accepted_correction_content';reason='Exact source-bound original-a238 livepatch_6 version6 contains the FREE_STATEID server/superblock lifetime correction. Activation and transition timing remain evaluator decisions.'
 else:
  decision='excluded_correction_absent';reason='Exact bound earlier cumulative version2-5 NFS replacement does not contain the FREE_STATEID nfs_sb_active/nfs_sb_deactive correction; no coverage accepted for74730.'
 rows.append({'cve':'CVE-2026-74730','tuple_key':r['tuple_key'],'identity_disposition':r['disposition'],'observations':r['observations'],'module_id':r['observed_identity']['id'],'patch_version':r['observed_identity']['patch_version'],'kernel_version':r['observed_identity']['kernel_version'],'booted_release':r['observed_identity']['booted_release'],'reported_linux_revision':r['observed_identity']['linux_revision'],'candidate_bindings':r['candidate_bindings'],'decision':decision,'reason':reason})
coverage=load(S/'assessment/implementer2/livepatch-coverage.json')
coverage.update({'schema':1,'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'bounded_observed_identity_and_content_review_complete','snapshot_sha256':expected,'identity_receipt':{'path':'assessment/implementer0/livepatch-source-identities.json','sha256':sha(identity_path)},'counts':{'observed_rows':len(rows),'content_dispositions':dict(collections.Counter(r['decision'] for r in rows)),'accepted_unique_tuples':len(accepted),'excluded_earlier_unique_tuples':len(identities['unique_bound_tuples'])-len(accepted)},'observed_content_dispositions':rows,'accepted_livepatches':accepted,'accepted_kernel_builds':[]})
cve=coverage['rows'][0]
cve['accepted_observed_tuples']=[r['tuple_key'] for r in rows if r['decision']=='accepted_correction_content']
cve['limit']='Content acceptance is separate from enabled/stable observed activation. Evaluator controls same-boot inheritance and atomic transitions. Quarantinedv6 is not recommended for deployment. No observed NFS-cancel variant/build or complete deployed identity/digests to accept; no build fabricated.'
cve['content_review']['acceptance_limit']='Central identity receipt now binds all three positive source recipes. Only exact listed tuples accepted; neither an earlier version nor NFS-cancel variant is interchangeable.'
cve['intrinsic_build_disposition']='Source correction verified in563bbb35; no matching observation, no accepted kernel build.'
(S/'assessment/implementer2/livepatch-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
yml=W/'advisories/CVE-2026-74730/advisory.yml'
dossier=load(yml);texts=dossier['texts'];dossier['platform']['accepted_livepatches']=accepted
yml.write_text(json.dumps(dossier,indent=2,ensure_ascii=False)+'\n');assert load(yml)['texts']==texts
print(json.dumps(coverage['counts'],indent=2))

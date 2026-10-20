import hashlib,json,os,pathlib,shutil
P=pathlib.Path('assessment/implementer1');W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');m=json.load(open(P/'primary-citation-fix-preparation.json'));expected='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274';assert hashlib.sha256((W/'.state/evidence.json').read_bytes()).hexdigest()==expected
B=W/'.state/implementer1-citation-fix-before';B.mkdir(mode=0o700,exist_ok=True);os.chmod(B,0o700);out=[]
for row in m['rows']:
 c=row['cve'];d=W/'advisories'/c;p=d/'analysis.md';raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==row['analysis_sha256_before'],c;old=row['old_url'].encode();new=row['replacement_url'].encode();assert raw.count(old)==row['old_occurrences']==1;assert row['retained_sha256']==row['decoded_sha256'];backup=B/c;backup.mkdir(mode=0o700,exist_ok=True)
 for name in ['analysis.md','advisory.yml','evaluation.json']:
  dest=backup/name;assert not dest.exists(),(c,'repeated mutation refused');shutil.copyfile(d/name,dest);os.chmod(dest,0o600)
 after=raw.replace(old,new);p.write_bytes(after);assert after.replace(new,old)==raw
 out.append({'cve':c,'replacement_count':1,'analysis_sha256_before':hashlib.sha256(raw).hexdigest(),'analysis_sha256_after':hashlib.sha256(after).hexdigest(),'advisory_sha256_unchanged':hashlib.sha256((d/'advisory.yml').read_bytes()).hexdigest()})
(P/'citation-fix-applied.json').write_text(json.dumps({'schema':1,'snapshot_sha256':expected,'scope':'Only verified20primary provider/path URLs replaced; evaluation regeneration next','rows':out},indent=2)+'\n');print('Changed exactly20verified URLs; publicYAML untouched; backuprestricted')

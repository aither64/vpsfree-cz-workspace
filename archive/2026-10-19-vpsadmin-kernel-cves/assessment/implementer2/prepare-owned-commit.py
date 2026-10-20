import json,hashlib,subprocess
from pathlib import Path
S=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');W=Path('.');receipts={}
for f in ['editorial-first5.json','editorial-owner2-next9.json','editorial-owner2-final6.json']:
 for r in json.loads((S/'assessment'/f).read_text())['rows']:receipts[r['cve']]=r['after_sha256']
r=json.loads((S/'assessment/editorial-98368-privilege-clarification.json').read_text());receipts[r['cve']]=r['after_sha256']
cifs={'CVE-2026-'+v for v in ['64383','64384','64385','64386','64387','64597','89633']}
matched=[]
for c,h in receipts.items():
 x=json.loads((W/'advisories'/c/'advisory.yml').read_text());x['platform'].pop('history_start_overrides',None)
 if c=='CVE-2026-74730':x['platform']['accepted_livepatches']=[]
 if c in cifs:
  assert x['impact']['vps_root']=='possible'
  # Approved post-editorial ordinary-file-user impact correction; texts untouched.
  x['impact']['vps_root']='not_applicable'
 assert hashlib.sha256((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()).hexdigest()==h,c
 matched.append(c)
assert len(matched)==20
p=S/'assessment/implementer2/final-package-checks.json';x=json.loads(p.read_text());x['lead_editorial_exact_hashes_preserved_after_removing_reviewed_technical_changes']=20;x['post_editorial_technical_changes']=['reviewed Node126-only lifecycle scope','74730 three exact accepted livepatch tuples','CIFS7 vps_root:possible ordinary file-user gain accepted by lead'];p.write_text(json.dumps(x,indent=2)+'\n')
ids=json.loads((S/'assessment/packages.json').read_text())['groups']['implementer2'];paths=[str(W/'advisories'/c/name) for c in ids for name in ('analysis.md','advisory.yml','evaluation.json')]
assert not subprocess.check_output(['git','diff','--cached','--name-only'],text=True).strip()
for c in ids:assert sorted(x.name for x in (W/'advisories'/c).iterdir())==['advisory.yml','analysis.md','evaluation.json']
subprocess.run(['git','add','--',*paths],check=True)
actual=subprocess.check_output(['git','diff','--cached','--name-only'],text=True).splitlines();assert set(actual)==set(paths) and len(actual)==60
subprocess.run(['git','diff','--cached','--check'],check=True)
msg='''Assess filesystem, MPTCP and XFRM kernel vulnerabilities

Record twenty approved CVEs with primary and exact platform source
analysis, complete version ranges, tenant prerequisites and separate
privilege, isolation and availability conclusions in English and Czech.

Bind evaluations to the frozen fleet snapshot and reviewed production
history scope. Preserve verified historical NFS livepatch mitigation and
keep the ineffective CIFS stable backports affected rather than claiming
an unsupported fix or publication readiness.
'''
assert max(map(len,msg.splitlines()))<=80
(S/'assessment/implementer2/assessment-commit-message.txt').write_text(msg)
print('20 editorial hashes match after reviewed technical-only changes; exact60 staged; whitespacecheck PASS')

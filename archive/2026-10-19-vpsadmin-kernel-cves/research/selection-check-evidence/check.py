#!/usr/bin/env python3
"""Read-only comparison of human CVE rows to pinned primary evidence."""
import collections,gzip,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]; E=R/'cve-evidence'
load=lambda p:json.loads(p.read_text())
manual=load(E/'manual-triage.json'); ledger={x['cve']:x for x in load(E/'range-records.json')}
dedup=set(re.findall(r'CVE-\d{4}-\d+', (R/'platform-evidence/dedup-cves.txt').read_text()))
errors=[]; rows=[]; comparisons=[]
for m in manual:
 c=m['cve']; p=load(E/'records'/f'{c}.json'); primary=p['containers']['cna']; fix=(m['fix_release'],m['fix_sha'])
 checks={'published':p['cveMetadata']['state']==m['state']=='PUBLISHED','id_matches':p['cveMetadata']['cveId']==c,'range_join':fix in [(f['release'],f['sha']) for f in ledger[c]['fixes']],'in_inclusive_range':95<=int(m['fix_release'].split('.')[-1])<=113,'not_reported':c not in dedup,'metrics_match':m['metrics']==primary.get('metrics',[])}
 commits=set(re.findall(r'^commit ([0-9a-f]{40})$',gzip.open(E/f"ChangeLog-{m['fix_release']}.gz",'rt').read(),re.M));checks['exact_changelog_sha']=m['fix_sha'] in commits
 rows.append({'cve':c,'fix_release':fix[0],'fix_sha':fix[1],'checks':checks})
 for k,v in checks.items():
  if not v:errors.append({'cve':c,'check':k})
for name in ['cve-candidates.md','classification.md','platform-baseline.md']:
 for line_no,line in enumerate((R/name).read_text().splitlines(),1):
  if not line.startswith('|'):continue
  ids=list(dict.fromkeys(re.findall(r'CVE-\d{4}-\d+',line)))
  if not ids and name=='platform-baseline.md' and re.match(r'^\| \d{5}',line):ids=['CVE-2026-'+x for x in re.findall(r'\b\d{5}\b',line.split('|')[1])]
  for c in ids:
   if c not in ledger:continue
   fixes=ledger[c]['fixes']; expected={f['release'] for f in fixes}
   versions=set(re.findall(r'6\.12\.\d+',line.split('|')[2])); short=re.match(r'^\|[^|]+\|\s*\.(\d+)\s*\|',line)
   if short:versions.add('6.12.'+short[1])
   issues=[]
   if versions and not versions<=expected:issues.append('fix_release')
   sha_links=re.findall(r'https://git.kernel.org/stable/c/([0-9a-f]{40})',line)
   if any(s not in {f['sha'] for f in fixes} for s in sha_links):issues.append('fix_sha')
   metrics=ledger[c]['metrics']; scores=[v['baseScore'] for metric in metrics for k,v in metric.items() if k.startswith('cvss') and isinstance(v,dict) and 'baseScore' in v]
   cells=line.split('|'); scorecell=cells[-2].strip() if name=='cve-candidates.md' else cells[3].strip() if name=='classification.md' and len(cells)>4 else ''
   score=re.match(r'^(\d+\.\d+)\s+(?:HIGH|CRITICAL|High|Critical)',scorecell)
   if score and float(score[1]) not in scores:issues.append('score')
   if scorecell.lower().startswith('unscored') and scores:issues.append('unscored')
   comparisons.append({'file':name,'line':line_no,'cve':c,'versions':sorted(versions),'sha_checks':len(sha_links),'score_checked':bool(score) or scorecell.lower().startswith('unscored'),'issues':issues})
   for issue in issues:errors.append({'file':name,'line':line_no,'cve':c,'check':issue})
inputs=[E/n for n in ['manual-triage.json','range-records.json','coverage.json','source-manifest.json','stable-source-verification.json']]+[R/n for n in ['classification.md','cve-candidates.md','platform-baseline.md','platform-evidence/dedup-cves.txt']]
result={'date':'2026-10-19','manual_count':len(manual),'unique_manual_count':len({m['cve'] for m in manual}),'human_rows_checked':len(comparisons),'human_score_checks':sum(r['score_checked'] for r in comparisons),'human_sha_checks':sum(r['sha_checks'] for r in comparisons),'errors':errors,'manual_checks':rows,'human_comparisons':comparisons,'input_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}}
(R/'selection-check-evidence/result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['manual_checks','human_comparisons','input_sha256']},indent=2))

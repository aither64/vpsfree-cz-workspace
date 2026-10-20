#!/usr/bin/env python3
"""Validate a selection snapshot; subsequent runs check changed entries only."""
import collections,gzip,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]; O=Path(__file__).resolve().parent
raw=(R/'selection.json').read_bytes(); s=json.loads(raw)
priorpath=O/'selection-snapshot.json'; old=json.loads(priorpath.read_text()) if priorpath.exists() else None
before={e['cve']:e for e in old['entries']} if old else {}; entries=s['entries']; now={e['cve']:e for e in entries}
changed=[c for c,e in now.items() if before.get(c)!=e]; removed=sorted(set(before)-set(now)); errors=[]; results=[]
ledger={e['cve']:e for e in json.loads((R/'cve-evidence/range-records.json').read_text())}; dedup=set(re.findall(r'CVE-\d{4}-\d+', (R/'platform-evidence/dedup-cves.txt').read_text()))
counts=dict(collections.Counter(e['decision'] for e in entries))
if len(entries)!=len(now):errors.append('duplicate IDs')
if counts!=s['counts']:errors.append('declared counts differ')
for c in changed:
 e=now[c]; p=ledger.get(c); checks={'in_primary_ledger':bool(p),'not_public_duplicate':c not in dedup,'decision_source_exists':(R/e['decision_source']).is_file()}
 if p:
  checks.update(title_matches=e['title']==p['title'],fix_matches=any(f['release']==e['first_fix_release'] and f['sha']==e['stable_fix_sha'] for f in p['fixes']),primary_url_matches=e['primary_url']==p['cna_url'],metrics_match=e['cvss_metrics']==[{k:v for k,v in m.items() if k.startswith('cvss')} for m in p['metrics']])
  recordpath=R/'cve-evidence/records'/f'{c}.json'
  if recordpath.exists():checks['published']=json.loads(recordpath.read_text())['cveMetadata']['state']=='PUBLISHED'
  else:checks['published']='ledger source manifest asserts all PUBLISHED; no individual cached record'
  version=e['first_fix_release']; checks['inclusive_range']=95<=int(version.split('.')[-1])<=113
  checks['exact_release_changelog_sha']=e['stable_fix_sha'] in re.findall(r'^commit ([0-9a-f]{40})$',gzip.open(R/'cve-evidence'/f'ChangeLog-{version}.gz','rt').read(),re.M)
 results.append({'cve':c,'decision':e['decision'],'checks':checks})
 errors.extend({'cve':c,'check':k} for k,v in checks.items() if v is False)
r={'selection_sha256':hashlib.sha256(raw).hexdigest(),'status':s['status'],'counts':counts,'total_unique':len(now),'baseline':old is None,'changed_or_added_ids':changed,'removed_ids':removed,'errors':errors,'checks':results}
name='selection-result.json' if old is None else 'selection-delta-result.json'
(O/name).write_text(json.dumps(r,indent=2)+'\n')
if old is None:priorpath.write_bytes(raw)
print(json.dumps({k:v for k,v in r.items() if k!='checks'},indent=2))

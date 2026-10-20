#!/usr/bin/env python3
import collections,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]; p=R.parent/'selection-for-approval.md'; raw=p.read_bytes(); s=json.loads((R/'selection.json').read_text()); entries={e['cve']:e for e in s['entries']}; seen=[];errors=[]; rows=[]; group=None
for n,line in enumerate(raw.decode().splitlines(),1):
 if line.startswith('## Recommended'):group='recommended'
 elif line.startswith('## Conditional'):group='conditional_host_enabled'
 elif line.startswith('## Borderline'):group='borderline_not_recommended'
 if not line.startswith('| [CVE-'):continue
 cells=line.split('|');c=re.search(r'CVE-\d{4}-\d+',cells[1])[0]; e=entries[c]; seen.append(c)
 metrics=e['cvss_metrics']; ratings=[f"{v['baseScore']:.1f} {v['baseSeverity'].title()}" for m in metrics for k,v in m.items() if k.startswith('cvss')]
 checks={'group':group==e['decision'],'fix':cells[2].strip()==e['first_fix_release'],'score':cells[3].strip() in (ratings or ['Not supplied']),'url':re.search(r'\]\(([^)]+)\)',cells[1])[1]==e['primary_url']}
 rows.append({'cve':c,'line':n,'checks':checks});errors.extend({'cve':c,'check':k} for k,v in checks.items() if not v)
expected={c for c,e in entries.items() if e['decision']!='deferred_not_eligible'}
if set(seen)!=expected:errors.append({'missing':sorted(expected-set(seen)),'extra':sorted(set(seen)-expected)})
if len(seen)!=len(set(seen)):errors.append('duplicate table IDs')
platform=(R/'platform-baseline.md').read_text(); correction=next(l for l in platform.splitlines() if l.startswith('| ip6_tunnel:') and 'CVE-2026-74597' in l)
corrected='IPV6_TUNNEL=y is built in' in correction and 'mip6' in correction and 'absent from default preload' in correction
if not corrected:errors.append('74597 correction not confirmed')
result={'selection_sha256':hashlib.sha256((R/'selection.json').read_bytes()).hexdigest(),'approval_sha256':hashlib.sha256(raw).hexdigest(),'table_rows':len(seen),'unique_ids':len(set(seen)),'counts':dict(collections.Counter(entries[c]['decision'] for c in seen)),'errors':errors,'74597_narrative_corrected':corrected,'74597_source_row':correction,'rows':rows}
(R/'selection-check-evidence/approval-result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['rows','74597_source_row']},indent=2))

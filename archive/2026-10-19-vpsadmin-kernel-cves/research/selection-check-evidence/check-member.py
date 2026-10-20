#!/usr/bin/env python3
import collections,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]; O=Path(__file__).resolve().parent
raw=(R/'member-selection.json').read_bytes(); s=json.loads(raw); old=json.loads((R/'selection.json').read_text()); prior={e['cve']:e for e in old['entries']}; ledger={e['cve']:e for e in json.loads((R/'cve-evidence/range-records.json').read_text())}; entries=s['entries']; now={e['cve']:e for e in entries}; dedup=set(re.findall(r'CVE-\d{4}-\d+',(R/'platform-evidence/dedup-cves.txt').read_text())); errors=[]; checks=[]
core=['title','first_fix_release','stable_fix_sha','primary_url']
cvss=lambda ms:[{k:v for k,v in m.items() if k.startswith('cvss')} for m in ms]
retained={c for c,e in prior.items() if e['decision']=='recommended'}
if not retained<=now.keys():errors.append('prior41 missing')
for c in retained:
 e=now[c]; p=prior[c]
 if any(e[k]!=p[k] for k in core) or cvss(e['cvss_metrics'])!=cvss(p['cvss_metrics']):errors.append({'cve':c,'issue':'prior41 factual drift'})
for e in entries:
 c=e['cve']; p=ledger[c]; record=R/e['primary_record_path']; x=json.loads(record.read_text()); scope=e['exposure']; tests={'published':x['cveMetadata']['state']==e['primary_status']=='PUBLISHED','primary_id':x['cveMetadata']['cveId']==c,'public_dedup':c not in dedup,'decision_source':(R/e['decision_source']).is_file(),'primary_record':record.is_file(),'title':e['title']==p['title'],'fix':any(f['release']==e['first_fix_release'] and f['sha']==e['stable_fix_sha'] for f in p['fixes']),'metrics':cvss(e['cvss_metrics'])==cvss(p['metrics']),'url':e['primary_url']==p['cna_url'],'range':95<=int(e['first_fix_release'].split('.')[-1])<=113,'scope_present':bool(scope.get('scope')),'runtime_unknown':'unknown' in scope.get('runtime_and_history',''),'mitigation_unassessed':scope.get('current_mitigation','').startswith('unassessed')}
 if scope['conclusion']=='not_affected':
  config=R/'platform-evidence/frozen-6.12.95-dot-config.txt'; tests['config_hash']=hashlib.sha256(config.read_bytes()).hexdigest()==scope['exact_build']['config_sha256']; condition=scope['required_condition_or_exclusion']; tests['config_exclusion']=condition in config.read_text() or ('# '+condition.replace('=n',' is not set')) in config.read_text();tests['exact_scope']='exact' in scope['scope'] and bool(scope.get('roles')) and bool(scope.get('time'))
 checks.append({'cve':c,'new_to_prior69':c not in prior,'checks':tests})
 errors.extend({'cve':c,'check':k} for k,v in tests.items() if not v)
groups=dict(collections.Counter(e['proposal_group'] for e in entries)); seen=[]; rows=[]; group=None
text=(R.parent/'member-selection-for-approval.md').read_text()
for n,line in enumerate(text.splitlines(),1):
 if line.startswith('## Retained'):group='retained_tenant_path'
 elif line.startswith('## Informative'):group='not_affected_exact_build'
 elif line.startswith('## Serious privileged'):group='privileged_program_conditional'
 elif line.startswith('## Host feature'):group='new_member_relevant_conditional'
 if not line.startswith('| [CVE-'):continue
 cells=line.split('|'); c=re.search(r'CVE-\d{4}-\d+',cells[1])[0];seen.append(c);e=now[c];ratings=[f"{v['baseScore']:.1f} {v['baseSeverity'].title()}" for m in e['cvss_metrics'] for k,v in m.items() if k.startswith('cvss')]
 tests={'group':group==e['proposal_group'],'version':cells[2].strip()==e['first_fix_release'],'score':cells[3].strip() in (ratings or ['Not supplied']),'url':re.search(r'\]\(([^)]+)\)',cells[1])[1]==e['primary_url']};rows.append({'cve':c,'line':n,'checks':tests});errors.extend({'cve':c,'table_check':k} for k,v in tests.items() if not v)
if set(seen)!=set(now) or len(seen)!=len(set(seen)):errors.append('table exactset/duplicates')
if len(entries)!=len(now) or len(now)!=s['counts']['proposed']:errors.append('entry duplicates/count')
r={'status':s['status'],'selection_sha256':hashlib.sha256(raw).hexdigest(),'approval_sha256':hashlib.sha256(text.encode()).hexdigest(),'count':len(now),'groups':groups,'prior41_preserved':not any(isinstance(x,str) and 'prior41' in x or isinstance(x,dict) and x.get('issue')=='prior41 factual drift' for x in errors),'new_to_prior69':sorted(set(now)-set(prior)),'prior69_not_proposed':sorted(set(prior)-set(now)),'table_count':len(seen),'errors':errors,'checks':checks,'table_rows':rows}
(O/'member-result.json').write_text(json.dumps(r,indent=2)+'\n');(O/'member-snapshot.json').write_bytes(raw);print(json.dumps({k:v for k,v in r.items() if k not in ['checks','table_rows']},indent=2))

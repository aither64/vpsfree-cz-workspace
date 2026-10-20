#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];O=Path(__file__).resolve().parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((O/'member-snapshot.json').read_text());b=json.loads((R/'member-selection.json').read_text());aa={e['cve']:e for e in a['entries']};bb={e['cve']:e for e in b['entries']}; errors=[]; changed={};paths=[]
if set(aa)!=set(bb):errors.append('proposed ID set changed')
core=['title','first_fix_release','stable_fix_sha','cvss_metrics','primary_url','proposal_group','primary_record_path','primary_status']
for c,e in bb.items():
 delta=[k for k in set(e)|set(aa[c]) if e.get(k)!=aa[c].get(k)]
 if delta:changed[c]=delta
 if any(e.get(k)!=aa[c].get(k) for k in core):errors.append({'cve':c,'issue':'factual/group drift'})
 if not delta:continue
 ex=e['exposure']
 for k in ['exact_scope','node_roles','calendar_period','current_deployed_status','historical_fleet_interval','mitigation_state']:
  if not ex.get(k):errors.append({'cve':c,'missing_scope':k})
 for ref in ex.get('source_gate_refs',[]):
  if ref not in e.get('source_gate_evidence',{}):errors.append({'cve':c,'missing_gate':ref})
controls=b['review_only_entries']+b['deferred_entries']
if len(controls)!=7 or len(set(e['cve'] for e in controls)|set(bb))!=67:errors.append('control counts/overlap')
def walk(obj):
 if isinstance(obj,dict):
  for k,v in obj.items():
   if k in ['file','provenance','primary_record_path','source_manifest'] and isinstance(v,str):paths.append(v)
   elif k=='files':paths.extend(v)
   elif k=='evidence_record' and isinstance(v,str):paths.append(v.split('#')[0])
   walk(v)
 elif isinstance(obj,list):
  for v in obj:walk(v)
walk([bb[c] for c in changed]+controls)
missing=sorted({p for p in paths if not (R/p).is_file()})
if missing:errors.append({'missing_paths':missing})
manifest=R/b['source_manifest'];m=json.loads(manifest.read_text());hashchecks={i['path']:h(manifest.parent/i['path'])==i['sha256'] for i in m['inputs']}
if not all(hashchecks.values()):errors.append({'manifest_hash_mismatches':[p for p,v in hashchecks.items() if not v]})
if h(manifest)!=b['source_manifest_sha256']:errors.append('manifest self hash')
if h(R/'member-relevance-evidence/proposal.json')!=b['bounded_evidence_sha256']:errors.append('bounded evidence hash')
approvalhash=h(R.parent/'member-selection-for-approval.md'); priorresult=json.loads((O/'member-result.json').read_text())
if approvalhash!=priorresult['approval_sha256']:errors.append('approval document changed')
r={'status':b['status'],'selection_sha256':h(R/'member-selection.json'),'approval_sha256':approvalhash,'proposed_count':len(bb),'changed_entry_count':len(changed),'unchanged_entry_count':len(bb)-len(changed),'changed_fields':changed,'all_core_fields_preserved':not any(isinstance(x,dict) and x.get('issue')=='factual/group drift' for x in errors),'controls':len(controls),'source_paths_checked':len(set(paths)),'manifest_input_hashes':hashchecks,'errors':errors,'limits':'Object delta, required field/path presence and provenance hashes only; no repeated primary facts or security reclassification. Approval exact60 table check inherited from byte-identical accepted document and unchanged core/group fields.'}
(O/'member-final-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k not in ['changed_fields','manifest_input_hashes']},indent=2))

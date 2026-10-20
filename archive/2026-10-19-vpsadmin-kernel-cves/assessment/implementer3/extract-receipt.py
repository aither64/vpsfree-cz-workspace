#!/usr/bin/env python3
import json,hashlib,os,re,collections,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; REPO=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories'); state=REPO/'.state';p=state/'evidence.json';raw=p.read_bytes();sha=hashlib.sha256(raw).hexdigest();assert sha=='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'; x=json.loads(raw);assert x['schema_version']==8
out=Path(__file__).resolve().parent
stamp=lambda s:datetime.datetime.fromisoformat(s.replace('Z','+00:00'))
t=stamp(x['collected_at']);counts=collections.Counter(); flags=[];observations=[];tuples={};issues=[];release_counts=collections.Counter();req=json.loads((out/'union-result.json').read_text());required=set(req['collector_all_dossiers_option_names']); catalogs=[]
for digest,cat in x['kernel_configurations'].items():
 assert isinstance(cat['options'],dict); names=set(cat['options']);catalogs.append({'available_options':len(names),'missing_required_options':sorted(required-names)})
def releases(k,link):
 for field in ['booted_release','reported_release']:
  counts['release_fields_checked']+=1; v=k.get(field)
  if not v:counts['missing_release_fields']+=1;continue
  release_counts[v]+=1
  if not re.fullmatch(r'\d+\.\d+\.\d+',v):flags.append(dict(link,field=field,release=v,prerelease=bool(re.search(r'rc|alpha|beta|pre',v,re.I)),relevant_7_2=bool(re.match(r'^7\.2(?:\.|-)',v))))
def patches(arr,k,software,link):
 if arr is None:counts['missing_livepatch_container']+=1;return
 assert isinstance(arr,list)
 counts['livepatch_containers']+=1
 if not arr:counts['empty_livepatch_containers']+=1
 for patch in arr:
  counts['patch_observations']+=1
  ident={'id':patch.get('id'),'patch_version':patch.get('patch_version'),'kernel_version':patch.get('kernel_version'),'booted_release':k.get('booted_release'),'reported_release':k.get('reported_release'),'linux_revision':k.get('kernel_source_revision'),'vpsadminos':[s for s in software if s.get('component')=='vpsadminos']}
  key=hashlib.sha256((sha+json.dumps(ident,sort_keys=True,separators=(',',':'))).encode()).hexdigest()
  entry=tuples.setdefault(key,{'tuple_key':key,'identity':ident,'observations':0,'activation_states':[]});entry['observations']+=1
  activation={f:patch.get(f) for f in ['loaded','enabled','transition']}
  if activation not in entry['activation_states']:entry['activation_states'].append(activation)
  observations.append({'tuple_key':key,**link,'boot_id':k.get('boot_id'),'kernel':k,'software_versions':software,'patch':patch})
for n in x['nodes']:
 counts['nodes']+=1; k=n['kernel'];link={'node_id':n['node_id'],'node_name':n['node_name'],'kind':'current'};releases(k,link);patches(n['runtime_mitigations'].get('livepatches'),k,n['software_versions'],link)
 problems=[]
 try:
  if (t-stamp(n['received_at'])).total_seconds()>900:problems.append('receipt_older_than15min')
  if (stamp(n['observed_at'])-stamp(n['received_at'])).total_seconds()>300:problems.append('observation_future_skew')
  cov=k['history_coverage'];required_since=stamp(req['collector_all_dossiers_history_required_since'])
  if stamp(cov['started_at'])>required_since:problems.append('history_start_after_required')
  if (t-stamp(cov['observed_through'])).total_seconds()>900:problems.append('history_end_stale')
  rec=cov['reconstruction']
  if required_since<stamp(cov['exact_events_started_at']):
   if rec.get('complete') is not True:problems.append('reconstruction_incomplete')
   if stamp(rec['started_at'])>required_since:problems.append('reconstruction_start_after_required')
 except (KeyError,TypeError,ValueError,AttributeError):problems.append('timestamp_or_coverage_shape')
 if problems:issues.append({'node_id':n['node_id'],'problems':problems})
 for e in k['history']:
  counts['events']+=1;link={'node_id':n['node_id'],'node_name':n['node_name'],'kind':'event','event_id':e['id'],'event_type':e['event_type']};releases(e,link);se=e.get('security_evidence')
  if not se:counts['events_without_security_evidence']+=1;continue
  counts['events_with_security_evidence']+=1;releases(se['kernel'],dict(link,kind='event.security_evidence'));patches(se.get('livepatches'),se['kernel'],se.get('software_versions',[]),link)
def restricted(name,obj):
 fd=os.open(state/name,os.O_CREAT|os.O_TRUNC|os.O_WRONLY,0o600);os.fchmod(fd,0o600)
 with os.fdopen(fd,'w') as f:json.dump(obj,f,indent=2);f.write('\n')
restricted('livepatch-observations.json',{'snapshot_sha256':sha,'observations':observations})
restricted('mechanical-receipt-details.json',{'snapshot_sha256':sha,'release_flags':flags,'issues':issues})
index={'snapshot_sha256':sha,'counts':dict(counts),'distinct_tuple_count':len(tuples),'tuples':list(tuples.values()),'limits':'Mechanical extraction only; inactive/transition observations retained; no identity filling, acceptance, coverage or activation classification.'};(out/'livepatch-observed-tuples.json').write_text(json.dumps(index,indent=2)+'\n')
receipt={'snapshot_sha256':sha,'bytes':len(raw),'mode':oct(p.stat().st_mode&511),'schema':x['schema_version'],'collected_at':x['collected_at'],'elapsed_seconds':None,'elapsed_note':'unknown; prior zero placeholder is not elapsed duration','counts':dict(counts),'catalogs':catalogs,'freshness_history_issue_count':len(issues),'release_strings':dict(release_counts),'flagged_release_strings':sorted({f['release'] for f in flags}),'prerelease_observations':sum(f['prerelease'] for f in flags),'relevant_7_2_observations':sum(f['relevant_7_2'] for f in flags),'74753_prerelease_gate':'no observed7.2/prerelease; other numeric custom versions referred for exact source identity; no safe-state inference','distinct_livepatch_tuples':len(tuples),'limits':'Offline shape/catalog/timestamp inspection; collector EXIT0 supplies API revision-coherence provenance, not independently replayed. No API/recollection or security classification.'};(out/'snapshot-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k not in ['release_strings','catalogs']},indent=2))

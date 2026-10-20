import collections,hashlib,json,os,pathlib
P=pathlib.Path('assessment/implementer1');W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');review=json.load(open(P/'livepatch-coverage.json'));snap=review['snapshot_sha256'];assert hashlib.sha256((W/'.state/evidence.json').read_bytes()).hexdigest()==snap
private=[];public=[]
for row in review['rows']:
 if row['decision']!='source_content_accepted':continue
 c=row['cve'];old=json.load(open(W/'.state/implementer1-before-livepatch'/(c+'.json')));new=json.load(open(W/'advisories'/c/'evaluation.json'));before={str(r['node_id']):r for r in old['nodes']};after={str(r['node_id']):r for r in new['nodes']};assert set(before)==set(after)
 changes=[{'node_id':k,'before':before[k],'after':after[k]} for k in before if any(before[k].get(f)!=after[k].get(f) for f in ['state','reason','vulnerable_until','mitigated_since'])];private.append({'cve':c,'changes':changes});earlier=0;later=0
 for x in changes:
  a=x['before']['mitigated_since'];b=x['after']['mitigated_since']
  if isinstance(a,str) and isinstance(b,str):earlier+=b<a;later+=b>a
 public.append({'cve':c,'changed_node_count':len(changes),'earlier_mitigation_count':earlier,'later_mitigation_count':later,'state_counts':dict(collections.Counter(r['state'] for r in new['nodes']))})
path=W/'.state/implementer1-livepatch-evaluation-diff.json';path.write_text(json.dumps({'snapshot_sha256':snap,'rows':private},indent=2)+'\n');os.chmod(path,0o600)
(P/'livepatch-evaluation-diff.json').write_text(json.dumps({'snapshot_sha256':snap,'scope':'Counts only; exact node/date/state linkage restricted to ignored .state/implementer1-livepatch-evaluation-diff.json','rows':public},indent=2)+'\n')
print(json.dumps(public,indent=2))

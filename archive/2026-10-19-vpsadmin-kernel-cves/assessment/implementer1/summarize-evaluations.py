import collections,datetime,hashlib,json,pathlib
P=pathlib.Path('assessment/implementer1');W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');ids=json.load(open('assessment/packages.json'))['groups']['implementer1'];expected='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274';assert hashlib.sha256((W/'.state/evidence.json').read_bytes()).hexdigest()==expected
rows=[]
for c in ids:
 d=json.load(open(W/'advisories'/c/'evaluation.json'))
 # Result shape is checked before extracting conclusions; no raw linkage is copied here.
 nodes=d.get('nodes',d.get('results'))
 if isinstance(nodes,dict):nodes=list(nodes.values())
 if not isinstance(nodes,list):raise ValueError('unexpected result shape '+str(d.keys()))
 counts=collections.Counter(n.get('state') for n in nodes);reasons=collections.Counter(('missing_baseline' if 'baseline' in str(n.get('reason','')).lower() else 'missing_configuration' if 'configuration' in str(n.get('reason','')).lower() and n.get('state')=='unknown' else 'role_exclusion' if 'role' in str(n.get('reason','')).lower() and n.get('state')=='not_affected' else 'other_'+str(n.get('state'))) for n in nodes)
 row={'cve':c,'node_count':len(nodes),'states':dict(counts),'reason_groups':dict(reasons),'evaluation_sha256':hashlib.sha256((W/'advisories'/c/'evaluation.json').read_bytes()).hexdigest(),'collected_at':d.get('collected_at'),'completeness_counts':{k:v for k,v in (d.get('completeness') or {}).items() if isinstance(v,(int,bool))}};rows.append(row)
 print(c,dict(counts))
(P/'evaluation-summary.json').write_text(json.dumps({'schema':1,'snapshot_sha256':expected,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'provisional_livepatch_acceptance':True,'rows':rows},indent=2)+'\n')

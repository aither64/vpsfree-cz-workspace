import datetime,hashlib,json,os,pathlib,subprocess,sys
W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');P=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves/assessment/implementer1');ids=json.load(open(P.parent/'packages.json'))['groups']['implementer1'];expected='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
if sys.argv[1:]:
 assert set(sys.argv[1:]) <= set(ids)
 ids=sys.argv[1:]
assert hashlib.sha256((W/'.state/evidence.json').read_bytes()).hexdigest()==expected
out=W/'.state/implementer1-evaluate';out.mkdir(mode=0o700,exist_ok=True);os.chmod(out,0o700)
rows=[]
for c in ids:
 with (out/(c+'.log')).open('w') as f:
  os.chmod(out/(c+'.log'),0o600)
  r=subprocess.run(['bin/security-advisory','evaluate',c],cwd=W,stdout=f,stderr=subprocess.STDOUT)
 row={'cve':c,'exit_code':r.returncode};rows.append(row);print(c,'exit',r.returncode,flush=True)
 if r.returncode:break
assert hashlib.sha256((W/'.state/evidence.json').read_bytes()).hexdigest()==expected
(P/('evaluation-execution-livepatch.json' if sys.argv[1:] else 'evaluation-execution.json')).write_text(json.dumps({'schema':1,'snapshot_sha256':expected,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows},indent=2)+'\n')
if any(x['exit_code'] for x in rows):raise SystemExit(1)

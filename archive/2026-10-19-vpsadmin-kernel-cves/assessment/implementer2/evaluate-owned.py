import hashlib,json,os,subprocess
from pathlib import Path
S=Path(__file__).resolve().parents[2]
W=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories')
ids=json.loads((S/'assessment/packages.json').read_text())['groups']['implementer2']
e=W/'.state/evidence.json'; expected='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274';assert hashlib.sha256(e.read_bytes()).hexdigest()==expected
os.umask(0o077);out=W/'.state/implementer2';out.mkdir(exist_ok=True);results=[]
for c in ids:
 with (out/(c+'.stdout.json')).open('w')as stdout,(out/(c+'.stderr.txt')).open('w')as stderr:
  r=subprocess.run([str(W/'bin/security-advisory'),'evaluate',c],cwd=W,stdout=stdout,stderr=stderr)
 if r.returncode:results.append({'cve':c,'exit':r.returncode});continue
 d=json.loads((W/'advisories'/c/'evaluation.json').read_text());results.append({'cve':c,'exit':0,'schema_version':d['schema_version'],'states':d['completeness']['states'],'node_set_complete':d['completeness']['node_set_complete'],'resolution_complete':d['completeness']['resolution_complete'],'unknown_reasons':sorted({n['reason']for n in d['nodes']if n['state']=='unknown'}),'vulnerable_reasons':sorted({n['reason']for n in d['nodes']if n['state']=='vulnerable'})})
 assert hashlib.sha256(e.read_bytes()).hexdigest()==expected
summary={'evidence_sha256':expected,'evaluations':results}
(S/'assessment/implementer2/evaluation-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

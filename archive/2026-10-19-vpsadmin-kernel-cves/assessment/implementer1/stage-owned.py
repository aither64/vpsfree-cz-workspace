import json,pathlib,subprocess
P=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves/assessment/implementer1');W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');ids=json.load(open(P.parent/'packages.json'))['groups']['implementer1']
def git(*args):return subprocess.check_output(['git',*args],cwd=W).decode()
assert not git('diff','--cached','--name-only').strip(),'Shared index unexpectedly occupied'
assert git('rev-parse','HEAD').strip()=='69027fd51efc5c7eb0a4711947b4f9d08190940e'
allowed={'advisories/'+c+'/'+f for c in ids for f in ['analysis.md','advisory.yml','evaluation.json']}
for c in ids:assert {p.name for p in (W/'advisories'/c).iterdir()}=={'analysis.md','advisory.yml','evaluation.json'},c
assert max(map(len,(P/'commit-message.txt').read_text().splitlines()))<=80
subprocess.run(['git','add','--',*sorted(allowed)],cwd=W,check=True)
actual=set(git('diff','--cached','--name-only').splitlines());assert actual==allowed,(actual^allowed)
subprocess.run(['git','diff','--cached','--check'],cwd=W,check=True)
(P/'staged-inventory.json').write_text(json.dumps({'base_head':'69027fd51efc5c7eb0a4711947b4f9d08190940e','staged_path_count':len(actual),'cve_count':len(ids),'staged_paths':sorted(actual),'git_diff_check_exit':0,'message_max_columns':max(map(len,(P/'commit-message.txt').read_text().splitlines()))},indent=2)+'\n')
print('Staged exact60 owned paths (20CVEs x3); diff check PASS')

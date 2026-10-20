import pathlib,json,re
s=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');o=s/'assessment/implementer0';ids=json.loads((s/'assessment/packages.json').read_text())['groups']['implementer0'];out={}
def norm(v):return v+'.0' if len(v.split('.'))==2 else v
def vt(v):return tuple(int(n)for n in v.split('.'))
lts=['3.0','3.2','3.4','3.10','3.12','3.14','3.16','3.18','4.1','4.4','4.9','4.14','4.19','5.4','5.10','5.15','6.1','6.6','6.12','6.18']
for c in ids:
 r=json.loads((s/f'research/cve-evidence/records/{c}.json').read_text())['containers']['cna'];g=[v for a in r['affected']for v in a['versions']if v.get('versionType')=='git'];sv=[v for a in r['affected']for v in a['versions']if v.get('versionType')!='git'];fixes={};infos=[]
 for v in g:
  h=v['lessThan'];m=(o/f'primary/{h}.makefile').read_text();p=(o/f'primary/{h}.patch').read_text();branch='.'.join(re.search('^'+k+r'\s*=\s*(\S+)',m,re.M).group(1)for k in ['VERSION','PATCHLEVEL']);upstream=bool(re.search(r'(?i)(?:upstream commit|commit [0-9a-f]{40} upstream)',p));infos.append(dict(sha=h,branch=branch,introduced_commit=v['version'],is_backport=upstream))
  if upstream:fixes[branch]=v
 if c.endswith('74753'):intro='7.2.0-rc1';fixed='7.2.0'
 else:
  intro=norm(next(v['version'] for v in sv if v['status']=='affected'and'lessThan'not in v and'lessThanOrEqual'not in v));fixed=norm(next(v['version']for v in sv if v.get('versionType')=='original_commit_for_fix'))
 rules={};overrides={'.'.join(v['version'].split('.')[:2]):v for v in sv if v.get('versionType')=='semver'and v['status']=='affected'and'lessThan'in v}
 for v in sv:
  if v['status']=='unaffected'and v.get('lessThanOrEqual','').endswith('.*'):
   b='.'.join(v['version'].split('.')[:2]);gv=fixes[b];start=overrides.get(b,{}).get('version',max(norm(b),intro,key=vt)) if c.endswith('74753')==False else overrides[b]['version'];rules[b]=dict(affected_from=norm(start),fixed_in=norm(v['version']),introduced_commit=gv['version'],fixed_commit=gv['lessThan'])
 for b,v in overrides.items():
  if b not in rules:
   gv=fixes.get(b);rules[b]=dict(affected_from=norm(v['version']),fixed_in=norm(v['lessThan']),introduced_commit=gv['version'],fixed_commit=gv['lessThan'])
 if not c.endswith('74753'):
  for b in lts:
   if b not in rules and vt(norm(b))>=vt(intro)and vt(norm(b))<vt(fixed):rules[b]=dict(affected_from=norm(b),fixed_in=None,introduced_commit=g[0]['version'])
 out[c]=dict(affected_from=intro,fixed_from=fixed,rules=dict(sorted(rules.items(),key=lambda x:vt(x[0]))),primary_fixes=infos,mainline_fix=next(x['sha']for x in infos if not x['is_backport']))
(o/'version-inputs.json').write_text(json.dumps(out,indent=2)+'\n');print('versions written',len(out))

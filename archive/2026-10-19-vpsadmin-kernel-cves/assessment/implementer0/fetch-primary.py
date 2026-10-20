import concurrent.futures,datetime,hashlib,json,pathlib,urllib.request
s=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves')
o=s/'assessment/implementer0';d=o/'primary';d.mkdir(exist_ok=True)
ids=json.loads((s/'assessment/packages.json').read_text())['groups']['implementer0'];jobs=[]
for c in ids:
 r=json.loads((s/f'research/cve-evidence/records/{c}.json').read_text())['containers']['cna']
 for a in r['affected']:
  for v in a['versions']:
   if v.get('versionType')=='git' and v.get('lessThan'):
    sha=v['lessThan']
    for kind,u in [('patch',f'https://github.com/gregkh/linux/commit/{sha}.patch'),('makefile',f'https://raw.githubusercontent.com/gregkh/linux/{sha}/Makefile')]:jobs.append((c,sha,kind,u))
def one(job):
 c,sha,k,u=job;p=d/f'{sha}.{k}'
 try:
  b=p.read_bytes() if p.exists() else urllib.request.urlopen(u,timeout=18).read()
  p.write_bytes(b)
  return dict(cve=c,sha=sha,kind=k,url=u,path=str(p.relative_to(s)),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
 except Exception as e:return dict(cve=c,sha=sha,kind=k,url=u,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 rows=list(ex.map(one,jobs))
(o/'primary-http-manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
print('retrieved',sum('error' not in x for x in rows),'of',len(rows),'objects');print([x for x in rows if 'error'in x])

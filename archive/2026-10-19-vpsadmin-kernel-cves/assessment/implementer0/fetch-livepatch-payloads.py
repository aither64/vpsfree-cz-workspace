import concurrent.futures,datetime,hashlib,json,pathlib,urllib.request
s=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');o=s/'assessment/implementer0';idx=json.loads((s/'assessment/implementer3/livepatch-observed-tuples.json').read_text());revs=sorted({x['revision']for t in idx['tuples']for x in t['identity']['vpsadminos']if x.get('revision')and x.get('revision_dirty')is False});jobs=[]
for rev in revs:
 jobs.append((rev,'os/packages/linux/available-kernels.nix'))
 p=o/'livepatch-source'/rev/'os/livepatches/available-patches.nix';txt=p.read_text()
 if 'bp-6.12.95-cumulative'in txt:
  jobs.append((rev,'os/livepatches/bp-6.12.95-cumulative.patch'))
  if 'bp-6.12.95-uname'in txt:jobs.append((rev,'os/livepatches/bp-6.12.95-uname.patch'))
def f(j):
 rev,p=j;u=f'https://raw.githubusercontent.com/vpsfreecz/vpsadminos/{rev}/{p}';q=o/'livepatch-source'/rev/p;q.parent.mkdir(parents=True,exist_ok=True)
 try:
  b=q.read_bytes()if q.exists()else urllib.request.urlopen(u,timeout=20).read();q.write_bytes(b);return dict(repository='vpsadminos',revision=rev,path=p,url=u,file=str(q.relative_to(s)),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
 except Exception as e:return dict(repository='vpsadminos',revision=rev,path=p,url=u,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as ex:rows=list(ex.map(f,jobs))
p=o/'livepatch-source-manifest.json';allrows=json.loads(p.read_text())+rows;p.write_text(json.dumps(allrows,indent=2)+'\n');print('payloads',sum('error'not in x for x in rows),'/',len(rows));print([x for x in rows if 'error'in x])

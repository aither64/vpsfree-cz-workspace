import datetime,gzip,hashlib,json,os,pathlib,stat,sys
os.umask(0o077);T=pathlib.Path(__file__).resolve().parent
parents=[pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-'+n) for n in ['working4','working5']]
rows=[];before=os.statvfs('/nix/store');free_before=before.f_bavail*before.f_frsize
for root in parents:
 for p in sorted(root.glob('*/measurements.jsonl')):
  result=p.parent/'result.json'
  if not result.is_file():continue
  v=json.loads(result.read_text())
  if v.get('complete') is not True or not v.get('finished_at'):continue
  expected=v.get('evidence_sha256',{}).get('measurements.jsonl')
  if not expected:continue
  st=p.lstat()
  assert stat.S_ISREG(st.st_mode) and st.st_uid==os.getuid() and stat.S_IMODE(st.st_mode)==0o600
  h=hashlib.sha256();count=0;out=p.with_name('measurements.jsonl.gz')
  with p.open('rb') as source,out.open('xb') as raw:
   with gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=6,mtime=0) as packed:
    while data:=source.read(1024*1024):h.update(data);count+=len(data);packed.write(data)
   raw.flush();os.fsync(raw.fileno())
  assert h.hexdigest()==expected and count==st.st_size
  verified=hashlib.sha256();verified_size=0
  with gzip.open(out,'rb') as source:
   while data:=source.read(1024*1024):verified.update(data);verified_size+=len(data)
  assert verified.hexdigest()==expected and verified_size==count
  latest=p.lstat();assert (latest.st_dev,latest.st_ino,latest.st_size,latest.st_mtime_ns)==(st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns)
  transport={'schema':1,'original_name':p.name,'original_sha256':expected,'original_size':count,'gzip_name':out.name,'gzip_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'gzip_size':out.stat().st_size,'original_receipt_unchanged':True,'retention':'gzip decompresses to original exact native bytes; no receipt/body/state/schema conversion'}
  m=p.parent/'measurements-retention.json';assert not m.exists();m.write_text(json.dumps(transport,indent=2)+'\n')
  assert p.lstat().st_ino==st.st_ino
  p.unlink()
  rows.append({'context':str(p.parent),'original_sha256':expected,'original_bytes':count,'original_allocated_bytes':st.st_blocks*512,'gzip_bytes':out.stat().st_size,'gzip_allocated_bytes':out.stat().st_blocks*512,'retention_manifest_sha256':hashlib.sha256(m.read_bytes()).hexdigest()})
after=os.statvfs('/nix/store')
value={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete':True,'scope':'Lossless compression only of own completed private wrapper measurement logs; exact original bytes verified through decompression before unlink, private native receipts remain byte-identical. No backup/campaign/config/credential/guest/store deletion.','files':rows,'original_bytes':sum(x['original_bytes'] for x in rows),'compressed_bytes':sum(x['gzip_bytes'] for x in rows),'free_bytes_before':free_before,'free_bytes_after':after.f_bavail*after.f_frsize,'limits':'Transport changes only; historical evidence is read through explicit adjacent retention manifest. Free delta includes other host activity; no guessed admission credit.'}
o=T/'finish-working-delivery-compress-completed-observations5.json';assert not o.exists();o.write_text(json.dumps(value,indent=2)+'\n')
print(json.dumps({'complete':True,'files':len(rows),'original_bytes':value['original_bytes'],'compressed_bytes':value['compressed_bytes'],'free_bytes_before':free_before,'free_bytes_after':value['free_bytes_after']}),flush=True)

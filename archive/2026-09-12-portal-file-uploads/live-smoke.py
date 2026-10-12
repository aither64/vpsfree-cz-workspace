#!/usr/bin/env python3
"""Authenticated smoke check; credentials stay in process memory."""
import base64,hashlib,json,ssl,urllib.error,urllib.request,uuid
from pathlib import Path

base='https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
context=ssl.create_default_context(cafile='/var/lib/dev-workspaces/public/ca.pem')
password=Path('/var/lib/dev-workspaces/password/password').read_bytes().strip()
authorization='Basic '+base64.b64encode(b'aither:'+password).decode()

def call(method,path,body=None,headers=None,authenticated=True):
 values={'Origin':base,**(headers or {})}
 if authenticated:values['Authorization']=authorization
 request=urllib.request.Request(base+path,body,values,method=method)
 try:
  with urllib.request.urlopen(request,context=context,timeout=30) as response:return response.status,response.read(),response.headers
 except urllib.error.HTTPError as response:return response.code,response.read(),response.headers

status,_,_=call('GET','/healthz',authenticated=False)
assert status==401,('unauthenticated',status)
status,body,_=call('GET','/healthz')
assert status==200,('health',status)
print('PASS authenticated HTTPS health; unauthenticated access denied',flush=True)
if __import__('os').environ.get('UPLOAD_SMOKE_MUTATE')=='1':
 status,body,_=call('POST','/api/upload-drafts',b'{}',{'Content-Type':'application/json'})
 assert status==201,('draft',status)
 scope=json.loads(body);payload=b'Portal file upload deployment check.\n'+b'x'*(8<<20)
 status,body,_=call('POST',scope['url'],json.dumps({'clientId':str(uuid.uuid4()),'name':'deployment-check.txt','size':len(payload)}).encode(),{'Content-Type':'application/json'})
 assert status==201,('create',status)
 file=json.loads(body);path=scope['url']+'/'+file['id']
 try:
  for offset in range(0,len(payload),4<<20):
   chunk=payload[offset:offset+(4<<20)]
   status,_,_=call('PATCH',path,chunk,{'Upload-Offset':str(offset),'Upload-Checksum':hashlib.sha256(chunk).hexdigest(),'Content-Type':'application/octet-stream'})
   assert status==200,('chunk',offset,status)
  status,_,_=call('POST',path,b'')
  assert status==200,('complete',status)
  status,content,headers=call('GET',path+'/content')
  assert status==200 and content==payload
  assert headers['Content-Type']=='application/octet-stream' and headers['Content-Disposition'].startswith('attachment;')
  print('PASS live 8 MiB upload in three chunks, checksums, completion and exact download through nginx',flush=True)
 finally:
  status,_,_=call('DELETE',path)
  assert status==200,('delete',status)
  status,_,_=call('GET',path+'/content')
  assert status==404,('removed content',status)
 print('PASS live draft removal',flush=True)

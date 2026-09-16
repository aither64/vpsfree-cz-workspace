#!/usr/bin/env python3
"""Authenticated checks with synthetic files; credentials remain in memory."""
import base64,hashlib,json,ssl,urllib.error,urllib.request,uuid
from email.message import Message
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
  with urllib.request.urlopen(request,context=context,timeout=30) as r:return r.status,r.read(),r.headers
 except urllib.error.HTTPError as r:return r.code,r.read(),r.headers

def create(scope,name,size,client=None):
 return call('POST',scope['url'],json.dumps({'clientId':client or str(uuid.uuid4()),'name':name,'size':size}).encode(),{'Content-Type':'application/json'})

assert call('GET','/healthz',authenticated=False)[0]==401
assert call('GET','/healthz')[0]==200
assert call('GET','/2026-09-16-portal-upload-recovery/')[0]==200
print('PASS authenticated HTTPS health and initiative page; unauthenticated access denied',flush=True)
for path,marker in [('/static/app.js','conversation.js?v=9'),('/codex/assets/conversation.js?v=9','uploads.js?v=3'),('/codex/assets/uploads.js?v=3','entry.creation = "unknown"')]:
 status,body,_=call('GET',path)
 assert status==200 and marker in body.decode(),path
print('PASS deployed cache-version chain and recovery assets',flush=True)
status,body,_=call('POST','/api/upload-drafts',b'{}',{'Content-Type':'application/json'})
assert status==201,('draft',status)
scope=json.loads(body)
for name in ['bad\nsubject.eml','bad\tname.eml','bad\u0085name.eml']:
 status,body,_=create(scope,name,1)
 assert status==400 and 'control characters' in json.loads(body)['error'],(status,body)
print('PASS distinct control-character rejection',flush=True)
names=["Mail ' OR 1=1; <img onerror=alert(1)> žluťoučký.eml",'backslash\\quote"subject.eml','../../path-like.eml']
for name in names:
 payload=b'Synthetic upload recovery deployment check.\n'
 client=str(uuid.uuid4());status,body,_=create(scope,name,len(payload),client)
 assert status==201,('create',status,body)
 file=json.loads(body);path=scope['url']+'/'+file['id']
 try:
  assert file['name']==name
  status,body,_=create(scope,name,len(payload),client)
  assert status==201 and json.loads(body)['id']==file['id']
  status,_,_=call('PATCH',path,payload,{'Upload-Offset':'0','Upload-Checksum':hashlib.sha256(payload).hexdigest(),'Content-Type':'application/octet-stream'})
  assert status==200,('chunk',status)
  assert call('POST',path,b'')[0]==200
  status,content,headers=call('GET',path+'/content')
  assert status==200 and content==payload
  assert headers['Content-Type']=='application/octet-stream' and headers['X-Content-Type-Options']=='nosniff'
  message=Message();message['Content-Disposition']=headers['Content-Disposition']
  assert message.get_content_disposition()=='attachment' and message.get_filename()==name
 finally:
  assert call('DELETE',path)[0]==200
  assert call('GET',path+'/content')[0]==404
 status,body,_=call('GET',scope['url']);assert status==200
 assert all(x['id']!=file['id'] or x['state']=='deleted' for x in json.loads(body)['files'])
 print('PASS special filename, idempotent create, bytes, MIME round trip and removal',flush=True)
print('PASS live verification; all synthetic files removed',flush=True)

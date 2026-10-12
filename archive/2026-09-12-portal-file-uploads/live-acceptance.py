#!/usr/bin/env python3
"""Post-review real Codex acceptance in private metadata/workspace fixtures."""
import hashlib,http.client,importlib.util,json,os,pty,select,signal,subprocess,tempfile,time,uuid
from pathlib import Path

root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('upload_fixture',root/'live-fixture.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
package=Path(os.environ['ACCEPT_PACKAGE']).resolve(strict=True)
previous=Path(os.environ['ACCEPT_PREVIOUS']).resolve(strict=True)
codex=package/'libexec/codex/bin/codex'
fixture=None;server=None;results=[]
private_home=tempfile.TemporaryDirectory(prefix="upload-codex-",dir="/tmp")
def record(name,**details):results.append({'check':name,**details});print('PASS '+name,flush=True)
def raw(method,path,body=b'',headers=None):
 connection=module.UnixHTTP(fixture.root/'portal.sock',timeout=30)
 values={'Origin':fixture.base,**(headers or {})}
 connection.request(method,path,body,values)
 response=connection.getresponse();data=response.read();status=response.status;connection.close()
 if status>=400:raise AssertionError(f'{method} {path}: {status} {data.decode()}')
 return status,json.loads(data or b'{}')
def lifecycle(action,slug):
 master,slave=pty.openpty()
 process=subprocess.Popen([*fixture.cli(package),action,slug,'--as-is'],stdin=slave,stdout=slave,stderr=slave,cwd=fixture.workspace,env=fixture.environment,start_new_session=True)
 os.close(slave);output=b'';answered=False;deadline=time.monotonic()+120
 try:
  while process.poll() is None:
   if time.monotonic()>deadline:process.kill();raise TimeoutError(action)
   if select.select([master],[],[],.2)[0]:
    try:chunk=os.read(master,65536)
    except OSError:break
    output+=chunk
    if b'[y/N]' in output and not answered:os.write(master,b'y\n');answered=True
  process.wait(timeout=10)
  while select.select([master],[],[],0)[0]:
   try:chunk=os.read(master,65536)
   except OSError:break
   if not chunk:break
   output+=chunk
 finally:os.close(master)
 (fixture.root/(action+'-'+slug+'.log')).write_bytes(output)
 assert process.returncode==0, f'{action} failed; see owned fixture log'

def upload(url,name,content):
 _,entry=raw('POST',url,json.dumps({'clientId':str(uuid.uuid4()),'name':name,'size':len(content)}).encode(),{'Content-Type':'application/json'})
 if content:raw('PATCH',url+'/'+entry['id'],content,{'Upload-Offset':'0','Upload-Checksum':hashlib.sha256(content).hexdigest(),'Content-Type':'application/octet-stream'})
 raw('POST',url+'/'+entry['id'])
 return entry
try:
 private=private_home.name
 home=Path(private)/'metadata';home.mkdir(mode=0o700)
 for name in ['auth.json','config.toml']:
  source=Path.home()/'.codex'/name
  if source.exists():(home/name).symlink_to(source)
 socket=Path(private)/'app.sock'
 environment=os.environ.copy();environment['CODEX_HOME']=str(home)
 log=open(Path(private)/'app-server.log','ab')
 server=subprocess.Popen([str(codex),'app-server','--listen','unix://'+str(socket)],env=environment,stdout=log,stderr=log,start_new_session=True);log.close()
 module.until(lambda: socket.is_socket() or (server.poll() is not None and (_ for _ in ()).throw(RuntimeError('isolated App Server stopped'))),seconds=30,interval=.1,label='private App Server')
 os.environ['ACCEPT_CODEX_SOCKET']=str(socket);os.environ['CODEX_HOME']=str(home)
 fixture=module.Fixture();fixture.prepare()
 fixture.command(['git','init','--bare',fixture.root/'origin.git'],'origin-init')
 fixture.command(['git','remote','add','origin',fixture.root/'origin.git'],'origin-add')
 fixture.command(['git','push','-u','origin','master'],'origin-push')
 (fixture.workspace/'AGENTS.md').write_text('This is a disposable upload acceptance fixture. Read only files attached to the explicit request. Do not change files, use network services, delegate, or run session lifecycle commands. Return the requested file content and keep the session open.\n')
 _,scope=raw('POST','/api/upload-drafts',b'{}',{'Content-Type':'application/json'})
 token='UPLOAD_ACCEPTED_'+uuid.uuid4().hex
 entry=upload(scope['url'],'token.txt',(token+'\n').encode())
 source,fork=fixture.slugs
 goal='Read the attached file with one shell command. Reply with exactly its contents, then stop. Do not change files or run session lifecycle commands.'
 status,body,headers,_=fixture.http('/sessions',{'name':fixture.names[0],'creation_date':fixture.date,'goal':goal,'uploadScope':scope['id'],'attachmentIds':entry['id']},form=True)
 assert status==303,(status,body)
 fixture.ready(source);transcript=fixture.idle(source)
 if not any(e.get('kind')=='agentMessage' and token in e.get('text','') for e in transcript['entries']):
  (fixture.root/'initial-transcript.json').write_text(json.dumps(transcript,indent=2))
  pane=subprocess.run([fixture.tmux,'-S',str(fixture.root/'tmux.sock'),'capture-pane','-p','-t',source],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  (fixture.root/'native-pane.txt').write_bytes(pane.stdout+pane.stderr)
  assert any(e.get('turnStatus')=='interrupted' for e in transcript['entries']), 'initial turn failed for an unexpected reason'
  record('initial native handoff interrupted; continuing the exact same thread')
  status,body,_,_=fixture.http('/api/sessions/'+source+'/message',{'message':goal,'attachmentIds':[entry['id']],'clientUserMessageId':str(uuid.uuid4())})
  assert status==202,(status,body)
  transcript=fixture.idle(source)
 assert any(e.get('kind')=='agentMessage' and token in e.get('text','') for e in transcript['entries']),transcript
 user=[e for e in transcript['entries'] if e.get('kind')=='userMessage']
 assert user and user[0]['attachments'][0]['id']==entry['id'] and user[0]['displayText']==goal
 wire=user[0]['text'];path=json.loads(wire.split('outside version control):\n',1)[1])[0]['path']
 assert Path(path).read_text()==token+'\n'
 assert not str(Path(path)).startswith(str(fixture.workspace)+'/')
 record('real prompt reads private uploaded file bound at session creation',codexVersion=fixture.version)
 # Rollback ignores upload state but retains readable bytes and the wire prompt.
 fixture.stop();fixture.start(previous)
 assert Path(path).read_text()==token+'\n'
 old=fixture.transcript(source)
 assert any(e.get('text')==wire for e in old['entries'])
 fixture.stop();fixture.start(package)
 recovered=fixture.transcript(source)
 assert any(e.get('attachments',[{}])[0].get('id')==entry['id'] for e in recovered['entries'] if e.get('attachments'))
 record('package rollback retains bytes and rollforward restores attachment metadata')
 status,body,_,_=fixture.http('/api/sessions/'+source+'/fork',{'name':fixture.names[1],'creationDate':fixture.date,'model':fixture.defaults['model'],'reasoningEffort':fixture.defaults['reasoningEffort']})
 assert status==202,(status,body)
 fixture.ready(fork)
 inherited=fixture.transcript(fork)
 assert any(e.get('attachments',[{}])[0].get('id')==entry['id'] for e in inherited['entries'] if e.get('attachments'))
 record('real fork retains the original attachment without copying bytes')
 fork_attempt=str(uuid.uuid4())
 status,body,_,_=fixture.http('/api/sessions/'+fork+'/message',{'message':'Read the attached file with one shell command and reply with its contents. Do not change files.','attachmentIds':[entry['id']],'clientUserMessageId':fork_attempt})
 assert status==202,(status,body)
 inherited=fixture.idle(fork)
 assert any(e.get('clientUserMessageId')==fork_attempt for e in inherited['entries'])
 assert token in inherited['entries'][-1].get('text',''),inherited
 record('fork reads the shared file in its own completed turn')
 # The fixture has no project branches. Archive/revive must retain shared input.
 fixture.command(['git','add','AGENTS.md','work'],'active-tracking-stage')
 fixture.command(['git','commit','-m','Record active upload acceptance sessions'],'active-tracking-commit')
 tracking=fixture.workspace/'work'/source/'state.md'
 tracking.write_text(tracking.read_text().replace('lifecycle: active','lifecycle: complete',1))
 fixture.command(['git','add','work'],'tracking-stage')
 fixture.command(['git','commit','-m','Record completed upload acceptance sessions'],'tracking-commit')
 lifecycle('archive',source)
 assert Path(path).read_text()==token+'\n'
 archived=fixture.transcript(source)
 assert any(e.get('attachments',[{}])[0].get('id')==entry['id'] for e in archived['entries'] if e.get('attachments'))
 lifecycle('revive',source)
 fixture.ready(source);fixture.idle(source)
 assert Path(path).read_text()==token+'\n'
 record('archive and revive retain the original input and conversation')
 # Both conversations are idle; deletion reports both references and removes bytes.
 _,listing=raw('GET','/uploads/s-'+source)
 item=next(item for item in listing['files'] if item['id']==entry['id'])
 assert sorted(item['references'])==sorted([source,fork]),item
 raw('DELETE','/uploads/s-'+source+'/'+entry['id']+'?confirmed=true')
 assert not Path(path).exists()
 inherited=fixture.transcript(fork)
 assert any(e.get('attachments',[{}])[0].get('state')=='deleted' for e in inherited['entries'] if e.get('attachments'))
 record('confirmed sent deletion affects both real fork references')
 extra=upload('/uploads/s-'+source,'remove-with-session.txt',b'owned session input')
 _,extra_content=raw('GET','/uploads/s-'+source+'/'+extra['id'])
 # Inspect only this fixture's private upload catalog to prove unlinking, without
 # deriving the storage namespace in the lifecycle caller.
 catalogs=list((fixture.root/'state'/'portal').glob('*/uploads/catalog.json'))
 assert len(catalogs)==1
 file_dirs=list((catalogs[0].parent/'files'/extra['id']).iterdir())
 assert len(file_dirs)==1
 extra_path=file_dirs[0]
 lifecycle('delete',source)
 assert not extra_path.exists()
 assert not (fixture.workspace/'worktrees'/'.locks'/(source+'.delete.json')).exists()
 record('real session deletion completes owner cleanup before journal finalization')
 lifecycle('delete',fork)
finally:
 if fixture:
  fixture.close()
  subprocess.run([fixture.tmux,'-S',str(fixture.root/'tmux.sock'),'kill-server'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 if server:
  server.terminate()
  try:server.wait(timeout=10)
  except subprocess.TimeoutExpired:os.killpg(server.pid,signal.SIGKILL);server.wait()
 private_home.cleanup()
 (root/'live-results.json').write_text(json.dumps({'checks':results},indent=2)+'\n')

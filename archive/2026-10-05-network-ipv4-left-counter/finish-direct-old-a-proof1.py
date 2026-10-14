import datetime,hashlib,json,os,pathlib,stat
ROOT=pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g4/campaign/state-a')
RUN='a6b66057-6117-4e46-89e3-faf53bd7e139';INSTANCE='c3e220f5-d7ba-4e5c-bee1-8149d1c40bbd'
def record(path):
 for parent in path.parents:
  s=parent.lstat();assert stat.S_ISDIR(s.st_mode)
 s=path.lstat();assert stat.S_ISREG(s.st_mode) and s.st_uid==os.getuid() and stat.S_IMODE(s.st_mode)==0o600 and s.st_size<=2097152
 fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW)
 try:
  v=os.fstat(fd);assert stat.S_ISREG(v.st_mode) and v.st_uid==os.getuid() and stat.S_IMODE(v.st_mode)==0o600 and v.st_size<=2097152;assert (s.st_dev,s.st_ino)==(v.st_dev,v.st_ino)
  b=os.read(fd,2097153);assert len(b)<=2097152;return json.loads(b),hashlib.sha256(b).hexdigest()
 finally:os.close(fd)
def current(x):
 p=pathlib.Path('/proc')/str(x['pid'])
 try:
  v=(p/'stat').read_text().rsplit(') ',1)[1].split()
  if v[0]=='Z':return None
  return dict(pid=x['pid'],start_ticks=int(v[19]),boot_id=pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip(),owner_uid=p.stat().st_uid,executable=os.readlink(p/'exe'),argv=(p/'cmdline').read_bytes().decode().rstrip('\0').split('\0'))
 except FileNotFoundError:return None
def prove():
 d=ROOT/'clusters/same-slug'
 for p in [ROOT,ROOT/'clusters',d]:
  s=p.lstat();assert stat.S_ISDIR(s.st_mode) and s.st_uid==os.getuid() and stat.S_IMODE(s.st_mode)==0o700
 identity,ih=record(d/'identity.json');phase,ph=record(d/'phase.json');launch,lh=record(d/f'launch-{RUN}.json');reservation,rh=record(d/f'reservation-{RUN}.json');processes,xh=record(d/f'processes-{RUN}.json');artifact,ah=record(d/f'artifact-{launch["artifact_id"]}.json')
 assert identity['instance_id']==INSTANCE and identity['state_root']==str(ROOT) and identity['owner_uid']==os.getuid() and identity['schema']==2
 assert phase==dict(schema=1,phase='starting',run_id=RUN) and launch==reservation
 for x in (launch,processes):assert x['instance_id']==INSTANCE and x['run_id']==RUN and x['artifact_id']==launch['artifact_id'] and x['artifact_sha256']==ah
 r=processes['runner'];assert current(r)==r and r['boot_id']==launch['boot_id'] and r['owner_uid']==os.getuid();expected=launch['runner_identity'];assert r['executable']==os.path.realpath(expected['executable']) and expected['entrypoint'] in r['argv']
 for opt,key in {'--config':'config_path','--state-dir':'state_dir','--sock-dir':'socket_dir','--run-id':'run_id','--instance-id':'instance_id','--artifact-id':'artifact_id','--artifact-sha256':'artifact_sha256'}.items():assert [opt,launch[key]] in [r['argv'][i:i+2] for i in range(len(r['argv'])-1)]
 sock=pathlib.Path(launch['socket_dir'])/'control.sock';s=sock.lstat();assert stat.S_ISSOCK(s.st_mode) and s.st_uid==os.getuid()
 children=[]
 for x in processes['children']:
  y=current(x);matches=y==x;gone=y is None or y['start_ticks']!=x['start_ticks'];assert matches or gone;children.append(dict(pid=x['pid'],matches=matches,gone=gone))
 return dict(schema=1,at=datetime.datetime.now(datetime.timezone.utc).isoformat(),generator='ab09bd437b310f57e4ff2453ec0432555d85eaca',instance_id=INSTANCE,run_id=RUN,artifact_id=launch['artifact_id'],runner_pid=r['pid'],runner_current_exact_tuple_match=True,runner_argv_sha256=hashlib.sha256(json.dumps(r['argv']).encode()).hexdigest(),control_socket_owned=True,children=children,complete=processes['complete'],records=dict(identity=ih,phase=ph,launch=lh,reservation=rh,artifact=ah,processes=xh),scope='Read-only recorded tuple observation; public stop repeats live/control authority.')
if __name__=='__main__':
 out=prove();p=pathlib.Path(__file__).with_name('finish-direct-old-a-authority1.json')
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out))

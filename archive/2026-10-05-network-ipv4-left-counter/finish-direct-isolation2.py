#!/usr/bin/env python3
import datetime,hashlib,json,os,pathlib,signal,subprocess,sys,time
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
PREFIX=T/'finish-direct-isolation2'; a=json.loads((T/'finish-direct-package-realize2-acceptance.json').read_text()); c=json.loads((T/'finish-direct-private-configs2.json').read_text()); cap=json.loads((T/'finish-direct-capacity-isolation2.json').read_text())
assert a['accepted'] and a['generator']=='7dc4d70830e535f4559bccfa668cf65cdce1de2d'
assert hashlib.sha256(pathlib.Path(cap['private_receipt_path']).read_bytes()).hexdigest()==cap['sha256']
private=pathlib.Path(c['private_parent']); assert pathlib.Path(c['campaign_root'],'receipts/installed-layout.json').is_file(); assert not pathlib.Path(c['campaign_root'],'receipts/isolation-continuity-update-attempt.json').exists()
env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ};env['PATH']=a['selection']['path'];env['LANG']='C.UTF-8'
argv=[a['package']+'/bin/vpsfree-kb-verify','--root',c['campaign_root'],'--config-a',c['configurations'][0]['path'],'--config-b',c['configurations'][1]['path'],'--predecessor-ref','github:vpsfreecz/vpsfree-kb-contracts/68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e','--capacity-receipt',cap['private_receipt_path'],'--phase','isolation-continuity-update']
record={'schema':1,'generator':a['generator'],'phase':'isolation-continuity-update','argv':argv,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Targeted real public-command two-cluster start, predecessor resume, live changed-source update, final isolation/reset/resume and capture-lease exclusion/loss. Preview and foreign state untouched; no CI or media capture.'}
child=None;cancel=None
signal.signal(signal.SIGTERM,lambda *args: (_ for _ in ()).throw(KeyboardInterrupt()))
with (private/'isolation2.stdout').open('xb') as out,(private/'isolation2.stderr').open('xb') as err,(private/'isolation2.measurements.jsonl').open('x') as measurements:
 child=subprocess.Popen(argv,cwd='/home/aither',env=env,stdout=out,stderr=err,close_fds=True);record['pid']=child.pid;record['wrapper_pid']=os.getpid();record['boot_id']=pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip();record['start_ticks']=int(pathlib.Path('/proc/'+str(child.pid)+'/stat').read_text().rsplit(')',1)[1].split()[19])
 with pathlib.Path(str(PREFIX)+'.started.json').open('x') as f:json.dump(record,f,indent=2)
 try:
  while child.poll() is None:
   fs=os.statvfs('/nix/store');free=fs.f_bavail*fs.f_frsize;ram=int(next(x for x in pathlib.Path('/proc/meminfo').read_text().splitlines() if x.startswith('MemAvailable:')).split()[1])*1024;shm=os.statvfs('/dev/shm');shm_free=shm.f_bavail*shm.f_frsize; measurements.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'available_bytes':free,'ram_available_bytes':ram,'shm_available_bytes':shm_free})+'\n');measurements.flush()
   if free<32*1024**3:cancel='host plus retained G4 sparse-growth reserve lost';break
   if ram<8*1024**3 or shm_free<2*1024**3:cancel='host RAM/shared-memory safety headroom lost';break
   expected={'node1':'/nix/store/mad7zijkfkvvmp58512idxgjn5ar2mv4-linux-6.12.95/bzImage','services':'/nix/store/zfi3x0y2ci656yw3xznsin34vag44g6s-linux-6.12.107/bzImage'}
   for cfg in pathlib.Path(c['campaign_root']).glob('state-*/clusters/same-slug/result-config-*'):
    if cfg.is_symlink() and str(cfg.resolve()).startswith('/nix/store/') and cfg.is_file():
     actual=json.loads(cfg.read_text())['machines']
     if {key:value['kernel'] for key,value in actual.items()}!=expected:cancel='actual prepared kernel differs from pre-realized plan';break
   if cancel:break
   time.sleep(1)
 except BaseException as interruption:cancel='wrapper interruption '+type(interruption).__name__
 finally:
  if cancel and child.poll() is None:
   child.terminate()
   try:child.wait(timeout=15)
   except subprocess.TimeoutExpired:child.kill();child.wait()
  child.wait()
record.update(exit_code=child.returncode,cancel_reason=cancel,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),daemon_or_detached_cleanup_certified=False)
record['private_evidence']={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [private/'isolation2.stdout',private/'isolation2.stderr',private/'isolation2.measurements.jsonl']}
with pathlib.Path(str(PREFIX)+'.json').open('x') as out:json.dump(record,out,indent=2);out.write('\n')
with pathlib.Path(str(PREFIX)+'.exit').open('x') as out:out.write(str(child.returncode)+'\n')
print(json.dumps({'phase':record['phase'],'exit_code':child.returncode,'cancel_reason':cancel,'receipt':str(PREFIX)+'.json'}));sys.exit(child.returncode)

#!/usr/bin/env python3
import datetime,hashlib,json,os,pathlib,signal,subprocess,sys,time
TRACKING=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
PREFIX=TRACKING/'finish-direct-package-realize5'
G='922e71e5eb75b6eb416bf55e39160e9a7236e654'
NIX='/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix'
gate=json.loads((TRACKING/'finish-stop-waiter-step9-acceptance.json').read_text());assert gate['generator']==G and gate['construction_may_proceed'] is True
assessment=json.loads((TRACKING/'finish-direct-package-realize5-assessment.json').read_text());assert assessment['generator']==G
private=pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification')
if private.exists():
 st=private.lstat();assert not private.is_symlink() and private.is_dir() and st.st_uid==os.getuid() and st.st_mode&0o777==0o700
else:private.mkdir(mode=0o700)
link=private/'2026-10-05-network-ipv4-left-counter-g12-package'
assert not os.path.lexists(link)
env={k:os.environ[k] for k in ('HOME','USER','LOGNAME','XDG_RUNTIME_DIR') if k in os.environ}
env['PATH']=str(pathlib.Path(NIX).parent)+':/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin:/run/current-system/sw/bin'
env['NIX_CONFIG']='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 4\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n'
argv=[NIX,'build','--no-write-lock-file','--json','--out-link',str(link),'github:vpsfreecz/vpsfree-kb-contracts/'+G+'#runtime-verify']
record={'schema':1,'generator':G,'argv':argv,'gc_root':str(link),'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Targeted immutable verifier package preparation; no source check/CI/guest operation.'}
child=None;cancel=None
def interrupted(signum,frame):
 global cancel
 cancel='wrapper signal '+str(signum)
signal.signal(signal.SIGTERM,interrupted)
signal.signal(signal.SIGINT,interrupted)
with pathlib.Path(str(PREFIX)+'.stdout').open('xb') as out,pathlib.Path(str(PREFIX)+'.stderr').open('xb') as err,pathlib.Path(str(PREFIX)+'.measurements.jsonl').open('x') as measurements:
 child=subprocess.Popen(argv,cwd='/home/aither',env=env,stdout=out,stderr=err,close_fds=True);record['pid']=child.pid
 record['wrapper_pid']=os.getpid()
 record['boot_id']=pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip()
 record['child_start_ticks']=int(pathlib.Path('/proc/'+str(child.pid)+'/stat').read_text().rsplit(')',1)[1].split()[19])
 with pathlib.Path(str(PREFIX)+'.started.json').open('x') as started:json.dump(record,started,indent=2)
 try:
  while child.poll() is None:
   fs=os.statvfs('/nix/store');available=fs.f_bavail*fs.f_frsize
   mem=int(next(x for x in pathlib.Path('/proc/meminfo').read_text().splitlines() if x.startswith('MemAvailable:')).split()[1])*1024
   measurements.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'store_available_bytes':available,'ram_available_bytes':mem})+'\n');measurements.flush()
   if cancel:break
   if available<assessment['reserve_bytes']:cancel='host filesystem reserve lost';break
   time.sleep(1)
 except BaseException as interruption:
  cancel='wrapper interrupted: '+type(interruption).__name__
 finally:
  if cancel and child.poll() is None:
   child.terminate()
   try:child.wait(timeout=10)
   except subprocess.TimeoutExpired:child.kill();child.wait()
  if child.poll() is None:child.wait()
record['exit_code']=child.returncode;record['cancel_reason']=cancel;record['daemon_or_detached_cleanup_certified']=False
record['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['evidence']={str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in [pathlib.Path(str(PREFIX)+'.stdout'),pathlib.Path(str(PREFIX)+'.stderr'),pathlib.Path(str(PREFIX)+'.measurements.jsonl')]}
with pathlib.Path(str(PREFIX)+'.json').open('x') as out:json.dump(record,out,indent=2);out.write('\n')
with pathlib.Path(str(PREFIX)+'.exit').open('x') as out:out.write(str(child.returncode)+'\n')
print(json.dumps({'exit_code':child.returncode,'cancel_reason':cancel,'gc_root':str(link)}));sys.exit(child.returncode)

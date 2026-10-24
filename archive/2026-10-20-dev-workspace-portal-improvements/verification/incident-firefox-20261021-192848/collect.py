#!/usr/bin/env python3
import datetime,fcntl,hashlib,json,os,pathlib,shlex,subprocess,sys,time
p=pathlib.Path(__file__).resolve().parent
root=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
assert str(root)=='/home/aither/workspace/ai/vpsfree.cz'
slug='2026-10-20-dev-workspace-portal-improvements'
assert os.environ.get('DEV_SESSION_SLUG') in (None,slug)
assert os.environ.get('DEV_SESSION_WORKSPACE') in (None,str(root))
assert bool(os.environ.get('DEV_SESSION_SLUG'))==bool(os.environ.get('DEV_SESSION_WORKSPACE'))
assert subprocess.check_output(['dev-session','current'],cwd=root,text=True).strip()==slug
remote=(p/'collect-remote.py').read_bytes()
argv=['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','IdentitiesOnly=yes','-o','ConnectTimeout=10','-i','/home/aither/.ssh/id_ed25519','root@172.16.106.40',shlex.quote(os.path.realpath(sys.executable))+' -']
start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
r=subprocess.run(argv,input=remote,capture_output=True,timeout=35)
if r.returncode:raise SystemExit('remote collection failed exit '+str(r.returncode)+'; no raw remote stderr retained')
data=json.loads(r.stdout)
receipt={'started_utc':start,'elapsed_s':round(time.monotonic()-t,3),'exit':r.returncode,'argv':argv,'collector_sha256':hashlib.sha256(remote).hexdigest(),'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_present':bool(r.stderr),'scope':'Read-only historical log aggregate; no network application probe, connection count/reset, credential read or service command.'}
with open(root/'.git/dev-session-tracking.lock','a') as f:
 fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
 if (p/'aggregate.json').exists():raise SystemExit('retained aggregate exists; refusing overwrite/repeat')
 (p/'aggregate.json').write_text(json.dumps(data,indent=2)+'\n')
 (p/'command-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(data,indent=2))

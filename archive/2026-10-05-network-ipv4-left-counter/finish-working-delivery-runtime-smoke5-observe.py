import datetime,hashlib,json,pathlib,re,subprocess,time
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
p=json.loads((T/'finish-working-delivery-runtime-smoke5-preparation.json').read_text())
c=pathlib.Path(p['context']);root=pathlib.Path(p['capacity_path']).parent/'campaign'
systemctl='/nix/store/khnfirshq5j299s6sfj0laxj0vr7gaa6-systemd-260.2/bin/systemctl'
last=None;reported=0
while not (c/'result.json').exists():
 stage={};a=root/'receipts/runtime-smoke-attempt.json'
 if a.exists():
  try:
   v=json.loads(a.read_text());stage={k:v[k] for k in ['stage','time','failed_stage','error_class'] if k in v}
  except (FileNotFoundError,json.JSONDecodeError):pass
 r=subprocess.run([systemctl,'--user','show',p['unit'],'--property=ActiveState,SubState,MainPID'],capture_output=True,text=True,check=True)
 props=dict(x.split('=',1) for x in r.stdout.splitlines() if '=' in x)
 kernels=[]
 for f in root.glob('diagnostics/*/stderr'):
  # Export only an exact immutable Linux derivation name, never log text.
  for line in f.read_text(errors='replace').splitlines():
   m=re.fullmatch(r"building '(/nix/store/[a-z0-9]{32}-linux-[^/']+\.drv)'\.\.\.",line)
   if m:kernels.append(m.group(1))
 if kernels:
  print(json.dumps({'unexpected_kernel_builds':kernels,'unit':p['unit'],'result':'escalation'}),flush=True);raise SystemExit(2)
 status=(stage,props)
 if status!=last or time.monotonic()-reported>=60:
  print(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stage':stage,'unit':props,'result':'pending'}),flush=True)
  last=status;reported=time.monotonic()
 if props.get('ActiveState') in ['failed','inactive'] and props.get('MainPID')=='0':
  print(json.dumps({'result':'incomplete','unit':props}),flush=True);raise SystemExit(1)
 time.sleep(5)
v=json.loads((c/'result.json').read_text());accepted=v.get('complete') is True and v.get('exit_code')==0 and not v.get('cancel_reason') and not v.get('wrapper_failure')
safe={k:v.get(k) for k in ['complete','exit_code','cancel_reason','wrapper_failure','started_at','finished_at']}
safe.update(accepted=accepted,unit=p['unit'],result_sha256=hashlib.sha256((c/'result.json').read_bytes()).hexdigest())
print(json.dumps(safe),flush=True)
raise SystemExit(0 if accepted else 1)

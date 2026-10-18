import json,os,pathlib,subprocess,time
root=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz');out=root/'work/2026-10-16-idle-coordination-worker'
env=os.environ|{'DEV_SESSION_SLUG':'2026-10-16-idle-coordination-worker','DEV_SESSION_WORKSPACE':str(root)}
previous=None
while True:
 r=subprocess.run(['dev-session','coordination','status','2026-10-16-idle-coordination-worker','--as-is','--json'],cwd=root,env=env,capture_output=True,text=True)
 if r.returncode:
  print('status_error',r.returncode,r.stderr[-1500:],flush=True);raise SystemExit(r.returncode)
 v=json.loads(r.stdout);(out/'compat-deployment-status.json').write_text(r.stdout)
 projection={'jobs':[{k:x.get(k) for k in ['id','kind','state','revision','attempt','reason']} for x in v['jobs']],'reservations':[{k:x.get(k) for k in ['id','state','revision']} for x in v['reservations']],'foreign':v.get('foreignReservations',[]),'profile':os.path.realpath('/home/aither/.local/state/dev-workspaces/profile')}
 if projection!=previous:
  with (out/'compat-deployment-observations.jsonl').open('a') as log:log.write(json.dumps({'time':time.time(),'status':v})+'\n')
  print(json.dumps(projection),flush=True);previous=projection
 states={x['state'] for x in v['jobs']}
 if states & {'needs_refresh','failed','canceled','reconciling'}:raise SystemExit(3)
 if states=={'succeeded'}:raise SystemExit(0)
 time.sleep(15)

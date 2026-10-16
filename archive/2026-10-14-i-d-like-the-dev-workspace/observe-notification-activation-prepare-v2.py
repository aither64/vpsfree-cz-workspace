import pathlib, time, json
root=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace')
for name in ['machine','profile']:
 p=root/(name+'-prepare-notification-activation-v2.status')
 while not p.exists():time.sleep(5)
 d=dict(line.split('=',1) for line in p.read_text().splitlines())
 print(json.dumps({'phase':name,**d}),flush=True)
 if d.get('exit_status')!='0':raise SystemExit(1)

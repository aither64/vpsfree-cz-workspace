import json,subprocess
r=subprocess.run(['curl','--silent','--max-time','5','--max-filesize','8192','--unix-socket','/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock','--header','Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz','--write-out','\n%{http_code}','http://localhost/api/browser-notifications'],capture_output=True,text=True)
status,available=0,False
try:
 body,code=r.stdout.rsplit('\n',1);status=int(code);payload=json.loads(body);available=r.returncode==0 and status==200 and payload.get('available') is True
except (ValueError,TypeError,AttributeError):
 pass
print(json.dumps({'http_status':status,'available':available}))
raise SystemExit(0 if status==200 and available else 1)

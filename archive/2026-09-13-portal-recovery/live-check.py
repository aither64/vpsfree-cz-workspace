import base64,hashlib,json,ssl,urllib.request,urllib.error
from pathlib import Path
root=Path(__file__).parent
base='https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
slug='2026-09-13-portal-recovery'
context=ssl.create_default_context(cafile='/var/lib/dev-workspaces/public/ca.pem')
password=Path('/var/lib/dev-workspaces/password/password').read_text().strip()
headers={'Authorization':'Basic '+base64.b64encode(('aither:'+password).encode()).decode()}
def get(path,auth=True):return urllib.request.urlopen(urllib.request.Request(base+path,headers=headers if auth else {}),context=context,timeout=35)
results={}
for path in ['/healthz','/','/'+slug+'/','/static/app.js','/static/repository-review.js','/codex/assets/conversation.js?v=7','/codex/assets/sync.js?v=1','/api/sessions/'+slug+'/thread']:
 with get(path) as response:
  data=response.read();results[path]={'status':response.status,'cacheControl':response.headers.get('Cache-Control')}
  if path.endswith('/thread'):
   payload=json.loads(data);results[path]['threadStatus']=payload['status'];results[path]['entries']=len(payload.get('entries',[]))
  if '/assets/sync.js' in path:assert b'cycle.abort.abort()' in data
  if path=='/static/repository-review.js':assert b'historyHasPages' in data and b'payload.summary' in data
try:
 with get('/healthz',False) as response:raise AssertionError('unauthenticated health accepted')
except urllib.error.HTTPError as e:assert e.code==401;results['unauthenticatedHealth']=401
with get('/api/sessions/'+slug+'/events') as response:
 events=[]
 while len(events)<2:
  line=response.readline().decode().strip()
  if line.startswith('event:'):events.append(line)
 assert events==['event: ready','event: heartbeat'],events
 results['sse']=events
# Repository ids are deterministic, opaque review IDs visible in the actual page.
with get('/'+slug+'/') as response:html=response.read().decode()
import re
ids=re.findall(r'data-repository-id="([^"]+)"',html)
with get('/api/sessions/'+slug+'/repository-histories?'+urllib.parse.urlencode([('repository',i) for i in ids])) as response:
 payload=json.load(response);results['repositories']=[]
 for item in payload['repositories']:
  assert 'summary' in item,item
  summary=item['summary'];assert summary['commitCount']>0
  results['repositories'].append({'id':item['repository'],'summary':summary})
(root/'live-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))

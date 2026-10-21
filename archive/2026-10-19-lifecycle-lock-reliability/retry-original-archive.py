from pathlib import Path
import json,socket,http.client,os,fcntl,time
tracking=Path(__file__).resolve().parent
slug='2026-10-19-session-archive-refresh-fix'
class UnixHTTP(http.client.HTTPConnection):
    def connect(self):
        self.sock=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        self.sock.connect('/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock')
def request(method,path,payload=None):
    connection=UnixHTTP('localhost',timeout=30)
    headers={'Origin':'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'}
    body=None
    if payload is not None:
        body=json.dumps(payload);headers['Content-Type']='application/json'
    connection.request(method,path,body,headers)
    response=connection.getresponse();data=response.read();connection.close()
    if response.status>=300:raise SystemExit(str(response.status)+' '+data.decode())
    return json.loads(data)
base='/api/sessions/'+slug+'/operation'
old=json.loads((tracking/'original-archive-before.json').read_text())
current=request('GET',base)
assert current['receiptId']==old['receiptId']
assert current['options']['journalId']==old['options']['journalId']
assert current['attempt']==old['attempt'] and current['state'] in ['failed','paused']
package=os.path.realpath('/home/aither/.local/state/dev-workspaces/profile')
text=(tracking/'profile-prepare.stdout').read_text()
prepared=json.JSONDecoder().raw_decode(text[text.index('{'):])[0]
assert package==prepared['operation']['candidatePackage']
with open('/run/user/1000/dev-workspaces/vpsfree-cz/authority/'+slug+'.lock','rb') as shared:
    fcntl.flock(shared,fcntl.LOCK_SH)
    reply=request('POST',base+'/retry',{'receiptId':current['receiptId'],'journalId':current['options']['journalId']})
    (tracking/'original-archive-retry.json').write_text(json.dumps(reply,indent=2)+'\n')
    waiting=None
    for _ in range(30):
        observed=request('GET',base)
        if observed.get('progress',{}).get('stage')=='Waiting for session access':
            waiting=observed;break
        assert observed.get('state') not in ['failed','complete'], observed
        time.sleep(1)
    assert waiting, 'archive worker did not publish waiting stage while shared access held'
    assert waiting['receiptId']==old['receiptId'] and waiting['attempt']==old['attempt']+1
    assert (tracking.parents[1]/'work'/slug).is_dir()
    (tracking/'original-archive-contention-proof.json').write_text(json.dumps(waiting,indent=2)+'\n')
    fcntl.flock(shared,fcntl.LOCK_UN)
print(json.dumps(reply))

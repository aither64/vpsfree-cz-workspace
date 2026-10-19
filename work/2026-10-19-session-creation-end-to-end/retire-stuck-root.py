"""Exact-root native retirement to resume the already accepted deletion journal."""
import json, socket, pathlib, websocket
thread = '01a153e8-7364-7321-b0ae-0f636dd6824b'
cwd = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-haveapi-async-client-plan'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect('/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock')
ws = websocket.create_connection('ws://localhost/', socket=sock, timeout=30)
sequence = 0
def request(method, params):
 global sequence
 sequence += 1
 ws.send(json.dumps({'id': sequence, 'method': method, 'params': params}))
 while True:
  value = json.loads(ws.recv())
  if value.get('id') != sequence: continue
  if 'error' in value: raise RuntimeError(value['error'])
  return value['result']
request('initialize', {'clientInfo':{'name':'creation-deletion-recovery','version':'1'},'capabilities':{'experimentalApi':True}})
ws.send(json.dumps({'method':'initialized'}))
metadata = request('thread/read', {'threadId':thread,'excludeTurns':False})['thread']
assert metadata['id'] == thread and metadata['cwd'] == cwd, 'Retained root identity mismatch'
assert metadata['status']['type'] != 'active', 'Root must be idle before retirement'
result = request('thread/archive', {'threadId':thread})
after = request('thread/read', {'threadId':thread,'excludeTurns':True})['thread']
assert after['id'] == thread and after['cwd'] == cwd and '/archived_sessions/' in after['path']
record = {'threadId':thread,'cwd':cwd,'beforeStatus':metadata['status'],'archived':True,'result':result,
 'reason':'Normal delete already accepted, but provider-scoped active discovery hid the exact existing root. No journal or ownership record is edited.'}
pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-session-creation-end-to-end/stuck-root-retired.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
ws.close()

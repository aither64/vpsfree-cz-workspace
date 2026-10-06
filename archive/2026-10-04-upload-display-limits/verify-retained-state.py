from pathlib import Path
import json,subprocess
r=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits')
a=json.loads((r/'pre-switch-roster.json').read_text())['roster']
b=json.loads((r/'post-switch-roster.json').read_text())['roster']
for key in ['workspace','slug','rootThreadId','presetId','catalogDigest','teamDigest','leadModel','leadEffort','leadInstructions']:
    assert a[key]==b[key],key
assert a['members']==b['members'],'retained member settings/identities changed'
assert json.loads((r/'pre-switch-registry.json').read_text())==json.loads(Path('/home/aither/.config/dev-workspaces/registry.json').read_text()),'registration changed'
old=[l for l in (r/'pre-switch-tmux.txt').read_text().splitlines() if '2026-10-04-upload-display-limits' in l]
new=subprocess.check_output(['tmux','-S','/run/user/1000/dev-workspaces/vpsfree-cz/tmux.sock','list-sessions','-F','#{session_id} #{session_name}'],text=True).splitlines()
assert old and all(l in new for l in old),'own tmux identity changed'
expected=Path('/nix/store/jq982nq0jxfhmr4jxyvkglnyy77n1kxf-dev-workspace-0.2.0')
assert Path('/home/aither/.local/state/dev-workspaces/profile').resolve()==expected,'unexpected profile'
pid=subprocess.check_output(['systemctl','--user','show','workspace-portal@vpsfree-cz.service','-p','MainPID','--value'],text=True).strip()
assert (Path('/proc')/pid/'exe').resolve()==(expected/'bin/workspace-portal').resolve(),'serving portal executable mismatch'
print('Exact candidate profile and serving executable, registration, own tmux and retained root/member identities/settings passed.')

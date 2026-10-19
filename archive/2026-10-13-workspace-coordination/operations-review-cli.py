import json,os,subprocess,tomllib
from pathlib import Path
root=Path('/home/aither/workspace/ai/vpsfree.cz')
t=root/'work/2026-10-13-workspace-coordination'
package=Path('/nix/store/11l74j11jc86l0zw5gjqw0zf6n0c8lbc-dev-workspace-0.2.0')
catalog=json.loads((package/'share/dev-workspace/agent-teams.json').read_text())
team=catalog['default_development_team']; role=catalog['teams'][team]['roles']['reviewer']
assert role['model']=='gpt-6-astra' and role['effort']=='xhigh' and role['access']=='read_only'
native=next(x for x in catalog['native_agent_configs']['roles'] if x['team']==team and x['role']=='reviewer' and x['effort']==role['effort'])
instructions=tomllib.loads((package/native['path']).read_text())['developer_instructions']
args=['/run/current-system/sw/bin/codex','exec','--model',role['model'],'-c','model_reasoning_effort='+json.dumps(role['effort']),'-c','developer_instructions='+json.dumps(instructions),'--sandbox','read-only','--ephemeral','--json','--output-last-message',str(t/'operations-review-native.md'),'-']
identity={'model':role['model'],'effort':role['effort'],'access':role['access'],'nativeRole':native['name'],'catalogDigest':catalog['catalog_digest'],'fallbackReason':'Existing reviewer thread transport could not be validated: native MCP connection to 127.0.0.1:38935 failed. Fresh standalone catalog-policy reviewer via CLI.'}
(t/'operations-review-native-identity.json').write_text(json.dumps(identity,indent=2)+'\n')
env=dict(os.environ,DEV_SESSION_SLUG='2026-10-13-workspace-coordination',DEV_SESSION_WORKSPACE=str(root))
prompt='You are a fresh independent final reviewer. Read '+str(t/'operations-review-packet.md')+' and follow all four review lanes directly. The packet\'s prior retained reviewer paragraph is superseded by operations-review-native-identity.json: thread transport is unavailable, so you are a fresh policy-matched standalone replacement, Astra/xhigh/read-only. Read applicable AGENTS and procedure paths before acting. Do not edit, deploy, fetch/push, create threads or delegate. Review committed deliverables and all complete histories, including generated pin consolidation and no-migration conclusion. Return findings, tested evidence and residual gaps as your final message; the CLI retains it as an artifact. No source or tracking mutations.'
status=subprocess.run(args,input=prompt,text=True,cwd=root,env=env).returncode
p=t/'operations-review-native.status.tmp';p.write_text(str(status)+'\n');p.replace(t/'operations-review-native.status')
raise SystemExit(status)

import json,sys
from pathlib import Path
import subprocess
expected_revisions = {
    'workspace': '3de65bbd0e90f0c3b19e0d64ed925158155647a6',
    'dev-workspace': 'db25364999aa4bf12b67506662a08e9e464bee33',
    'codex-web': '852e8c51091512bc79ca6c921ef1f5ccc46a9535',
}
verification_sources = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements')
for name, revision in expected_revisions.items():
    assert subprocess.check_output(['git','-C',str(verification_sources/name),'rev-parse','HEAD'],text=True).strip()==revision, name
lock=json.loads((verification_sources/'workspace/flake.lock').read_text())
assert lock['nodes']['dev-workspace']['locked']['rev']==expected_revisions['dev-workspace']
assert lock['nodes']['codex-web']['locked']['rev']==expected_revisions['codex-web']
assert lock['nodes']['vpsfree-dev-workspace']['locked']['rev']=='767dfd587e346168e1443e65ccdb67ce748f3fe3'
package=Path(sys.argv[1]); shared=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/codex-web')
metadata=json.loads((package/'share/dev-workspace/package.json').read_text())
catalog=json.loads((package/metadata['agent_teams']['catalog']['path']).read_text())
assert catalog['schema_version']==6 and catalog['execution_access']=='full_access'
assert catalog['default_team']==catalog['default_development_team']=='delegated'
assert sorted(catalog['teams'])==['delegated','delegated_3','delegated_4','delegated_5','delegated_6','lead_designed','lead_reviewed','solo']
assert catalog['capacity']['required_native_child_threads']==8
assert metadata['agent_teams']['capacity']['required_native_child_threads']==8
assert metadata['agent_teams']['native_capacity']=={'config_key':'agents.max_concurrent_threads_per_session','required_value':8}
assert metadata['agent_teams']['catalog']['digest']==catalog['catalog_digest']
for count in range(2,7):
    preset='delegated' if count==2 else f'delegated_{count}'
    team=catalog['teams'][preset]
    assert team['initial_member_counts']=={'implementer':count}
    assert team['max_open_agents']==count+2 and team['design_owner']=='designer'
    assert team['roles']==catalog['teams']['delegated']['roles']
    assert team['roles']['team_lead']['model']=='gpt-6.1-sol' and team['roles']['team_lead']['effort']=='high'
    assert team['roles']['designer']['model']=='gpt-6-astra' and team['roles']['designer']['effort']=='xhigh'
    for role in ['implementer','reviewer']:
        assert team['roles'][role]['model']=='gpt-6.1-sol' and team['roles'][role]['effort']=='xhigh'
watcher=catalog['utilities']['verification_watcher']
assert watcher['model']=='gpt-6-luna' and watcher['effort']=='low' and watcher['max_concurrent']==1
for variant in catalog['native_agent_configs']['roles']+catalog['native_agent_configs']['utilities']:
    config=(package/variant['path']).read_text()
    assert 'sandbox_mode = "danger-full-access"' in config
    assert 'approval_policy = "never"' in config
for source in (shared/'codex').glob('*.go'):
    if not source.name.endswith('_test.go'):
        assert (package/'share/workspace-portal/codex'/source.name).read_bytes()==source.read_bytes(),source.name
native=(package/'libexec/codex/libexec/codex/codex-package.json')
assert json.loads(native.read_text())['version']=='0.163.0'
print('Catalog/default/family/model/utility/native policy and metadata capacity8 match; shipped Go source matches A; Codex remains0.163.0')

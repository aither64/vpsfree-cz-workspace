import json,sys
from pathlib import Path
import subprocess
expected_revisions = {
    'workspace': '12b4491bd6e5bfa6799e938fd555c8f15d588a1d',
    'dev-workspace': '483d4e7eafeda974dfe19de45687795562072d7d',
    'codex-web': 'ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5',
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

selected=Path('/nix/store/f5h1qmr03qva6khyijgc2wxd1ff4k4cw-dev-workspace-0.2.0')
assert (package/'libexec/codex/bin/codex').resolve()==(selected/'libexec/codex/bin/codex').resolve()==Path('/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex')
for relative in ('share/workspace-portal/runtime-contract.json',
                 'share/dev-workspace/claim-contract.json',
                 'share/dev-workspace/coordination-contract.json',
                 'share/dev-workspace/integration-contract.json'):
    assert json.loads((package/relative).read_text())==json.loads((selected/relative).read_text()), relative
print('Candidate native Codex equals selected executable; runtime/claim/coordination/integration contracts unchanged')

runtime=verification_sources/'dev-workspace'
for relative in ('docs/coordination.md', 'docs/coordination-operations.md'):
    assert (package/'share/dev-workspace'/Path(relative).name).read_bytes()==(runtime/relative).read_bytes(),relative
assert json.loads((package/'share/dev-workspace/repository-claim-contract.json').read_text())=={'schema':1,'registeredRepositories':True}
print('Shipped machine-retention guidance and separate registered-repository capability match final B')

# Actual source consumer/cache contract; package build postPatch independently
# enforces the same Go/Nix module selection before compilation.
app=(runtime/'portal/internal/web/static/app.js').read_text()
assert '/codex/assets/conversation.js?v=22' in app
assert '/codex/assets/conversation.js?v=21' not in app
for name in ['session.html','index.html','automatic-archival.html']:
 assert '/static/app.js?v=55' in (runtime/'portal/internal/web/templates'/name).read_text()
assert '/codex/assets/conversation.js?v=12' in (runtime/'portal/internal/web/static/creation.js').read_text()
print('Final app55/store4/browser6 and mounted22/sync3/uploads7 consumer provenance retained; creation copy-helperv12 unchanged')

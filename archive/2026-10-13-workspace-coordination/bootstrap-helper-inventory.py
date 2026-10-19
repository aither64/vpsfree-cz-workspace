import json
import subprocess
from pathlib import Path

root = Path('/home/aither/workspace/ai/vpsfree.cz')
tracking = root / 'work/2026-10-13-workspace-coordination'
inventory = json.loads((tracking / 'creation-provider-final-inventory.json').read_text())

def git(repo, *args):
    return subprocess.check_output(['git', '-C', repo, *args], text=True)

for item in inventory:
    repo = item['worktree']
    assert not git(repo, 'status', '--porcelain')
    previous = item['head']
    item['previousHead'] = previous
    item['reviewedHead'] = previous
    item['head'] = git(repo, 'rev-parse', 'HEAD').strip()
    item['commits'] = git(repo, 'log', '--reverse', '--format=%H %s', item['base'] + '..' + item['head']).splitlines()
    for field, args in [('finalDiff', ('diff', item['base'], item['head'])), ('deltaDiff', ('diff', previous, item['head']))]:
        path = tracking / (item['repository'] + '-bootstrap-helper-' + field + '.patch')
        path.write_text(git(repo, *args))
        item[field] = str(path.relative_to(root))
    item['migrationProvenance'] = 'No migrations. Source-only helper uses the selected installed schemas; deployed predecessor refs and immutable rollout evidence remain retained.'

path = tracking / 'bootstrap-helper-final-inventory.json'
assert not path.exists()
path.write_text(json.dumps(inventory, indent=2) + '\n')

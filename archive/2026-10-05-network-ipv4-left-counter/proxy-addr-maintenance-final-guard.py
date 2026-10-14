import json
import os
import re
import subprocess
import sys
from pathlib import Path


tracking = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
repo = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-proxy-addr')
base = '02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51'
prefix = 'proxy-addr-maintenance-final'
paths = {'bff/package-lock.json', 'packages/bff.nix', 'docs/design/PACKAGING.md',
         'docs/work-log/2026-10-06-proxy-addr-patch.md'}
mode = sys.argv[1]
assert mode in ['hooks', 'staged', 'committed', 'metadata']


def git(*args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True)


if mode == 'hooks':
    for name in ['.overcommit.yml', '.pre-commit-config.yaml', '.pre-commit-config.yml',
                 'lefthook.yml', 'lefthook.yaml', '.husky']:
        assert not (repo / name).exists(), f'New hook declaration needs normal setup and inspection: {name}'
    manifest = json.loads((repo / 'package.json').read_text())
    assert not any(key in manifest for key in ['husky', 'simple-git-hooks'])
    assert not any(name in manifest.get('devDependencies', {}) for name in
                   ['husky', 'lefthook', 'simple-git-hooks'])
    configured = subprocess.run(['git', '-C', str(repo), 'config', '--get', 'core.hooksPath'],
                                text=True, capture_output=True)
    assert configured.returncode == 1, 'Custom hook path needs inspection before this operation'
    for hook in ['pre-commit', 'prepare-commit-msg', 'commit-msg', 'post-commit', 'pre-push']:
        hook_path = Path(git('rev-parse', '--git-path', f'hooks/{hook}').strip())
        if not hook_path.is_absolute():
            hook_path = repo / hook_path
        assert not os.access(hook_path, os.X_OK), f'Active undeclared Git hook needs inspection: {hook}'
    print('No declared framework, custom hook path or active undeclared hook; use normal git with no bypass')
    sys.exit(0)

if mode == 'staged':
    assert git('rev-parse', 'HEAD').strip() == base
    assert set(git('diff', '--cached', '--name-only').splitlines()) == paths
    assert not git('diff', '--name-only').strip(), 'Unexpected unstaged tracked change'
    assert not git('ls-files', '--others', '--exclude-standard').strip(), 'Unexpected untracked source'
    print('Exactly the four approved maintenance paths are staged')
    sys.exit(0)

selected = sys.argv[2]
assert re.fullmatch(r'[0-9a-f]{40}', selected)
assert git('rev-parse', 'HEAD').strip() == selected
assert git('rev-parse', 'HEAD^').strip() == base
assert git('rev-list', '--count', f'{base}..HEAD').strip() == '1'
assert not git('status', '--porcelain').strip()
assert set(git('diff', '--name-only', f'{base}..HEAD').splitlines()) == paths
print(f'One clean committed maintenance candidate: {selected}; exactly four paths; no migrations')
if mode == 'committed':
    sys.exit(0)


def build_output(name):
    assert (tracking / f'{prefix}-{name}.exit').read_text().strip() == '0'
    values = [line for line in (tracking / f'{prefix}-{name}.log').read_text().splitlines()
              if re.fullmatch(r'/nix/store/[0-9a-z]{32}-[^/\s]+', line)]
    assert len(values) == 1, (name, values)
    return Path(values[0])


frontend = build_output('build-frontend')
bff = build_output('build-bff')
checks = {name: str(build_output(f'check-{name}')) for name in
          ['provenance', 'source-contents', 'package-contents']}
frontend_info = json.loads((frontend / 'build-info.json').read_text())
bff_info = json.loads((bff / 'share/vpsadmin-webui-bff/build-info.json').read_text())
expected = {'schemaVersion': 1, 'commit': selected, 'shortCommit': selected[:12],
            'dirty': False, 'source': 'environment'}
assert frontend_info['dirty'] is False and bff_info['dirty'] is False
assert frontend_info == bff_info == expected, 'Paired metadata is not the exact clean committed full SHA'
installed = json.loads((bff / 'lib/vpsadmin-webui-bff/node_modules/proxy-addr/package.json').read_text())
assert installed['version'] == '2.0.8', 'BFF package does not contain the selected patched leaf'
evidence = {'revision': selected, 'branch': 'dev/proxy-addr-patch',
            'frontend': str(frontend), 'bff': str(bff), 'checks': checks,
            'frontendMetadata': frontend_info, 'bffMetadata': bff_info,
            'installedProxyAddr': installed['version']}
with (tracking / f'{prefix}-paired-package-metadata.json').open('x') as output:
    json.dump(evidence, output, indent=2)
    output.write('\n')
print(json.dumps(evidence, sort_keys=True))

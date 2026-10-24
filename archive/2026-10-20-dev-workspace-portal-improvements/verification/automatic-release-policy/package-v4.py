#!/usr/bin/env python3
"""Prepared only. Parent binds reviewed identities before a fresh utility runs it."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

HERE = Path(__file__).resolve().parent
WORKSPACE = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-20-dev-workspace-portal-improvements'
ROOT = WORKSPACE / 'worktrees' / SLUG
SELECTED = Path('/nix/store/m8bqmkdzgk85vng42hcsavqmaz56rwgc-dev-workspace-0.2.0')
HEADS = {
    'codex-web': 'ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5',
    'dev-workspace': 'bf6d4b0c49600c15e17fe71248807ef43424e932',
    'workspace': '6bc355ba27032f927e29fe50ed19afbbf2f7ba73',
    'vpsfree-cz-configuration': '1d71ce148d43e156d4f3be9193a2b8caad56e94a',
}
BASES = {
    'dev-workspace': '483d4e7eafeda974dfe19de45687795562072d7d',
    'workspace': '1f29a819e565d79a15be446073dbb96b4b3951ab',
    'vpsfree-cz-configuration': 'ef2194e63367b3a8e4f5fbdd27002293d779becb',
}
REVIEW = {
    'path': '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/automatic-release-policy/review-refresh-certificate.json',
    'sha256': '08b69b4e2f2d2ea5cdd593885487078a259d13ab816cbdb37daf71f7b44c9c7b',
    'sources': HEADS, 'accepted': True,
}
ALLOWED = {
    'dev-workspace': {
        'portal/internal/workspacecodex/lead_policy.go',
        'portal/internal/workspacecodex/lead_policy_test.go',
        'portal/internal/teamruntime/runtime_test.go', 'docs/coordination.md', 'docs/coordination-operations.md',
    },
    'workspace': {
        'AGENTS.md', 'docs/coordination.md', 'docs/agent-instructions/deployment.md',
        'docs/agent-instructions/lifecycle.md', 'docs/agent-instructions/git.md',
        'test/agent_instructions_test.rb', 'flake.nix', 'flake.lock',
    },
    'vpsfree-cz-configuration': {'docs/operations/workspace-coordination-aitherdev.md', 'flake.lock'},
}


def require(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def capture(argv, cwd=None, env=None):
    return subprocess.check_output(argv, cwd=cwd, env=env, stderr=subprocess.PIPE)


def git(repo, *args):
    return capture(['git', '-C', str(ROOT / repo), *args])


def source(repo, revision, path):
    return git(repo, 'show', revision + ':' + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(path, value):
    with path.open('x') as output:
        json.dump(value, output, indent=2)
        output.write('\n')


def lock_guard(repo, input_path):
    old, new = [json.loads(source(repo, revision, 'flake.lock')) for revision in (BASES[repo], HEADS[repo])]
    def key(lock):
        node = lock['root']
        for name in input_path:
            node = lock['nodes'][node]['inputs'][name]
            require(isinstance(node, str), 'unexpected follows path')
        return node
    old_key, new_key = key(old), key(new)
    require(old_key == new_key, 'runtime node renamed')
    selected = new['nodes'][new_key]['locked']
    require(selected['repo'] == 'dev-workspace' and selected['owner'] == 'aither64' and
            selected['rev'] == HEADS['dev-workspace'], 'wrong runtime pin')
    for lock, node in ((old, old_key), (new, new_key)):
        lock['nodes'][node]['locked'] = 'RUNTIME_IDENTITY'
        original = lock['nodes'][node].get('original', {})
        if 'rev' in original:
            original['rev'] = 'RUNTIME_REVISION'
    require(old == new, 'unrelated dependency graph delta')
    return selected


def guards():
    require(all(re.fullmatch('[0-9a-f]{40}', v) for v in HEADS.values()), 'source heads pending')
    require(REVIEW['accepted'] is True and REVIEW['sources'] == HEADS and
            re.fullmatch('[0-9a-f]{64}', REVIEW['sha256']), 'final review pending')
    review = Path(REVIEW['path']).resolve(strict=True)
    require(review.is_relative_to(WORKSPACE / 'work' / SLUG) and review.is_file() and
            sha(review.read_bytes()) == REVIEW['sha256'], 'review receipt absent or changed')
    require(capture(['dev-session', 'current']).decode().strip() == SLUG, 'wrong session')
    a, b = os.getenv('DEV_SESSION_SLUG'), os.getenv('DEV_SESSION_WORKSPACE')
    require((a is None and b is None) or (a == SLUG and b == str(WORKSPACE)), 'environment mismatch')
    require(Path('/home/aither/bin/workspace-host').resolve(strict=True) == SELECTED / 'bin/workspace-host' and
            Path('/home/aither/.local/state/dev-workspaces/profile').resolve(strict=True) == SELECTED,
            'selected predecessor changed')
    for repo, head in HEADS.items():
        require(git(repo, 'rev-parse', 'HEAD').decode().strip() == head and
                not git(repo, 'status', '--porcelain'), 'head or cleanliness mismatch: ' + repo)
    boundary = {}
    for repo, allowed in ALLOWED.items():
        changed = set(git(repo, 'diff', '--name-only', BASES[repo], HEADS[repo]).decode().splitlines())
        require(changed == allowed, 'assigned path boundary changed: ' + repo)
        boundary[repo] = sorted(changed)
    require(source('dev-workspace', BASES['dev-workspace'], 'flake.lock') ==
            source('dev-workspace', HEADS['dev-workspace'], 'flake.lock'), 'B dependency graph changed')
    c_pin = lock_guard('workspace', ['vpsfree-dev-workspace', 'dev-workspace'])
    require(c_pin == lock_guard('vpsfree-cz-configuration', ['devWorkspace']), 'C/config pins differ')
    require(json.loads(source('dev-workspace', HEADS['dev-workspace'], 'flake.lock'))['nodes']['codex-web']['locked']['rev'] ==
            HEADS['codex-web'], 'A revision changed')
    finite = {}
    paths = ['nix/host-module.nix', 'nix/host-paths.nix', 'nix/systemd', 'nix/codex-package.nix',
             'libexec/workspace-host', 'libexec/workspace-profile-identity.rb',
             'libexec/workspace-coordination-host.rb', 'libexec/workspace-coordination-claims-host.rb',
             'nix/claim-contract.json', 'nix/coordination-contract.json',
             'portal/internal/session/runtime-contract.json', 'portal/go.mod', 'portal/go.sum',
             'portal/internal/web/static', 'portal/internal/web/templates', 'portal/internal/teamruntime/runtime.go']
    for path in paths:
        rows = [git('dev-workspace', 'ls-tree', rev, '--', path) for rev in
                (BASES['dev-workspace'], HEADS['dev-workspace'])]
        require(rows[0] and rows[0] == rows[1], 'host/native/browser payload changed: ' + path)
        finite[path] = rows[0].decode().strip()
    for path in ['flake.nix', 'cluster/cz.vpsfree/machines/aitherdev/config.nix',
                 'cluster/cz.vpsfree/machines/aitherdev/module.nix',
                 'cluster/cz.vpsfree/machines/aitherdev/dev-workspace-site.nix']:
        require(source('vpsfree-cz-configuration', BASES['vpsfree-cz-configuration'], path) ==
                source('vpsfree-cz-configuration', HEADS['vpsfree-cz-configuration'], path), 'host config changed')
    return {'sources': HEADS, 'assignedDelta': boundary, 'unchangedPayloads': finite,
            'A_tree': git('codex-web', 'rev-parse', 'HEAD^{tree}').decode().strip(),
            'review': REVIEW, 'C_config_runtime': c_pin, 'predecessor': str(SELECTED)}


def stage(operation, label, attribute):
    expression = '(builtins.getFlake "git+file://' + str(ROOT / 'workspace') + '?rev=' + HEADS['workspace'] + '").' + attribute
    def logged(index, argv):
        with (operation / (label + '-' + str(index) + '.stdout')).open('xb') as out, \
                (operation / (label + '-' + str(index) + '.log')).open('xb') as err:
            subprocess.run(argv, stdout=out, stderr=err, check=True)
    instantiate = ['nix-instantiate', '--expr', expression, '--add-root',
                   str(operation / 'roots' / (label + '.drv')), '--indirect']
    logged(0, instantiate)
    drv = str((operation / 'roots' / (label + '.drv')).resolve(strict=True))
    require(re.fullmatch('/nix/store/[a-z0-9]{32}-[^/]+[.]drv', drv), 'invalid evaluated derivation')
    derivation = capture(['nix', 'derivation', 'show', drv])
    (operation / (label + '-derivation.json')).write_bytes(derivation)
    record = json.loads(derivation)
    require(set(record) == {'derivations', 'version'} and record['version'] == 4 and
            set(record['derivations']) == {Path(drv).name}, 'expected exact Nix v4 derivation envelope')
    record = {drv: record['derivations'][Path(drv).name]}
    require(list(record) == [drv] and set(record[drv]['outputs']) == {'out'}, 'expected one derivation output')
    output = '/nix/store/' + record[drv]['outputs']['out']['path']
    require(re.fullmatch('/nix/store/[a-z0-9]{32}-[^/]+', output), 'invalid evaluated output')
    if label == 'workspace':
        require(drv == '/nix/store/715a6j8ncmaa9a2qylrd2ds8nj9w56ax-dev-workspace-0.2.0.drv' and
                output == '/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0',
                'workspace identity differs from preserved first evaluation')
    require(capture(['nix-store', '--query', '--outputs', drv]).decode().splitlines() == [output],
            'evaluated output query differs')
    # Persist the immutable source/attribute and evaluated identities before realization.
    write(operation / (label + '-evaluated.json'), {
        'source': HEADS['workspace'], 'attribute': attribute, 'drv': drv, 'output': output,
        'derivationSHA256': sha(derivation), 'instantiate': instantiate,
    })
    realize = ['nix-store', '--realise', drv, '--add-root', str(operation / 'roots' / label), '--indirect']
    logged(1, realize)
    require(str((operation / 'roots' / label).resolve(strict=True)) == output and
            capture(['nix-store', '--query', '--outputs', drv]).decode().splitlines() == [output],
            'realized output mismatch')
    info = capture(['nix', 'path-info', '--json', output])
    (operation / (label + '-path-info.json')).write_bytes(info)
    parsed = json.loads(info)
    paths = [row['path'] for row in parsed] if isinstance(parsed, list) else list(parsed)
    require(paths == [output], 'path-info output mismatch')
    return {'commands': [instantiate, realize], 'drv': drv, 'output': output}


def packaged_policy(operation, package):
    package = Path(package)
    for relative in ['share/workspace-portal/runtime-contract.json', 'share/dev-workspace/claim-contract.json',
                     'share/dev-workspace/coordination-contract.json', 'share/dev-workspace/integration-contract.json',
                     'share/workspace-portal/codex-models.json', 'share/dev-workspace/agent-teams.json']:
        require((package / relative).read_bytes() == (SELECTED / relative).read_bytes(), 'packaged contract/catalog changed')
    require((package / 'libexec/codex/bin/codex').resolve(strict=True) ==
            (SELECTED / 'libexec/codex/bin/codex').resolve(strict=True), 'native executable changed')
    expected_docs = []
    for name in ['coordination.md', 'coordination-operations.md']:
        expected = source('dev-workspace', HEADS['dev-workspace'], 'docs/' + name)
        require((package / 'share/dev-workspace' / name).read_bytes() == expected, 'installed guide differs from reviewed source')
        expected_docs.append(expected)
    cwd = operation / 'guide-workspace'
    cwd.mkdir()
    guide = capture([str(package / 'bin/workspace-host'), 'coordination', 'guide'], cwd=cwd)
    (operation / 'installed-guide.log').write_bytes(guide)
    for expected in expected_docs:
        require(expected in guide, 'guide command omitted installed document')
    normalized = ' '.join(guide.decode().split())
    for required in ['Promptly release each deployed physical machine once both conditions are met',
                     'Deployment and its effects have been verified',
                     'complete deployed feature lineage is integrated into the approved remote default branches',
                     'without waiting for separate UI acceptance or release direction',
                     'exact claim owned by this session', 'verify its resulting state']:
        require(required in normalized, 'new policy text absent: ' + required)
    for obsolete in ['user accepts the resulting UI/behavior', 'user explicitly directs its release',
                     'verify all three conditions', 'renewed user acceptance']:
        require(obsolete not in normalized, 'obsolete human gate present')
    return {'guideSHA256': sha(guide), 'nativeAndCatalogUnchanged': True,
            'generatedBindings': 'Normal package go test ./... includes the reviewed lead/member instruction-contract tests; no live turn or role rewrite.'}


def main():
    proof = guards()  # All PENDING/absent-review guards precede Nix and result creation.
    operation = HERE / 'run-v4'
    operation.mkdir(exist_ok=False)
    (operation / 'roots').mkdir()
    write(operation / 'guards.json', proof)
    started = time.monotonic()
    try:
        stages = [stage(operation, 'workspace', 'packages.x86_64-linux.default'),
                  stage(operation, 'agent-instructions', 'checks.x86_64-linux.agent-instructions')]
        policy = packaged_policy(operation, stages[0]['output'])
        require(guards() == proof, 'source/predecessor changed during verification')
        write(operation / 'result.json', {'state': 'passed', 'sources': HEADS, 'stages': stages,
              'policy': policy, 'seconds': time.monotonic() - started, 'profileSelection': False})
    except BaseException:
        write(operation / 'result.json', {'state': 'failed', 'seconds': time.monotonic() - started,
              'sources': HEADS, 'profileSelection': False, 'retryPerformed': False})
        raise


if __name__ == '__main__':
    main()

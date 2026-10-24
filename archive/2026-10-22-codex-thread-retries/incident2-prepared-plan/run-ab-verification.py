#!/usr/bin/env python3
"""One exact, parent-selected verification batch; all evidence is retained."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

TRACK = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries')
B = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace')
RELEASE = json.loads((TRACK / 'incident2-prepared-plan/verification-release.json').read_text())
assert RELEASE['reviewAccepted'] is True
A = B.parent / 'codex-web'
RUN = TRACK / RELEASE['run']
HEAD, TREE = RELEASE['B']['head'], RELEASE['B']['tree']
NATIVE = Path('/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex')
UNDER = NATIVE.parent.parent / 'libexec/codex/bin/codex'
CHECKS = ['package', 'codex-package', 'ruby-source-filter', 'host-module',
          'host-auth-benchmark', 'host-package-contract', 'extension-catalog',
          'agent-team-catalog', 'user-namespace', 'generic-source', 'ruby-verification']
env = os.environ.copy()
env.update(DEV_SESSION_SLUG='2026-10-22-codex-thread-retries',
           DEV_SESSION_WORKSPACE='/home/aither/workspace/ai/vpsfree.cz', TMPDIR='/tmp')
os.umask(0o077)
RUN.mkdir()
results = []

def save(name, value):
    (RUN / name).write_text(json.dumps(value, indent=2) + '\n')

def command(label, args, cwd=B):
    save(label + '.command.json', {'command': args, 'cwd': str(cwd),
                                 'environment': {k: env[k] for k in ('DEV_SESSION_SLUG', 'DEV_SESSION_WORKSPACE', 'TMPDIR')}})
    started = time.monotonic()
    with (RUN / (label + '.stdout')).open('wb') as out, (RUN / (label + '.stderr')).open('wb') as err:
        completed = subprocess.run(args, cwd=cwd, env=env, stdout=out, stderr=err)
    result = {'label': label, 'exit': completed.returncode, 'elapsed': time.monotonic() - started}
    results.append(result)
    save(label + '.status.json', result)
    print(json.dumps(result), flush=True)
    if completed.returncode:
        raise RuntimeError('command failed: ' + label)
    return (RUN / (label + '.stdout')).read_text()

def identity(label):
    actual = command(label, ['git', 'status', '--porcelain'])
    assert not actual.strip(), actual
    assert command(label + '-head', ['git', 'rev-parse', 'HEAD']).strip() == HEAD
    assert command(label + '-tree', ['git', 'rev-parse', 'HEAD^{tree}']).strip() == TREE

try:
    assert command('session', ['dev-session', 'current'], TRACK).strip() == '2026-10-22-codex-thread-retries'
    for key in ('DEV_SESSION_SLUG', 'DEV_SESSION_WORKSPACE'):
        assert key not in os.environ or os.environ[key] == env[key]
    identity('source-before')
    assert not command('A-source-before', ['git', 'status', '--porcelain'], A).strip()
    assert command('A-head', ['git', 'rev-parse', 'HEAD'], A).strip() == RELEASE['A']['head']
    assert command('A-tree', ['git', 'rev-parse', 'HEAD^{tree}'], A).strip() == RELEASE['A']['tree']
    (RUN / 'A-flake.lock').write_bytes((A / 'flake.lock').read_bytes())
    command('A-metadata', ['nix', 'flake', 'metadata', '--json', '--no-write-lock-file', str(A)], A)
    a_mapping = json.loads(command('A-selectors', ['nix', 'eval', '--json', '--no-write-lock-file', str(A) + '#checks.x86_64-linux', '--apply',
        'checks: builtins.mapAttrs (_: drv: { drv = drv.drvPath; output = drv.outPath; }) checks'], A))
    a_roots = Path('/nix/var/nix/gcroots/per-user/aither') / (RELEASE['rootsName'] + '-A')
    a_roots.mkdir()
    for name, entry in a_mapping.items():
        assert Path(entry['drv']).exists(), entry
        (a_roots / name).symlink_to(entry['drv'])
    save('A-derivation-roots.json', {p.name: str(p.readlink()) for p in a_roots.iterdir()})
    a_selectors = [str(A) + '#checks.x86_64-linux.' + n for n in ('default', 'generic-source')]
    command('A-recursive-derivations', ['nix', 'derivation', 'show', '--recursive', '--no-write-lock-file'] + a_selectors, A)
    command('A-flakecheck-no-build', ['nix', 'flake', 'check', '--no-build', '--no-write-lock-file', '--print-build-logs'], A)
    a_built = json.loads(command('A-build-checks', ['nix', 'build', '--no-write-lock-file', '--print-build-logs', '--json', '--out-link', str(RUN / 'A-check-output')] + a_selectors, A))
    command('A-output-closures', ['nix', 'path-info', '--json', '--recursive'] + sorted({p for row in a_built for p in row['outputs'].values()}), A)
    (RUN / 'flake.lock').write_bytes((B / 'flake.lock').read_bytes())
    command('nix-version', ['nix', '--version'])
    command('metadata', ['nix', 'flake', 'metadata', '--json', '--no-write-lock-file', str(B)])
    raw_mapping = json.loads(command('selectors', ['nix', 'eval', '--json', '--no-write-lock-file',
         str(B) + '#checks.x86_64-linux', '--apply',
         'checks: builtins.mapAttrs (_: drv: { drv = drv.drvPath; output = drv.outPath; }) checks']))
    mapping = {name: {'drvPath': entry['drv'], 'outPath': entry['output']} for name, entry in raw_mapping.items()}
    save('selector-map.json', mapping)
    assert len([name for name in mapping if name.startswith('ruby-') and name != 'ruby-verification' and name != 'ruby-source-filter']) == 13
    old = json.loads((TRACK / 'verification-build/final-receipts-d819/metadata-comparison.json').read_text())['records']['B']['selectorMap']
    save('historical-selector-comparison.json', {name: {'current': mapping[name], 'prior': old.get(name), 'same': mapping[name] == old.get(name)} for name in CHECKS + [n for n in mapping if n.startswith('ruby-') and n not in CHECKS]})
    roots = Path('/nix/var/nix/gcroots/per-user/aither') / RELEASE['rootsName']
    roots.mkdir()
    for name in CHECKS:
        drv = Path(mapping[name]['drvPath'])
        assert drv.exists(), str(drv)
        (roots / name).symlink_to(drv)
    save('derivation-roots.json', {p.name: str(p.readlink()) for p in roots.iterdir()})
    selectors = [str(B) + '#checks.x86_64-linux.' + name for name in CHECKS]
    command('recursive-derivations', ['nix', 'derivation', 'show', '--recursive', '--no-write-lock-file'] + selectors)
    command('flakecheck-no-build', ['nix', 'flake', 'check', '--no-build', '--no-write-lock-file', '--print-build-logs'])
    built = json.loads(command('build-checks', ['nix', 'build', '--no-write-lock-file', '--print-build-logs', '--json', '--out-link', str(RUN / 'check-output')] + selectors))
    outputs = sorted({path for record in built for path in record['outputs'].values()})
    command('output-closures', ['nix', 'path-info', '--json', '--recursive'] + outputs)
    timings = []
    for name, entry in mapping.items():
        if name.startswith('ruby-') and name not in ('ruby-verification', 'ruby-source-filter'):
            timings.append(str(Path(entry['outPath']) / 'timings.json'))
    if all(Path(path).exists() for path in timings):
        command('ruby-shard-coverage', ['python3', str(B / 'test/check_ruby_shards.py')] + sorted(timings))
    else:
        historical = json.loads((TRACK / 'verification-build/final-receipts-d819/metadata-comparison.json').read_text())['records']['B']
        assert len(historical['rubyShards']) == 13
        assert all(mapping[name] == old[name] for name in historical['rubyShards'] + ['ruby-verification'])
        save('ruby-coverage-reuse.json', {'prior': 'verification-build/ab-d819ad04/build-B-ruby.status',
            'graphReceipt': 'verification-build/final-receipts-d819/metadata-comparison.json',
            'exactUnchangedAggregateAnd13Shards': historical['rubyShards'],
            'output': mapping['ruby-verification']['outPath'], 'reason': 'Exact successful historical derivations; some old individual timing outputs absent. No duplicate suite for receipt recovery.'})
    save('native-hashes.json', {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (NATIVE, UNDER)})
    assert hashlib.sha256(NATIVE.read_bytes()).hexdigest() == 'dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b'
    assert hashlib.sha256(UNDER.read_bytes()).hexdigest() == '5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5'
    a_raw = command('native-library', ['nix', 'develop', str(B), '-c', 'env', 'CODEX_WEB_TEST_BINARY=' + str(NATIVE),
          'go', 'test', '-mod=readonly', './codex', '-run', '^TestPinnedCodex(RecoveryRemainsColdUntilActivation|FailedTurnRetryContract)$',
          '-count=1', '-json', '-timeout=5m'], A)
    a_events = [json.loads(line) for line in a_raw.splitlines() if line.strip()]
    a_required = {'TestPinnedCodexRecoveryRemainsColdUntilActivation', 'TestPinnedCodexFailedTurnRetryContract'}
    a_required.update('TestPinnedCodexFailedTurnRetryContract/' + name for name in (
        'nonempty_continuation_default', 'nonempty_continuation_plan', 'exact_cyber_terminal',
        'automatic_queue_uses_execution_context', 'lost_accepted_reply_recreated_client',
        'native_direct_busy_race_compatibility'))
    assert a_required <= {event.get('Test') for event in a_events if event.get('Action') == 'pass'}
    assert not [event for event in a_events if event.get('Action') in ('skip', 'fail')]
    save('A-native-case-inventory.json', {'required': sorted(a_required), 'events': [e for e in a_events if e.get('Action') in ('pass', 'skip', 'fail')]})
    raw = command('native-runtime', ['nix', 'develop', str(B), '-c', 'env', 'LIVE_SWITCH_CODEX=' + str(NATIVE),
          'go', 'test', '-mod=readonly', '-tags=live_switch_integration', './cmd/workspace-portal', '-run',
          '^TestNative(LiveSwitchReconnect|TurnRetryController)$', '-count=1', '-json', '-timeout=5m'], B / 'portal')
    events = [json.loads(line) for line in raw.splitlines() if line.strip()]
    required = {'TestNativeLiveSwitchReconnect', 'TestNativeTurnRetryController'}
    assert required <= {event.get('Test') for event in events if event.get('Action') == 'pass'}
    assert not [event for event in events if event.get('Action') in ('skip', 'fail')]
    save('native-case-inventory.json', {'required': sorted(required), 'events': [e for e in events if e.get('Action') in ('pass', 'skip', 'fail')]})
    for case in RELEASE.get('extraChecks', []):
        assert set(case) == {'label', 'command', 'cwd'}
        command(case['label'], case['command'], Path(case['cwd']))
    identity('source-after')
    assert not command('A-source-after', ['git', 'status', '--porcelain'], A).strip()
    assert command('A-head-after', ['git', 'rev-parse', 'HEAD'], A).strip() == RELEASE['A']['head']
    assert command('A-tree-after', ['git', 'rev-parse', 'HEAD^{tree}'], A).strip() == RELEASE['A']['tree']
    save('result.json', {'result': 'passed', 'head': HEAD, 'tree': TREE, 'commands': results, 'roots': str(roots)})
except BaseException as error:
    save('result.json', {'result': 'incomplete', 'head': HEAD, 'tree': TREE, 'error': str(error), 'commands': results})
    raise

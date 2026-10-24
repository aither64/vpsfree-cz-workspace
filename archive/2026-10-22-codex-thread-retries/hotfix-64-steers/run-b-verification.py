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
RUN = TRACK / 'hotfix-64-steers/verification-b-ed2a75b9-final'
HEAD = 'ed2a75b98a75f9b37b7a359e9091a94e9846644e'
TREE = '63eba6140c340d28f38c39b010d0a5b2874b7680'
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
    roots = Path('/nix/var/nix/gcroots/per-user/aither/thread-retries-hotfix-ed2a75b9-final')
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
    raw = command('native-runtime', ['nix', 'develop', str(B), '-c', 'env', 'LIVE_SWITCH_CODEX=' + str(NATIVE),
          'go', 'test', '-mod=readonly', '-tags=live_switch_integration', './cmd/workspace-portal', '-run',
          '^TestNative(LiveSwitchReconnect|TurnRetryController)$', '-count=1', '-json', '-timeout=5m'], B / 'portal')
    events = [json.loads(line) for line in raw.splitlines() if line.strip()]
    required = {'TestNativeLiveSwitchReconnect', 'TestNativeTurnRetryController'}
    assert required <= {event.get('Test') for event in events if event.get('Action') == 'pass'}
    assert not [event for event in events if event.get('Action') in ('skip', 'fail')]
    save('native-case-inventory.json', {'required': sorted(required), 'events': [e for e in events if e.get('Action') in ('pass', 'skip', 'fail')]})
    identity('source-after')
    save('result.json', {'result': 'passed', 'head': HEAD, 'tree': TREE, 'commands': results, 'roots': str(roots)})
except BaseException as error:
    save('result.json', {'result': 'incomplete', 'head': HEAD, 'tree': TREE, 'error': str(error), 'commands': results})
    raise

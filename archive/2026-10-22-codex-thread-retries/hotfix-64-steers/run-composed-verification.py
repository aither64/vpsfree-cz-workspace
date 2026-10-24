#!/usr/bin/env python3
"""Exact reviewed downstream verification/builds. Does not deploy."""
import json
import os
from pathlib import Path
import re
import subprocess
import time

TRACK = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries')
GROUP = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries')
W, C = GROUP / 'workspace', GROUP / 'vpsfree-cz-configuration'
RUN = TRACK / 'hotfix-64-steers/verification-composed-7feaa9e1'
EXPECTED = {W: ('0a1d20e7430b93ba1afff32dc385ff9e0f7a5904', '3cdb39ca2977cf1acc26ecd787f3c4c881543ffd'),
            C: ('7feaa9e166ec8f474cf3628029e50ac02cc824b0', '6714b2ae4bd3736d334a0129dc07715f968feee7')}
CHECKS = {W: ['deployment-contract', 'agent-instructions', 'agent-team-policy', 'cluster-provider-composition'],
          C: ['nix-store-cleanup', 'alert-recipients', 'infra-monitoring-rules', 'infra-monitoring-config',
              'vpsf-status-prometheus-rules', 'vps-autostart-prometheus-rules',
              'process-count-prometheus-rules', 'newadmin-prometheus-rules']}
MACHINE = 'cz.vpsfree/machines/aitherdev'
env = os.environ.copy()
env.update(DEV_SESSION_SLUG='2026-10-22-codex-thread-retries', DEV_SESSION_WORKSPACE='/home/aither/workspace/ai/vpsfree.cz', TMPDIR='/tmp', CONFCTL_TTY='0')
os.umask(0o077)
RUN.mkdir()
results = []
roots = Path('/nix/var/nix/gcroots/per-user/aither/thread-retries-hotfix-composed-7feaa9e1')
roots.mkdir()

def save(name, value):
    (RUN / name).write_text(json.dumps(value, indent=2) + '\n')

def command(label, args, cwd, extra=None):
    command_env = env | (extra or {})
    save(label + '.command.json', {'command': args, 'cwd': str(cwd), 'extraEnvironment': extra or {}})
    started = time.monotonic()
    with (RUN / (label + '.stdout')).open('wb') as out, (RUN / (label + '.stderr')).open('wb') as err:
        completed = subprocess.run(args, cwd=cwd, env=command_env, stdout=out, stderr=err)
    record = {'label': label, 'exit': completed.returncode, 'elapsed': time.monotonic() - started}
    results.append(record)
    save(label + '.status.json', record)
    print(json.dumps(record), flush=True)
    if completed.returncode:
        raise RuntimeError('command failed: ' + label)
    return (RUN / (label + '.stdout')).read_text()

def identity(label, source):
    head, tree = EXPECTED[source]
    assert not command(label + '-status', ['git', 'status', '--porcelain'], source).strip()
    assert command(label + '-head', ['git', 'rev-parse', 'HEAD'], source).strip() == head
    assert command(label + '-tree', ['git', 'rev-parse', 'HEAD^{tree}'], source).strip() == tree

try:
    assert command('session', ['dev-session', 'current'], TRACK).strip() == '2026-10-22-codex-thread-retries'
    for key in ('DEV_SESSION_SLUG', 'DEV_SESSION_WORKSPACE'):
        assert key not in os.environ or os.environ[key] == env[key]
    for source in (W, C):
        name = 'W' if source == W else 'C'
        identity(name + '-before', source)
        (RUN / (name + '-flake.lock')).write_bytes((source / 'flake.lock').read_bytes())
        command(name + '-metadata', ['nix', 'flake', 'metadata', '--json', '--no-write-lock-file', str(source)], source)
        mapping = json.loads(command(name + '-selectors', ['nix', 'eval', '--json', '--no-write-lock-file',
                 str(source) + '#checks.x86_64-linux', '--apply',
                 'checks: builtins.mapAttrs (_: drv: { drv = drv.drvPath; output = drv.outPath; }) checks'], source))
        assert set(mapping) == set(CHECKS[source]), sorted(mapping)
        for selector, entry in mapping.items():
            assert Path(entry['drv']).exists(), entry
            (roots / (name + '-' + selector)).symlink_to(entry['drv'])
        selectors = [str(source) + '#checks.x86_64-linux.' + n for n in CHECKS[source]]
        command(name + '-input-graph', ['nix', 'derivation', 'show', '--recursive', '--no-write-lock-file'] + selectors, source)
        command(name + '-flakecheck', ['nix', 'flake', 'check', '--no-build', '--no-write-lock-file', '--print-build-logs'], source)
        built = json.loads(command(name + '-checks', ['nix', 'build', '--no-write-lock-file', '--print-build-logs', '--json', '--out-link', str(RUN / (name + '-checks-output'))] + selectors, source))
        outputs = sorted({p for row in built for p in row['outputs'].values()})
        command(name + '-output-closures', ['nix', 'path-info', '--json', '--recursive'] + outputs, source)
    package_selector = str(W) + '#packages.x86_64-linux.default'
    command('profile-input-graph', ['nix', 'derivation', 'show', '--recursive', '--no-write-lock-file', package_selector], W)
    package = json.loads(command('profile-build', ['nix', 'build', '--no-write-lock-file', '--print-build-logs', '--json', '--out-link', str(RUN / 'workspace-package'), package_selector], W))
    assert len(package) == 1
    profile = package[0]['outputs']['out']
    (roots / 'profile').symlink_to(package[0]['drvPath'])
    command('profile-output-closure', ['nix', 'path-info', '--json', '--recursive', profile], W)
    cenv = {'BUNDLE_GEMFILE': str(C / 'Gemfile'), 'BUNDLE_APP_CONFIG': str(C / '.bundle'), 'BUNDLE_PATH': str(C / '.gems')}
    raw = command('system-build', ['nix', 'develop', str(C), '-c', 'confctl', '--color', 'never', 'build', '--yes', MACHINE], C, cenv)
    names = re.findall(r'Built generations:\s*\n(\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2})\s*\n\s+cz\.vpsfree/machines/aitherdev', raw)
    assert len(names) == 1, names
    generation = names[0]
    command('generation-list', ['nix', 'develop', str(C), '-c', 'confctl', '--color', 'never', 'generation', 'ls', '--local', MACHINE, generation], C, cenv)
    directory = C / '.confctl/generations/cz.vpsfree:machines:aitherdev' / generation
    metadata = json.loads((directory / 'generation.json').read_text())
    assert metadata['mode'] == 'flakes'
    top = Path(metadata['toplevel'])
    rollback = Path(metadata['auto_rollback'])
    assert (directory / 'toplevel').resolve() == top.resolve()
    assert (directory / 'auto_rollback').resolve() == rollback.resolve()
    config = json.loads((top / 'etc/confctl/configuration-info.json').read_text())
    inputs = json.loads((top / 'etc/confctl/inputs-info.json').read_text())
    assert config['schemaVersion'] == 1 and config['revision'] == EXPECTED[C][0] and config['revisionDirty'] is False
    assert inputs == metadata['inputs_info']
    assert inputs['devWorkspace']['rev'] == 'ed2a75b98a75f9b37b7a359e9091a94e9846644e'
    save('system-build-receipt.json', {'generation': generation, 'directory': str(directory), 'metadata': metadata, 'configuration': config, 'inputs': inputs})
    for label, path in [('system', top), ('rollback', rollback)]:
        (RUN / label).symlink_to(path)
        drv = command(label + '-deriver', ['nix-store', '--query', '--deriver', str(path)], C).strip()
        assert drv.endswith('.drv') and Path(drv).exists(), drv
        (roots / label).symlink_to(drv)
        command(label + '-input-graph', ['nix', 'derivation', 'show', '--recursive', drv], C)
        command(label + '-output-closure', ['nix', 'path-info', '--json', '--recursive', str(path)], C)
    for source in (W, C):
        identity(('W' if source == W else 'C') + '-after', source)
    save('result.json', {'result': 'passed', 'sources': {str(k): list(v) for k, v in EXPECTED.items()},
         'generation': generation, 'profile': profile, 'toplevel': str(top), 'rollback': str(rollback), 'commands': results, 'roots': str(roots)})
except BaseException as error:
    save('result.json', {'result': 'incomplete', 'error': str(error), 'commands': results})
    raise

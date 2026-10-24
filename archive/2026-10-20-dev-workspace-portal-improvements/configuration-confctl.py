#!/usr/bin/env python3
"""Prepared rollout commands only; no phase runs without an explicit argv."""
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

WORKSPACE = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-20-dev-workspace-portal-improvements'
SESSION = WORKSPACE / 'work' / SLUG
TREES = WORKSPACE / 'worktrees' / SLUG
CONFIG = TREES / 'vpsfree-cz-configuration'
CONFIG_HEAD = '450e1ff538c1e94c1ec74f57b50fbe2efb31502b'
RUNTIME = 'f8f2938b4e2cfd6e5b82657d08f014357817808f'
SHARED = '852e8c51091512bc79ca6c921ef1f5ccc46a9535'
COMPOSED = '530038a8ee2bf6772144b07ca0cb02426fc1e6d6'
EXTENSION = '767dfd587e346168e1443e65ccdb67ce748f3fe3'
PREDECESSOR = '/nix/store/75w4s3zavi0g6z05scrb9ldck4lf2hfg-nixos-system-aitherdev-26.05.20261020.cd4ea8d'
SELECTED = '/nix/store/6bbjch8a42315qq855803c3y97knis2l-dev-workspace-0.2.0'
CONFCTL = '/nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl'
RUBY = '/nix/store/3rcm37q1arwggzjxzcnbiz5s8a7c1ppx-ruby-3.4.9'
HOST = 'cz.vpsfree/machines/aitherdev'
GENERATIONS = CONFIG / '.confctl/generations/cz.vpsfree:machines:aitherdev'
EVIDENCE = SESSION / 'verification/configuration-450e1ff5/deployment'
SSH = ['ssh', '-o', 'BatchMode=yes', '-o', 'StrictHostKeyChecking=yes',
       '-o', 'IdentitiesOnly=yes', '-o', 'ConnectTimeout=10',
       '-i', '/home/aither/.ssh/id_ed25519', 'root@172.16.106.40']


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def capture(argv, cwd=CONFIG):
    return subprocess.check_output(argv, cwd=cwd, text=True).strip()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def guards():
    require(('DEV_SESSION_SLUG' in os.environ) == ('DEV_SESSION_WORKSPACE' in os.environ),
            'incomplete session environment identity')
    for key, expected in [('DEV_SESSION_SLUG', SLUG), ('DEV_SESSION_WORKSPACE', str(WORKSPACE))]:
        require(key not in os.environ or os.environ[key] == expected, 'session environment mismatch')
    require(capture(['dev-session', 'current'], SESSION) == SLUG, 'current session mismatch')
    os.environ.update(DEV_SESSION_SLUG=SLUG, DEV_SESSION_WORKSPACE=str(WORKSPACE))
    for name, expected in [('vpsfree-cz-configuration', CONFIG_HEAD),
                           ('dev-workspace', RUNTIME), ('workspace', COMPOSED)]:
        tree = TREES / name
        require(capture(['git', 'rev-parse', 'HEAD'], tree) == expected, name + ' head changed')
        require(not capture(['git', 'status', '--porcelain'], tree), name + ' is dirty')
    require(str((Path.home() / '.local/state/dev-workspaces/profile').resolve()) == SELECTED,
            'selected profile changed; reconcile deployment preparation')
    for name, node in [('vpsfree-cz-configuration', 'devWorkspace'), ('workspace', 'dev-workspace')]:
        lock = json.loads((TREES / name / 'flake.lock').read_text())['nodes']
        require(lock[node]['locked']['rev'] == RUNTIME, 'runtime pin mismatch')
        require(lock[lock[node]['inputs']['codex-web']]['locked']['rev'] == SHARED, 'shared pin mismatch')
        if name == 'workspace':
            require(lock['vpsfree-dev-workspace']['locked']['rev'] == EXTENSION, 'extension pin mismatch')
    require(not os.environ.get('CONFCTL_SSH_CONFIG'), 'unexpected confctl SSH configuration override')
    os.environ['SSH_ASKPASS_REQUIRE'] = 'never'
    # Nix copy uses these explicit proven options. MachineControl retains its
    # proven ordinary configured root route. setsid + EOF prevents prompting.
    os.environ['NIX_SSHOPTS'] = '-o BatchMode=yes -o StrictHostKeyChecking=yes -o IdentitiesOnly=yes -o ConnectTimeout=10 -i /home/aither/.ssh/id_ed25519'


def confctl(log, *args):
    argv = ['setsid', '--wait', 'nix', 'develop', '--no-update-lock-file', '-c', CONFCTL, *args]
    log.write(('ARGV ' + json.dumps(argv) + '\n').encode())
    log.flush()
    subprocess.run(argv, cwd=CONFIG, stdin=subprocess.DEVNULL, stdout=log, stderr=log, check=True)


def root(name, target):
    path = EVIDENCE / 'roots' / name
    path.parent.mkdir(exist_ok=True)
    if path.is_symlink():
        require(str(path.resolve()) == target and Path(target).exists(), 'retained root mismatch: ' + name)
        return
    require(Path(target).exists(), 'missing prepared store path: ' + target)
    subprocess.run(['nix-store', '--add-root', str(path), '--indirect', '-r', target],
                   stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=True)


def metadata(toplevel):
    directory = Path(toplevel) / 'etc/confctl'
    configuration = json.loads((directory / 'configuration-info.json').read_text())
    inputs = json.loads((directory / 'inputs-info.json').read_text())
    require(configuration.get('schemaVersion') == 1 and configuration.get('revision') == CONFIG_HEAD
            and configuration.get('revisionDirty') is False, 'built configuration metadata mismatch')
    require(inputs.get('devWorkspace', {}).get('rev') == RUNTIME, 'built runtime metadata mismatch')
    return {'configuration': configuration, 'inputs': inputs}


def receipt():
    value = json.loads((EVIDENCE / 'generation-receipt.json').read_text())
    require(value['configurationHead'] == CONFIG_HEAD and value['runtime'] == RUNTIME
            and value['composedHead'] == COMPOSED and value['shared'] == SHARED, 'receipt source mismatch')
    name = value['generation']
    require(re.fullmatch(r'\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2}', name), 'invalid exact generation name')
    path = GENERATIONS / name / 'generation.json'
    require(digest(path) == value['generationJsonSha256'], 'generation metadata changed')
    generation = json.loads(path.read_text())
    require(generation['toplevel'] == value['toplevel'] and generation['auto_rollback'] == value['autoRollback'],
            'generation artifact mismatch')
    metadata(value['toplevel'])
    for field in ['toplevel', 'autoRollback']:
        require(re.fullmatch(r'/nix/store/[0-9a-z]{32}-[A-Za-z0-9+._?=-]+', value[field]),
                'invalid retained store path')
    return value


def claim():
    identity = os.environ.get('DEV_WORKSPACE_CLAIM_ID', '')
    require(re.fullmatch(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', identity),
            'exact held machine claim ID required')
    value = json.loads(capture(['dev-session', 'coordination', 'claim-status', SLUG,
                               '--as-is', '--id', identity, '--json'], SESSION))
    require(value['id'] == identity and value['state'] == 'held'
            and value['resources'] == ['machine:vpsfree:aitherdev']
            and value['request']['repositories'] == [], 'machine-only claim is not held')
    write_json(EVIDENCE / (PHASE + '-claim.json'), value)


def remote_proof(name, expected):
    # Nonsecret paths and configuration/input metadata only; no auth files.
    paths = capture(SSH + ['id -u; readlink -f /run/current-system; readlink -f /nix/var/nix/profiles/system']).splitlines()
    require(len(paths) == 3 and paths[0] == '0', 'root/system identity proof failed')
    proof = {'uid': 0, 'live': paths[1], 'profile': paths[2]}
    write_json(EVIDENCE / (name + '-system-paths.json'), proof)
    require(paths[1] == expected and paths[2] == expected, 'live/profile system selection mismatch; retain claim')
    for label, base in [('live', '/run/current-system'), ('profile', '/nix/var/nix/profiles/system')]:
        proof[label + 'Configuration'] = json.loads(capture(SSH + ['cat -- ' + base + '/etc/confctl/configuration-info.json']))
        proof[label + 'Inputs'] = json.loads(capture(SSH + ['cat -- ' + base + '/etc/confctl/inputs-info.json']))
    write_json(EVIDENCE / (name + '-system-proof.json'), proof)
    expected_config = CONFIG_HEAD if expected != PREDECESSOR else '37a338b25192d9271ee211110800c2dc6a094a57'
    expected_runtime = RUNTIME if expected != PREDECESSOR else '968646471b1190c16a8cf60ff50736cd0525fa3f'
    for label in ['live', 'profile']:
        cfg = proof[label + 'Configuration']
        require(cfg['revision'] == expected_config and cfg['revisionDirty'] is False
                and proof[label + 'Inputs']['devWorkspace']['rev'] == expected_runtime,
                'remote embedded source mismatch; retain claim')


def execute(log):
    if PHASE == 'build':
        root('confctl', str(Path(CONFCTL).parent.parent))
        root('ruby', RUBY)
        root('predecessor-system', PREDECESSOR)
        before = sorted(p.name for p in GENERATIONS.iterdir()) if GENERATIONS.exists() else []
        write_json(EVIDENCE / 'generation-names-before.json', before)
        confctl(log, 'build', '--yes', HOST)
        guards()
        confctl(log, 'generation', 'ls', '--local', HOST)
        # BuildList.current is set by this successful build, including an exact
        # output reuse. Resolve it once into an immutable named receipt.
        directory = (GENERATIONS / 'current').resolve(strict=True)
        require(directory.parent == GENERATIONS, 'build generation escaped expected directory')
        generation = json.loads((directory / 'generation.json').read_text())
        require(generation['mode'] == 'flakes', 'expected flake generation')
        proof = metadata(generation['toplevel'])
        require(generation['inputs_info']['devWorkspace']['rev'] == RUNTIME, 'generation input mismatch')
        store_paths = {'toplevel': generation['toplevel'], 'auto-rollback': generation['auto_rollback']}
        store_paths.update({'input-' + key: value for key, value in generation['inputs'].items()})
        for key, path in list(store_paths.items()):
            root(key, path)
        deriver = capture(['nix-store', '--query', '--deriver', generation['toplevel']])
        require(deriver.endswith('.drv') and Path(deriver).exists(), 'system derivation unavailable')
        root('toplevel-drv', deriver)
        (EVIDENCE / 'generation.json').write_bytes((directory / 'generation.json').read_bytes())
        result = {'configurationHead': CONFIG_HEAD, 'runtime': RUNTIME, 'shared': SHARED,
                  'composedHead': COMPOSED, 'generation': directory.name, 'generationDirectory': str(directory),
                  'generationJsonSha256': digest(directory / 'generation.json'),
                  'toplevel': generation['toplevel'], 'autoRollback': generation['auto_rollback'],
                  'deriver': deriver, 'roots': store_paths, 'embeddedMetadata': proof,
                  'generationExistedBeforeBuild': directory.name in before}
        write_json(EVIDENCE / 'generation-receipt.json', result)
        receipt()
        print('Prepared generation: ' + directory.name, flush=True)
        return
    prepared = receipt()
    if PHASE == 'copy':
        confctl(log, 'deploy', '--generation', prepared['generation'], '--copy-only', '--yes',
                '--no-interactive', '--no-reboot', HOST)
        # Verify actual copied immutable bytes without changing live selection.
        require(capture(SSH + ['set -eu; test -x ' + prepared['toplevel'] + '/bin/switch-to-configuration; test -e '
                               + prepared['autoRollback'] + '; printf copied']) == 'copied', 'copy proof failed')
        remote_proof('after-copy', PREDECESSOR)
        guards()
        return
    require(json.loads((EVIDENCE / 'copy-status.json').read_text())['state'] == 'passed', 'copy phase not verified')
    claim()
    remote_proof('before-' + PHASE, PREDECESSOR)
    if PHASE == 'dry':
        confctl(log, 'deploy', '--generation', prepared['generation'], '--no-reboot', '--yes',
                '--no-interactive', HOST, 'dry-activate')
        remote_proof('after-dry', PREDECESSOR)
    elif PHASE == 'switch':
        require(json.loads((EVIDENCE / 'dry-status.json').read_text())['state'] == 'passed', 'dry activation not verified')
        claim()
        confctl(log, 'deploy', '--generation', prepared['generation'], '--dry-activate-first',
                '--no-reboot', '--yes', '--no-interactive', HOST, 'switch')
        remote_proof('after-switch', prepared['toplevel'])
    guards()


if __name__ == '__main__':
    require(len(sys.argv) == 2 and sys.argv[1] in ['build', 'copy', 'dry', 'switch'],
            'usage: portal-improvements-confctl.py build|copy|dry|switch')
    PHASE = sys.argv[1]
    os.umask(0o077)
    guards()
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    with (EVIDENCE / 'driver.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        status_path = EVIDENCE / (PHASE + '-status.json')
        require(not status_path.exists(), 'phase already attempted; inspect retained evidence, no automatic retry')
        started = time.time()
        status = {'phase': PHASE, 'pid': os.getpid(), 'state': 'running',
                  'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'configurationHead': CONFIG_HEAD, 'runtime': RUNTIME, 'composedHead': COMPOSED}
        write_json(status_path, status)
        try:
            with (EVIDENCE / (PHASE + '.log')).open('wb', buffering=0) as log:
                execute(log)
            status.update(state='passed', exitCode=0)
        except BaseException as error:
            status.update(state='failed', error=type(error).__name__, exitCode=1)
            print('Phase failed; inspect phase log/status and reconcile effects before retry/release.', file=sys.stderr)
            raise
        finally:
            status['elapsedSeconds'] = round(time.time() - started, 3)
            write_json(status_path, status)

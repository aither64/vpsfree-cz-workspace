#!/usr/bin/env python3
"""Prepared parent-only profile mutation driver. No system activation or cleanup."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / 'candidate.json').read_text())
PROFILE = Path('/home/aither/.local/state/dev-workspaces/profile')
PENDING = Path('/home/aither/.local/state/dev-workspaces/codex/pending')
operation = None
phase = 'preflight'
child = None


def require(condition):
    if not condition:
        raise RuntimeError('guard_not_satisfied')


def read_json(path):
    return json.loads(Path(path).read_text())


def command(argv):
    return subprocess.check_output(argv, stderr=subprocess.PIPE, timeout=30).decode().strip()


def save(path, value):
    temporary = path.with_suffix(path.suffix + '.tmp')
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as output:
        output.write(json.dumps(value, indent=2) + '\n')
        output.flush()
        os.fsync(output.fileno())
    os.replace(temporary, path)


def effects():
    result = {'scope': 'user_profile_only', 'systemActivation': False,
              'deployedHostConfiguration': CFG['systemConfiguration'],
              'deployedHostRuntime': CFG['systemRuntime'],
              'contractRelation': 'mixed source revisions with equivalent host contract'}
    for name, path in [('selectedPackage', PROFILE), ('liveSystem', Path('/run/current-system')),
                       ('systemProfile', Path('/nix/var/nix/profiles/system'))]:
        try:
            result[name] = str(path.resolve(strict=True))
        except OSError:
            result[name] = None
    result['pendingReconciliationPresent'] = PENDING.exists() or PENDING.is_symlink()
    return result


def identity_guards():
    require(all(isinstance(head, str) and len(head) == 40 for head in CFG['sources'].values()))
    require(isinstance(CFG['candidate'], str) and isinstance(CFG['derivation'], str))
    require(command(['dev-session', 'current']) == CFG['slug'])
    slug, workspace = os.getenv('DEV_SESSION_SLUG'), os.getenv('DEV_SESSION_WORKSPACE')
    require((slug is None and workspace is None) or
            (slug == CFG['slug'] and workspace == CFG['workspace']))
    require(os.getenv('DEV_WORKSPACE_CLAIM_ID', CFG['claim']) == CFG['claim'])
    require(os.getenv('DEV_WORKSPACES_STATE', '/home/aither/.local/state/dev-workspaces') ==
            '/home/aither/.local/state/dev-workspaces')
    for repo, head in CFG['sources'].items():
        source = str(Path(CFG['sourceRoot']) / repo)
        require(command(['git', '-C', source, 'rev-parse', 'HEAD']) == head)
        require(command(['git', '-C', source, 'status', '--porcelain']) == '')
    require(str(PROFILE.resolve(strict=True)) == CFG['selected'])
    require(str(Path('/home/aither/bin/workspace-host').resolve(strict=True)) == CFG['selected'] + '/bin/workspace-host')
    require(not PENDING.exists() and not PENDING.is_symlink())
    for path in ['/run/current-system', '/nix/var/nix/profiles/system']:
        require(str(Path(path).resolve(strict=True)) == CFG['system'])
        require(read_json(Path(path) / 'etc/confctl/configuration-info.json')['revision'] == CFG['systemConfiguration'])
        require(read_json(Path(path) / 'etc/confctl/inputs-info.json')['devWorkspace']['rev'] == CFG['systemRuntime'])
    wlock = read_json(Path(CFG['sourceRoot']) / 'workspace/flake.lock')['nodes']
    clock = read_json(Path(CFG['sourceRoot']) / 'vpsfree-cz-configuration/flake.lock')['nodes']
    require(wlock['dev-workspace']['locked']['rev'] == CFG['sources']['dev-workspace'])
    require(clock['devWorkspace']['locked'] == wlock['dev-workspace']['locked'])
    require(wlock['codex-web']['locked']['rev'] == CFG['sources']['codex-web'])
    require(wlock['vpsfree-dev-workspace']['locked']['rev'] == '767dfd587e346168e1443e65ccdb67ce748f3fe3')


def evidence_guards():
    # Parent normalizes actual controller/utility results only after completion.
    # This local record binds evidence; it is not a new user-approval workflow.
    evidence = read_json(HERE / 'verification-gates.json')
    require(evidence['schema'] == 1 and evidence['state'] == 'passed')
    require(evidence['sources'] == CFG['sources'])
    require(evidence['candidate'] == CFG['candidate'] and evidence['derivation'] == CFG['derivation'])
    require(evidence['reviewDisposition'] == 'accepted_with_F1_and_pending_step9')
    require(evidence['coverage'] == {'firefoxReadBudget': True, 'componentCountEvidence': True, 'notificationDisabledEpoch': True, 'filesInline': True, 'filesArchiveRevive': True})
    require(evidence['withdrawnCoverage'] == {'native50': 'withdrawn_unverified', 'nativeDiscardRestore': 'withdrawn_unverified', 'extendedForegroundSoak': 'withdrawn_unverified'})
    require(set(evidence['artifacts']) == {'review', 'f1', 'pendingReview', 'step9', 'creationArchive', 'hostContract', 'packages', 'chromium', 'notifications', 'firefoxReadBudget', 'components', 'readBudgetReview', 'reusedEvidence', 'filesReview', 'filesBrowser', 'filesArchiveRevive'})
    tracking = Path(CFG['tracking']).resolve()
    for key, artifact in evidence['artifacts'].items():
        path = Path(artifact['path']).resolve(strict=True)
        require(path.is_relative_to(tracking) and path.is_file())
        with path.open('rb') as source:
            checksum = hashlib.file_digest(source, 'sha256').hexdigest()
        require(checksum == artifact['sha256'])
        if key in ['creationArchive', 'packages', 'chromium', 'notifications', 'firefoxReadBudget', 'filesBrowser', 'filesArchiveRevive']:
            require(artifact['exitCode'] == 0)
    roots = Path(CFG['roots'])
    require(str((roots / 'workspace').resolve(strict=True)) == CFG['candidate'])
    require(str((roots / 'workspace.drv').resolve(strict=True)) == CFG['derivation'])
    require(command(['nix-store', '--query', '--outputs', CFG['derivation']]) == CFG['candidate'])
    # No realization/build: require every completed stage's output and drv root.
    for label in ['workspace', 'agent-team-policy', 'runtime-generic-source', 'shared-default', 'shared-generic-source']:
        output, drv = (roots / label).resolve(strict=True), (roots / (label + '.drv')).resolve(strict=True)
        require(output.exists() and drv.is_file())
        command(['nix-store', '--check-validity', str(output), str(drv)])
        receipt = read_json(roots.parent / (label + '-derivation.json'))
        require(str(drv) in receipt and receipt[str(drv)]['outputs']['out']['path'] == str(output))


def package_guards():
    old, new = Path(CFG['selected']), Path(CFG['candidate'])
    for relative in ['share/workspace-portal/runtime-contract.json', 'share/dev-workspace/claim-contract.json',
                     'share/dev-workspace/coordination-contract.json', 'share/dev-workspace/integration-contract.json']:
        require(read_json(old / relative) == read_json(new / relative))
    runtime = read_json(new / 'share/workspace-portal/runtime-contract.json')
    require(runtime['livePackageSwitchPolicy'] == 1)
    before, after = [read_json(p / 'share/dev-workspace/package.json') for p in [old, new]]
    for key in ['schema', 'routerSocket', 'userNamespace', 'integration', 'activationEnvironmentAliases']:
        require(before[key] == after[key])
    require(after['schema'] == 1 and after['userNamespace'] == 'dev-workspaces')
    require(after['routerSocket'] == '/run/dev-workspaces/router.sock')
    before, after = [read_json(p / 'share/dev-workspace/coordination.json') for p in [old, new]]
    for key in ['schema', 'machines', 'profileMachine']:
        require(before[key] == after[key])
    require(after['profileMachine'] == 'vpsfree:aitherdev')
    require(read_json(new / 'share/dev-workspace/repository-claim-contract.json') == {'schema': 1, 'registeredRepositories': True})
    for relative in ['libexec/codex/bin/codex', 'libexec/codex/libexec/codex/bin/codex']:
        require((old / relative).resolve(strict=True) == (new / relative).resolve(strict=True))


def claim_guard(label):
    claim = json.loads(command(['dev-session', 'coordination', 'claim-status', CFG['slug'], '--as-is', '--id', CFG['claim'], '--json']))
    require(claim['state'] == 'held' and claim['resources'] == ['machine:vpsfree:aitherdev'])
    require(claim['request']['repositories'] == [])
    if 'id' in claim:
        require(claim['id'] == CFG['claim'])
    save(operation / ('claim-' + label + '.json'), claim)


def smoke(which):
    environment = dict(os.environ, NODE_PATH=CFG['nodePath'], PLAYWRIGHT_BROWSERS_PATH=CFG['browsers'],
                       DEV_SESSION_SLUG=CFG['slug'], DEV_SESSION_WORKSPACE=CFG['workspace'])
    for name in ['DEBUG', 'PWDEBUG', 'NODE_DEBUG']:
        environment.pop(name, None)
    with (operation / (which + '-smoke.log')).open('xb') as output:
        result = subprocess.run([CFG['node'], str(HERE / 'continuity-diagnostic.cjs'), which, str(operation)],
                                env=environment, stdin=subprocess.DEVNULL, stdout=output, stderr=output, timeout=180)
    require(result.returncode == 0)
    require(read_json(operation / ('continuity-' + which + '.json'))['state'] == 'passed')


def main():
    global operation, phase, child
    os.umask(0o077)
    identity_guards()
    evidence_guards()
    package_guards()
    operation = HERE / 'attempts' / str(uuid.uuid4())
    operation.mkdir(parents=True, mode=0o700)
    save(HERE / 'latest-attempt.json', {'path': str(operation), 'scope': 'user_profile_only'})
    claim_guard('before')
    phase = 'before'
    save(operation / 'status.json', {'state': 'running', 'phase': phase})
    smoke('before')  # Fresh complete updated roster/settings/process/attempt baseline.
    identity_guards()
    require(time.time() - (operation / 'continuity-before.json').stat().st_mtime < 120)
    claim_guard('pre-switch')
    phase = 'profile-switch'
    argv = ['/home/aither/bin/workspace-host', 'switch', '--source', str(Path(CFG['sourceRoot']) / 'workspace')]
    save(operation / 'status.json', {'state': 'running', 'phase': phase, 'argv': argv, 'effectsBefore': effects()})
    environment = dict(os.environ, DEV_SESSION_SLUG=CFG['slug'], DEV_SESSION_WORKSPACE=CFG['workspace'], DEV_WORKSPACE_CLAIM_ID=CFG['claim'])
    started = time.monotonic()
    # Drain and hash normal command output; never print/store unknown identifiers
    # or arguments. The normal package journals retain recovery diagnostics.
    process = subprocess.Popen(argv, env=environment, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    child = process
    save(operation / 'command.json', {'driverPID': os.getpid(), 'commandPID': process.pid, 'argv': argv,
                                     'startedAt': time.time(), 'claim': CFG['claim']})
    output_hash, output_bytes = hashlib.sha256(), 0
    for chunk in iter(lambda: process.stdout.read(65536), b''):
        output_hash.update(chunk)
        output_bytes += len(chunk)
    code = process.wait()
    save(operation / 'switch-result.json', {'exitCode': code, 'elapsedSeconds': round(time.monotonic() - started, 3),
                                         'outputSha256': output_hash.hexdigest(), 'outputBytes': output_bytes, 'effects': effects()})
    require(code == 0 and str(PROFILE.resolve(strict=True)) == CFG['candidate'])
    require(not PENDING.exists() and not PENDING.is_symlink())
    phase = 'after'
    save(operation / 'status.json', {'state': 'running', 'phase': phase, 'effects': effects()})
    smoke('after')
    claim_guard('after')
    final_effects = effects()
    require(final_effects['selectedPackage'] == CFG['candidate'])
    require(final_effects['liveSystem'] == final_effects['systemProfile'] == CFG['system'])
    require(not final_effects['pendingReconciliationPresent'])
    result = {'state': 'passed', 'phase': 'complete', 'effects': final_effects, 'scope': 'user_profile_only',
              'humanUIAcceptance': False, 'machineReleased': False, 'namingTurnVerified': False}
    save(operation / 'result.json', result)
    save(operation / 'status.json', result)
    print(json.dumps({'state': 'passed', 'scope': 'user_profile_only', 'continuity': True, 'systemUnchanged': True}))


if __name__ == '__main__':
    try:
        main()
    except BaseException:
        # This includes interruption: never infer rollback or run automatic retry.
        result = {'state': 'requires_reconciliation' if phase in ['profile-switch', 'after'] else 'not_confirmed',
                  'phase': phase, 'effects': effects(), 'automaticRecovery': False, 'machineReleased': False,
                  'ownedCommandMayStillRun': child is not None and child.poll() is None}
        if operation:
            save(operation / 'result.json', result)
            save(operation / 'status.json', result)
        print(json.dumps({'state': result['state'], 'phase': phase, 'reason': 'inspect_original_effects_and_forward_recovery'}))
        sys.exit(1)

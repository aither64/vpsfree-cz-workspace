#!/usr/bin/env python3
"""Prepared real Git target-movement fixture; writes only its owned local fixture."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('c_verification', HERE / 'package-c-r-post-review.py')
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)

INITIAL = '9d63ab4f30929043b8695225c0128029b188a985'
STALE_TIP = 'cc40679d267165aecfa569128438bb55fe910268'
MANUAL_PIN = '5436d3d7c36d3d5174eab3c44e3578830749d3db'


def lock(revision):
    # This raw GitHub source has no nested flake graph. NAR fields are optional
    # to the read-only graph checker; the fixture never asks Nix to fetch it.
    return {'version': 7, 'root': 'root', 'nodes': {
        'root': {'inputs': {'fixture': 'source'}},
        'source': {'flake': False, 'locked': {
            'type': 'github', 'owner': 'vpsfreecz', 'repo': 'confctl', 'rev': revision}}}}


def perform(op):
    if not os.environ.get('GITHUB_TOKEN'):
        raise ValueError('Supply GITHUB_TOKEN through private environment')
    if op.manifest['provider_head'] != MANUAL_PIN:
        raise ValueError('Provider fixture revision differs from reviewed manifest')
    op.receipt.update(fixture_script_sha256=driver.sha(__file__),
                      revisions={'initial': INITIAL, 'stale_tip': STALE_TIP, 'manual_pin': MANUAL_PIN},
                      candidate_supplier='Deterministic lock fixture; live Nix generation is a separate check')
    locks = {}
    for name, revision in [('initial', INITIAL), ('stale', STALE_TIP), ('manual', MANUAL_PIN)]:
        path = op.out / (name + '.lock')
        path.write_text(json.dumps(lock(revision), indent=2) + '\n')
        locks[name] = path
    op.receipt['lock_sha256'] = {name: driver.sha(path) for name, path in locks.items()}
    canonical = Path(op.manifest['workspace']) / 'repos/confctl.git'
    for old, new in [(INITIAL, STALE_TIP), (STALE_TIP, MANUAL_PIN)]:
        op.run(['git', '--git-dir=' + str(canonical), 'merge-base', '--is-ancestor', old, new],
               label='immutable-source-ancestry-witness')

    def expected(argv, status, cwd, label):
        try:
            result = op.run(argv, cwd=cwd, label=label)
        except driver.Failed as error:
            if error.status != status or op.kernel:
                raise
            op.receipt['commands'][-1]['expected_exit_status'] = status
            op.save()
            return Path(op.receipt['commands'][-1]['stdout'])
        if status:
            raise ValueError(f'{label} unexpectedly succeeded; expected {status}')
        return result

    def check(old, new, repo, status, label):
        return expected(['nix', 'shell', op.manifest['provider_flake'], '-c', 'confctl',
                         'inputs', 'check-update', '--old-lock', str(old), '--new-lock', str(new)],
                        status, repo, label)

    def git(repo, *args, label):
        return op.run(['git', *args], cwd=repo, label=label)

    def head(repo):
        return git(repo, 'rev-parse', 'HEAD', label='fixture-head').read_text().strip()

    remote = op.out / 'remote.git'
    op.run(['git', 'init', '--bare', '--initial-branch=master', str(remote)], label='init-local-bare-remote')

    def clone(name):
        repo = op.out / name
        op.run(['git', 'clone', str(remote), str(repo)], label='clone-local-' + name)
        git(repo, 'config', 'user.name', 'Guard race fixture', label='fixture-author-name')
        git(repo, 'config', 'user.email', 'guard-race@example.invalid', label='fixture-author-email')
        actual_remote = git(repo, 'remote', 'get-url', '--push', 'origin',
                            label='fixture-local-push-target').read_text().strip()
        if actual_remote != str(remote):
            raise ValueError('Fixture push target is not its exact owned local bare repository')
        return repo

    def commit(repo, selected_lock, subject):
        (repo / 'flake.lock').write_bytes(selected_lock.read_bytes())
        git(repo, 'add', '--', 'flake.nix', 'flake.lock', label='stage-fixture-lock')
        message = op.out / (repo.name + '-commit.txt')
        message.write_text(subject + '\n')
        git(repo, 'commit', '-F', str(message), label='commit-fixture-lock')
        return head(repo)

    def target():
        return op.run(['git', '--git-dir=' + str(remote), 'rev-parse', 'refs/heads/master'],
                      label='local-remote-target').read_text().strip()

    seed = clone('seed')
    (seed / 'flake.nix').write_text('{ outputs = { self }: {}; }\n')
    initial_head = commit(seed, locks['initial'], 'fixture: initial lock')
    git(seed, 'push', 'origin', 'HEAD:master', label='publish-initial-to-local-fixture-only')
    stale = clone('stale-updater')
    manual = clone('manual-writer')
    old_lock = op.out / 'stale-original.lock'
    old_lock.write_bytes((stale / 'flake.lock').read_bytes())
    check(old_lock, locks['stale'], stale, 0, 'accept-original-candidate')
    stale_head = commit(stale, locks['stale'], 'fixture: stale automated candidate')
    committed = git(stale, 'show', 'HEAD:flake.lock', label='stale-committed-lock')
    check(old_lock, committed, stale, 0, 'accept-original-committed-blob')

    manual_head = commit(manual, locks['manual'], 'fixture: concurrent manual pin')
    git(manual, 'push', 'origin', 'HEAD:master', label='advance-local-target-with-manual-pin')
    if target() != manual_head:
        raise ValueError('Manual target advancement was not recorded')
    rejected = expected(['git', 'push', '--porcelain', 'origin', 'HEAD:master'], 1, stale,
                        'ordinary-stale-push-must-reject')
    if '[rejected]' not in rejected.read_text() or target() != manual_head:
        raise ValueError('Ordinary stale push did not preserve the manual target')

    fresh = clone('fresh-updater')
    if head(fresh) != manual_head:
        raise ValueError('Fresh run did not start from the manual pin')
    fresh_baseline = op.out / 'fresh-original.lock'
    fresh_baseline.write_bytes((fresh / 'flake.lock').read_bytes())
    index_before = git(fresh, 'ls-files', '--stage', '-z', label='fresh-original-index').read_bytes()
    regenerated = op.out / 'fresh-regenerated-candidate.lock'
    regenerated.write_bytes(locks['stale'].read_bytes())
    check(fresh_baseline, regenerated, fresh, 3, 'fresh-baseline-rejects-old-channel-tip')
    check(fresh_baseline, locks['manual'], fresh, 0, 'equal-manual-pin-is-retained')
    if (head(fresh) != manual_head or target() != manual_head or
            (fresh / 'flake.lock').read_bytes() != fresh_baseline.read_bytes() or
            git(fresh, 'ls-files', '--stage', '-z', label='fresh-final-index').read_bytes() != index_before or
            git(fresh, 'status', '--porcelain', label='fresh-final-status').read_text().strip()):
        raise ValueError('Fresh run modified or published over the manual pin')
    op.receipt.update(initial_target=initial_head, stale_candidate_head=stale_head,
                      manual_target=manual_head, final_target=target(),
                      stale_push_rejected=True, fresh_baseline_rejected_stale_tip=True,
                      fresh_lock_index_head_preserved=True, fresh_index_sha256=hashlib.sha256(index_before).hexdigest(),
                      complete=True, exit_status=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--review-receipt', required=True)
    args = parser.parse_args()
    args.stage = 'git-race'
    args.project = None
    op = driver.Operation(args)
    try:
        perform(op)
        return 0
    except driver.Failed as error:
        op.receipt.update(exit_status=error.status, failed_command=str(error), kernel_escalation=op.kernel)
        return error.status
    except Exception as error:
        op.receipt.update(exit_status=1, fixture_error=str(error), kernel_escalation=op.kernel)
        return 1
    finally:
        op.receipt['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        op.save()
        print('Receipt:', op.out / 'receipt.json', flush=True)


if __name__ == '__main__':
    sys.exit(main())

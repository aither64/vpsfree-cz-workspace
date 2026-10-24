#!/usr/bin/env python3
"""Authorized exact reviewed feature publication; no default mutation or retry."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
SLUG = HERE.name
REVIEW_SHA = '6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd'
INVENTORY_SHA = 'd3af5016f23f620df83c990840dccbb1f82faa2eb2ce43beb3cffbe85a4fdd66'
PROVIDER = '822c0e35dbe2549111912f539116b4225dfd3035'
OUT = HERE / 'verification/c7-git-cache-publication'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=['preflight', 'publish'])
    parser.add_argument('project', nargs='?')
    parser.add_argument('--receipt-name')
    args = parser.parse_args()
    inventory_path = HERE / 'package-c7-final-source-inventory.json'
    assert sha(inventory_path) == INVENTORY_SHA
    assert sha(HERE / 'review-git-cache-report.md') == REVIEW_SHA
    inventory = json.loads(inventory_path.read_text())
    assert subprocess.check_output(['/home/aither/bin/dev-session', 'current'], cwd=WORKSPACE, text=True).strip() == SLUG
    assert [os.environ.get(k) for k in ('DEV_SESSION_SLUG', 'DEV_SESSION_WORKSPACE')] in ([None, None], [SLUG, str(WORKSPACE)])
    provider_proof = HERE / 'verification/git-cache-publication/published.json'
    proof = json.loads(provider_proof.read_text())
    assert proof['provider_head'] == PROVIDER and proof['review_sha256'] == REVIEW_SHA
    assert proof['preserved_r_before_feature_push']['preservation_verified_before_feature_push']
    OUT.mkdir(exist_ok=True)
    name = args.receipt_name or ('preflight' if args.stage == 'preflight' else args.project)
    assert name
    assert '/' not in name and '..' not in name
    receipt_path = OUT / (name + '.json')
    assert not receipt_path.exists(), 'Existing attempt requires diagnosis; never retry automatically'
    receipt = {'stage': args.stage, 'project': args.project, 'review_sha256': REVIEW_SHA,
               'source_inventory_sha256': INVENTORY_SHA, 'provider_publication_sha256': sha(provider_proof),
               'provider_head': PROVIDER, 'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               'commands': [], 'complete': False}

    def save():
        receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')

    def run(argv, label, cwd=WORKSPACE):
        n = len(receipt['commands']) + 1
        stdout, stderr = OUT / f'{name}-{n:02d}-{label}.stdout', OUT / f'{name}-{n:02d}-{label}.stderr'
        print(name + ': ' + label, flush=True)
        started = time.monotonic()
        with stdout.open('xb') as out, stderr.open('xb') as err:
            process = subprocess.Popen(argv, cwd=cwd, stdout=out, stderr=err, start_new_session=True)
            record = {'argv': argv, 'cwd': str(cwd), 'pid': process.pid, 'pgid': process.pid,
                      'stdout': str(stdout), 'stderr': str(stderr), 'label': label}
            receipt['commands'].append(record); save()
            status = process.wait()
        record.update(exit_status=status, elapsed_seconds=round(time.monotonic() - started, 3),
                      stdout_sha256=sha(stdout), stderr_sha256=sha(stderr)); save()
        assert status == 0, label + ' failed; inspect captured effects before another operation'
        return stdout.read_text()

    def local(item):
        cwd = Path(item['worktree'])
        head = run(['git', 'rev-parse', 'HEAD'], item['project'] + '-head', cwd).strip()
        tree = run(['git', 'rev-parse', 'HEAD^{tree}'], item['project'] + '-tree', cwd).strip()
        status = run(['git', 'status', '--porcelain=v1'], item['project'] + '-clean', cwd)
        lock = run(['git', 'rev-parse', 'HEAD:flake.lock'], item['project'] + '-lock', cwd).strip()
        assert head == item['head'] and tree == item['tree'] and not status and lock == item['flake_lock_objects']['final']
        return {'head': head, 'tree': tree, 'clean': True, 'lock_blob': lock}

    def remote(item, expected_feature):
        repo = WORKSPACE / 'repos' / (item['project'] + '.git')
        remote_url = run(['git', '--git-dir=' + str(repo), 'remote', 'get-url', 'origin'], item['project'] + '-origin').strip()
        assert remote_url == 'git@github.com:vpsfreecz/' + item['project'] + '.git'
        raw = run(['git', '--git-dir=' + str(repo), 'ls-remote', '--symref', 'origin', 'HEAD',
                   'refs/heads/' + item['target'], 'refs/heads/' + SLUG], item['project'] + '-ssh')
        refs = {line.split()[1]: line.split()[0] for line in raw.splitlines() if not line.startswith('ref:')}
        expected_target = '1103a3a14b1dc6dec17fc4859df80220a54f111d' if item['project'] == 'haveapi' else item['base']
        receipt.setdefault('remote_observations', []).append({'project': item['project'], 'refs': refs,
                       'expected_feature': expected_feature, 'expected_target': expected_target,
                       'haveapi_target_divergence_deferred': item['project'] == 'haveapi'})
        save()
        assert refs['refs/heads/' + item['target']] == expected_target, 'Target moved; stop and report before repair'
        assert refs['refs/heads/' + SLUG] == expected_feature, 'Feature lease moved; stop and report before repair'
        return refs

    save()
    try:
        provider_refs = run(['git', 'ls-remote', 'git@github.com:vpsfreecz/confctl.git', 'refs/heads/' + SLUG,
                             'refs/heads/' + SLUG + '-provider-r-evidence'], 'provider-first-fresh-ssh')
        refs = {line.split()[1]: line.split()[0] for line in provider_refs.splitlines()}
        assert refs['refs/heads/' + SLUG] == PROVIDER
        assert refs['refs/heads/' + SLUG + '-provider-r-evidence'] == '5436d3d7c36d3d5174eab3c44e3578830749d3db'
        receipt['provider_first_fresh_ssh_verified'] = True
        if args.stage == 'preflight':
            receipt['projects'] = []
            for item in inventory['projects']:
                state = local(item)
                repo = WORKSPACE / 'repos' / (item['project'] + '.git')
                run(['git', '--git-dir=' + str(repo), 'fetch', '--no-tags', 'origin',
                     '+refs/heads/' + item['target'] + ':refs/remotes/origin/' + item['target'],
                     '+refs/heads/' + SLUG + ':refs/remotes/origin/' + SLUG], item['project'] + '-fetch-ssh')
                refs = remote(item, item['expected_published_lease'])
                receipt['projects'].append({'project': item['project'], 'local': state, 'remote': refs})
        else:
            initial = json.loads((OUT / 'preflight.json').read_text())
            assert initial['complete'] and initial['exit_status'] == 0 and initial['review_sha256'] == REVIEW_SHA
            item = next(i for i in inventory['projects'] if i['project'] == args.project)
            receipt.update(base=item['base'], head=item['head'], previous_feature_lease=item['expected_published_lease'])
            receipt['before'] = local(item)
            remote(item, item['expected_published_lease'])
            run(['nix', 'develop', '--no-write-lock-file', '-c', 'git', 'push',
                 '--force-with-lease=refs/heads/' + SLUG + ':' + item['expected_published_lease'],
                 'origin', 'HEAD:refs/heads/' + SLUG], 'ordinary-declared-shell-exact-lease-push', Path(item['worktree']))
            receipt['published_remote'] = remote(item, item['head'])
            receipt['after'] = local(item)
            assert receipt['before'] == receipt['after']
            run(['/home/aither/bin/dev-session', 'worktree', 'capture-comparison', SLUG, item['project'], '--as-is',
                 '--base', item['base'], '--head', item['head']], 'capture-exact-final-comparison')
        receipt.update(complete=True, exit_status=0)
    except Exception as error:
        receipt.update(exit_status=1, failure_class=type(error).__name__, failed_assertion=str(error))
        raise
    finally:
        receipt['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()); save()
        print('Receipt:', receipt_path, flush=True)


if __name__ == '__main__':
    main()

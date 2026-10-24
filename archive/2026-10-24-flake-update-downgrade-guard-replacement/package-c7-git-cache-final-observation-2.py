#!/usr/bin/env python3
"""One authorized read-only C7 source/ref/CI observation; no waits or mutations."""
import hashlib
import json
from pathlib import Path
import subprocess
import time

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
SLUG = HERE.name
OUT = HERE / 'verification/c7-git-cache-final-observation-2'
REVIEW_SHA = '6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd'
INVENTORY_SHA = '821181a5dad2340b149f1013846cf1430c8373bec8258c881da49caf6bc833ab'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    review = HERE / 'review-git-cache-report.md'
    reviewed_path = HERE / 'git-rework-final-source-inventory.json'
    assert digest(review.read_bytes()) == REVIEW_SHA
    assert digest(reviewed_path.read_bytes()) == INVENTORY_SHA
    reviewed = json.loads(reviewed_path.read_text())
    owners = json.loads((HERE / 'package-c7-final-source-inventory.json').read_text())
    assert reviewed['ready_for_review']
    OUT.mkdir()
    result = {'observed_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
              'review_sha256': REVIEW_SHA, 'reviewed_inventory_sha256': INVENTORY_SHA,
              'scope': 'One read-only final C7 source/SSH-ref/CI observation; no runtime or active cache access',
              'source_or_ref_mutations': False, 'ci_wait_dispatch_rerun_cancel': False,
              'repositories': [], 'commands': [], 'complete': False}
    def save():
        (OUT / 'receipt.json').write_text(json.dumps(result, indent=2) + '\n')
    def run(argv, label, cwd=WORKSPACE, permit_failure=False):
        stdout, stderr = OUT / (label + '.stdout'), OUT / (label + '.stderr')
        process = subprocess.run(argv, cwd=cwd, capture_output=True)
        stdout.write_bytes(process.stdout); stderr.write_bytes(process.stderr)
        result['commands'].append({'argv': argv, 'cwd': str(cwd), 'label': label,
                                   'exit_status': process.returncode, 'stdout': str(stdout), 'stderr': str(stderr),
                                   'stdout_sha256': digest(process.stdout), 'stderr_sha256': digest(process.stderr)})
        save()
        if not permit_failure:
            assert process.returncode == 0, label + ': inspect captured evidence before another action'
        return process.stdout, process.returncode
    save()
    for owner in owners['projects']:
        name = owner['project']; item = next(i for i in reviewed['sources'] if i['repository'] == name)
        cwd = Path(item['worktree'])
        def git(*args, suffix):
            return run(['git', '--no-optional-locks', '-c', 'core.fsmonitor=false', *args], name + '-' + suffix, cwd)[0]
        head = git('rev-parse', 'HEAD', suffix='head').decode().strip()
        tree = git('rev-parse', 'HEAD^{tree}', suffix='tree').decode().strip()
        status = git('status', '--porcelain=v1', suffix='status').decode()
        index = git('ls-files', '--stage', '-z', suffix='index')
        series = git('log', '--reverse', '--format=fuller', item['base'] + '..HEAD', suffix='series')
        commits = git('rev-list', '--reverse', item['base'] + '..HEAD', suffix='commits').decode().splitlines()
        patch = git('diff', '--no-ext-diff', '--binary', item['base'], 'HEAD', suffix='full-binary-diff')
        lock_blob = git('rev-parse', 'HEAD:flake.lock', suffix='lock-blob').decode().strip()
        lock_bytes = git('show', 'HEAD:flake.lock', suffix='head-lock')
        source_equal = (head == item['head'] and tree == item['tree'] and not status
                        and series.decode() == item['series'] and patch.decode() == item['final_diff']
                        and len(commits) == item['commit_count']
                        and commits == [c['sha'] for c in owner['series']]
                        and lock_blob == owner['flake_lock_objects']['final']
                        and (cwd / 'flake.lock').read_bytes() == lock_bytes)
        remote = 'git@github.com:vpsfreecz/' + name + '.git'
        canonical = WORKSPACE / 'repos' / (name + '.git')
        refs_raw, _ = run(['git', '--git-dir=' + str(canonical), 'ls-remote', '--symref', remote, 'HEAD',
                          'refs/heads/' + item['target'], 'refs/heads/' + SLUG], name + '-canonical-ssh-refs')
        refs = {line.split()[1]: line.split()[0] for line in refs_raw.decode().splitlines() if not line.startswith('ref:')}
        expected_target = '1103a3a14b1dc6dec17fc4859df80220a54f111d' if name == 'haveapi' else item['base']
        fields = 'databaseId,workflowName,name,headSha,headBranch,status,conclusion,url,event,createdAt,updatedAt'
        runs_raw, _ = run(['gh', 'run', 'list', '--repo', 'vpsfreecz/' + name, '--branch', SLUG, '--limit', '100',
                          '--json', fields], name + '-ci-list')
        current = [r for r in json.loads(runs_raw) if r['headSha'] == item['head'] and r['headBranch'] == SLUG]
        row = {'repository': name, 'base': item['base'], 'reviewed_head': item['head'], 'head': head,
               'tree': tree, 'clean': not status, 'index_sha256': digest(index), 'lock_blob': lock_blob,
               'working_lock_equals_head': (cwd / 'flake.lock').read_bytes() == lock_bytes,
               'series': commits, 'series_sha256': digest(series), 'full_binary_diff_sha256': digest(patch),
               'source_series_binary_diff_equals_review': source_equal, 'remote_refs': refs,
               'feature_equals_review': refs.get('refs/heads/' + SLUG) == item['head'],
               'expected_target': expected_target, 'target_matches_last_accepted': refs.get('refs/heads/' + item['target']) == expected_target,
               'haveapi_default_divergence_deferred': name == 'haveapi', 'exact_head_runs': current,
               'no_matching_head_runs': not current, 'failed_run_evidence': []}
        result['repositories'].append(row); save()
        for run_record in current:
            if run_record['status'] == 'completed' and run_record['conclusion'] in ('failure', 'timed_out', 'action_required', 'startup_failure'):
                ident = str(run_record['databaseId'])
                jobs, jobs_status = run(['gh', 'run', 'view', ident, '--repo', 'vpsfreecz/' + name,
                                         '--json', 'jobs,conclusion,status,headSha,url'], name + '-failed-' + ident + '-jobs', permit_failure=True)
                logs, logs_status = run(['gh', 'run', 'view', ident, '--repo', 'vpsfreecz/' + name, '--log-failed'],
                                        name + '-failed-' + ident + '-logs', permit_failure=True)
                row['failed_run_evidence'].append({'run_id': run_record['databaseId'], 'jobs_fetch_exit': jobs_status,
                                                   'logs_fetch_exit': logs_status, 'logs_sha256': digest(logs),
                                                   'owner_diagnosis_required': True})
                save()
        print(name + ': source=' + str(source_equal) + ', remote=' + str(row['feature_equals_review'])
              + ', target=' + str(row['target_matches_last_accepted']) + ', head CI=' + str(len(current)), flush=True)
    result['all_source_series_diffs_equal_review'] = all(r['source_series_binary_diff_equals_review'] for r in result['repositories'])
    result['all_remote_features_equal_review'] = all(r['feature_equals_review'] for r in result['repositories'])
    result['all_targets_match_last_accepted'] = all(r['target_matches_last_accepted'] for r in result['repositories'])
    result['complete'] = True; save()


if __name__ == '__main__':
    main()

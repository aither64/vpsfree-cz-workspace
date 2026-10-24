#!/usr/bin/env python3
"""Record the seven owned, committed consumer ranges without network operations."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-24-flake-update-downgrade-guard-replacement'
SESSION = ROOT / 'work' / SLUG
PIN = '822c0e35dbe2549111912f539116b4225dfd3035'
BASES = {
    'haveapi': '7ac977a26080d45d44b6608aafad2cadd2ec7f81',
    'terraform-provider-vpsadmin': '2a2c1055302f86f8e250f1d7e4c331d62012efe8',
    'vpsadminos': 'e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854',
    'vpsf-status': '587cd65bb02e6dddea7f6b6409e42a15f36ab4fb',
    'vpsfree-irc-bot': '94ac4eb5a7caf0456fff7df86a44cae198463276',
    'vpsfree-cz-configuration': '50d263d4127c05163d660fae1c4b9b887584032d',
    'vpsadminos-org-configuration': '6b04b48e9c076e5525ccb7c38ce174232414f0b5',
}
OWNED = {
    'haveapi': ['.github/workflows/update-nixpkgs.yml', 'doc/agent-instructions/development.md'],
    'terraform-provider-vpsadmin': ['.github/workflows/update-vpsadmin-flake.yml', 'README.md', 'tools/update-vpsadmin-flake-input.sh'],
    'vpsadminos': ['.github/workflows/flake-update.yml', 'README.md'],
    'vpsf-status': ['.github/workflows/update-dependencies.yml', 'README.md'],
    'vpsfree-irc-bot': ['.github/workflows/nixpkgs-update.yml', 'README.md', 'tools/update_nixpkgs_flake.sh'],
    'vpsfree-cz-configuration': ['.github/workflows/daily-update.yml'],
    'vpsadminos-org-configuration': ['.github/workflows/daily-update.yml'],
}


def git(worktree, *args):
    return subprocess.run(['git', '-C', str(worktree), *args], check=True, capture_output=True, text=True).stdout


def patch_id(worktree, commit):
    patch = git(worktree, 'show', '--format=', commit)
    return subprocess.run(['git', 'patch-id', '--stable'], input=patch, text=True, check=True, capture_output=True).stdout.split()[0]


starting = json.loads((SESSION / 'package-c7-cache-start-inventory.json').read_text())
folder = SESSION / 'package-c7-final-source'
folder.mkdir(exist_ok=False)
projects = []
for prior in starting['projects']:
    project = prior['project']
    worktree = ROOT / 'worktrees' / SLUG / project
    base = BASES[project]
    old = prior['head']
    head = git(worktree, 'rev-parse', 'HEAD').strip()
    tree = git(worktree, 'rev-parse', 'HEAD^{tree}').strip()
    assert not git(worktree, 'status', '--porcelain=v1'), project
    assert git(worktree, 'branch', '--show-current').strip() == SLUG
    git(worktree, 'merge-base', '--is-ancestor', base, head)
    assert git(worktree, 'rev-parse', prior['backup_ref']).strip() == old
    series = git(worktree, 'rev-list', '--reverse', base + '..' + head).splitlines()
    assert len(series) == (3 if project == 'vpsf-status' else 1), (project, series)
    subjects = [git(worktree, 'show', '-s', '--format=%s', c).strip() for c in series]
    assert not any(s.startswith(('fixup!', 'squash!', 'WIP')) for s in subjects)
    delta_paths = git(worktree, 'diff', '--name-only', old, head).splitlines()
    assert set(delta_paths) == set(OWNED[project]), (project, delta_paths)
    git(worktree, 'diff', '--check', base, head)
    lock_objects = {name: git(worktree, 'rev-parse', sha + ':flake.lock').strip()
                    for name, sha in [('base', base), ('R', old), ('final', head)]}
    assert len(set(lock_objects.values())) == 1
    assert git(worktree, 'rev-parse', old + ':flake.nix') == git(worktree, 'rev-parse', head + ':flake.nix')
    workflow = prior['workflow']
    content = (worktree / workflow).read_text()
    assert content.count('CONFCTL_FLAKE:') == 1 and content.count(PIN) == 1
    assert '5436d3d7c36d3d5174eab3c44e3578830749d3db' not in content
    assert 'if: ${{ !cancelled() }}' in content
    record_path = SESSION / ('package-c7-final-commit-' + project + '.json')
    if project == 'haveapi': record_path = SESSION / 'package-c7-final-commit-haveapi-3.json'
    commit_record = json.loads(record_path.read_text())
    assert tree == commit_record['expected_tree'], project
    files = {}
    for kind, args in [('full', ['diff', '--no-ext-diff', '--binary', base, head]),
                       ('from-R', ['diff', '--no-ext-diff', '--binary', old, head]),
                       ('range-diff', ['range-diff', base + '..' + old, base + '..' + head]),
                       ('series', ['log', '--reverse', '--format=fuller', base + '..' + head])]:
        p = folder / (project + '.' + kind + ('.patch' if kind in ('full', 'from-R') else '.txt'))
        p.write_text(git(worktree, *args))
        files[kind] = str(p.relative_to(SESSION))
    item = {'project': project, 'worktree': str(worktree), 'target': 'staging' if project == 'vpsadminos' else 'master',
            'base': base, 'old_R_head': old, 'expected_published_lease': old,
            'head': head, 'tree': tree, 'clean': True, 'index_clean': True,
            'series': [{'sha': c, 'subject': s} for c, s in zip(series, subjects)],
            'full_branch_paths': git(worktree, 'diff', '--name-only', base, head).splitlines(),
            'R_delta_paths': delta_paths, 'flake_lock_objects': lock_objects,
            'flake_nix_unchanged_from_R': True, 'intended_tree_preserved_by_consolidation': True,
            'backup_ref': prior['backup_ref'], 'workflow': workflow,
            'workflow_sha256': hashlib.sha256(content.encode()).hexdigest(),
            'documentation': [p for p in OWNED[project] if p.endswith('.md')],
            'hook_receipt': record_path.name, 'comparisons': files}
    if project == 'vpsf-status':
        old_independent = ['6b5e8a6089926112bfbb63a45413b886ee56e549', 'd4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa']
        item['independent_patch_provenance'] = []
        for before, after in zip(old_independent, series[1:]):
            a = patch_id(worktree, before); b = patch_id(worktree, after); assert a == b
            item['independent_patch_provenance'].append({'old': before, 'new': after, 'stable_patch_id': a, 'unchanged': True})
    projects.append(item)
    print(project, base, head, len(series), 'clean')
provider = ROOT / 'worktrees' / SLUG / 'confctl'
assert git(provider, 'rev-parse', 'HEAD').strip() == PIN
report = {'provider': PIN, 'provider_tree': git(provider, 'rev-parse', 'HEAD^{tree}').strip(),
          'phase': 'Committed, quick checks/hooks passed, ready for affected final review; publication held',
          'projects': projects, 'remote_proof': 'No new remote/default fetch; expected leases are accepted historical published R heads. Fresh SSH checks required at authorized publication.',
          'history_conclusion': 'One consolidated final adoption/pin stream per consumer. Status retains two independent baseline fixes after its adoption. No obsolete pin/fixup commits in final branch series.',
          'migrations': {'conclusion': 'no migrations', 'versions': [], 'production_deployment': 'none authorized or performed', 'R_consumption': 'Historical published feature CI/isolated verification evidence retained; exact R source refs and receipts preserved.'},
          'limits': ['Not independently reviewed yet.', 'No source publication or default integration.', 'No new actual package/live/VM checks.', 'HaveAPI later master1103 divergence consciously deferred; feature remains on accepted7ac base.'],
          'quick_receipt': 'package-c7-final-quick.json', 'action_receipt': 'package-c7-cache-actions.json'}
(SESSION / 'package-c7-final-source-inventory.json').write_text(json.dumps(report, indent=2) + '\n')
lines = ['# Final local consumer source inventory', '',
         'All seven final pins use `822c0e35dbe2549111912f539116b4225dfd3035`. Ordinary hooks and final-pin quick checks passed. Publication remains held for root final review.', '',
         '| Project | Base | Final head | Commits |', '| --- | --- | --- | --- |']
lines += [f"| {p['project']} | `{p['base']}` | `{p['head']}` | {len(p['series'])} |" for p in projects]
lines += ['', '[Full inventory and exact R leases](package-c7-final-source-inventory.json), [final quick receipt](package-c7-final-quick.json), and full/range/R-delta patches in `package-c7-final-source/` bind this packet.', '',
          'History: one final adoption per stream; status retains separate vendor-hash/Perl and metrics-test baseline fixes with identical stable patch IDs and unchanged intended final tree. No migrations. Locks and configuration deployment-tool pins are unchanged. Status retains its previously reviewed devShell/native-check Perl prerequisites; this rework does not change them.', '',
          'The R heads are preserved under each local `refs/backup/' + SLUG + '/before-git-cache-rework`. Earlier R reviews, failed/successful roots and receipts remain historical evidence. HaveAPI retains the accepted7ac base; later master1103 movement is deliberately deferred. No new remote proof or integration claim is made.', '',
          'HaveAPI ordinary hooks initially stopped at configuration/PythonChecks signature gates. Tracked configuration and both custom hooks were read and proved byte-identical reviewed74f, then signed through ordinary Overcommit commands; both failed attempts are preserved and the third amendment passed. Status initial sequence-editor preflight failed on a custom display instruction format before any rebase effects; HEAD/tree/index and absent rebase state were reconciled, then exact-SHA validation replaced display parsing and the bounded rebase completed. No hook bypass, custom index/worktree, stash or unrelated source repair.', '',
          'Runtime packet preparation follows source inventory acceptance. New selected-path checks will bind B same final package receipt/cache and omit unchanged dependency refresh/build/TF8; no new package/live/watcher/auth command ran here.', '',
          'Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/' + SLUG + '/']
(SESSION / 'package-c7-final-source-report.md').write_text('\n'.join(lines) + '\n')
print('saved package-c7-final-source-inventory.json and package-c7-final-source-report.md')

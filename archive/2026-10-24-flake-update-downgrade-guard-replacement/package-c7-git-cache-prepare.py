#!/usr/bin/env python3
"""Freeze selected workflow scripts and exact source blobs; never run an updater."""
import hashlib
import json
import os
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
SLUG = HERE.name
PROVIDER = '822c0e35dbe2549111912f539116b4225dfd3035'
FLAKE = f'github:vpsfreecz/confctl/{PROVIDER}#confctl'
MANIFEST = HERE / 'package-c7-git-cache-manifest.json'
SELECTED = {
    'haveapi': ['Save lock baseline', 'Configure git author', 'Update nixpkgs', 'Push update'],
    'terraform-provider-vpsadmin': ['Save lock baseline', 'Setup git', 'Update vpsAdmin input', 'Push update'],
    'vpsadminos': ['Save lock baseline', 'Update flake inputs', 'Commit and push changes'],
    'vpsf-status': ['Configure Git', 'Record starting revision', 'Update flake input',
                    'Check committed dependency updates', 'Push changes'],
    'vpsfree-irc-bot': ['Save lock baseline', 'Setup git', 'Update nixpkgs', 'Push updates'],
    'vpsfree-cz-configuration': ['Save input baseline', 'Setup git', 'Install git hooks',
                               'Update inputs', 'Update llm-agents when Codex changes', 'Check and push updates'],
    'vpsadminos-org-configuration': ['Save input baseline', 'Setup git', 'Install git hooks',
                                  'Update flake inputs', 'Check and push updates'],
}
GC_LINES = {
    'sudo mkdir "/nix/var/nix/gcroots/per-user/$USER"',
    'sudo chown "$USER" "/nix/var/nix/gcroots/per-user/$USER"',
    'sudo mkdir /nix/var/nix/gcroots/per-user/$USER',
    'sudo chown $USER /nix/var/nix/gcroots/per-user/$USER',
}
DEPENDENCY_STEPS = {'Update Go dependencies', 'Run tests', 'Build Nix package', 'Update package dependencies'}
EXTRA = {
    'haveapi': ['utils/update-nixpkgs.sh'],
    'terraform-provider-vpsadmin': ['tools/update-vpsadmin-flake-input.sh'],
    'vpsadminos': ['.github/workflows/scripts/flake-update-commit-message.rb'],
    'vpsfree-irc-bot': ['tools/update_nixpkgs_flake.sh'],
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(project, *args):
    return subprocess.check_output(['git', '--git-dir=' + str(WORKSPACE / 'repos' / (project + '.git')), *args])


def yaml(raw):
    # Only the parser is isolated from Bundler; real caller environments are preserved.
    env = {k: v for k, v in os.environ.items()
           if not (k.startswith('BUNDLE') or k.startswith('GEM_') or k in ('RUBYOPT', 'RUBYLIB'))}
    return json.loads(subprocess.check_output(
        ['ruby', '-ryaml', '-rjson', '-e', 'puts JSON.generate(YAML.safe_load(STDIN.read, aliases: false))'],
        input=raw, env=env))


def main():
    inventory_path = HERE / 'package-c7-final-source-inventory.json'
    inventory = json.loads(inventory_path.read_text())
    assert inventory['provider'] == PROVIDER
    result = {
        'schema': 1, 'slug': SLUG, 'workspace': str(WORKSPACE),
        'provider_head': PROVIDER, 'provider_flake': FLAKE,
        'source_inventory_sha256': sha(inventory_path.read_bytes()),
        'driver_sha256': sha((HERE / 'package-c7-git-cache-post-review.py').read_bytes()),
        'runner': {'path': 'package-c-r-post-review.py', 'sha256': sha((HERE / 'package-c-r-post-review.py').read_bytes())},
        'probe': {'path': 'package-c7-git-cache-runtime-probe.sh', 'sha256': sha((HERE / 'package-c7-git-cache-runtime-probe.sh').read_bytes())},
        'provider_receipt_root': '/tmp/flake-update-guard-b-git-cache-rspec-2026-10-24-1',
        'owned_root': '/tmp/flake-update-guard-c7-git-cache-2026-10-24-1',
        'review_receipt': 'review-git-cache-report.md',
        'scope': 'Seven selected guarded updater/commit/final-HEAD-lock paths, caller shells/hooks, shared cache and local Git race',
        'omitted_scope': ['unchanged Go/Ruby dependency refresh', 'application builds', 'Terraform eight-example VM',
                          'external Git publication', 'GitHub Actions cache transport'],
        'historical_evidence': 'git-mirror-verification.md; R receipts remain historical source/input-bound evidence',
        'projects': [],
    }
    for record in inventory['projects']:
        project, head = record['project'], record['head']
        raw = git(project, 'show', head + ':' + record['workflow'])
        assert sha(raw) == record['workflow_sha256']
        data = yaml(raw)
        assert data['env']['CONFCTL_FLAKE'] == FLAKE
        steps = data['jobs']['update']['steps']
        selected = [s for s in steps if s.get('name') in SELECTED[project]]
        assert [s['name'] for s in selected] == SELECTED[project]
        item = {k: record[k] for k in ('project', 'base', 'head', 'tree', 'workflow')}
        item.update(ssh_remote=f'git@github.com:vpsfreecz/{project}.git', source_files=[], steps=[], omitted_steps=[],
                    lock_data=json.loads(git(project, 'show', head + ':flake.lock')),
                    caller_probe=project in ('vpsfree-irc-bot', 'vpsfree-cz-configuration', 'vpsadminos-org-configuration'),
                    probe_input='nixpkgsStable' if project == 'vpsfree-cz-configuration' else 'nixpkgs',
                    configuration=project.endswith('-configuration'))
        paths = {'flake.nix', 'flake.lock', record['workflow'], *record['full_branch_paths'], *EXTRA.get(project, [])}
        for optional in ('Gemfile', 'Gemfile.lock', 'gemset.nix', '.overcommit.yml', 'lefthook.yml', 'Makefile'):
            found = git(project, 'ls-tree', '--name-only', head, '--', optional).decode().strip()
            if found:
                paths.add(optional)
        for hook in git(project, 'ls-tree', '-r', '--name-only', head, '--', '.git-hooks').decode().splitlines():
            paths.add(hook)
        for path in sorted(paths):
            content = git(project, 'show', head + ':' + path)
            item['source_files'].append({'path': path, 'git_blob': git(project, 'rev-parse', head + ':' + path).decode().strip(),
                                         'sha256': sha(content)})
        for step in steps:
            if step in selected:
                kept, omissions = [], []
                for line in step['run'].splitlines(keepends=True):
                    command = line.strip()
                    if command in GC_LINES:
                        omissions.append({'kind': 'verified-existing-gcroot-directory', 'line': command})
                    elif command.startswith('git push '):
                        omissions.append({'kind': 'external-publication', 'line': command})
                    else:
                        kept.append(line)
                script = ''.join(kept)
                assert 'git push' not in script and 'sudo ' not in script and '${{' not in script
                item['steps'].append({'name': step['name'], 'condition': step.get('if'),
                                      'original_script_sha256': sha(step['run'].encode()), 'script_sha256': sha(script.encode()),
                                      'script': script, 'omissions': omissions})
            elif 'run' in step:
                if step['name'] == 'Install jq':
                    reason = 'Declared Nix shell supplies jq; no hosted apt mutation'
                else:
                    assert step['name'] in DEPENDENCY_STEPS
                    reason = 'Unchanged dependency refresh/application check omitted by accepted bounded brief'
                item['omitted_steps'].append({'name': step['name'], 'original_script_sha256': sha(step['run'].encode()), 'reason': reason})
            else:
                assert 'uses' in step
                item['omitted_steps'].append({'name': step.get('name'), 'uses': step['uses'],
                                              'reason': 'Hosted action transport omitted; exact clone/environment/shared owned cache is recorded locally'})
        omissions = [o['kind'] for s in item['steps'] for o in s['omissions']]
        assert omissions.count('external-publication') == 1
        assert omissions.count('verified-existing-gcroot-directory') == (2 if item['configuration'] else 0)
        result['projects'].append(item)
    # Exclusive creation preserves an already-frozen packet.
    with MANIFEST.open('x') as output:
        output.write(json.dumps(result, indent=2) + '\n')
    print('Prepared manifest:', MANIFEST)
    print('SHA256:', sha(MANIFEST.read_bytes()))
    print('Only local immutable Git objects and script syntax were inspected; no updater/package/network command ran.')


if __name__ == '__main__':
    main()

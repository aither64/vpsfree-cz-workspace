#!/usr/bin/env python3
"""Prepared selected C7 checks; root launches only after final review/publication."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import pwd
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
SLUG = HERE.name
PROVIDER = '822c0e35dbe2549111912f539116b4225dfd3035'
MANIFEST = HERE / 'package-c7-git-cache-org-manifest-2.json'
RUNNER = HERE / 'package-c-r-post-review.py'
RUNNER_SHA = '237b5b40646218726a33355ec0a35a706e96330390454621035558291b70f1bf'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha(RUNNER) != RUNNER_SHA:
    raise ValueError('Frozen command runner changed')
spec = importlib.util.spec_from_file_location('c7_frozen_runner', RUNNER)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.MANIFEST = MANIFEST  # Reuse only command/source/graph/environment receipt methods.
Failed = base.Failed


def read_provider(root, review):
    status_path, identity_path = root / 'status.json', root / 'identities.json'
    status, identity = json.loads(status_path.read_text()), json.loads(identity_path.read_text())
    if not (status['exit_status'] == 0 and status['phase'] == 'passed' and status['provider_head'] == PROVIDER
            and status['preceding_review_receipt_sha256'] == sha(review)
            and identity['provider_head'] == PROVIDER
            and identity['coverage'] == {'examples': 203, 'failures': 0, 'pending': 0,
                                         'source': 'Exact exported check build log'}):
        raise ValueError('Completed exact-provider exported203/review evidence required')
    package = Path(identity['package_output'])
    if not ((root / 'provider').is_symlink() and (root / 'provider').resolve() == package and package.is_dir()
            and (root / 'rspec').is_symlink() and str((root / 'rspec').resolve()) == identity['check_output']
            and (root / 'rspec').resolve().exists() and sha(package / 'bin/confctl') == identity['wrapper_sha256']):
        raise ValueError('Retained exact package/check outputs missing or changed')
    for field in ('recursive_provider_derivations', 'recursive_check_derivations', 'source_archive',
                  'source_closure', 'provider_closure', 'check_closure'):
        path = root / identity[field]
        if path.parent != root or not path.is_file():
            raise ValueError('Provider recursive receipt missing')
    metadata = json.loads((root / 'metadata.json').read_text())
    if not (metadata['locked']['rev'] == PROVIDER and metadata['path'] == identity['source']
            and metadata['locked']['narHash'] == identity['source_nar_hash'] and Path(identity['source']).is_dir()):
        raise ValueError('Provider immutable source identity disagreement')
    return identity


def gcroot_preflight():
    user = pwd.getpwuid(os.getuid()).pw_name
    path = Path('/nix/var/nix/gcroots/per-user') / user
    if path.is_symlink() or not path.is_dir() or path.stat().st_uid != os.getuid() or not os.access(path, os.W_OK | os.X_OK):
        raise ValueError('Existing ordinary writable user GC-root directory required')
    return {'path': str(path), 'uid': os.getuid(), 'mode': oct(path.stat().st_mode & 0o7777),
            'reason': 'Hosted-runner mkdir/chown postcondition already holds; no privileged change'}


class Operation(base.Operation):
    def __init__(self, args):
        manifest = json.loads(MANIFEST.read_text())
        if sha(MANIFEST) != args.manifest_sha256 or manifest['driver_sha256'] != sha(__file__):
            raise ValueError('Manifest/driver binding changed')
        if manifest['runner']['sha256'] != sha(RUNNER) or sha(HERE / manifest['probe']['path']) != manifest['probe']['sha256']:
            raise ValueError('Prepared dependency changed')
        if sha(args.review_receipt) != manifest['review_sha256']:
            raise ValueError('Completed frozen review receipt changed')
        values = [os.environ.get(k) for k in ('DEV_SESSION_SLUG', 'DEV_SESSION_WORKSPACE')]
        if values not in ([None, None], [SLUG, str(WORKSPACE)]):
            raise ValueError('Session environment identity mismatch')
        current = subprocess.check_output(['/home/aither/bin/dev-session', 'current'], cwd=WORKSPACE, text=True).strip()
        if current != SLUG or str(Path(args.root).absolute()) != manifest['owned_root']:
            raise ValueError('Session/owned root identity mismatch')
        provider_root = Path(manifest['provider_receipt_root'])
        self.provider = read_provider(provider_root, Path(args.review_receipt))
        expected_receipts = manifest['provider_receipt_hashes']
        if any(sha(provider_root / name) != value for name, value in expected_receipts.items()):
            raise ValueError('Accepted exported203 identity/status receipt changed')
        super().__init__(args)
        if self.root.stat().st_uid != os.getuid() or self.root.is_symlink():
            raise ValueError('Owned root identity mismatch')
        # Reuse only the previously observed cache; never copy, preseed or relabel it.
        ownership = manifest['shared_cache_ownership']
        shared_root = Path(ownership['original_root'])
        if (shared_root.is_symlink() or not shared_root.is_dir()
                or shared_root.stat().st_uid != os.getuid()
                or json.loads((shared_root / 'owner.json').read_text()) != ownership['original_root_owner']):
            raise ValueError('Original shared root ownership changed')
        self.cache = shared_root / 'xdg-cache'
        if (self.cache.is_symlink() or not self.cache.is_dir() or self.cache.stat().st_uid != os.getuid()
                or json.loads((self.cache / 'owner.json').read_text()) != ownership['original_cache_owner']):
            raise ValueError('Original shared cache ownership changed')
        self.receipt['shared_cache_provenance'] = ownership
        self.receipt['cold_cache_claim'] = False
        self.env.update(XDG_CACHE_HOME=str(self.cache))
        self.receipt.update(provider_identities_sha256=sha(provider_root / 'identities.json'),
                            provider_status_sha256=sha(provider_root / 'status.json'), provider_identity=self.provider,
                            driver_sha256=sha(__file__), frozen_runner_sha256=sha(RUNNER),
                            provider_receipt_root=str(provider_root), shared_xdg_cache=str(self.cache),
                            scope=self.manifest['scope'], omitted_scope=self.manifest['omitted_scope'])
        self.save()

    def source(self, item):
        repo = super().source(item)
        # The old tools shell writes this local Bundler file before any update.
        # Ignore exactly that generated file before baseline; retain all other checks.
        exclude = repo / '.git/info/exclude'
        before = sha(exclude)
        with exclude.open('a') as output:
            output.write('\n/.bundle/config\n')
        self.receipt['fixture_local_exclude'] = {
            'rule': '/.bundle/config', 'path': str(exclude), 'before_sha256': before,
            'after_sha256': sha(exclude), 'phase': 'before baseline and shell setup',
            'source': self.manifest['fixture_correction']['source'],
        }
        self.save()
        return repo

    def state(self, repo, label):
        head = self.run(['git', 'rev-parse', 'HEAD'], cwd=repo, label=label + '-head').read_text().strip()
        index = self.run(['git', 'ls-files', '--stage', '-z'], cwd=repo, label=label + '-index')
        committed = self.run(['git', 'show', 'HEAD:flake.lock'], cwd=repo, label=label + '-head-lock')
        status = self.run(['git', 'status', '--porcelain=v1'], cwd=repo, label=label + '-status')
        return {'head': head, 'index_sha256': sha(index), 'working_lock_sha256': sha(repo / 'flake.lock'),
                'committed_lock_sha256': sha(committed), 'lock_equals_head': committed.read_bytes() == (repo / 'flake.lock').read_bytes(),
                'status': status.read_text(), 'status_receipt': str(status)}

    def mirror_snapshot(self, label):
        directory = self.cache / 'confctl/git-mirrors'
        entries = {}
        if directory.exists():
            for path in sorted(directory.iterdir()):
                if path.name.endswith('.lock'):
                    continue
                if not (len(path.name) == 64 and all(c in '0123456789abcdef' for c in path.name)
                        and path.is_dir() and not path.is_symlink()):
                    raise ValueError('Unexpected shared mirror cache entry; inspect before reuse')
                git = self.provider['runtime_binaries']['git']
                origin = self.run([git, '--git-dir=' + str(path), 'config', '--local', '--no-includes',
                                   '--get-all', 'remote.origin.url'], label=label + '-mirror-origin').read_text().strip()
                if not origin.startswith('https://github.com/') or hashlib.sha256(origin.encode()).hexdigest() != path.name:
                    raise ValueError('Mirror exact URL/cache key mismatch')
                objects = self.run([git, '--git-dir=' + str(path), 'count-objects', '-v'], label=label + '-mirror-objects')
                entries[origin] = {'path': str(path), 'url_sha256': path.name, 'inode': path.stat().st_ino,
                                   'device': path.stat().st_dev, 'objects': objects.read_text(),
                                   'fetch_head_sha256': sha(path / 'FETCH_HEAD') if (path / 'FETCH_HEAD').is_file() else None,
                                   'bare': (path / 'HEAD').is_file(),
                                   'pack_files': [{'name': p.name, 'bytes': p.stat().st_size, 'mtime_ns': p.stat().st_mtime_ns}
                                                  for p in sorted((path / 'objects/pack').iterdir()) if p.is_file()]}
        self.receipt.setdefault('cache_snapshots', {})[label] = entries
        self.save()
        return entries

    def retain_graph(self, repo, label):
        metadata = self.graph(str(repo), label, cwd=repo)
        archive_command = next(r for r in reversed(self.receipt['commands']) if r['label'] == label + '-source-archive')
        archive = json.loads(Path(archive_command['stdout']).read_text())
        paths = set()
        def collect(node):
            paths.add(node['path'])
            for child in node.get('inputs', {}).values():
                collect(child)
        collect(archive)
        for i, path in enumerate(sorted(paths)):
            self.run(['nix-store', '--add-root', str(self.out / f'{label}-source-{i}'), '--indirect', '--realise', path],
                     label=label + '-retain-source')
        self.receipt.setdefault('graphs', {})[label] = {'source': metadata['path'], 'source_paths': sorted(paths),
                                                       'input_lock': json.loads((repo / 'flake.lock').read_text())}
        self.package('.#devShells.x86_64-linux.default', label + '-shell', cwd=repo,
                     out_link=self.out / (label + '-shell'))
        self.save()

    def verify_provider(self, repo, env):
        binary = self.run(['nix', 'shell', self.manifest['provider_flake'], '-c', 'bash', '-c', 'command -v confctl'],
                          cwd=repo, env=env, label='selected-provider-binary').read_text().strip()
        if Path(binary).resolve() != (Path(self.provider['package_output']) / 'bin/confctl').resolve():
            raise ValueError('Selected provider differs from successful exported check')
        self.run(['nix-store', '--add-root', str(self.out / 'provider'), '--indirect', '--realise', self.provider['package_output']],
                 label='retain-same-provider')

    def project(self, item):
        repo = self.source(item)
        tree = self.run(['git', 'rev-parse', 'HEAD^{tree}'], cwd=repo, label='verify-exact-source-tree').read_text().strip()
        if tree != item['tree']:
            raise ValueError('Exact consumer source tree mismatch')
        runtime = self.out / 'runner-temp'; runtime.mkdir()
        env = dict(self.env, RUNNER_TEMP=str(runtime), UPDATE_OLD_LOCK=str(runtime / 'flake-update-baseline.lock'),
                   GITHUB_ENV=str(runtime / 'github-env'), GITHUB_OUTPUT=str(runtime / 'github-output'))
        Path(env['GITHUB_ENV']).touch(); Path(env['GITHUB_OUTPUT']).touch()
        original = self.out / 'original-flake.lock'
        original.write_bytes((repo / 'flake.lock').read_bytes())  # Before any environment or update operation.
        self.receipt['baseline'] = self.state(repo, 'baseline')
        self.receipt.update(source=item, baseline_lock_sha256=sha(original), selected_steps=[],
                            omitted_steps=item['omitted_steps'], caller_probe=item['caller_probe'])
        self.mirror_snapshot('before-setup')
        self.setup(item, repo)
        if item['project'] == 'haveapi':
            # Sign custom hooks as well as the merged configuration in the owned clone.
            self.run(['nix', 'develop', '--no-write-lock-file', '-c', 'bundle', 'exec', 'overcommit', '--sign', 'pre-commit'],
                     cwd=repo, label='declared-shell-custom-hook-signatures')
        self.verify_provider(repo, env)
        self.retain_graph(repo, 'baseline')
        auxiliary = 'github:NixOS/nixpkgs/nixos-unstable' if item['project'] == 'vpsfree-irc-bot' else None
        if auxiliary:
            auxiliary_before = self.graph(auxiliary, 'auxiliary-jq-before')
            self.package(auxiliary + '#jq', 'auxiliary-jq', out_link=self.out / 'auxiliary-jq')
        if item['configuration']:
            self.receipt['gcroot_preflight'] = gcroot_preflight()
        if item['caller_probe']:
            probe_env = dict(env, RUNTIME_RECEIPT=str(self.out / 'caller-runtime'), PROBE_INPUT=item['probe_input'],
                             PROBE_CHANNELS='1' if item['configuration'] else '0',
                             EXPECTED_PROVIDER_BINARY=str(Path(self.provider['package_output']) / 'bin/confctl'))
            self.run(['nix', 'develop', '--no-write-lock-file', '-c', 'bash', str(HERE / self.manifest['probe']['path'])],
                     cwd=repo, env=probe_env, label='actual-workflow-caller-shell-probe')
        rows_argv = ['nix', 'shell', self.manifest['provider_flake'], '-c', 'confctl', 'inputs', 'ls', '--json']
        before_rows = self.json(rows_argv, cwd=repo, env=env, label='baseline-resolved-inputs')
        for i, step in enumerate(item['steps']):
            if step['condition']:
                if item['project'] != 'haveapi' or step['condition'] != "steps.update.outputs.committed == 'true'":
                    raise ValueError('Unexpected selected-step condition')
                committed = dict(line.split('=', 1) for line in Path(env['GITHUB_OUTPUT']).read_text().splitlines()).get('committed')
                if committed not in ('true', 'false'):
                    raise ValueError('Missing HaveAPI update outcome')
                if committed == 'false':
                    self.receipt['selected_steps'].append({'name': step['name'], 'condition_taken': False})
                    continue
            script = self.out / f'step-{i:02d}.sh'
            script.write_text('set -euo pipefail\n' + step['script'])
            self.receipt['selected_steps'].append(dict({k: v for k, v in step.items() if k != 'script'},
                                                       executed_script_sha256=sha(script)))
            before = self.state(repo, f'step-{i:02d}-before')
            self.mirror_snapshot(f'step-{i:02d}-before')
            if step['name'] == 'Update llm-agents when Codex changes':
                llm_before = self.graph('github:numtide/llm-agents.nix', 'llm-upstream-before')
            argv = ['bash', '--noprofile', '--norc', str(script)] if item['configuration'] else [
                'nix', 'develop', '--no-write-lock-file', '-c', 'bash', str(script)]
            try:
                output = self.run(argv, cwd=repo, env=env, label=f'selected-workflow-step-{i:02d}')
            except Failed as error:
                self.receipt.update(update_status=error.status, before_failed_step=before,
                                    after_failed_step=self.state(repo, f'step-{i:02d}-failure'), failed_step=step['name'],
                                    effect_scope='Per-step snapshots; earlier accepted local commits may remain')
                self.mirror_snapshot('failure-retained')
                raise
            if step['name'] == 'Update llm-agents when Codex changes':
                text = output.read_text()
                self.receipt['llm_agents_branch'] = 'skipped-version-equal' if 'skipping llm-agents' in text else 'updated-version-verified' if 'Updating llm-agents' in text else 'unclassified'
                if self.receipt['llm_agents_branch'] == 'unclassified':
                    raise ValueError('Conditional llm-agents result not recorded')
                self.receipt['llm_agents_mock_coverage'] = 'package-c7-final-quick.json: vpsfree-cz-configuration12 including both version branches'
                llm_after = self.graph('github:numtide/llm-agents.nix', 'llm-upstream-after')
                if llm_before['locked'] != llm_after['locked']:
                    raise ValueError('Mutable llm-agents source changed during version selection')
            for line in Path(env['GITHUB_ENV']).read_text().splitlines():
                key, value = line.split('=', 1)
                if key not in ('UPDATE_START_REF', 'UPDATE_OLD_LOCK'):
                    raise ValueError('Unexpected workflow environment output')
                env[key] = value
            self.mirror_snapshot(f'step-{i:02d}-after')
        if (runtime / 'flake-update-baseline.lock').read_bytes() != original.read_bytes():
            raise ValueError('Workflow baseline differs from original checkout lock')
        final = self.run(['git', 'show', 'HEAD:flake.lock'], cwd=repo, label='final-committed-lock')
        warm_before = self.mirror_snapshot('warm-final-before')
        self.run(['nix', 'shell', self.manifest['provider_flake'], '-c', 'confctl', 'inputs', 'check-update',
                  '--old-lock', str(original), '--new-lock', str(final)], cwd=repo, env=env,
                 label='same-provider-final-HEAD-lock-check')
        warm_after = self.mirror_snapshot('warm-final-after')
        if warm_before != warm_after:
            raise ValueError('Final repeated guard changed shared mirror storage; inspect warm-cache evidence')
        after_rows = self.json(rows_argv, cwd=repo, env=env, label='final-resolved-inputs')
        if auxiliary:
            auxiliary_after = self.graph(auxiliary, 'auxiliary-jq-after')
            if auxiliary_before['locked'] != auxiliary_after['locked']:
                raise ValueError('Mutable auxiliary jq source changed during selected updater path')
        if item['project'] in ('vpsf-status', 'vpsfree-irc-bot'):
            for parent in ('vpsadmin', 'vpsadminos'):
                old = [r for r in before_rows if r['input'] == parent]
                new = [r for r in after_rows if r['input'] == parent]
                if len(old) != 1 or old != new:
                    raise ValueError('Leaf update changed a parent source')
        generated = self.run(['git', 'log', '--format=%H %s', item['head'] + '..HEAD'], cwd=repo, label='generated-commits')
        state = self.state(repo, 'final')
        if not state['lock_equals_head'] or state['status']:
            raise ValueError('Final selected-path checkout is not clean and committed')
        self.retain_graph(repo, 'final')
        initial_cache = self.receipt['cache_snapshots']['before-setup']
        self.receipt.update(final=state, final_lock_sha256=sha(final), input_locks={'baseline': item['lock_data'], 'final': json.loads(final.read_text())},
                            generated_commits=generated.read_text().splitlines(), warm_final_cache_unchanged=True,
                            new_mirrors=sorted(set(warm_after) - set(initial_cache)), reused_mirrors=sorted(set(warm_after) & set(initial_cache)),
                            outcome='selected-path-passed', all_seven_full_workflows=False)


def execute(args):
    op = None
    try:
        op = Operation(args)
        op.run(['nix', '--version'], label='host-nix-version')
        item = next(i for i in op.manifest['projects'] if i['project'] == args.project)
        op.project(item)
        op.receipt.update(complete=True, exit_status=0)
        return 0
    except Failed as error:
        if op:
            op.receipt.update(exit_status=error.status, failed_command=str(error), kernel_escalation=op.kernel)
        return error.status
    except Exception as error:
        if op:
            op.receipt.update(exit_status=2, failure_class=type(error).__name__)
        print('Prepared-operation failure (' + type(error).__name__ + '); parent diagnosis required', file=sys.stderr)
        return 2
    finally:
        if op:
            op.receipt['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            op.save()
            print('Receipt:', op.out / 'receipt.json', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--review-receipt', required=True)
    parser.add_argument('--manifest-sha256', required=True)
    parser.add_argument('stage', choices=['project'])
    parser.add_argument('project', choices=['vpsadminos-org-configuration'])
    return execute(parser.parse_args())


if __name__ == '__main__':
    sys.exit(main())

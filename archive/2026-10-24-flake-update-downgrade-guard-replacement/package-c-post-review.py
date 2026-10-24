#!/usr/bin/env python3
"""Prepared C verification operation. No default action; never pushes or deploys."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import threading
import time

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'package-c-verification-manifest.json'
KERNEL = re.compile(rb"building [\"']?/nix/store/[^\r\n]*-linux(?:-vpsadminos)?-[0-9][^\r\n]*\.drv")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Failed(Exception):
    def __init__(self, status, label):
        self.status = status if 0 < status < 256 else 1
        super().__init__(f'{label} exited {status}')


class Operation:
    def __init__(self, args):
        self.args = args
        self.manifest = json.loads(MANIFEST.read_text())
        self.root = Path(args.root).absolute()
        if self.root.parent != Path('/tmp') or not self.root.name.startswith('flake-update-guard-'):
            raise ValueError('Use an owned /tmp/flake-update-guard-* directory')
        if not Path(args.review_receipt).is_file():
            raise ValueError('Completed independent-review receipt is required')
        identity = {'slug': self.manifest['slug'], 'manifest_sha256': sha(MANIFEST),
                    'review_receipt_sha256': sha(args.review_receipt)}
        marker = self.root / 'owner.json'
        if self.root.exists():
            if self.root.is_symlink() or json.loads(marker.read_text()) != identity:
                raise ValueError('Verification directory ownership does not match')
        else:
            self.root.mkdir(mode=0o700)
            marker.write_text(json.dumps(identity, indent=2) + '\n')
        name = args.stage + ('-' + args.project if args.project else '')
        self.out = self.root / name
        self.out.mkdir()  # An existing attempt needs parent inspection, not an automatic retry.
        self.receipt = dict(identity, stage=name, driver_sha256=sha(__file__), commands=[],
                            started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                            provider_head=self.manifest['provider_head'], complete=False)
        self.env = dict(os.environ, CONFCTL_FLAKE=self.manifest['provider_flake'])
        self.kernel = False
        self.number = 0

    def run(self, argv, cwd=None, env=None, label=None):
        self.number += 1
        label = label or f'command-{self.number:03d}'
        stdout = self.out / f'{self.number:03d}-{label}.stdout'
        stderr = self.out / f'{self.number:03d}-{label}.stderr'
        started = time.monotonic()
        print(f'{label}: starting; logs {stdout.name}, {stderr.name}', flush=True)
        p = subprocess.Popen(argv, cwd=cwd, env=env or self.env, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, start_new_session=True)
        record = dict(argv=argv, cwd=str(cwd) if cwd else None, pid=p.pid, pgid=p.pid,
                      stdout=str(stdout), stderr=str(stderr), label=label)
        self.receipt['commands'].append(record)
        self.save()
        kernel = threading.Event()

        def copy(src, dest):
            with dest.open('wb') as f:
                for line in iter(src.readline, b''):
                    f.write(line)
                    f.flush()
                    if KERNEL.search(line):
                        kernel.set()
            src.close()

        threads = [threading.Thread(target=copy, args=(p.stdout, stdout)),
                   threading.Thread(target=copy, args=(p.stderr, stderr))]
        for thread in threads:
            thread.start()
        interrupted = False
        while p.poll() is None:
            if kernel.is_set() and not interrupted:
                interrupted = True
                self.kernel = True
                print(f'ESCALATE: unexpected local kernel build in {label}; interrupting owned process group {p.pid}', flush=True)
                os.killpg(p.pid, signal.SIGINT)
            try:
                p.wait(timeout=0.5)
            except subprocess.TimeoutExpired:
                pass  # No generic quiet-build deadline.
        for thread in threads:
            thread.join()
        if kernel.is_set():
            self.kernel = True
            if not interrupted:
                print(f'ESCALATE: kernel build reported as {label} exited; inspect completed command effects', flush=True)
        record.update(exit_status=p.returncode, elapsed_seconds=round(time.monotonic() - started, 3),
                      stdout_sha256=sha(stdout), stderr_sha256=sha(stderr), kernel_interrupt=interrupted,
                      kernel_build_reported=kernel.is_set())
        self.save()
        if kernel.is_set() or p.returncode:
            raise Failed(p.returncode or 125, label)
        return stdout

    def json(self, argv, **kwargs):
        return json.loads(self.run(argv, **kwargs).read_text())

    def save(self):
        (self.out / 'receipt.json').write_text(json.dumps(self.receipt, indent=2) + '\n')

    def source(self, item):
        repo = self.out / 'checkout'
        self.run(['git', 'clone', '--no-checkout', '--filter=blob:none', '--no-tags',
                  item['ssh_remote'], str(repo)], label='clone-exact-source')
        self.run(['git', 'checkout', '--detach', item['head']], cwd=repo, label='checkout-exact-head')
        self.run(['git', 'remote', 'set-url', '--push', 'origin', 'disabled://nonpublishing-verification'],
                 cwd=repo, label='disable-push')
        actual = self.run(['git', 'rev-parse', 'HEAD'], cwd=repo, label='source-head').read_text().strip()
        if actual != item['head']:
            raise ValueError('Source head mismatch')
        self.run(['git', 'ls-tree', '-r', '--full-tree', 'HEAD'], cwd=repo, label='source-tree')
        self.receipt['source'] = item
        for expected in item['source_files']:
            if sha(repo / expected['path']) != expected['sha256']:
                raise ValueError('Source content mismatch: ' + expected['path'])
        return repo

    def graph(self, flake, label, cwd=None):
        metadata = self.json(['nix', 'flake', 'metadata', '--json', '--no-write-lock-file', flake],
                             cwd=cwd, label=label + '-metadata')
        archive = self.json(['nix', 'flake', 'archive', '--json', '--no-write-lock-file', flake],
                            cwd=cwd, label=label + '-source-archive')
        if metadata.get('path') != archive.get('path'):
            raise ValueError('Source changed between metadata and archive: ' + label)
        paths = set()

        def collect(node):
            if isinstance(node, dict):
                if isinstance(node.get('path'), str) and node['path'].startswith('/nix/store/'):
                    paths.add(node['path'])
                for value in node.values():
                    collect(value)
        collect(archive)
        if not paths:
            raise ValueError('Archive omitted source store paths')
        self.json(['nix', 'path-info', '--json', '--recursive', *sorted(paths)],
                  label=label + '-source-closure')
        return metadata

    def package(self, flake, label, cwd=None):
        self.json(['nix', 'derivation', 'show', '--recursive', flake], cwd=cwd,
                  label=label + '-derivations')
        built = self.json(['nix', 'build', '--no-link', '--json', flake], cwd=cwd,
                          label=label + '-build')
        paths = sorted({path for entry in built for path in entry['outputs'].values()})
        if not paths:
            raise ValueError('Package build omitted output paths: ' + label)
        self.json(['nix', 'path-info', '--json', '--recursive', *paths],
                  label=label + '-runtime-closure')
        return paths

    def startup(self):
        item = self.manifest['provider']
        self.receipt['source'] = item
        flake = self.manifest['provider_flake']
        metadata = self.graph(flake.split('#')[0], 'provider')
        if metadata.get('locked', {}).get('rev') != self.manifest['provider_head']:
            raise ValueError('Actual provider source revision mismatch')
        paths = self.package(flake, 'provider')
        if len(paths) != 1:
            raise ValueError('Expected one confctl package output')
        wrapper = Path(paths[0]) / 'bin/confctl'
        wrapper_text = wrapper.read_text()
        (self.out / 'confctl-wrapper').write_text(wrapper_text)
        match = re.search(r'export PATH="([^"\n]+):\$PATH"', wrapper_text)
        if not match:
            raise ValueError('Package wrapper PATH contract changed')
        nix_binary = next((Path(directory) / 'nix' for directory in match[1].split(':')
                           if (Path(directory) / 'nix').is_file()), None)
        if nix_binary is None:
            raise ValueError('Packaged Nix executable not found')
        self.receipt.update(package_output=paths[0], wrapper_sha256=sha(wrapper), packaged_nix=str(nix_binary),
                            inherited_ruby_environment={key: bool(self.env.get(key)) for key in
                                                       ('RUBYOPT', 'BUNDLE_GEMFILE', 'GEM_HOME', 'GEM_PATH')})
        self.run([str(nix_binary), '--version'], label='actual-packaged-nix-version')
        for args in [['--help'], ['inputs', 'update', '--help'], ['inputs', 'ls', '--help'],
                     ['inputs', 'check-update', '--help']]:
            self.run(['nix', 'shell', flake, '-c', 'confctl', *args], label='actual-package-startup')

    def setup(self, item, repo):
        project = item['project']
        self.run(['git', 'config', 'user.name', 'Flake guard verification'], cwd=repo, label='fixture-git-name')
        self.run(['git', 'config', 'user.email', 'flake-guard-verification@example.invalid'],
                 cwd=repo, label='fixture-git-email')
        if project in ('haveapi', 'vpsadminos', 'vpsfree-irc-bot'):
            self.run(['nix', 'develop', '-c', 'bash', '-c',
                      'bundle exec overcommit --install && bundle exec overcommit --sign'],
                     cwd=repo, label='declared-shell-hooks')
        elif project == 'vpsf-status':
            self.run(['nix', 'develop', '-c', 'make', 'hooks'], cwd=repo, label='declared-shell-hooks')
        else:
            self.run(['nix', 'develop', '-c', 'true'], cwd=repo, label='declared-shell')
        for expected in item['source_files']:
            if sha(repo / expected['path']) != expected['sha256']:
                raise ValueError('Environment setup changed pinned source: ' + expected['path'])

    def project(self, item):
        repo = self.source(item)
        runtime = self.out / 'runner-temp'
        runtime.mkdir()
        env = dict(self.env, RUNNER_TEMP=str(runtime), UPDATE_OLD_LOCK=str(runtime / 'flake-update-baseline.lock'),
                   GITHUB_ENV=str(runtime / 'github-env'), GITHUB_OUTPUT=str(runtime / 'github-output'))
        Path(env['GITHUB_ENV']).touch()
        Path(env['GITHUB_OUTPUT']).touch()
        baseline = (repo / 'flake.lock').read_bytes()
        (self.out / 'original-flake.lock').write_bytes(baseline)
        before_index = self.run(['git', 'ls-files', '--stage', '-z'], cwd=repo, label='baseline-index').read_bytes()
        self.graph(str(repo), 'baseline')
        self.setup(item, repo)
        self.package('.#devShells.x86_64-linux.default', 'baseline-dev-shell', cwd=repo)
        self.receipt['baseline_lock_sha256'] = hashlib.sha256(baseline).hexdigest()
        self.receipt['baseline_index_sha256'] = hashlib.sha256(before_index).hexdigest()
        auxiliary = None
        if item['project'] == 'vpsfree-irc-bot':
            auxiliary = 'github:NixOS/nixpkgs/nixos-unstable'
            before_auxiliary = self.graph(auxiliary, 'auxiliary-jq-before')
            self.package(auxiliary + '#jq', 'auxiliary-jq')
        metadata_argv = ['nix', 'shell', self.manifest['provider_flake'], '-c',
                         'confctl', 'inputs', 'ls', '--json']
        before_rows = self.json(metadata_argv, cwd=repo, env=env, label='baseline-resolved-inputs')
        try:
            for i, step in enumerate(item['steps']):
                if 'git push' in step['script']:
                    raise ValueError('Publication command in prepared step')
                script = self.out / f'step-{i:02d}.sh'
                script.write_text('set -euo pipefail\n' + step['script'])
                self.run(['nix', 'develop', '-c', 'bash', str(script)], cwd=repo, env=env,
                         label=f'workflow-step-{i:02d}')
                for line in Path(env['GITHUB_ENV']).read_text().splitlines():
                    key, _, value = line.partition('=')
                    if key not in ('UPDATE_START_REF', 'UPDATE_OLD_LOCK'):
                        raise ValueError('Unexpected workflow environment output')
                    env[key] = value
        except Failed as error:
            unchanged = ((repo / 'flake.lock').read_bytes() == baseline and
                         self.run(['git', 'rev-parse', 'HEAD'], cwd=repo, label='failure-head').read_text().strip() == item['head'] and
                         self.run(['git', 'ls-files', '--stage', '-z'], cwd=repo, label='failure-index').read_bytes() == before_index)
            self.receipt.update(update_status=error.status, original_lock_index_head_unchanged=unchanged)
            raise
        final_lock = self.run(['git', 'show', 'HEAD:flake.lock'], cwd=repo, label='published-lock-snapshot')
        self.run(['nix', 'shell', self.manifest['provider_flake'], '-c', 'confctl', 'inputs', 'check-update',
                  '--old-lock', str(self.out / 'original-flake.lock'), '--new-lock', str(final_lock)],
                 cwd=repo, env=env, label='final-committed-blob-check')
        self.run(['git', 'log', '--format=%H %s', item['head'] + '..HEAD'], cwd=repo, label='generated-commits')
        self.run(['git', 'status', '--porcelain'], cwd=repo, label='final-status')
        self.graph(str(repo), 'candidate')
        self.package('.#devShells.x86_64-linux.default', 'candidate-dev-shell', cwd=repo)
        after_rows = self.json(metadata_argv, cwd=repo, env=env, label='final-resolved-inputs')
        if item['project'] in ('vpsf-status', 'vpsfree-irc-bot'):
            for name in ('vpsadmin', 'vpsadminos'):
                before = [row for row in before_rows if row['input'] == name]
                after = [row for row in after_rows if row['input'] == name]
                if len(before) != 1 or before != after:
                    raise ValueError('Leaf update changed parent source identity/revision: ' + name)
        if auxiliary:
            after_auxiliary = self.graph(auxiliary, 'auxiliary-jq-after')
            if before_auxiliary.get('locked') != after_auxiliary.get('locked'):
                raise ValueError('Mutable auxiliary jq source changed during verification')
        if item['project'] == 'vpsf-status':
            self.package('.#vpsf-status', 'candidate-status-package', cwd=repo)
        self.receipt.update(final_lock_sha256=sha(final_lock),
                            final_head=self.run(['git', 'rev-parse', 'HEAD'], cwd=repo,
                                                label='final-head').read_text().strip())
        (self.out / 'final-flake.lock').write_bytes((repo / 'flake.lock').read_bytes())
        self.receipt['input_locks'] = {'baseline': json.loads(baseline), 'final': json.loads(final_lock.read_bytes())}

    def terraform_smoke(self, item):
        repo = self.source(item)
        runtime = self.out / 'runner-temp'
        runtime.mkdir()
        self.graph(str(repo), 'terraform-baseline')
        installable = '.#tests.x86_64-linux.workflows'
        self.json(['nix', 'derivation', 'show', '--recursive', installable], cwd=repo,
                  label='selected-workflows-derivations')
        selected = self.run(['./test-runner.sh', 'ls', 'workflows'], cwd=repo,
                            label='selected-workflows-metadata').read_text().strip()
        if selected != 'workflows':
            raise ValueError('Expected exactly the singleton workflows test')
        self.run(['./test-runner.sh', 'test', '-f', '--jobs', '1', '--stop-on-failure',
                  '--state-dir', str(runtime / 'terraform-workflows-state'), 'workflows'],
                 cwd=repo, label='terraform-workflows-only')
        config = self.json(['nix', 'build', '--no-link', '--json', installable], cwd=repo,
                           label='selected-workflows-config')
        paths = sorted({path for entry in config for path in entry['outputs'].values()})
        self.json(['nix', 'path-info', '--json', '--recursive', *paths], label='selected-workflows-runtime-closure')
        self.receipt.update(integration=item['integration'], state_directory=str(runtime / 'terraform-workflows-state'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--review-receipt', required=True)
    parser.add_argument('stage', choices=['startup', 'project', 'terraform-smoke'])
    parser.add_argument('project', nargs='?')
    args = parser.parse_args()
    operation = Operation(args)
    try:
        if args.stage == 'startup':
            operation.startup()
        else:
            name = args.project if args.stage == 'project' else 'terraform-provider-vpsadmin'
            item = next(item for item in operation.manifest['projects'] if item['project'] == name)
            if args.stage == 'project':
                operation.project(item)
            else:
                operation.terraform_smoke(item)
        operation.receipt['complete'] = True
        operation.receipt['exit_status'] = 0
        return 0
    except Failed as error:
        operation.receipt.update(exit_status=error.status, failed_command=str(error), kernel_escalation=operation.kernel)
        return error.status
    except Exception as error:
        operation.receipt.update(exit_status=1, preparation_or_receipt_error=str(error),
                                 kernel_escalation=operation.kernel)
        return 1
    finally:
        operation.receipt['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        operation.save()
        print('Receipt:', operation.out / 'receipt.json', flush=True)


if __name__ == '__main__':
    sys.exit(main())

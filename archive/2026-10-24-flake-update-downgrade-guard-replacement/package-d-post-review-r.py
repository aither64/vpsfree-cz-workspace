#!/usr/bin/env python3
"""Prepare or run exact, nonpublishing D verification after lead assignment."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import pwd
import re
import signal
import socket
import subprocess
import sys
import threading
import time

HERE = Path(__file__).resolve().parent
WORKSPACE = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-24-flake-update-downgrade-guard-replacement'
MANIFEST = HERE / 'package-d-verification-manifest-r.json'
PROVIDER = '5436d3d7c36d3d5174eab3c44e3578830749d3db'
FLAKE = f'github:vpsfreecz/confctl/{PROVIDER}#confctl'
WORKFLOW = '.github/workflows/daily-update.yml'
PROBE = HERE / 'provider-runtime-probe-r.sh'
SELECTED = {
    'vpsfree-cz-configuration': [
        'Save input baseline', 'Setup git', 'Install git hooks', 'Update inputs',
        'Update llm-agents when Codex changes', 'Update package dependencies', 'Check and push updates'],
    'vpsadminos-org-configuration': [
        'Save input baseline', 'Setup git', 'Install git hooks', 'Update flake inputs', 'Check and push updates'],
}
GCPREP = {
    'vpsfree-cz-configuration': [
        'sudo mkdir "/nix/var/nix/gcroots/per-user/$USER"',
        'sudo chown "$USER" "/nix/var/nix/gcroots/per-user/$USER"'],
    'vpsadminos-org-configuration': [
        'sudo mkdir /nix/var/nix/gcroots/per-user/$USER',
        'sudo chown $USER /nix/var/nix/gcroots/per-user/$USER'],
}
KERNEL = re.compile(rb'building ["\']?/nix/store/[^\r\n]*-linux(?:-vpsadminos)?-[0-9][^\r\n]*\.drv')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    return digest(Path(path).read_bytes())


def git_blob(project, head, path):
    return subprocess.check_output(['git', '--git-dir=' + str(WORKSPACE / 'repos' / (project + '.git')),
                                    'show', head + ':' + path])


def git_value(project, revision):
    return subprocess.check_output(['git', '--git-dir=' + str(WORKSPACE / 'repos' / (project + '.git')),
                                    'rev-parse', revision], text=True).strip()


def gcroot_preflight():
    name = pwd.getpwuid(os.getuid()).pw_name
    path = Path('/nix/var/nix/gcroots/per-user') / name
    if os.environ.get('USER') != name or path.is_symlink() or not path.is_dir():
        raise ValueError('GC-root preflight: expected existing ordinary directory for the executing user')
    stat = path.stat()
    if stat.st_uid != os.getuid() or not os.access(path, os.W_OK | os.X_OK):
        raise ValueError('GC-root preflight: existing directory must be owned, writable and searchable')
    return {'path': str(path), 'host': socket.gethostname(), 'executing_uid': os.getuid(),
            'owner_uid': stat.st_uid, 'mode': oct(stat.st_mode & 0o7777), 'writable_searchable': True,
            'omission_reason': 'Hosted-runner mkdir/chown postcondition already holds; no privileged mutation needed'}


def transform(project, name, script):
    kept, omitted = [], []
    for line in script.splitlines(keepends=True):
        command = line.strip()
        if command in GCPREP[project]:
            omitted.append({'kind': 'verified-gcroot-preparation', 'line': line.rstrip('\n')})
        elif command == 'git push origin master':
            if name != 'Check and push updates':
                raise ValueError('Publication line outside expected final block')
            omitted.append({'kind': 'publication', 'line': line.rstrip('\n')})
        else:
            kept.append(line)
    transformed = ''.join(kept)
    if re.search(r'\bsudo\b|\bgit\s+push\b', transformed):
        raise ValueError('Unexpected privileged/publication command remains')
    return transformed, omitted


def yaml_data(raw):
    # Only the fixture parser is isolated from Bundler, never an actual tool invocation.
    env = {key: value for key, value in os.environ.items()
           if not (key.startswith('BUNDLE') or key.startswith('GEM_') or key in ('RUBYOPT', 'RUBYLIB'))}
    raw_json = subprocess.check_output(['ruby', '-ryaml', '-rjson', '-e',
                                       'puts JSON.generate(YAML.safe_load(STDIN.read, aliases: false))'], input=raw, env=env)
    return json.loads(raw_json)


def prepare():
    branches = json.loads((HERE / 'package-d-branches-r.json').read_text())['repositories']
    prepared = {'schema': 1, 'slug': SLUG, 'workspace': str(WORKSPACE), 'provider_head': PROVIDER,
                'provider_flake': FLAKE, 'driver_sha256': file_sha(__file__),
                'probe_sha256': file_sha(PROBE), 'gcroot_preflight_at_preparation': gcroot_preflight(),
                'status': 'Prepared only; execution requires completed review and a separate lead assignment', 'projects': []}
    for record in branches:
        project, head = record['project'], record['head']
        raw = git_blob(project, head, WORKFLOW)
        if digest(raw) != record['workflow_sha256']:
            raise ValueError('Workflow does not match the recorded final source')
        workflow = yaml_data(raw)
        if workflow['env']['CONFCTL_FLAKE'] != FLAKE:
            raise ValueError('Unexpected provider pin')
        if workflow['env']['GITHUB_TOKEN'] != '${{ secrets.GITHUB_TOKEN }}':
            raise ValueError('Provider token must come from workflow environment')
        steps = workflow['jobs']['update']['steps']
        selected = [step for step in steps if 'run' in step]
        if [step['name'] for step in selected] != SELECTED[project]:
            raise ValueError('Unexpected workflow run-step order')
        item = {'project': project, 'base': record['base'], 'head': head,
                'tree': git_value(project, head + '^{tree}'), 'ssh_remote': record['remote'],
                'workflow': WORKFLOW, 'probe_input': 'nixpkgsStable' if project == 'vpsfree-cz-configuration' else 'nixpkgs',
                'source_files': [], 'lock_data': json.loads(git_blob(project, head, 'flake.lock')), 'steps': [],
                'nonexecuted_actions': [dict(uses=step['uses'], reason=('Exact SSH clone and pinned detached checkout replace hosted checkout' if step['uses'].startswith('actions/checkout@') else 'Existing host Nix and verified packaged Nix replace installer; versions recorded' if step['uses'].startswith('cachix/install-nix-action@') else 'Cache transport omitted; actual updater/dependency commands retained'))
                                        for step in steps if 'uses' in step]}
        for path in ('flake.nix', 'flake.lock', WORKFLOW, 'Gemfile', 'Gemfile.lock', '.overcommit.yml',
                     '.git-hooks/pre_commit/nixfmt.rb'):
            content = git_blob(project, head, path)
            item['source_files'].append({'path': path, 'git_blob': git_value(project, head + ':' + path),
                                         'sha256': digest(content)})
        omissions = []
        for step in selected:
            script, omitted = transform(project, step['name'], step['run'])
            item['steps'].append({'name': step['name'], 'original_script_sha256': digest(step['run'].encode()),
                                  'script_sha256': digest(script.encode()), 'script': script, 'omissions': omitted})
            omissions.extend(omitted)
        if sorted(entry['kind'] for entry in omissions) != ['publication', 'verified-gcroot-preparation', 'verified-gcroot-preparation']:
            raise ValueError('Expected exactly two GC-root omissions and one removed publication line')
        prepared['projects'].append(item)
    provider_files = ['flake.nix', 'flake.lock', 'nix/package.nix', 'Gemfile', 'Gemfile.lock', 'gemset.nix']
    prepared['provider'] = {'head': PROVIDER, 'tree': git_value('confctl', PROVIDER + '^{tree}'),
                            'source_files': [{'path': path, 'git_blob': git_value('confctl', PROVIDER + ':' + path),
                                              'sha256': digest(git_blob('confctl', PROVIDER, path))} for path in provider_files],
                            'lock_data': json.loads(git_blob('confctl', PROVIDER, 'flake.lock'))}
    MANIFEST.write_text(json.dumps(prepared, indent=2) + '\n')
    print('Prepared manifest:', MANIFEST)
    print('Manifest SHA-256:', file_sha(MANIFEST))
    print('No package, update, clone, privileged command or publication executed.')


class Failed(Exception):
    def __init__(self, status, record):
        self.status = status if 0 < status < 256 else 1
        self.record = record
        super().__init__(record['label'] + ' exited ' + str(status))


class Operation:
    def __init__(self, args):
        self.manifest = json.loads(MANIFEST.read_text())
        if file_sha(MANIFEST) != args.manifest_sha256 or self.manifest['driver_sha256'] != file_sha(__file__):
            raise ValueError('Manifest/driver hash mismatch')
        if self.manifest['probe_sha256'] != file_sha(PROBE):
            raise ValueError('Runtime probe changed after manifest preparation')
        if not Path(args.review_receipt).is_file():
            raise ValueError('Completed independent-review receipt is required')
        source = json.loads(Path(args.provider_receipt).read_text())
        if not (source.get('complete') and source.get('exit_status') == 0 and
                source.get('provider_head') == PROVIDER and source.get('package_output') and source.get('packaged_nix')):
            raise ValueError('Successful exact-provider startup receipt required')
        values = [os.environ.get(key) for key in ('DEV_SESSION_SLUG', 'DEV_SESSION_WORKSPACE')]
        if values not in ([None, None], [SLUG, str(WORKSPACE)]):
            raise ValueError('Session environment identity mismatch')
        current = subprocess.check_output(['/home/aither/bin/dev-session', 'current'], cwd=WORKSPACE, text=True).strip()
        if current != SLUG:
            raise ValueError('dev-session identity mismatch')
        self.gcroot = gcroot_preflight()  # Must pass again before omitting hosted-runner setup.
        if not os.environ.get('GITHUB_TOKEN'):
            raise ValueError('GITHUB_TOKEN must be supplied through the watcher environment')
        self.secrets = [os.environ[key].encode() for key in ('GITHUB_TOKEN', 'GH_TOKEN') if os.environ.get(key)]
        self.item = next(item for item in self.manifest['projects'] if item['project'] == args.project)
        self.env = dict(os.environ, CONFCTL_FLAKE=FLAKE)
        root = Path(args.root).absolute()
        if root.parent != Path('/tmp') or not root.name.startswith('flake-update-guard-d-') or root.is_symlink():
            raise ValueError('Use an owned direct /tmp/flake-update-guard-d-* directory')
        identity = {'slug': SLUG, 'manifest_sha256': file_sha(MANIFEST),
                    'review_receipt_sha256': file_sha(args.review_receipt)}
        if root.exists():
            if not root.is_dir() or root.stat().st_uid != os.getuid():
                raise ValueError('Disposable root is not owned by the executing user')
            if not (root / 'owner.json').is_file() or json.loads((root / 'owner.json').read_text()) != identity:
                raise ValueError('Disposable root ownership does not match')
        else:
            root.mkdir(mode=0o700)
            (root / 'owner.json').write_text(json.dumps(identity, indent=2) + '\n')
        self.out = root / (args.stage + '-' + args.project)
        self.out.mkdir()  # Existing attempts require parent inspection, never an automatic retry.
        self.startup = source
        self.receipt = dict(identity, stage=args.stage, project=args.project, provider_head=PROVIDER,
                            source_head=self.item['head'], source_tree=self.item['tree'], driver_sha256=file_sha(__file__), phase='source',
                            provider_startup_receipt_sha256=file_sha(args.provider_receipt), gcroot_preflight=self.gcroot,
                            started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), commands=[], complete=False)
        self.number = 0
        self.save()

    def redact(self, data):
        for secret in self.secrets:
            data = data.replace(secret, b'<redacted>')
        return data

    def save(self):
        raw = json.dumps(self.receipt, indent=2).encode() + b'\n'
        (self.out / 'receipt.json').write_bytes(self.redact(raw))

    def run(self, argv, label, cwd=None, env=None, permit=(0,)):
        self.number += 1
        record = {'label': label, 'argv': argv, 'cwd': str(cwd) if cwd else None}
        for stream in ('stdout', 'stderr'):
            record[stream] = str(self.out / f'{self.number:03d}-{label}.{stream}')
        started = time.monotonic()
        print(label + ': starting', flush=True)
        process = subprocess.Popen(argv, cwd=cwd, env=env or self.env, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, start_new_session=True)
        record.update(pid=process.pid, pgid=process.pid)
        self.receipt['commands'].append(record)
        self.save()
        kernel, secret_seen = threading.Event(), threading.Event()
        def copy(pipe, target):
            with Path(target).open('wb') as output:
                for line in iter(pipe.readline, b''):
                    filtered = self.redact(line)
                    if filtered != line:
                        secret_seen.set()
                    output.write(filtered); output.flush()
                    if KERNEL.search(line):
                        kernel.set()
            pipe.close()
        threads = [threading.Thread(target=copy, args=(process.stdout, record['stdout'])),
                   threading.Thread(target=copy, args=(process.stderr, record['stderr']))]
        for thread in threads:
            thread.start()
        interrupted = False
        try:
            while process.poll() is None:
                if kernel.is_set() and not interrupted:
                    interrupted = True
                    print('ESCALATE unexpected local kernel build; interrupting owned group ' + str(process.pid), flush=True)
                    os.killpg(process.pid, signal.SIGINT)
                try:
                    process.wait(timeout=0.5)
                except subprocess.TimeoutExpired:
                    pass  # No quiet-build deadline or retry.
        except BaseException:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGINT)
                process.wait()
            raise
        finally:
            for thread in threads:
                thread.join()
            record.update(exit_status=process.returncode, elapsed_seconds=round(time.monotonic() - started, 3),
                          stdout_sha256=file_sha(record['stdout']), stderr_sha256=file_sha(record['stderr']),
                          kernel_interrupt=interrupted, kernel_build_detected=kernel.is_set(),
                          credential_output_redacted=secret_seen.is_set())
            self.save()
        if kernel.is_set():
            self.receipt['kernel_escalation'] = True
            self.save()
        if kernel.is_set() or secret_seen.is_set():
            raise Failed(125 if kernel.is_set() else 2, record)
        if process.returncode not in permit:
            raise Failed(process.returncode, record)
        return Path(record['stdout']), process.returncode

    def source(self):
        repo = self.out / 'checkout'
        self.run(['git', 'clone', '--no-checkout', '--filter=blob:none', '--no-tags', self.item['ssh_remote'], str(repo)], 'clone-exact-source')
        self.run(['git', 'remote', 'set-url', '--push', 'origin', 'disabled://nonpublishing-verification'], 'disable-push', repo)
        push, _ = self.run(['git', 'remote', 'get-url', '--push', 'origin'], 'verify-disabled-push', repo)
        if push.read_text().strip() != 'disabled://nonpublishing-verification':
            raise ValueError('Push URL was not disabled')
        self.run(['git', 'checkout', '--detach', self.item['head']], 'checkout-exact-head', repo)
        head, _ = self.run(['git', 'rev-parse', 'HEAD'], 'verify-source-head', repo)
        tree, _ = self.run(['git', 'rev-parse', 'HEAD^{tree}'], 'verify-source-tree', repo)
        if head.read_text().strip() != self.item['head'] or tree.read_text().strip() != self.item['tree']:
            raise ValueError('Exact source revision/tree mismatch')
        for expected in self.item['source_files']:
            if file_sha(repo / expected['path']) != expected['sha256']:
                raise ValueError('Source content mismatch: ' + expected['path'])
        self.receipt['source_files'] = self.item['source_files']
        return repo

    def state(self, repo, label):
        head, _ = self.run(['git', 'rev-parse', 'HEAD'], label + '-head', repo)
        index, _ = self.run(['git', 'ls-files', '--stage', '-z'], label + '-index', repo)
        committed, _ = self.run(['git', 'show', 'HEAD:flake.lock'], label + '-committed-lock', repo)
        _, staged = self.run(['git', 'diff', '--cached', '--quiet'], label + '-staged-difference', repo, permit=(0, 1))
        return {'head': head.read_text().strip(), 'lock_sha256': file_sha(repo / 'flake.lock'),
                'index_sha256': file_sha(index), 'committed_lock_sha256': file_sha(committed),
                'lock_equals_head': (repo / 'flake.lock').read_bytes() == committed.read_bytes(), 'index_matches_head': staged == 0}

    def retain_provider(self):
        self.run(['nix-store', '--add-root', str(self.out / 'provider-root'), '--indirect', '--realise',
                  self.startup['package_output']], 'retain-verified-provider')
        self.run(['nix', 'path-info', '--json', '--recursive', self.startup['package_output']], 'verified-provider-closure')
        if file_sha(Path(self.startup['package_output']) / 'bin/confctl') != self.startup['wrapper_sha256']:
            raise ValueError('Retained provider differs from startup receipt')
        self.receipt['owned_provider_root'] = str(self.out / 'provider-root')
        self.save()

    def graph_and_shell(self, repo, label):
        metadata, _ = self.run(['nix', 'flake', 'metadata', '--json', '--no-write-lock-file', str(repo)],
                               label + '-metadata', repo)
        archive, _ = self.run(['nix', 'flake', 'archive', '--json', '--no-write-lock-file', str(repo)],
                              label + '-source-archive', repo)
        meta, archived = json.loads(metadata.read_text()), json.loads(archive.read_text())
        if meta['path'] != archived['path']:
            raise ValueError('Source changed between metadata and archive')
        paths = set()
        def collect(item):
            paths.add(item['path'])
            for child in item.get('inputs', {}).values():
                collect(child)
        collect(archived)
        for index, path in enumerate(sorted(paths)):
            self.run(['nix-store', '--add-root', str(self.out / f'{label}-source-{index}'), '--indirect',
                      '--realise', path], f'{label}-retain-source-{index}')
        self.run(['nix', 'path-info', '--json', '--recursive', *sorted(paths)], label + '-source-closure')
        shell = '.#devShells.x86_64-linux.default'
        self.run(['nix', 'derivation', 'show', '--recursive', shell], label + '-shell-derivations', repo)
        built, _ = self.run(['nix', 'build', '--json', '--no-write-lock-file', '--out-link',
                             str(self.out / (label + '-devshell')), shell], label + '-shell-build', repo)
        outputs = sorted({path for item in json.loads(built.read_text()) for path in item['outputs'].values()})
        if len(outputs) != 1:
            raise ValueError('Expected one old config development-shell output')
        self.run(['nix', 'path-info', '--json', '--recursive', *outputs], label + '-shell-closure')
        self.receipt.setdefault('consumer_graphs', {})[label] = {
            'metadata': str(metadata), 'archive': str(archive), 'source_paths': sorted(paths),
            'devshell_output': outputs[0], 'owned_devshell_root': str(self.out / (label + '-devshell')),
            'scope': 'Exact worktree source at this stage; committed final lock is recorded separately'}
        self.save()

    def runtime(self, repo):
        self.receipt['phase'] = 'runtime'
        self.graph_and_shell(repo, 'runtime-baseline')
        runtime = self.out / 'runtime-receipt'
        env = dict(self.env, RUNTIME_RECEIPT=str(runtime), PROBE_INPUT=self.item['probe_input'], PROBE_CHANNELS='1')
        self.run(['nix', 'develop', '-c', 'bash', str(PROBE)], 'actual-package-in-old-config-shell', repo, env)
        actual = json.loads((runtime / 'wrapper-runtime.json').read_text())
        expected_bin = str(Path(self.startup['package_output']) / 'bin/confctl')
        if (actual['provider_binary'] != str(Path(expected_bin).resolve()) or
                actual['bundled_nix'] != self.startup['packaged_nix'] or
                file_sha(expected_bin) != self.startup['wrapper_sha256']):
            raise ValueError('Old-shell runtime differs from the verified provider artifact')
        self.receipt['runtime'] = actual

    def project(self, repo):
        self.receipt['phase'] = 'project'
        runtime = self.out / 'runner-temp'; runtime.mkdir()
        env = dict(self.env, RUNNER_TEMP=str(runtime))
        initial = self.state(repo, 'baseline')
        self.receipt['baseline'] = initial
        self.receipt['baseline_input_graph'] = self.item['lock_data']
        self.receipt['steps'] = []
        self.save()
        for index, step in enumerate(self.item['steps']):
            script = self.out / f'step-{index:02d}.sh'
            script.write_text(step['script'])
            if file_sha(script) != step['script_sha256']:
                raise ValueError('Prepared script hash mismatch')
            self.receipt['steps'].append({key: value for key, value in step.items() if key != 'script'})
            before = self.state(repo, f'step-{index:02d}-before')
            try:
                self.run(['bash', '--noprofile', '--norc', '-e', '-o', 'pipefail', str(script)], f'workflow-step-{index:02d}', repo, env)
                if index == 0:  # The workflow's own baseline copy precedes all Nix/dependency preparation.
                    self.graph_and_shell(repo, 'baseline')
            except Failed as error:
                after = self.state(repo, f'step-{index:02d}-failure')
                output = Path(error.record['stdout']).read_text(errors='replace') + Path(error.record['stderr']).read_text(errors='replace')
                if error.status == 3 and 'Forward-only update rejected:' in output:
                    outcome = 'policy_rejection'
                elif 'Forward-only update could not be verified:' in output:
                    outcome = 'evidence_error'
                elif step['name'] in ('Save input baseline', 'Setup git', 'Install git hooks') or error.record.get('kernel_build_detected') or error.record.get('credential_output_redacted'):
                    outcome = 'fixture_error'
                else:
                    outcome = 'workflow_error'
                self.receipt.update(outcome=outcome, failed_step=step['name'], before_failed_step=before,
                                    after_failed_step=after, earlier_commits_may_remain=True,
                                    preservation_scope='State snapshots bracket the workflow step, not every guarded invocation inside it')
                self.save()
                raise
        final = self.state(repo, 'final')
        final_lock = runtime / 'flake-update-final.lock'
        if not final_lock.is_file() or file_sha(final_lock) != final['committed_lock_sha256']:
            raise ValueError('Final guarded snapshot is not the committed published blob')
        self.run(['git', 'log', '--format=%H %s', self.item['head'] + '..HEAD'], 'generated-commits', repo)
        self.run(['git', 'status', '--porcelain=v1'], 'final-checkout-status', repo)
        self.graph_and_shell(repo, 'final-worktree')
        self.receipt.update(outcome='accepted', final=final, final_input_graph=json.loads(final_lock.read_text()),
                            final_snapshot_sha256=file_sha(final_lock), baseline_snapshot_sha256=file_sha(runtime / 'flake-update-baseline.lock'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=['prepare', 'runtime', 'project'])
    parser.add_argument('project', nargs='?', choices=list(SELECTED))
    parser.add_argument('--root')
    parser.add_argument('--review-receipt')
    parser.add_argument('--provider-receipt')
    parser.add_argument('--manifest-sha256')
    args = parser.parse_args()
    if args.stage == 'prepare':
        prepare(); return 0
    if not all((args.project, args.root, args.review_receipt, args.provider_receipt, args.manifest_sha256)):
        parser.error('execution requires project, owned root, review receipt, successful provider receipt and exact manifest SHA')
    operation = None
    try:
        operation = Operation(args)
        operation.run(['nix', '--version'], 'host-nix-version')
        operation.retain_provider()
        repo = operation.source()
        if args.stage == 'runtime':
            operation.runtime(repo); operation.receipt['outcome'] = 'runtime_passed'
        else:
            operation.project(repo)
        operation.receipt.update(complete=True, exit_status=0)
        return 0
    except Failed as error:
        if operation:
            operation.receipt.setdefault('outcome', 'runtime_error' if operation.receipt.get('phase') == 'runtime' else 'fixture_error')
            operation.receipt.update(exit_status=error.status, failed_command=error.record['label'])
        return error.status
    except (ValueError, OSError, KeyError) as error:
        # Fixed labels/classes only; do not echo arbitrary environment/command error values.
        print('Fixture/preflight error (' + type(error).__name__ + '); parent diagnosis required', file=sys.stderr)
        if operation:
            operation.receipt.update(outcome='fixture_error', exit_status=2, failure_class=type(error).__name__)
        return 2
    finally:
        if operation:
            operation.receipt['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            operation.save()
            print('Receipt:', operation.out / 'receipt.json', flush=True)


if __name__ == '__main__':
    sys.exit(main())

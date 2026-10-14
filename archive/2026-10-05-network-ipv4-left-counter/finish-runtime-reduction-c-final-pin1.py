#!/usr/bin/env python3
"""One canonical final V/W configuration selection, preserving old refs."""
import datetime
import hashlib
import json
import os
import pathlib
import subprocess

T = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
C = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration')
git = '/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git'
nix = '/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix'
old = '2271dff38fe1e78806af1c4bb42a264dfa39902f'
old_base = 'c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a'
new_base = '6e4947b52abe103c582bfab2d0b37a8f17a7c02d'
v = 'ebe4fab3d50a51bda1f94014ca95c73ba2a967a8'
w = 'cce681424b866f6a51cbc0a1e4daa226ed33fc07'
branch = '2026-10-05-network-ipv4-left-counter'
environment = os.environ.copy()
environment['PATH'] = '/home/aither/bin:/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:' + environment.get('PATH', '')
commands = []
def run(arguments, cwd=C, env=environment):
    q = subprocess.run(arguments, cwd=cwd, env=env, capture_output=True, text=True)
    commands.append({'argv': arguments, 'exit_code': q.returncode})
    with (T / 'finish-runtime-reduction-c-final-pin1.native.log').open('a') as output:
        output.write(q.stdout)
        output.write(q.stderr)
    if q.returncode:
        raise RuntimeError('Canonical configuration operation refused; native log retained')
    return q.stdout.strip()
def g(*arguments):
    return run([git, *arguments])
def blob(revision):
    return json.loads(g('show', revision + ':flake.lock'))
def root_input(lock, role):
    return lock['nodes'][lock['nodes'][lock['root']]['inputs'][role]]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

assert run(['/home/aither/bin/dev-session', 'current'], cwd=T) == branch
assert not os.environ.get('DEV_SESSION_SLUG') and not os.environ.get('DEV_SESSION_WORKSPACE')
assert g('rev-parse', 'HEAD') == old and not g('status', '--porcelain')
assert g('branch', '--show-current') == branch
assert g('remote', 'get-url', 'origin') == 'git@github.com:vpsfreecz/vpsfree-cz-configuration.git'
hook = pathlib.Path(g('rev-parse', '--git-path', 'hooks/pre-commit'))
if not hook.is_absolute():
    hook = C / hook
assert hook.is_file() and os.access(hook, os.X_OK)
g('fetch', 'origin', 'master')
assert g('rev-parse', 'origin/master') == new_base
assert g('rev-parse', 'HEAD~2') == old_base
assert g('ls-remote', 'origin', 'refs/heads/' + branch).split()[0] == old
g('branch', 'preserve/finish-network-config-pre-w30', old)
before_lock = blob(old)
rebase_environment = environment.copy()
rebase_environment['GIT_SEQUENCE_EDITOR'] = 'python3 ' + str(T / 'finish-runtime-reduction-c-rebase-editor1.py')
rebase_environment['GIT_EDITOR'] = 'true'
run([git, 'rebase', '-i', '--onto', new_base, old_base], env=rebase_environment)
assert g('rev-parse', 'HEAD^') == new_base
retained_v_commit = g('rev-parse', 'HEAD')
v_lock = blob(retained_v_commit)
assert root_input(v_lock, 'vpsadminServices')['locked']['rev'] == v
run([nix, 'develop', '--no-write-lock-file', '--command', 'confctl', 'inputs', 'channel', 'set', '--commit', '--no-editor', 'vpsadmin-webui', 'vpsadmin-webui', w])
head = g('rev-parse', 'HEAD')
assert g('rev-parse', 'HEAD^') == retained_v_commit and not g('status', '--porcelain')
assert g('rev-list', '--count', new_base + '..HEAD') == '2'
final_lock = blob(head)
assert root_input(final_lock, 'vpsadminServices')['locked']['rev'] == v
assert root_input(final_lock, 'vpsadminWebui')['locked']['rev'] == w
assert root_input(final_lock, 'vpsadminWebui')['inputs']['vpsadmin'] == ['vpsadminServices']
assert g('diff', '--name-only', new_base, head) == 'flake.lock'
changed_nodes = [key for key in set(v_lock['nodes']) | set(final_lock['nodes']) if v_lock['nodes'].get(key) != final_lock['nodes'].get(key)]
assert changed_nodes == ['vpsadminWebui']
assert v_lock['root'] == final_lock['root'] and v_lock['version'] == final_lock['version']
assert g('diff', '--exit-code', old, head, '--', 'flake.nix') == ''
run([git, 'range-diff', old_base + '..cf6203d38a62d589983e00dfd7c3cdaa59fe4c9d', new_base + '..' + retained_v_commit])
g('push', '--force-with-lease=refs/heads/' + branch + ':' + old, 'origin', 'HEAD:refs/heads/' + branch)
assert g('ls-remote', 'origin', 'refs/heads/' + branch).split()[0] == head
for suffix, arguments in [('diff', ['diff', '--binary', '--full-index', new_base, head]), ('history', ['log', '--reverse', '--format=fuller', new_base + '..' + head])]:
    (T / ('finish-runtime-reduction-c-final-pin1.' + suffix)).write_text(g(*arguments) + '\n')
proof = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'project': 'vpsfree-cz-configuration',
    'base': new_base, 'head': head, 'tree': g('rev-parse', 'HEAD^{tree}'), 'retained_v_commit': retained_v_commit,
    'v': v, 'w': w, 'clean': True, 'commits': 2, 'only_generated_path': 'flake.lock', 'only_new_pin_node': changed_nodes,
    'old_preservation_ref': 'preserve/finish-network-config-pre-w30', 'hooks_not_bypassed': True,
    'canonical_command': 'confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui ' + w,
    'generated_messages_preserved': True, 'commands': commands,
    'artifact_sha256': {suffix: sha(T / ('finish-runtime-reduction-c-final-pin1.' + suffix)) for suffix in ['diff', 'history', 'native.log']},
    'scope': 'Canonical configuration input preparation/publication only; no default integration, host build/deployment or production consumption claim.'}
with (T / 'finish-runtime-reduction-c-final-pin1.json').open('x') as output:
    json.dump(proof, output, indent=2)
    output.write('\n')
print(json.dumps({'head': head, 'commits': 2, 'published': True, 'proof': 'finish-runtime-reduction-c-final-pin1.json'}))

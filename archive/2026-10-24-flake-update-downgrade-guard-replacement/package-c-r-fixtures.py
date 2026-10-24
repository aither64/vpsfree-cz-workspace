#!/usr/bin/env python3
"""Focused workflow command contracts; no network, builds, or remote pushes."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

WORKSPACE = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-24-flake-update-downgrade-guard-replacement'
TREE = WORKSPACE / 'worktrees' / SLUG
TOOL = 'github:vpsfreecz/confctl/5436d3d7c36d3d5174eab3c44e3578830749d3db#confctl'
PROJECTS = {
    'haveapi': ('update-nixpkgs.yml', 'Update nixpkgs', 'Push update', 'utils/update-nixpkgs.sh', 11),
    'terraform-provider-vpsadmin': ('update-vpsadmin-flake.yml', 'Update vpsAdmin input', 'Push update', 'tools/update-vpsadmin-flake-input.sh', 9),
    'vpsadminos': ('flake-update.yml', 'Update flake inputs', 'Commit and push changes', None, 9),
    'vpsf-status': ('update-dependencies.yml', 'Update flake input', 'Push changes', None, 11),
    'vpsfree-irc-bot': ('nixpkgs-update.yml', 'Update nixpkgs', 'Push updates', 'tools/update_nixpkgs_flake.sh', 9),
}
REAL_GIT = shutil.which('git')
REAL_RUBY = shutil.which('ruby')
RUBY_ENV = {k: v for k, v in os.environ.items() if k not in ('RUBYOPT', 'BUNDLE_GEMFILE', 'BUNDLE_BIN_PATH', 'BUNDLE_PATH', 'GEM_HOME', 'GEM_PATH')}


def run(args, cwd, env=None, check=True):
    p = subprocess.run(args, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if check and p.returncode:
        raise AssertionError(f'{args}: {p.returncode}\n{p.stdout}')
    return p


def load_workflow(path):
    return json.loads(run([REAL_RUBY, '-ryaml', '-rjson', '-e', 'puts JSON.generate(YAML.load_file(ARGV[0]))', str(path)], TREE, RUBY_ENV).stdout)


def graph(project, rev):
    source = {'type': 'github', 'owner': 'example', 'repo': 'source', 'rev': 'c' * 40}
    nodes = {
        'main': {'inputs': {'vpsadmin': 'arbitrary-parent', 'vpsadminos': ['vpsadmin', 'vpsadminos'], 'nixpkgs': ['vpsadminos', 'nixpkgs']}},
        'arbitrary-parent': {'locked': dict(source), 'inputs': {'vpsadminos': 'arbitrary-os'}},
        'arbitrary-os': {'locked': dict(source), 'inputs': {'nixpkgs': 'renumbered-leaf'}},
        'renumbered-leaf': {'locked': dict(source, repo='nixpkgs', rev=rev)},
    }
    if project in ('haveapi', 'vpsadminos'):
        nodes['main']['inputs'] = {'nixpkgs': 'renumbered-leaf'}
    elif project == 'terraform-provider-vpsadmin':
        nodes['arbitrary-parent']['locked']['rev'] = rev
    return {'root': 'main', 'version': 7, 'nodes': nodes}


MOCK_NIX = r'''#!/usr/bin/env python3
import json, os, pathlib, shutil, subprocess, sys
args=sys.argv[1:]
with open(os.environ['FIXTURE_TRACE'],'a') as f: f.write('nix '+json.dumps(args)+'\n')
if args[:1] == ['shell']:
    if args[1] == 'github:NixOS/nixpkgs/nixos-unstable#jq':
        os.execvp(args[3],args[3:])
    assert args[1] == os.environ['CONFCTL_FLAKE'] and args[2:5] == ['-c','confctl','inputs'], args
    action=args[5]
    if action == 'ls':
        assert args[6]=='--json', args
        if os.environ.get('BAD_METADATA'):
            print('[]'); sys.exit(0)
        code="require 'json'; require 'confctl/flake_lock'; l=ConfCtl::FlakeLock.load('flake.lock'); n=ARGV[0]; puts JSON.generate([{input:n,rev:l.input_info(n)[:rev]}])"
        ruby_env={k:v for k,v in os.environ.items() if k not in ('RUBYOPT','BUNDLE_GEMFILE','BUNDLE_BIN_PATH','BUNDLE_PATH','GEM_HOME','GEM_PATH')}
        sys.exit(subprocess.run([os.environ['REAL_RUBY'],'-I',os.environ['CONFCTL_SOURCE_LIB'],'-e',code,args[7]],env=ruby_env).returncode)
    if action == 'update':
        assert '--forward-only' in args, args
        expected='--all' if os.environ['FIXTURE_PROJECT']=='vpsadminos' else ('vpsadmin' if os.environ['FIXTURE_PROJECT']=='terraform-provider-vpsadmin' else 'nixpkgs')
        assert args[-1]==expected,args
        status=int(os.environ.get('UPDATE_STATUS','0'))
        if status: sys.exit(status)
        if not os.environ.get('NO_CHANGE'): shutil.copyfile(os.environ['FIXTURE_CANDIDATE'],'flake.lock')
        sys.exit(0)
    if action == 'check-update':
        old=pathlib.Path(args[args.index('--old-lock')+1]).resolve()
        assert not old.is_relative_to(pathlib.Path.cwd()),old
        assert old.read_bytes()==pathlib.Path(os.environ['FIXTURE_EXPECTED_OLD']).read_bytes()
        new=pathlib.Path(args[args.index('--new-lock')+1]).resolve()
        assert not new.is_relative_to(pathlib.Path.cwd()),new
        committed=subprocess.check_output([os.environ['REAL_GIT'],'show','HEAD:flake.lock'])
        assert new.read_bytes()==committed,'final check must validate the published HEAD blob'
        sys.exit(int(os.environ.get('CHECK_STATUS','0')))
    raise AssertionError(args)
if args[:2]==['flake','check']: sys.exit(0)
raise AssertionError(args)
'''
MOCK_GIT = r'''#!/usr/bin/env python3
import json,os,sys,subprocess,shutil
args=sys.argv[1:]
if args[:1] in (['commit'],['push']):
    with open(os.environ['FIXTURE_TRACE'],'a') as f:f.write('git '+json.dumps(args)+'\n')
if args[:1]==['push']:sys.exit(0)
if args[:1]==['commit'] and os.environ.get('WORKTREE_DRIFT'):
    status=subprocess.call([os.environ['REAL_GIT']]+args)
    if status==0:shutil.copyfile(os.environ['FIXTURE_DRIFT'],'flake.lock')
    sys.exit(status)
os.execv(os.environ['REAL_GIT'],[os.environ['REAL_GIT']]+args)
'''


def check_project(project):
    filename, update_name, push_name, helper, digits = PROJECTS[project]
    workflow_path = TREE / project / '.github/workflows' / filename
    # Exercise the actual checked-in graph too; equality must require no API.
    code = "require 'confctl/flake_lock'; require 'confctl/inputs/forward_guard'; l=ConfCtl::FlakeLock.load('flake.lock'); r=ConfCtl::Inputs::ForwardGuard.new.validate(l,l); abort(r.issues.join('; ')) unless r.status==:unchanged; puts 'actual lock graph equality passed'"
    run([REAL_RUBY, '-I', str(TREE/'confctl/lib'), '-e', code], TREE/project, RUBY_ENV)
    doc = load_workflow(workflow_path)
    assert doc['env']['CONFCTL_FLAKE'] == TOOL
    assert doc['env']['GITHUB_TOKEN'] == '${{ secrets.GITHUB_TOKEN }}'
    steps = doc['jobs']['update']['steps']
    by_name = {step.get('name'): step for step in steps}
    update = by_name[update_name]['run']
    push = by_name[push_name]['run']
    assert 'check-update' in push and push.index('check-update') < push.index('git push')
    assert '--force' not in push and 'git pull' not in push and 'git rebase' not in push
    for step in steps:
        if 'run' in step:
            p = subprocess.run(['bash', '-n'], input=step['run'], text=True, capture_output=True)
            assert p.returncode == 0, (step.get('name'), p.stderr)
    assert len([1 for line in workflow_path.read_text().splitlines() if 'CONFCTL_FLAKE:' in line]) == 1

    scenarios = [('forward', 0, 0), ('rejected', 3, 0), ('evidence-error', 1, 0), ('final-rejected', 0, 3), ('final-error', 0, 1), ('worktree-drift', 0, 0)]
    if helper or project == 'vpsf-status':
        scenarios += [('unmatched-metadata', 0, 0)]
    if helper:
        scenarios += [('unchanged', 0, 0), ('missing-tool', 0, 0)]
    for scenario, update_status, check_status in scenarios:
        with tempfile.TemporaryDirectory(prefix=f'flake-{project}-') as tmp:
            base = Path(tmp)
            repo = base / 'repo'
            repo.mkdir()
            bins = base / 'bin'
            bins.mkdir()
            for name, text in [('nix', MOCK_NIX), ('git', MOCK_GIT)]:
                p = bins / name
                p.write_text(text)
                p.chmod(0o755)
            if helper:
                p = repo / helper
                p.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(TREE / project / helper, p)
            if project == 'vpsadminos':
                p = repo / '.github/workflows/scripts/flake-update-commit-message.rb'
                p.parent.mkdir(parents=True)
                shutil.copy2(TREE / project / '.github/workflows/scripts/flake-update-commit-message.rb', p)
            # Existing vpsAdminOS formatter assumes root; ordinary fixtures exercise non-root IDs.
            old = graph(project, 'a' * 40)
            new = graph(project, 'b' * 40)
            if project == 'vpsadminos':
                old['nodes']['root'] = old['nodes'].pop('main'); old['root'] = 'root'
                new['nodes']['root'] = new['nodes'].pop('main'); new['root'] = 'root'
            (repo / 'flake.lock').write_text(json.dumps(old))
            (repo / 'flake.nix').write_text('{}')
            drift = base / 'drift.lock'
            drift.write_text(json.dumps(graph(project, 'd' * 40)))
            candidate = base / 'candidate.lock'
            candidate.write_text(json.dumps(new))
            baseline = base / 'baseline.lock'
            shutil.copy2(repo / 'flake.lock', baseline)
            expected = base / 'expected.lock'
            shutil.copy2(baseline, expected)
            run([REAL_GIT, 'init', '-q'], repo)
            run([REAL_GIT, 'config', 'user.name', 'Fixture'], repo)
            run([REAL_GIT, 'config', 'user.email', 'fixture@example.invalid'], repo)
            run([REAL_GIT, 'add', '.'], repo)
            msg = base / 'initial-message'
            msg.write_text('Initial fixture\n')
            run([REAL_GIT, 'commit', '-q', '-F', str(msg)], repo)
            head = run([REAL_GIT, 'rev-parse', 'HEAD'], repo).stdout.strip()
            trace = base / 'trace'
            trace.touch()
            env = dict(os.environ, PATH=str(bins)+os.pathsep+os.environ['PATH'], CONFCTL_FLAKE=TOOL,
                       REAL_GIT=REAL_GIT, REAL_RUBY=REAL_RUBY, FIXTURE_TRACE=str(trace),
                       CONFCTL_SOURCE_LIB=str(TREE/'confctl/lib'), FIXTURE_PROJECT=project,
                       FIXTURE_CANDIDATE=str(candidate), FIXTURE_EXPECTED_OLD=str(expected), FIXTURE_DRIFT=str(drift),
                       UPDATE_OLD_LOCK=str(baseline), UPDATE_START_REF=head, RUNNER_TEMP=str(base), GITHUB_REF_NAME='master',
                       GITHUB_OUTPUT=str(base/'outputs'), UPDATE_STATUS=str(update_status), CHECK_STATUS=str(check_status))
            if scenario == 'unmatched-metadata': env['BAD_METADATA'] = '1'
            if scenario == 'unchanged': env['NO_CHANGE'] = '1'
            if scenario == 'missing-tool': env.pop('CONFCTL_FLAKE')
            if scenario == 'worktree-drift': env['WORKTREE_DRIFT'] = '1'
            p = run(['bash', '-euo', 'pipefail', '-c', update], repo, env, False)
            successful_update = scenario in ('forward', 'final-rejected', 'final-error', 'unchanged', 'worktree-drift')
            assert (p.returncode == 0) == successful_update, (project, scenario, p.returncode, p.stdout)
            events = trace.read_text()
            if not successful_update:
                assert 'git ["commit"' not in events and 'git ["push"' not in events, (scenario, events)
                assert run([REAL_GIT, 'rev-parse', 'HEAD'], repo).stdout.strip() == head
                assert (repo/'flake.lock').read_bytes() == baseline.read_bytes()
                continue
            if scenario == 'unchanged':
                assert 'git ["commit"' not in events
                continue
            # HaveAPI push output conditional is already true after its successful helper commit.
            push_code = push.replace('${{ github.event.repository.default_branch }}', 'master')
            p = run(['bash', '-euo', 'pipefail', '-c', push_code], repo, env, False)
            events = trace.read_text()
            assert (p.returncode == 0) == (check_status == 0), (project, scenario, p.stdout)
            assert ('git ["push"' in events) == (check_status == 0), (project, scenario, events)
            subject = run([REAL_GIT, 'log', '-1', '--format=%s'], repo).stdout.strip()
            target = 'vpsadmin' if project == 'terraform-provider-vpsadmin' else 'nixpkgs'
            assert subject == f'flake: {target} '+ 'a'*digits+' -> '+'b'*digits, (project, subject)
            assert baseline.read_bytes() == expected.read_bytes()
    print(f'{project}: {len(scenarios)} scenarios passed, inline shell syntax and publication contract passed')


for name in sys.argv[1:] or PROJECTS:
    check_project(name)

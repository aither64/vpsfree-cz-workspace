#!/usr/bin/env python3
"""Check actual cache YAML and model GHA scheduling; shell bodies have separate fixtures."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-24-flake-update-downgrade-guard-replacement'
TREE = ROOT / 'worktrees' / SLUG
PROJECTS = {
    'haveapi': ('update-nixpkgs.yml', 'Update nixpkgs', 'Push update'),
    'terraform-provider-vpsadmin': ('update-vpsadmin-flake.yml', 'Update vpsAdmin input', 'Push update'),
    'vpsadminos': ('flake-update.yml', 'Update flake inputs', 'Commit and push changes'),
    'vpsf-status': ('update-dependencies.yml', 'Update flake input', 'Push changes'),
    'vpsfree-irc-bot': ('nixpkgs-update.yml', 'Update nixpkgs', 'Push updates'),
    'vpsfree-cz-configuration': ('daily-update.yml', 'Update inputs', 'Check and push updates'),
    'vpsadminos-org-configuration': ('daily-update.yml', 'Update flake inputs', 'Check and push updates'),
}
KEY = 'confctl-cache-${{ runner.os }}-${{ github.run_id }}'
PREFIX = 'confctl-cache-${{ runner.os }}'
SAVE_IF = '${{ !cancelled() }}'


def load(project):
    filename, update, push = PROJECTS[project]
    path = TREE / project / '.github/workflows' / filename
    env = {k: v for k, v in os.environ.items()
           if not (k.startswith('BUNDLE') or k.startswith('GEM_') or k in ('RUBYOPT', 'RUBYLIB'))}
    result = subprocess.run([shutil.which('ruby'), '-ryaml', '-rjson', '-e',
                             'puts JSON.generate(YAML.load_file(ARGV[0]))', str(path)],
                            env=env, capture_output=True, text=True, check=True)
    document = json.loads(result.stdout)
    assert document['env']['GITHUB_TOKEN'] == '${{ secrets.GITHUB_TOKEN }}'
    steps = document['jobs']['update']['steps']
    return steps, update, push


def validate(steps, update, push):
    restore = [s for s in steps if s.get('uses', '').startswith('actions/cache/restore@')]
    save = [s for s in steps if s.get('uses', '').startswith('actions/cache/save@')]
    assert len(restore) == len(save) == 1
    restore, save = restore[0], save[0]
    assert restore['uses'] == 'actions/cache/restore@v6'
    assert save['uses'] == 'actions/cache/save@v6'
    assert restore['with'] == {'path': '~/.cache/confctl', 'key': KEY, 'restore-keys': PREFIX + '\n'}
    assert save['with'] == {'path': '~/.cache/confctl', 'key': KEY}
    assert 'if' not in restore and not restore.get('continue-on-error', False)
    assert save.get('if') == SAVE_IF and not save.get('continue-on-error', False)
    by_name = {s.get('name'): s for s in steps}
    assert steps.index(restore) < steps.index(by_name[update]) < steps.index(by_name[push]) < steps.index(save)
    for step in steps:
        assert 'cache-hit' not in str(step.get('if', ''))
        if 'run' in step:
            assert '!cancelled()' not in str(step.get('if', ''))
            result = subprocess.run(['bash', '-n'], input=step['run'], text=True, capture_output=True)
            assert result.returncode == 0, (step.get('name'), result.stderr)
    return restore, save


def scheduling(steps, update, push, warm, update_exit=0, final_exit=0, cancelled=False, save_exit=0):
    """Model only GHA cache scheduling, with opaque guard outcomes, never ancestry."""
    with tempfile.TemporaryDirectory(prefix='confctl-c7-cache-') as directory:
        cache = Path(directory) / 'opaque-cache'
        if warm:
            cache.mkdir()
            (cache / 'prior-history').write_text('prior fixture data')
        events = []
        first_failure = 0
        was_cancelled = False
        for step in steps:
            uses = step.get('uses', '')
            if uses.startswith('actions/cache/save@'):
                if step.get('if') == SAVE_IF and not was_cancelled:
                    events.append('save')
                    assert (cache / 'downloaded-history').exists()
                    if not first_failure:
                        first_failure = save_exit
                continue
            if first_failure or was_cancelled:
                continue
            if uses.startswith('actions/cache/restore@'):
                events.append('restore-hit' if warm else 'restore-miss')
                continue
            if step.get('name') == update:
                events.append('guard')
                cache.mkdir(exist_ok=True)
                (cache / 'downloaded-history').write_text('fetched fixture data')
                first_failure = update_exit
                if cancelled:
                    was_cancelled = True
                    first_failure = 130
            elif step.get('name') == push:
                events.append('final-check')
                first_failure = final_exit
                if not first_failure:
                    events.append('push')
        return first_failure, events


def check(project):
    steps, update, push = load(project)
    validate(steps, update, push)
    cases = [('success', 0, 0, False, 0), ('update-reject', 3, 0, False, 0),
             ('update-error', 1, 0, False, 0), ('final-reject', 0, 3, False, 0),
             ('final-error', 0, 1, False, 0), ('cancelled', 0, 0, True, 0),
             ('rejected-save-error', 3, 0, False, 1)]
    for warm in [False, True]:
        for case, update_exit, final_exit, cancelled, save_exit in cases:
            status, events = scheduling(steps, update, push, warm, update_exit, final_exit, cancelled, save_exit)
            expected = 130 if cancelled else update_exit or final_exit or save_exit
            assert status == expected, (project, case, status, events)
            assert events[0] == ('restore-hit' if warm else 'restore-miss')
            assert events.count('guard') == 1, (project, case, events)
            assert ('save' in events) == (not cancelled), (project, case, events)
            assert ('push' in events) == (not expected), (project, case, events)
            if update_exit or cancelled:
                assert 'final-check' not in events
            if not cancelled:
                assert events[-1] == 'save'
    # These mutations detect the two regressions this adoption must prevent.
    for kind in ['success-only-save', 'skip-guard-on-hit']:
        changed = copy.deepcopy(steps)
        if kind == 'success-only-save':
            next(s for s in changed if s.get('uses', '').startswith('actions/cache/save@')).pop('if')
        else:
            next(s for s in changed if s.get('name') == update)['if'] = "steps.cache.outputs.cache-hit != 'true'"
        try:
            validate(changed, update, push)
        except AssertionError:
            pass
        else:
            raise AssertionError('negative control escaped: ' + kind)
    print(f'{project}: cache YAML, 14 scheduling scenarios and 2 negative controls passed')


if __name__ == '__main__':
    for project in sys.argv[1:] or PROJECTS:
        check(project)

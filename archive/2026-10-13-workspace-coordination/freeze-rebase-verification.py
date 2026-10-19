from pathlib import Path
import hashlib
import json
import os
import subprocess

root = Path('/home/aither/workspace/ai/vpsfree.cz')
tracking = root / 'work/2026-10-13-workspace-coordination'
generations = root / 'worktrees/2026-10-13-workspace-coordination/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev'
old_path = generations / '2026-10-14--00-11-18/generation.json'
new_path = generations / '2026-10-14--12-45-16/generation.json'
old = json.loads(old_path.read_text())
new = json.loads(new_path.read_text())
assert (tracking / 'integration-rebase-verification.status').read_text().strip() == '0'
assert (tracking / 'configuration-rebase-build.status').read_text().strip() == '0'
assert old['inputs'] == new['inputs']
assert old['inputs_info'] == new['inputs_info']
assert new['inputs_info']['devWorkspace']['rev'] == 'a10af6c4539c4c7a6a97a883d89825346d5451ad'
old_top = Path(old['toplevel'])
new_top = Path(new['toplevel'])
old_etc = os.readlink(old_top / 'etc')
new_etc = os.readlink(new_top / 'etc')

def inventory(path):
    result = {}
    def visit(current, relative, ancestors):
        if current.is_symlink() and (not current.exists() or not str(current.resolve()).startswith('/nix/store/')):
            result[relative] = ('link', os.readlink(current))
        elif current.is_dir():
            resolved = str(current.resolve())
            assert resolved not in ancestors, relative
            for child in current.iterdir():
                visit(child, str(Path(relative) / child.name), ancestors | {resolved})
        elif current.is_file():
            result[relative] = ('file', hashlib.sha256(current.read_bytes()).hexdigest())
        else:
            raise AssertionError(relative)
    visit(path, '', set())
    return result

before_etc = inventory(old_top / 'etc')
after_etc = inventory(new_top / 'etc')
etc_changes = [name for name in sorted(before_etc.keys() | after_etc.keys()) if before_etc.get(name) != after_etc.get(name)]
assert etc_changes == ['confctl/configuration-info.json'], etc_changes
assert json.loads((new_top / 'etc/confctl/configuration-info.json').read_text()) == {
    'revision': '9a481ba1c69a0f22a7e84e3353d676911df2271e', 'revisionDirty': False, 'schemaVersion': 1}
assert {p.name for p in old_top.iterdir()} == {p.name for p in new_top.iterdir()}
changed = []

def compare(before, after, relative):
    if before.is_symlink() and after.is_symlink():
        if os.readlink(before) != os.readlink(after):
            assert relative == 'etc'
            changed.append(relative)
    elif before.is_dir() and after.is_dir():
        assert {p.name for p in before.iterdir()} == {p.name for p in after.iterdir()}
        for child in before.iterdir():
            compare(child, after / child.name, str(Path(relative) / child.name))
    else:
        assert before.is_file() and after.is_file()
        first = before.read_bytes()
        second = after.read_bytes()
        if first != second:
            replaced = first.replace(str(old_top).encode(), str(new_top).encode()).replace(old_etc.encode(), new_etc.encode())
            assert replaced == second, relative
            changed.append(relative)

for child in old_top.iterdir():
    compare(child, new_top / child.name, child.name)
assert str(Path('/run/current-system').resolve()) == str(old_top)
assert str(Path('/nix/var/nix/profiles/system').resolve()) == str(old_top)
app = json.loads((tracking / 'bootstrap-rebase-application-equivalence.json').read_text())
assert app['before'] == app['after']

def ref(path):
    return {'path': str(path.relative_to(root)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

result = {
    'schema': 1, 'outcome': 'passed',
    'configurationHead': '9a481ba1c69a0f22a7e84e3353d676911df2271e',
    'workspaceHead': 'b78dc0a4105c065af3aed75f780cef93f7d0e924',
    'verificationCommand': 'bash work/2026-10-13-workspace-coordination/integration-rebase-verification.sh',
    'execution': 'documented host parent-monitor fallback after diagnosed sandbox GC-root restriction',
    'checks': {'configurationBuild': True, 'deploymentContract': True, 'agentInstructions': True,
               'identicalEvaluatedInputs': True, 'metadataAndSelfReferencesOnly': True,
               'applicationDerivationUnchanged': True, 'noActivation': True},
    'deployedGeneration': ref(old_path), 'rebuiltGeneration': ref(new_path),
    'deployedSystem': str(old_top), 'rebuiltSystem': str(new_top),
    'inputsInfo': new['inputs_info'], 'etcSemanticDifferences': etc_changes,
    'systemChangedPaths': sorted(changed),
    'differenceExplanation': 'Only confctl configuration revision changes; derived etc and toplevel self references follow it. Kernel, initrd, services and all evaluated inputs are unchanged. No redeployment is needed.',
    'logs': [ref(tracking / name) for name in ['configuration-rebase-build.log', 'integration-rebase-workspace-checks.log']],
    'applicationEquivalence': ref(tracking / 'bootstrap-rebase-application-equivalence.json'),
    'configurationCI': 'No configured workflow; scoped confctl build is applicable verification',
}
destination = tracking / 'integration-rebase-acceptance.json'
with destination.open('x') as output:
    json.dump(result, output, indent=2)
    output.write('\n')
print(json.dumps({'outcome': result['outcome'], 'systemChangedPaths': result['systemChangedPaths']}))

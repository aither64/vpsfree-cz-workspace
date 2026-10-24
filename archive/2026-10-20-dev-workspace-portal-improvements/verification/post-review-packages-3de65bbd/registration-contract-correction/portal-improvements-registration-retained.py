import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path('/home/aither/workspace/ai/vpsfree.cz')
slug = '2026-10-20-dev-workspace-portal-improvements'
sources = root / 'worktrees' / slug
logs = root / 'work' / slug / 'verification/post-review-packages-3de65bbd'
revisions = {
    'workspace': '3de65bbd0e90f0c3b19e0d64ed925158155647a6',
    'dev-workspace': 'db25364999aa4bf12b67506662a08e9e464bee33',
    'codex-web': '852e8c51091512bc79ca6c921ef1f5ccc46a9535',
}
for name, revision in revisions.items():
    assert subprocess.check_output(['git', '-C', str(sources / name), 'rev-parse', 'HEAD'], text=True).strip() == revision
    assert not subprocess.check_output(['git', '-C', str(sources / name), 'status', '--porcelain'])

retained_hashes = {
    'workspace.json': 'c4ee24e717b0e4f491fdf3f55d8c51d8b016461526591a9e4daaf8f50bcb818c',
    'workspace-package.path': '27062a7a26ae099a3cd8fad1988b03f683a937313d95c1e1f98ffd59b09ee20a',
    'registration.json': '7c2aae0c4712878158272a04bc3eda52aa2dc831e3e42cba7b651152cf7f7a36',
    'registration.log': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'metadata-assertions.log': '0a0ce8c1c703264e87078dc18c01535c5e1537f9ae23479a8d6aadd484f8ea38',
}
for name, digest in retained_hashes.items():
    assert hashlib.sha256((logs / name).read_bytes()).hexdigest() == digest, name
original_launcher = Path('/tmp/portal-improvements-post-review-packages.before-registration-correction.sh')
assert hashlib.sha256(original_launcher.read_bytes()).hexdigest() == '3524756528ccaa83a360cca18f6c13cee29b7c942e7369dd4a8c491d2ec1bd4a'
assert hashlib.sha256(Path('/tmp/portal-improvements-post-review-metadata.py').read_bytes()).hexdigest() == '49a3bbc44558ad178fbab008945ba1956ffd1068dda83ac0dd870c1ddbfc9e16'

drv = '/nix/store/6vf82012b1ljprmznm2jcdizml8g6spx-dev-workspace-0.2.0.drv'
package = '/nix/store/5d43h2q5q7d494l6v718l71lfk0sm5in-dev-workspace-0.2.0'
receipt = json.loads((logs / 'workspace.json').read_text())
assert receipt[0] == {'drvPath': drv, 'outputs': {'out': package}}
assert (logs / 'workspace-package.path').read_text().strip() == package
assert subprocess.check_output(['nix-store', '--query', '--outputs', drv], text=True).strip() == package
data = json.loads(subprocess.check_output(['nix', 'derivation', 'show', drv], text=True))
derivations = data.get('derivations', data)
assert len(derivations) == 1
derivation = next(iter(derivations.values()))
assert derivation['env']['out'] == package
source = Path(derivation['env']['src'])
assert str(source) == '/nix/store/l2wg4c2qgg4c8a4nmndh8dpa2bskxkdh-source'
path_info = json.loads(subprocess.check_output(['nix', 'path-info', '--json', str(source)], text=True))
lock = json.loads((sources / 'workspace/flake.lock').read_text())
runtime = lock['nodes']['dev-workspace']['locked']
shared = lock['nodes']['codex-web']['locked']
assert runtime['rev'] == revisions['dev-workspace']
assert shared['rev'] == revisions['codex-web']
assert runtime['narHash'] == path_info[str(source)]['narHash'] == 'sha256-YF9+Yd24UK8KbrGcuklUtTW2qSAlVz1TZahRBv9lzyw='
assert shared['narHash'] == 'sha256-6dAMMwgGkCJVxUGyckpzyir6ETxpVHvI0w4b00ZQbIc='
assert json.loads((source / 'flake.lock').read_text())['nodes']['codex-web']['locked'] == shared
assert lock['nodes']['vpsfree-dev-workspace']['locked']['rev'] == '767dfd587e346168e1443e65ccdb67ce748f3fe3'

batch_log = (logs.parent / 'packages-3de65bbd.log').read_text()
assert all('Passed ' + name in batch_log for name in ('workspace', 'codex-web', 'dev-workspace'))
assert 'AssertionError' in batch_log
assert 'exit=1\n' in (logs.parent / 'packages-3de65bbd-result.txt').read_text()
print('Exact clean A/B/C, original helper hashes, unchanged stage/metadata/registration receipts and derivation/input identities verified', flush=True)
subprocess.run([
    sys.executable, '/tmp/portal-improvements-post-review-registration.py',
    str(logs / 'registration.json'), package,
    str(logs / 'disposable-registration/state'),
    str(logs / 'disposable-registration/workspace'),
], check=True)
print('PASS: corrected pure postcondition on ORIGINAL actual registration output; no package build, realization, metadata or CLI rerun')

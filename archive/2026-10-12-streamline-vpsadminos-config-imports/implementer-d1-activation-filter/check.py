from pathlib import Path
import hashlib
import re
import shlex
import subprocess

artifact = Path(__file__).resolve().parent
repo = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos')
relative = 'image-scripts/tests/nixos_rebuild.sh'
base = '6d8c92b57151721701efce5578739a11678d03aa'
script = repo / relative
source = script.read_text()
log = []


def run(arguments, **kwargs):
    result = subprocess.run(arguments, cwd=repo, capture_output=True, text=True, **kwargs)
    log.append(f'$ {shlex.join(arguments)}\nexit {result.returncode}\n{result.stdout}{result.stderr}')
    (artifact / 'checks.log').write_text('\n'.join(log))
    assert result.returncode == 0, result.stderr
    return result.stdout


head = run(['git', 'rev-parse', 'HEAD']).strip()
assert head == base, head
original = run(['git', 'show', f'{base}:{relative}'])
old_lines = original.splitlines()
new_lines = source.splitlines()
assert len(old_lines) == len(new_lines)
changed = [i for i, pair in enumerate(zip(old_lines, new_lines), 1) if pair[0] != pair[1]]
assert changed == [133], changed
assert run(['git', 'diff', '--name-only']).strip() == relative
assert run(['git', 'diff', '--cached', '--name-only']).strip() == ''
run(['bash', '-n', relative])
fragments = re.findall(r"\bbash -c '([^']*)'", source, flags=re.S)
assert len(fragments) == 4, len(fragments)
for i, fragment in enumerate(fragments, 1):
    fragment_file = artifact / f'nested-fragment-{i}.sh'
    fragment_file.write_text(fragment + '\n')
    run(['bash', '-n', str(fragment_file)])
run(['git', 'diff', '--check'])

old_pattern = shlex.split(old_lines[132])[3]
pattern = shlex.split(new_lines[132])[3]
assert pattern.endswith(old_pattern), 'Original filter alternatives must be retained'
fixture = artifact / 'activation-fixture.sh'
baseline = run(['grep', '-n', '-E', old_pattern, str(fixture)])
(artifact / 'baseline-output.txt').write_text(baseline)
output = run(['grep', '-n', '-E', pattern, str(fixture)])
(artifact / 'filter-output.txt').write_text(output)
selected = [int(line.split(':', 1)[0]) for line in output.splitlines()]
expected = [5, 6, 7, 9, 11, 12, 13, 14, 16, 17, 18, 22]
assert selected == expected, selected
fixture_lines = fixture.read_text().splitlines()
assert output == ''.join(f'{i}:{fixture_lines[i - 1]}\n' for i in expected)
assert [int(line.split(':', 1)[0]) for line in baseline.splitlines()] == [12, 13, 14, 17, 18]

diff = run(['git', 'diff', '--', relative])
(artifact / 'source.diff').write_text(diff)
summary = (
    f'PASS: base/head {head}; only source line 133 changed; index unchanged.\n'
    'PASS: outer Bash syntax and all four nested fragments; git diff --check.\n'
    f'PASS: filter selected original fixture lines {selected} in unchanged order.\n'
    'Fixture is synthetic and was only read by grep; no guest or Nix operation ran.\n'
    f'Source SHA256: {hashlib.sha256(script.read_bytes()).hexdigest()}\n'
)
(artifact / 'summary.txt').write_text(summary)
(artifact / 'checks.status').write_text('0\n')
print(summary, end='')

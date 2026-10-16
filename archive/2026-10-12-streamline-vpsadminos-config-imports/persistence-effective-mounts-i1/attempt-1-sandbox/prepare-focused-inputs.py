#!/usr/bin/env python3
"""Compose literal helper delta into retained evaluated inputs; never run them."""
from pathlib import Path
import hashlib
import json
import shlex
import subprocess
import textwrap

out = Path(__file__).resolve().parent
session = out.parent
product = session.parents[1] / 'worktrees' / session.name / 'vpsadminos'
for entry in json.loads((out / 'frozen-sha256.json').read_text()):
    assert hashlib.sha256((product / entry['path']).read_bytes()).hexdigest() == entry['sha256']
name = 'os/lib/nixos-container/stable/vpsadminos-26.05.nix'
def helper(text):
    start = text.index('    vpsadminosPrepareStateDirectory() {')
    end = text.index('    vpsadminosMountRequired() {', start)
    return textwrap.dedent(text[start:end])
old = helper((out / 'original' / name).read_text())
new = helper((product / name).read_text())
commands = [shlex.split(line) for line in (session / 'effective-mounts-quick/retained-shell-checks.sh').read_text().splitlines() if line.startswith('bash ')]
assert len(commands) == 30
focus = out / 'focused-inputs'
focus.mkdir(exist_ok=False)
rows = []
invocations = ['#!/usr/bin/env bash', 'set -euo pipefail', '# Parent execution only: retained evaluated body with the exact literal I1 helper delta.']
for index, argv in enumerate(commands):
    assert len(argv) == 6 and argv[0] == 'bash'
    source, mounts = Path(argv[2]), Path(argv[3])
    text = source.read_text()
    assert text.count(old) == 1, source
    updated = text.replace(old, new, 1)
    assert updated.replace(new, old, 1) == text
    snippet = focus / f'{index:02d}-snippet.sh'
    calls = focus / f'{index:02d}-mounts.sh'
    snippet.write_text(updated)
    calls.write_bytes(mounts.read_bytes())
    # Syntax only, no sourced callbacks or harness execution.
    for path in [snippet, calls]:
        subprocess.run(['bash', '-n', str(path)], check=True)
    rows.append({'index': index, 'mode': argv[4], 'original_snippet': str(source), 'original_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'snippet_sha256': hashlib.sha256(snippet.read_bytes()).hexdigest(), 'mounts_sha256': hashlib.sha256(calls.read_bytes()).hexdigest(), 'inverse_byte_equal': True})
    invocations.append(shlex.join(['bash', str(product / 'tests/nixos-container-persistence-shell.sh'), str(snippet), str(calls), argv[4], argv[5]]))
(out / 'focused-shell-checks.sh').write_text('\n'.join(invocations) + '\n')
(out / 'focused-inputs-receipt.json').write_text(json.dumps({'old_helper_sha256': hashlib.sha256(old.encode()).hexdigest(), 'new_helper_sha256': hashlib.sha256(new.encode()).hexdigest(), 'inputs': rows}, indent=2) + '\n')
print('Prepared 30 retained callback inputs with only literal helper substitution; inverse byte equality and 60 Bash syntax checks pass. No callbacks or harness executed.')

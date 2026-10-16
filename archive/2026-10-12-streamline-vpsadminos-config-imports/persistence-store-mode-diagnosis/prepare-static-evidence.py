#!/usr/bin/env python3
"""Session-only scope comparison and syntax fixtures; no Nix or runtime work."""
import hashlib
import json
from pathlib import Path
import subprocess
import textwrap

out = Path(__file__).resolve().parent
session = out.parent
product = session.parents[1] / "worktrees" / session.name / "vpsadminos"
relative = "tests/suite/dist-config/nixos-persistence-upgrade.nix"
before = subprocess.check_output(["git", "-C", str(product), "show", "HEAD:" + relative]).decode()
after = (product / relative).read_text()
addition = (
    "              # The fresh dataset root is 0750; /nix needs non-root traversal.\n"
    "              chmod 0755 \"#{nix_root}\"\n"
)
anchor = '              set -e\n              mkdir -p "#{nix_root}/store"\n'
assert before.count(anchor) == 1
assert after == before.replace(anchor, anchor.replace('              mkdir', addition + '              mkdir'), 1)
assert after.count(addition) == 1
assert after.replace(addition, '', 1) == before
assert hashlib.sha256(before.encode()).hexdigest() == '2354e5ab31f0180e7bb5fec6d472e91e5ccbc61aaef4d9162c3dfa09dc0fcb83'
(out / 'scope-comparison.txt').write_text(
    'PASS: current suite is exactly HEAD plus the expected comment/chmod lines.\n'
    'PASS: inverse removal restores HEAD byte-for-byte.\n'
    'PASS: HEAD suite matches the previous frozen private-store setup SHA256.\n'
    'All other source, generations, storage, diagnostics and assertions are unchanged.\n'
)
(out / 'mode-setup.patch').write_bytes(subprocess.check_output(['git', '-C', str(product), 'diff', '--', relative]))

# Amend retained evaluated Ruby text only for syntax, not execution/evaluation.
scripts = out / 'static-ruby'
scripts.mkdir(exist_ok=True)
for path in sorted((session / 'store-fixture-generated-scripts').glob('*.rb')):
    ruby = path.read_text()
    ruby_anchor = '      set -e\n      mkdir -p "#{nix_root}/store"\n'
    assert ruby.count(ruby_anchor) == 1, path
    ruby_addition = textwrap.dedent(addition)
    amended = ruby.replace(ruby_anchor, '      set -e\n' + textwrap.indent(ruby_addition, '      ') + '      mkdir -p "#{nix_root}/store"\n', 1)
    (scripts / path.name).write_text(
        '# Static amendment of retained evaluated script; not reevaluated or executed.\n' + amended
    )
assert len(list(scripts.glob('*.rb'))) == 8
shell = after.split('            machine.succeeds(<<~SHELL)\n', 1)[1].split('            SHELL\n', 1)[0]
shell = textwrap.dedent(shell).replace('#{nix_root}', '/fixture/nix').replace('${registration}', '/fixture/registration')
(out / 'store-copy-template.sh').write_text(shell)

logs = Path('/tmp/ni.ljm4450b/os-test-dist-config__nixos-persistence-upgrade-8c45b496')
paths = list(sorted(logs.glob('*.log'))) + [logs / 'test-result.txt']
paths += list(sorted((session / 'runtime-attempt.dymifpby').glob('*')))
manifest = []
for path in paths:
    if not path.is_file():
        continue
    data = path.read_bytes()
    manifest.append({'path': str(path), 'bytes': len(data), 'lines': len(data.splitlines()), 'sha256': hashlib.sha256(data).hexdigest()})
(out / 'original-logs.json').write_text(json.dumps(manifest, indent=2) + '\n')
lines = (logs / 'machine-shell.log').read_text().splitlines()
(out / 'all-command-statuses.txt').write_text('\n'.join(
    f'{i}: {line}' for i, line in enumerate(lines, 1)
    if line.startswith(('COMMAND:', 'STATUS:', 'ERROR:', 'ACTION:'))
) + '\n')
print((out / 'scope-comparison.txt').read_text(), end='')
print('Prepared eight static Ruby amendments and copy Bash syntax fixture.')

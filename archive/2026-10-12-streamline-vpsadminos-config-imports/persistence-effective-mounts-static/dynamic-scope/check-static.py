#!/usr/bin/env python3
"""Run only the approved parser/formatter/syntax/whitespace checks."""
import json
from pathlib import Path
import subprocess
import sys

out = Path(__file__).resolve().parent
session = out.parent
product = session.parents[1] / 'worktrees' / session.name / 'vpsadminos'
owned = [entry['path'] for entry in json.loads((out / 'owned-sha256.json').read_text())]
nix = [name for name in owned if name.endswith('.nix')]
checks = [('nixfmt', ['/nix/store/ffrsk7yvqqmlj7d40hs2prkqgly2gr2q-nixfmt-1.5.0/bin/nixfmt', '--check', *nix])]
checks += [('parse ' + name, ['nix-instantiate', '--parse', name]) for name in nix]
checks += [('bash ' + str(path), ['bash', '-n', str(path)]) for path in [
    product / 'tests/nixos-container-persistence-shell.sh',
    out / 'helpers-template.sh', out / 'store-copy-template.sh', out / 'readiness-template.sh',
]]
checks += [
    ('Ruby static template', ['/nix/store/m0nfdb4mhfgwkgss4ymyqmvviwy30i6y-ruby-3.4.9/bin/ruby', '-c', str(out / 'suite-template.rb')]),
    ('whitespace', ['git', 'diff', '--check']),
    ('index unchanged/empty', ['git', 'diff', '--cached', '--quiet']),
    ('latest stable identical', ['cmp', owned[1], owned[2]]),
]
results = []
with (out / 'static-checks.log').open('w') as log:
    for name, argv in checks:
        log.write(f'CHECK {name}\nCOMMAND {json.dumps(argv)}\n')
        log.flush()
        status = subprocess.run(argv, cwd=product, stdout=subprocess.DEVNULL if name.startswith('parse ') else log, stderr=log).returncode
        log.write(f'STATUS {status}\n\n')
        results.append({'name': name, 'status': status})
(out / 'static-checks.json').write_text(json.dumps(results, indent=2) + '\n')
for result in results:
    print(f"{result['status']} {result['name']}")
sys.exit(1 if any(result['status'] != 0 for result in results) else 0)

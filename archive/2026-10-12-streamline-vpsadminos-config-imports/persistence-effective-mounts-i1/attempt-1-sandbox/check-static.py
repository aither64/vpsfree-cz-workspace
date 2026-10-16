#!/usr/bin/env python3
"""Only prepared formatting, parsing and syntax checks; no evaluation/tests."""
from pathlib import Path
import json
import subprocess
import sys

out = Path(__file__).resolve().parent
session = out.parent
product = session.parents[1] / 'worktrees' / session.name / 'vpsadminos'
owned = [entry['path'] for entry in json.loads((out / 'frozen-sha256.json').read_text())]
nix_paths = [name for name in owned if name.endswith('.nix')]
checks = [('nixfmt', ['/nix/store/ffrsk7yvqqmlj7d40hs2prkqgly2gr2q-nixfmt-1.5.0/bin/nixfmt', '--check', *nix_paths])]
checks += [('parse ' + name, ['nix-instantiate', '--parse', name]) for name in nix_paths]
checks += [('shell syntax', ['bash', '-n', 'tests/nixos-container-persistence-shell.sh']),
           ('helper static syntax', ['bash', '-n', str(out / 'helper-template.sh')]),
           ('suite static Ruby syntax', ['/nix/store/m0nfdb4mhfgwkgss4ymyqmvviwy30i6y-ruby-3.4.9/bin/ruby', '-c', str(out / 'suite-template.rb')]),
           ('whitespace', ['git', 'diff', '--check']),
           ('inverse patch read-only check', ['git', 'apply', '--check', '--whitespace=error-all', str(out / 'inverse.patch')]),
           ('index empty', ['git', 'diff', '--cached', '--quiet']),
           ('latest stable equals 26.05', ['cmp', owned[1], owned[2]])]
results = []
with (out / 'static-checks.log').open('w') as log:
    for name, argv in checks:
        log.write('CHECK ' + name + '\nCOMMAND ' + json.dumps(argv) + '\n'); log.flush()
        result = subprocess.run(argv, cwd=product, stdout=subprocess.DEVNULL if name.startswith('parse ') else log, stderr=log)
        log.write(f'STATUS {result.returncode}\n\n')
        results.append({'name': name, 'argv': argv, 'status': result.returncode})
(out / 'static-checks.json').write_text(json.dumps(results, indent=2) + '\n')
for result in results: print(str(result['status']) + ' ' + result['name'])
sys.exit(1 if any(r['status'] != 0 for r in results) else 0)

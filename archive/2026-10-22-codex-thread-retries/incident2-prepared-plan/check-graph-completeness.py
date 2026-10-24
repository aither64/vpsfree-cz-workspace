#!/usr/bin/env python3
"""Read retained Nix v4 recursive graphs; never realize or alter derivations."""
import json
from pathlib import Path
import sys

rows = []
for argument in sys.argv[1:]:
    path = Path(argument)
    raw = json.loads(path.read_text())
    data = raw.get('derivations', raw)
    names = {name if name.startswith('/nix/store/') else '/nix/store/' + name for name in data}
    missing = set()
    for record in data.values():
        for name in record.get('inputDrvs', {}):
            absolute = name if name.startswith('/nix/store/') else '/nix/store/' + name
            if absolute not in names:
                missing.add(absolute)
    rows.append({'file': str(path), 'derivations': len(data), 'missingInputDerivations': sorted(missing)})
print(json.dumps(rows, indent=2))
assert rows and all(not row['missingInputDerivations'] for row in rows)

import json
import re
import sys
from pathlib import Path

repo, revision = Path(sys.argv[1]), sys.argv[2]
assert re.fullmatch(r'[0-9a-f]{40}', revision)
previous = json.loads((repo / 'captures.json').read_text())['vpsadmin_commit']
assert previous != revision
patterns = {
    'flake.nix': r'(vpsadmin\.url = "github:vpsfreecz/vpsadmin/)' + previous + r'(";)',
    'captures.json': r'("vpsadmin_commit": ")' + previous + r'(")',
    'contract/navigation.yml': r'(vpsadmin_revision: )' + previous + r'(\n)',
    'contract/pages.yml': r'(  vpsadmin: )' + previous + r'(\n)',
}
prepared = {}
for name, pattern in patterns.items():
    path = repo / name
    updated, count = re.subn(pattern, lambda match: match[1] + revision + match[2], path.read_text())
    assert count == 1, (name, count)
    prepared[path] = updated
for path, updated in prepared.items():
    path.write_text(updated)

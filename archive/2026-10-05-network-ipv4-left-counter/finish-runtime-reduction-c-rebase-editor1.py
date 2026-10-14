#!/usr/bin/env python3
"""Drop only the superseded unmerged WebUI pin from this exact two-entry series."""
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
lines = path.read_text().splitlines(keepends=True)
picks = [(index, line.split()[1]) for index, line in enumerate(lines) if line.startswith('pick ')]
assert len(picks) == 2
assert 'cf6203d38a62d589983e00dfd7c3cdaa59fe4c9d'.startswith(picks[0][1])
assert '2271dff38fe1e78806af1c4bb42a264dfa39902f'.startswith(picks[1][1])
index = picks[1][0]
lines[index] = lines[index].replace('pick ', 'drop ', 1)
path.write_text(''.join(lines))
